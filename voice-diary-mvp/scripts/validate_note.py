#!/usr/bin/env python3
"""Check a generated daily note against the controlled tag registry."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

TAG_RE = re.compile(r"(?<![\w])#[\w/-]+", re.UNICODE)
ITEM_RE = re.compile(r"^\s*-\s+.+$")


def load_registry(path: Path) -> tuple[set[str], set[str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    domains = set(data["primary_domains"])
    tags = domains | set(data["facets"])
    for children in data["primary_domains"].values():
        tags.update(children)
    return tags, domains


def validate(note: str, tags: set[str], domains: set[str]) -> list[str]:
    errors: list[str] = []
    item_count = 0
    for line_no, line in enumerate(note.splitlines(), start=1):
        if not ITEM_RE.match(line):
            continue
        item_count += 1
        found = TAG_RE.findall(line)
        unknown = sorted(set(found) - tags)
        if unknown:
            errors.append(f"line {line_no}: unknown tags: {', '.join(unknown)}")
        roots = {tag.split("/", 1)[0] for tag in found if tag not in {"#idea", "#todo", "#milestone", "#review"}}
        if not roots or len(roots) > 2:
            errors.append(f"line {line_no}: expected one primary domain and at most one related domain, found {len(roots)}")
        if len(found) != len(set(found)):
            errors.append(f"line {line_no}: duplicate tags")
        for tag in found:
            if tag in domains and any(other.startswith(tag + "/") for other in found):
                errors.append(f"line {line_no}: parent and child domain tags should not both be present ({tag})")
                break
    if not item_count:
        errors.append("note has no list items")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("note", type=Path, help="Markdown daily note to validate")
    parser.add_argument("--registry", type=Path, default=Path(__file__).parents[1] / "config" / "tags.json")
    args = parser.parse_args()
    tags, domains = load_registry(args.registry)
    errors = validate(args.note.read_text(encoding="utf-8"), tags, domains)
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Valid: {args.note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
