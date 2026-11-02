---
type: "source"
title: "Source SRC-04-025"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-04-025"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Vault API, FileManager, atomic edits, and DataAdapter boundaries]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://raw.githubusercontent.com/obsidianmd/eslint-plugin/master/lib/rules/preferFileManagerTrashFile.ts"
---

# Source SRC-04-025

Original paraphrase of [Official eslint-plugin-obsidianmd Rule - prefer-file-manager-trash-file](https://raw.githubusercontent.com/obsidianmd/eslint-plugin/master/lib/rules/preferFileManagerTrashFile.ts); reviewed 2026-11-01.

- The prefer-file-manager-trash-file rule recommends FileManager.trashFile over Vault.trash and Vault.delete to respect user deletion settings. This rule source does not establish its configured severity.

Public reference ID: `SRC-04-025`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
