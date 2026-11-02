---
type: "concept"
title: "UI frameworks in plugins Vanilla DOM, React, Svelte, and Vue"
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
  - "[[Source src-03-obsidian-css-colors-vars]]"
  - "[[Source src-03-obsidian-html-elements]]"
  - "[[Source src-03-obsidian-api-dts]]"
  - "[[Source src-03-obsidian-views-guide]]"
  - "[[Source src-03-obsidian-react-guide]]"
  - "[[Source src-03-react-createroot-docs]]"
  - "[[Source src-03-react-root-event-delegation]]"
  - "[[Source src-03-obsidian-svelte-guide]]"
  - "[[Source src-03-svelte-v5-imperative-api]]"
  - "[[Source src-03-svelte-v5-migration]]"
  - "[[Source src-03-svelte-scoped-styles]]"
  - "[[Source src-03-vue-application-api]]"
  - "[[Source src-03-vue-sfc-css-features]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
source_urls:
  - "https://docs.obsidian.md/Reference/CSS+variables/Foundations/Colors"
  - "https://docs.obsidian.md/Plugins/User+interface/HTML+elements"
  - "https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts"
  - "https://docs.obsidian.md/Plugins/User+interface/Views"
  - "https://docs.obsidian.md/Plugins/Getting+started/Use+React+in+your+plugin"
  - "https://react.dev/reference/react-dom/client/createRoot"
  - "https://legacy.reactjs.org/blog/2020/08/10/react-v17-rc.html"
  - "https://docs.obsidian.md/Plugins/Getting+started/Use+Svelte+in+your+plugin"
  - "https://svelte.dev/docs/svelte/imperative-component-api"
  - "https://svelte.dev/docs/svelte/v5-migration-guide"
  - "https://svelte.dev/docs/svelte/scoped-styles"
  - "https://vuejs.org/api/application.html"
  - "https://vuejs.org/api/sfc-css-features.html"
---

# UI frameworks in plugins Vanilla DOM, React, Svelte, and Vue

Choose a framework for a concrete interaction need.

## Verified source guidance

Paraphrases from the dated sources below. Repeated upstream origins are consistency checks, not independent corroboration.

### Obsidian Developer Documentation: Foundations Color CSS Variables

- [evidence-based] Obsidian documents semantic background, border, interactive, and text colors for themed interfaces. ([[Source src-03-obsidian-css-colors-vars]])
- [evidence-based] The current color reference marks legacy RGB and HSL variables deprecated as of Obsidian 1.13 and recommends color-mix with the corresponding color variables. ([[Source src-03-obsidian-css-colors-vars]])

### Obsidian Developer Documentation: HTML Elements

- [evidence-based] Obsidian provides createEl, createDiv, createSpan, and empty helpers for constructing and clearing DOM elements; text can be supplied without parsing HTML. ([[Source src-03-obsidian-html-elements]])

### Obsidian API TypeScript Definitions: obsidian.d.ts (DOM, SVG, and Popout Window Helpers)

- [practitioner] The public typings include createFragment, DOM creation options, and document/window helpers for DOM nodes. Use the owning document and window when handling popout views. ([[Source src-03-obsidian-api-dts]])

### Obsidian Developer Documentation: Views (ItemView Lifecycle)

- [evidence-based] The Views guide registers an ItemView factory, builds content in onOpen, and assigns resource cleanup to onClose; it warns against retaining view references in the plugin. ([[Source src-03-obsidian-views-guide]])

### Obsidian Developer Documentation: Use React in Your Plugin

- [evidence-based] The official React guide mounts a createRoot tree in ItemView.onOpen and unmounts it in onClose. It also demonstrates an App context hook. ([[Source src-03-obsidian-react-guide]])

### React Reference Documentation: createRoot (react-dom/client)

- [evidence-based] React createRoot mounts a tree in a DOM container; root.unmount removes that tree and lets its components clean up effects and subscriptions. ([[Source src-03-react-createroot-docs]])

### React Architectural Change: Root Container Event Delegation (React 17+)

- [evidence-based] The React 17 announcement explains that delegated event listeners moved from document to the root DOM container. ([[Source src-03-react-root-event-delegation]])

### Obsidian Developer Documentation: Use Svelte in Your Plugin

- [evidence-based] The official Svelte guide configures esbuild-svelte and Svelte checking, then mounts a component in ItemView.onOpen and unmounts it in onClose. ([[Source src-03-obsidian-svelte-guide]])

### Svelte 5 Documentation: Imperative Component API (mount and unmount)

- [evidence-based] Svelte exposes mount and unmount for imperative component lifecycles; these replace class instantiation and $destroy for current Svelte components. ([[Source src-03-svelte-v5-imperative-api]])

