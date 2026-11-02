---
type: "source"
title: "Source SRC-04-023"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-04-023"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Vault API, FileManager, atomic edits, and DataAdapter boundaries]]"
  - "[[MetadataCache, link resolution, subpath deep-linking, and Obsidian URI]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://docs.obsidian.md/Reference/TypeScript+API/FileManager"
---

# Source SRC-04-023

Original paraphrase of [Obsidian TypeScript API Reference - FileManager](https://docs.obsidian.md/Reference/TypeScript+API/FileManager); reviewed 2026-11-01.

- FileManager.renameFile updates links according to user preferences; generateMarkdownLink also follows link format preferences.
- FileManager.processFrontMatter atomically reads, modifies, and saves frontmatter, and callers must handle errors.

Public reference ID: `SRC-04-023`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
