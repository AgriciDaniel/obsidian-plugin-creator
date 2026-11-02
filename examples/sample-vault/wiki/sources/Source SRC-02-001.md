---
type: "source"
title: "Source SRC-02-001"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-02-001"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Workspace leaves, custom ItemView dashboards, and deferred views]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Views.md"
---

# Source SRC-02-001

Original paraphrase of [Obsidian custom ItemView interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Views.md); reviewed 2026-11-01.

- A custom workspace view extends ItemView and provides a unique getViewType and a human-readable getDisplayText.
- Register custom views with a factory passed to registerView; Obsidian may invoke that factory multiple times.
- Build view content in onOpen and release view-owned resources in onClose.
- Find view instances through workspace leaves rather than maintaining view references on the plugin class.

Public reference ID: `SRC-02-001`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
