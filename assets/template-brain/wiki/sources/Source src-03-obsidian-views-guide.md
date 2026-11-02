---
type: "source"
title: "Source src-03-obsidian-views-guide"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "src-03-obsidian-views-guide"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[3D WebGL, Three.js, React Three Fiber, and spatial codex views]]"
  - "[[UI frameworks in plugins Vanilla DOM, React, Svelte, and Vue]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://docs.obsidian.md/Plugins/User+interface/Views"
---

# Source src-03-obsidian-views-guide

Original paraphrase of [Obsidian Developer Documentation: Views (ItemView Lifecycle)](https://docs.obsidian.md/Plugins/User+interface/Views); reviewed 2026-11-01.

- The Views guide registers an ItemView factory, builds content in onOpen, and assigns resource cleanup to onClose; it warns against retaining view references in the plugin.

Public reference ID: `src-03-obsidian-views-guide`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
