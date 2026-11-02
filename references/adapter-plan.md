# Adapter Plan

Implemented and locally tested on 2026-11-01. The zero-dependency adapter reads an existing plugin repository in place and executes none of its code.

## Supported inputs

- Required manifest.json with supported metadata fields.
- Optional versions.json, package.json, and recognized bundler configurations.
- Bounded TypeScript, JavaScript, Svelte, Vue, and CSS source text.

The adapter recognizes static text patterns. Dynamic configuration, generated code, aliases, wrappers, and semantic relationships require manual review. Heap profiles and startup traces are operator evidence, not parsed input types in V1.

## Implemented surfaces

- Importer: `obsidian_plugin_brain/importers/plugin_repo.py`
- Synthesis: `obsidian_plugin_brain/synthesis/review_health.py`
- Rule catalog: `references/schemas/review-rules-catalog.json`
- Report: `obsidian_plugin_brain/reports/readiness_report.py`
- CLI: `scripts/plugin_review_audit.py` and `review-plugin`
- Fixtures and negative tests: `tests/test_obsidian_plugin_adapter.py`

## Contract

A clear result is `static-signals-clear`; release readiness stays unverified. Missing source, bundler, or compatibility evidence yields unknown or a warning. Unsafe symlinks and oversized scans fail closed. Unrecognized manifest metadata is excluded from output. Findings link to source IDs and official URLs.

The supported delivery is a complete editable source checkout. Actual builds, official lint, Obsidian runtime, mobile devices, and submission acceptance are outside this adapter's evidence class.
