# Obsidian Plugin Brain: Security & Refusal Playbook


> Use this playbook before any release to verify safety gates hold.

## When to invoke

- Before tagging a new release.
- After adding any importer, synthesis module, or report renderer.
- After any change to refusal rules in the spec.

## Prerequisites

- `references/safety-gates.md` exists.
- The spec's `refusal_rules` are explicit.

## Step-by-step

1. Audit every importer for shell injection or path traversal.
2. Audit every synthesis module for credential persistence (none allowed).
3. Audit `.gitignore` to ensure `.env`, raw API JSON, and credential files are
   excluded.
4. Run `scripts/package_release.py --release-type market-ready --dry-run` and
   confirm the secret-scan passes.
5. Audit `SKILL.md` for the four required safety phrases: "no credentials",
   "read-only", "rollback", "source".
6. Verify `references/safety-gates.md` enumerates all refusal rules from the
   spec.

## Outputs

- Clean secret scan.
- Updated `references/safety-gates.md` if rules changed.

## Quality gates

- No credentials in repo (grep -r for known token prefixes).
- No mutation of raw sources by importers.
- All refusal rules documented in both SKILL.md and safety-gates.md.

## Sources

- [[No Source No Claim]]
- Spec refusal_rules: 6 declared.
