# 010. Vault API, FileManager, atomic edits, and DataAdapter boundaries

Distilled official documentation, retrieved 2026-11-01; confidence: practitioner for the integration recipe. All source statements are labeled paraphrases.

Core thesis: Treat vault changes as fallible transactions.

## How to use it

1. [practitioner] Use the documented Vault and FileManager surfaces for ordinary note operations.
2. [practitioner] Validate paths and re-resolve file identity after user interaction or asynchronous work.
3. [practitioner] Use atomic process-style updates where appropriate; preserve concurrent external edits.
4. [practitioner] Separate a read-only recommendation from any approved write operation and its recovery copy.

## Evidence and caveats

- [Obsidian Developer Documentation - Editor](https://docs.obsidian.md/Plugins/Editor/Editor); retrieved 2026-11-01; source `SRC-04-001`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - Vault](https://docs.obsidian.md/Plugins/Vault); retrieved 2026-11-01; source `SRC-04-021`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines); retrieved 2026-11-01; source `SRC-04-022`; verify the linked source note for exact supported claims.
- [Obsidian TypeScript API Reference - FileManager](https://docs.obsidian.md/Reference/TypeScript+API/FileManager); retrieved 2026-11-01; source `SRC-04-023`; verify the linked source note for exact supported claims.
- [Obsidian TypeScript API Reference - DataAdapter](https://docs.obsidian.md/Reference/TypeScript+API/DataAdapter); retrieved 2026-11-01; source `SRC-04-024`; verify the linked source note for exact supported claims.
- [Official eslint-plugin-obsidianmd Rule - prefer-file-manager-trash-file](https://raw.githubusercontent.com/obsidianmd/eslint-plugin/master/lib/rules/preferFileManagerTrashFile.ts); retrieved 2026-11-01; source `SRC-04-025`; verify the linked source note for exact supported claims.
- [Obsidian Official TypeScript API Definitions - obsidian.d.ts](https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts); retrieved 2026-11-01; source `SRC-04-026`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - Optimize plugin load time](https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time); retrieved 2026-11-01; source `SRC-04-028`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - Events](https://docs.obsidian.md/Plugins/Events); retrieved 2026-11-01; source `SRC-04-029`; verify the linked source note for exact supported claims.

No fabricated quotations or page numbers. Source relationships do not establish independent corroboration. Runtime behavior remains untested here.

## Brain hooks

Folded into [[Vault API, FileManager, atomic edits, and DataAdapter boundaries]]. Verify with [[Runtime Acceptance Matrix]] and [[Claim Verification Flow]].
