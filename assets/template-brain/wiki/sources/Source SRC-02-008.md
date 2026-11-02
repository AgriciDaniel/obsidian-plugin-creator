---
type: "source"
title: "Source SRC-02-008"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-02-008"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Modals, suggest interfaces, menus, settings tabs, and SecretStorage]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Migrate%20to%20declarative%20settings.md"
---

# Source SRC-02-008

Original paraphrase of [Migrate Obsidian plugins to declarative settings](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Migrate%20to%20declarative%20settings.md); reviewed 2026-11-01.

- The declarative PluginSettingTab.getSettingDefinitions API requires Obsidian 1.13.0 or later.
- For minAppVersion at least 1.13.0, the documented migration implements getSettingDefinitions and removes display; dual support retains display for older app versions.
- getSettingDefinitions also runs for search indexing when the tab is registered, so the guide requires cheap definitions without I/O or network work.
- Use update to refresh declarative settings; custom render callbacks do not automatically save values and validate callbacks do not repair previously stored invalid settings.

Public reference ID: `SRC-02-008`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
