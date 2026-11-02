---
type: "source"
title: "Source obs-docs-store-secrets"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "obs-docs-store-secrets"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[Security, XSS prevention, Sync storage limits, and network disclosure]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://docs.obsidian.md/Plugins/Guides/Store+secrets"
---

# Source obs-docs-store-secrets

Original paraphrase of [Obsidian Developer Docs: Store secrets (SecretStorage and SecretComponent)](https://docs.obsidian.md/Plugins/Guides/Store+secrets); reviewed 2026-11-01.

- SecretComponent stores the selected secret name in plugin settings; app.secretStorage.getSecret retrieves the value.
- The guide describes actual secret storage as local storage keyed to the vault. It does not promise an OS keychain, encryption at rest, or access isolation from other enabled plugins.

Public reference ID: `obs-docs-store-secrets`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
