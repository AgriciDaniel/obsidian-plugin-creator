---
type: "concept"
title: "Community Store submission, eslint-plugin review gates, BRAT, and release CI"
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
  - "[[Source SRC-01-001]]"
  - "[[Source SRC-01-002]]"
  - "[[Source SRC-01-003]]"
  - "[[Source SRC-01-004]]"
  - "[[Source SRC-01-005]]"
  - "[[Source SRC-01-006]]"
  - "[[Source SRC-01-007]]"
  - "[[Source SRC-01-008]]"
  - "[[Source SRC-01-009]]"
  - "[[Source SRC-06-001]]"
  - "[[Source SRC-06-003]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md"
  - "https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/Manifest.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Submit%20your%20plugin.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Developer%20policies.md"
  - "https://github.com/obsidianmd/eslint-plugin/blob/837b01dc1647cb3f0c532becb60ea83bec137656/docs/configuration.md"
  - "https://github.com/obsidianmd/obsidian-sample-plugin/blob/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/esbuild.config.mjs"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Getting%20started/Mobile%20development.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Submission%20requirements%20for%20plugins.md"
  - "https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/package.json"
  - "https://registry.npmjs.org/eslint-plugin-obsidianmd/0.4.2"
---

# Community Store submission, eslint-plugin review gates, BRAT, and release CI

Review the exact artifact against the current submission channel.

## Verified source guidance

Paraphrases from the dated sources below. Repeated upstream origins are consistency checks, not independent corroboration.

### Obsidian plugin guidelines

- [evidence-based] Use the plugin-provided this.app reference rather than the debugging global app object. ([[Source SRC-01-001]])
- [evidence-based] Release plugin resources on unload through registered lifecycle ownership where possible; do not detach workspace leaves in onunload. ([[Source SRC-01-001]])
- [evidence-based] Avoid retaining custom view instances on the Plugin class; locate live view instances through the workspace. ([[Source SRC-01-001]])
- [evidence-based] Construct user-facing DOM with DOM APIs or Obsidian helpers instead of interpolating user input into innerHTML, outerHTML, or insertAdjacentHTML. ([[Source SRC-01-001]])
- [evidence-based] Use CSS classes and Obsidian CSS variables instead of hardcoded visual styling in plugin TypeScript. ([[Source SRC-01-001]])

### Obsidian public TypeScript API declarations

- [evidence-based] Component supports register, registerEvent, registerDomEvent, and registerInterval cleanup, as well as child component ownership through addChild and removeChild. ([[Source SRC-01-002]])
- [evidence-based] Plugin.registerBasesView(viewId, registration) returns a boolean and is marked since 1.10.0; false indicates Bases is disabled in the vault. ([[Source SRC-01-002]])
- [evidence-based] SecretStorage and SecretComponent are marked since 1.11.4; SecretStorage.getSecret(id) returns a string or null. ([[Source SRC-01-002]])
- [evidence-based] PluginSettingTab.getSettingDefinitions is marked since 1.13.0 in these public declarations. ([[Source SRC-01-002]])
- [evidence-based] requestUrl accepts a URL string or RequestUrlParam and returns RequestUrlResponsePromise. ([[Source SRC-01-002]])

### Obsidian manifest specification

- [evidence-based] Required common manifest properties are author, minAppVersion, name, and version; plugin-specific required properties are description, id, and isDesktopOnly. ([[Source SRC-01-003]])
- [evidence-based] Plugin ids allow lowercase letters and hyphens, must not end with plugin, and must not contain obsidian. ([[Source SRC-01-003]])
- [evidence-based] Manifest versions use the x.y.z form of semantic versioning; minAppVersion records the minimum required app version. ([[Source SRC-01-003]])
- [evidence-based] For local development the manifest id should match the plugin folder name; the documentation warns that mismatches prevent some methods such as onExternalSettingsChange from being called. ([[Source SRC-01-003]])

### Submit a plugin to the Obsidian Community directory

- [evidence-based] The current submission guide directs authors to community.obsidian.md, sign in with an Obsidian account, and link their GitHub account before adding a plugin. ([[Source SRC-01-004]])
- [evidence-based] The repository root must contain README.md, LICENSE, and manifest.json before submission. ([[Source SRC-01-004]])
- [evidence-based] The GitHub release tag must match manifest.json version; release binary attachments are main.js, manifest.json, and optional styles.css. ([[Source SRC-01-004]])
- [evidence-based] The directory reads manifest.json at the default branch HEAD; users install release assets from the GitHub tag matching the manifest version. ([[Source SRC-01-004]])
- [evidence-based] Automated review errors must be resolved before a submitted plugin becomes installable from Obsidian. ([[Source SRC-01-004]])

### Obsidian Community directory developer policies

- [evidence-based] Directory-listed plugins must not obscure their code purpose, add client-side telemetry, or install or update themselves or their dependencies. ([[Source SRC-01-005]])
- [evidence-based] Network use, required payment or accounts, external vault file access, in-plugin static advertising, and server-side telemetry require README disclosures; server-side telemetry also requires a privacy policy. ([[Source SRC-01-005]])
- [evidence-based] Directory policies require a license, respect for third-party code licenses, and compliance with the Obsidian trademark policy. ([[Source SRC-01-005]])

### Official Obsidian ESLint configuration guide

