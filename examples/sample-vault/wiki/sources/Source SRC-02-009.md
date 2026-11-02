---
type: "source"
title: "Source SRC-02-009"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-02-009"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Design system, CSS variables, themes, icons, and accessibility]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Icons.md"
---

# Source SRC-02-009

Original paraphrase of [Obsidian icons](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Icons.md); reviewed 2026-11-01.

- Use setIcon to insert an available named icon into a custom interface element.
- Set --icon-size with a documented size variable to control icon dimensions.
- addIcon registers custom SVG content without the surrounding svg tag; the guide specifies a 0 0 100 100 view box for that custom icon content.

Public reference ID: `SRC-02-009`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
