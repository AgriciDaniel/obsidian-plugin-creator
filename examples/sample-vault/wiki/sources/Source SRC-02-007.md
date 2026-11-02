---
type: "source"
title: "Source SRC-02-007"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "SRC-02-007"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Modals, suggest interfaces, menus, settings tabs, and SecretStorage]]"
  - "[[Security, XSS prevention, Sync storage limits, and network disclosure]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Store%20secrets.md"
---

# Source SRC-02-007

Original paraphrase of [Obsidian SecretStorage and SecretComponent guide](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Store%20secrets.md); reviewed 2026-11-01.

- Store a secret identifier in plugin settings instead of a raw API key or token in data.json.
- SecretComponent lets users select or create a named secret, while app.secretStorage.getSecret retrieves its string value or null at runtime.
- The guide describes secret values as local storage keyed to the vault and does not establish an operating-system keychain or end-to-end encrypted secret store.

Public reference ID: `SRC-02-007`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
