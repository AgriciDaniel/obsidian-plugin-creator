---
type: "concept"
title: "Design system, CSS variables, themes, icons, and accessibility"
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
  - "[[Source SRC-01-001]]"
  - "[[Source SRC-02-006]]"
  - "[[Source SRC-02-009]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/CSS%20variables/About%20styling.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Icons.md"
---

# Design system, CSS variables, themes, icons, and accessibility

Make the plugin belong to the active theme.

## Verified source guidance

Paraphrases from the dated sources below. Repeated upstream origins are consistency checks, not independent corroboration.

### Obsidian plugin guidelines

- [evidence-based] Use the plugin-provided this.app reference rather than the debugging global app object. ([[Source SRC-01-001]])
- [evidence-based] Release plugin resources on unload through registered lifecycle ownership where possible; do not detach workspace leaves in onunload. ([[Source SRC-01-001]])
- [evidence-based] Avoid retaining custom view instances on the Plugin class; locate live view instances through the workspace. ([[Source SRC-01-001]])
- [evidence-based] Construct user-facing DOM with DOM APIs or Obsidian helpers instead of interpolating user input into innerHTML, outerHTML, or insertAdjacentHTML. ([[Source SRC-01-001]])
- [evidence-based] Use CSS classes and Obsidian CSS variables instead of hardcoded visual styling in plugin TypeScript. ([[Source SRC-01-001]])

### Obsidian CSS variables and styling

- [evidence-based] Obsidian exposes CSS variables for consistent interface styling across the app. ([[Source SRC-02-006]])
- [evidence-based] Using built-in CSS variables for plugin elements supports native-looking interfaces compatible with community themes. ([[Source SRC-02-006]])
- [evidence-based] Ship plugin CSS classes in styles.css and reference variables such as --background-secondary instead of fixed theme-specific colors. ([[Source SRC-02-006]])

### Obsidian icons

- [evidence-based] Use setIcon to insert an available named icon into a custom interface element. ([[Source SRC-02-009]])
- [evidence-based] Set --icon-size with a documented size variable to control icon dimensions. ([[Source SRC-02-009]])
- [evidence-based] addIcon registers custom SVG content without the surrounding svg tag; the guide specifies a 0 0 100 100 view box for that custom icon content. ([[Source SRC-02-009]])

## Engineering recipe

[practitioner] This sequence applies the cited contracts; it is not a tested plugin implementation.

1. Use scoped classes and Obsidian CSS variables for surfaces, text, and spacing.
2. Keep layout rules in styles.css and limit selectors to the plugin root.
3. Design loading, empty, error, narrow-pane, and high-contrast states alongside the happy path.
4. Verify focus visibility, labels, and reduced motion in the actual rendered interface.

## Verification

[practitioner] Switch light/dark themes and test a narrow split pane with keyboard-only input.

Record app version, operating system, plugin artifact hash, input size, observed outcome, and evidence path in [[Runtime Acceptance Matrix]].

## Limits

This brain has no physical-device result for this recipe. A static scan cannot prove lifecycle correctness, mobile support, rendering performance, or submission acceptance. Refresh policy and API claims before release.

## Sources

- [Obsidian plugin guidelines](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian CSS variables and styling](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/CSS%20variables/About%20styling.md), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian icons](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Icons.md), retrieved 2026-11-01, refresh due 2026-12-01.

## Related

- [[Source SRC-01-001]]
- [[Source SRC-02-006]]
- [[Source SRC-02-009]]
- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[Obsidian Bases API, native dashboards, and query surfaces]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
