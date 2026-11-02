---
type: "source"
title: "Source SRC-04-021"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-04-021"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Vault API, FileManager, atomic edits, and DataAdapter boundaries]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://docs.obsidian.md/Plugins/Vault"
---

# Source SRC-04-021

Original paraphrase of [Obsidian Developer Documentation - Vault](https://docs.obsidian.md/Plugins/Vault); reviewed 2026-11-01.

- Use cachedRead for display-only reads and read when content will be edited. Vault.process supplies an atomic synchronous read-modify-write operation.
- The Vault API works with visible vault files; DataAdapter provides lower-level access, including hidden paths.

Public reference ID: `SRC-04-021`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
