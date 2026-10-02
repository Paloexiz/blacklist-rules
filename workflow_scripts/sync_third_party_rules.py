#!/usr/bin/env python3
"""Sync every third-party provider used by the Mihomo override in three formats."""

from __future__ import annotations

import argparse
import hashlib
import ipaddress
import json
import re
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen

from build_rules import BuildError, Rule, render_items, render_json_rules, self_check


ROOT = Path(__file__).resolve().parents[1]
PROVIDERS = ROOT / "client_conf/mihomo_override/mihomo_override.js"
FORMATS = {"clash": ".yaml", "surge": ".list", "sing-box": ".json"}


def targets() -> dict[str, tuple[str, str, str]]:
    source = PROVIDERS.read_text(encoding="utf-8")
    match = re.search(r"const ruleProviders\s*=\s*(\{.*?\});", source, re.S)
    if not match:
        raise BuildError("Cannot find ruleProviders in the Mihomo override")
    literal = re.sub(r"^\s*\.\.\.ruleProvider(?:Mrs|Yaml),\s*$", "", match[1], flags=re.M)
    providers = json.loads(literal)
    result = {}
    for index, provider in providers.items():
        url = provider["url"]
        if "/Paloexiz/blacklist-rules@" in url:
            continue
        match = re.fullmatch(r"https://fastly\.jsdelivr\.net/gh/([^/]+/[^@]+)@([^/]+)/(.+)", url)
        if not match:
            raise BuildError(f"Unsupported third-party source: {index}")
        repository, branch, path = match.groups()
        kind = {"domain": "Domain", "ipcidr": "IP", "classical": "Process"}.get(provider["behavior"])
        if kind is None:
            raise BuildError(f"Unsupported provider behavior: {index}")
        stem = Path(path).stem
        if repository == "peiyingyao/Rule-for-OCD":
            name = stem.replace("_OCD_", "_")
            path = str(Path(path).with_suffix(".txt")).replace("\\", "/")
        elif repository == "MetaCubeX/meta-rules-dat":
            name = f"{stem}_{kind}"
            path = str(Path(path).with_suffix(".yaml")).replace("\\", "/")
        elif repository == "Cats-Team/AdRules" and index == "adrules":
            name, path = "adrules_Domain", "adrules_domainset.txt"
        elif repository == "Loyalsoldier/clash-rules" and index == "applications":
            name = "applications"
        else:
            raise BuildError(f"Unsupported third-party repository: {index}")
        if not re.fullmatch(r"[A-Za-z0-9_-]+", name):
            raise BuildError(f"Unsafe output name: {index}")
        result[index] = (name, f"https://raw.githubusercontent.com/{repository}/{branch}/{path}", kind)
    if not result or len({name for name, _, _ in result.values()}) != len(result):
        raise BuildError("Empty or colliding third-party output names")
    return result


def download(url: str) -> str:
    request = Request(url, headers={"User-Agent": "blacklist-rules-sync"})
    with urlopen(request, timeout=30) as response:
        content = response.read(16 * 1024 * 1024 + 1)
    if len(content) > 16 * 1024 * 1024:
        raise BuildError(f"Source exceeds 16 MiB: {url}")
    return content.decode("utf-8-sig")


def convert(text: str, kind: str) -> dict[str, bytes]:
    items = []
    payload = False
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith(("#", "//")):
            continue
        if line == "payload:" and not items and not payload:
            payload = True
            continue
        if payload:
            if not line.startswith("- "):
                raise BuildError("Unsupported YAML payload")
            line = line[2:].strip()
            if line.startswith('"'):
                line = json.loads(line)
            elif line.startswith("'") and line.endswith("'"):
                line = line[1:-1].replace("''", "'")
        items.append(Rule(line))
    if not items:
        raise BuildError("Third-party source is empty")
    content = render_json_rules(items)
    fields = {field for rule in json.loads(content)["rules"] for field in rule}
    allowed = {"Domain": {"domain", "domain_suffix", "domain_regex"}, "IP": {"ip_cidr"}, "Process": {"process_name"}}[kind]
    if not fields or not fields <= allowed:
        raise BuildError(f"Source does not contain only {kind} rules")
    if kind == "IP":
        surge = []
        for item in items:
            network = ipaddress.ip_network(item.raw, strict=False)
            surge.append(f"IP-CIDR{'6' if network.version == 6 else ''},{network},no-resolve")
    else:
        surge = render_items(items, "surge")
    return {
        "clash": ("\n".join(render_items(items, "clash")) + "\n").encode("utf-8"),
        "surge": ("\n".join(surge) + "\n").encode("utf-8"),
        "sing-box": (content + "\n").encode("utf-8"),
    }


