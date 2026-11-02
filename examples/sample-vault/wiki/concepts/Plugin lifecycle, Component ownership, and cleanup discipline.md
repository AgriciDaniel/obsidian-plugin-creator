---
type: "concept"
title: "Plugin lifecycle, Component ownership, and cleanup discipline"
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
  - "[[Workspace leaves, custom ItemView dashboards, and deferred views]]"
  - "[[Obsidian Bases API, native dashboards, and query surfaces]]"
  - "[[Modals, suggest interfaces, menus, settings tabs, and SecretStorage]]"
  - "[[Source SRC-01-001]]"
  - "[[Source SRC-01-002]]"
  - "[[Source SRC-01-003]]"
  - "[[Source SRC-01-006]]"
  - "[[Source SRC-01-010]]"
  - "[[Source SRC-01-011]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md"
  - "https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/Manifest.md"
  - "https://github.com/obsidianmd/eslint-plugin/blob/837b01dc1647cb3f0c532becb60ea83bec137656/docs/configuration.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Events.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Commands.md"
---

# Plugin lifecycle, Component ownership, and cleanup discipline

Start with the smallest plugin lifecycle.

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

### Obsidian manifest specification

- [evidence-based] Required common manifest properties are author, minAppVersion, name, and version; plugin-specific required properties are description, id, and isDesktopOnly. ([[Source SRC-01-003]])
- [evidence-based] Plugin ids allow lowercase letters and hyphens, must not end with plugin, and must not contain obsidian. ([[Source SRC-01-003]])
- [evidence-based] Manifest versions use the x.y.z form of semantic versioning; minAppVersion records the minimum required app version. ([[Source SRC-01-003]])
- [evidence-based] For local development the manifest id should match the plugin folder name; the documentation warns that mismatches prevent some methods such as onExternalSettingsChange from being called. ([[Source SRC-01-003]])

### Official Obsidian ESLint configuration guide

- [evidence-based] The recommended ESLint config is an array of flat config objects; spread it into the top-level config array and supply TypeScript parser project options. ([[Source SRC-01-006]])
- [evidence-based] The recommended config includes ESLint core rules, typescript-eslint, Obsidian rules, security plugins, Obsidian globals, and package dependency checks. ([[Source SRC-01-006]])
- [evidence-based] The community scanner uses a configuration derived from the recommended config, ignores build and test files, and treats most non-security violations as warnings; local recommended config severities are not identical to scanner severities. ([[Source SRC-01-006]])
- [evidence-based] The documented scanner example keeps no-eval, no-implied-eval, no-unsanitized/method, no-unsanitized/property, obsidianmd/regex-lookbehind, and obsidianmd/no-forbidden-elements as errors. ([[Source SRC-01-006]])

### Obsidian plugin event lifecycle

- [evidence-based] Use Plugin.registerEvent with subscribed event references so event handlers detach during plugin unload. ([[Source SRC-01-010]])
- [evidence-based] Use registerInterval with window.setInterval for repeating work owned by the plugin lifecycle. ([[Source SRC-01-010]])
- [evidence-based] Obsidian exposes its internal Moment library through the obsidian module; the guide does not require a separate Moment runtime installation. ([[Source SRC-01-010]])

### Obsidian command interfaces

- [evidence-based] Register commands through addCommand during onload and use checkCallback for conditionally available actions. ([[Source SRC-01-011]])
- [evidence-based] A conditional command must check its preconditions both during availability checking and during execution. ([[Source SRC-01-011]])
- [evidence-based] editorCallback receives the active editor and editor context; editor commands appear only when an editor is active. ([[Source SRC-01-011]])
- [evidence-based] Avoid default command hotkeys for distributed plugins because user and plugin keybindings can conflict. ([[Source SRC-01-011]])

## Engineering recipe

[practitioner] This sequence applies the cited contracts; it is not a tested plugin implementation.

1. List each command, event, timer, observer, and component before implementing it.
2. Assign one lifecycle owner to every resource; write its cleanup beside its creation.
3. Keep onload focused on registration; defer expensive work until it is needed.
4. Exercise enable, disable, reload, and workspace restore before adding more features.

## Verification

[practitioner] Repeat enable/disable ten times and compare listener, timer, and heap behavior.

Record app version, operating system, plugin artifact hash, input size, observed outcome, and evidence path in [[Runtime Acceptance Matrix]].

## Limits

This brain has no physical-device result for this recipe. A static scan cannot prove lifecycle correctness, mobile support, rendering performance, or submission acceptance. Refresh policy and API claims before release.

## Sources

- [Obsidian plugin guidelines](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian public TypeScript API declarations](https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian manifest specification](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/Manifest.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Official Obsidian ESLint configuration guide](https://github.com/obsidianmd/eslint-plugin/blob/837b01dc1647cb3f0c532becb60ea83bec137656/docs/configuration.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian plugin event lifecycle](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Events.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian command interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Commands.md), retrieved 2026-11-01, refresh due 2026-12-01.

## Related

- [[Source SRC-01-001]]
- [[Source SRC-01-002]]
- [[Source SRC-01-003]]
- [[Source SRC-01-006]]
- [[Source SRC-01-010]]
- [[Source SRC-01-011]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[Obsidian Bases API, native dashboards, and query surfaces]]
- [[Modals, suggest interfaces, menus, settings tabs, and SecretStorage]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
