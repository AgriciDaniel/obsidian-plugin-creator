from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any


class ImporterError(ValueError):
    """Raised when an Obsidian plugin directory cannot be statically imported safely."""


SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
PLUGIN_ID_RE = re.compile(r"^[a-z][a-z-]*$")
MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_TOTAL_BYTES = 20 * 1024 * 1024
MAX_FILES = 1000
MANIFEST_FIELDS = {"id", "name", "version", "minAppVersion", "description", "author", "isDesktopOnly"}
BUNDLER_FILES = (
    ("esbuild", "esbuild.config.mjs"),
    ("esbuild", "esbuild.config.js"),
    ("esbuild", "esbuild.config.cjs"),
    ("esbuild", "esbuild.config.ts"),
    ("vite", "vite.config.ts"),
    ("vite", "vite.config.mts"),
    ("vite", "vite.config.js"),
    ("vite", "vite.config.mjs"),
    ("rollup", "rollup.config.js"),
    ("rollup", "rollup.config.mjs"),
    ("rollup", "rollup.config.ts"),
)
SOURCE_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx", ".mjs", ".svelte", ".vue"}
SKIP_DIRS = {
    ".git",
    ".obsidian",
    "node_modules",
    "dist",
    "dist-plugin",
    "build",
    "coverage",
    ".cache",
    "__pycache__",
}
NODE_BUILTINS = {
    "_http_agent",
    "_http_client",
    "_http_common",
    "_http_incoming",
    "_http_outgoing",
    "_http_server",
    "_stream_duplex",
    "_stream_passthrough",
    "_stream_readable",
    "_stream_transform",
    "_stream_wrap",
    "_stream_writable",
    "_tls_common",
    "_tls_wrap",
    "assert",
    "async_hooks",
    "buffer",
    "cluster",
    "console",
    "constants",
    "diagnostics_channel",
    "domain",
    "events",
    "fs",
    "path",
    "os",
    "crypto",
    "child_process",
    "http",
    "https",
    "net",
    "tls",
    "worker_threads",
    "dgram",
    "dns",
    "readline",
    "inspector",
    "module",
    "perf_hooks",
    "process",
    "punycode",
    "querystring",
    "repl",
    "stream",
    "string_decoder",
    "sys",
    "timers",
    "trace_events",
    "tty",
    "url",
    "util",
    "v8",
    "vm",
    "wasi",
    "zlib",
}


def strip_code_comments(source: str) -> str:
    """Remove JS/TS block and line comments while preserving string literals."""
    pattern = re.compile(
        r'("(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|`(?:\\.|[^`\\])*`)|(/\*[\s\S]*?\*/|//[^\n]*)'
    )
    return pattern.sub(lambda m: m.group(1) if m.group(1) is not None else " ", source)


def _read_json(path: Path, label: str, *, required: bool = False) -> tuple[dict[str, Any] | None, list[str]]:
    if path.is_symlink():
        raise ImporterError(f"Refusing symlink input: {path.name}")
    if not path.exists():
        if required:
            raise ImporterError(f"Missing required {label}: {path.name}")
        return None, []
    if not path.is_file():
        raise ImporterError(f"{label} must be a regular file: {path.name}")
    if path.stat().st_size > MAX_FILE_BYTES:
        raise ImporterError(f"Input exceeds per-file limit: {path.name}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        if required:
            raise ImporterError(f"Malformed {label} ({path.name}): {exc}") from exc
        return None, [f"Could not parse optional {path.name}: {exc}"]
    if not isinstance(data, dict):
        if required:
            raise ImporterError(f"{label} ({path.name}) must contain a top-level JSON object")
        return None, [f"Optional {path.name} does not contain a top-level JSON object"]
    return data, []


def _extract_onunload_bodies(code: str) -> list[str]:
    """Extract approximate onunload() method bodies with brace matching."""
    bodies: list[str] = []
    for match in re.finditer(r"\bonunload\s*\([^)]*\)\s*(?::\s*[^{]+)?\{", code):
        start = match.end()
        depth = 1
        idx = start
        while idx < len(code) and depth > 0:
            ch = code[idx]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            idx += 1
        bodies.append(code[start : max(start, idx - 1)])
    return bodies


def _collect_source_files(root: Path) -> list[Path]:
    collected: list[Path] = []
    visited = 0
    bundler_names = {fname for _, fname in BUNDLER_FILES} | {"version-bump.mjs"}
    for dirname, dirs, filenames in os.walk(root, followlinks=False):
        visited += len(dirs) + len(filenames)
        if visited > 20000:
            raise ImporterError("Repository entry count exceeds static scan limit")
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not d.startswith(".") and not (Path(dirname) / d).is_symlink())
        if Path(dirname) == root:
            dirs[:] = [d for d in dirs if d not in {"scripts", "tests", "test", "__tests__"}]
        for name in sorted(filenames):
            path = Path(dirname) / name
            if name.startswith(".") or name in bundler_names or path.suffix not in SOURCE_EXTENSIONS:
                continue
            if path.is_symlink():
                raise ImporterError(f"Refusing symlink source: {path.relative_to(root)}")
            collected.append(path)
            if len(collected) > MAX_FILES:
                raise ImporterError("Source file count exceeds static scan limit")
    return collected


