---
type: "concept"
title: "Mobile compatibility, startup performance, and memory profiling"
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
  - "[[Source SRC-01-008]]"
  - "[[Source obs-sample-plugin-repo]]"
  - "[[Source obs-sample-esbuild-config]]"
  - "[[Source pjeby-hot-reload]]"
  - "[[Source wdio-obsidian-service-docs]]"
  - "[[Source obs-docs-mobile-development]]"
  - "[[Source obs-api-dts]]"
  - "[[Source obs-docs-platform-api]]"
  - "[[Source obs-docs-requesturl-api]]"
  - "[[Source obs-docs-optimize-load-time]]"
  - "[[Source obs-docs-defer-views]]"
  - "[[Source obs-docs-debounce-api]]"
  - "[[Source chrome-devtools-heap-snapshots]]"
  - "[[Source mdn-web-workers]]"
  - "[[Source obs-docs-plugin-guidelines]]"
  - "[[Source obs-eslint-plugin]]"
  - "[[Source obs-help-data-storage]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Getting%20started/Mobile%20development.md"
  - "https://github.com/obsidianmd/obsidian-sample-plugin"
  - "https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/master/esbuild.config.mjs"
  - "https://github.com/pjeby/hot-reload"
  - "https://webdriver.io/docs/wdio-obsidian-service"
  - "https://docs.obsidian.md/Plugins/Getting+started/Mobile+development"
  - "https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts"
  - "https://docs.obsidian.md/Reference/TypeScript+API/Platform"
  - "https://docs.obsidian.md/Reference/TypeScript+API/requestUrl"
  - "https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time"
  - "https://docs.obsidian.md/Plugins/Guides/Defer+views"
  - "https://docs.obsidian.md/Reference/TypeScript+API/debounce"
  - "https://developer.chrome.com/docs/devtools/memory-problems/heap-snapshots"
  - "https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers"
  - "https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines"
  - "https://github.com/obsidianmd/eslint-plugin"
  - "https://obsidian.md/help/data-storage"
---

# Mobile compatibility, startup performance, and memory profiling

Budget startup and verify actual platforms.

## Verified source guidance

Paraphrases from the dated sources below. Repeated upstream origins are consistency checks, not independent corroboration.

### Obsidian mobile development

- [evidence-based] Node.js and Electron APIs are unavailable on mobile, including calls made indirectly by plugin dependencies. ([[Source SRC-01-008]])
- [evidence-based] The documented desktop-only manifest switch is isDesktopOnly: true when the plugin requires Node.js or Electron APIs. ([[Source SRC-01-008]])
- [evidence-based] Platform.isIosApp and Platform.isAndroidApp provide app platform detection. ([[Source SRC-01-008]])
- [evidence-based] The guide distinguishes desktop mobile emulation from inspecting Obsidian on an actual Android or iOS device. ([[Source SRC-01-008]])
- [evidence-based] The mobile guide warns that regular-expression lookbehind is unsupported on iOS versions below 16.4. ([[Source SRC-01-008]])

### Obsidian Sample Plugin Repository (package.json, tsconfig.json, version-bump.mjs, eslint.config.mts)

- [evidence-based] The official sample repository provides TypeScript development scripts, a manifest, build configuration, and a release workflow for a plugin project. ([[Source obs-sample-plugin-repo]])

### Obsidian Sample Plugin esbuild.config.mjs

- [evidence-based] The official sample bundles src/main.ts into a CommonJS main.js targeting ES2021, externalizes host-provided modules, and enables minification for production. ([[Source obs-sample-esbuild-config]])

### Hot-Reload Plugin for Obsidian Plugins (pjeby/hot-reload)

- [evidence-based] The Hot Reload maintainer documents reloading development plugins when built files change, with eligibility determined by a git directory or .hotreload marker. ([[Source pjeby-hot-reload]])

### WebdriverIO Documentation: wdio-obsidian-service

