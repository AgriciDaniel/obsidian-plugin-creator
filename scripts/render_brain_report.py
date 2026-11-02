#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path


LOCAL_PATH = re.compile(r"(?:/home/|/Users/|[A-Za-z]:\\Users\\)[A-Za-z0-9_.-]+")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render the weekly report as HTML.")
    parser.add_argument("--vault", required=True)
    parser.add_argument("--out", default="")
    parser.add_argument("--html-only", action="store_true")
    args = parser.parse_args(argv)
    vault = Path(args.vault).expanduser().resolve()
    report = vault / "wiki" / "reports" / "Weekly Report.md"
    if not report.exists():
        print("ERROR: report not found; run synthesize first", file=sys.stderr)
        return 2
    out = Path(args.out).expanduser().resolve() if args.out else vault / "weekly-report.html"
    text = report.read_text(encoding="utf-8")
    if text.startswith("---\n") and "\n---" in text[4:]:
        text = text[4:].split("\n---", 1)[1].lstrip("-\n")  # frontmatter is metadata, not report content
    html_text = markdown_to_html(text)
    html_text = LOCAL_PATH.sub("[local-path-redacted]", html_text)
    out.write_text(html_text, encoding="utf-8")
    print(out)
    return 0


def markdown_to_html(text: str) -> str:
    body = []
    for line in text.splitlines():
        if line.startswith("---"):
            continue
        if line.startswith("# "):
            body.append(f"<h1>{html.escape(line[2:])}</h1>")
        elif line.startswith("## "):
            body.append(f"<h2>{html.escape(line[3:])}</h2>")
        elif line.startswith("- "):
            body.append(f"<li>{html.escape(line[2:])}</li>")
        elif line.strip():
            body.append(f"<p>{html.escape(line)}</p>")
    return "<!doctype html><meta charset='utf-8'><title>Weekly Report</title><body>" + "\n".join(body) + "</body>\n"


if __name__ == "__main__":
    raise SystemExit(main())
