---
type: "source"
title: "Source SRC-06-003"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-06-003"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Build toolchains, esbuild, Vite dual-target, hot-reload, and testing]]"
  - "[[Community Store submission, eslint-plugin review gates, BRAT, and release CI]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://registry.npmjs.org/eslint-plugin-obsidianmd/0.4.2"
---

# Source SRC-06-003

Original paraphrase of [Official Obsidian ESLint package 0.4.2 metadata](https://registry.npmjs.org/eslint-plugin-obsidianmd/0.4.2); reviewed 2026-11-01.

- The 0.4.2 Obsidian ESLint package declares an Obsidian peer dependency of 1.8.7 and an @eslint/js peer range of ^9.30.1.
- Its declared peer versions require deliberate resolution when a project targets a newer Obsidian API package.

Public reference ID: `SRC-06-003`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
