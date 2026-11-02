---
type: "source"
title: "Source SRC-01-003"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-01-003"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Plugin lifecycle, Component ownership, and cleanup discipline]]"
  - "[[Community Store submission, eslint-plugin review gates, BRAT, and release CI]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/Manifest.md"
---

# Source SRC-01-003

Original paraphrase of [Obsidian manifest specification](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/Manifest.md); reviewed 2026-11-01.

- Required common manifest properties are author, minAppVersion, name, and version; plugin-specific required properties are description, id, and isDesktopOnly.
- Plugin ids allow lowercase letters and hyphens, must not end with plugin, and must not contain obsidian.
- Manifest versions use the x.y.z form of semantic versioning; minAppVersion records the minimum required app version.
- For local development the manifest id should match the plugin folder name; the documentation warns that mismatches prevent some methods such as onExternalSettingsChange from being called.

Public reference ID: `SRC-01-003`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