- [evidence-based] wdio-obsidian-service integrates WebdriverIO with Obsidian application sessions and exposes options for application versions, plugins, and a test vault. ([[Source wdio-obsidian-service-docs]])

### Obsidian Developer Docs: Mobile development

- [evidence-based] Node.js and Electron APIs are unavailable on mobile. Plugins requiring these APIs must declare desktop-only support. ([[Source obs-docs-mobile-development]])
- [evidence-based] The guide documents desktop mobile-layout emulation and separate real-device debugging procedures for Android and iOS; emulation is not physical-device validation. ([[Source obs-docs-mobile-development]])

### Obsidian Official TypeScript API Definitions (obsidian.d.ts)

- [evidence-based] The official typings define Platform checks, requestUrl, debounce, sanitizeHTMLToDom, SecretStorage, and plugin data APIs. Availability must be matched to the supported app version. ([[Source obs-api-dts]])

### Obsidian Developer Docs: Platform TypeScript API Reference

- [evidence-based] Platform exposes runtime and device flags including desktop, mobile, iOS, and Android variants; use the documented flag appropriate to the condition. ([[Source obs-docs-platform-api]])

### Obsidian Developer Docs: requestUrl TypeScript API Reference

- [evidence-based] requestUrl performs HTTP or HTTPS requests without browser CORS restrictions. Its signature accepts a URL string or RequestUrlParam. ([[Source obs-docs-requesturl-api]])

### Obsidian Developer Docs: Optimize plugin load time

- [evidence-based] Obsidian loads enabled plugins before users can interact; keep onload and view construction lightweight and defer expensive startup work. ([[Source obs-docs-optimize-load-time]])
- [evidence-based] Vault create events fire for existing files during initialization; check layout readiness or register the create handler inside onLayoutReady. ([[Source obs-docs-optimize-load-time]])

### Obsidian Developer Docs: Defer views

- [evidence-based] Obsidian defers background views at startup. Check view types before accessing custom instances and load a deferred view only when needed. ([[Source obs-docs-defer-views]])

### Obsidian Developer Docs: debounce TypeScript API Reference

- [evidence-based] Obsidian debounce returns a Debouncer that can cancel or immediately run a pending invocation. ([[Source obs-docs-debounce-api]])

### Chrome DevTools Documentation: Record Heap Snapshots

- [evidence-based] Chrome heap snapshots support comparison and retained-object inspection for diagnosing JavaScript and detached DOM memory retention. ([[Source chrome-devtools-heap-snapshots]])

### MDN Web Docs: Using Web Workers (Embedded Blob URL Workers)

- [practitioner] Workers can be terminated explicitly; MDN also demonstrates embedding worker source in a Blob and obtaining an object URL. This does not verify that a particular Obsidian desktop or mobile runtime supports that deployment path. ([[Source mdn-web-workers]])

### Obsidian Developer Docs: Plugin guidelines

- [evidence-based] Plugin guidelines reject unsafe insertion of untrusted HTML, retaining custom view instances on the Plugin, and detaching custom leaves during onunload. ([[Source obs-docs-plugin-guidelines]])
- [evidence-based] Use Vault.configDir rather than a hardcoded configuration path and normalize user-provided vault paths. ([[Source obs-docs-plugin-guidelines]])

### Official ESLint Plugin for Obsidian Plugins (obsidianmd/eslint-plugin)

- [practitioner] The official ESLint plugin documents Obsidian-specific checks and a recommended configuration. Authors must run the actual configured version rather than infer a full scan result from text matches. ([[Source obs-eslint-plugin]])

### Obsidian Help: How Obsidian stores data (Vault, Config Folder, Global Settings, IndexedDB)

- [evidence-based] Obsidian uses IndexedDB for local backend state, including metadata cache and Sync connection state. ([[Source obs-help-data-storage]])
- [evidence-based] The help page warns that Apple Lockdown Mode can prevent database persistence unless Obsidian is excluded, requiring reindexing on launch. ([[Source obs-help-data-storage]])

