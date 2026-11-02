---
type: "source"
title: "Source SRC-01-004"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-01-004"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Community Store submission, eslint-plugin review gates, BRAT, and release CI]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Submit%20your%20plugin.md"
---

# Source SRC-01-004

Original paraphrase of [Submit a plugin to the Obsidian Community directory](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Submit%20your%20plugin.md); reviewed 2026-11-01.

- The current submission guide directs authors to community.obsidian.md, sign in with an Obsidian account, and link their GitHub account before adding a plugin.
- The repository root must contain README.md, LICENSE, and manifest.json before submission.
- The GitHub release tag must match manifest.json version; release binary attachments are main.js, manifest.json, and optional styles.css.
- The directory reads manifest.json at the default branch HEAD; users install release assets from the GitHub tag matching the manifest version.
- Automated review errors must be resolved before a submitted plugin becomes installable from Obsidian.

Public reference ID: `SRC-01-004`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
