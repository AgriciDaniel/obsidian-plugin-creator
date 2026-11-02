---
type: "concept"
title: "Build toolchains, esbuild, Vite dual-target, hot-reload, and testing"
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
  - "[[Source SRC-01-007]]"
  - "[[Source obs-sample-plugin-repo]]"
  - "[[Source obs-sample-esbuild-config]]"
  - "[[Source obs-sample-release-workflow]]"
  - "[[Source obs-docs-build-plugin]]"
  - "[[Source obs-docs-github-actions-release]]"
  - "[[Source obs-docs-submit-plugin]]"
  - "[[Source esbuild-api-docs]]"
  - "[[Source vite-build-library-mode]]"
  - "[[Source vitest-config-docs]]"
  - "[[Source vitest-mocking-guide]]"
  - "[[Source pjeby-hot-reload]]"
  - "[[Source wdio-obsidian-service-docs]]"
  - "[[Source mdn-web-workers]]"
  - "[[Source obs-eslint-plugin]]"
  - "[[Source SRC-06-001]]"
  - "[[Source SRC-06-002]]"
  - "[[Source SRC-06-003]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-sample-plugin/blob/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/esbuild.config.mjs"
  - "https://github.com/obsidianmd/obsidian-sample-plugin"
  - "https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/master/esbuild.config.mjs"
  - "https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/master/.github/workflows/release.yml"
  - "https://docs.obsidian.md/Plugins/Getting+started/Build+a+plugin"
  - "https://docs.obsidian.md/Plugins/Releasing/Release+your+plugin+with+GitHub+Actions"
  - "https://docs.obsidian.md/Plugins/Releasing/Submit+your+plugin"
  - "https://esbuild.github.io/api/"
  - "https://vite.dev/guide/build"
  - "https://vitest.dev/config/"
  - "https://vitest.dev/guide/mocking"
  - "https://github.com/pjeby/hot-reload"
  - "https://webdriver.io/docs/wdio-obsidian-service"
  - "https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers"
  - "https://github.com/obsidianmd/eslint-plugin"
  - "https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/package.json"
  - "https://registry.npmjs.org/obsidian/1.14.4"
  - "https://registry.npmjs.org/eslint-plugin-obsidianmd/0.4.2"
---

# Build toolchains, esbuild, Vite dual-target, hot-reload, and testing

Make the build contract explicit.

## Verified source guidance

Paraphrases from the dated sources below. Repeated upstream origins are consistency checks, not independent corroboration.

### Official sample plugin esbuild configuration

- [evidence-based] The official sample builds src/main.ts into main.js using esbuild bundling and CommonJS output. ([[Source SRC-01-007]])
- [evidence-based] The sample external list includes obsidian, electron, named @codemirror and @lezer packages, and Node builtinModules so those imports are not bundled into main.js. ([[Source SRC-01-007]])
- [evidence-based] The sample production build disables inline sourcemaps, enables minification, and uses a one-shot rebuild; development uses context.watch. ([[Source SRC-01-007]])

### Obsidian Sample Plugin Repository (package.json, tsconfig.json, version-bump.mjs, eslint.config.mts)

- [evidence-based] The official sample repository provides TypeScript development scripts, a manifest, build configuration, and a release workflow for a plugin project. ([[Source obs-sample-plugin-repo]])

### Obsidian Sample Plugin esbuild.config.mjs

- [evidence-based] The official sample bundles src/main.ts into a CommonJS main.js targeting ES2021, externalizes host-provided modules, and enables minification for production. ([[Source obs-sample-esbuild-config]])

### Obsidian Sample Plugin GitHub Actions Release Workflow (release.yml)

- [evidence-based] The retrieved official sample workflow builds on tag pushes, generates build provenance attestations, and creates a draft release attaching main.js, manifest.json, and optional styles.css. ([[Source obs-sample-release-workflow]])

### Obsidian Developer Docs: Build a plugin

- [evidence-based] The getting started guide recommends a separate development vault and explains installing a local plugin with manifest.json and main.js. ([[Source obs-docs-build-plugin]])