def _collect_css_files(root: Path) -> list[Path]:
    css_files: list[Path] = []
    candidates = [root / "styles.css"]
    if (root / "src").is_dir() and not (root / "src").is_symlink():
        for dirname, dirs, files in os.walk(root / "src", followlinks=False):
            dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not d.startswith(".") and not (Path(dirname) / d).is_symlink())
            candidates.extend(Path(dirname) / name for name in sorted(files) if name.endswith(".css") and not name.startswith("."))
            if len(candidates) > MAX_FILES:
                raise ImporterError("CSS file count exceeds static scan limit")
    for candidate in candidates:
        if candidate.is_symlink():
            raise ImporterError(f"Refusing symlink CSS input: {candidate.name}")
        if candidate.is_file() and candidate not in css_files:
            css_files.append(candidate)
    return css_files


def import_plugin_repo(plugin_dir: str | Path) -> dict[str, Any]:
    """Statically inspect an Obsidian plugin repository directory.

    Reads JSON manifests, bundler configs, CSS files, and TypeScript/JavaScript
    plugin sources without executing code, spawning subprocesses, or reading
    secret/environment files.
    """
    root = Path(plugin_dir).resolve()
    if not root.exists():
        raise ImporterError(f"Plugin directory does not exist: {root}")
    if not root.is_dir():
        raise ImporterError(f"Plugin path must be a directory: {root}")

    warnings: list[str] = []
    no_data: list[str] = [
        "Live Obsidian startup profiler duration (Settings -> Community plugins -> Debug startup time)",
        "Detached DOM and WebGL heap retention across repeated view open/close cycles",
        "Real iOS WebKit and Android WebView touch layout verification",
    ]
    inspected_files: list[str] = []
    scanned_bytes = 0

    def read_text(path: Path) -> str:
        nonlocal scanned_bytes
        if path.is_symlink():
            raise ImporterError(f"Refusing symlink input: {path.name}")
        if not path.is_file() or not path.resolve().is_relative_to(root):
            raise ImporterError(f"Input is not a regular in-repository file: {path.name}")
        size = path.stat().st_size
        scanned_bytes += size
        if size > MAX_FILE_BYTES or scanned_bytes > MAX_TOTAL_BYTES:
            raise ImporterError("Static scan byte limit exceeded")
        try:
            return path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            raise ImporterError(f"Could not read input: {path.name}") from exc

    manifest, m_warn = _read_json(root / "manifest.json", "plugin manifest", required=True)
    assert manifest is not None
    manifest = {key: value for key, value in manifest.items() if key in MANIFEST_FIELDS}
    warnings.extend(m_warn)
    inspected_files.append("manifest.json")

    for req_key in ("id", "name", "version", "minAppVersion", "description", "author"):
        val = manifest.get(req_key)
        if not isinstance(val, str) or not val.strip():
            raise ImporterError(f"manifest.json missing non-empty string field '{req_key}'")
    if not isinstance(manifest.get("isDesktopOnly"), bool):
        raise ImporterError("manifest.json missing boolean field 'isDesktopOnly'")

    versions, v_warn = _read_json(root / "versions.json", "versions map", required=False)
    warnings.extend(v_warn)
    invalid_version_entries = 0
    if versions is not None:
        inspected_files.append("versions.json")
        valid_versions = {key: value for key, value in versions.items() if SEMVER_RE.fullmatch(key) and isinstance(value, str) and SEMVER_RE.fullmatch(value)}
        invalid_version_entries = len(versions) - len(valid_versions)
        if invalid_version_entries:
            warnings.append(f"versions.json contains {invalid_version_entries} invalid compatibility entries; their contents are excluded from output")
        versions = valid_versions
    else:
        no_data.append("versions.json compatibility history (file not present)")

    package_json, p_warn = _read_json(root / "package.json", "package.json", required=False)
    warnings.extend(p_warn)
    all_deps: dict[str, str] = {}
    if package_json is not None:
        inspected_files.append("package.json")
        for dep_section in ("dependencies", "devDependencies"):
            sec = package_json.get(dep_section)
            if isinstance(sec, dict):
                for k, v in sec.items():
                    if isinstance(k, str) and isinstance(v, str):
                        all_deps[k] = v
    else:
        no_data.append("package.json dependency declarations")

    bundlers_detected: list[str] = []
    externals: set[str] = set()
    bundler_text_chunks: list[str] = []
    for b_kind, b_name in BUNDLER_FILES:
        b_path = root / b_name
        if b_path.is_file():
            bundlers_detected.append(b_kind)
            inspected_files.append(b_name)
            b_text = strip_code_comments(read_text(b_path))
            bundler_text_chunks.append(b_text)
            external_arrays = re.findall(r"\bexternal\s*:\s*\[([\s\S]*?)\]", b_text)
            for ext_match in re.findall(r"""['"](@?[a-zA-Z0-9_.*:/-]+)['"]""", "\n".join(external_arrays)):
                if (
                    ext_match in {"obsidian", "electron"}
                    or ext_match.startswith("@codemirror/")
                    or ext_match.startswith("@lezer/")
                    or ext_match.startswith("node:")
                    or ext_match in NODE_BUILTINS
                ):
                    externals.add(ext_match)
            if "builtinModules" in b_text or "builtins" in b_text:
                externals.add("node:builtinModules")

    bundler_combined = "\n".join(bundler_text_chunks)
    if not bundlers_detected:
        no_data.append("Bundler configuration file (esbuild/vite/rollup config not found)")

    source_files = _collect_source_files(root)
    raw_sources: list[tuple[str, str]] = []
    stripped_chunks: list[str] = []
    setting_tab_chunks: list[str] = []
    for src_path in source_files:
        rel_str = src_path.relative_to(root).as_posix()
        inspected_files.append(rel_str)
        raw = read_text(src_path)
        stripped = strip_code_comments(raw)
        raw_sources.append((rel_str, stripped))
        stripped_chunks.append(stripped)
        if "PluginSettingTab" in stripped:
            setting_tab_chunks.append(stripped)

    combined_code = "\n".join(stripped_chunks)
    combined_settings_code = "\n".join(setting_tab_chunks)
    if not source_files:
        warnings.append("No TypeScript or JavaScript plugin source files were found under root or src/")
        no_data.append("Plugin TypeScript/JavaScript source tree")

    css_files = _collect_css_files(root)
    css_chunks: list[str] = []
    for css_path in css_files:
        inspected_files.append(css_path.relative_to(root).as_posix())
        css_chunks.append(read_text(css_path))
    combined_css = "\n".join(css_chunks)

    # Scope detection across the 12 Obsidian plugin archetypes
    scopes: list[str] = ["core-commands-lifecycle"]
    if re.search(r"\b(ItemView|FileView|TextFileView|EditableFileView|registerView)\b", combined_code):
        scopes.append("dashboard-custom-views")
    if re.search(r"\b(BasesView|registerBasesView)\b", combined_code):
        scopes.append("bases-custom-view")
    if re.search(
        r"\b(Modal|SuggestModal|FuzzySuggestModal|EditorSuggest|AbstractInputSuggest|PluginSettingTab)\b",
        combined_code,
    ):
        scopes.append("modals-suggests-settings")
    if (
        re.search(r"\b(d3|cytoscape)\b", combined_code)
        or "getContext('2d')" in combined_code
        or 'getContext("2d")' in combined_code
        or ".canvas" in combined_code
        or any(k.startswith("d3") or k == "cytoscape" for k in all_deps)
    ):
        scopes.append("visuals-2d-canvas-svg")
    if (
        re.search(r"\b(THREE|WebGLRenderer|GLTFLoader)\b", combined_code)
        or "three" in all_deps
        or "@react-three/fiber" in all_deps
    ):
        scopes.append("visuals-3d-webgl")
    if (
        re.search(r"\b(registerEditorExtension|ViewPlugin|StateField|WidgetType|Decoration)\b", combined_code)
        or "@codemirror/" in combined_code
    ):
        scopes.append("editor-codemirror6")
    if re.search(
        r"\b(registerMarkdownPostProcessor|registerMarkdownCodeBlockProcessor|MarkdownRenderChild|MarkdownRenderer\.render)\b",
        combined_code,
    ):
        scopes.append("markdown-processors")
    if re.search(
        r"\b(metadataCache|processFrontMatter|openLinkText|resolveSubpath|registerObsidianProtocolHandler|getMarkdownFiles)\b",
        combined_code,
    ):
        scopes.append("vault-metadata-links")
    if (
        re.search(r"\b(createRoot|hydrateRoot|createApp)\b", combined_code)
        or any(k in all_deps for k in ("react", "react-dom", "svelte", "vue"))
    ):
        scopes.append("ui-framework-mounted")

    is_desktop_only = bool(manifest.get("isDesktopOnly", False))
    if not is_desktop_only:
        scopes.append("mobile-cross-platform")
    if re.search(r"\b(?:requestUrl\b|fetch\s*\(|new\s+WebSocket\b)", combined_code):
        scopes.append("network-external-api")

    # Extract static review and architecture signals
    plugin_id = str(manifest["id"])
    plugin_name = str(manifest["name"])
    plugin_version = str(manifest["version"])
    min_app_version = str(manifest["minAppVersion"])
    description = str(manifest["description"]).strip()

    onunload_bodies = _extract_onunload_bodies(combined_code)
    detach_in_onunload = any("detachLeavesOfType" in body for body in onunload_bodies)

    node_imports: set[str] = set()
    for mod in re.findall(r"""(?:from|\bimport|require\s*\()\s*['"]([^'"]+)['"]""", combined_code):
        if mod == "electron" or mod.startswith("node:") or mod.split("/")[0] in NODE_BUILTINS:
            node_imports.add(mod)

    command_ids = re.findall(
        r"""addCommand\s*\(\s*\{[^}]*?\bid\s*:\s*['"]([^'"]+)['"]""",
        combined_code,
        flags=re.S,
    )
    prefixed_command_ids = [cid for cid in command_ids if cid.startswith(plugin_id)]

    default_hotkeys_declared = bool(
        re.search(r"""addCommand\s*\(\s*\{[\s\S]{0,400}?\bhotkeys\s*:\s*\[""", combined_code)
    )

    imported_host_modules = set(re.findall(r"""['"]((?:@codemirror|@lezer)/[^'"]+)['"]""", combined_code))
    imports_codemirror = bool(imported_host_modules)
    cm_externals_present = all(mod in externals or mod.split("/")[0] + "/*" in externals for mod in imported_host_modules)

    uses_raw_inner_html = bool(
        re.search(
            r"(\.\s*(?:innerHTML|outerHTML)\s*=|\binsertAdjacentHTML\s*\(|\bdangerouslySetInnerHTML\b)",
            combined_code,
        )
    )
    uses_global_app = bool(re.search(r"\b(?:window|globalThis)(?:\s+as[^;\n]{0,120}\))?\s*\.app\b", combined_code))

    uses_raw_heading_in_settings = bool(
        combined_settings_code
        and re.search(r"""createEl\s*\(\s*['"]h[1-6]['"]""", combined_settings_code)
        and "setHeading" not in combined_settings_code
    )

    uses_vault_create = bool(re.search(r"""vault\.on\s*\(\s*['"]create['"]""", combined_code))
    has_on_layout_ready = "onLayoutReady" in combined_code

    uses_vault_rename_directly = bool(re.search(r"\bvault\.rename\s*\(", combined_code))
    uses_vault_delete_or_trash = bool(re.search(r"\bvault\.(?:delete|trash)\s*\(", combined_code))
    uses_deprecated_render_markdown = bool(re.search(r"\bMarkdownRenderer\.renderMarkdown\s*\(", combined_code))

    uses_fetch = bool(re.search(r"(?<![.\w])fetch\s*\(", combined_code))
    uses_request_url = "requestUrl" in combined_code

    uses_react_create_root = "createRoot" in combined_code
    has_react_unmount = ".unmount(" in combined_code

    css_uses_vars = "var(--" in combined_css
    css_hardcoded_hex_count = len(re.findall(r"#[0-9a-fA-F]{3,8}\b", combined_css))

    versions_matches_manifest = (
        versions is not None and versions.get(plugin_version) == min_app_version
    )

    signals: dict[str, Any] = {
        "plugin_id": plugin_id,
        "plugin_id_valid_format": bool(PLUGIN_ID_RE.fullmatch(plugin_id)) and not plugin_id.endswith("plugin"),
        "plugin_id_contains_obsidian": "obsidian" in plugin_id.lower(),
        "plugin_name_contains_obsidian": "obsidian" in plugin_name.lower(),
        "version_valid_semver": bool(SEMVER_RE.match(plugin_version)),
        "min_app_version_valid_semver": bool(SEMVER_RE.match(min_app_version)),
        "description_length": len(description),
        "description_ends_with_punctuation": description.endswith((".", "!", "?")),
        "is_desktop_only": is_desktop_only,
        "source_files_present": bool(source_files),
        "versions_present": versions is not None,
        "versions_invalid_entry_count": invalid_version_entries,
        "versions_matches_manifest": versions_matches_manifest,
        "has_eslint_plugin_obsidianmd": "eslint-plugin-obsidianmd" in all_deps,
        "externalizes_obsidian": "obsidian" in externals,
        "imports_codemirror": imports_codemirror,
        "externalizes_codemirror": cm_externals_present,
        "has_prod_sourcemap_disabled": bool(
            re.search(r"sourcemap\s*:\s*prod\s*\?\s*false", bundler_combined)
            or "sourcemap: false" in bundler_combined
        ),
        "has_hotreload_marker": ".hotreload" in bundler_combined or (root / ".hotreload").exists(),
        "detach_leaves_in_onunload": detach_in_onunload,
        "uses_global_window_app": uses_global_app,
        "uses_raw_inner_html": uses_raw_inner_html,
        "uses_raw_heading_in_settings": uses_raw_heading_in_settings,
        "prefixed_command_ids": prefixed_command_ids,
        "default_hotkeys_declared": default_hotkeys_declared,
        "node_or_electron_imports": sorted(node_imports),
        "uses_fetch": uses_fetch,
        "uses_request_url": uses_request_url,
        "uses_vault_create_without_layout_ready": uses_vault_create and not has_on_layout_ready,
        "uses_vault_rename_directly": uses_vault_rename_directly,
        "uses_vault_delete_or_trash": uses_vault_delete_or_trash,
        "uses_deprecated_render_markdown": uses_deprecated_render_markdown,
        "uses_register_helpers": bool(
            re.search(r"\bthis\.(?:register|registerEvent|registerDomEvent|registerInterval|registerView)\b", combined_code)
        ),
        "uses_react_create_root": uses_react_create_root,
        "has_react_unmount": has_react_unmount,
        "webgl_has_resize_observer": "ResizeObserver" in combined_code,
        "webgl_has_visibility_guard": bool(
            re.search(r"\b(visibilitychange|visibilityState|IntersectionObserver|windowVisibility|hidden)\b", combined_code)
        ),
        "webgl_has_dispose": ".dispose(" in combined_code,
        "css_present": bool(css_files),
        "css_uses_obsidian_variables": css_uses_vars,
        "css_hardcoded_hex_count": css_hardcoded_hex_count,
    }

    primary_bundler = bundlers_detected[0] if bundlers_detected else None
    if len(set(bundlers_detected)) > 1:
        primary_bundler = "+".join(sorted(set(bundlers_detected)))

    return {
        "plugin_root_name": root.name,
        "inspected_files": inspected_files,
        "manifest": manifest,
        "versions": versions,
        "scopes": scopes,
        "bundler": primary_bundler,
        "externals": sorted(externals),
        "signals": signals,
        "warnings": warnings,
        "no_data": no_data,
    }
