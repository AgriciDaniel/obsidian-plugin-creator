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
