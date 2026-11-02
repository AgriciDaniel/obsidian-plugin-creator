---
type: "flow"
title: "Plugin Debugging and Learning"
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
  - "[[Plugin UX and Accessibility]]"
  - "[[Plugin Data and Integration Design]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md"
  - "https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Defer%20views.md"
  - "https://codemirror.net/docs/ref/"
---

# Plugin Debugging and Learning

[practitioner] A bug, slow operation, integration failure, or disputed design needs a reproducible diagnosis.

## When to invoke

Use this playbook at the matching creator stage. It applies the cited official contracts; its sequence is engineering judgment.

## Prerequisites

Read [[Plugin Creator Studio]], the project brief, and the relevant technical concept. Record missing inputs as no data. Preserve unrelated work and immutable raw evidence.

## Step by step

1. Capture the user's task, expected result, observed result, app/plugin versions, artifact hash, and smallest reproducible fixture.
2. Classify evidence as source declaration, static scan, compiler/lint, desktop runtime, physical device, network response, or human observation.
3. Reproduce with a minimal disposable vault and the smallest plugin feature set. Preserve the original failure and avoid private vault uploads.
4. For editor failures, inspect host-module duplication, selection/transaction logic, viewport assumptions, and Source/Live Preview differences.
5. For view failures, inspect deferred leaves, per-leaf state, lifecycle ownership, event subscriptions, resize behavior, and retained DOM.
6. For data failures, inspect schema versions, missing metadata, rename/delete races, cache invalidation, and incomplete rollback.
7. For visual failures, separate unsupported context, renderer initialization, layout sizing, resource disposal, and demand-render scheduling.
8. Form one falsifiable hypothesis and change one material factor at a time. Record contradictory observations rather than selecting only the preferred result.
9. Fix the cause, add a meaningful regression, and rerun the affected acceptance slice on the new artifact.
10. Fold the lesson into the project's handoff and the brain only when it has reusable scope, sources, evidence, and explicit limitations.

## Outputs

- A minimal reproduction and failure record
- A verified repair and regression
- SESSION_HANDOFF.md with preserved dissent and next action

## Quality gates

- The original failure is reproducible or honestly remains unverified
- The repair addresses the observed trigger
- The lesson does not generalize beyond its evidence

## Failure modes

- Changing several dependencies and surfaces at once
- Deleting negative evidence after a successful retry
- Turning a single device observation into a universal platform claim

## Sources

Paraphrase and application; no independent corroboration is implied by repeated upstream works.

- [[Source SRC-01-001]]: [Obsidian plugin guidelines](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md), retrieved 2026-11-01.
- [[Source SRC-04-028]]: [Obsidian Developer Documentation - Optimize plugin load time](https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time), retrieved 2026-11-01.
- [[Source SRC-02-002]]: [Obsidian deferred view lifecycle](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Defer%20views.md), retrieved 2026-11-01.
- [[Source SRC-04-011]]: [CodeMirror 6 Documentation - Reference Manual](https://codemirror.net/docs/ref/), retrieved 2026-11-01.

## Related

- [[Plugin Creator Studio]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
- [[Research Pack]]
- [[Plugin Discovery and Brief]]
- [[Plugin Architecture and API Contract]]
- [[Plugin UX and Accessibility]]
- [[Plugin Data and Integration Design]]