def sync(root: Path, fetch=download) -> None:
    selected = targets()
    candidates: dict[Path, bytes] = {}
    sources = {}
    urls = [url for _, url, _ in selected.values()]
    # Validate every source and format before changing outputs; licenses remain fixed copies.
    with ThreadPoolExecutor(max_workers=4) as executor:
        downloaded = list(executor.map(fetch, urls))
    for (index, (name, url, kind)), text in zip(selected.items(), downloaded):
        owner = url.split("/")[3]
        notice_path = {"MetaCubeX": "licenses/MetaCubeX/LICENSE", "peiyingyao": "licenses/Rule-for-OCD/LICENSE", "Loyalsoldier": "licenses/Loyalsoldier/LICENSE", "Cats-Team": "NOTICE.md"}[owner]
        sources[index] = {"source": url, "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(), "kind": kind, "notices": notice_path, "outputs": {fmt: f"{fmt}/{name}{extension}" for fmt, extension in FORMATS.items()}}
        for fmt, content in convert(text, kind).items():
            if fmt != "sing-box":
                content = f"# Converted by blacklist-rules; matching rules retain upstream ownership.\n# Source: {url}\n# Notices: third_party/{notice_path}\n".encode("utf-8") + content
            candidates[root / "third_party" / fmt / f"{name}{FORMATS[fmt]}"] = content
    candidates[root / "third_party/sources.json"] = (json.dumps(sources, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    for path, content in candidates.items():
        if path.exists() and path.read_bytes() == content:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        print(f"[OK] {path.relative_to(root)}")
    print(f"Synchronized {len(selected)} providers in {len(FORMATS)} formats.")


def self_test() -> None:
    self_check()
    domain = convert('payload:\n  - "+.example.com"\n  - exact.test\n', "Domain")
    assert json.loads(domain["sing-box"])["rules"][0]["domain"] == ["example.com", "exact.test"]
    assert domain["surge"] == b".example.com\nexact.test\n"
    assert convert("192.0.2.1/24\n2001:db8::/32", "IP")["surge"] == b"IP-CIDR,192.0.2.0/24,no-resolve\nIP-CIDR6,2001:db8::/32,no-resolve\n"
    assert json.loads(convert("payload:\n - PROCESS-NAME,App.exe", "Process")["sing-box"])["rules"] == [{"process_name": ["App.exe"]}]
    for text, kind in [("# empty", "Domain"), ("<html>error</html>", "Domain"), ("example.com", "IP"), ("192.0.2.0/24", "Domain"), ("payload:\nother: value", "Domain")]:
        try:
            convert(text, kind)
        except BuildError:
            continue
        raise AssertionError(f"Invalid {kind} source accepted")
    selected = targets()
    assert selected["steam"][0] == "Steam_Domain" and selected["google_ip"][0] == "Google_IP"
    assert {"openai", "cn_domain", "applications", "adrules"} <= selected.keys()
    assert all("_OCD_" not in name for name, _, _ in selected.values())
    samples = {url: {"Domain": "+.example.com", "IP": "192.0.2.0/24", "Process": "PROCESS-NAME,App.exe"}[kind] for _, url, kind in selected.values()}
    with tempfile.TemporaryDirectory(prefix="ai-agent-third-party-") as temporary:
        root = Path(temporary)
        license_file = root / "third_party/licenses/AdRules/SCRIPT-LICENSE"
        license_file.parent.mkdir(parents=True)
        license_file.write_bytes(b"Fixed license copy\n")
        sync(root, samples.__getitem__)
        assert license_file.read_bytes() == b"Fixed license copy\n"
        assert {path for path in (root / "third_party/licenses").rglob("*") if path.is_file()} == {license_file}
        before = {path: path.read_bytes() for path in root.rglob("*") if path.is_file()}
        assert len(before) == len(selected) * len(FORMATS) + 2

        def fail_one(url: str) -> str:
            if url == selected["openai"][1]:
                raise OSError("Simulated download failure")
            return samples[url].replace("example.com", "changed.test")

        try:
            sync(root, fail_one)
        except OSError:
            pass
        else:
            raise AssertionError("Download failure was ignored")
        assert before == {path: path.read_bytes() for path in root.rglob("*") if path.is_file()}
    print("Three-format conversion, provider coverage, fixed licenses and failure retention passed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        self_test() if args.self_test else sync(ROOT)
    except (OSError, UnicodeError, ValueError, BuildError) as exc:
        parser.exit(1, f"[ERROR] {exc}\n")


if __name__ == "__main__":
    main()
