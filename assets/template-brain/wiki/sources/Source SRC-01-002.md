---
type: "source"
title: "Source SRC-01-002"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-01-002"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Plugin lifecycle, Component ownership, and cleanup discipline]]"
  - "[[Workspace leaves, custom ItemView dashboards, and deferred views]]"
  - "[[Obsidian Bases API, native dashboards, and query surfaces]]"
  - "[[Modals, suggest interfaces, menus, settings tabs, and SecretStorage]]"
  - "[[Community Store submission, eslint-plugin review gates, BRAT, and release CI]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts"
---

# Source SRC-01-002

Original paraphrase of [Obsidian public TypeScript API declarations](https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts); reviewed 2026-11-01.

- Component supports register, registerEvent, registerDomEvent, and registerInterval cleanup, as well as child component ownership through addChild and removeChild.
- Plugin.registerBasesView(viewId, registration) returns a boolean and is marked since 1.10.0; false indicates Bases is disabled in the vault.
- SecretStorage and SecretComponent are marked since 1.11.4; SecretStorage.getSecret(id) returns a string or null.
- PluginSettingTab.getSettingDefinitions is marked since 1.13.0 in these public declarations.
- requestUrl accepts a URL string or RequestUrlParam and returns RequestUrlResponsePromise.

Public reference ID: `SRC-01-002`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
