---
type: "source"
title: "Source SRC-04-020"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-04-020"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Markdown post-processors, codeblock widgets, and Reading view parity]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://raw.githubusercontent.com/obsidianmd/eslint-plugin/master/lib/rules/noPluginAsComponent.ts"
---

# Source SRC-04-020

Original paraphrase of [Official eslint-plugin-obsidianmd Rule - no-plugin-as-component](https://raw.githubusercontent.com/obsidianmd/eslint-plugin/master/lib/rules/noPluginAsComponent.ts); reviewed 2026-11-01.

- The official no-plugin-as-component rule checks MarkdownRenderer.render component ownership, including Plugin instances and inline unowned Component construction. The source rule alone does not establish configured lint severity.

Public reference ID: `SRC-04-020`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
