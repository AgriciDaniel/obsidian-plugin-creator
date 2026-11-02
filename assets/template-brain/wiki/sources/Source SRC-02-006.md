---
type: "source"
title: "Source SRC-02-006"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-02-006"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Design system, CSS variables, themes, icons, and accessibility]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/CSS%20variables/About%20styling.md"
---

# Source SRC-02-006

Original paraphrase of [Obsidian CSS variables and styling](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/CSS%20variables/About%20styling.md); reviewed 2026-11-01.

- Obsidian exposes CSS variables for consistent interface styling across the app.
- Using built-in CSS variables for plugin elements supports native-looking interfaces compatible with community themes.
- Ship plugin CSS classes in styles.css and reference variables such as --background-secondary instead of fixed theme-specific colors.

Public reference ID: `SRC-02-006`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
