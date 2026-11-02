---
type: "source"
title: "Source SRC-02-002"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-02-002"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Workspace leaves, custom ItemView dashboards, and deferred views]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Defer%20views.md"
---

# Source SRC-02-002

Original paraphrase of [Obsidian deferred view lifecycle](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Defer%20views.md); reviewed 2026-11-01.

- Since Obsidian 1.7.2, startup views may be DeferredView instances until their tab becomes visible.
- getLeavesOfType alone does not establish that leaf.view is an initialized custom view; perform an instanceof check.
- Await workspace.revealLeaf before interacting with the revealed custom view and confirm its concrete class.
- loadIfDeferred can initialize a hidden leaf but defeats the lazy-loading performance optimization; the guide recommends sparse use and shows a requireApiVersion guard.

Public reference ID: `SRC-02-002`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
