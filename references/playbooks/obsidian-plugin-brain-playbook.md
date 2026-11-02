# Obsidian Plugin Brain: End-to-End Playbook

> Full chain: research → adapter → demo → release for the `obsidian-plugin-brain` brain.

## Stage 1 - Research

# Obsidian Plugin Brain: Research Playbook


> Use this playbook when running the **research-scout** role packet. It moves a brain
> from `scaffolded` to `researched` by filling the source pack and locking
> dated, official/primary sources.

## When to invoke

- The brain is at maturity `scaffolded` or has stale `refresh_due` entries.
- A high-stakes (accounting, tax, legal, medical, finance, compliance, security) or
  fast-moving (ads, platforms, APIs, social, AI) domain is in scope.
- `brainstein research-audit` reports placeholder content in `references/`.

## Prerequisites

- `specs/<slug>.yaml` exists and validates with `brainstein validate`.
- `references/research-plan.md` exists (written by `brainstein research-plan`).
- Operator has read access to the source materials enumerated in the spec's
  `raw_sources` and `enrichment_sources`.

## Step-by-step

1. Open `references/research-plan.md` and confirm the buyer questions and
   official-source checklist for this domain.
2. For each official/primary source, capture: URL, retrieval date, version,
   confidence, and 2-3 claims. Write to `references/public-sources.json`.
3. Update `references/current-requirements.md` with dated bullets pointing to
   source-ledger entries.
4. Update `references/market-research.md` with practitioner / market signals.
5. Run `brainstein research-audit <repo>` and resolve every critical failure.
6. Update `wiki/activity.md` with the date and the list of new sources.

## Outputs

- `references/public-sources.json` with ≥2 official sources (high-stakes/fast-moving)
  or ≥1 (stable domain), each with `retrieved`, `refresh_due`, `source_type`, and
  `claims`.
- `references/current-requirements.md` with no placeholders.
- `wiki/sources/*` notes (one per source) with frontmatter and wikilinks.

## Quality gates

- [[Quality Gate Matrix|Quality Gate Matrix]] entry: **Research Gate**.
- All dated claims cite a source-ledger entry.
- No URL points to `example.com`, `localhost`, or similar placeholder hosts.

## Failure modes

- **Source paywalled or unavailable**: capture archive.org snapshot, mark
  `confidence: low`, and add a refresh task in orchestration.
- **Contradictory official sources**: split into `claims` array with both;
  add a [[risks/_index|risk]] note.
- **Stale `refresh_due`**: a future-dated `refresh_due` ≤ today triggers
  research-audit failure. Refresh or remove.

## Sources

- [[No Source No Claim|No Source No Claim doctrine]]
- [[researching-a-domain|Researching a domain playbook]]
- Safety risks driving stricter sourcing: Stale Obsidian API or submission review claims due to new desktop, mobile, or Bases releases, DOM XSS vulnerabilities when rendering untrusted Markdown, frontmatter, JSONL traces, or external responses via innerHTML, Mobile crashes on iOS and Android caused by unguarded Node.js or Electron imports when isDesktopOnly is false.


## Stage 2 - Adapter

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


## Stage 3 - Demo verification

# Obsidian Plugin Brain: Demo Verification Playbook


> Use this playbook for the **demo-verifier** role packet. It moves a brain
> from `domain-adapted` to `demo-verified` by proving the pipeline is
> deterministic end-to-end.

## When to invoke

- Adapters are real, tests pass locally, but `examples/sample-vault/` has not
  been regenerated under a pinned reference date.
- CI does not yet enforce sample-vault hash determinism.

## Prerequisites

- Adapter gate passed.
- `tests/fixtures/sample-vault.sha256` may exist (will be rewritten on first
  successful run).

## Step-by-step

1. Choose a representative spec (typically the highest-stakes domain).
2. Run `python scripts/regenerate_sample_vault.py --spec specs/<slug>.yaml --out examples/sample-vault/ --reference-date 2026-05-17 --seed 42`.
3. Inspect the output for shape (deliverables, frontmatter, manifest hashes).
4. Compute the SHA256 manifest of the vault tree; commit to
   `examples/sample-vault/.manifest-sha256.json` and the top-level hash to
   `tests/fixtures/sample-vault.sha256`.
5. Re-run regeneration; assert byte-identical output (use `diff -rq`).
6. Add `tests/test_sample_vault.py` with `test_manifest_matches_committed`.
7. Add a CI job that runs the regenerator and diffs against committed.
8. Run `brainstein audit <repo>` - expect `status: demo-verified`.

## Outputs

- `examples/sample-vault/` with full structure and produced deliverables:
  Plugin scope and architecture decision matrix mapping product goals to Obsidian API surfaces, Community Store submission and eslint-plugin readiness scorecard, Lifecycle, memory-leak, and deferred-view audit checklist, Visuals, dashboards, Bases, and 3D WebGL engineering runbook, CodeMirror 6 Live Preview and Reading view parity guide.
- `tests/fixtures/sample-vault.sha256` (single line, 64-hex).
- `.github/workflows/ci.yml` job `sample-vault-determinism` green.

## Quality gates

- Determinism job green across Linux, macOS, Windows × Python 3.11/3.12.
- No PDF binary differences (CreationDate/ModDate stripped or markdown-only).
- `.gitattributes` forces `* text eol=lf`.

## Failure modes

