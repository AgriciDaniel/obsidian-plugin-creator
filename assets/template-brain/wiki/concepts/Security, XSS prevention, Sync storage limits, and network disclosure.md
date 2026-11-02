---
type: "concept"
title: "Security, XSS prevention, Sync storage limits, and network disclosure"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/concept"
  - "confidence/practitioner"
related:
  - "[[Plugin lifecycle, Component ownership, and cleanup discipline]]"
  - "[[Workspace leaves, custom ItemView dashboards, and deferred views]]"
  - "[[Obsidian Bases API, native dashboards, and query surfaces]]"
  - "[[Source SRC-01-005]]"
  - "[[Source SRC-01-006]]"
  - "[[Source SRC-02-007]]"
  - "[[Source obs-docs-submit-plugin]]"
  - "[[Source obs-api-dts]]"
  - "[[Source obs-docs-requesturl-api]]"
  - "[[Source obs-docs-plugin-guidelines]]"
  - "[[Source obs-docs-html-elements]]"
  - "[[Source obs-docs-sanitize-html]]"
  - "[[Source obs-eslint-plugin]]"
  - "[[Source obs-help-sync-plans]]"
  - "[[Source obs-help-sync-settings]]"
  - "[[Source obs-help-data-storage]]"
  - "[[Source mdn-indexeddb-api]]"
  - "[[Source obs-docs-store-secrets]]"
  - "[[Source obs-docs-developer-policies]]"
  - "[[Source obs-help-plugin-security]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Developer%20policies.md"
  - "https://github.com/obsidianmd/eslint-plugin/blob/837b01dc1647cb3f0c532becb60ea83bec137656/docs/configuration.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Store%20secrets.md"
  - "https://docs.obsidian.md/Plugins/Releasing/Submit+your+plugin"
  - "https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts"
  - "https://docs.obsidian.md/Reference/TypeScript+API/requestUrl"
  - "https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines"
  - "https://docs.obsidian.md/Plugins/User+interface/HTML+elements"
  - "https://docs.obsidian.md/Reference/TypeScript+API/sanitizeHTMLToDom"
  - "https://github.com/obsidianmd/eslint-plugin"
  - "https://help.obsidian.md/sync/plans"
  - "https://help.obsidian.md/sync/settings"
  - "https://obsidian.md/help/data-storage"
  - "https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API"
  - "https://docs.obsidian.md/Plugins/Guides/Store+secrets"
  - "https://docs.obsidian.md/Community+directory/Developer+policies"
  - "https://help.obsidian.md/plugin-security"
---

# Security, XSS prevention, Sync storage limits, and network disclosure

Minimize stored data and disclosed network access.

## Verified source guidance

Paraphrases from the dated sources below. Repeated upstream origins are consistency checks, not independent corroboration.

### Obsidian Community directory developer policies

- [evidence-based] Directory-listed plugins must not obscure their code purpose, add client-side telemetry, or install or update themselves or their dependencies. ([[Source SRC-01-005]])
- [evidence-based] Network use, required payment or accounts, external vault file access, in-plugin static advertising, and server-side telemetry require README disclosures; server-side telemetry also requires a privacy policy. ([[Source SRC-01-005]])
- [evidence-based] Directory policies require a license, respect for third-party code licenses, and compliance with the Obsidian trademark policy. ([[Source SRC-01-005]])

### Official Obsidian ESLint configuration guide

- [evidence-based] The recommended ESLint config is an array of flat config objects; spread it into the top-level config array and supply TypeScript parser project options. ([[Source SRC-01-006]])
- [evidence-based] The recommended config includes ESLint core rules, typescript-eslint, Obsidian rules, security plugins, Obsidian globals, and package dependency checks. ([[Source SRC-01-006]])
- [evidence-based] The community scanner uses a configuration derived from the recommended config, ignores build and test files, and treats most non-security violations as warnings; local recommended config severities are not identical to scanner severities. ([[Source SRC-01-006]])
- [evidence-based] The documented scanner example keeps no-eval, no-implied-eval, no-unsanitized/method, no-unsanitized/property, obsidianmd/regex-lookbehind, and obsidianmd/no-forbidden-elements as errors. ([[Source SRC-01-006]])

### Obsidian SecretStorage and SecretComponent guide

