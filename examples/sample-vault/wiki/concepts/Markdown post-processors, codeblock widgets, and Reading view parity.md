---
type: "concept"
title: "Markdown post-processors, codeblock widgets, and Reading view parity"
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
  - "[[Source SRC-04-002]]"
  - "[[Source SRC-04-016]]"
  - "[[Source SRC-04-017]]"
  - "[[Source SRC-04-018]]"
  - "[[Source SRC-04-019]]"
  - "[[Source SRC-04-020]]"
  - "[[Source SRC-04-022]]"
  - "[[Source SRC-04-026]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
source_urls:
  - "https://docs.obsidian.md/Plugins/Editor/Editor+extensions"
  - "https://docs.obsidian.md/Plugins/Editor/Markdown+post+processing"
  - "https://docs.obsidian.md/Reference/TypeScript+API/MarkdownPostProcessorContext"
  - "https://docs.obsidian.md/Reference/TypeScript+API/MarkdownRenderer"
  - "https://docs.obsidian.md/Plugins/Guides/Manage+plugin+lifecycle"
  - "https://raw.githubusercontent.com/obsidianmd/eslint-plugin/master/lib/rules/noPluginAsComponent.ts"
  - "https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines"
  - "https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts"
---

# Markdown post-processors, codeblock widgets, and Reading view parity

Design Reading view parity explicitly.

## Verified source guidance

Paraphrases from the dated sources below. Repeated upstream origins are consistency checks, not independent corroboration.

### Obsidian Developer Documentation - Editor extensions

- [evidence-based] Obsidian editor extensions use CodeMirror 6 and are registered with registerEditorExtension. Reading view customization instead uses Markdown post processing. ([[Source SRC-04-002]])

### Obsidian Developer Documentation - Markdown post processing

- [evidence-based] Markdown post processors modify rendered sections, while registerMarkdownCodeBlockProcessor handles fenced blocks of a named language. Editor-mode behavior requires its own extension. ([[Source SRC-04-016]])
- [evidence-based] The post processing guide describes async processing and print-mode differences; rendered export behavior still needs application testing. ([[Source SRC-04-016]])

### Obsidian TypeScript API Reference - MarkdownPostProcessorContext

- [evidence-based] MarkdownPostProcessorContext provides sourcePath, addChild, and getSectionInfo; getSectionInfo can return null and should be checked before use. ([[Source SRC-04-017]])

### Obsidian TypeScript API Reference - MarkdownRenderer

- [evidence-based] MarkdownRenderer.render accepts an App, Markdown text, target element, source path, and owning Component; the older renderMarkdown entry is deprecated. ([[Source SRC-04-018]])

### Obsidian Developer Documentation - Manage plugin lifecycle

- [evidence-based] Component registration helpers attach child components, event handlers, DOM listeners, and intervals to an owner lifecycle. ([[Source SRC-04-019]])

### Official eslint-plugin-obsidianmd Rule - no-plugin-as-component

- [evidence-based] The official no-plugin-as-component rule checks MarkdownRenderer.render component ownership, including Plugin instances and inline unowned Component construction. The source rule alone does not establish configured lint severity. ([[Source SRC-04-020]])

### Obsidian Developer Documentation - Plugin guidelines

- [evidence-based] Plugin guidelines prefer Editor APIs for editing the active note, processFrontMatter for frontmatter, and Vault APIs for normal vault files. ([[Source SRC-04-022]])
- [evidence-based] Guidelines recommend direct file lookup APIs, normalizePath for user paths, and safe DOM construction instead of assigning untrusted HTML. ([[Source SRC-04-022]])

### Obsidian Official TypeScript API Definitions - obsidian.d.ts

- [evidence-based] The official typings expose editorLivePreviewField, editorInfoField, link parsing helpers, and APIs for opening files with editor state. Minimum supported versions must be checked against the target typings. ([[Source SRC-04-026]])

## Engineering recipe

[practitioner] This sequence applies the cited contracts; it is not a tested plugin implementation.

1. Share the data model between editor widgets and Markdown processors.
2. Attach rendered resources to the processor's lifecycle rather than a global registry.
3. Handle repeated rendering and dispose observers, events, and framework roots.
4. Build DOM from validated values and treat external HTML as untrusted.

## Verification

[practitioner] Render the same content in Reading view, Live Preview, and an embed; close all of them.

Record app version, operating system, plugin artifact hash, input size, observed outcome, and evidence path in [[Runtime Acceptance Matrix]].

## Limits

This brain has no physical-device result for this recipe. A static scan cannot prove lifecycle correctness, mobile support, rendering performance, or submission acceptance. Refresh policy and API claims before release.

## Sources

- [Obsidian Developer Documentation - Editor extensions](https://docs.obsidian.md/Plugins/Editor/Editor+extensions), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - Markdown post processing](https://docs.obsidian.md/Plugins/Editor/Markdown+post+processing), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian TypeScript API Reference - MarkdownPostProcessorContext](https://docs.obsidian.md/Reference/TypeScript+API/MarkdownPostProcessorContext), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian TypeScript API Reference - MarkdownRenderer](https://docs.obsidian.md/Reference/TypeScript+API/MarkdownRenderer), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - Manage plugin lifecycle](https://docs.obsidian.md/Plugins/Guides/Manage+plugin+lifecycle), retrieved 2026-11-01, refresh due 2026-12-01.
- [Official eslint-plugin-obsidianmd Rule - no-plugin-as-component](https://raw.githubusercontent.com/obsidianmd/eslint-plugin/master/lib/rules/noPluginAsComponent.ts), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Official TypeScript API Definitions - obsidian.d.ts](https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts), retrieved 2026-11-01, refresh due 2026-12-01.

## Related

- [[Source SRC-04-002]]
- [[Source SRC-04-016]]
- [[Source SRC-04-017]]
- [[Source SRC-04-018]]
- [[Source SRC-04-019]]
- [[Source SRC-04-020]]
- [[Source SRC-04-022]]
- [[Source SRC-04-026]]
- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[Obsidian Bases API, native dashboards, and query surfaces]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
