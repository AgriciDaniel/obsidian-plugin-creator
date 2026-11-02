#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
PY = sys.executable
REFERENCE_DATE = "2026-11-01"
sys.path.insert(0, str(REPO))
from obsidian_plugin_brain.public_distribution import excluded_path


def run(args: list[str]) -> None:
    subprocess.run([PY, *args], cwd=REPO, check=True,
                   env={**os.environ, "OBSIDIAN_BRAIN_REFERENCE_DATE": REFERENCE_DATE})


def tree_manifest(root: Path) -> dict[str, str]:
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*"))
            if p.is_file() and p.name != ".manifest-sha256.json" and not excluded_path(p.relative_to(root))}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build and verify the demo at a fixed reference date.")
    parser.add_argument("--check", action="store_true", help="Verify retained hashes without replacing output.")
    parser.add_argument("--update-hashes", action="store_true", help="Explicitly replace expected fixture hashes.")
    args = parser.parse_args(argv)
    demo_parent = REPO / "examples"
    demo = demo_parent / "sample-vault"
    with tempfile.TemporaryDirectory(prefix="obsidian-brain-demo-stage-") as tmp:
        staged = Path(tmp) / "sample-vault"
        run(["scripts/scaffold_vault.py", "--client", "sample-vault", "--client-name", "Sample Client", "--owner", "Daniel Agrici", "--out-dir", tmp])
        run(["scripts/synthesize_brain.py", "--vault", str(staged)])
        run(["scripts/generate_vault_visuals.py", "--vault", str(staged)])
        run(["scripts/render_brain_report.py", "--vault", str(staged), "--html-only"])
        run(["scripts/lint_vault.py", "--vault", str(staged)])
        hashes = tree_manifest(staged)
        serialized = json.dumps(hashes, indent=2, sort_keys=True) + "\n"
        digest = hashlib.sha256(serialized.encode()).hexdigest()
        expected = REPO / "tests/fixtures/sample-vault.sha256"
        if not args.update_hashes and (not expected.exists() or expected.read_text().strip() != digest):
            raise SystemExit("Demo hashes differ; inspect the change, then use --update-hashes explicitly.")
        (staged / ".manifest-sha256.json").write_text(serialized)
        if args.check:
            if tree_manifest(demo) != hashes or not (demo / ".manifest-sha256.json").is_file() or (demo / ".manifest-sha256.json").read_text() != serialized:
                raise SystemExit("Retained demo differs from regeneration")
        else:
            # Keep a recoverable copy before replacing generated output.
            if demo.exists():
                backup = Path(tempfile.mkdtemp(prefix="obsidian-brain-demo-backup-")) / "sample-vault"
                shutil.copytree(demo, backup)
                shutil.rmtree(demo)
            demo_parent.mkdir(parents=True, exist_ok=True)
            for name in hashes:
                target = demo / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(staged / name, target)
            shutil.copy2(staged / ".manifest-sha256.json", demo / ".manifest-sha256.json")
        if args.update_hashes:
            expected.write_text(digest + "\n")
    print(demo)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
