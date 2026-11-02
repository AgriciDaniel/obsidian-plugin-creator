---
type: "source"
title: "Source SRC-04-003"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-04-003"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[CodeMirror 6 architecture, StateFields, ViewPlugins, and Live Preview]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://docs.obsidian.md/Plugins/Editor/Communicating+with+editor+extensions"
---

# Source SRC-04-003

Original paraphrase of [Obsidian Developer Documentation - Communicating with editor extensions](https://docs.obsidian.md/Plugins/Editor/Communicating+with+editor+extensions); reviewed 2026-11-01.

- The communication guide describes obtaining the underlying CodeMirror view through a property absent from the public Editor typings. Treat this access as an explicitly documented integration caveat.
- CodeMirror view plugins can be queried through EditorView.plugin and custom state can be changed through dispatched effects.

Public reference ID: `SRC-04-003`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
