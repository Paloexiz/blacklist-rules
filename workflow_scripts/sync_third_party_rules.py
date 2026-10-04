#!/usr/bin/env python3
"""Sync fixed upstream rules, including complete native Surge rule sets."""

from __future__ import annotations

import argparse
import hashlib
import ipaddress
import json
import re
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from build_rules import BuildError, Rule, render_items, render_json_rules, self_check


ROOT = Path(__file__).resolve().parents[1]
FORMATS = {"clash": ".yaml", "surge": ".list", "sing-box": ".json"}


UPSTREAM_RULES: dict[str, tuple[str, str, str]] = {
    "adrules": ("adrules_Domain", "https://raw.githubusercontent.com/Cats-Team/AdRules/main/adrules_domainset.txt", "Domain"),
    "private_ip": ("private_IP", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/private.yaml", "IP"),
    "private_domain": ("private_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/private.yaml", "Domain"),
    "steam": ("Steam_Domain", "https://raw.githubusercontent.com/peiyingyao/Rule-for-OCD/master/rule/Clash/Steam/Steam_OCD_Domain.txt", "Domain"),
    "copilot_ip": ("Copilot_IP", "https://raw.githubusercontent.com/peiyingyao/Rule-for-OCD/master/rule/Clash/Copilot/Copilot_OCD_IP.txt", "IP"),
    "copilot_domain": ("Copilot_Domain", "https://raw.githubusercontent.com/peiyingyao/Rule-for-OCD/master/rule/Clash/Copilot/Copilot_OCD_Domain.txt", "Domain"),
    "gemini": ("google-gemini_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/google-gemini.yaml", "Domain"),
    "adobeactivation": ("adobe-activation_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/adobe-activation.yaml", "Domain"),
    "googlefcm": ("googlefcm_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/googlefcm.yaml", "Domain"),
    "z-library": ("z-library_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/z-library.yaml", "Domain"),
    "linuxdo": ("linuxdo_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/linuxdo.yaml", "Domain"),
    "twitter_ip": ("twitter_IP", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/twitter.yaml", "IP"),
    "twitter_domain": ("twitter_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/twitter.yaml", "Domain"),
    "github": ("github_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/github.yaml", "Domain"),
    "gitlab": ("gitlab_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/gitlab.yaml", "Domain"),
    "onedrive": ("onedrive_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/onedrive.yaml", "Domain"),
    "microsoft": ("Microsoft_Domain", "https://raw.githubusercontent.com/peiyingyao/Rule-for-OCD/master/rule/Clash/Microsoft/Microsoft_OCD_Domain.txt", "Domain"),
    "openai": ("openai_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/openai.yaml", "Domain"),
    "anthropic": ("anthropic_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/anthropic.yaml", "Domain"),
    "discord": ("discord_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/discord.yaml", "Domain"),
    "aliyun": ("aliyun_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/aliyun.yaml", "Domain"),
    "cloudflare": ("cloudflare_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/cloudflare.yaml", "Domain"),
    "docker": ("docker_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/docker.yaml", "Domain"),
    "homebrew": ("homebrew_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/homebrew.yaml", "Domain"),
    "python": ("python_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/python.yaml", "Domain"),
    "icloud": ("icloud_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/icloud.yaml", "Domain"),
    "apple": ("apple_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/apple.yaml", "Domain"),
    "youtube": ("youtube_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/youtube.yaml", "Domain"),
    "google_ip": ("Google_IP", "https://raw.githubusercontent.com/peiyingyao/Rule-for-OCD/master/rule/Clash/Google/Google_OCD_IP.txt", "IP"),
    "google_domain": ("Google_Domain", "https://raw.githubusercontent.com/peiyingyao/Rule-for-OCD/master/rule/Clash/Google/Google_OCD_Domain.txt", "Domain"),
    "twitch": ("twitch_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/twitch.yaml", "Domain"),
    "niconico": ("niconico_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/niconico.yaml", "Domain"),
    "pixiv": ("Pixiv_Domain", "https://raw.githubusercontent.com/peiyingyao/Rule-for-OCD/master/rule/Clash/Pixiv/Pixiv_OCD_Domain.txt", "Domain"),
    "netflix_ip": ("netflix_IP", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/netflix.yaml", "IP"),
    "netflix_domain": ("netflix_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/netflix.yaml", "Domain"),
    "disney": ("disney_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/disney.yaml", "Domain"),
    "bilibili": ("bilibili_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/bilibili.yaml", "Domain"),
    "spotify": ("spotify_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/spotify.yaml", "Domain"),
    "dmm": ("dmm_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/dmm.yaml", "Domain"),
    "telegram_ip": ("Telegram_IP", "https://raw.githubusercontent.com/peiyingyao/Rule-for-OCD/master/rule/Clash/Telegram/Telegram_OCD_IP.txt", "IP"),
    "telegram_domain": ("Telegram_Domain", "https://raw.githubusercontent.com/peiyingyao/Rule-for-OCD/master/rule/Clash/Telegram/Telegram_OCD_Domain.txt", "Domain"),
    "gfw": ("gfw_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/gfw.yaml", "Domain"),
    "applications": ("applications", "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/applications.txt", "Process"),
    "cn_domain": ("cn_Domain", "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/cn.yaml", "Domain"),
    "lan_classical": ("Lan_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Lan/Lan.list", "Surge"),
    "steam_classical": ("Steam_Classical", "https://raw.githubusercontent.com/peiyingyao/Rule-for-OCD/master/rule/Surge/Steam/Steam.list", "Surge"),
    "adobeactivation_classical": ("adobe-activation_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AdobeActivation/AdobeActivation.list", "Surge"),
    "googlefcm_classical": ("googlefcm_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/GoogleFCM/GoogleFCM.list", "Surge"),
    "twitter_classical": ("twitter_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Twitter/Twitter.list", "Surge"),
    "openai_classical": ("openai_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/OpenAI/OpenAI.list", "Surge"),
    "copilot_classical": ("Copilot_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Copilot/Copilot.list", "Surge"),
    "github_classical": ("github_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/GitHub/GitHub.list", "Surge"),
    "onedrive_classical": ("onedrive_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/OneDrive/OneDrive.list", "Surge"),
    "microsoft_classical": ("Microsoft_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Microsoft/Microsoft.list", "Surge"),
    "icloud_classical": ("icloud_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/iCloud/iCloud.list", "Surge"),
    "apple_classical": ("apple_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Apple/Apple.list", "Surge"),
    "youtube_classical": ("youtube_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/YouTube/YouTube.list", "Surge"),
    "google_classical": ("Google_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Google/Google.list", "Surge"),
    "twitch_classical": ("twitch_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Twitch/Twitch.list", "Surge"),
    "niconico_classical": ("niconico_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Niconico/Niconico.list", "Surge"),
    "netflix_classical": ("netflix_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Netflix/Netflix.list", "Surge"),
    "disney_classical": ("disney_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Disney/Disney.list", "Surge"),
    "bilibili_classical": ("bilibili_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/BiliBili/BiliBili.list", "Surge"),
    "spotify_classical": ("spotify_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Spotify/Spotify.list", "Surge"),
    "dmm_classical": ("dmm_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/DMM/DMM.list", "Surge"),
    "telegram_classical": ("Telegram_Classical", "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Telegram/Telegram.list", "Surge"),
}


def targets() -> dict[str, tuple[str, str, str]]:
    result = dict(UPSTREAM_RULES)
    for index, (name, url, kind) in result.items():
        if not re.fullmatch(r"[A-Za-z0-9_-]+", name):
            raise BuildError(f"Unsafe output name: {index}")
        if kind not in {"Domain", "IP", "Process", "Surge"}:
            raise BuildError(f"Unsupported rule kind: {index}")
        if not url.startswith("https://raw.githubusercontent.com/"):
            raise BuildError(f"Unsupported upstream source: {index}")
    if not result or len({name for name, _, _ in result.values()}) != len(result):
        raise BuildError("Empty or colliding third-party output names")
    return result


def download(url: str) -> str | None:
    request = Request(url, headers={"User-Agent": "blacklist-rules-sync"})
    try:
        with urlopen(request, timeout=30) as response:
            content = response.read(16 * 1024 * 1024 + 1)
    except HTTPError as exc:
        if exc.code in {404, 410}:
            return None
        raise
    if len(content) > 16 * 1024 * 1024:
        raise BuildError(f"Source exceeds 16 MiB: {url}")
    return content.decode("utf-8-sig")


def convert(text: str, kind: str) -> dict[str, bytes]:
    if kind == "Surge":
        # Keep the complete upstream file; mixed Surge rules cannot be reduced to domain sets.
        rules = [line.strip() for line in text.splitlines() if line.strip() and not line.strip().startswith(("#", "//"))]
        allowed = {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD", "IP-CIDR", "IP-CIDR6", "IP-ASN", "USER-AGENT", "PROCESS-NAME", "AND", "OR", "NOT"}
        if not rules:
            raise BuildError("Third-party source is empty")
        for line in rules:
            rule_type, separator, value = line.partition(",")
            if rule_type not in allowed or not separator or not value.strip():
                raise BuildError(f"Unsupported native Surge rule: {line}")
            if rule_type in {"IP-CIDR", "IP-CIDR6"}:
                network = ipaddress.ip_network(value.split(",")[0], strict=False)
                if network.version != (6 if rule_type == "IP-CIDR6" else 4):
                    raise BuildError(f"Wrong native Surge IP family: {line}")
            elif rule_type == "IP-ASN" and not re.fullmatch(r"\d+(?:,no-resolve)?", value):
                raise BuildError(f"Invalid native Surge ASN: {line}")
        return {"surge": text.replace("\r\n", "\n").encode("utf-8")}
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
    previous_sources = None
    urls = [url for _, url, _ in selected.values()]
    # Validate every source and format before changing outputs; licenses remain fixed copies.
    with ThreadPoolExecutor(max_workers=4) as executor:
        downloaded = list(executor.map(fetch, urls))
    for (index, (name, url, kind)), text in zip(selected.items(), downloaded):
        if text is None:
            # The manifest is only a record of the last successful download, never the inventory.
            if previous_sources is None:
                previous_path = root / "third_party/sources.json"
                if not previous_path.is_file():
                    raise BuildError(f"Missing upstream has no successful source record: {index}")
                previous_sources = json.loads(previous_path.read_text(encoding="utf-8"))
            previous = previous_sources.get(index, {})
            expected = {fmt: f"{fmt}/{name}{extension}" for fmt, extension in FORMATS.items() if kind != "Surge" or fmt == "surge"}
            if previous.get("source") != url or previous.get("kind") != kind or previous.get("outputs") != expected or not all((root / "third_party" / path).is_file() for path in expected.values()):
                raise BuildError(f"Missing upstream has no matching published copy: {index}")
            sources[index] = previous
            print(f"[KEEP] {index}: upstream missing; retaining last successful files")
            continue
        owner = url.split("/")[3]
        notice_path = {"MetaCubeX": "licenses/MetaCubeX/LICENSE", "peiyingyao": "licenses/Rule-for-OCD/LICENSE", "Loyalsoldier": "licenses/Loyalsoldier/LICENSE", "Cats-Team": "NOTICE.md", "blackmatrix7": "licenses/blackmatrix7-LICENSE"}[owner]
        converted = convert(text, kind)
        sources[index] = {"source": url, "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(), "kind": kind, "notices": notice_path, "outputs": {fmt: f"{fmt}/{name}{FORMATS[fmt]}" for fmt in converted}}
        for fmt, content in converted.items():
            if fmt != "sing-box":
                action = "Mirrored" if kind == "Surge" else "Converted"
                content = f"# {action} by blacklist-rules; matching rules retain upstream ownership.\n# Source: {url}\n# Notices: third_party/{notice_path}\n".encode("utf-8") + content
            candidates[root / "third_party" / fmt / f"{name}{FORMATS[fmt]}"] = content
    candidates[root / "third_party/sources.json"] = (json.dumps(sources, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    for path, content in candidates.items():
        if path.exists() and path.read_bytes() == content:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        print(f"[OK] {path.relative_to(root)}")
    print(f"Checked {len(selected)} sources; generated {len(candidates) - 1} rule files.")


def self_test() -> None:
    self_check()
    for status in (404, 410):
        with patch(__name__ + ".urlopen", side_effect=HTTPError("https://example.com", status, "Missing", None, None)):
            assert download("https://example.com") is None
    with patch(__name__ + ".urlopen", side_effect=HTTPError("https://example.com", 503, "Unavailable", None, None)):
        try:
            download("https://example.com")
        except HTTPError:
            pass
        else:
            raise AssertionError("Transient upstream error was ignored")
    domain = convert('payload:\n  - "+.example.com"\n  - exact.test\n', "Domain")
    assert json.loads(domain["sing-box"])["rules"][0]["domain"] == ["example.com", "exact.test"]
    assert domain["surge"] == b".example.com\nexact.test\n"
    assert convert("192.0.2.1/24\n2001:db8::/32", "IP")["surge"] == b"IP-CIDR,192.0.2.0/24,no-resolve\nIP-CIDR6,2001:db8::/32,no-resolve\n"
    assert json.loads(convert("payload:\n - PROCESS-NAME,App.exe", "Process")["sing-box"])["rules"] == [{"process_name": ["App.exe"]}]
    classical = "# Upstream notice\nDOMAIN-KEYWORD,example\nIP-CIDR,192.0.2.0/24,no-resolve\nIP-ASN,64500\nUSER-AGENT,Example*\nPROCESS-NAME,App\nOR,((DOMAIN,example.com),(IP-CIDR6,2001:db8::/32))\n"
    assert convert(classical, "Surge") == {"surge": classical.encode("utf-8")}
    for text, kind in [("# empty", "Domain"), ("<html>error</html>", "Domain"), ("example.com", "IP"), ("192.0.2.0/24", "Domain"), ("payload:\nother: value", "Domain"), ("# empty", "Surge"), ("<html>error</html>", "Surge"), ("IP-CIDR,2001:db8::/32", "Surge"), ("IP-ASN,invalid", "Surge")]:
        try:
            convert(text, kind)
        except BuildError:
            continue
        raise AssertionError(f"Invalid {kind} source accepted")
    with patch.object(Path, "read_text", side_effect=AssertionError("Rule inventory must not read client profiles or generated manifests")):
        selected = targets()
    assert selected["steam"][0] == "Steam_Domain" and selected["google_ip"][0] == "Google_IP"
    assert {"openai", "cn_domain", "applications", "adrules"} <= selected.keys()
    assert all("_OCD_" not in name for name, _, _ in selected.values())
    samples = {url: {"Domain": "+.example.com", "IP": "192.0.2.0/24", "Process": "PROCESS-NAME,App.exe", "Surge": classical}[kind] for _, url, kind in selected.values()}
    with tempfile.TemporaryDirectory(prefix="ai-agent-third-party-") as temporary:
        root = Path(temporary)
        license_file = root / "third_party/licenses/AdRules/SCRIPT-LICENSE"
        license_file.parent.mkdir(parents=True)
        license_file.write_bytes(b"Fixed license copy\n")
        sync(root, samples.__getitem__)
        assert license_file.read_bytes() == b"Fixed license copy\n"
        assert {path for path in (root / "third_party/licenses").rglob("*") if path.is_file()} == {license_file}
        before = {path: path.read_bytes() for path in root.rglob("*") if path.is_file()}
        assert len(before) == sum(1 if kind == "Surge" else len(FORMATS) for _, _, kind in selected.values()) + 2

        reduced = "# Upstream notice\nDOMAIN-KEYWORD,example\n"
        sync(root, lambda url: reduced if url == selected["steam_classical"][1] else samples[url])
        mirrored = root / "third_party/surge/Steam_Classical.list"
        assert mirrored.read_text(encoding="utf-8").split("\n", 3)[3] == reduced
        assert b"PROCESS-NAME,App" not in mirrored.read_bytes()
        missing_url = selected["steam_classical"][1]
        retained = mirrored.read_bytes()
        old_source = json.loads((root / "third_party/sources.json").read_text(encoding="utf-8"))["steam_classical"]
        sync(root, lambda url: None if url == missing_url else samples[url].replace("example.com", "updated.test"))
        assert mirrored.read_bytes() == retained
        assert json.loads((root / "third_party/sources.json").read_text(encoding="utf-8"))["steam_classical"] == old_source
        assert b"updated.test" in (root / "third_party/surge/adrules_Domain.list").read_bytes()
        before = {path: path.read_bytes() for path in root.rglob("*") if path.is_file()}
        sync(root, lambda url: None)
        assert before == {path: path.read_bytes() for path in root.rglob("*") if path.is_file()}

        unpublished = root / "ai-agent-unpublished"
        try:
            sync(unpublished, lambda url: None)
        except BuildError:
            pass
        else:
            raise AssertionError("Missing source without a published copy was accepted")
        assert not unpublished.exists()

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
    print("Fixed inventory, conversion, complete Surge mirrors, upstream deletion and missing-source retention passed.")


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
