---
type: "source"
title: "Source SRC-01-006"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-01-006"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Plugin lifecycle, Component ownership, and cleanup discipline]]"
  - "[[Security, XSS prevention, Sync storage limits, and network disclosure]]"
  - "[[Community Store submission, eslint-plugin review gates, BRAT, and release CI]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/eslint-plugin/blob/837b01dc1647cb3f0c532becb60ea83bec137656/docs/configuration.md"
---

# Source SRC-01-006

Original paraphrase of [Official Obsidian ESLint configuration guide](https://github.com/obsidianmd/eslint-plugin/blob/837b01dc1647cb3f0c532becb60ea83bec137656/docs/configuration.md); reviewed 2026-11-01.

- The recommended ESLint config is an array of flat config objects; spread it into the top-level config array and supply TypeScript parser project options.
- The recommended config includes ESLint core rules, typescript-eslint, Obsidian rules, security plugins, Obsidian globals, and package dependency checks.
- The community scanner uses a configuration derived from the recommended config, ignores build and test files, and treats most non-security violations as warnings; local recommended config severities are not identical to scanner severities.
- The documented scanner example keeps no-eval, no-implied-eval, no-unsanitized/method, no-unsanitized/property, obsidianmd/regex-lookbehind, and obsidianmd/no-forbidden-elements as errors.

Public reference ID: `SRC-01-006`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