- **Hash drift on Windows**: ensure `.gitattributes` and explicit `\n` writes.
- **Random ordering**: every JSON dump uses `sort_keys=True`.
- **Timestamps**: every date stamp pulled from `--reference-date` propagation.

## Sources

- [[Brain Factory Lifecycle]]
- [[Maturity Contract]]


## Stage 4 - Release

# Obsidian Plugin Brain: Market-Ready Release Playbook


> Use this playbook for the **release-gate** role packet. It moves a brain
> from `demo-verified` to `market-ready` and produces a signed release zip.

## When to invoke

- Demo gate passed.
- All 29 anatomy items are at least medium-coverage.
- The brand-and-legal cluster (CHANGELOG, NOTICES, SKILL.md allowed-tools) is the
  remaining gap.

## Prerequisites

- `brainstein audit-brain <repo>` returns grade `SS` or `S` (close to SSS+).
- Operator has GPG signing key available if signing release artifacts.

## Step-by-step

1. Date `CHANGELOG.md` top entry with today's ISO date; use Keep-a-Changelog.
2. Populate `THIRD_PARTY_NOTICES.md` (or declare zero deps explicitly, ≥200
   bytes).
3. Add a minimal `allowed-tools` line to the `SKILL.md` frontmatter.
4. Bump `pyproject.toml` version to match the tag.
5. Run `brainstein audit-brain <repo> --strict` - must return SSS+.
6. Run all CI jobs on a tagged ref; all must be green.
7. Tag `git tag v<version>`.
8. Run `python scripts/package_release.py --version <version> --release-type market-ready`.
9. Verify the release zip + manifest + SHA256SUMS match the source tree.

## Outputs

- `dist/<slug>-<version>.zip` plus `RELEASE_MANIFEST.json` and `SHA256SUMS`.
- Git tag `v<version>` pointing to a clean working tree.
- `CHANGELOG.md` top entry with real ISO date.

## Quality gates

- Privacy grep returns zero hits in shipped artifacts (no references to
  private brain skills).
- All anatomy rubric categories ≥ 70% of their max weight.
- No critical audit failures.

## Failure modes

- **Tag/pyproject/plugin version mismatch**: `semver-tag-match` CI job blocks.
- **Stale CHANGELOG date**: `audit-brain` flags the `YYYY-MM-DD` placeholder.
- **Untracked drift**: `package_release.py` rejects if git working tree dirty.

## Sources

- [[Quality Gate Matrix]]
- [[Maturity Contract]]


---

## Domain-specific notes

- Slug: `obsidian-plugin-brain`
- Domain: Architecting, building, styling, optimizing, testing, auditing, and shipping Obsidian plugins across all plugin scopes: core commands, multi-pane dashboards and Bases views, 2D and 3D WebGL visuals and canvases, CodeMirror 6 editor extensions, Markdown processors, vault and MetadataCache engines, mobile compatibility, and Community Store releases.
- Buyer: Indie makers, developer-creators, tool builders, and AI engineering teams who build vault-specific or Community Store Obsidian plugins and need source-cited official APIs, review rules, and scope-specific architecture patterns instead of outdated forum folklore.
- Owner: Daniel Agrici

### Workflows
- Plugin scope classification and architecture selection across commands, custom views, Bases views, 2D and 3D visuals, CodeMirror 6 extensions, Markdown processors, and vault indexers
- Lifecycle, Component ownership, and cleanup design for onload, onunload, registered events, intervals, and deferred workspace leaves
- Dashboard, ItemView, Bases view, modal, suggest, and settings UX engineering with theme-native Obsidian CSS variables
- 2D Canvas, SVG, and 3D WebGL or Three.js visual engineering with ResizeObserver sizing, tab-visibility render throttling, and GPU disposal
- Editor and Markdown pipeline engineering across Source mode, Live Preview (CodeMirror 6), and Reading view post-processors
- Vault, FileManager, MetadataCache, atomic background edits, and deep subpath or URI interlinking
- Cross-platform mobile hardening (iOS and Android), startup performance profiling, Sync-safe storage, and XSS security review
- Pre-submission static review against obsidianmd/eslint-plugin, obsidian-releases bot checks, versions.json parity, and GitHub Actions release packaging

### Refusal rules
- No unsourced Obsidian API, submission policy, or version claims
- No guidance that violates official Obsidian Plugin Guidelines such as calling detachLeavesOfType in onunload or injecting unsanitized innerHTML
- No recommendation to bundle duplicate @codemirror/* or obsidian runtime modules into main.js
- No credentials, API keys, sync tokens, or private vault content in repo artifacts or sample fixtures
- No account, registry, or host-system mutation in V1
- No irreversible recommendation without owner, confidence, source, and rollback note

### Safety risks
- Stale Obsidian API or submission review claims due to new desktop, mobile, or Bases releases
- DOM XSS vulnerabilities when rendering untrusted Markdown, frontmatter, JSONL traces, or external responses via innerHTML
- Mobile crashes on iOS and Android caused by unguarded Node.js or Electron imports when isDesktopOnly is false
- Obsidian Sync corruption or quota failures caused by writing large indexes or caches into .obsidian/plugins/<id>/data.json
- Memory leaks, detached DOM trees, and background WebGL GPU drain when views close or hide without disposal
- Secret leakage when storing plaintext API keys inside git-tracked vault plugin data files
