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
