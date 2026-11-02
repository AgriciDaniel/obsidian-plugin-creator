---
type: "source"
title: "Source SRC-02-003"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-02-003"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Obsidian Bases API, native dashboards, and query surfaces]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Build%20a%20Bases%20view.md"
---

# Source SRC-02-003

Original paraphrase of [Build a custom Obsidian Bases view](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Build%20a%20Bases%20view.md); reviewed 2026-11-01.

- Register a Bases view with registerBasesView(viewId, registration) and provide a factory receiving the query controller and parent element.
- A custom Bases view extends BasesView, calls super(controller), and responds to configuration or query data changes in onDataUpdated.
- Bases view registration options define controls whose user values are stored in the Base configuration.
- Use this.config.getOrder, this.config.get, this.data.groupedData, and entry.getValue when presenting filtered property query results.
- An unfiltered Base can include every vault file, so the guide recommends reusing DOM elements and avoiding unnecessary offscreen rendering for thousands of entries.

Public reference ID: `SRC-02-003`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
