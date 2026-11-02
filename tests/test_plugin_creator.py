#!/usr/bin/env python3
"""Offline artifact generation, provenance, and destination-boundary regressions."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
from obsidian_plugin_brain.creator import ARCHETYPES, CreatorError, create_project, load_brief, render_project, validate_brief


class CreatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.brief = json.loads((REPO / "references/creator/example-brief.json").read_text())

    def test_all_starters_deterministic_and_source_bound(self) -> None:
        for archetype in ARCHETYPES:
            brief = {**self.brief, "archetype": archetype}
            first = render_project(brief)
            self.assertEqual(first, render_project(brief))
            manifest = json.loads(first["manifest.json"])
            package = json.loads(first["package.json"])
            lock = json.loads(first["package-lock.json"])
            self.assertEqual(manifest["id"], self.brief["id"])
            self.assertEqual(package["name"], lock["name"])
            self.assertEqual(package["devDependencies"], lock["packages"][""]["devDependencies"])
            self.assertEqual(package["devDependencies"]["obsidian"], manifest["minAppVersion"])
            self.assertIn("Unverified", first["docs/ACCEPTANCE.md"])
            self.assertIn("https://", first["docs/SOURCES.md"])
            self.assertIn("docs/DATA_AND_MIGRATIONS.md", first)
            for text in first.values():
                self.assertNotIn("__VIEW_ID__", text)
                self.assertNotIn("__ROOT_CLASS__", text)
                self.assertFalse(any(c in text for c in ("\u2013", "\u2014")))
            if archetype == "webgl":
                self.assertIn("Permission is hereby granted", first["THIRD_PARTY_NOTICES.md"])

    def test_dry_run_and_receipt_match_created_files(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            workspace = Path(root)
            output = workspace / "sources" / "heading-compass"
            preview = create_project(self.brief, output, workspace=workspace, dry_run=True)
            self.assertFalse((workspace / "sources").exists())
            receipt = create_project(self.brief, output, workspace=workspace)
            self.assertEqual(preview, receipt)
            for name, expected in receipt["files"].items():
                self.assertEqual(hashlib.sha256((output / name).read_bytes()).hexdigest(), expected)
            self.assertEqual(receipt["plugin_runtime"], "unverified")
            self.assertFalse(receipt["installed"])
            self.assertFalse((output / "main.js").exists())
            self.assertFalse((output / "node_modules").exists())

    def test_no_overwrite_escape_symlink_or_vault_destination(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            workspace = Path(root)
            existing = workspace / "existing"
            existing.mkdir()
            original = existing / "owner.txt"
            original.write_text("Keep this user content")
            with self.assertRaises(CreatorError):
                create_project(self.brief, existing, workspace=workspace)
            self.assertEqual(original.read_text(), "Keep this user content")
            with self.assertRaises(CreatorError):
                create_project(self.brief, workspace.parent / "escaped-creator-output", workspace=workspace)
            (workspace / "alias").symlink_to(existing, target_is_directory=True)
            with self.assertRaises(CreatorError):
                create_project(self.brief, workspace / "alias" / "new", workspace=workspace)
            with self.assertRaises(CreatorError):
                create_project(self.brief, workspace / ".config" / "new", workspace=workspace)
            active = workspace / "active"
            (active / ".obsidian").mkdir(parents=True)
            with self.assertRaises(CreatorError):
                create_project(self.brief, active / "new", workspace=workspace)
            deployed = workspace / "brain"
            (deployed / "wiki").mkdir(parents=True)
            (deployed / "CODEX.md").write_text("Vault root")
            with self.assertRaises(CreatorError):
                create_project(self.brief, deployed / "new", workspace=workspace)

    def test_invalid_briefs_fail_before_writes(self) -> None:
        cases = [dict(api_key="do-not-store"), dict(id="../escape"), dict(name="My Obsidian Plugin"),
                 dict(archetype="unknown"), dict(platforms=["desktop", "desktop"]),
                 dict(platforms=[True]), dict(acceptance_criteria=[]), dict(purpose=" "),
                 dict(name="bad\nname"), dict(name="bad\u2014name")]
        with tempfile.TemporaryDirectory() as root:
            workspace = Path(root)
            for patch in cases:
                with self.assertRaises(CreatorError):
                    create_project({**self.brief, **patch}, workspace / "new", workspace=workspace)
                self.assertFalse((workspace / "new").exists())
            oversized = workspace / "large.json"
            oversized.write_text("x" * (64 * 1024 + 1))
            with self.assertRaises(CreatorError):
                load_brief(oversized)

    def test_cli_preview_and_list(self) -> None:
        listed = subprocess.run([sys.executable, "-m", "obsidian_plugin_brain", "starters"], cwd=REPO, capture_output=True, text=True)
        self.assertEqual(listed.returncode, 0, listed.stderr)
        self.assertEqual(set(json.loads(listed.stdout)), set(ARCHETYPES))
        with tempfile.TemporaryDirectory() as root:
            preview = subprocess.run([sys.executable, "-m", "obsidian_plugin_brain", "create-plugin", "--brief", "references/creator/example-brief.json", "--workspace", root, "--out", "new-source", "--dry-run"], cwd=REPO, capture_output=True, text=True)
            self.assertEqual(preview.returncode, 0, preview.stderr)
            self.assertEqual(json.loads(preview.stdout)["evidence_class"], "generated-source-only")
            self.assertFalse((Path(root) / "new-source").exists())

    def test_brain_package_excludes_generated_projects_and_node_modules(self) -> None:
        spec = importlib.util.spec_from_file_location("release_for_creator_test", REPO / "scripts/package_release.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as root:
            workspace = Path(root)
            (workspace / "public.md").write_text("Brain source")
            private = workspace / "unrelated-project"
            private.mkdir()
            (private / "CREATOR_RECEIPT.json").write_text("{}")
            (private / "private.md").write_text("Never ship this project")
            dependencies = workspace / "node_modules"
            dependencies.mkdir()
            (dependencies / "hidden.js").write_text("Dependency code")
            self.assertEqual([p.relative_to(workspace).as_posix() for p in module.iter_tree(workspace)], ["public.md"])


if __name__ == "__main__":
    unittest.main()
