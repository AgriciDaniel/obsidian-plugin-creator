---
type: "source"
title: "Source SRC-04-028"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-04-028"
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
  - "https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time"
---

# Source SRC-04-028

Original paraphrase of [Obsidian Developer Documentation - Optimize plugin load time](https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time); reviewed 2026-11-01.

- Keep onload limited to essential registrations, use a production bundle, and defer substantial startup work through onLayoutReady. Vault create events also fire for existing files during initialization.

Public reference ID: `SRC-04-028`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
