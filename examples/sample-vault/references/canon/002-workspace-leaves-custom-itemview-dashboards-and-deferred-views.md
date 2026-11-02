# 002. Workspace leaves, custom ItemView dashboards, and deferred views

Distilled official documentation, retrieved 2026-11-01; confidence: practitioner for the integration recipe. All source statements are labeled paraphrases.

Core thesis: Treat each workspace leaf as an independent view.

## How to use it

1. [practitioner] Register a view factory and keep per-leaf state in the view.
2. [practitioner] Persist serializable state separately from DOM nodes and renderer objects.
3. [practitioner] Resolve deferred leaves before relying on a concrete view instance.
4. [practitioner] Suspend work when a view is inactive and release view resources when it closes.

## Evidence and caveats

- [Obsidian plugin guidelines](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md); retrieved 2026-11-01; source `SRC-01-001`; verify the linked source note for exact supported claims.
- [Obsidian public TypeScript API declarations](https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts); retrieved 2026-11-01; source `SRC-01-002`; verify the linked source note for exact supported claims.
- [Obsidian custom ItemView interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Views.md); retrieved 2026-11-01; source `SRC-02-001`; verify the linked source note for exact supported claims.
- [Obsidian deferred view lifecycle](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Defer%20views.md); retrieved 2026-11-01; source `SRC-02-002`; verify the linked source note for exact supported claims.

No fabricated quotations or page numbers. Source relationships do not establish independent corroboration. Runtime behavior remains untested here.

## Brain hooks

Folded into [[Workspace leaves, custom ItemView dashboards, and deferred views]]. Verify with [[Runtime Acceptance Matrix]] and [[Claim Verification Flow]].
