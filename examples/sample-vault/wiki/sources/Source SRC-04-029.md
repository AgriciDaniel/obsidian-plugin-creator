---
type: "source"
title: "Source SRC-04-029"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-04-029"
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
  - "https://docs.obsidian.md/Plugins/Events"
---

# Source SRC-04-029

Original paraphrase of [Obsidian Developer Documentation - Events](https://docs.obsidian.md/Plugins/Events); reviewed 2026-11-01.

- Use registerEvent for event references and registerInterval for repeating timers so plugin unload releases them.

Public reference ID: `SRC-04-029`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
