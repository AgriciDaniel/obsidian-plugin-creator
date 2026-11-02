# 012. UI frameworks in plugins Vanilla DOM, React, Svelte, and Vue

Distilled official documentation, retrieved 2026-11-01; confidence: practitioner for the integration recipe. All source statements are labeled paraphrases.

Core thesis: Choose a framework for a concrete interaction need.

## How to use it

1. [practitioner] Use the Obsidian Setting and DOM helpers for small native interfaces.
2. [practitioner] Mount a framework only inside a view-owned root and unmount it on cleanup.
3. [practitioner] Share domain state outside the framework so an editor widget and dashboard can reuse it.
4. [practitioner] Measure bundle size and startup cost; do not assume one framework is universally faster.

## Evidence and caveats

- [Obsidian Developer Documentation: Foundations Color CSS Variables](https://docs.obsidian.md/Reference/CSS+variables/Foundations/Colors); retrieved 2026-11-01; source `src-03-obsidian-css-colors-vars`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation: HTML Elements](https://docs.obsidian.md/Plugins/User+interface/HTML+elements); retrieved 2026-11-01; source `src-03-obsidian-html-elements`; verify the linked source note for exact supported claims.
- [Obsidian API TypeScript Definitions: obsidian.d.ts (DOM, SVG, and Popout Window Helpers)](https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts); retrieved 2026-11-01; source `src-03-obsidian-api-dts`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation: Views (ItemView Lifecycle)](https://docs.obsidian.md/Plugins/User+interface/Views); retrieved 2026-11-01; source `src-03-obsidian-views-guide`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation: Use React in Your Plugin](https://docs.obsidian.md/Plugins/Getting+started/Use+React+in+your+plugin); retrieved 2026-11-01; source `src-03-obsidian-react-guide`; verify the linked source note for exact supported claims.
- [React Reference Documentation: createRoot (react-dom/client)](https://react.dev/reference/react-dom/client/createRoot); retrieved 2026-11-01; source `src-03-react-createroot-docs`; verify the linked source note for exact supported claims.
- [React Architectural Change: Root Container Event Delegation (React 17+)](https://legacy.reactjs.org/blog/2020/08/10/react-v17-rc.html); retrieved 2026-11-01; source `src-03-react-root-event-delegation`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation: Use Svelte in Your Plugin](https://docs.obsidian.md/Plugins/Getting+started/Use+Svelte+in+your+plugin); retrieved 2026-11-01; source `src-03-obsidian-svelte-guide`; verify the linked source note for exact supported claims.
- [Svelte 5 Documentation: Imperative Component API (mount and unmount)](https://svelte.dev/docs/svelte/imperative-component-api); retrieved 2026-11-01; source `src-03-svelte-v5-imperative-api`; verify the linked source note for exact supported claims.
- [Svelte 5 Documentation: Svelte 5 Migration Guide](https://svelte.dev/docs/svelte/v5-migration-guide); retrieved 2026-11-01; source `src-03-svelte-v5-migration`; verify the linked source note for exact supported claims.
- [Svelte Documentation: Scoped Styles](https://svelte.dev/docs/svelte/scoped-styles); retrieved 2026-11-01; source `src-03-svelte-scoped-styles`; verify the linked source note for exact supported claims.
- [Vue 3 Documentation: Application API (createApp, mount, unmount)](https://vuejs.org/api/application.html); retrieved 2026-11-01; source `src-03-vue-application-api`; verify the linked source note for exact supported claims.
- [Vue 3 Documentation: Single-File Component CSS Features](https://vuejs.org/api/sfc-css-features.html); retrieved 2026-11-01; source `src-03-vue-sfc-css-features`; verify the linked source note for exact supported claims.

No fabricated quotations or page numbers. Source relationships do not establish independent corroboration. Runtime behavior remains untested here.

## Brain hooks

Folded into [[UI frameworks in plugins Vanilla DOM, React, Svelte, and Vue]]. Verify with [[Runtime Acceptance Matrix]] and [[Claim Verification Flow]].
