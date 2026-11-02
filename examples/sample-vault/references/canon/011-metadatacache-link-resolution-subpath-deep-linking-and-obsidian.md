# 011. MetadataCache, link resolution, subpath deep-linking, and Obsidian URI

Distilled official documentation, retrieved 2026-11-01; confidence: practitioner for the integration recipe. All source statements are labeled paraphrases.

Core thesis: Resolve links from the source note's context.

## How to use it

1. [practitioner] Use cached metadata and public link-resolution APIs rather than inventing path rules.
2. [practitioner] Treat missing cache entries and unresolved links as ordinary states.
3. [practitioner] Keep headings and block identifiers separate from file paths.
4. [practitioner] Rebuild only affected relationships after file or metadata events.

## Evidence and caveats

- [Obsidian Developer Documentation - Manage plugin lifecycle](https://docs.obsidian.md/Plugins/Guides/Manage+plugin+lifecycle); retrieved 2026-11-01; source `SRC-04-019`; verify the linked source note for exact supported claims.
- [Obsidian TypeScript API Reference - FileManager](https://docs.obsidian.md/Reference/TypeScript+API/FileManager); retrieved 2026-11-01; source `SRC-04-023`; verify the linked source note for exact supported claims.
- [Obsidian Official TypeScript API Definitions - obsidian.d.ts](https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts); retrieved 2026-11-01; source `SRC-04-026`; verify the linked source note for exact supported claims.
- [Obsidian TypeScript API Reference - MetadataCache](https://docs.obsidian.md/Reference/TypeScript+API/MetadataCache); retrieved 2026-11-01; source `SRC-04-027`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - Optimize plugin load time](https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time); retrieved 2026-11-01; source `SRC-04-028`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - Events](https://docs.obsidian.md/Plugins/Events); retrieved 2026-11-01; source `SRC-04-029`; verify the linked source note for exact supported claims.

No fabricated quotations or page numbers. Source relationships do not establish independent corroboration. Runtime behavior remains untested here.

## Brain hooks

Folded into [[MetadataCache, link resolution, subpath deep-linking, and Obsidian URI]]. Verify with [[Runtime Acceptance Matrix]] and [[Claim Verification Flow]].
