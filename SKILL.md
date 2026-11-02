---
name: obsidian-plugin-brain
description: >
  Source-cited advisory brain for scoping, engineering, and reviewing Obsidian
  plugins across commands, custom views, Bases, visuals, CodeMirror, Markdown,
  vault metadata, mobile, security, and release workflows. Use for Obsidian
  Plugin Brain, Obsidian Plugin Creator, creating plugins, product briefs, architecture,
  source refresh, local source generation, and read-only repository review.
argument-hint: "create-plugin | starters | review-plugin | new | ingest | synthesize | report | visuals | lint | next"
allowed-tools: Read Grep Glob Bash(python3 scripts/create_plugin.py *) Bash(python3 scripts/lint_vault.py *) Bash(python3 scripts/audit_brain.py *) Bash(python3 scripts/guide_next_action.py *)
license: Apache-2.0
---

# Obsidian Plugin Creator

Operate the deployed vault first. Treat `CODEX.md`, `wiki/home.md`, and
`wiki/index.md` as vault-root-relative paths, where the vault root is the
directory passed to `--vault` or opened in Obsidian. In this repo, the template
vault root is `assets/template-brain/` and the demo vault root is
`examples/sample-vault/`.

Secretary: use `agents/obsidian-plugin-secretary.md` for grounded answers, claim review,
and vault maintenance. That secretary reads the brain first, cites a vault note
and an official URL, and stays advisory and read-only.

## Creator Routing

Start with `<vault>/wiki/meta/Plugin Creator Studio.md`. Use the product brief,
architecture/API contract, UX, data/integration, implementation, verification,
release/maintenance, debugging, and advanced-surface playbooks as needed.

- A question or problem description calls for assessment. Do not change a plugin
  until the user asks for implementation.
- A planning request produces the brief, architecture decision, and acceptance
  plan. Make routine choices and state their tradeoffs.
- An explicit creation request may generate new source artifacts in the selected
  workspace. Infer routine metadata; ask one question only when the answer changes
  material work. Never overwrite or install into an active vault.
- An implementation request uses the generated project's contract and completes
  its actual product criteria. A starter is only a starting example.
- A review request uses the source-bound static scanner and reports its limits.
- A release request prepares exact assets and evidence; ask immediately before
  commit, push, publication, submission, account changes, or active-vault installation.

```bash
python3 -m obsidian_plugin_brain starters
python3 -m obsidian_plugin_brain create-plugin --brief references/creator/example-brief.json --out created-projects/heading-compass --dry-run
```

Remove `--dry-run` to create the source artifact. `--workspace` explicitly selects
an existing parent boundary; output must be new and below it. Generation is offline,
refuses symlinks/overwrite and known vault markers, and writes a hash receipt.
It performs no npm installation, generated plugin execution, note mutation, or
active-plugin installation. Custom vault configurations still require careful
workspace selection. Recovery applies only to newly generated artifacts after
checking their receipt and preserving subsequent user edits.

## Start With A Plugin Task

Read `wiki/concepts/Plugin Architecture Matrix.md` in the selected vault, then
read the matching concept and its source notes. Record actual execution in
`wiki/flows/Runtime Acceptance Matrix.md`. Research is dated 2026-11-01 and
refreshes monthly or before a release. The source pack contains 121 entries;
entries can share an upstream origin and are not independent corroboration.

Read-only source-checkout review:

```bash
python3 scripts/plugin_review_audit.py --plugin-dir <plugin-repo> --json
python3 -m obsidian_plugin_brain review-plugin --plugin-dir <plugin-repo> --strict
```

A clear result means only that the implemented static signals found no blocking
pattern. The tool does not execute TypeScript, official lint, Obsidian, physical
devices, or a submission review. Missing evidence is unknown.

## Commands

```bash
/obsidian-plugin-brain new <client-slug> --owner <name>
/obsidian-plugin-brain ingest --vault <path> --file <source>
/obsidian-plugin-brain synthesize --vault <path>
/obsidian-plugin-brain report --vault <path>
/obsidian-plugin-brain visuals --vault <path>
/obsidian-plugin-brain lint --vault <path>
/obsidian-plugin-brain next --vault <path>
```

Source checkout equivalent:

```bash
obsidian-plugin-brain new <client-slug> --owner <name>
obsidian-plugin-brain ingest --vault <path> --file <source>
obsidian-plugin-brain synthesize --vault <path>
obsidian-plugin-brain report --vault <path> --html-only
```

## Required Operating Rules

1. Read `<vault>/CODEX.md`.
2. Read `<vault>/wiki/home.md`.
3. Read `<vault>/wiki/index.md`.
4. Preserve `.raw/` as immutable source material.
5. Never store credentials in the vault.
6. Never make domain-specific claims without dated trustworthy sources.
7. Keep `home`, `index`, `overview`, and `activity` current.
8. Record research evidence in `references/public-sources.json`.
9. Record domain adapter completion in `references/adapter-manifest.json`.

## Script Mapping

- `create-plugin` -> `python3 scripts/create_plugin.py`
- `starters` -> `python3 scripts/create_plugin.py --list`

- `new` -> `python3 scripts/scaffold_vault.py`
- `ingest` -> `python3 scripts/ingest_source.py`
- `synthesize` -> `python3 scripts/synthesize_brain.py`
- `report` -> `python3 scripts/render_brain_report.py`
- `visuals` -> `python3 scripts/generate_vault_visuals.py`
- `lint` -> `python3 scripts/lint_vault.py`
- `next` -> `python3 scripts/guide_next_action.py`

## Quality Gates

- No unsourced Obsidian API, submission policy, or version claims
- No guidance that violates official Obsidian Plugin Guidelines such as calling detachLeavesOfType in onunload or injecting unsanitized innerHTML
- No recommendation to bundle duplicate @codemirror/* or obsidian runtime modules into main.js
- No credentials, API keys, sync tokens, or private vault content in repo artifacts or sample fixtures
- No account, registry, or host-system mutation in V1
- No irreversible recommendation without owner, confidence, source, and rollback note

Do not call this brain market-ready unless `scripts/audit_brain.py --require
market-ready` passes. A scaffold is not a finished brain.

## Research Refresh

monthly for docs.obsidian.md, obsidian.md/changelog, obsidian-api typings, eslint-plugin rules, and obsidian-releases submission policies; on-release for major Obsidian desktop and mobile updates
