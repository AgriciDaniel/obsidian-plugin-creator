# Obsidian Plugin Brain: Vault Architecture Playbook


> Use this playbook for the **vault-architect** role packet. It keeps the
> Obsidian vault graph clean and the wikilinks resolvable.

## When to invoke

- After bulk doctrine additions.
- Before a release (vault hygiene is a release gate).
- When `lint_vault.py` reports >5 issues.

## Prerequisites

- `wiki/` exists with at least one note per folder.
- `wiki/rubric/Brain Anatomy Rubric.md` defines the frontmatter contract.

## Step-by-step

1. Run `python brainstein-brain/scripts/lint_vault.py --vault <path> --strict`.
2. For every dead wikilink, either fix the target name or create the missing
   note.
3. For every missing frontmatter field, add `type`, `title`, `created`,
   `updated`, `status`.
4. For every empty note, either populate or delete.
5. Run `brainstein audit <repo> --no-strict-vault` then `--strict-vault`; both
   must pass.

## Outputs

- Zero dead wikilinks across `wiki/`.
- Frontmatter compliant on every note.
- `.obsidian/graph.json` with `colorGroups` mapping folders to colors.

## Sources

- [[Brain Anatomy Rubric|Anatomy rubric - vault category]]
- [[Quality Gate Matrix]]
