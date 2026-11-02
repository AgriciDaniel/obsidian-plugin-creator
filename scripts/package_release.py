#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
from obsidian_plugin_brain.public_distribution import excluded_path, assert_public_tree, validate_public_edition

TEXT_SUFFIXES = {".base", ".canvas", ".css", ".csv", ".html", ".json", ".md", ".py", ".sh", ".svg", ".toml", ".txt", ".yaml", ".yml", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".svelte", ".vue"}
SKIP_PARTS = {".git", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv", "__pycache__", "build", "dist", "venv", "node_modules", "created-projects"}
SKIP_SUFFIXES = {".pyc", ".pyo", ".log"}
FORBIDDEN_ENTRY_NAMES = {".env", ".env.local", ".env.production", ".DS_Store", "Thumbs.db", "workspace.json"}
MAX_SCAN_BYTES = 25 * 1024 * 1024
FORBIDDEN_TEXT_PATTERNS = {
    "local home path": re.compile(rb"/home/(?!\.\.\.)[A-Za-z0-9_.-]+"),
    "local macOS home path": re.compile(rb"/Users/(?!\.\.\.|Shared\b)[A-Za-z0-9_.-]+"),
    "local Windows home path": re.compile(rb"[A-Za-z]:\\\\?Users\\\\?(?!\.\.\.|Public\b)[A-Za-z0-9_.-]+"),
    "private key": re.compile(rb"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "openai api key": re.compile(rb"sk-[A-Za-z0-9_-]{20,}"),
    "anthropic api key": re.compile(rb"sk-ant-[A-Za-z0-9_-]{20,}"),
    "github token": re.compile(rb"(gh[pousr]|github_pat)_[A-Za-z0-9_]{20,}"),
    "aws key": re.compile(rb"AKIA[0-9A-Z]{16}"),
    "google api key": re.compile(rb"AIza[0-9A-Za-z_-]{20,}"),
    "bearer literal": re.compile(rb"Bearer\s+[A-Za-z0-9._-]{24,}"),
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build verified release ZIP artifacts.")
    parser.add_argument("--version", required=True)
    parser.add_argument("--dist-dir", default="dist")
    parser.add_argument("--release-type", default="scaffold", choices=["scaffold", "demo", "market-ready"])
    args = parser.parse_args(argv)
    version = normalize_version(args.version)
    dist = (REPO / args.dist_dir).resolve()
    if dist == REPO or not dist.is_relative_to(REPO):
        raise SystemExit(f"ERROR: --dist-dir must be a folder inside the repo: {dist}")
    dist.mkdir(parents=True, exist_ok=True)
    if args.release_type == "market-ready":
        enforce_market_ready_gate()
    scan_source_tree()
    artifacts = [
        build_zip(dist / f"obsidian-plugin-brain-template-v{version}.zip", REPO / "assets" / "template-brain", "obsidian-plugin-brain-template"),
        build_zip(dist / f"obsidian-plugin-brain-sample-vault-v{version}.zip", REPO / "examples" / "sample-vault", "obsidian-plugin-brain-sample-vault"),
        build_source_zip(dist / f"obsidian-plugin-brain-source-v{version}.zip", version),
        build_starters_zip(dist / f"obsidian-plugin-creator-starters-v{version}.zip"),
    ]
    for artifact in artifacts:
        validate_zip(artifact["path"])
    manifest = {
        "product": "obsidian-plugin-brain",
        "version": version,
        "release_type": args.release_type,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "git_commit": git_commit(),
        "artifacts": [{"file": a["path"].name, "sha256": sha256_file(a["path"]), "bytes": a["path"].stat().st_size, "entries": a["entries"]} for a in artifacts],
        "checks": ["repo source scan passed", "zip entry scan passed", "zip content secret scan passed", "zip content local-path scan passed"],
    }
    manifest_path = dist / "RELEASE_MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sums = dist / "SHA256SUMS"
    write_sha256s(sums, [*(a["path"] for a in artifacts), manifest_path])
    validate_sha256s(sums)
    print(f"Release package built in {dist}")
    return 0


def enforce_market_ready_gate() -> None:
    audit = REPO / "scripts" / "audit_brain.py"
    if not audit.exists():
        raise SystemExit("ERROR: market-ready release blocked: missing scripts/audit_brain.py")
    proc = subprocess.run(
        [sys.executable, str(audit), "--require", "market-ready", "--json"],
        cwd=REPO,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode:
        detail = "\n".join(part for part in [proc.stdout.strip(), proc.stderr.strip()] if part)
        raise SystemExit("ERROR: market-ready release blocked by audit:\n" + detail)


def normalize_version(value: str) -> str:
    version = value.strip().removeprefix("v")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise SystemExit("ERROR: --version must look like 0.1.0")
    return version


def should_skip(path: Path) -> bool:
    if excluded_path(path):
        return True
    if set(path.parts) & SKIP_PARTS:
        return True
    if any(part.endswith(".egg-info") for part in path.parts):
        return True
    return path.suffix in SKIP_SUFFIXES


def is_generated_project(path: Path) -> bool:
    for parent in path.parents:
        if parent == REPO:
            break
        if (parent / "CREATOR_RECEIPT.json").is_file():
            return True
    return False


def reject_forbidden_entry(path: Path) -> None:
    if path.name in FORBIDDEN_ENTRY_NAMES:
        raise SystemExit(f"ERROR: forbidden release entry: {path.as_posix()}")
    if path.is_absolute() or ".." in path.parts:
        raise SystemExit(f"ERROR: unsafe release entry: {path.as_posix()}")


def iter_tree(root: Path) -> list[Path]:
    files: list[Path] = []
    for dirname, dirs, names in os.walk(root, followlinks=False):
        current = Path(dirname)
        if (current / "CREATOR_RECEIPT.json").is_file():
            dirs[:] = []
            continue
        kept = []
        for name in sorted(dirs):
            path = current / name
            if should_skip(path.relative_to(root)) or (path / "CREATOR_RECEIPT.json").is_file():
                continue
            if path.is_symlink():
                raise SystemExit(f"ERROR: symlink not allowed: {path.relative_to(root).as_posix()}")
            kept.append(name)
        dirs[:] = kept
        for name in sorted(names):
            path = current / name
            rel = path.relative_to(root)
            if should_skip(rel):
                continue
            reject_forbidden_entry(rel)
            if path.is_symlink():
                raise SystemExit(f"ERROR: symlink not allowed: {rel.as_posix()}")
            if path.is_file():
                files.append(path)
    return sorted(files)


def source_files() -> list[Path]:
    if (REPO / ".git").exists():
        reject_dirty_tracked_files()
        reject_untracked_files()
        proc = subprocess.run(["git", "ls-files", "-z", "--cached"], cwd=REPO, capture_output=True, check=False)
        if proc.returncode != 0:
            raise SystemExit(proc.stderr.decode("utf-8", "replace"))
        files = []
        for raw in proc.stdout.split(b"\0"):
            if raw:
                rel = Path(raw.decode("utf-8", "replace"))
                if should_skip(rel):
                    continue
                reject_forbidden_entry(rel)
                path = REPO / rel
                if is_generated_project(path):
                    continue
                if path.is_symlink():
                    raise SystemExit(f"ERROR: symlink not allowed: {rel.as_posix()}")
                if path.is_file():
                    files.append(path)
        return sorted(files)
    return iter_tree(REPO)


def reject_dirty_tracked_files() -> None:
    dirty: set[str] = set()
    for args in (["git", "diff", "--name-only", "-z"], ["git", "diff", "--name-only", "-z", "--cached"]):
        proc = subprocess.run(args, cwd=REPO, capture_output=True, check=False)
        if proc.returncode != 0:
            raise SystemExit(proc.stderr.decode("utf-8", "replace"))
        dirty.update(raw.decode("utf-8", "replace") for raw in proc.stdout.split(b"\0") if raw)
    blocked = sorted(path for path in dirty if not should_skip(Path(path)) and not is_generated_project(REPO / path))
    if blocked:
        raise SystemExit("ERROR: dirty tracked files would make release non-reproducible: " + ", ".join(blocked[:10]))


def reject_untracked_files() -> None:
    proc = subprocess.run(["git", "ls-files", "-z", "--others", "--exclude-standard"], cwd=REPO, capture_output=True, check=False)
    if proc.returncode != 0:
        raise SystemExit(proc.stderr.decode("utf-8", "replace"))
    untracked = sorted(raw.decode("utf-8", "replace") for raw in proc.stdout.split(b"\0") if raw)
    allowed = [p for p in untracked if not should_skip(Path(p)) and not is_generated_project(REPO / p)]
    if allowed:
        raise SystemExit("ERROR: untracked files would make release non-reproducible: " + ", ".join(allowed[:10]))


def scan_source_tree() -> None:
    try:
        assert_public_tree(REPO)
        validate_public_edition(REPO)
    except ValueError as exc:
        raise SystemExit(str(exc))
    for path in source_files():
        rel = path.relative_to(REPO)
        if not should_skip(rel):
            scan_file(path, rel.as_posix())


def build_zip(out: Path, source: Path, root_name: str) -> dict[str, object]:
    entries = 0
    # List first and skip the output folder, or the zip could pack itself.
    files = [path for path in iter_tree(source) if not path.resolve().is_relative_to(out.parent.resolve())]
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            zf.write(path, (Path(root_name) / path.relative_to(source)).as_posix())
            entries += 1
    return {"path": out, "entries": entries}


def build_source_zip(out: Path, version: str) -> dict[str, object]:
    entries = 0
    files = [path for path in source_files() if not path.resolve().is_relative_to(out.parent.resolve())]
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            rel = path.relative_to(REPO)
            if not should_skip(rel):
                zf.write(path, (Path(f"obsidian-plugin-brain-v{version}") / rel).as_posix())
                entries += 1
    return {"path": out, "entries": entries}


def build_starters_zip(out: Path) -> dict[str, object]:
    # Only our curated templates are rendered here. User-generated projects stay excluded.
    from obsidian_plugin_brain.creator import ARCHETYPES, render_project
    brief = json.loads((REPO / "references/creator/example-brief.json").read_text())
    entries = 0
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for archetype in ARCHETYPES:
            example = {**brief, "id": "creator-" + archetype, "name": "Creator " + archetype.replace("-", " "),
                       "purpose": f"Reference {archetype} starter for local Obsidian plugin development.",
                       "archetype": archetype, "acceptance_criteria": ["Replace the reference example with the product-specific acceptance criteria before claiming feature completion."]}
            files = render_project(example)
            receipt = {"evidence_class": "curated-example-source-only", "runtime": "unverified",
                       "files": {name: hashlib.sha256(body.encode()).hexdigest() for name, body in files.items()}}
            files["CREATOR_RECEIPT.json"] = json.dumps(receipt, indent=2) + "\n"
            for name, body in sorted(files.items()):
                archive.writestr(f"obsidian-plugin-creator-starters/{archetype}/{name}", body.encode())
                entries += 1
    return {"path": out, "entries": entries}


def validate_zip(path: Path) -> None:
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        if not names:
            raise SystemExit(f"ERROR: empty artifact: {path.name}")
        for name in names:
            rel = Path(name)
            for part in rel.parts:
                reject_forbidden_entry(Path(part))
            if should_skip(rel) or any(part in SKIP_PARTS for part in rel.parts):
                raise SystemExit(f"ERROR: forbidden zip entry in {path.name}: {name}")
            mode = zf.getinfo(name).external_attr >> 16
            if stat.S_ISLNK(mode):
                raise SystemExit(f"ERROR: symlink entry in {path.name}: {name}")
            scan_bytes(zf.read(name), f"{path.name}:{name}", rel.suffix)


def scan_file(path: Path, label: str) -> None:
    size = path.stat().st_size
    if size > MAX_SCAN_BYTES:
        raise SystemExit(f"ERROR: file too large for release scan: {label}")
    scan_bytes(path.read_bytes(), label, path.suffix)


def scan_bytes(data: bytes, label: str, suffix: str) -> None:
    if suffix and suffix not in TEXT_SUFFIXES:
        return
    for name, pattern in FORBIDDEN_TEXT_PATTERNS.items():
        if pattern.search(data):
            raise SystemExit(f"ERROR: {name} found in {label}")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_sha256s(path: Path, artifacts: list[Path]) -> None:
    path.write_text("\n".join(f"{sha256_file(a)}  {a.name}" for a in artifacts) + "\n", encoding="utf-8")


def validate_sha256s(path: Path) -> None:
    for line in path.read_text(encoding="utf-8").splitlines():
        expected, filename = line.split("  ", 1)
        actual = sha256_file(path.parent / filename)
        if expected != actual:
            raise SystemExit(f"ERROR: checksum mismatch for {filename}")


def git_commit() -> str | None:
    if not (REPO / ".git").exists():
        return None
    proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True, text=True, check=False)
    return proc.stdout.strip() if proc.returncode == 0 else None


if __name__ == "__main__":
    raise SystemExit(main())