- [evidence-based] Store a secret identifier in plugin settings instead of a raw API key or token in data.json. ([[Source SRC-02-007]])
- [evidence-based] SecretComponent lets users select or create a named secret, while app.secretStorage.getSecret retrieves its string value or null at runtime. ([[Source SRC-02-007]])
- [evidence-based] The guide describes secret values as local storage keyed to the vault and does not establish an operating-system keychain or end-to-end encrypted secret store. ([[Source SRC-02-007]])

### Obsidian Developer Docs: Submit your plugin

- [evidence-based] Current submission documentation describes submission through the Community directory and automated scanning. Repository metadata and a valid built release are required. ([[Source obs-docs-submit-plugin]])

### Obsidian Official TypeScript API Definitions (obsidian.d.ts)

- [evidence-based] The official typings define Platform checks, requestUrl, debounce, sanitizeHTMLToDom, SecretStorage, and plugin data APIs. Availability must be matched to the supported app version. ([[Source obs-api-dts]])

### Obsidian Developer Docs: requestUrl TypeScript API Reference

- [evidence-based] requestUrl performs HTTP or HTTPS requests without browser CORS restrictions. Its signature accepts a URL string or RequestUrlParam. ([[Source obs-docs-requesturl-api]])

### Obsidian Developer Docs: Plugin guidelines

- [evidence-based] Plugin guidelines reject unsafe insertion of untrusted HTML, retaining custom view instances on the Plugin, and detaching custom leaves during onunload. ([[Source obs-docs-plugin-guidelines]])
- [evidence-based] Use Vault.configDir rather than a hardcoded configuration path and normalize user-provided vault paths. ([[Source obs-docs-plugin-guidelines]])

### Obsidian Developer Docs: HTML elements

- [evidence-based] Obsidian DOM helpers create elements and accept text content and CSS classes without requiring HTML string parsing. ([[Source obs-docs-html-elements]])

### Obsidian Developer Docs: sanitizeHTMLToDom TypeScript API Reference

- [practitioner] sanitizeHTMLToDom converts an HTML string into a sanitized DocumentFragment. Sanitization does not by itself establish every caller interaction is safe. ([[Source obs-docs-sanitize-html]])

### Official ESLint Plugin for Obsidian Plugins (obsidianmd/eslint-plugin)

- [practitioner] The official ESLint plugin documents Obsidian-specific checks and a recommended configuration. Authors must run the actual configured version rather than infer a full scan result from text matches. ([[Source obs-eslint-plugin]])

### Obsidian Help: Plans and storage limits (Obsidian Sync)

- [evidence-based] As retrieved on 2026-11-01, Sync Standard permits files up to 5 MB and 1 GB storage; Sync Plus permits files up to 200 MB and storage tiers from 10 GB to 100 GB. ([[Source obs-help-sync-plans]])
- [evidence-based] Version history and attachments count toward storage. Reaching the account limit stops file syncing and prompts pruning. ([[Source obs-help-sync-plans]])

### Obsidian Help: Sync settings and selective syncing

- [evidence-based] Dot-prefixed hidden files and folders are excluded from Obsidian Sync except the active configuration folder. Community plugin syncing requires enabling its configuration options. ([[Source obs-help-sync-settings]])
- [evidence-based] The help page distinguishes device-specific Sync settings from synced vault configuration and links onExternalSettingsChange for plugin settings refresh. ([[Source obs-help-sync-settings]])

### Obsidian Help: How Obsidian stores data (Vault, Config Folder, Global Settings, IndexedDB)

- [evidence-based] Obsidian uses IndexedDB for local backend state, including metadata cache and Sync connection state. ([[Source obs-help-data-storage]])
- [evidence-based] The help page warns that Apple Lockdown Mode can prevent database persistence unless Obsidian is excluded, requiring reindexing on launch. ([[Source obs-help-data-storage]])

### MDN Web Docs: IndexedDB API

- [practitioner] IndexedDB provides asynchronous transactions for substantial structured client-side data and follows the same-origin policy. Exact Obsidian vault-origin isolation must be tested rather than assumed. ([[Source mdn-indexeddb-api]])

### Obsidian Developer Docs: Store secrets (SecretStorage and SecretComponent)

- [evidence-based] SecretComponent stores the selected secret name in plugin settings; app.secretStorage.getSecret retrieves the value. ([[Source obs-docs-store-secrets]])
- [practitioner] The guide describes actual secret storage as local storage keyed to the vault. It does not promise an OS keychain, encryption at rest, or access isolation from other enabled plugins. ([[Source obs-docs-store-secrets]])

