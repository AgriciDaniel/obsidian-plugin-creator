---
type: "source"
title: "Source SRC-01-011"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-01-011"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Plugin lifecycle, Component ownership, and cleanup discipline]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Commands.md"
---

# Source SRC-01-011

Original paraphrase of [Obsidian command interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Commands.md); reviewed 2026-11-01.

- Register commands through addCommand during onload and use checkCallback for conditionally available actions.
- A conditional command must check its preconditions both during availability checking and during execution.
- editorCallback receives the active editor and editor context; editor commands appear only when an editor is active.
- Avoid default command hotkeys for distributed plugins because user and plugin keybindings can conflict.

Public reference ID: `SRC-01-011`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
