---
type: "concept"
title: "CodeMirror 6 architecture, StateFields, ViewPlugins, and Live Preview"
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
  - "[[Source SRC-04-001]]"
  - "[[Source SRC-04-002]]"
  - "[[Source SRC-04-003]]"
  - "[[Source SRC-04-004]]"
  - "[[Source SRC-04-005]]"
  - "[[Source SRC-04-006]]"
  - "[[Source SRC-04-007]]"
  - "[[Source SRC-04-008]]"
  - "[[Source SRC-04-009]]"
  - "[[Source SRC-04-010]]"
  - "[[Source SRC-04-011]]"
  - "[[Source SRC-04-012]]"
  - "[[Source SRC-04-013]]"
  - "[[Source SRC-04-014]]"
  - "[[Source SRC-04-015]]"
  - "[[Source SRC-04-022]]"
  - "[[Source SRC-04-026]]"
  - "[[Source SRC-06-002]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-sample-plugin/blob/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/esbuild.config.mjs"
  - "https://docs.obsidian.md/Plugins/Editor/Editor"
  - "https://docs.obsidian.md/Plugins/Editor/Editor+extensions"
  - "https://docs.obsidian.md/Plugins/Editor/Communicating+with+editor+extensions"
  - "https://docs.obsidian.md/Plugins/Editor/State+management"
  - "https://docs.obsidian.md/Plugins/Editor/State+fields"
  - "https://docs.obsidian.md/Plugins/Editor/View+plugins"
  - "https://docs.obsidian.md/Plugins/Editor/Decorations"
  - "https://docs.obsidian.md/Plugins/Editor/Viewport"
  - "https://docs.obsidian.md/Plugins/User+interface/Status+bar"
  - "https://codemirror.net/docs/guide/"
  - "https://codemirror.net/docs/ref/"
  - "https://codemirror.net/examples/gutter/"
  - "https://codemirror.net/examples/config/"
  - "https://raw.githubusercontent.com/codemirror/state/main/src/facet.ts"
  - "https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/master/esbuild.config.mjs"
  - "https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines"
  - "https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts"
  - "https://registry.npmjs.org/obsidian/1.14.4"
---

# CodeMirror 6 architecture, StateFields, ViewPlugins, and Live Preview

Keep editor state and rendered decorations separate.

## Verified source guidance

Paraphrases from the dated sources below. Repeated upstream origins are consistency checks, not independent corroboration.

### Official sample plugin esbuild configuration

- [evidence-based] The official sample builds src/main.ts into main.js using esbuild bundling and CommonJS output. ([[Source SRC-01-007]])
- [evidence-based] The sample external list includes obsidian, electron, named @codemirror and @lezer packages, and Node builtinModules so those imports are not bundled into main.js. ([[Source SRC-01-007]])
- [evidence-based] The sample production build disables inline sourcemaps, enables minification, and uses a one-shot rebuild; development uses context.watch. ([[Source SRC-01-007]])

### Obsidian Developer Documentation - Editor

- [evidence-based] The Obsidian Editor abstraction exposes selections, cursors, and text replacement without requiring direct CodeMirror access. ([[Source SRC-04-001]])

### Obsidian Developer Documentation - Editor extensions

- [evidence-based] Obsidian editor extensions use CodeMirror 6 and are registered with registerEditorExtension. Reading view customization instead uses Markdown post processing. ([[Source SRC-04-002]])

### Obsidian Developer Documentation - Communicating with editor extensions

- [practitioner] The communication guide describes obtaining the underlying CodeMirror view through a property absent from the public Editor typings. Treat this access as an explicitly documented integration caveat. ([[Source SRC-04-003]])
- [evidence-based] CodeMirror view plugins can be queried through EditorView.plugin and custom state can be changed through dispatched effects. ([[Source SRC-04-003]])

### Obsidian Developer Documentation - State management

- [evidence-based] CodeMirror represents state as immutable values and applies document and selection changes through transactions. ([[Source SRC-04-004]])

### Obsidian Developer Documentation - State fields

- [evidence-based] StateField defines custom editor state with create and update functions; StateEffect carries typed effects in transactions. ([[Source SRC-04-005]])

### Obsidian Developer Documentation - View plugins

- [evidence-based] A CodeMirror ViewPlugin can maintain per-view state and implement update and destroy lifecycle methods. Layout-affecting decorations require the appropriate state-based provider. ([[Source SRC-04-006]])

### Obsidian Developer Documentation - Decorations

- [evidence-based] CodeMirror decorations support marks, widgets, replacement ranges, and line styling. A view plugin can limit scanning to visible ranges. ([[Source SRC-04-007]])

### Obsidian Developer Documentation - Viewport

- [evidence-based] CodeMirror renders a viewport rather than all document content into DOM; extensions must account for visible range and viewport changes. ([[Source SRC-04-008]])

### Obsidian Developer Documentation - Status bar

- [evidence-based] addStatusBarItem creates a status bar element that is cleaned up with the plugin. Obsidian status bar items are unavailable on mobile. ([[Source SRC-04-009]])

### CodeMirror 6 Documentation - System Guide

- [evidence-based] CodeMirror separates immutable editor state from the DOM-facing EditorView; application code should update editor state through transactions. ([[Source SRC-04-010]])

### CodeMirror 6 Documentation - Reference Manual

- [evidence-based] CodeMirror decoration providers that run after viewport computation cannot introduce block widgets or replacements spanning line breaks. ([[Source SRC-04-011]])
- [evidence-based] WidgetType supports DOM creation, equality comparison, and destruction; requestMeasure can notify the editor when layout needs measuring. ([[Source SRC-04-011]])

### CodeMirror 6 Example - Custom Gutters

