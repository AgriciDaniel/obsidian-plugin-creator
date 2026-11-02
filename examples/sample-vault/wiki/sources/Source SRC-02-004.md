---
type: "source"
title: "Source SRC-02-004"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-02-004"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Modals, suggest interfaces, menus, settings tabs, and SecretStorage]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Modals.md"
---

# Source SRC-02-004

Original paraphrase of [Obsidian modals and suggestion interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Modals.md); reviewed 2026-11-01.

- Subclass Modal to present an interaction and open it with open; use contentEl and Setting controls to collect user input.
- SuggestModal implements a query-to-suggestions interaction through getSuggestions, renderSuggestion, and onChooseSuggestion.
- FuzzySuggestModal supplies fuzzy matching around getItems, getItemText, and onChooseItem; renderSuggestion can customize presentation.

Public reference ID: `SRC-02-004`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
