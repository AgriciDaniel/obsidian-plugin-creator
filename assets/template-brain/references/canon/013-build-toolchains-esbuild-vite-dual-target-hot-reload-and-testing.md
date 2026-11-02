# 013. Build toolchains, esbuild, Vite dual-target, hot-reload, and testing

Distilled official documentation, retrieved 2026-11-01; confidence: practitioner for the integration recipe. All source statements are labeled paraphrases.

Core thesis: Make the build contract explicit.

## How to use it

1. [practitioner] Start from the official sample build and document any departure.
2. [practitioner] Inspect the final bundle and external module list, not just package.json dependencies.
3. [practitioner] Run the build, TypeScript checks, and official lint on the actual project.
4. [practitioner] Release the exact tested main.js, manifest.json, and optional styles.css with matching version metadata.

## Evidence and caveats

- [Official sample plugin esbuild configuration](https://github.com/obsidianmd/obsidian-sample-plugin/blob/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/esbuild.config.mjs); retrieved 2026-11-01; source `SRC-01-007`; verify the linked source note for exact supported claims.
- [Obsidian Sample Plugin Repository (package.json, tsconfig.json, version-bump.mjs, eslint.config.mts)](https://github.com/obsidianmd/obsidian-sample-plugin); retrieved 2026-11-01; source `obs-sample-plugin-repo`; verify the linked source note for exact supported claims.
- [Obsidian Sample Plugin esbuild.config.mjs](https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/master/esbuild.config.mjs); retrieved 2026-11-01; source `obs-sample-esbuild-config`; verify the linked source note for exact supported claims.
- [Obsidian Sample Plugin GitHub Actions Release Workflow (release.yml)](https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/master/.github/workflows/release.yml); retrieved 2026-11-01; source `obs-sample-release-workflow`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: Build a plugin](https://docs.obsidian.md/Plugins/Getting+started/Build+a+plugin); retrieved 2026-11-01; source `obs-docs-build-plugin`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: Release your plugin with GitHub Actions](https://docs.obsidian.md/Plugins/Releasing/Release+your+plugin+with+GitHub+Actions); retrieved 2026-11-01; source `obs-docs-github-actions-release`; verify the linked source note for exact supported claims.
- [Obsidian Developer Docs: Submit your plugin](https://docs.obsidian.md/Plugins/Releasing/Submit+your+plugin); retrieved 2026-11-01; source `obs-docs-submit-plugin`; verify the linked source note for exact supported claims.
- [esbuild API Documentation (external, format, target, sourcemap, treeShaking)](https://esbuild.github.io/api/); retrieved 2026-11-01; source `esbuild-api-docs`; verify the linked source note for exact supported claims.
- [Vite Guide: Building for Production and Library Mode](https://vite.dev/guide/build); retrieved 2026-11-01; source `vite-build-library-mode`; verify the linked source note for exact supported claims.
- [Vitest Configuration Reference (resolve.alias, environment)](https://vitest.dev/config/); retrieved 2026-11-01; source `vitest-config-docs`; verify the linked source note for exact supported claims.
- [Vitest Guide: Mocking Modules, Globals, and Timers](https://vitest.dev/guide/mocking); retrieved 2026-11-01; source `vitest-mocking-guide`; verify the linked source note for exact supported claims.
- [Hot-Reload Plugin for Obsidian Plugins (pjeby/hot-reload)](https://github.com/pjeby/hot-reload); retrieved 2026-11-01; source `pjeby-hot-reload`; verify the linked source note for exact supported claims.
- [WebdriverIO Documentation: wdio-obsidian-service](https://webdriver.io/docs/wdio-obsidian-service); retrieved 2026-11-01; source `wdio-obsidian-service-docs`; verify the linked source note for exact supported claims.
- [MDN Web Docs: Using Web Workers (Embedded Blob URL Workers)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers); retrieved 2026-11-01; source `mdn-web-workers`; verify the linked source note for exact supported claims.
- [Official ESLint Plugin for Obsidian Plugins (obsidianmd/eslint-plugin)](https://github.com/obsidianmd/eslint-plugin); retrieved 2026-11-01; source `obs-eslint-plugin`; verify the linked source note for exact supported claims.
- [Official sample plugin package and scripts](https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/package.json); retrieved 2026-11-01; source `SRC-06-001`; verify the linked source note for exact supported claims.
- [Obsidian npm API package 1.14.4 metadata](https://registry.npmjs.org/obsidian/1.14.4); retrieved 2026-11-01; source `SRC-06-002`; verify the linked source note for exact supported claims.
- [Official Obsidian ESLint package 0.4.2 metadata](https://registry.npmjs.org/eslint-plugin-obsidianmd/0.4.2); retrieved 2026-11-01; source `SRC-06-003`; verify the linked source note for exact supported claims.

No fabricated quotations or page numbers. Source relationships do not establish independent corroboration. Runtime behavior remains untested here.

## Brain hooks

Folded into [[Build toolchains, esbuild, Vite dual-target, hot-reload, and testing]]. Verify with [[Runtime Acceptance Matrix]] and [[Claim Verification Flow]].
