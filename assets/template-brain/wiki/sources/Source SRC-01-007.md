---
type: "source"
title: "Source SRC-01-007"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-01-007"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[CodeMirror 6 architecture, StateFields, ViewPlugins, and Live Preview]]"
  - "[[Build toolchains, esbuild, Vite dual-target, hot-reload, and testing]]"
  - "[[Community Store submission, eslint-plugin review gates, BRAT, and release CI]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-sample-plugin/blob/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/esbuild.config.mjs"
---

# Source SRC-01-007

Original paraphrase of [Official sample plugin esbuild configuration](https://github.com/obsidianmd/obsidian-sample-plugin/blob/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/esbuild.config.mjs); reviewed 2026-11-01.

- The official sample builds src/main.ts into main.js using esbuild bundling and CommonJS output.
- The sample external list includes obsidian, electron, named @codemirror and @lezer packages, and Node builtinModules so those imports are not bundled into main.js.
- The sample production build disables inline sourcemaps, enables minification, and uses a one-shot rebuild; development uses context.watch.

Public reference ID: `SRC-01-007`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
