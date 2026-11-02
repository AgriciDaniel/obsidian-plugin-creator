# Public edition

The public edition preserves the creator, source reviewer, linked knowledge,
vault creation, intake, synthesis, reports, and visual tools. It contains 121
reviewed public source entries and 200 original paraphrased claims, from the
research snapshot dated 2026-11-01.

## Public provenance

`references/public-sources.json` is the product's public reference catalog.
The creator and reviewer bind their source IDs to that catalog. The public
vaults carry byte-identical copies and a `PUBLIC_VAULT.json` hash marker. Vault
lint rejects missing, changed, or malformed public provenance.

The original research captures, internal ledgers, operational history, and
private repository history are omitted. Public notes cite official URLs and
their review dates directly. Entries sharing an upstream work do not establish
independent corroboration. The dates are retained evidence dates, not a claim
that this release performed a new live research review.

## Working vaults

Create a new, separate working vault with the `new` command. It copies the
public knowledge, creates an immutable local snapshot of the public catalog,
initializes a fresh private intake manifest, and applies reviewed generic
Obsidian defaults, including the note-type palette and seven generic graph bookmarks. The shared domain color is a final fallback. No existing active vault is overwritten by this workflow
unless the caller separately invokes the existing explicit force option.

The checked-in template and sample remain public source snapshots. They can be
read directly in Obsidian. To ingest, synthesize, and maintain your own knowledge,
use the separate working vault. Never put private sources into this checkout.

Navigation uses `wiki/home.md` and `wiki/activity.md`. Agent entrypoints and
workflow links follow those names. These generic public notes contain no copied
private operational history.

## Packaging and checks

The release packager excludes private runtime paths from source, template,
sample, and starter ZIPs. It also rejects a contaminated source tree before
packaging and rejects forbidden entries during ZIP verification.

The Python pipeline verifies a new working vault, local ingestion and synthesis,
immutable public-catalog provenance, reports, graph configuration, deterministic
public demo regeneration, installed creator/reviewer commands, and archives.
Separate negative controls exercise private paths, tampered provenance, ZIP
entries, and credential patterns.

The public source snapshot is compiled from reviewed first-party material.
Private research compilation and its historical inputs are maintainer-only.
Refreshing product knowledge requires a reviewed catalog and corresponding
source-note update, fresh catalog hashes, and repeated checks.

## Release limits

A generated starter is not an implemented arbitrary plugin. Actual Obsidian
behavior, physical-device compatibility, accessibility, integration security,
and directory acceptance require evidence for the specific plugin artifact.
The public edition's own hosted CI remains unverified until it is published and
runs there. Canonical private CI results are not public-edition CI results.
