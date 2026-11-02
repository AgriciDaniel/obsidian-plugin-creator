---
type: "source"
title: "Source SRC-01-010"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-01-010"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Plugin lifecycle, Component ownership, and cleanup discipline]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Events.md"
---

# Source SRC-01-010

Original paraphrase of [Obsidian plugin event lifecycle](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Events.md); reviewed 2026-11-01.

- Use Plugin.registerEvent with subscribed event references so event handlers detach during plugin unload.
- Use registerInterval with window.setInterval for repeating work owned by the plugin lifecycle.
- Obsidian exposes its internal Moment library through the obsidian module; the guide does not require a separate Moment runtime installation.

Public reference ID: `SRC-01-010`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
