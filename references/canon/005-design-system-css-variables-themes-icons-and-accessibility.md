# 005. Design system, CSS variables, themes, icons, and accessibility

Distilled official documentation, retrieved 2026-11-01; confidence: practitioner for the integration recipe. All source statements are labeled paraphrases.

Core thesis: Make the plugin belong to the active theme.

## How to use it

1. [practitioner] Use scoped classes and Obsidian CSS variables for surfaces, text, and spacing.
2. [practitioner] Keep layout rules in styles.css and limit selectors to the plugin root.
3. [practitioner] Design loading, empty, error, narrow-pane, and high-contrast states alongside the happy path.
4. [practitioner] Verify focus visibility, labels, and reduced motion in the actual rendered interface.

## Evidence and caveats

- [Obsidian plugin guidelines](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md); retrieved 2026-11-01; source `SRC-01-001`; verify the linked source note for exact supported claims.
- [Obsidian CSS variables and styling](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/CSS%20variables/About%20styling.md); retrieved 2026-11-01; source `SRC-02-006`; verify the linked source note for exact supported claims.
- [Obsidian icons](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Icons.md); retrieved 2026-11-01; source `SRC-02-009`; verify the linked source note for exact supported claims.

No fabricated quotations or page numbers. Source relationships do not establish independent corroboration. Runtime behavior remains untested here.

## Brain hooks

Folded into [[Design system, CSS variables, themes, icons, and accessibility]]. Verify with [[Runtime Acceptance Matrix]] and [[Claim Verification Flow]].
