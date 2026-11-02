---
type: "flow"
title: "Plugin Discovery and Brief"
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
  - "[[Plugin Architecture and API Contract]]"
  - "[[Plugin UX and Accessibility]]"
  - "[[Plugin Data and Integration Design]]"
  - "[[Plugin Implementation Workflow]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/Manifest.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Developer%20policies.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Views.md"
---

# Plugin Discovery and Brief

[practitioner] A plugin idea, an existing plugin improvement, or an unclear feature request needs an implementable contract.

## When to invoke

Use this playbook at the matching creator stage. It applies the cited official contracts; its sequence is engineering judgment.

## Prerequisites

Read [[Plugin Creator Studio]], the project brief, and the relevant technical concept. Record missing inputs as no data. Preserve unrelated work and immutable raw evidence.

## Step by step

1. Describe one primary user, the recurring task, its trigger, and the observable successful outcome.
2. Record the current workaround. If comparison or demand matters, collect actual evidence rather than inventing competitors, testimonials, or time savings.
3. List representative input data, vault size, note types, metadata gaps, and offline requirements. Use sanitized fixtures, not a private production vault.
4. Choose desktop-only or intended desktop/mobile targets. Record the minimum app version as a decision to verify against every used API.
5. Classify the surface: command, custom view, Bases query, editor extension, Markdown widget, 2D/3D visual, or vault service. Start with one vertical slice.
6. Specify the feature list and explicit exclusions. Separate the starter's example behavior from the requested product behavior.
7. Write user-visible acceptance criteria including loading, empty, invalid input, failure, cancellation, and recovery outcomes.
8. Declare all external services, credentials, stored data, note writes, licenses, and account/payment needs. Unknowns remain no data.
9. Ask only the next question whose answer changes architecture or acceptance. Fill routine reversible choices with a stated recommendation.
10. Complete the JSON creator brief for source generation and the full product brief for implementation.

## Outputs

- creator-brief.json with a selected archetype
- PRODUCT_BRIEF.md with measurable criteria
- A bounded first slice and a list of decisions still needed

## Quality gates

- The primary task is testable without guessing the business goal
- Platform intent is separate from tested compatibility
- Permissions and data writes are declared before implementation

## Failure modes

- Treating an attractive dashboard as the product definition
- Assuming a generic starter satisfies the requested acceptance criteria
- Claiming demand or measured savings without a sample and denominator

## Sources

Paraphrase and application; no independent corroboration is implied by repeated upstream works.

- [[Source SRC-01-003]]: [Obsidian manifest specification](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/Manifest.md), retrieved 2026-11-01.
- [[Source SRC-01-005]]: [Obsidian Community directory developer policies](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Developer%20policies.md), retrieved 2026-11-01.
- [[Source SRC-02-001]]: [Obsidian custom ItemView interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Views.md), retrieved 2026-11-01.

## Related

- [[Plugin Creator Studio]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
- [[Research Pack]]
- [[Plugin Architecture and API Contract]]
- [[Plugin UX and Accessibility]]
- [[Plugin Data and Integration Design]]
- [[Plugin Implementation Workflow]]