- [evidence-based] The recommended ESLint config is an array of flat config objects; spread it into the top-level config array and supply TypeScript parser project options. ([[Source SRC-01-006]])
- [evidence-based] The recommended config includes ESLint core rules, typescript-eslint, Obsidian rules, security plugins, Obsidian globals, and package dependency checks. ([[Source SRC-01-006]])
- [evidence-based] The community scanner uses a configuration derived from the recommended config, ignores build and test files, and treats most non-security violations as warnings; local recommended config severities are not identical to scanner severities. ([[Source SRC-01-006]])
- [evidence-based] The documented scanner example keeps no-eval, no-implied-eval, no-unsanitized/method, no-unsanitized/property, obsidianmd/regex-lookbehind, and obsidianmd/no-forbidden-elements as errors. ([[Source SRC-01-006]])

### Official sample plugin esbuild configuration

- [evidence-based] The official sample builds src/main.ts into main.js using esbuild bundling and CommonJS output. ([[Source SRC-01-007]])
- [evidence-based] The sample external list includes obsidian, electron, named @codemirror and @lezer packages, and Node builtinModules so those imports are not bundled into main.js. ([[Source SRC-01-007]])
- [evidence-based] The sample production build disables inline sourcemaps, enables minification, and uses a one-shot rebuild; development uses context.watch. ([[Source SRC-01-007]])

### Obsidian mobile development

- [evidence-based] Node.js and Electron APIs are unavailable on mobile, including calls made indirectly by plugin dependencies. ([[Source SRC-01-008]])
- [evidence-based] The documented desktop-only manifest switch is isDesktopOnly: true when the plugin requires Node.js or Electron APIs. ([[Source SRC-01-008]])
- [evidence-based] Platform.isIosApp and Platform.isAndroidApp provide app platform detection. ([[Source SRC-01-008]])
- [evidence-based] The guide distinguishes desktop mobile emulation from inspecting Obsidian on an actual Android or iOS device. ([[Source SRC-01-008]])
- [evidence-based] The mobile guide warns that regular-expression lookbehind is unsupported on iOS versions below 16.4. ([[Source SRC-01-008]])

### Obsidian plugin submission requirements

- [evidence-based] Set minAppVersion to the minimum app version the plugin actually supports; the guide recommends the latest stable build when the author cannot determine a suitable minimum. ([[Source SRC-01-009]])
- [evidence-based] Plugin descriptions must have at most 250 characters, end in a period, avoid emoji and special characters, and use appropriate capitalization. ([[Source SRC-01-009]])
- [evidence-based] Command ids should omit the plugin id because Obsidian prefixes it automatically. ([[Source SRC-01-009]])
- [evidence-based] Remove unused sample plugin code before submission and use fundingUrl for financial support links. ([[Source SRC-01-009]])

### Official sample plugin package and scripts

- [evidence-based] The official sample plugin builds with TypeScript checks followed by esbuild. ([[Source SRC-06-001]])
- [evidence-based] The sample package defines an ESLint command and uses the Obsidian API as a development dependency. ([[Source SRC-06-001]])

### Official Obsidian ESLint package 0.4.2 metadata

- [evidence-based] The 0.4.2 Obsidian ESLint package declares an Obsidian peer dependency of 1.8.7 and an @eslint/js peer range of ^9.30.1. ([[Source SRC-06-003]])
- [evidence-based] Its declared peer versions require deliberate resolution when a project targets a newer Obsidian API package. ([[Source SRC-06-003]])

## Engineering recipe

[practitioner] This sequence applies the cited contracts; it is not a tested plugin implementation.

1. Refresh submission instructions and developer policies before release.
2. Run official lint and inspect every finding; this brain's scanner is only a preliminary heuristic.
3. Check manifest, compatibility map, tagged assets, license, README disclosures, and platform support.
4. Submit only with owner approval and retain review results and rollback instructions.

## Verification

[practitioner] Install the tagged assets in a disposable vault and complete the full acceptance matrix.

Record app version, operating system, plugin artifact hash, input size, observed outcome, and evidence path in [[Runtime Acceptance Matrix]].

## Limits

This brain has no physical-device result for this recipe. A static scan cannot prove lifecycle correctness, mobile support, rendering performance, or submission acceptance. Refresh policy and API claims before release.

## Sources

- [Obsidian plugin guidelines](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian public TypeScript API declarations](https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian manifest specification](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/Manifest.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Submit a plugin to the Obsidian Community directory](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Submit%20your%20plugin.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Community directory developer policies](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Developer%20policies.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Official Obsidian ESLint configuration guide](https://github.com/obsidianmd/eslint-plugin/blob/837b01dc1647cb3f0c532becb60ea83bec137656/docs/configuration.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Official sample plugin esbuild configuration](https://github.com/obsidianmd/obsidian-sample-plugin/blob/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/esbuild.config.mjs), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian mobile development](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Getting%20started/Mobile%20development.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian plugin submission requirements](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Submission%20requirements%20for%20plugins.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Official sample plugin package and scripts](https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/package.json), retrieved 2026-11-01, refresh due 2026-12-01.
- [Official Obsidian ESLint package 0.4.2 metadata](https://registry.npmjs.org/eslint-plugin-obsidianmd/0.4.2), retrieved 2026-11-01, refresh due 2026-12-01.

## Related

- [[Source SRC-01-001]]
- [[Source SRC-01-002]]
- [[Source SRC-01-003]]
- [[Source SRC-01-004]]
- [[Source SRC-01-005]]
- [[Source SRC-01-006]]
- [[Source SRC-01-007]]
- [[Source SRC-01-008]]
- [[Source SRC-01-009]]
- [[Source SRC-06-001]]
- [[Source SRC-06-003]]
- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[Obsidian Bases API, native dashboards, and query surfaces]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
