---
type: "source"
title: "Source SRC-01-009"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-01-009"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Community Store submission, eslint-plugin review gates, BRAT, and release CI]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Submission%20requirements%20for%20plugins.md"
---

# Source SRC-01-009

Original paraphrase of [Obsidian plugin submission requirements](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Submission%20requirements%20for%20plugins.md); reviewed 2026-11-01.

- Set minAppVersion to the minimum app version the plugin actually supports; the guide recommends the latest stable build when the author cannot determine a suitable minimum.
- Plugin descriptions must have at most 250 characters, end in a period, avoid emoji and special characters, and use appropriate capitalization.
- Command ids should omit the plugin id because Obsidian prefixes it automatically.
- Remove unused sample plugin code before submission and use fundingUrl for financial support links.

Public reference ID: `SRC-01-009`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
