---
type: "flow"
title: "Plugin Architecture and API Contract"
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
  - "[[Plugin UX and Accessibility]]"
  - "[[Plugin Data and Integration Design]]"
  - "[[Plugin Implementation Workflow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md"
  - "https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Views.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Defer%20views.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Build%20a%20Bases%20view.md"
  - "https://docs.obsidian.md/Plugins/Editor/Editor+extensions"
---

# Plugin Architecture and API Contract

[practitioner] The brief is clear enough to select surfaces and define ownership before coding.

## When to invoke

Use this playbook at the matching creator stage. It applies the cited official contracts; its sequence is engineering judgment.

## Prerequisites

Read [[Plugin Creator Studio]], the project brief, and the relevant technical concept. Record missing inputs as no data. Preserve unrelated work and immutable raw evidence.

## Step by step

1. Choose the narrowest surface with Plugin Architecture Matrix. A query-driven property view and a workspace dashboard have different state owners.
2. Draw modules for domain logic, vault services, presentation, settings, and integration clients. Keep the domain model reusable across editor and Reading view.
3. Record each public API symbol, its exact declaration source, required app version, and fallback. Do not infer supported APIs from private runtime objects.
4. Assign every event, interval, observer, worker, framework root, and GPU resource to a plugin, view, or render-child lifecycle.
5. Define per-leaf state and serialized workspace state. Plan split panes and deferred restoration rather than storing view instances on the Plugin class.
6. Define startup registration separately from expensive indexing, network requests, and visual initialization. Make repeated activation idempotent where practical.
7. Write read and write boundaries, cancellation behavior, and what happens if a note is renamed or deleted during asynchronous work.
8. Choose dependency and build contracts. Externalize host modules and inspect the final bundle; a package declaration alone does not prove externalization.
9. Capture the selected design, rejected alternatives, tradeoffs, source IDs, and required tests in an architecture decision record.
10. Map every product criterion to an implementation module and an acceptance test before adding optional frameworks.

## Outputs

- ARCHITECTURE_DECISION.md
- API and lifecycle ownership inventory
- Module-to-acceptance trace and build contract

## Quality gates

- All resources have a cleanup owner
- Version and platform assumptions have cited sources
- The proposed surface supports the actual task and recovery path

## Failure modes

- Treating API typings as proof of real behavior
- Sharing view instances across leaves
- Adding a framework or renderer without a product need or resource budget

## Sources

Paraphrase and application; no independent corroboration is implied by repeated upstream works.

- [[Source SRC-01-001]]: [Obsidian plugin guidelines](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md), retrieved 2026-11-01.
- [[Source SRC-01-002]]: [Obsidian public TypeScript API declarations](https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts), retrieved 2026-11-01.
- [[Source SRC-02-001]]: [Obsidian custom ItemView interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Views.md), retrieved 2026-11-01.
- [[Source SRC-02-002]]: [Obsidian deferred view lifecycle](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Defer%20views.md), retrieved 2026-11-01.
- [[Source SRC-02-003]]: [Build a custom Obsidian Bases view](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Build%20a%20Bases%20view.md), retrieved 2026-11-01.
- [[Source SRC-04-002]]: [Obsidian Developer Documentation - Editor extensions](https://docs.obsidian.md/Plugins/Editor/Editor+extensions), retrieved 2026-11-01.

## Related

- [[Plugin Creator Studio]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
- [[Research Pack]]
- [[Plugin Discovery and Brief]]
- [[Plugin UX and Accessibility]]
- [[Plugin Data and Integration Design]]
- [[Plugin Implementation Workflow]]