- [evidence-based] CodeMirror custom gutters use gutter and GutterMarker; markers can define their DOM and equality behavior. ([[Source SRC-04-012]])

### CodeMirror 6 Example - Configuration and Compartments

- [evidence-based] CodeMirror Compartment wraps an extension so a transaction can reconfigure that part of an editor configuration. ([[Source SRC-04-013]])

### CodeMirror 6 @codemirror/state Source - src/facet.ts

- [evidence-based] The CodeMirror state source validates extension identity and reports that duplicate module instances can break instanceof checks. ([[Source SRC-04-014]])

### Obsidian Sample Plugin - esbuild.config.mjs

- [evidence-based] The official sample esbuild configuration externalizes Obsidian, Electron, named CodeMirror and Lezer packages, and Node built-ins rather than bundling them. ([[Source SRC-04-015]])

### Obsidian Developer Documentation - Plugin guidelines

- [evidence-based] Plugin guidelines prefer Editor APIs for editing the active note, processFrontMatter for frontmatter, and Vault APIs for normal vault files. ([[Source SRC-04-022]])
- [evidence-based] Guidelines recommend direct file lookup APIs, normalizePath for user paths, and safe DOM construction instead of assigning untrusted HTML. ([[Source SRC-04-022]])

### Obsidian Official TypeScript API Definitions - obsidian.d.ts

- [evidence-based] The official typings expose editorLivePreviewField, editorInfoField, link parsing helpers, and APIs for opening files with editor state. Minimum supported versions must be checked against the target typings. ([[Source SRC-04-026]])

### Obsidian npm API package 1.14.4 metadata

- [evidence-based] Obsidian API package 1.14.4 declares peer versions @codemirror/view 6.43.13 and @codemirror/state 6.7.6. ([[Source SRC-06-002]])
- [evidence-based] Package metadata records dependency compatibility declarations; it does not establish runtime compatibility of a generated plugin. ([[Source SRC-06-002]])

## Engineering recipe

[practitioner] This sequence applies the cited contracts; it is not a tested plugin implementation.

1. Choose a StateField for durable editor state and a ViewPlugin for view-scoped behavior.
2. Derive decorations from the current document and viewport instead of mutating the editor DOM.
3. Register extensions through Obsidian and avoid bundling duplicate editor runtime modules.
4. Keep the feature useful in Source mode and explicitly test Live Preview.

## Verification

[practitioner] Test selection, undo/redo, composition input, large notes, and editor recreation.

Record app version, operating system, plugin artifact hash, input size, observed outcome, and evidence path in [[Runtime Acceptance Matrix]].

## Limits

This brain has no physical-device result for this recipe. A static scan cannot prove lifecycle correctness, mobile support, rendering performance, or submission acceptance. Refresh policy and API claims before release.

## Sources

- [Official sample plugin esbuild configuration](https://github.com/obsidianmd/obsidian-sample-plugin/blob/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/esbuild.config.mjs), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - Editor](https://docs.obsidian.md/Plugins/Editor/Editor), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - Editor extensions](https://docs.obsidian.md/Plugins/Editor/Editor+extensions), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - Communicating with editor extensions](https://docs.obsidian.md/Plugins/Editor/Communicating+with+editor+extensions), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - State management](https://docs.obsidian.md/Plugins/Editor/State+management), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - State fields](https://docs.obsidian.md/Plugins/Editor/State+fields), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - View plugins](https://docs.obsidian.md/Plugins/Editor/View+plugins), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - Decorations](https://docs.obsidian.md/Plugins/Editor/Decorations), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - Viewport](https://docs.obsidian.md/Plugins/Editor/Viewport), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - Status bar](https://docs.obsidian.md/Plugins/User+interface/Status+bar), retrieved 2026-11-01, refresh due 2026-12-01.
- [CodeMirror 6 Documentation - System Guide](https://codemirror.net/docs/guide/), retrieved 2026-11-01, refresh due 2026-12-01.
- [CodeMirror 6 Documentation - Reference Manual](https://codemirror.net/docs/ref/), retrieved 2026-11-01, refresh due 2026-12-01.
- [CodeMirror 6 Example - Custom Gutters](https://codemirror.net/examples/gutter/), retrieved 2026-11-01, refresh due 2026-12-01.
- [CodeMirror 6 Example - Configuration and Compartments](https://codemirror.net/examples/config/), retrieved 2026-11-01, refresh due 2026-12-01.
- [CodeMirror 6 @codemirror/state Source - src/facet.ts](https://raw.githubusercontent.com/codemirror/state/main/src/facet.ts), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Sample Plugin - esbuild.config.mjs](https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/master/esbuild.config.mjs), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation - Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Official TypeScript API Definitions - obsidian.d.ts](https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian npm API package 1.14.4 metadata](https://registry.npmjs.org/obsidian/1.14.4), retrieved 2026-11-01, refresh due 2026-12-01.

## Related

- [[Source SRC-01-007]]
- [[Source SRC-04-001]]
- [[Source SRC-04-002]]
- [[Source SRC-04-003]]
- [[Source SRC-04-004]]
- [[Source SRC-04-005]]
- [[Source SRC-04-006]]
- [[Source SRC-04-007]]
- [[Source SRC-04-008]]
- [[Source SRC-04-009]]
- [[Source SRC-04-010]]
- [[Source SRC-04-011]]
- [[Source SRC-04-012]]
- [[Source SRC-04-013]]
- [[Source SRC-04-014]]
- [[Source SRC-04-015]]
- [[Source SRC-04-022]]
- [[Source SRC-04-026]]
- [[Source SRC-06-002]]
- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[Obsidian Bases API, native dashboards, and query surfaces]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
