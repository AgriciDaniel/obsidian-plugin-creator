---
type: "experiment"
title: "Static analyzer verification probe against both clean and anti-pattern Obsidian"
domain: "Obsidian plugin engineering"
status: "local-fixture-passed"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/experiment"
  - "confidence/practitioner"
related:
  - "[[Plugin Verification and Performance]]"
  - "[[Health Scorecard]]"
  - "[[Plugin Creator Studio]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
  - "[[Source SRC-01-001]]"
  - "[[Source SRC-01-008]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Getting%20started/Mobile%20development.md"
---

# Static analyzer verification probe against both clean and anti-pattern Obsidian

[practitioner] The synthetic healthy, flawed, malformed, missing-data, symlink, oversized, host-external, mobile builtin, and compatibility cases run in tests/test_obsidian_plugin_adapter.py. These are static fixture outcomes, not official lint or Obsidian execution. The creator adds independent real build/lint evidence for its retained source templates.

## Evidence and next action

Keep the evidence class, exact artifact, app/device, source date, expected/observed result, and remaining gap visible. Use the matching creator playbook for the next project-specific task.

## Sources

- [[Source SRC-01-001]]: [Obsidian plugin guidelines](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md), retrieved 2026-11-01.
- [[Source SRC-01-008]]: [Obsidian mobile development](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Getting%20started/Mobile%20development.md), retrieved 2026-11-01.

## Related

- [[Plugin Verification and Performance]]
- [[Health Scorecard]]
- [[Plugin Creator Studio]]
- [[Research Pack]]
- [[Claim Verification Flow]]
- [[Source SRC-01-001]]
- [[Source SRC-01-008]]
