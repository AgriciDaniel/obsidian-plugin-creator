---
type: "flow"
title: "Plugin UX and Accessibility"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/flow"
  - "confidence/practitioner"
related:
  - "[[Plugin Creator Studio]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
  - "[[Research Pack]]"
  - "[[Plugin Discovery and Brief]]"
  - "[[Plugin Architecture and API Contract]]"
  - "[[Plugin Data and Integration Design]]"
  - "[[Plugin Implementation Workflow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Modals.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Settings.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/CSS%20variables/About%20styling.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Icons.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md"
---

# Plugin UX and Accessibility

[practitioner] A command, modal, settings page, dashboard, editor widget, or visual needs a coherent interaction design.

## When to invoke

Use this playbook at the matching creator stage. It applies the cited official contracts; its sequence is engineering judgment.

## Prerequisites

Read [[Plugin Creator Studio]], the project brief, and the relevant technical concept. Record missing inputs as no data. Preserve unrelated work and immutable raw evidence.

## Step by step

1. Write the main task as a short path from trigger to result. Put the next useful action where the user reaches a decision.
2. Define loading, success, empty, partial data, invalid input, offline, permission, cancellation, and retry states alongside the primary screen.
3. Choose commands for quick actions, suggests for search/selection, modals for focused decisions, settings for configuration, and views for persistent work.
4. Use scoped classes and theme variables for colors, spacing, surfaces, and typography. Verify custom CSS does not affect unrelated views.
5. Specify focus order, visible focus, accessible names, semantic controls, Escape behavior, keyboard shortcuts, and return of focus after dismissal.
6. Design for narrow split panes, touch input, zoom, reduced motion, and long translated labels. Do not treat desktop resize emulation as mobile evidence.
7. Give Canvas/WebGL content a readable text alternative and a non-pointer path through important actions.
8. Keep labels concise and state errors in terms of the user's next action. Show missing data explicitly; do not turn unknown metrics into zero.
9. Test actual light and dark themes, keyboard-only completion, screen-reader semantics, and large content in Obsidian.
10. Retain observed results and screenshots for the artifact tested. A screenshot alone does not establish keyboard or screen-reader behavior.

## Outputs

- UI_STATE_SPEC.md
- Keyboard and assistive-technology acceptance cases
- Theme and responsive behavior decisions

## Quality gates

- Every important state has a useful next action
- Core actions have semantic keyboard-accessible controls
- Visual interfaces have meaningful accessible alternatives

## Failure modes

- Polishing only the populated happy path
- Hardcoding theme colors or globally broad CSS
- Advertising accessibility based only on a static screenshot

## Sources

Paraphrase and application; no independent corroboration is implied by repeated upstream works.

- [[Source SRC-02-004]]: [Obsidian modals and suggestion interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Modals.md), retrieved 2026-11-01.
- [[Source SRC-02-005]]: [Obsidian plugin settings interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Settings.md), retrieved 2026-11-01.
- [[Source SRC-02-006]]: [Obsidian CSS variables and styling](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/CSS%20variables/About%20styling.md), retrieved 2026-11-01.
- [[Source SRC-02-009]]: [Obsidian icons](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Icons.md), retrieved 2026-11-01.
- [[Source SRC-01-001]]: [Obsidian plugin guidelines](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md), retrieved 2026-11-01.

## Related

- [[Plugin Creator Studio]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
- [[Research Pack]]
- [[Plugin Discovery and Brief]]
- [[Plugin Architecture and API Contract]]
- [[Plugin Data and Integration Design]]
- [[Plugin Implementation Workflow]]
