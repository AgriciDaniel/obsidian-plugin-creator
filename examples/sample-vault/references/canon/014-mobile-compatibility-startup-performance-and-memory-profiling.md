# 014. Mobile compatibility, startup performance, and memory profiling

Distilled official documentation, retrieved 2026-11-01; confidence: practitioner for the integration recipe. All source statements are labeled paraphrases.

Core thesis: Budget startup and verify actual platforms.

## How to use it

1. [practitioner] Keep initial registration cheap and lazy-load expensive indexes or visual libraries.
2. [practitioner] Treat mobile support as a tested product claim, with desktop-only APIs isolated.
3. [practitioner] Measure cold startup, large-vault behavior, and close/reopen memory use.
4. [practitioner] Retain physical-device results separately from static scans and desktop emulation.

## Evidence and caveats

- [Obsidian mobile development](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Getting%20started/Mobile%20development.md); retrieved 2026-11-01; source `SRC-01-008`; verify the linked source note for exact supported claims.
- [Obsidian Sample Plugin Repository (package.json, tsconfig.json, version-bump.mjs, eslint.config.mts)](https://github.com/obsidianmd/obsidian-sample-plugin); retrieved 2026-11-01; source `obs-sample-plugin-repo`; verify the linked source note for exact supported claims.
- [Obsidian Sample Plugin esbuild.config.mjs](https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/master/esbuild.config.mjs); retrieved 2026-11-01; source `obs-sample-esbuild-config`; verify the linked source note for exact supported claims.
- [Hot-Reload Plugin for Obsidian Plugins (pjeby/hot-reload)](https://github.com/pjeby/hot-reload); retrieved 2026-11-01; source `pjeby-hot-reload`; verify the linked source note for exact supported claims.
- [WebdriverIO Documentation: wdio-obsidian-service](https://webdriver.io/docs/wdio-obsidian-service); retrieved 2026-11-01; source `wdio-obsidian-service-docs`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: Mobile development](https://docs.obsidian.md/Plugins/Getting+started/Mobile+development); retrieved 2026-11-01; source `obs-docs-mobile-development`; verify the linked source note for exact supported claims.
- [Obsidian Official TypeScript API Definitions (obsidian.d.ts)](https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts); retrieved 2026-11-01; source `obs-api-dts`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: Platform TypeScript API Reference](https://docs.obsidian.md/Reference/TypeScript+API/Platform); retrieved 2026-11-01; source `obs-docs-platform-api`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: requestUrl TypeScript API Reference](https://docs.obsidian.md/Reference/TypeScript+API/requestUrl); retrieved 2026-11-01; source `obs-docs-requesturl-api`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: Optimize plugin load time](https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time); retrieved 2026-11-01; source `obs-docs-optimize-load-time`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: Defer views](https://docs.obsidian.md/Plugins/Guides/Defer+views); retrieved 2026-11-01; source `obs-docs-defer-views`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: debounce TypeScript API Reference](https://docs.obsidian.md/Reference/TypeScript+API/debounce); retrieved 2026-11-01; source `obs-docs-debounce-api`; verify the linked source note for exact supported claims.
- [Chrome DevTools Documentation: Record Heap Snapshots](https://developer.chrome.com/docs/devtools/memory-problems/heap-snapshots); retrieved 2026-11-01; source `chrome-devtools-heap-snapshots`; verify the linked source note for exact supported claims.
- [MDN Web Docs: Using Web Workers (Embedded Blob URL Workers)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers); retrieved 2026-11-01; source `mdn-web-workers`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines); retrieved 2026-11-01; source `obs-docs-plugin-guidelines`; verify the linked source note for exact supported claims.
- [Official ESLint Plugin for Obsidian Plugins (obsidianmd/eslint-plugin)](https://github.com/obsidianmd/eslint-plugin); retrieved 2026-11-01; source `obs-eslint-plugin`; verify the linked source note for exact supported claims.
- [Obsidian Help: How Obsidian stores data (Vault, Config Folder, Global Settings, IndexedDB)](https://obsidian.md/help/data-storage); retrieved 2026-11-01; source `obs-help-data-storage`; verify the linked source note for exact supported claims.

No fabricated quotations or page numbers. Source relationships do not establish independent corroboration. Runtime behavior remains untested here.

## Brain hooks

Folded into [[Mobile compatibility, startup performance, and memory profiling]]. Verify with [[Runtime Acceptance Matrix]] and [[Claim Verification Flow]].
