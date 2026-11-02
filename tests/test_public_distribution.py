#!/usr/bin/env python3
"""Public distribution and local private-state boundaries, including negative controls."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
from obsidian_plugin_brain.public_distribution import assert_public_tree, excluded_path, initialize_runtime, validate_public_vault, validate_public_edition

spec = importlib.util.spec_from_file_location("release", REPO / "scripts/package_release.py")
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class PublicDistributionTests(unittest.TestCase):
    def copy_vault(self, folder: str) -> Path:
        vault = Path(folder) / "vault"
        shutil.copytree(REPO / "assets/template-brain", vault)
        return vault

    def test_public_snapshot_has_only_reviewed_provenance(self) -> None:
        assert_public_tree(REPO)
        for name in ("assets/template-brain", "examples/sample-vault"):
            catalog = validate_public_vault(REPO / name)
            self.assertEqual(len(catalog["sources"]), 121)
            self.assertEqual(sum(len(s["claims"]) for s in catalog["sources"]), 200)
            self.assertFalse((REPO / name / ".raw").exists())
            self.assertFalse((REPO / name / ".obsidian").exists())

    def test_root_catalog_cannot_drift_from_reviewed_vault_catalog(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "references").mkdir()
            shutil.copy2(REPO / "PUBLIC_EDITION.json", root / "PUBLIC_EDITION.json")
            shutil.copy2(REPO / "references/public-sources.json", root / "references/public-sources.json")
            shutil.copytree(REPO / "assets/template-brain", root / "assets/template-brain")
            validate_public_edition(root, include_sample=False)
            path = root / "references/public-sources.json"
            path.write_text(path.read_text() + " ")
            with self.assertRaisesRegex(ValueError, "Root public source catalog hash mismatch"):
                validate_public_edition(root, include_sample=False)
            edition_path = root / "PUBLIC_EDITION.json"
            edition = json.loads(edition_path.read_text())
            edition["catalog_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
            edition_path.write_text(json.dumps(edition))
            with self.assertRaisesRegex(ValueError, "catalogs differ"):
                validate_public_edition(root, include_sample=False)

    def test_new_runtime_has_local_immutable_catalog_and_generic_config(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            vault = self.copy_vault(folder)
            initialize_runtime(vault, REPO / "assets/vault-defaults")
            manifest = json.loads((vault / ".raw/.manifest.json").read_text())
            entry = manifest["sources"][0]
            self.assertEqual(entry["source_type"], "public-source-catalog")
            self.assertEqual(hashlib.sha256((vault / entry["path"]).read_bytes()).hexdigest(), entry["sha256"])
            self.assertGreaterEqual(len(json.loads((vault / ".obsidian/graph.json").read_text())["colorGroups"]), 4)
            graph = json.loads((vault / ".obsidian/graph.json").read_text())
            self.assertTrue(graph["colorGroups"][-1]["query"].startswith("tag:#domain/"))
            self.assertTrue(graph["colorGroups"][0]["query"].startswith("tag:#type/"))
            self.assertFalse(graph["showTags"])
            self.assertEqual(graph["search"], 'path:"wiki/"')
            bookmarks = json.loads((vault / ".obsidian/bookmarks.json").read_text())
            views = bookmarks["items"][0]["items"]
            self.assertEqual(len(views), 7)
            self.assertEqual({view["title"] for view in views}, {
                "The whole brain", "Creator playbooks", "Concepts and architecture",
                "Source notes", "Decisions and outputs", "Questions and experiments",
                "Show tag connections"})
            self.assertTrue(all(view["type"] == "graph" and view["options"]["colorGroups"] == graph["colorGroups"] for view in views))
            self.assertTrue(views[-1]["options"]["showTags"])
            self.assertTrue((vault / "wiki/meta/Graph Views.md").is_file())
            with self.assertRaisesRegex(ValueError, "new vault"):
                initialize_runtime(vault, REPO / "assets/vault-defaults")

    def test_tampered_catalog_is_rejected_before_runtime_writes(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            vault = self.copy_vault(folder)
            path = vault / "references/public-sources.json"
            path.write_text(path.read_text() + " ")
            with self.assertRaisesRegex(ValueError, "hash mismatch"):
                initialize_runtime(vault, REPO / "assets/vault-defaults")
            self.assertFalse((vault / ".raw").exists())
            self.assertFalse((vault / ".obsidian").exists())

    def test_unknown_catalog_field_is_rejected_even_with_new_hash(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            vault = self.copy_vault(folder)
            path = vault / "references/public-sources.json"
            data = json.loads(path.read_text())
            data["sources"][0]["private_capture"] = "synthetic unapproved field"
            path.write_text(json.dumps(data))
            marker_path = vault / "PUBLIC_VAULT.json"
            marker = json.loads(marker_path.read_text())
            marker["catalog_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
            marker_path.write_text(json.dumps(marker))
            with self.assertRaisesRegex(ValueError, "Unreviewed field"):
                validate_public_vault(vault)

    def test_runtime_manifest_loss_or_capture_tampering_fails_lint(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            vault = self.copy_vault(folder)
            initialize_runtime(vault, REPO / "assets/vault-defaults")
            manifest = vault / ".raw/.manifest.json"
            source = vault / json.loads(manifest.read_text())["sources"][0]["path"]
            source.write_text("tampered synthetic fixture")
            command = [sys.executable, str(REPO / "scripts/lint_vault.py"), "--vault", str(vault), "--template"]
            proc = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("sha256 mismatch", proc.stderr)
            manifest.unlink()
            proc = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("missing its manifest", proc.stderr)

    def test_private_source_tree_and_archive_entries_are_blocked(self) -> None:
        entries = [".raw/private.txt", "vault/.obsidian/workspace.json", "references/source-ledger.json", "vault/wiki/log.md", "references/research/capture.json", ".env.staging"]
        for entry in entries:
            with self.subTest(entry=entry), tempfile.TemporaryDirectory() as folder:
                path = Path(folder) / entry
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("synthetic private fixture")
                with self.assertRaises(ValueError):
                    assert_public_tree(Path(folder))
                archive = Path(folder) / "unsafe.zip"
                with zipfile.ZipFile(archive, "w") as z:
                    z.writestr("source/" + entry, "synthetic private fixture")
                with self.assertRaises(SystemExit):
                    release.validate_zip(archive)

    def test_template_zip_has_public_navigation_and_no_private_paths(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            archive = Path(folder) / "template.zip"
            release.build_zip(archive, REPO / "assets/template-brain", "template")
            release.validate_zip(archive)
            with zipfile.ZipFile(archive) as z:
                self.assertIn("template/wiki/home.md", z.namelist())
                self.assertIn("template/wiki/activity.md", z.namelist())
                self.assertFalse(any(excluded_path(Path(name)) for name in z.namelist()))


if __name__ == "__main__":
    unittest.main()
