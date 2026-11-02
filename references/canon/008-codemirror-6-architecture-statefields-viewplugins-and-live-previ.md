# 008. CodeMirror 6 architecture, StateFields, ViewPlugins, and Live Preview

Distilled official documentation, retrieved 2026-11-01; confidence: practitioner for the integration recipe. All source statements are labeled paraphrases.

Core thesis: Keep editor state and rendered decorations separate.

## How to use it

1. [practitioner] Choose a StateField for durable editor state and a ViewPlugin for view-scoped behavior.
2. [practitioner] Derive decorations from the current document and viewport instead of mutating the editor DOM.
3. [practitioner] Register extensions through Obsidian and avoid bundling duplicate editor runtime modules.
4. [practitioner] Keep the feature useful in Source mode and explicitly test Live Preview.

## Evidence and caveats

- [Official sample plugin esbuild configuration](https://github.com/obsidianmd/obsidian-sample-plugin/blob/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/esbuild.config.mjs); retrieved 2026-11-01; source `SRC-01-007`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - Editor](https://docs.obsidian.md/Plugins/Editor/Editor); retrieved 2026-11-01; source `SRC-04-001`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - Editor extensions](https://docs.obsidian.md/Plugins/Editor/Editor+extensions); retrieved 2026-11-01; source `SRC-04-002`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - Communicating with editor extensions](https://docs.obsidian.md/Plugins/Editor/Communicating+with+editor+extensions); retrieved 2026-11-01; source `SRC-04-003`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - State management](https://docs.obsidian.md/Plugins/Editor/State+management); retrieved 2026-11-01; source `SRC-04-004`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - State fields](https://docs.obsidian.md/Plugins/Editor/State+fields); retrieved 2026-11-01; source `SRC-04-005`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - View plugins](https://docs.obsidian.md/Plugins/Editor/View+plugins); retrieved 2026-11-01; source `SRC-04-006`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - Decorations](https://docs.obsidian.md/Plugins/Editor/Decorations); retrieved 2026-11-01; source `SRC-04-007`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - Viewport](https://docs.obsidian.md/Plugins/Editor/Viewport); retrieved 2026-11-01; source `SRC-04-008`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - Status bar](https://docs.obsidian.md/Plugins/User+interface/Status+bar); retrieved 2026-11-01; source `SRC-04-009`; verify the linked source note for exact supported claims.
- [CodeMirror 6 Documentation - System Guide](https://codemirror.net/docs/guide/); retrieved 2026-11-01; source `SRC-04-010`; verify the linked source note for exact supported claims.
- [CodeMirror 6 Documentation - Reference Manual](https://codemirror.net/docs/ref/); retrieved 2026-11-01; source `SRC-04-011`; verify the linked source note for exact supported claims.
- [CodeMirror 6 Example - Custom Gutters](https://codemirror.net/examples/gutter/); retrieved 2026-11-01; source `SRC-04-012`; verify the linked source note for exact supported claims.
- [CodeMirror 6 Example - Configuration and Compartments](https://codemirror.net/examples/config/); retrieved 2026-11-01; source `SRC-04-013`; verify the linked source note for exact supported claims.
- [CodeMirror 6 @codemirror/state Source - src/facet.ts](https://raw.githubusercontent.com/codemirror/state/main/src/facet.ts); retrieved 2026-11-01; source `SRC-04-014`; verify the linked source note for exact supported claims.
- [Obsidian Sample Plugin - esbuild.config.mjs](https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/master/esbuild.config.mjs); retrieved 2026-11-01; source `SRC-04-015`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines); retrieved 2026-11-01; source `SRC-04-022`; verify the linked source note for exact supported claims.
- [Obsidian Official TypeScript API Definitions - obsidian.d.ts](https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts); retrieved 2026-11-01; source `SRC-04-026`; verify the linked source note for exact supported claims.
- [Obsidian npm API package 1.14.4 metadata](https://registry.npmjs.org/obsidian/1.14.4); retrieved 2026-11-01; source `SRC-06-002`; verify the linked source note for exact supported claims.

No fabricated quotations or page numbers. Source relationships do not establish independent corroboration. Runtime behavior remains untested here.

## Brain hooks

Folded into [[CodeMirror 6 architecture, StateFields, ViewPlugins, and Live Preview]]. Verify with [[Runtime Acceptance Matrix]] and [[Claim Verification Flow]].
