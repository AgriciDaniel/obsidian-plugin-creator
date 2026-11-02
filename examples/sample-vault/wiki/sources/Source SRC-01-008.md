---
type: "source"
title: "Source SRC-01-008"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-01-008"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Mobile compatibility, startup performance, and memory profiling]]"
  - "[[Community Store submission, eslint-plugin review gates, BRAT, and release CI]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Getting%20started/Mobile%20development.md"
---

# Source SRC-01-008

Original paraphrase of [Obsidian mobile development](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Getting%20started/Mobile%20development.md); reviewed 2026-11-01.

- Node.js and Electron APIs are unavailable on mobile, including calls made indirectly by plugin dependencies.
- The documented desktop-only manifest switch is isDesktopOnly: true when the plugin requires Node.js or Electron APIs.
- Platform.isIosApp and Platform.isAndroidApp provide app platform detection.
- The guide distinguishes desktop mobile emulation from inspecting Obsidian on an actual Android or iOS device.
- The mobile guide warns that regular-expression lookbehind is unsupported on iOS versions below 16.4.

Public reference ID: `SRC-01-008`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
