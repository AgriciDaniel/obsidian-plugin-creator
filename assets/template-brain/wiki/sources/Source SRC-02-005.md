---
type: "source"
title: "Source SRC-02-005"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-02-005"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Modals, suggest interfaces, menus, settings tabs, and SecretStorage]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Settings.md"
---

# Source SRC-02-005

Original paraphrase of [Obsidian plugin settings interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Settings.md); reviewed 2026-11-01.

- Register a PluginSettingTab with the plugin and maintain a typed settings object loaded from persisted plugin data.
- Current documentation supports declarative settings definitions, with definitions for controls and custom render callbacks.
- A control definition binds a setting value for the declarative settings system; imperative render callbacks require their own persistence handling.

Public reference ID: `SRC-02-005`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
