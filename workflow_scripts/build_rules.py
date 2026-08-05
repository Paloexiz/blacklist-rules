#!/usr/bin/env python3
"""Build Clash and Surge rule files from neutral .rules sources."""

from __future__ import annotations

import argparse
import json
from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
BUILD_CONFIG_PATH = ROOT / "rule_sources" / "rules.build.json"


class BuildError(RuntimeError):
    """Raised when source files or build config are invalid."""


@dataclass(frozen=True)
class Marker:
    kind: str
    text: str


@dataclass(frozen=True)
class Rule:
    raw: str
    enabled: bool = True
    note: str = ""


Item = Marker | Rule


def load_config(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise BuildError(f"Failed to read build config: {path}") from exc
    except json.JSONDecodeError as exc:
        raise BuildError(f"Build config is not valid JSON: {path}") from exc

    if not isinstance(data, dict) or not isinstance(data.get("outputs"), list):
        raise BuildError("Build config must contain an `outputs` array")
    return data


def split_note(text: str) -> tuple[str, str]:
    if " # " not in text:
        return text.strip(), ""
    raw, note = text.split(" # ", 1)
    return raw.strip(), note.strip()


def parse_source(path: Path) -> list[Item]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise BuildError(f"Failed to read source file: {path}") from exc

    items: list[Item] = []
    for number, line in enumerate(lines, 1):
        text = line.strip()
        if not text:
            continue
        if text.startswith("### "):
            items.append(Marker("group", text[4:].strip()))
            continue
        if text.startswith("## "):
            items.append(Marker("category", text[3:].strip()))
            continue

        enabled = True
        if text.startswith("! "):
            enabled = False
            text = text[2:].strip()

        raw, note = split_note(text)
        if not raw:
            raise BuildError(f"Empty rule in {path} at line {number}")
        items.append(Rule(raw=raw, enabled=enabled, note=note))

    return items


def load_sources(paths: Iterable[str]) -> list[Item]:
    items: list[Item] = []
    for source in paths:
        items.extend(parse_source(ROOT / source))
    return items


def source_sort_key(value: str | None) -> str:
    return "" if value is None else value.casefold()


def merge_sort_categories_groups(items: list[Item]) -> list[Item]:
    categories: "OrderedDict[str | None, OrderedDict[str | None, list[Rule]]]" = OrderedDict()
    current_category: str | None = None
    current_group: str | None = None

    for item in items:
        if isinstance(item, Marker) and item.kind == "category":
            current_category = item.text
            current_group = None
            categories.setdefault(current_category, OrderedDict())
            continue
        if isinstance(item, Marker) and item.kind == "group":
            current_group = item.text
            categories.setdefault(current_category, OrderedDict()).setdefault(current_group, [])
            continue
        if isinstance(item, Rule):
            categories.setdefault(current_category, OrderedDict()).setdefault(current_group, []).append(item)

    merged: list[Item] = []
    for category in sorted(categories, key=source_sort_key):
        if category is not None:
            merged.append(Marker("category", category))
        groups = categories[category]
        if None in groups:
            merged.extend(groups[None])
        for group in sorted((name for name in groups if name is not None), key=source_sort_key):
            merged.append(Marker("group", group))
            merged.extend(groups[group])
    return merged


def to_surge_rule(raw: str) -> str:
    if raw.startswith("+."):
        return raw[1:]
    return raw


def render_items(items: list[Item], fmt: str, include_categories: bool = True) -> list[str]:
    if fmt not in {"clash", "surge"}:
        raise BuildError(f"Unsupported output format: {fmt}")

    lines: list[str] = []
    if fmt == "clash":
        lines.append("payload:")

    for item in items:
        if isinstance(item, Marker):
            if item.kind == "category" and not include_categories:
                continue
            if item.kind == "category":
                comment = f"/*{item.text}*/"
            elif item.kind == "group":
                comment = item.text
            else:
                raise BuildError(f"Unsupported marker kind: {item.kind}")
            lines.append(f"  # {comment}" if fmt == "clash" else f"# {comment}")
            continue

        raw = item.raw if fmt == "clash" else to_surge_rule(item.raw)
        note = f" # {item.note}" if fmt == "clash" and item.note else ""
        if fmt == "clash":
            prefix = "  - " if item.enabled else "  # - "
            lines.append(f"{prefix}{raw}{note}")
        else:
            prefix = "" if item.enabled else "# "
            lines.append(f"{prefix}{raw}")

    return lines


def detect_line_ending(path: Path) -> str:
    if not path.exists():
        return "\n"
    content = path.read_bytes()
    return "\r\n" if b"\r\n" in content else "\n"


def build_output(output: dict[str, Any]) -> tuple[Path, str]:
    path = ROOT / str(output.get("path", ""))
    fmt = str(output.get("format", "")).lower()
    sources = output.get("sources")
    if not path.name or not isinstance(sources, list):
        raise BuildError("Each output must define `path`, `format`, and `sources`")

    items = load_sources(str(source) for source in sources)
    if output.get("merge") == "sort_categories_groups":
        items = merge_sort_categories_groups(items)

    line_ending = detect_line_ending(path)
    include_categories = not bool(output.get("omit_categories", False))
    content = line_ending.join(render_items(items, fmt, include_categories)) + line_ending
    return path, content


def build_targets(check_mode: bool) -> int:
    config = load_config(BUILD_CONFIG_PATH)
    failures = 0

    for output in config["outputs"]:
        if not isinstance(output, dict):
            raise BuildError("Output entries must be objects")
        target_path, content = build_output(output)

        if check_mode:
            try:
                expected = target_path.read_bytes().decode("utf-8")
            except OSError as exc:
                raise BuildError(f"Failed to read target file: {target_path}") from exc
            if expected != content:
                print(f"[DIFF] {target_path.relative_to(ROOT)}")
                failures += 1
            continue

        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(content, encoding="utf-8", newline="")
        print(f"[OK] {target_path.relative_to(ROOT)}")

    return failures


def main() -> None:
    parser = argparse.ArgumentParser(description="Build rule outputs from .rules sources")
    parser.add_argument("--check", action="store_true", help="Check generated files without writing")
    args = parser.parse_args()

    try:
        failures = build_targets(check_mode=args.check)
    except BuildError as exc:
        print(f"[ERROR] {exc}")
        raise SystemExit(1)

    if args.check and failures:
        print(f"Build check failed, mismatch count: {failures}")
        raise SystemExit(1)
    if args.check:
        print("Build check passed.")
    else:
        print("Build completed.")


if __name__ == "__main__":
    main()
