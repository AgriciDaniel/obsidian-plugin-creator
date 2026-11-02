# Obsidian Plugin Brain Operator Kit

## Public edition

Read the checked-in template or sample as public knowledge snapshots. Create a
separate working vault before private intake or synthesis. The `new` command
initializes its own local intake and reviewed Obsidian configuration. See
[Public distribution](PUBLIC_DISTRIBUTION.md).

## Five-Minute Path

```bash
python3 -m pip install -e .
obsidian-plugin-brain demo
obsidian-plugin-brain lint --vault examples/sample-vault
obsidian-plugin-brain report --vault examples/sample-vault --html-only
```

Open `examples/sample-vault/` in Obsidian and read:

1. `CODEX.md`
2. `wiki/home.md`
3. `wiki/index.md`
4. `wiki/meta/dashboard.md`

## Client Vault

```bash
obsidian-plugin-brain new acme --client-name "Acme Co" --owner "Daniel Agrici" --out-dir ~/obsidian-plugin-brain-vaults
obsidian-plugin-brain ingest --vault ~/obsidian-plugin-brain-vaults/acme --file tests/fixtures/sample-source.md
obsidian-plugin-brain synthesize --vault ~/obsidian-plugin-brain-vaults/acme
obsidian-plugin-brain report --vault ~/obsidian-plugin-brain-vaults/acme --html-only
```

## Plugin Task

In the opened vault, start with `wiki/concepts/Plugin Architecture Matrix.md`.
Select the matching concept and inspect its linked official source notes. For a
real plugin, record actual results in `wiki/flows/Runtime Acceptance Matrix.md`.

From the complete editable source checkout:

```bash
python3 scripts/plugin_review_audit.py --plugin-dir /path/to/plugin --json
python3 tests/test_obsidian_plugin_adapter.py
python3 scripts/build_demo_vault.py --check
```

The static analyzer never executes the inspected repository. It reports bounded
text signals and unknowns; build, official lint, actual Obsidian execution, and
submission acceptance require separate evidence. Standalone wheels omit the
operating assets and are not a supported installation format.

## Research Rule

The initial source review was completed on 2026-11-01. Refresh current official
or primary sources monthly and immediately before releases. Keep stale claims
visibly marked until the actual source is reverified.

Research evidence must be written into `references/public-sources.json` with
source URL, source type, retrieved date, refresh due date, confidence, and claim
coverage. Markdown research notes alone do not satisfy market-ready release.

## Adapter Rule

Domain-adapted status requires `references/adapter-manifest.json` to name real
schemas, importer paths, synthesis modules, report renderers, fixtures, and
tests. Generic scaffold scripts are intentionally capped below market-ready.

## Creator workspace

Open Plugin Creator Studio in the vault and follow docs/CREATOR_GUIDE.md in the source checkout. `starters` lists the eight surfaces; `create-plugin` produces a new local source project from a validated brief. Dry-run creates no directories. The source creator performs no network, dependency installation, generated-plugin execution, active installation, or note writes. Keep the selected source workspace outside active vaults, including custom configurations.