## Engineering recipe

[practitioner] This sequence applies the cited contracts; it is not a tested plugin implementation.

1. Keep initial registration cheap and lazy-load expensive indexes or visual libraries.
2. Treat mobile support as a tested product claim, with desktop-only APIs isolated.
3. Measure cold startup, large-vault behavior, and close/reopen memory use.
4. Retain physical-device results separately from static scans and desktop emulation.

## Verification

[practitioner] Run on desktop plus real iOS/Android devices where those platforms are advertised.

Record app version, operating system, plugin artifact hash, input size, observed outcome, and evidence path in [[Runtime Acceptance Matrix]].

## Limits

This brain has no physical-device result for this recipe. A static scan cannot prove lifecycle correctness, mobile support, rendering performance, or submission acceptance. Refresh policy and API claims before release.

## Sources

- [Obsidian mobile development](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Getting%20started/Mobile%20development.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Sample Plugin Repository (package.json, tsconfig.json, version-bump.mjs, eslint.config.mts)](https://github.com/obsidianmd/obsidian-sample-plugin), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Sample Plugin esbuild.config.mjs](https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/master/esbuild.config.mjs), retrieved 2026-11-01, refresh due 2026-12-01.
- [Hot-Reload Plugin for Obsidian Plugins (pjeby/hot-reload)](https://github.com/pjeby/hot-reload), retrieved 2026-11-01, refresh due 2026-12-01.
- [WebdriverIO Documentation: wdio-obsidian-service](https://webdriver.io/docs/wdio-obsidian-service), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: Mobile development](https://docs.obsidian.md/Plugins/Getting+started/Mobile+development), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Official TypeScript API Definitions (obsidian.d.ts)](https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: Platform TypeScript API Reference](https://docs.obsidian.md/Reference/TypeScript+API/Platform), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: requestUrl TypeScript API Reference](https://docs.obsidian.md/Reference/TypeScript+API/requestUrl), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: Optimize plugin load time](https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: Defer views](https://docs.obsidian.md/Plugins/Guides/Defer+views), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: debounce TypeScript API Reference](https://docs.obsidian.md/Reference/TypeScript+API/debounce), retrieved 2026-11-01, refresh due 2026-12-01.
- [Chrome DevTools Documentation: Record Heap Snapshots](https://developer.chrome.com/docs/devtools/memory-problems/heap-snapshots), retrieved 2026-11-01, refresh due 2026-12-01.
- [MDN Web Docs: Using Web Workers (Embedded Blob URL Workers)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Docs: Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines), retrieved 2026-11-01, refresh due 2026-12-01.
- [Official ESLint Plugin for Obsidian Plugins (obsidianmd/eslint-plugin)](https://github.com/obsidianmd/eslint-plugin), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Help: How Obsidian stores data (Vault, Config Folder, Global Settings, IndexedDB)](https://obsidian.md/help/data-storage), retrieved 2026-11-01, refresh due 2026-12-01.

## Related

- [[Source SRC-01-008]]
- [[Source obs-sample-plugin-repo]]
- [[Source obs-sample-esbuild-config]]
- [[Source pjeby-hot-reload]]
- [[Source wdio-obsidian-service-docs]]
- [[Source obs-docs-mobile-development]]
- [[Source obs-api-dts]]
- [[Source obs-docs-platform-api]]
- [[Source obs-docs-requesturl-api]]
- [[Source obs-docs-optimize-load-time]]
- [[Source obs-docs-defer-views]]
- [[Source obs-docs-debounce-api]]
- [[Source chrome-devtools-heap-snapshots]]
- [[Source mdn-web-workers]]
- [[Source obs-docs-plugin-guidelines]]
- [[Source obs-eslint-plugin]]
- [[Source obs-help-data-storage]]
- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[Obsidian Bases API, native dashboards, and query surfaces]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