### Svelte 5 Documentation: Svelte 5 Migration Guide

- [evidence-based] Svelte 5 replaces class-based component instantiation with mount or hydrate. Its migration guide documents changes to component instance APIs. ([[Source src-03-svelte-v5-migration]])

### Svelte Documentation: Scoped Styles

- [evidence-based] Svelte scopes component styles with generated class names. Scoped CSS still requires care with global selectors and inherited properties. ([[Source src-03-svelte-scoped-styles]])

### Vue 3 Documentation: Application API (createApp, mount, unmount)

- [evidence-based] Vue createApp creates an application instance that supports provide, mount, and unmount for host-managed component lifecycles. ([[Source src-03-vue-application-api]])

### Vue 3 Documentation: Single-File Component CSS Features

- [evidence-based] Vue scoped styles use generated data attributes; deep and global selectors can intentionally cross component boundaries. ([[Source src-03-vue-sfc-css-features]])

## Engineering recipe

[practitioner] This sequence applies the cited contracts; it is not a tested plugin implementation.

1. Use the Obsidian Setting and DOM helpers for small native interfaces.
2. Mount a framework only inside a view-owned root and unmount it on cleanup.
3. Share domain state outside the framework so an editor widget and dashboard can reuse it.
4. Measure bundle size and startup cost; do not assume one framework is universally faster.

## Verification

[practitioner] Mount two independent roots, close one, then reload the plugin and inspect retained nodes.

Record app version, operating system, plugin artifact hash, input size, observed outcome, and evidence path in [[Runtime Acceptance Matrix]].

## Limits

This brain has no physical-device result for this recipe. A static scan cannot prove lifecycle correctness, mobile support, rendering performance, or submission acceptance. Refresh policy and API claims before release.

## Sources

- [Obsidian Developer Documentation: Foundations Color CSS Variables](https://docs.obsidian.md/Reference/CSS+variables/Foundations/Colors), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation: HTML Elements](https://docs.obsidian.md/Plugins/User+interface/HTML+elements), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian API TypeScript Definitions: obsidian.d.ts (DOM, SVG, and Popout Window Helpers)](https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation: Views (ItemView Lifecycle)](https://docs.obsidian.md/Plugins/User+interface/Views), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation: Use React in Your Plugin](https://docs.obsidian.md/Plugins/Getting+started/Use+React+in+your+plugin), retrieved 2026-11-01, refresh due 2026-12-01.
- [React Reference Documentation: createRoot (react-dom/client)](https://react.dev/reference/react-dom/client/createRoot), retrieved 2026-11-01, refresh due 2026-12-01.
- [React Architectural Change: Root Container Event Delegation (React 17+)](https://legacy.reactjs.org/blog/2020/08/10/react-v17-rc.html), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation: Use Svelte in Your Plugin](https://docs.obsidian.md/Plugins/Getting+started/Use+Svelte+in+your+plugin), retrieved 2026-11-01, refresh due 2026-12-01.
- [Svelte 5 Documentation: Imperative Component API (mount and unmount)](https://svelte.dev/docs/svelte/imperative-component-api), retrieved 2026-11-01, refresh due 2026-12-01.
- [Svelte 5 Documentation: Svelte 5 Migration Guide](https://svelte.dev/docs/svelte/v5-migration-guide), retrieved 2026-11-01, refresh due 2026-12-01.
- [Svelte Documentation: Scoped Styles](https://svelte.dev/docs/svelte/scoped-styles), retrieved 2026-11-01, refresh due 2026-12-01.
- [Vue 3 Documentation: Application API (createApp, mount, unmount)](https://vuejs.org/api/application.html), retrieved 2026-11-01, refresh due 2026-12-01.
- [Vue 3 Documentation: Single-File Component CSS Features](https://vuejs.org/api/sfc-css-features.html), retrieved 2026-11-01, refresh due 2026-12-01.

## Related

- [[Source src-03-obsidian-css-colors-vars]]
- [[Source src-03-obsidian-html-elements]]
- [[Source src-03-obsidian-api-dts]]
- [[Source src-03-obsidian-views-guide]]
- [[Source src-03-obsidian-react-guide]]
- [[Source src-03-react-createroot-docs]]
- [[Source src-03-react-root-event-delegation]]
- [[Source src-03-obsidian-svelte-guide]]
- [[Source src-03-svelte-v5-imperative-api]]
- [[Source src-03-svelte-v5-migration]]
- [[Source src-03-svelte-scoped-styles]]
- [[Source src-03-vue-application-api]]
- [[Source src-03-vue-sfc-css-features]]
- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[Obsidian Bases API, native dashboards, and query surfaces]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
