---
type: "concept"
title: "Obsidian Bases API, native dashboards, and query surfaces"
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
  - "[[Modals, suggest interfaces, menus, settings tabs, and SecretStorage]]"
  - "[[Source SRC-01-002]]"
  - "[[Source SRC-02-003]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Build%20a%20Bases%20view.md"
---

# Obsidian Bases API, native dashboards, and query surfaces

Choose Bases for a data query surface.

## Verified source guidance

Paraphrases from the dated sources below. Repeated upstream origins are consistency checks, not independent corroboration.

### Obsidian public TypeScript API declarations

- [evidence-based] Component supports register, registerEvent, registerDomEvent, and registerInterval cleanup, as well as child component ownership through addChild and removeChild. ([[Source SRC-01-002]])
- [evidence-based] Plugin.registerBasesView(viewId, registration) returns a boolean and is marked since 1.10.0; false indicates Bases is disabled in the vault. ([[Source SRC-01-002]])
- [evidence-based] SecretStorage and SecretComponent are marked since 1.11.4; SecretStorage.getSecret(id) returns a string or null. ([[Source SRC-01-002]])
- [evidence-based] PluginSettingTab.getSettingDefinitions is marked since 1.13.0 in these public declarations. ([[Source SRC-01-002]])
- [evidence-based] requestUrl accepts a URL string or RequestUrlParam and returns RequestUrlResponsePromise. ([[Source SRC-01-002]])

### Build a custom Obsidian Bases view

- [evidence-based] Register a Bases view with registerBasesView(viewId, registration) and provide a factory receiving the query controller and parent element. ([[Source SRC-02-003]])
- [evidence-based] A custom Bases view extends BasesView, calls super(controller), and responds to configuration or query data changes in onDataUpdated. ([[Source SRC-02-003]])
- [evidence-based] Bases view registration options define controls whose user values are stored in the Base configuration. ([[Source SRC-02-003]])
- [evidence-based] Use this.config.getOrder, this.config.get, this.data.groupedData, and entry.getValue when presenting filtered property query results. ([[Source SRC-02-003]])
- [evidence-based] An unfiltered Base can include every vault file, so the guide recommends reusing DOM elements and avoiding unnecessary offscreen rendering for thousands of entries. ([[Source SRC-02-003]])

## Engineering recipe

[practitioner] This sequence applies the cited contracts; it is not a tested plugin implementation.

1. Use a Bases custom view when the product consumes a Bases query and its property model.
2. Use ItemView when the product owns a workspace independent of a Bases query.
3. Use a Markdown code block when a note should carry a small embedded surface.
4. Check the target API declaration and minimum app version before choosing a signature.

## Verification

[practitioner] Change filters and properties, then test empty results and a large result set.

Record app version, operating system, plugin artifact hash, input size, observed outcome, and evidence path in [[Runtime Acceptance Matrix]].

## Limits

This brain has no physical-device result for this recipe. A static scan cannot prove lifecycle correctness, mobile support, rendering performance, or submission acceptance. Refresh policy and API claims before release.

## Sources

- [Obsidian public TypeScript API declarations](https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts), retrieved 2026-11-01, refresh due 2026-12-01.
- [Build a custom Obsidian Bases view](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Build%20a%20Bases%20view.md), retrieved 2026-11-01, refresh due 2026-12-01.

## Related

- [[Source SRC-01-002]]
- [[Source SRC-02-003]]
- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[Modals, suggest interfaces, menus, settings tabs, and SecretStorage]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
