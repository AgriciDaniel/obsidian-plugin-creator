# Obsidian Plugin Brain: Adapter Playbook


> Use this playbook for the **domain-adapter** role packet. It moves a brain
> from `researched` to `domain-adapted` by replacing generic scripts with
> domain-specific importers, synthesis modules, and report renderers.

## When to invoke

- The brain has a complete source pack but generic adapter scripts.
- `brainstein audit <repo>` returns `status: researched`.
- `references/adapter-manifest.json` is empty or declares `generic_only: true`.

## Prerequisites

- Research gate passed.
- `references/adapter-plan.md` exists with raw input types enumerated.
- Sample fixtures available under `tests/fixtures/`.

## Step-by-step

1. Open `references/adapter-plan.md`; for every raw input type list a schema.
2. Implement `input_schemas/` JSON or YAML schema files.
3. Implement `importers/` Python modules that copy raw sources into
   `.raw/sources/` and update `.raw/.manifest.json`.
4. Implement `synthesis_modules/` that read parsed inputs and produce sourced
   facts, recommendations, and refusals.
5. Implement `report_renderers/` that compile deliverables.
6. Add a fixture for each importer; add a test asserting determinism.
7. Update `references/adapter-manifest.json` with paths for every section.
8. Run `brainstein audit <repo>` - expect `status: domain-adapted`.

## Outputs

- `references/adapter-manifest.json` with `generic_only: false` and populated
  `input_schemas`, `importers`, `synthesis_modules`, `report_renderers`,
  `fixtures`, `tests`.
- All paths in the manifest resolve on disk.
- At least one importer per raw input type: Operator-supplied Obsidian plugin repositories, manifest.json, versions.json, package.json, esbuild or Vite configs, TypeScript source files, styles.css, and startup or heap profile traces.

## Quality gates

- [[Adapter Manifest Standard|Adapter Manifest Standard]] passes.
- All importers idempotent; re-running yields identical manifest hashes.
- No path traversal or secret leakage in importer code.

## Failure modes

- **Importer mutates raw source**: importers MUST copy + hash; never edit
  in place.
- **Manifest path missing**: every entry must resolve; CI rejects otherwise.
- **Synthesis confidently asserts without source**: every recommendation must
  cite a source-ledger or wiki entry.

## Sources

- [[Adapter Manifest Standard]]
- [[Brain Factory Lifecycle]]
