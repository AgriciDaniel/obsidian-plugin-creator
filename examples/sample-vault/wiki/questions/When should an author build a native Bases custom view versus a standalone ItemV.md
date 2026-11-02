---
type: "question"
title: "When should an author build a native Bases custom view versus a standalone ItemV"
domain: "Obsidian plugin engineering"
status: "answered-for-guidance"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/question"
  - "confidence/practitioner"
related:
  - "[[Plugin Architecture Matrix]]"
  - "[[Plugin Architecture and API Contract]]"
  - "[[Plugin Creator Studio]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
  - "[[Source SRC-02-001]]"
  - "[[Source SRC-02-003]]"
  - "[[Source SRC-04-016]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Views.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Build%20a%20Bases%20view.md"
  - "https://docs.obsidian.md/Plugins/Editor/Markdown+post+processing"
---

# When should an author build a native Bases custom view versus a standalone ItemV

[practitioner] Choose a Bases custom view when the product consumes a Bases query and property model; choose ItemView for an independent workspace; choose a Markdown processor for content embedded in a note. Record the tradeoff and actual product acceptance before combining surfaces.

## Evidence and next action

Keep the evidence class, exact artifact, app/device, source date, expected/observed result, and remaining gap visible. Use the matching creator playbook for the next project-specific task.

## Sources

- [[Source SRC-02-001]]: [Obsidian custom ItemView interfaces](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/User%20interface/Views.md), retrieved 2026-11-01.
- [[Source SRC-02-003]]: [Build a custom Obsidian Bases view](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Build%20a%20Bases%20view.md), retrieved 2026-11-01.
- [[Source SRC-04-016]]: [Obsidian Developer Documentation - Markdown post processing](https://docs.obsidian.md/Plugins/Editor/Markdown+post+processing), retrieved 2026-11-01.

## Related

- [[Plugin Architecture Matrix]]
- [[Plugin Architecture and API Contract]]
- [[Plugin Creator Studio]]
- [[Research Pack]]
- [[Claim Verification Flow]]
- [[Source SRC-02-001]]
- [[Source SRC-02-003]]
- [[Source SRC-04-016]]