### Obsidian Developer Docs: Release your plugin with GitHub Actions

- [evidence-based] The release guide packages main.js, manifest.json, and optional styles.css as release assets and uses the manifest version for the release tag. ([[Source obs-docs-github-actions-release]])

### Obsidian Developer Docs: Submit your plugin

- [evidence-based] Current submission documentation describes submission through the Community directory and automated scanning. Repository metadata and a valid built release are required. ([[Source obs-docs-submit-plugin]])

### esbuild API Documentation (external, format, target, sourcemap, treeShaking)

- [evidence-based] esbuild external excludes matching imports from a bundle; sourcemap and minify options control production artifact composition. ([[Source esbuild-api-docs]])

### Vite Guide: Building for Production and Library Mode

- [practitioner] Vite library mode supports explicit library entry points, output formats, and external dependencies. An Obsidian adapter configuration is an engineering choice, not a first-party Vite plugin guarantee. ([[Source vite-build-library-mode]])

### Vitest Configuration Reference (resolve.alias, environment)

- [practitioner] Vitest configuration supports test environments and module aliasing for host dependencies that are unavailable in a unit test runtime. ([[Source vitest-config-docs]])

### Vitest Guide: Mocking Modules, Globals, and Timers

- [practitioner] Vitest provides module mocking and fake timers for isolated tests. Mock results do not establish real Obsidian runtime behavior. ([[Source vitest-mocking-guide]])

### Hot-Reload Plugin for Obsidian Plugins (pjeby/hot-reload)

- [evidence-based] The Hot Reload maintainer documents reloading development plugins when built files change, with eligibility determined by a git directory or .hotreload marker. ([[Source pjeby-hot-reload]])

### WebdriverIO Documentation: wdio-obsidian-service

- [evidence-based] wdio-obsidian-service integrates WebdriverIO with Obsidian application sessions and exposes options for application versions, plugins, and a test vault. ([[Source wdio-obsidian-service-docs]])

### MDN Web Docs: Using Web Workers (Embedded Blob URL Workers)

- [practitioner] Workers can be terminated explicitly; MDN also demonstrates embedding worker source in a Blob and obtaining an object URL. This does not verify that a particular Obsidian desktop or mobile runtime supports that deployment path. ([[Source mdn-web-workers]])

### Official ESLint Plugin for Obsidian Plugins (obsidianmd/eslint-plugin)

- [practitioner] The official ESLint plugin documents Obsidian-specific checks and a recommended configuration. Authors must run the actual configured version rather than infer a full scan result from text matches. ([[Source obs-eslint-plugin]])

### Official sample plugin package and scripts

- [evidence-based] The official sample plugin builds with TypeScript checks followed by esbuild. ([[Source SRC-06-001]])
- [evidence-based] The sample package defines an ESLint command and uses the Obsidian API as a development dependency. ([[Source SRC-06-001]])

### Obsidian npm API package 1.14.4 metadata

- [evidence-based] Obsidian API package 1.14.4 declares peer versions @codemirror/view 6.43.13 and @codemirror/state 6.7.6. ([[Source SRC-06-002]])
- [evidence-based] Package metadata records dependency compatibility declarations; it does not establish runtime compatibility of a generated plugin. ([[Source SRC-06-002]])

### Official Obsidian ESLint package 0.4.2 metadata

- [evidence-based] The 0.4.2 Obsidian ESLint package declares an Obsidian peer dependency of 1.8.7 and an @eslint/js peer range of ^9.30.1. ([[Source SRC-06-003]])
- [evidence-based] Its declared peer versions require deliberate resolution when a project targets a newer Obsidian API package. ([[Source SRC-06-003]])

## Engineering recipe

[practitioner] This sequence applies the cited contracts; it is not a tested plugin implementation.

1. Start from the official sample build and document any departure.
2. Inspect the final bundle and external module list, not just package.json dependencies.
3. Run the build, TypeScript checks, and official lint on the actual project.
4. Release the exact tested main.js, manifest.json, and optional styles.css with matching version metadata.

## Verification