### Obsidian Developer Docs: Community Directory Developer Policies

- [evidence-based] Community directory policies prohibit code obfuscation, client-side telemetry, dynamic network ads, and self-installation or self-updates. ([[Source obs-docs-developer-policies]])
- [evidence-based] README disclosures are required for network services, access outside vaults, payment or account requirements, in-plugin static ads, and server-side telemetry with a privacy policy. ([[Source obs-docs-developer-policies]])

### Obsidian Help: Plugin security

- [evidence-based] Obsidian cannot reliably restrict enabled plugins to individual permissions; plugins inherit its access. Restricted mode prevents third-party plugin execution. ([[Source obs-help-plugin-security]])
- [evidence-based] The help page states that every plugin version is scanned and directory pages display safety scorecards; manual reviews continue for popular, featured, and flagged plugins. ([[Source obs-help-plugin-security]])

## Engineering recipe

[practitioner] This sequence applies the cited contracts; it is not a tested plugin implementation.

1. Keep compact settings separate from rebuildable caches and large derived indexes.
2. Use current secret APIs when supported; do not assume encryption or Sync behavior without evidence.
3. Define where every network request goes and what note content it sends.
4. Test malformed input, missing credentials, offline mode, and storage recovery.

## Verification

[practitioner] Inspect stored files for secrets and verify the visible disclosure against observed requests.

Record app version, operating system, plugin artifact hash, input size, observed outcome, and evidence path in [[Runtime Acceptance Matrix]].

## Limits

This brain has no physical-device result for this recipe. A static scan cannot prove lifecycle correctness, mobile support, rendering performance, or submission acceptance. Refresh policy and API claims before release.

## Sources

- [Obsidian Community directory developer policies](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Developer%20policies.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Official Obsidian ESLint configuration guide](https://github.com/obsidianmd/eslint-plugin/blob/837b01dc1647cb3f0c532becb60ea83bec137656/docs/configuration.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian SecretStorage and SecretComponent guide](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Store%20secrets.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: Submit your plugin](https://docs.obsidian.md/Plugins/Releasing/Submit+your+plugin), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Official TypeScript API Definitions (obsidian.d.ts)](https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: requestUrl TypeScript API Reference](https://docs.obsidian.md/Reference/TypeScript+API/requestUrl), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: HTML elements](https://docs.obsidian.md/Plugins/User+interface/HTML+elements), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: sanitizeHTMLToDom TypeScript API Reference](https://docs.obsidian.md/Reference/TypeScript+API/sanitizeHTMLToDom), retrieved 2026-11-01, refresh due 2026-12-01.
- [Official ESLint Plugin for Obsidian Plugins (obsidianmd/eslint-plugin)](https://github.com/obsidianmd/eslint-plugin), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Help: Plans and storage limits (Obsidian Sync)](https://help.obsidian.md/sync/plans), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Help: Sync settings and selective syncing](https://help.obsidian.md/sync/settings), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Help: How Obsidian stores data (Vault, Config Folder, Global Settings, IndexedDB)](https://obsidian.md/help/data-storage), retrieved 2026-11-01, refresh due 2026-12-01.
- [MDN Web Docs: IndexedDB API](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: Store secrets (SecretStorage and SecretComponent)](https://docs.obsidian.md/Plugins/Guides/Store+secrets), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: Community Directory Developer Policies](https://docs.obsidian.md/Community+directory/Developer+policies), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Help: Plugin security](https://help.obsidian.md/plugin-security), retrieved 2026-11-01, refresh due 2026-12-01.

## Related

- [[Source SRC-01-005]]
- [[Source SRC-01-006]]
- [[Source SRC-02-007]]
- [[Source obs-docs-submit-plugin]]
- [[Source obs-api-dts]]
- [[Source obs-docs-requesturl-api]]
- [[Source obs-docs-plugin-guidelines]]
- [[Source obs-docs-html-elements]]
- [[Source obs-docs-sanitize-html]]
- [[Source obs-eslint-plugin]]
- [[Source obs-help-sync-plans]]
- [[Source obs-help-sync-settings]]
- [[Source obs-help-data-storage]]
- [[Source mdn-indexeddb-api]]
- [[Source obs-docs-store-secrets]]
- [[Source obs-docs-developer-policies]]
- [[Source obs-help-plugin-security]]
- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[Obsidian Bases API, native dashboards, and query surfaces]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
