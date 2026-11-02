# Public distribution policy

This edition distributes first-party code, original editorial summaries, links
to public sources, reviewed generic vault defaults, and synthetic examples.

The public source catalog is `references/public-sources.json`. It is an
allowlisted projection of reviewed source IDs, titles, public URLs, dates,
confidence, original paraphrased claims, and upstream reference metadata. It
contains no private captures, account data, credentials, or internal review
ledger. Source availability alone is not permission to redistribute full works.

The following paths are excluded from this source tree and every release ZIP:

- `.raw/` and `.obsidian/` at any level.
- `hot.md`, `log.md`, `source-ledger.json`, and `claim-ledger.md`.
- The original `references/research/` reports and private verification history.
- Local workspaces, dependency folders, generated user projects, caches, secrets,
  and private operational material.

`Home` and `Activity` are newly authored generic navigation notes, not renamed
private activity history. `assets/vault-defaults/` contains reviewed generic
configuration templates, not an existing user's Obsidian state.

Creating a new working vault generates its private intake store and Obsidian
configuration locally. Those runtime files are user-owned and are never included
in public source packaging. Keep working vaults outside this checkout.

Public source, archive, and credential-pattern checks must pass before release.
Review the exact candidate and its inventory. A passing engineering audit does
not constitute rights clearance, runtime acceptance, commercial validation, or
permission to publish. Publication requires the owner's explicit approval.
