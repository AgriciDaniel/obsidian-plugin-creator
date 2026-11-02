---
type: "concept"
title: "MetadataCache, link resolution, subpath deep-linking, and Obsidian URI"
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
  - "[[Source SRC-04-019]]"
  - "[[Source SRC-04-023]]"
  - "[[Source SRC-04-026]]"
  - "[[Source SRC-04-027]]"
  - "[[Source SRC-04-028]]"
  - "[[Source SRC-04-029]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
source_urls:
  - "https://docs.obsidian.md/Plugins/Guides/Manage+plugin+lifecycle"
  - "https://docs.obsidian.md/Reference/TypeScript+API/FileManager"
  - "https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts"
  - "https://docs.obsidian.md/Reference/TypeScript+API/MetadataCache"
  - "https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time"
  - "https://docs.obsidian.md/Plugins/Events"
---

# MetadataCache, link resolution, subpath deep-linking, and Obsidian URI

Resolve links from the source note's context.

## Verified source guidance

Paraphrases from the dated sources below. Repeated upstream origins are consistency checks, not independent corroboration.

### Obsidian Developer Documentation - Manage plugin lifecycle

- [evidence-based] Component registration helpers attach child components, event handlers, DOM listeners, and intervals to an owner lifecycle. ([[Source SRC-04-019]])

### Obsidian TypeScript API Reference - FileManager

- [evidence-based] FileManager.renameFile updates links according to user preferences; generateMarkdownLink also follows link format preferences. ([[Source SRC-04-023]])
- [evidence-based] FileManager.processFrontMatter atomically reads, modifies, and saves frontmatter, and callers must handle errors. ([[Source SRC-04-023]])

### Obsidian Official TypeScript API Definitions - obsidian.d.ts

- [evidence-based] The official typings expose editorLivePreviewField, editorInfoField, link parsing helpers, and APIs for opening files with editor state. Minimum supported versions must be checked against the target typings. ([[Source SRC-04-026]])

### Obsidian TypeScript API Reference - MetadataCache

- [evidence-based] MetadataCache provides resolved and unresolved link maps, getFileCache, and getFirstLinkpathDest. Its changed event does not cover renames, so rename handling requires a Vault event. ([[Source SRC-04-027]])

### Obsidian Developer Documentation - Optimize plugin load time

- [evidence-based] Keep onload limited to essential registrations, use a production bundle, and defer substantial startup work through onLayoutReady. Vault create events also fire for existing files during initialization. ([[Source SRC-04-028]])

### Obsidian Developer Documentation - Events

- [evidence-based] Use registerEvent for event references and registerInterval for repeating timers so plugin unload releases them. ([[Source SRC-04-029]])

## Engineering recipe

[practitioner] This sequence applies the cited contracts; it is not a tested plugin implementation.

1. Use cached metadata and public link-resolution APIs rather than inventing path rules.
2. Treat missing cache entries and unresolved links as ordinary states.
3. Keep headings and block identifiers separate from file paths.
4. Rebuild only affected relationships after file or metadata events.

## Verification

[practitioner] Check duplicate basenames, relative links, aliases, headings, blocks, rename, and deletion.

Record app version, operating system, plugin artifact hash, input size, observed outcome, and evidence path in [[Runtime Acceptance Matrix]].

## Limits

This brain has no physical-device result for this recipe. A static scan cannot prove lifecycle correctness, mobile support, rendering performance, or submission acceptance. Refresh policy and API claims before release.

## Sources

- [Obsidian Developer Documentation - Manage plugin lifecycle](https://docs.obsidian.md/Plugins/Guides/Manage+plugin+lifecycle), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian TypeScript API Reference - FileManager](https://docs.obsidian.md/Reference/TypeScript+API/FileManager), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Official TypeScript API Definitions - obsidian.d.ts](https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian TypeScript API Reference - MetadataCache](https://docs.obsidian.md/Reference/TypeScript+API/MetadataCache), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - Optimize plugin load time](https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - Events](https://docs.obsidian.md/Plugins/Events), retrieved 2026-11-01, refresh due 2026-12-01.

## Related

- [[Source SRC-04-019]]
- [[Source SRC-04-023]]
- [[Source SRC-04-026]]
- [[Source SRC-04-027]]
- [[Source SRC-04-028]]
- [[Source SRC-04-029]]
- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[Obsidian Bases API, native dashboards, and query surfaces]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
