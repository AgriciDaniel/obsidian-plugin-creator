---
type: "concept"
title: "Modals, suggest interfaces, menus, settings tabs, and SecretStorage"
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
  - "[[Source SRC-01-002]]"
  - "[[Source SRC-02-004]]"
  - "[[Source SRC-02-005]]"
  - "[[Source SRC-02-007]]"
  - "[[Source SRC-02-008]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Modals.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Settings.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Store%20secrets.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Migrate%20to%20declarative%20settings.md"
---

# Modals, suggest interfaces, menus, settings tabs, and SecretStorage

Use the narrowest interaction surface.

## Verified source guidance

Paraphrases from the dated sources below. Repeated upstream origins are consistency checks, not independent corroboration.

### Obsidian public TypeScript API declarations

- [evidence-based] Component supports register, registerEvent, registerDomEvent, and registerInterval cleanup, as well as child component ownership through addChild and removeChild. ([[Source SRC-01-002]])
- [evidence-based] Plugin.registerBasesView(viewId, registration) returns a boolean and is marked since 1.10.0; false indicates Bases is disabled in the vault. ([[Source SRC-01-002]])
- [evidence-based] SecretStorage and SecretComponent are marked since 1.11.4; SecretStorage.getSecret(id) returns a string or null. ([[Source SRC-01-002]])
- [evidence-based] PluginSettingTab.getSettingDefinitions is marked since 1.13.0 in these public declarations. ([[Source SRC-01-002]])
- [evidence-based] requestUrl accepts a URL string or RequestUrlParam and returns RequestUrlResponsePromise. ([[Source SRC-01-002]])

### Obsidian modals and suggestion interfaces

- [evidence-based] Subclass Modal to present an interaction and open it with open; use contentEl and Setting controls to collect user input. ([[Source SRC-02-004]])
- [evidence-based] SuggestModal implements a query-to-suggestions interaction through getSuggestions, renderSuggestion, and onChooseSuggestion. ([[Source SRC-02-004]])
- [evidence-based] FuzzySuggestModal supplies fuzzy matching around getItems, getItemText, and onChooseItem; renderSuggestion can customize presentation. ([[Source SRC-02-004]])

### Obsidian plugin settings interfaces

- [evidence-based] Register a PluginSettingTab with the plugin and maintain a typed settings object loaded from persisted plugin data. ([[Source SRC-02-005]])
- [evidence-based] Current documentation supports declarative settings definitions, with definitions for controls and custom render callbacks. ([[Source SRC-02-005]])
- [evidence-based] A control definition binds a setting value for the declarative settings system; imperative render callbacks require their own persistence handling. ([[Source SRC-02-005]])

### Obsidian SecretStorage and SecretComponent guide

- [evidence-based] Store a secret identifier in plugin settings instead of a raw API key or token in data.json. ([[Source SRC-02-007]])
- [evidence-based] SecretComponent lets users select or create a named secret, while app.secretStorage.getSecret retrieves its string value or null at runtime. ([[Source SRC-02-007]])
- [evidence-based] The guide describes secret values as local storage keyed to the vault and does not establish an operating-system keychain or end-to-end encrypted secret store. ([[Source SRC-02-007]])

### Migrate Obsidian plugins to declarative settings

- [evidence-based] The declarative PluginSettingTab.getSettingDefinitions API requires Obsidian 1.13.0 or later. ([[Source SRC-02-008]])
- [evidence-based] For minAppVersion at least 1.13.0, the documented migration implements getSettingDefinitions and removes display; dual support retains display for older app versions. ([[Source SRC-02-008]])
- [evidence-based] getSettingDefinitions also runs for search indexing when the tab is registered, so the guide requires cheap definitions without I/O or network work. ([[Source SRC-02-008]])
- [evidence-based] Use update to refresh declarative settings; custom render callbacks do not automatically save values and validate callbacks do not repair previously stored invalid settings. ([[Source SRC-02-008]])

## Engineering recipe

[practitioner] This sequence applies the cited contracts; it is not a tested plugin implementation.

1. Choose commands for actions, modals for focused decisions, and suggests for searchable choices.
2. Keep settings persistent, validate input, and separate secret identifiers from secret values.
3. Feature-check newer settings and secret APIs against the declared app version.
4. Provide keyboard navigation, cancellation, and clear error feedback.

## Verification

[practitioner] Complete the task with the keyboard, reopen settings, and simulate a missing secret.

Record app version, operating system, plugin artifact hash, input size, observed outcome, and evidence path in [[Runtime Acceptance Matrix]].

## Limits

This brain has no physical-device result for this recipe. A static scan cannot prove lifecycle correctness, mobile support, rendering performance, or submission acceptance. Refresh policy and API claims before release.

## Sources

- [Obsidian public TypeScript API declarations](https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian modals and suggestion interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Modals.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian plugin settings interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Settings.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian SecretStorage and SecretComponent guide](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Store%20secrets.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Migrate Obsidian plugins to declarative settings](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Migrate%20to%20declarative%20settings.md), retrieved 2026-11-01, refresh due 2026-12-01.

## Related

- [[Source SRC-01-002]]
- [[Source SRC-02-004]]
- [[Source SRC-02-005]]
- [[Source SRC-02-007]]
- [[Source SRC-02-008]]
- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[Obsidian Bases API, native dashboards, and query surfaces]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
