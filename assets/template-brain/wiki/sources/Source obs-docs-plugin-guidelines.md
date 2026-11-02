---
type: "source"
title: "Source obs-docs-plugin-guidelines"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "obs-docs-plugin-guidelines"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Mobile compatibility, startup performance, and memory profiling]]"
  - "[[Security, XSS prevention, Sync storage limits, and network disclosure]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines"
---

# Source obs-docs-plugin-guidelines

Original paraphrase of [Obsidian Developer Docs: Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines); reviewed 2026-11-01.

- Plugin guidelines reject unsafe insertion of untrusted HTML, retaining custom view instances on the Plugin, and detaching custom leaves during onunload.
- Use Vault.configDir rather than a hardcoded configuration path and normalize user-provided vault paths.

Public reference ID: `obs-docs-plugin-guidelines`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
