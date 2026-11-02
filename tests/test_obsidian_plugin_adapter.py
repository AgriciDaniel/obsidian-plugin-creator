#!/usr/bin/env python3
"""Unit and integration tests for the Obsidian Plugin Brain static adapter."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from obsidian_plugin_brain.importers.plugin_repo import ImporterError, import_plugin_repo
from obsidian_plugin_brain.reports.readiness_report import render_readiness_report
from obsidian_plugin_brain.synthesis.review_health import SynthesisError, synthesize_plugin_review


FIXTURES = REPO / "tests" / "fixtures" / "obsidian-plugin"


def test_healthy_multi_scope_plugin() -> None:
    imported = import_plugin_repo(FIXTURES / "healthy-multi-scope")
    assert imported["manifest"]["id"] == "spatial-graph-codex"
    assert "dashboard-custom-views" in imported["scopes"]
    assert "visuals-3d-webgl" in imported["scopes"]
    assert "editor-codemirror6" in imported["scopes"]
    assert "markdown-processors" in imported["scopes"]
    assert "ui-framework-mounted" in imported["scopes"]
    assert "mobile-cross-platform" in imported["scopes"]
    assert imported["signals"]["detach_leaves_in_onunload"] is False
    assert imported["signals"]["externalizes_codemirror"] is True

    synthesis = synthesize_plugin_review(imported)
    assert synthesis["gate_status"] == "static-signals-clear", synthesis
    assert synthesis["static_signal_score"] == 100
    assert synthesis["release_readiness"] == "unverified"
    assert synthesis["counts"]["critical"] == 0
    assert synthesis["counts"]["warning"] == 0

    report = render_readiness_report(imported, synthesis)
    assert "Spatial Graph Codex" in report
    assert "static-signals-clear" in report
    assert "No lint, compilation, Obsidian runtime" in report
    assert "\u2014" not in report and "\u2013" not in report


def test_flawed_antipattern_plugin() -> None:
    imported = import_plugin_repo(FIXTURES / "flawed-antipatterns")
    synthesis = synthesize_plugin_review(imported)
    assert synthesis["gate_status"] == "blocked-critical"
    assert synthesis["counts"]["critical"] >= 5
    failed_rules = {f["rule_id"] for f in synthesis["findings"] if f["status"] == "fail"}
    for expected in (
        "OB-REV-001",
        "OB-REV-002",
        "OB-REV-003",
        "OB-REV-004",
        "OB-REV-005",
        "OB-REV-006",
        "OB-REV-007",
        "OB-REV-008",
        "OB-REV-009",
        "OB-REV-010",
        "OB-REV-011",
        "OB-REV-012",
        "OB-REV-014",
    ):
        assert expected in failed_rules, f"Expected {expected} to fail, got {failed_rules}"


def test_malformed_and_missing_inputs() -> None:
    try:
        import_plugin_repo(FIXTURES / "malformed")
    except ImporterError as exc:
        assert "Malformed plugin manifest" in str(exc)
    else:
        raise AssertionError("Expected ImporterError on malformed manifest.json")

    try:
        import_plugin_repo(FIXTURES / "does-not-exist")
    except ImporterError as exc:
        assert "does not exist" in str(exc)
    else:
        raise AssertionError("Expected ImporterError on missing directory")


def test_unknown_source_id_rejected() -> None:
    imported = import_plugin_repo(FIXTURES / "healthy-multi-scope")
    with tempfile.TemporaryDirectory(prefix="obsidian-plugin-brain-bad-catalog-") as tmp:
        bad_catalog = Path(tmp) / "bad-catalog.json"
        bad_catalog.write_text(
            json.dumps(
                {
                    "version": 1,
                    "rules": {
                        "OB-REV-001": {
                            "title": "Test rule",
                            "scope": "core-commands-lifecycle",
                            "canon_note": "Plugin lifecycle, Component ownership, and cleanup discipline",
                            "confidence": "evidence-based",
                            "source_ids": ["nonexistent-ledger-source-id"],
                        }
                    },
                }
            ),
            encoding="utf-8",
        )
        try:
            synthesize_plugin_review(imported, catalog_path=bad_catalog)
        except SynthesisError as exc:
            assert "unknown source-ledger ids" in str(exc)
        else:
            raise AssertionError("Expected SynthesisError when catalog references unknown source id")


def test_cli_script_invocation() -> None:
    proc = subprocess.run(
        [
            sys.executable,
            str(REPO / "scripts" / "plugin_review_audit.py"),
            "--plugin-dir",
            str(FIXTURES / "healthy-multi-scope"),
            "--strict",
            "--json",
        ],
        cwd=REPO,
        text=True,
        capture_output=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    payload = json.loads(proc.stdout)
    assert payload["synthesis"]["gate_status"] == "static-signals-clear"


def test_missing_sources_and_metadata_do_not_pass() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        shutil.copy(FIXTURES / "healthy-multi-scope" / "manifest.json", root / "manifest.json")
        imported = import_plugin_repo(root)
        synthesis = synthesize_plugin_review(imported)
        assert synthesis["gate_status"] == "incomplete-static-evidence"
        assert synthesis["counts"]["unknown"] > 0
        assert synthesis["static_signal_score"] < 100
        assert synthesis["release_readiness"] == "unverified"


def test_symlinks_and_oversized_sources_rejected() -> None:
    for filename in ("manifest.json", "main.ts", "styles.css", "esbuild.config.mjs"):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "plugin"
            root.mkdir()
            shutil.copy(FIXTURES / "healthy-multi-scope" / "manifest.json", root / "manifest.json")
            outside = Path(tmp) / "private.txt"
            outside.write_text("PRIVATE_VALUE_MUST_NOT_BE_READ")
            target = root / filename
            target.unlink(missing_ok=True)
            target.symlink_to(outside)
            try:
                import_plugin_repo(root)
            except ImporterError as exc:
                assert "symlink" in str(exc)
                assert "PRIVATE_VALUE" not in str(exc)
            else:
                raise AssertionError(f"Symlink was accepted: {filename}")
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        shutil.copy(FIXTURES / "healthy-multi-scope" / "manifest.json", root / "manifest.json")
        (root / "main.ts").write_text("x" * (2 * 1024 * 1024 + 1))
        try:
            import_plugin_repo(root)
        except ImporterError as exc:
            assert "limit" in str(exc)
        else:
            raise AssertionError("Oversized source accepted")


def test_quoted_packages_are_not_externals_and_secrets_not_returned() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        manifest = json.loads((FIXTURES / "healthy-multi-scope" / "manifest.json").read_text())
        manifest["apiKey"] = "PRIVATE_EXTRA_METADATA"
        (root / "manifest.json").write_text(json.dumps(manifest))
        (root / ".env").write_text("KEY=PRIVATE_ENV_CONTENT")
        (root / "main.ts").write_text('import { Plugin } from "obsidian";')
        (root / "esbuild.config.mjs").write_text('const entry = "obsidian"; const config = { external: ["electron"] };')
        imported = import_plugin_repo(root)
        assert imported["signals"]["externalizes_obsidian"] is False
        assert "PRIVATE_EXTRA_METADATA" not in json.dumps(imported)
        assert "PRIVATE_ENV_CONTENT" not in json.dumps(imported)


def test_partial_host_externals_are_not_complete() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        shutil.copy(FIXTURES / "healthy-multi-scope" / "manifest.json", root / "manifest.json")
        (root / "main.ts").write_text('import { EditorView } from "@codemirror/view"; import { StateField } from "@codemirror/state";')
        (root / "esbuild.config.mjs").write_text('const config = { external: ["obsidian", "@codemirror/view"] };')
        imported = import_plugin_repo(root)
        assert imported["signals"]["externalizes_codemirror"] is False


def test_unprefixed_node_builtins_block_mobile_target() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "plugin"
        shutil.copytree(FIXTURES / "healthy-multi-scope", root)
        source = root / "src" / "main.ts"
        source.write_text(source.read_text() + '\nimport { Readable } from "stream"; import { Buffer } from "buffer"; import timers from "timers/promises";\n')
        imported = import_plugin_repo(root)
        assert {"stream", "buffer", "timers/promises"}.issubset(imported["signals"]["node_or_electron_imports"])
        synthesis = synthesize_plugin_review(imported)
        assert synthesis["gate_status"] == "blocked-critical"
        assert any(f["rule_id"] == "OB-REV-006" and f["status"] == "fail" for f in synthesis["findings"])


def test_invalid_compatibility_history_is_not_silently_accepted() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "plugin"
        shutil.copytree(FIXTURES / "healthy-multi-scope", root)
        path = root / "versions.json"
        versions = json.loads(path.read_text())
        versions["broken-entry"] = {"private": "PRIVATE_BAD_VERSION_VALUE"}
        path.write_text(json.dumps(versions))
        imported = import_plugin_repo(root)
        assert imported["signals"]["versions_invalid_entry_count"] == 1
        assert imported["warnings"]
        assert "PRIVATE_BAD_VERSION_VALUE" not in json.dumps(imported)
        synthesis = synthesize_plugin_review(imported)
        assert synthesis["gate_status"] == "needs-warnings-review"
        finding = next(f for f in synthesis["findings"] if f["rule_id"] == "OB-REV-002")
        assert finding["status"] == "fail"
        assert "invalid compatibility history" in finding["message"]


def main() -> int:
    test_healthy_multi_scope_plugin()
    test_flawed_antipattern_plugin()
    test_malformed_and_missing_inputs()
    test_unknown_source_id_rejected()
    test_cli_script_invocation()
    test_missing_sources_and_metadata_do_not_pass()
    test_symlinks_and_oversized_sources_rejected()
    test_quoted_packages_are_not_externals_and_secrets_not_returned()
    test_partial_host_externals_are_not_complete()
    test_unprefixed_node_builtins_block_mobile_target()
    test_invalid_compatibility_history_is_not_silently_accepted()
    print("Obsidian plugin adapter tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
