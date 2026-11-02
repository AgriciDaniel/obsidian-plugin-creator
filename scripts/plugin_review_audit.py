#!/usr/bin/env python3
"""Run a read-only static Obsidian plugin readiness and scope audit."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from obsidian_plugin_brain.importers.plugin_repo import ImporterError, import_plugin_repo
from obsidian_plugin_brain.reports.readiness_report import render_readiness_report
from obsidian_plugin_brain.synthesis.review_health import SynthesisError, synthesize_plugin_review


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Statically inspect an Obsidian plugin directory and emit a source-cited readiness audit."
    )
    parser.add_argument("--plugin-dir", required=True, help="Path to the Obsidian plugin repository directory")
    parser.add_argument("--out", default="", help="Optional path to write Markdown report (default: stdout)")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Emit structured JSON payload")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero if any critical blocker is found")
    args = parser.parse_args(argv)

    try:
        imported = import_plugin_repo(Path(args.plugin_dir).expanduser())
        synthesis = synthesize_plugin_review(imported)
    except (ImporterError, SynthesisError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.as_json:
        payload = {"imported": imported, "synthesis": synthesis}
        text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    else:
        text = render_readiness_report(imported, synthesis) + "\n"

    if args.out:
        out_path = Path(args.out).expanduser()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)

    if args.strict and synthesis["counts"]["critical"] > 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
