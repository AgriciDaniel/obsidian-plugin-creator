# 015. Security, XSS prevention, Sync storage limits, and network disclosure

Distilled official documentation, retrieved 2026-11-01; confidence: practitioner for the integration recipe. All source statements are labeled paraphrases.

Core thesis: Minimize stored data and disclosed network access.

## How to use it

1. [practitioner] Keep compact settings separate from rebuildable caches and large derived indexes.
2. [practitioner] Use current secret APIs when supported; do not assume encryption or Sync behavior without evidence.
3. [practitioner] Define where every network request goes and what note content it sends.
4. [practitioner] Test malformed input, missing credentials, offline mode, and storage recovery.

## Evidence and caveats

- [Obsidian Community directory developer policies](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Developer%20policies.md); retrieved 2026-11-01; source `SRC-01-005`; verify the linked source note for exact supported claims.
- [Official Obsidian ESLint configuration guide](https://github.com/obsidianmd/eslint-plugin/blob/837b01dc1647cb3f0c532becb60ea83bec137656/docs/configuration.md); retrieved 2026-11-01; source `SRC-01-006`; verify the linked source note for exact supported claims.
- [Obsidian SecretStorage and SecretComponent guide](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Store%20secrets.md); retrieved 2026-11-01; source `SRC-02-007`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: Submit your plugin](https://docs.obsidian.md/Plugins/Releasing/Submit+your+plugin); retrieved 2026-11-01; source `obs-docs-submit-plugin`; verify the linked source note for exact supported claims.
- [Obsidian Official TypeScript API Definitions (obsidian.d.ts)](https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts); retrieved 2026-11-01; source `obs-api-dts`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: requestUrl TypeScript API Reference](https://docs.obsidian.md/Reference/TypeScript+API/requestUrl); retrieved 2026-11-01; source `obs-docs-requesturl-api`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines); retrieved 2026-11-01; source `obs-docs-plugin-guidelines`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: HTML elements](https://docs.obsidian.md/Plugins/User+interface/HTML+elements); retrieved 2026-11-01; source `obs-docs-html-elements`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: sanitizeHTMLToDom TypeScript API Reference](https://docs.obsidian.md/Reference/TypeScript+API/sanitizeHTMLToDom); retrieved 2026-11-01; source `obs-docs-sanitize-html`; verify the linked source note for exact supported claims.
- [Official ESLint Plugin for Obsidian Plugins (obsidianmd/eslint-plugin)](https://github.com/obsidianmd/eslint-plugin); retrieved 2026-11-01; source `obs-eslint-plugin`; verify the linked source note for exact supported claims.
- [Obsidian Help: Plans and storage limits (Obsidian Sync)](https://help.obsidian.md/sync/plans); retrieved 2026-11-01; source `obs-help-sync-plans`; verify the linked source note for exact supported claims.
- [Obsidian Help: Sync settings and selective syncing](https://help.obsidian.md/sync/settings); retrieved 2026-11-01; source `obs-help-sync-settings`; verify the linked source note for exact supported claims.
- [Obsidian Help: How Obsidian stores data (Vault, Config Folder, Global Settings, IndexedDB)](https://obsidian.md/help/data-storage); retrieved 2026-11-01; source `obs-help-data-storage`; verify the linked source note for exact supported claims.
- [MDN Web Docs: IndexedDB API](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API); retrieved 2026-11-01; source `mdn-indexeddb-api`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: Store secrets (SecretStorage and SecretComponent)](https://docs.obsidian.md/Plugins/Guides/Store+secrets); retrieved 2026-11-01; source `obs-docs-store-secrets`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: Community Directory Developer Policies](https://docs.obsidian.md/Community+directory/Developer+policies); retrieved 2026-11-01; source `obs-docs-developer-policies`; verify the linked source note for exact supported claims.
- [Obsidian Help: Plugin security](https://help.obsidian.md/plugin-security); retrieved 2026-11-01; source `obs-help-plugin-security`; verify the linked source note for exact supported claims.

No fabricated quotations or page numbers. Source relationships do not establish independent corroboration. Runtime behavior remains untested here.

## Brain hooks

Folded into [[Security, XSS prevention, Sync storage limits, and network disclosure]]. Verify with [[Runtime Acceptance Matrix]] and [[Claim Verification Flow]].
