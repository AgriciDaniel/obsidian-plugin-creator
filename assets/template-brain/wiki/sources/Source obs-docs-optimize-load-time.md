---
type: "source"
title: "Source obs-docs-optimize-load-time"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "obs-docs-optimize-load-time"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Mobile compatibility, startup performance, and memory profiling]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time"
---

# Source obs-docs-optimize-load-time

Original paraphrase of [Obsidian Developer Docs: Optimize plugin load time](https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time); reviewed 2026-11-01.

- Obsidian loads enabled plugins before users can interact; keep onload and view construction lightweight and defer expensive startup work.
- Vault create events fire for existing files during initialization; check layout readiness or register the create handler inside onLayoutReady.

Public reference ID: `obs-docs-optimize-load-time`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
