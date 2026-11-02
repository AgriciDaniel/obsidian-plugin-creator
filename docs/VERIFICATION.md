# Verification

Public edition 0.2.0, local candidate checked on 2026-11-02. This record applies
to the public source edition. Its own hosted CI has not run because the edition
has not been committed or published.

## Observed local checks

| Check | Evidence class |
| --- | --- |
| Python compilation and regression pipeline | Local execution against the public candidate |
| Static source reviewer | Included positive and negative synthetic repositories |
| Eight creator source types | Deterministic generation and existing creator regressions |
| Public distribution tests | Eight test methods, including tampering and private-path negative controls |
| New working vault | Public catalog captured locally, fresh private manifest, category palette and seven graph bookmarks |
| Local source intake and synthesis | Temporary user vault; product canon remains unchanged |
| Reports and visuals | Actual local generated output |
| Template and sample vault lint | Public catalog hashes, source IDs, links, and frontmatter |
| Demo regeneration | Public file projection checked against retained hashes |
| Installed creator and reviewer | Temporary skill roots, no active agent installation |
| Public source and archive gates | Private paths and credential patterns are blocking |
| Product maturity audit | Internal project rubric; not commercial or runtime acceptance |

The separate [public release check record](../references/verification/public-release-checks.json) contains the final candidate's
observed exit statuses, toolchain result counts, and artifact checks. Public
release ZIP hashes are recorded in `dist/RELEASE_MANIFEST.json` and `dist/SHA256SUMS`
when packaging is run. The review handoff retains the exact file inventory.

## Source and build evidence

The public catalog has 121 entries and 200 original paraphrased claims, reviewed
on 2026-11-01. It retains public URLs, dates, confidence, and upstream references.
These are summaries, not complete upstream page captures. Multiple entries can
share an origin. No independent corroboration is implied by their count.

`references/verification/creator-builds.json` retains the earlier source-bound
compiler, bundle, and official lint observations for the unchanged starter
TypeScript. The public release workbench also reruns all eight starters against
the exact toolchain. Retained results and fresh execution are reported separately.

The exact dependency lock is in `references/creator/toolchain/`. The original
lint toolchain overrides an older Obsidian peer and includes a deprecated ESLint
transitive dependency. This remains a maintenance limitation, not an upstream
compatibility guarantee.

## Repeat the local checks

```bash
python3 -m compileall -q scripts obsidian_plugin_brain tests
python3 tests/test_pipeline.py
python3 scripts/build_demo_vault.py --check
python3 scripts/audit_brain.py --require market-ready --json
python3 scripts/package_release.py --version 0.2.0
```

The market-ready term belongs to the internal rubric. Public publication still
requires the distribution, privacy, rights, and owner approval checks.

## Remaining evidence

The public edition's hosted CI, actual Obsidian interaction, physical iOS and
Android, real-vault performance, accessibility, specific integrations, directory
acceptance, and commercial demand are not established by these local gates.
Each actual plugin needs its own implemented criteria and runtime evidence.
No publication, account change, or installation into an active vault occurred.
