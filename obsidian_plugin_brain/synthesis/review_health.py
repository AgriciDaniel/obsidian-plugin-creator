from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[2]
DEFAULT_CATALOG = REPO / "references" / "schemas" / "review-rules-catalog.json"
DEFAULT_LEDGER = REPO / "references" / "public-sources.json"


class SynthesisError(ValueError):
    """Raised when review rule metadata or source-ledger bindings are missing or invalid."""


def _load_json(path: Path, label: str) -> dict[str, Any]:
    if not path.is_file():
        raise SynthesisError(f"Missing {label}: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except ValueError as exc:
        raise SynthesisError(f"Malformed {label} ({path}): {exc}") from exc
    if not isinstance(data, dict):
        raise SynthesisError(f"{label} must be a JSON object: {path}")
    return data


def _emit(
    findings: list[dict[str, Any]],
    *,
    rule_id: str,
    status: str,
    severity: str,
    message: str,
    remediation: str,
    catalog_rules: dict[str, dict[str, Any]],
    ledger_ids: set[str],
) -> None:
    meta = catalog_rules.get(rule_id)
    if not isinstance(meta, dict):
        raise SynthesisError(f"Unknown rule_id not in review-rules-catalog.json: {rule_id}")
    source_ids = [s for s in meta.get("source_ids", []) if isinstance(s, str) and s]
    if not source_ids:
        raise SynthesisError(f"Rule {rule_id} declares no source_ids")
    missing = [s for s in source_ids if s not in ledger_ids]
    if missing:
        raise SynthesisError(f"Rule {rule_id} references unknown source-ledger ids: {', '.join(missing)}")
    findings.append(
        {
            "rule_id": rule_id,
            "title": str(meta.get("title", rule_id)),
            "scope": str(meta.get("scope", "core-commands-lifecycle")),
            "canon_note": str(meta.get("canon_note", "Plugin lifecycle, Component ownership, and cleanup discipline")),
            "status": status,
            "severity": severity,
            "confidence": "practitioner",
            "rule_confidence": str(meta.get("confidence", "evidence-based")),
            "message": message,
            "remediation": remediation,
            "source_ids": source_ids,
        }
    )


def synthesize_plugin_review(
    imported: dict[str, Any],
    *,
    catalog_path: str | Path = DEFAULT_CATALOG,
    ledger_path: str | Path = DEFAULT_LEDGER,
) -> dict[str, Any]:
    """Evaluate imported Obsidian plugin signals against source-cited review rules."""
    if Path(ledger_path).resolve() == DEFAULT_LEDGER.resolve():
        from obsidian_plugin_brain.public_distribution import validate_public_edition
        try:
            validate_public_edition(REPO, include_sample=False)
        except (ValueError, OSError) as exc:
            raise SynthesisError("Public provenance verification failed: " + str(exc)) from exc
    catalog = _load_json(Path(catalog_path), "review rules catalog")
    ledger = _load_json(Path(ledger_path), "source ledger")
    ledger_ids = {
        entry.get("id")
        for entry in ledger.get("sources", [])
        if isinstance(entry, dict) and isinstance(entry.get("id"), str)
    }
    if not ledger_ids:
        raise SynthesisError("Source ledger contains no captured source ids")

    catalog_rules = catalog.get("rules")
    if not isinstance(catalog_rules, dict) or not catalog_rules:
        raise SynthesisError("review-rules-catalog.json contains no rules object")

    signals = imported.get("signals")
    if not isinstance(signals, dict):
        raise SynthesisError("Imported payload is missing 'signals' dictionary")
    scopes = set(imported.get("scopes") or [])
    findings: list[dict[str, Any]] = []

    # OB-REV-001: Manifest ID & naming compliance
    bad_id_or_name = (
        not signals.get("plugin_id_valid_format")
        or signals.get("plugin_id_contains_obsidian")
        or signals.get("plugin_name_contains_obsidian")
        or not signals.get("version_valid_semver")
        or not signals.get("min_app_version_valid_semver")
    )
    if bad_id_or_name:
        _emit(
            findings,
            rule_id="OB-REV-001",
            status="fail",
            severity="critical",
            message="manifest.json violates ID, naming, or X.Y.Z semver rules (avoid 'obsidian' in id/name and use strict X.Y.Z versions).",
            remediation="Use lowercase kebab-case id without 'obsidian', remove 'Obsidian' from name, and format version/minAppVersion as X.Y.Z.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )
    else:
        _emit(
            findings,
            rule_id="OB-REV-001",
            status="pass",
            severity="pass",
            message="Selected manifest ID, naming, and version patterns passed; full directory naming review remains manual.",
            remediation="None required.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )

    # OB-REV-002: Local description convention and optional compatibility history
    desc_len = int(signals.get("description_length") or 0)
    desc_ok = 0 < desc_len <= 250 and bool(signals.get("description_ends_with_punctuation"))
    if not desc_ok:
        _emit(
            findings,
            rule_id="OB-REV-002",
            status="fail",
            severity="warning",
            message=f"Description (length {desc_len}) differs from this brain's concise sentence convention; this is an editorial warning, not a verified directory rejection.",
            remediation="Review the description for clarity and current directory requirements; this brain suggests <= 250 characters and terminal punctuation.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )
    elif signals.get("versions_invalid_entry_count"):
        _emit(findings, rule_id="OB-REV-002", status="fail", severity="warning",
              message="versions.json contains invalid compatibility history entries; the map has not passed validation.",
              remediation="Review versions.json and use X.Y.Z string keys and minimum-app-version values for each compatibility entry.",
              catalog_rules=catalog_rules, ledger_ids=ledger_ids)
    elif signals.get("versions_present") and not signals.get("versions_matches_manifest"):
        _emit(
            findings,
            rule_id="OB-REV-002",
            status="fail",
            severity="warning",
            message="versions.json does not map the current manifest.json version to minAppVersion.",
            remediation="Run version-bump.mjs or update versions.json so versions[manifest.version] == manifest.minAppVersion.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )
    elif not signals.get("versions_present"):
        _emit(findings, rule_id="OB-REV-002", status="unknown", severity="info",
              message="No parseable versions.json compatibility history is available.",
              remediation="Check whether a compatibility map is needed and verify it before release.",
              catalog_rules=catalog_rules, ledger_ids=ledger_ids)
    else:
        _emit(
            findings,
            rule_id="OB-REV-002",
            status="pass",
            severity="pass",
            message="Manifest description length/punctuation and versions.json compatibility check passed.",
            remediation="Keep versions.json updated on every release tag.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )

    # OB-REV-003: Never detach leaves in onunload()
    if signals.get("detach_leaves_in_onunload"):
        _emit(
            findings,
            rule_id="OB-REV-003",
            status="fail",
            severity="critical",
            message="onunload() calls detachLeavesOfType(), destroying the user's saved workspace layout across reloads and updates.",
            remediation="Remove detachLeavesOfType() from onunload(); Obsidian manages registered view leaves automatically.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )
    else:
        _emit(
            findings,
            rule_id="OB-REV-003",
            status="pass",
            severity="pass",
            message="No detachLeavesOfType() call detected in the approximate onunload() scan.",
            remediation="None required.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )

    # OB-REV-004: Avoid global window.app & unregistered listeners
    if signals.get("uses_global_window_app"):
        _emit(
            findings,
            rule_id="OB-REV-004",
            status="fail",
            severity="critical",
            message="Plugin references global window.app or globalThis.app instead of the scoped Plugin.app instance.",
            remediation="Pass this.app explicitly (or via React/Svelte context) instead of reading window.app.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )
    else:
        _emit(
            findings,
            rule_id="OB-REV-004",
            status="pass",
            severity="pass",
            message="No global window.app reference detected.",
            remediation="Continue scoping lifecycle hooks through this.register* helpers.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )

    # OB-REV-005: DOM XSS sinks (innerHTML / outerHTML / dangerouslySetInnerHTML)
    if signals.get("uses_raw_inner_html"):
        _emit(
            findings,
            rule_id="OB-REV-005",
            status="fail",
            severity="critical",
            message="Raw HTML injection sink (innerHTML, outerHTML, insertAdjacentHTML, or dangerouslySetInnerHTML) detected.",
            remediation="Replace raw HTML injection with Obsidian createEl/createDiv/DomElementInfo, sanitizeHTMLToDom(), or MarkdownRenderer.render().",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )
    else:
        _emit(
            findings,
            rule_id="OB-REV-005",
            status="pass",
            severity="pass",
            message="Zero raw HTML injection sinks detected in plugin source files.",
            remediation="None required.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )

    # OB-REV-006: Mobile safety vs Node.js / Electron builtins
    node_imports = signals.get("node_or_electron_imports") or []
    if not signals.get("is_desktop_only") and node_imports:
        _emit(
            findings,
            rule_id="OB-REV-006",
            status="fail",
            severity="critical",
            message=f"manifest.json sets isDesktopOnly=false, but source imports desktop-only modules: {', '.join(node_imports)}.",
            remediation="Replace Node/Electron modules with Vault API, normalizePath, Web Crypto, and requestUrl, or set isDesktopOnly: true.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )
    else:
        _emit(
            findings,
            rule_id="OB-REV-006",
            status="pass",
            severity="pass",
            message="No conflicting desktop module import detected by the limited static import scan.",
            remediation="None required.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )

    # OB-REV-007: Bundler externals (obsidian + @codemirror/*)
    if not imported.get("bundler"):
        _emit(findings, rule_id="OB-REV-007", status="unknown", severity="info",
              message="No supported bundler config was found; host runtime externalization is unverified.",
              remediation="Inspect the actual bundler output and external declarations before release.",
              catalog_rules=catalog_rules, ledger_ids=ledger_ids)
    elif not signals.get("externalizes_obsidian"):
        _emit(
            findings,
            rule_id="OB-REV-007",
            status="fail",
            severity="critical",
            message="Bundler configuration does not mark 'obsidian' as external.",
            remediation="Add 'obsidian' and host-provided @codemirror/* and @lezer/* packages to bundler external list.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )
    elif signals.get("imports_codemirror") and imported.get("bundler") and not signals.get("externalizes_codemirror"):
        _emit(
            findings,
            rule_id="OB-REV-007",
            status="fail",
            severity="critical",
            message="Plugin imports @codemirror/* packages without externalizing them, breaking StateField/Facet identity in Obsidian's host editor.",
            remediation="Mark all @codemirror/* and @lezer/* packages external in esbuild/Vite/Rollup config.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )
    else:
        _emit(
            findings,
            rule_id="OB-REV-007",
            status="pass",
            severity="pass",
            message="Literal external arrays list obsidian and the detected host editor imports; built output remains unverified.",
            remediation="None required.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )

    # OB-REV-008: Command ID prefix & default hotkeys
    if signals.get("prefixed_command_ids") or signals.get("default_hotkeys_declared"):
        _emit(
            findings,
            rule_id="OB-REV-008",
            status="fail",
            severity="warning",
            message="addCommand() either prefixes command id with plugin id or sets default hotkeys.",
            remediation="Omit the plugin ID from command.id (Obsidian prefixes it automatically) and avoid default hotkeys to prevent user keybinding conflicts.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )
    else:
        _emit(
            findings,
            rule_id="OB-REV-008",
            status="pass",
            severity="pass",
            message="Command declarations omit redundant plugin ID prefixes and default hotkeys.",
            remediation="None required.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )

    # OB-REV-009: Settings tab headings (setHeading vs raw h1-h6)
    if signals.get("uses_raw_heading_in_settings"):
        _emit(
            findings,
            rule_id="OB-REV-009",
            status="fail",
            severity="warning",
            message="PluginSettingTab creates raw <h1>-<h6> elements instead of new Setting(containerEl).setName(...).setHeading().",
            remediation="Use Setting.setHeading() with sentence case so settings tabs match Obsidian core styling and pass eslint-plugin checks.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )

    # OB-REV-010: Vault startup create storm & FileManager link/trash hygiene
    if (
        signals.get("uses_vault_create_without_layout_ready")
        or signals.get("uses_vault_rename_directly")
        or signals.get("uses_vault_delete_or_trash")
    ):
        _emit(
            findings,
            rule_id="OB-REV-010",
            status="fail",
            severity="warning",
            message="Vault mutation or event hazard detected (unguarded vault.on('create'), direct vault.rename(), or direct vault.delete/trash()).",
            remediation="Wrap vault.on('create') inside workspace.onLayoutReady(), use fileManager.renameFile() to preserve links, and use fileManager.trashFile() to respect user trash preferences.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )
    else:
        _emit(
            findings,
            rule_id="OB-REV-010",
            status="pass",
            severity="pass",
            message="Vault event registration and FileManager link/trash boundaries look clean.",
            remediation="None required.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )

    # OB-REV-011: Network CORS & mobile safety (fetch vs requestUrl)
    if "network-external-api" in scopes and signals.get("uses_fetch") and not signals.get("uses_request_url"):
        _emit(
            findings,
            rule_id="OB-REV-011",
            status="fail",
            severity="info",
            message="Plugin calls browser fetch() without Obsidian requestUrl(), which can fail under CORS restrictions on desktop and mobile.",
            remediation="Prefer requestUrl() from 'obsidian' for cross-origin HTTP requests and disclose external endpoints in README.md.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )

    # OB-REV-012: 3D WebGL & Visual pane discipline (ResizeObserver, visibility pause, GPU dispose)
    if "visuals-3d-webgl" in scopes:
        missing_3d: list[str] = []
        if not signals.get("webgl_has_resize_observer"):
            missing_3d.append("ResizeObserver on pane container")
        if not signals.get("webgl_has_visibility_guard"):
            missing_3d.append("tab/window visibility throttling")
        if not signals.get("webgl_has_dispose"):
            missing_3d.append("WebGL resource .dispose() cleanup")
        if missing_3d:
            _emit(
                findings,
                rule_id="OB-REV-012",
                status="fail",
                severity="warning",
                message=f"3D WebGL visual plugin is missing lifecycle safeguards: {', '.join(missing_3d)}.",
                remediation="Size canvases via ResizeObserver on contentEl, pause render loops when hidden, and dispose geometries/materials/textures/renderers in onClose().",
                catalog_rules=catalog_rules,
                ledger_ids=ledger_ids,
            )
        else:
            _emit(
                findings,
                rule_id="OB-REV-012",
                status="pass",
                severity="pass",
            message="ResizeObserver, visibility, and dispose tokens detected; correct ownership and execution order require runtime review.",
                remediation="None required.",
                catalog_rules=catalog_rules,
                ledger_ids=ledger_ids,
            )

    # OB-REV-013: Mounted UI framework unmount & CSS variable theming
    if signals.get("uses_react_create_root") and not signals.get("has_react_unmount"):
        _emit(
            findings,
            rule_id="OB-REV-013",
            status="fail",
            severity="warning",
            message="Plugin mounts a React root via createRoot() without calling root.unmount() during view/modal teardown.",
            remediation="Store the Root instance on the ItemView or Modal and call this.root?.unmount() inside onClose().",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )
    if signals.get("css_present") and not signals.get("css_uses_obsidian_variables"):
        _emit(
            findings,
            rule_id="OB-REV-014",
            status="fail",
            severity="warning",
            message="Plugin CSS does not reference Obsidian theme variables (var(--background-*, --text-*, --interactive-*)).",
            remediation="Replace hardcoded palette values with Obsidian CSS variables so community dark and light themes render natively.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )
    elif signals.get("css_present"):
        _emit(
            findings,
            rule_id="OB-REV-014",
            status="pass",
            severity="pass",
            message="Plugin CSS adopts Obsidian CSS custom properties for theme-native styling.",
            remediation="None required.",
            catalog_rules=catalog_rules,
            ledger_ids=ledger_ids,
        )

    if not signals.get("source_files_present"):
        for finding in findings:
            if finding["rule_id"] not in {"OB-REV-001", "OB-REV-002", "OB-REV-007"}:
                finding.update(status="unknown", severity="info", message="Plugin source is absent; this source rule could not be evaluated.")

    sources_by_id = {entry["id"]: entry for entry in ledger.get("sources", []) if isinstance(entry, dict) and "id" in entry}
    for finding in findings:
        finding["source_urls"] = [sources_by_id[sid].get("url", "") for sid in finding["source_ids"]]

    critical_count = sum(1 for f in findings if f["severity"] == "critical")
    warning_count = sum(1 for f in findings if f["severity"] == "warning")
    info_count = sum(1 for f in findings if f["severity"] == "info")
    score = max(0, 100 - 25 * critical_count - 8 * warning_count - 2 * info_count)

    unknown_count = sum(1 for f in findings if f["status"] == "unknown")
    if critical_count > 0:
        gate = "blocked-critical"
    elif unknown_count > 0:
        gate = "incomplete-static-evidence"
    elif warning_count > 0:
        gate = "needs-warnings-review"
    else:
        gate = "static-signals-clear"

    return {
        "plugin_id": signals.get("plugin_id"),
        "scopes": sorted(scopes),
        "static_signal_score": score,
        "score_basis": "Selected static heuristic signals only; not release readiness or runtime correctness",
        "release_readiness": "unverified",
        "evidence_class": "local-static-analysis",
        "gate_status": gate,
        "counts": {
            "critical": critical_count,
            "warning": warning_count,
            "info": info_count,
            "unknown": unknown_count,
            "pass": sum(1 for f in findings if f["status"] == "pass"),
        },
        "findings": findings,
    }
