"""Public source distribution boundaries and new-vault runtime initialization."""
from __future__ import annotations

import hashlib
import json
import os
import shutil
from urllib.parse import urlparse
from pathlib import Path

PRIVATE_PARTS = {".raw", ".obsidian"}
PRIVATE_NAMES = {"hot.md", "log.md", "source-ledger.json", "claim-ledger.md"}
SKIP_PARTS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build", "created-projects", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
DEFAULT_FILES = {"app.json", "appearance.json", "core-plugins.json", "graph.json", "bookmarks.json", "templates.json", "snippets/brain.css"}


def excluded_path(path: Path) -> bool:
    return (bool(set(path.parts) & PRIVATE_PARTS) or path.name in PRIVATE_NAMES
            or any(path.parts[i:i + 2] == ("references", "research") for i in range(len(path.parts) - 1))
            or path.name.startswith(".env") and path.name != ".env.example")


def assert_public_tree(root: Path) -> None:
    for dirname, dirs, files in os.walk(root, followlinks=False):
        current = Path(dirname)
        if (current / "CREATOR_RECEIPT.json").is_file():
            dirs[:] = []
            continue
        kept = []
        for name in dirs:
            path = current / name
            rel = path.relative_to(root)
            if name in SKIP_PARTS or name.endswith(".egg-info"):
                continue
            if path.is_symlink():
                raise ValueError("Public distribution contains a symlink: " + rel.as_posix())
            if excluded_path(rel):
                raise ValueError("Private path in public source tree: " + rel.as_posix())
            kept.append(name)
        dirs[:] = kept
        for name in files:
            path = current / name
            rel = path.relative_to(root)
            if path.is_symlink() or excluded_path(rel) or name.startswith(".env") and name != ".env.example":
                raise ValueError("Private or unsafe path in public source tree: " + rel.as_posix())


def validate_public_vault(vault: Path) -> dict:
    marker = json.loads((vault / "PUBLIC_VAULT.json").read_text())
    if not isinstance(marker, dict):
        raise ValueError("Public vault marker must be an object")
    if marker.get("schema") != "obsidian-plugin-public-vault.v1" or marker.get("catalog") != "references/public-sources.json":
        raise ValueError("Invalid public vault marker")
    catalog = vault / "references/public-sources.json"
    data = catalog.read_bytes()
    if hashlib.sha256(data).hexdigest() != marker.get("catalog_sha256"):
        raise ValueError("Public source catalog hash mismatch")
    parsed = json.loads(data)
    if not isinstance(parsed, dict):
        raise ValueError("Public source catalog must be an object")
    if set(parsed) - {"version", "status", "domain", "retrieved", "refresh_cadence", "evidence_boundary", "sources"}:
        raise ValueError("Unreviewed public catalog field")
    sources = parsed.get("sources")
    if not isinstance(sources, list) or not sources:
        raise ValueError("Public source catalog is empty")
    ids = [s.get("id") for s in sources if isinstance(s, dict)]
    if len(ids) != len(sources) or any(not isinstance(s, str) or not s for s in ids) or len(set(ids)) != len(ids):
        raise ValueError("Public source IDs are invalid or duplicated")
    allowed = {"id", "title", "url", "source_type", "retrieved", "refresh_due", "confidence", "canon_targets", "claims", "structured_claims", "supports_claims", "distribution", "upstream_reference"}
    for source in sources:
        if set(source) - allowed:
            raise ValueError("Unreviewed field in public source catalog")
        url = urlparse(str(source.get("url", "")))
        if url.scheme != "https" or not url.hostname or url.username or url.password:
            raise ValueError("Unsafe public source URL")
        claims = source.get("claims")
        if not isinstance(claims, list) or not claims or any(not isinstance(c, str) or not c.strip() or len(c) > 2000 for c in claims):
            raise ValueError("Public source claims need reviewed concise paraphrases")
        structured = source.get("structured_claims", [])
        if not isinstance(structured, list):
            raise ValueError("Structured claims must be a list")
        for claim in structured:
            if not isinstance(claim, dict) or set(claim) - {"claim", "confidence", "source_relationship"}:
                raise ValueError("Unreviewed structured claim field")
            if claim.get("claim") not in claims:
                raise ValueError("Structured claim is not bound to a public paraphrase")
        upstream = source.get("upstream_reference", {})
        if not isinstance(upstream, dict) or set(upstream) - {"commit", "path", "sha256", "sections_or_symbols"}:
            raise ValueError("Unreviewed upstream reference field")
        path = upstream.get("path", "")
        if path and (str(path).startswith("/") or ".raw" in Path(str(path)).parts):
            raise ValueError("Private path in upstream reference")
    return parsed


def initialize_runtime(vault: Path, defaults: Path) -> None:
    """Create private intake and configuration only inside a newly scaffolded vault."""
    catalog = validate_public_vault(vault)
    if (vault / ".raw").exists() or (vault / ".obsidian").exists():
        raise ValueError("Runtime initialization requires a new vault without private state")
    configured = []
    for path in sorted(defaults.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(defaults).as_posix()
        if rel not in DEFAULT_FILES or path.is_symlink():
            raise ValueError("Unreviewed vault default: " + rel)
        configured.append((path, rel))
    if {rel for _, rel in configured} != DEFAULT_FILES:
        raise ValueError("Reviewed vault defaults are incomplete")
    data = (vault / "references/public-sources.json").read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    raw = vault / ".raw" / "sources"
    raw.mkdir(parents=True, mode=0o700)
    rel = ".raw/sources/public-catalog-" + digest[:12] + ".json"
    with (vault / rel).open("xb") as output:
        output.write(data)
    (vault / rel).chmod(0o600)
    manifest = {"brain_schema": "obsidian-plugin-brain.v1", "sources": [{"path": rel, "sha256": digest, "retrieved": catalog["retrieved"], "source_type": "public-source-catalog", "note": "Published editorial reference snapshot; not a private capture or full upstream page body."}]}
    (vault / ".raw/.manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    for source, rel in configured:
        target = vault / ".obsidian" / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)


def validate_public_edition(root: Path, *, include_sample: bool = True) -> dict:
    """Bind the product's root catalog to the reviewed copies used by its vaults."""
    edition = json.loads((root / "PUBLIC_EDITION.json").read_text())
    if not isinstance(edition, dict):
        raise ValueError("Public edition marker must be an object")
    if edition.get("schema") != "obsidian-plugin-public-edition.v1" or edition.get("source_catalog") != "references/public-sources.json":
        raise ValueError("Invalid public edition marker")
    data = (root / "references/public-sources.json").read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != edition.get("catalog_sha256"):
        raise ValueError("Root public source catalog hash mismatch")
    folders = ["assets/template-brain"] + (["examples/sample-vault"] if include_sample else [])
    catalog = None
    for folder in folders:
        vault = root / folder
        catalog = validate_public_vault(vault)
        if hashlib.sha256((vault / "references/public-sources.json").read_bytes()).hexdigest() != digest:
            raise ValueError("Root and vault public catalogs differ")
    if len(catalog["sources"]) != edition.get("source_count") or sum(len(s["claims"]) for s in catalog["sources"]) != edition.get("claim_count"):
        raise ValueError("Public catalog counts differ from the edition marker")
    return catalog
