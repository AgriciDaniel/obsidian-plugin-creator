---
type: "concept"
title: "Workspace leaves, custom ItemView dashboards, and deferred views"
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
  - "[[Obsidian Bases API, native dashboards, and query surfaces]]"
  - "[[Modals, suggest interfaces, menus, settings tabs, and SecretStorage]]"
  - "[[Source SRC-01-001]]"
  - "[[Source SRC-01-002]]"
  - "[[Source SRC-02-001]]"
  - "[[Source SRC-02-002]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md"
  - "https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Views.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Defer%20views.md"
---

# Workspace leaves, custom ItemView dashboards, and deferred views

Treat each workspace leaf as an independent view.

## Verified source guidance

Paraphrases from the dated sources below. Repeated upstream origins are consistency checks, not independent corroboration.

### Obsidian plugin guidelines

- [evidence-based] Use the plugin-provided this.app reference rather than the debugging global app object. ([[Source SRC-01-001]])
- [evidence-based] Release plugin resources on unload through registered lifecycle ownership where possible; do not detach workspace leaves in onunload. ([[Source SRC-01-001]])
- [evidence-based] Avoid retaining custom view instances on the Plugin class; locate live view instances through the workspace. ([[Source SRC-01-001]])
- [evidence-based] Construct user-facing DOM with DOM APIs or Obsidian helpers instead of interpolating user input into innerHTML, outerHTML, or insertAdjacentHTML. ([[Source SRC-01-001]])
- [evidence-based] Use CSS classes and Obsidian CSS variables instead of hardcoded visual styling in plugin TypeScript. ([[Source SRC-01-001]])

### Obsidian public TypeScript API declarations

- [evidence-based] Component supports register, registerEvent, registerDomEvent, and registerInterval cleanup, as well as child component ownership through addChild and removeChild. ([[Source SRC-01-002]])
- [evidence-based] Plugin.registerBasesView(viewId, registration) returns a boolean and is marked since 1.10.0; false indicates Bases is disabled in the vault. ([[Source SRC-01-002]])
- [evidence-based] SecretStorage and SecretComponent are marked since 1.11.4; SecretStorage.getSecret(id) returns a string or null. ([[Source SRC-01-002]])
- [evidence-based] PluginSettingTab.getSettingDefinitions is marked since 1.13.0 in these public declarations. ([[Source SRC-01-002]])
- [evidence-based] requestUrl accepts a URL string or RequestUrlParam and returns RequestUrlResponsePromise. ([[Source SRC-01-002]])

### Obsidian custom ItemView interfaces

- [evidence-based] A custom workspace view extends ItemView and provides a unique getViewType and a human-readable getDisplayText. ([[Source SRC-02-001]])
- [evidence-based] Register custom views with a factory passed to registerView; Obsidian may invoke that factory multiple times. ([[Source SRC-02-001]])
- [evidence-based] Build view content in onOpen and release view-owned resources in onClose. ([[Source SRC-02-001]])
- [evidence-based] Find view instances through workspace leaves rather than maintaining view references on the plugin class. ([[Source SRC-02-001]])

### Obsidian deferred view lifecycle

- [evidence-based] Since Obsidian 1.7.2, startup views may be DeferredView instances until their tab becomes visible. ([[Source SRC-02-002]])
- [evidence-based] getLeavesOfType alone does not establish that leaf.view is an initialized custom view; perform an instanceof check. ([[Source SRC-02-002]])
- [evidence-based] Await workspace.revealLeaf before interacting with the revealed custom view and confirm its concrete class. ([[Source SRC-02-002]])
- [evidence-based] loadIfDeferred can initialize a hidden leaf but defeats the lazy-loading performance optimization; the guide recommends sparse use and shows a requireApiVersion guard. ([[Source SRC-02-002]])

## Engineering recipe

[practitioner] This sequence applies the cited contracts; it is not a tested plugin implementation.

1. Register a view factory and keep per-leaf state in the view.
2. Persist serializable state separately from DOM nodes and renderer objects.
3. Resolve deferred leaves before relying on a concrete view instance.
4. Suspend work when a view is inactive and release view resources when it closes.

## Verification

[practitioner] Open two leaves, split a pane, restart the workspace, then close one leaf.

Record app version, operating system, plugin artifact hash, input size, observed outcome, and evidence path in [[Runtime Acceptance Matrix]].

## Limits

This brain has no physical-device result for this recipe. A static scan cannot prove lifecycle correctness, mobile support, rendering performance, or submission acceptance. Refresh policy and API claims before release.

## Sources

- [Obsidian plugin guidelines](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian public TypeScript API declarations](https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian custom ItemView interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Views.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian deferred view lifecycle](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Defer%20views.md), retrieved 2026-11-01, refresh due 2026-12-01.

## Related

- [[Source SRC-01-001]]
- [[Source SRC-01-002]]
- [[Source SRC-02-001]]
- [[Source SRC-02-002]]
- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Obsidian Bases API, native dashboards, and query surfaces]]
- [[Modals, suggest interfaces, menus, settings tabs, and SecretStorage]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
