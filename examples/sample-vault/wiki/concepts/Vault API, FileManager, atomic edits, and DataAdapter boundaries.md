---
type: "concept"
title: "Vault API, FileManager, atomic edits, and DataAdapter boundaries"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/concept"
  - "confidence/practitioner"
related:
  - "[[Plugin lifecycle, Component ownership, and cleanup discipline]]"
  - "[[Workspace leaves, custom ItemView dashboards, and deferred views]]"
  - "[[Obsidian Bases API, native dashboards, and query surfaces]]"
  - "[[Source SRC-04-001]]"
  - "[[Source SRC-04-021]]"
  - "[[Source SRC-04-022]]"
  - "[[Source SRC-04-023]]"
  - "[[Source SRC-04-024]]"
  - "[[Source SRC-04-025]]"
  - "[[Source SRC-04-026]]"
  - "[[Source SRC-04-028]]"
  - "[[Source SRC-04-029]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
source_urls:
  - "https://docs.obsidian.md/Plugins/Editor/Editor"
  - "https://docs.obsidian.md/Plugins/Vault"
  - "https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines"
  - "https://docs.obsidian.md/Reference/TypeScript+API/FileManager"
  - "https://docs.obsidian.md/Reference/TypeScript+API/DataAdapter"
  - "https://raw.githubusercontent.com/obsidianmd/eslint-plugin/master/lib/rules/preferFileManagerTrashFile.ts"
  - "https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts"
  - "https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time"
  - "https://docs.obsidian.md/Plugins/Events"
---

# Vault API, FileManager, atomic edits, and DataAdapter boundaries

Treat vault changes as fallible transactions.

## Verified source guidance

Paraphrases from the dated sources below. Repeated upstream origins are consistency checks, not independent corroboration.

### Obsidian Developer Documentation - Editor

- [evidence-based] The Obsidian Editor abstraction exposes selections, cursors, and text replacement without requiring direct CodeMirror access. ([[Source SRC-04-001]])

### Obsidian Developer Documentation - Vault

- [evidence-based] Use cachedRead for display-only reads and read when content will be edited. Vault.process supplies an atomic synchronous read-modify-write operation. ([[Source SRC-04-021]])
- [evidence-based] The Vault API works with visible vault files; DataAdapter provides lower-level access, including hidden paths. ([[Source SRC-04-021]])

### Obsidian Developer Documentation - Plugin guidelines

- [evidence-based] Plugin guidelines prefer Editor APIs for editing the active note, processFrontMatter for frontmatter, and Vault APIs for normal vault files. ([[Source SRC-04-022]])
- [evidence-based] Guidelines recommend direct file lookup APIs, normalizePath for user paths, and safe DOM construction instead of assigning untrusted HTML. ([[Source SRC-04-022]])

### Obsidian TypeScript API Reference - FileManager

- [evidence-based] FileManager.renameFile updates links according to user preferences; generateMarkdownLink also follows link format preferences. ([[Source SRC-04-023]])
- [evidence-based] FileManager.processFrontMatter atomically reads, modifies, and saves frontmatter, and callers must handle errors. ([[Source SRC-04-023]])

### Obsidian TypeScript API Reference - DataAdapter

- [practitioner] DataAdapter provides lower-level file operations using normalized paths; prefer the higher-level Vault API for normal indexed files. ([[Source SRC-04-024]])

### Official eslint-plugin-obsidianmd Rule - prefer-file-manager-trash-file

- [evidence-based] The prefer-file-manager-trash-file rule recommends FileManager.trashFile over Vault.trash and Vault.delete to respect user deletion settings. This rule source does not establish its configured severity. ([[Source SRC-04-025]])

### Obsidian Official TypeScript API Definitions - obsidian.d.ts

- [evidence-based] The official typings expose editorLivePreviewField, editorInfoField, link parsing helpers, and APIs for opening files with editor state. Minimum supported versions must be checked against the target typings. ([[Source SRC-04-026]])

### Obsidian Developer Documentation - Optimize plugin load time

- [evidence-based] Keep onload limited to essential registrations, use a production bundle, and defer substantial startup work through onLayoutReady. Vault create events also fire for existing files during initialization. ([[Source SRC-04-028]])

### Obsidian Developer Documentation - Events

- [evidence-based] Use registerEvent for event references and registerInterval for repeating timers so plugin unload releases them. ([[Source SRC-04-029]])

## Engineering recipe

[practitioner] This sequence applies the cited contracts; it is not a tested plugin implementation.

1. Use the documented Vault and FileManager surfaces for ordinary note operations.
2. Validate paths and re-resolve file identity after user interaction or asynchronous work.
3. Use atomic process-style updates where appropriate; preserve concurrent external edits.
4. Separate a read-only recommendation from any approved write operation and its recovery copy.

## Verification

[practitioner] Simulate rename/delete during a pending task and confirm failed writes preserve source content.

Record app version, operating system, plugin artifact hash, input size, observed outcome, and evidence path in [[Runtime Acceptance Matrix]].

## Limits

This brain has no physical-device result for this recipe. A static scan cannot prove lifecycle correctness, mobile support, rendering performance, or submission acceptance. Refresh policy and API claims before release.

## Sources

- [Obsidian Developer Documentation - Editor](https://docs.obsidian.md/Plugins/Editor/Editor), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - Vault](https://docs.obsidian.md/Plugins/Vault), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian TypeScript API Reference - FileManager](https://docs.obsidian.md/Reference/TypeScript+API/FileManager), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian TypeScript API Reference - DataAdapter](https://docs.obsidian.md/Reference/TypeScript+API/DataAdapter), retrieved 2026-11-01, refresh due 2026-12-01.
- [Official eslint-plugin-obsidianmd Rule - prefer-file-manager-trash-file](https://raw.githubusercontent.com/obsidianmd/eslint-plugin/master/lib/rules/preferFileManagerTrashFile.ts), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Official TypeScript API Definitions - obsidian.d.ts](https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - Optimize plugin load time](https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - Events](https://docs.obsidian.md/Plugins/Events), retrieved 2026-11-01, refresh due 2026-12-01.

## Related

- [[Source SRC-04-001]]
- [[Source SRC-04-021]]
- [[Source SRC-04-022]]
- [[Source SRC-04-023]]
- [[Source SRC-04-024]]
- [[Source SRC-04-025]]
- [[Source SRC-04-026]]
- [[Source SRC-04-028]]
- [[Source SRC-04-029]]
- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[Obsidian Bases API, native dashboards, and query surfaces]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
