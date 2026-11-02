# 004. Modals, suggest interfaces, menus, settings tabs, and SecretStorage

Distilled official documentation, retrieved 2026-11-01; confidence: practitioner for the integration recipe. All source statements are labeled paraphrases.

Core thesis: Use the narrowest interaction surface.

## How to use it

1. [practitioner] Choose commands for actions, modals for focused decisions, and suggests for searchable choices.
2. [practitioner] Keep settings persistent, validate input, and separate secret identifiers from secret values.
3. [practitioner] Feature-check newer settings and secret APIs against the declared app version.
4. [practitioner] Provide keyboard navigation, cancellation, and clear error feedback.

## Evidence and caveats

- [Obsidian public TypeScript API declarations](https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts); retrieved 2026-11-01; source `SRC-01-002`; verify the linked source note for exact supported claims.
- [Obsidian modals and suggestion interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Modals.md); retrieved 2026-11-01; source `SRC-02-004`; verify the linked source note for exact supported claims.
- [Obsidian plugin settings interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Settings.md); retrieved 2026-11-01; source `SRC-02-005`; verify the linked source note for exact supported claims.
- [Obsidian SecretStorage and SecretComponent guide](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Store%20secrets.md); retrieved 2026-11-01; source `SRC-02-007`; verify the linked source note for exact supported claims.
- [Migrate Obsidian plugins to declarative settings](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Migrate%20to%20declarative%20settings.md); retrieved 2026-11-01; source `SRC-02-008`; verify the linked source note for exact supported claims.

No fabricated quotations or page numbers. Source relationships do not establish independent corroboration. Runtime behavior remains untested here.

## Brain hooks

Folded into [[Modals, suggest interfaces, menus, settings tabs, and SecretStorage]]. Verify with [[Runtime Acceptance Matrix]] and [[Claim Verification Flow]].
