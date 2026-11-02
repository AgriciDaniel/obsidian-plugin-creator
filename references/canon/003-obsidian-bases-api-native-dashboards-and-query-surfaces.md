# 003. Obsidian Bases API, native dashboards, and query surfaces

Distilled official documentation, retrieved 2026-11-01; confidence: practitioner for the integration recipe. All source statements are labeled paraphrases.

Core thesis: Choose Bases for a data query surface.

## How to use it

1. [practitioner] Use a Bases custom view when the product consumes a Bases query and its property model.
2. [practitioner] Use ItemView when the product owns a workspace independent of a Bases query.
3. [practitioner] Use a Markdown code block when a note should carry a small embedded surface.
4. [practitioner] Check the target API declaration and minimum app version before choosing a signature.

## Evidence and caveats

- [Obsidian public TypeScript API declarations](https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts); retrieved 2026-11-01; source `SRC-01-002`; verify the linked source note for exact supported claims.
- [Build a custom Obsidian Bases view](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Build%20a%20Bases%20view.md); retrieved 2026-11-01; source `SRC-02-003`; verify the linked source note for exact supported claims.

No fabricated quotations or page numbers. Source relationships do not establish independent corroboration. Runtime behavior remains untested here.

## Brain hooks

Folded into [[Obsidian Bases API, native dashboards, and query surfaces]]. Verify with [[Runtime Acceptance Matrix]] and [[Claim Verification Flow]].
