# Product Boundaries

Version 0.2.0 adds explicit local source artifact generation to the advisory brain.

Obsidian Plugin Creator supplies researched engineering guidance, product
playbooks, a read-only repository reviewer, and a bounded offline source generator.
The existing `obsidian-plugin-brain` commands remain compatible.

## It Does

- Preserve raw sources under `.raw/`.
- Generate a new local source artifact from an explicit brief, output, and workspace.
- Refuse overwrite, symlink destinations, hidden configuration destinations, and detectable active/deployed vault markers.
- Synthesize source-cited notes and deliverables.
- Maintain action queues, reports, and next actions.
- Keep decisions auditable through source links and rollback notes.
- Gate maturity through `references/public-sources.json`,
  `references/adapter-manifest.json`, and `scripts/audit_brain.py`.

## It Does Not

- No unsourced Obsidian API, submission policy, or version claims
- No guidance that violates official Obsidian Plugin Guidelines such as calling detachLeavesOfType in onunload or injecting unsanitized innerHTML
- No recommendation to bundle duplicate @codemirror/* or obsidian runtime modules into main.js
- No credentials, API keys, sync tokens, or private vault content in repo artifacts or sample fixtures
- No account, registry, or host-system mutation in V1
- No irreversible recommendation without owner, confidence, source, and rollback note

## Safety Risks

- Stale Obsidian API or submission review claims due to new desktop, mobile, or Bases releases
- DOM XSS vulnerabilities when rendering untrusted Markdown, frontmatter, JSONL traces, or external responses via innerHTML
- Mobile crashes on iOS and Android caused by unguarded Node.js or Electron imports when isDesktopOnly is false
- Sync traffic, conflicts, and storage constraints when large derived caches are stored with plugin settings
- Memory leaks, detached DOM trees, and background WebGL GPU drain when views close or hide without disposal
- Secret leakage when storing plaintext API keys inside git-tracked vault plugin data files

## Source Generation Contract

Generation performs no network call, dependency installation, generated plugin
execution, note mutation, active-vault installation, commit, push, or publication.
The workspace is an explicit boundary and outputs must be new. Custom vault
configuration cannot be inferred reliably, so the selected workspace must be a
source workspace outside active vaults.

Dry-run renders the receipt without creating directories. A successful generation
records a SHA256 for every generated file. To recover, compare those hashes and
remove only unchanged newly generated artifacts after preserving any later user
edits. There is no automatic delete or force-overwrite function.

Brain release packaging excludes node_modules, created-projects, and directories
marked with CREATOR_RECEIPT.json, including projects generated at other paths.
Actual plugin distribution requires its own explicit release workflow.

## Maturity Boundary

Market-ready quality requires current
research, domain adapters, deterministic demo verification, source citations,
Obsidian graph hygiene, and release scans. The audit score is capped below 90
until those stages are complete.

## Public source edition

The public catalog replaces the private internal ledger as the source binding
for generation and review. The public source tree and archives exclude raw
captures, live Obsidian state, and private operational notes. New working vaults
create their own private state locally. Home and Activity are generic public
navigation notes; no private history was copied into them.
