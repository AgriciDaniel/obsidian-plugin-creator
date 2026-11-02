---
type: "source"
title: "Source SRC-01-001"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-01-001"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Plugin lifecycle, Component ownership, and cleanup discipline]]"
  - "[[Workspace leaves, custom ItemView dashboards, and deferred views]]"
  - "[[Design system, CSS variables, themes, icons, and accessibility]]"
  - "[[Community Store submission, eslint-plugin review gates, BRAT, and release CI]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md"
---

# Source SRC-01-001

Original paraphrase of [Obsidian plugin guidelines](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md); reviewed 2026-11-01.

- Use the plugin-provided this.app reference rather than the debugging global app object.
- Release plugin resources on unload through registered lifecycle ownership where possible; do not detach workspace leaves in onunload.
- Avoid retaining custom view instances on the Plugin class; locate live view instances through the workspace.
- Construct user-facing DOM with DOM APIs or Obsidian helpers instead of interpolating user input into innerHTML, outerHTML, or insertAdjacentHTML.
- Use CSS classes and Obsidian CSS variables instead of hardcoded visual styling in plugin TypeScript.

Public reference ID: `SRC-01-001`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
