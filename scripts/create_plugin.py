#!/usr/bin/env python3
"""Explicit creation of new source artifacts; no plugin execution or installation."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from obsidian_plugin_brain.creator import ARCHETYPES, CreatorError, create_project, load_brief


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a local Obsidian Plugin Creator starter")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--brief", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--workspace", type=Path, default=Path.cwd())
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.list:
        print(json.dumps({key: value[0] for key, value in ARCHETYPES.items()}, indent=2))
        return 0
    if not args.brief or not args.out:
        parser.error("--brief and --out are required unless --list is used")
    try:
        receipt = create_project(load_brief(args.brief), args.out, workspace=args.workspace, dry_run=args.dry_run)
        print(json.dumps(receipt, indent=2))
    except (CreatorError, OSError, KeyError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
