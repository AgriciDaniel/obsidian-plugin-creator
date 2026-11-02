# Current Requirements

Verified 2026-11-01; refresh due 2026-12-01 and immediately before a release.

The source ledger contains 121 dated entries covering lifecycle, custom views, Bases, UI, Canvas, WebGL, CodeMirror, Markdown, vault metadata, mobile, security, builds, and submission. Source statements are paraphrases with confidence markers.

## Material requirements

- [evidence-based] Manage plugin resources and avoid detaching leaves in unload. See [plugin guidelines](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md) and source `SRC-01-001`.
- [evidence-based] Use the current directory dashboard submission workflow. The official submission guide is source `SRC-01-004`; historical registry pull requests are not the complete current workflow.
- [evidence-based] Local recommended lint settings differ from community scanner severities. See `SRC-01-006`; run the actual configured lint rather than deriving acceptance from a regex scanner.
- [practitioner] Verify the API's declared introduction version and the actual minimum app version before choosing Bases, secrets, or declarative settings. Refer to pinned public typings and the feature guide.
- [practitioner] Keep sources, static fixture results, desktop runtime, physical devices, and submission acceptance as separate evidence classes.

## Evidence limits

The retrieval reports preserve source URLs, timestamps, and supported claims. Complete upstream documents are not bundled. A source hash records the body fetched by the researcher where supplied; it is not a measurement of runtime behavior. Multiple pages from the same vendor are not independent corroboration. Every claim in the claim ledger remains SINGLE-SOURCE until a specific second-source check is retained.

## Refresh procedure

Review changes at each source URL, verify affected claims, retain a new immutable research report, update the ledger and claim ledger, compile the vault, then rerun tests and both audits. Do not change an old capture to make it match a new source.
