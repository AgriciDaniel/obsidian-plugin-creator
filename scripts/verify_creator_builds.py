#!/usr/bin/env python3
"""Build trusted generated starters using an explicitly supplied local toolchain.

No dependency installation, Obsidian execution, or active-vault mutation occurs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
from obsidian_plugin_brain.creator import ARCHETYPES, create_project


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--node-modules", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    dependencies = args.node_modules.resolve(strict=True)
    node = shutil.which("node")
    if not node:
        raise SystemExit("Node.js is required; no installation is performed")
    brief = json.loads((REPO / "references/creator/example-brief.json").read_text())
    packages = json.loads((REPO / "references/creator/toolchain/package.json").read_text())["devDependencies"]
    for name, version in packages.items():
        actual = json.loads((dependencies / name / "package.json").read_text())["version"]
        if actual != version:
            raise SystemExit(f"Wrong toolchain version for {name}: expected {version}, got {actual}")
    results = []
    with tempfile.TemporaryDirectory(prefix="creator-build-check-") as root:
        workspace = Path(root)
        for archetype in ARCHETYPES:
            project = workspace / archetype
            spec = {**brief, "id": "creator-" + archetype, "name": "Creator " + archetype.replace("-", " "), "archetype": archetype}
            receipt = create_project(spec, project, workspace=workspace)
            (project / "node_modules").symlink_to(dependencies, target_is_directory=True)
            commands = [
                ("typescript", [node, str(dependencies / "typescript/bin/tsc"), "--noEmit"]),
                ("bundle", [node, "esbuild.config.mjs"]),
                ("official_lint", [node, str(dependencies / "eslint/bin/eslint.js"), "src", "--format", "json"]),
            ]
            runs = []
            for label, command in commands:
                proc = subprocess.run(command, cwd=project, text=True, capture_output=True, timeout=120)
                stdout = proc.stdout.replace(str(project), "<project>").replace(str(dependencies), "<toolchain>")
                stderr = proc.stderr.replace(str(project), "<project>").replace(str(dependencies), "<toolchain>")
                runs.append(dict(check=label, exit_code=proc.returncode, stdout=stdout, stderr=stderr))
            bundled = project / "main.js"
            result = dict(archetype=archetype, checks=runs, evidence_class="generated-source-build-and-official-lint",
                          source_sha256=receipt["files"]["src/main.ts"],
                          styles_sha256=receipt["files"]["styles.css"],
                          generation_receipt_sha256=hashlib.sha256(json.dumps(receipt, sort_keys=True).encode()).hexdigest(),
                          runtime="unverified", physical_devices="unverified",
                          bundle_sha256=hashlib.sha256(bundled.read_bytes()).hexdigest() if bundled.exists() else None,
                          bundle_bytes=bundled.stat().st_size if bundled.exists() else None)
            results.append(result)
            passed = all(r["exit_code"] == 0 for r in runs)
            print(archetype + ": " + ("PASS" if passed else "FAIL"), flush=True)
            if not passed:
                for run in runs:
                    if run["exit_code"]:
                        print(run["check"], run["stdout"], run["stderr"], flush=True)
    payload = dict(schema="obsidian-plugin-creator.build-evidence.v1", date=datetime.now(timezone.utc).date().isoformat(),
                   node=subprocess.check_output([node, "--version"], text=True).strip(),
                   dependency_lock_sha256=hashlib.sha256((REPO / "references/creator/toolchain/package-lock.json").read_bytes()).hexdigest(),
                   dependency_versions=packages, toolchain_install="External prerequisite; this verifier performs no network or install.",
                   outcomes=results)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, indent=2) + "\n")
    return 0 if all(c["exit_code"] == 0 for r in results for c in r["checks"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
