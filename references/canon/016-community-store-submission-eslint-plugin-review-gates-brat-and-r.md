# 016. Community Store submission, eslint-plugin review gates, BRAT, and release CI

Distilled official documentation, retrieved 2026-11-01; confidence: practitioner for the integration recipe. All source statements are labeled paraphrases.

Core thesis: Review the exact artifact against the current submission channel.

## How to use it

1. [practitioner] Refresh submission instructions and developer policies before release.
2. [practitioner] Run official lint and inspect every finding; this brain's scanner is only a preliminary heuristic.
3. [practitioner] Check manifest, compatibility map, tagged assets, license, README disclosures, and platform support.
4. [practitioner] Submit only with owner approval and retain review results and rollback instructions.

## Evidence and caveats

- [Obsidian plugin guidelines](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md); retrieved 2026-11-01; source `SRC-01-001`; verify the linked source note for exact supported claims.
- [Obsidian public TypeScript API declarations](https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts); retrieved 2026-11-01; source `SRC-01-002`; verify the linked source note for exact supported claims.
- [Obsidian manifest specification](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/Manifest.md); retrieved 2026-11-01; source `SRC-01-003`; verify the linked source note for exact supported claims.
- [Submit a plugin to the Obsidian Community directory](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Submit%20your%20plugin.md); retrieved 2026-11-01; source `SRC-01-004`; verify the linked source note for exact supported claims.
- [Obsidian Community directory developer policies](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Developer%20policies.md); retrieved 2026-11-01; source `SRC-01-005`; verify the linked source note for exact supported claims.
- [Official Obsidian ESLint configuration guide](https://github.com/obsidianmd/eslint-plugin/blob/837b01dc1647cb3f0c532becb60ea83bec137656/docs/configuration.md); retrieved 2026-11-01; source `SRC-01-006`; verify the linked source note for exact supported claims.
- [Official sample plugin esbuild configuration](https://github.com/obsidianmd/obsidian-sample-plugin/blob/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/esbuild.config.mjs); retrieved 2026-11-01; source `SRC-01-007`; verify the linked source note for exact supported claims.
- [Obsidian mobile development](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Getting%20started/Mobile%20development.md); retrieved 2026-11-01; source `SRC-01-008`; verify the linked source note for exact supported claims.
- [Obsidian plugin submission requirements](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Submission%20requirements%20for%20plugins.md); retrieved 2026-11-01; source `SRC-01-009`; verify the linked source note for exact supported claims.
- [Official sample plugin package and scripts](https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/package.json); retrieved 2026-11-01; source `SRC-06-001`; verify the linked source note for exact supported claims.
- [Official Obsidian ESLint package 0.4.2 metadata](https://registry.npmjs.org/eslint-plugin-obsidianmd/0.4.2); retrieved 2026-11-01; source `SRC-06-003`; verify the linked source note for exact supported claims.

No fabricated quotations or page numbers. Source relationships do not establish independent corroboration. Runtime behavior remains untested here.

## Brain hooks

Folded into [[Community Store submission, eslint-plugin review gates, BRAT, and release CI]]. Verify with [[Runtime Acceptance Matrix]] and [[Claim Verification Flow]].
