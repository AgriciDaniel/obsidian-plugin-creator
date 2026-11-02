#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Print the next operator action from home.md.")
    parser.add_argument("--vault", required=True)
    args = parser.parse_args(argv)
    vault = Path(args.vault).expanduser().resolve()
    if not (vault / "CODEX.md").exists():
        print(f"ERROR: not a brain vault: {vault}", file=sys.stderr)
        return 2
    hot = vault / "wiki" / "home.md"
    text = hot.read_text(encoding="utf-8") if hot.exists() else ""
    match = re.search(r"## Next Action\s+(.+?)(?:\n## |\Z)", text, re.S)
    print(match.group(1).strip() if match else "Read vault-root-relative CODEX.md, wiki/home.md, and wiki/index.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
