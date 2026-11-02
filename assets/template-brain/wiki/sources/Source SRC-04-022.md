---
type: "source"
title: "Source SRC-04-022"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-04-022"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[CodeMirror 6 architecture, StateFields, ViewPlugins, and Live Preview]]"
  - "[[Markdown post-processors, codeblock widgets, and Reading view parity]]"
  - "[[Vault API, FileManager, atomic edits, and DataAdapter boundaries]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines"
---

# Source SRC-04-022

Original paraphrase of [Obsidian Developer Documentation - Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines); reviewed 2026-11-01.

- Plugin guidelines prefer Editor APIs for editing the active note, processFrontMatter for frontmatter, and Vault APIs for normal vault files.
- Guidelines recommend direct file lookup APIs, normalizePath for user paths, and safe DOM construction instead of assigning untrusted HTML.

Public reference ID: `SRC-04-022`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