[practitioner] Build from a clean dependency install and inspect the resulting release archive.

Record app version, operating system, plugin artifact hash, input size, observed outcome, and evidence path in [[Runtime Acceptance Matrix]].

## Limits

This brain has no physical-device result for this recipe. A static scan cannot prove lifecycle correctness, mobile support, rendering performance, or submission acceptance. Refresh policy and API claims before release.

## Sources

- [Official sample plugin esbuild configuration](https://github.com/obsidianmd/obsidian-sample-plugin/blob/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/esbuild.config.mjs), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Sample Plugin Repository (package.json, tsconfig.json, version-bump.mjs, eslint.config.mts)](https://github.com/obsidianmd/obsidian-sample-plugin), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Sample Plugin esbuild.config.mjs](https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/master/esbuild.config.mjs), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Sample Plugin GitHub Actions Release Workflow (release.yml)](https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/master/.github/workflows/release.yml), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: Build a plugin](https://docs.obsidian.md/Plugins/Getting+started/Build+a+plugin), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: Release your plugin with GitHub Actions](https://docs.obsidian.md/Plugins/Releasing/Release+your+plugin+with+GitHub+Actions), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: Submit your plugin](https://docs.obsidian.md/Plugins/Releasing/Submit+your+plugin), retrieved 2026-11-01, refresh due 2026-12-01.
- [esbuild API Documentation (external, format, target, sourcemap, treeShaking)](https://esbuild.github.io/api/), retrieved 2026-11-01, refresh due 2026-12-01.
- [Vite Guide: Building for Production and Library Mode](https://vite.dev/guide/build), retrieved 2026-11-01, refresh due 2026-12-01.
- [Vitest Configuration Reference (resolve.alias, environment)](https://vitest.dev/config/), retrieved 2026-11-01, refresh due 2026-12-01.
- [Vitest Guide: Mocking Modules, Globals, and Timers](https://vitest.dev/guide/mocking), retrieved 2026-11-01, refresh due 2026-12-01.
- [Hot-Reload Plugin for Obsidian Plugins (pjeby/hot-reload)](https://github.com/pjeby/hot-reload), retrieved 2026-11-01, refresh due 2026-12-01.
- [WebdriverIO Documentation: wdio-obsidian-service](https://webdriver.io/docs/wdio-obsidian-service), retrieved 2026-11-01, refresh due 2026-12-01.
- [MDN Web Docs: Using Web Workers (Embedded Blob URL Workers)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers), retrieved 2026-11-01, refresh due 2026-12-01.
- [Official ESLint Plugin for Obsidian Plugins (obsidianmd/eslint-plugin)](https://github.com/obsidianmd/eslint-plugin), retrieved 2026-11-01, refresh due 2026-12-01.
- [Official sample plugin package and scripts](https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/package.json), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian npm API package 1.14.4 metadata](https://registry.npmjs.org/obsidian/1.14.4), retrieved 2026-11-01, refresh due 2026-12-01.
- [Official Obsidian ESLint package 0.4.2 metadata](https://registry.npmjs.org/eslint-plugin-obsidianmd/0.4.2), retrieved 2026-11-01, refresh due 2026-12-01.

## Related

- [[Source SRC-01-007]]
- [[Source obs-sample-plugin-repo]]
- [[Source obs-sample-esbuild-config]]
- [[Source obs-sample-release-workflow]]
- [[Source obs-docs-build-plugin]]
- [[Source obs-docs-github-actions-release]]
- [[Source obs-docs-submit-plugin]]
- [[Source esbuild-api-docs]]
- [[Source vite-build-library-mode]]
- [[Source vitest-config-docs]]
- [[Source vitest-mocking-guide]]
- [[Source pjeby-hot-reload]]
- [[Source wdio-obsidian-service-docs]]
- [[Source mdn-web-workers]]
- [[Source obs-eslint-plugin]]
- [[Source SRC-06-001]]
- [[Source SRC-06-002]]
- [[Source SRC-06-003]]
- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[Obsidian Bases API, native dashboards, and query surfaces]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
