---
type: "flow"
title: "Plugin Verification and Performance"
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
  - "https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Getting%20started/Mobile%20development.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Defer%20views.md"
  - "https://docs.obsidian.md/Plugins/Editor/Markdown+post+processing"
  - "https://threejs.org/manual/pages/how-to-dispose-of-objects.html"
---

# Plugin Verification and Performance

[practitioner] A real implementation needs evidence beyond code review or a static signal score.

## When to invoke

Use this playbook at the matching creator stage. It applies the cited official contracts; its sequence is engineering judgment.

## Prerequisites

Read [[Plugin Creator Studio]], the project brief, and the relevant technical concept. Record missing inputs as no data. Preserve unrelated work and immutable raw evidence.

## Step by step

1. Freeze the plugin artifact hash, lockfile hash, app version, OS/device, fixture, commands, and expected result for every test run.
2. Run meaningful domain tests, TypeScript checks, the actual bundle, and official lint. Keep their results distinct from Obsidian execution.
3. Test enable/disable, reload, repeated view open/close, split panes, deferred restoration, hidden panes, and app restart.
4. Test editor features in Source and Live Preview plus Reading view/embeds when parity is part of the promise. Include selection, undo, composition input, and long documents.
5. Test rename, deletion, external edits, incomplete metadata, malformed input, cancelled requests, and failed persistence with recovery.
6. Set product-specific startup, interaction, render, memory, bundle, and storage budgets before measuring. Unmeasured budgets are unverified, not satisfied.
7. Benchmark representative small and large sanitized vaults. Retain sample count, fixture dimensions, cold/warm distinction, and actual observations.
8. Inspect detached DOM, active observers, render loops, workers, and GPU resources across repeated lifecycle operations.
9. Test real iOS and Android devices for advertised mobile support. Record touch, keyboard, app background/resume, storage, and unsupported rendering behavior.
10. Retain negative results, owner, severity, reproduction, evidence path, and the next action. Release readiness remains incomplete while mandatory rows are unknown.

## Outputs

- ACCEPTANCE_RECORD.md
- Performance budget and measured run records
- A failure ledger tied to the exact artifact

## Quality gates

- Every acceptance claim cites the evidence class that supports it
- Required runtime/device rows have observed outcomes
- Performance statements include samples and conditions

## Failure modes

- Calling compiler success a runtime pass
- Treating an empty profiler record as zero cost
- Comparing different fixtures or artifacts as if they were a controlled benchmark

## Sources

Paraphrase and application; no independent corroboration is implied by repeated upstream works.

- [[Source SRC-04-028]]: [Obsidian Developer Documentation - Optimize plugin load time](https://docs.obsidian.md/Plugins/Guides/Optimize+plugin+load+time), retrieved 2026-11-01.
- [[Source SRC-01-008]]: [Obsidian mobile development](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Getting%20started/Mobile%20development.md), retrieved 2026-11-01.
- [[Source SRC-02-002]]: [Obsidian deferred view lifecycle](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Defer%20views.md), retrieved 2026-11-01.
- [[Source SRC-04-016]]: [Obsidian Developer Documentation - Markdown post processing](https://docs.obsidian.md/Plugins/Editor/Markdown+post+processing), retrieved 2026-11-01.
- [[Source src-03-threejs-dispose-manual]]: [Three.js Manual: How to Dispose of Objects](https://threejs.org/manual/pages/how-to-dispose-of-objects.html), retrieved 2026-11-01.

## Related

- [[Plugin Creator Studio]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
- [[Research Pack]]
- [[Plugin Discovery and Brief]]
- [[Plugin Architecture and API Contract]]
- [[Plugin UX and Accessibility]]
- [[Plugin Data and Integration Design]]
