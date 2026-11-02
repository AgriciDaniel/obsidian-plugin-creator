---
type: "source"
title: "Source SRC-04-011"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-04-011"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[CodeMirror 6 architecture, StateFields, ViewPlugins, and Live Preview]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://codemirror.net/docs/ref/"
---

# Source SRC-04-011

Original paraphrase of [CodeMirror 6 Documentation - Reference Manual](https://codemirror.net/docs/ref/); reviewed 2026-11-01.

- CodeMirror decoration providers that run after viewport computation cannot introduce block widgets or replacements spanning line breaks.
- WidgetType supports DOM creation, equality comparison, and destruction; requestMeasure can notify the editor when layout needs measuring.

Public reference ID: `SRC-04-011`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
