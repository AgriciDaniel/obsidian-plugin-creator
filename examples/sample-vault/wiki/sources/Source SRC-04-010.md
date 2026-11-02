---
type: "source"
title: "Source SRC-04-010"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-04-010"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[CodeMirror 6 architecture, StateFields, ViewPlugins, and Live Preview]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://codemirror.net/docs/guide/"
---

# Source SRC-04-010

Original paraphrase of [CodeMirror 6 Documentation - System Guide](https://codemirror.net/docs/guide/); reviewed 2026-11-01.

- CodeMirror separates immutable editor state from the DOM-facing EditorView; application code should update editor state through transactions.

Public reference ID: `SRC-04-010`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
