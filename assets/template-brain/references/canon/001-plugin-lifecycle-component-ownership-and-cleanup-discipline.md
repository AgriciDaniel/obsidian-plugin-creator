# 001. Plugin lifecycle, Component ownership, and cleanup discipline

Distilled official documentation, retrieved 2026-11-01; confidence: practitioner for the integration recipe. All source statements are labeled paraphrases.

Core thesis: Start with the smallest plugin lifecycle.

## How to use it

1. [practitioner] List each command, event, timer, observer, and component before implementing it.
2. [practitioner] Assign one lifecycle owner to every resource; write its cleanup beside its creation.
3. [practitioner] Keep onload focused on registration; defer expensive work until it is needed.
4. [practitioner] Exercise enable, disable, reload, and workspace restore before adding more features.

## Evidence and caveats

- [Obsidian plugin guidelines](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md); retrieved 2026-11-01; source `SRC-01-001`; verify the linked source note for exact supported claims.
- [Obsidian public TypeScript API declarations](https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts); retrieved 2026-11-01; source `SRC-01-002`; verify the linked source note for exact supported claims.
- [Obsidian manifest specification](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/Manifest.md); retrieved 2026-11-01; source `SRC-01-003`; verify the linked source note for exact supported claims.
- [Official Obsidian ESLint configuration guide](https://github.com/obsidianmd/eslint-plugin/blob/837b01dc1647cb3f0c532becb60ea83bec137656/docs/configuration.md); retrieved 2026-11-01; source `SRC-01-006`; verify the linked source note for exact supported claims.
- [Obsidian plugin event lifecycle](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Events.md); retrieved 2026-11-01; source `SRC-01-010`; verify the linked source note for exact supported claims.
- [Obsidian command interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Commands.md); retrieved 2026-11-01; source `SRC-01-011`; verify the linked source note for exact supported claims.

No fabricated quotations or page numbers. Source relationships do not establish independent corroboration. Runtime behavior remains untested here.

## Brain hooks

Folded into [[Plugin lifecycle, Component ownership, and cleanup discipline]]. Verify with [[Runtime Acceptance Matrix]] and [[Claim Verification Flow]].
