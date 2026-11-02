# 009. Markdown post-processors, codeblock widgets, and Reading view parity

Distilled official documentation, retrieved 2026-11-01; confidence: practitioner for the integration recipe. All source statements are labeled paraphrases.

Core thesis: Design Reading view parity explicitly.

## How to use it

1. [practitioner] Share the data model between editor widgets and Markdown processors.
2. [practitioner] Attach rendered resources to the processor's lifecycle rather than a global registry.
3. [practitioner] Handle repeated rendering and dispose observers, events, and framework roots.
4. [practitioner] Build DOM from validated values and treat external HTML as untrusted.

## Evidence and caveats

- [Obsidian Developer Documentation - Editor extensions](https://docs.obsidian.md/Plugins/Editor/Editor+extensions); retrieved 2026-11-01; source `SRC-04-002`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - Markdown post processing](https://docs.obsidian.md/Plugins/Editor/Markdown+post+processing); retrieved 2026-11-01; source `SRC-04-016`; verify the linked source note for exact supported claims.
- [Obsidian TypeScript API Reference - MarkdownPostProcessorContext](https://docs.obsidian.md/Reference/TypeScript+API/MarkdownPostProcessorContext); retrieved 2026-11-01; source `SRC-04-017`; verify the linked source note for exact supported claims.
- [Obsidian TypeScript API Reference - MarkdownRenderer](https://docs.obsidian.md/Reference/TypeScript+API/MarkdownRenderer); retrieved 2026-11-01; source `SRC-04-018`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - Manage plugin lifecycle](https://docs.obsidian.md/Plugins/Guides/Manage+plugin+lifecycle); retrieved 2026-11-01; source `SRC-04-019`; verify the linked source note for exact supported claims.
- [Official eslint-plugin-obsidianmd Rule - no-plugin-as-component](https://raw.githubusercontent.com/obsidianmd/eslint-plugin/master/lib/rules/noPluginAsComponent.ts); retrieved 2026-11-01; source `SRC-04-020`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation - Plugin guidelines](https://docs.obsidian.md/Plugins/Releasing/Plugin+guidelines); retrieved 2026-11-01; source `SRC-04-022`; verify the linked source note for exact supported claims.
- [Obsidian Official TypeScript API Definitions - obsidian.d.ts](https://raw.githubusercontent.com/obsidianmd/obsidian-api/master/obsidian.d.ts); retrieved 2026-11-01; source `SRC-04-026`; verify the linked source note for exact supported claims.

No fabricated quotations or page numbers. Source relationships do not establish independent corroboration. Runtime behavior remains untested here.

## Brain hooks

Folded into [[Markdown post-processors, codeblock widgets, and Reading view parity]]. Verify with [[Runtime Acceptance Matrix]] and [[Claim Verification Flow]].
