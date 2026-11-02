---
type: "source"
title: "Source obs-help-data-storage"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "obs-help-data-storage"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Mobile compatibility, startup performance, and memory profiling]]"
  - "[[Security, XSS prevention, Sync storage limits, and network disclosure]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://obsidian.md/help/data-storage"
---

# Source obs-help-data-storage

Original paraphrase of [Obsidian Help: How Obsidian stores data (Vault, Config Folder, Global Settings, IndexedDB)](https://obsidian.md/help/data-storage); reviewed 2026-11-01.

- Obsidian uses IndexedDB for local backend state, including metadata cache and Sync connection state.
- The help page warns that Apple Lockdown Mode can prevent database persistence unless Obsidian is excluded, requiring reindexing on launch.

Public reference ID: `obs-help-data-storage`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
