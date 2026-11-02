---
type: "flow"
title: "Runtime Acceptance Matrix"
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
  - "[[Research Pack]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Index]]"
  - "[[Dashboard]]"
source_urls: []
---

# Runtime Acceptance Matrix

[practitioner] Use this matrix for each real plugin. Every runtime row starts **unverified**. Record failures and unknowns explicitly; an empty result is no data.

| Evidence class | Check | Current brain evidence | Real plugin requirement |
|---|---|---|---|
| Static fixture | Import and inspect synthetic repository | Local automated tests | Repeat on the actual repository |
| Build/lint | TypeScript, bundler, official ESLint | Unverified for real plugins | Retain commands, outputs, dependency versions |
| Desktop runtime | Enable/disable/reload/workspace restore | Unverified | App version, OS, artifact hash, observed behavior |
| View lifecycle | Multiple leaves, deferred restore, close, hide/show | Unverified | No stale DOM or uncontrolled background work |
| Editor parity | Source, Live Preview, Reading, embeds | Unverified | Same semantics, valid selection and undo |
| Vault behavior | Rename/delete/external edit/large vault | Unverified | Correct event handling and recovery |
| WebGL | Resize/context loss/disposal/accessibility | Unverified | Measured frame, heap and GPU observations |
| Physical iOS | Real device, keyboard/touch, app restart | Unverified | Device and app version plus retained outcome |
| Physical Android | Real device, keyboard/touch, app restart | Unverified | Device and app version plus retained outcome |
| Security | Malicious labels/HTML/paths, secrets, network | Unverified for real plugins | Manual review and observed request/storage behavior |
| Submission | Current directory rules and exact release assets | Research guidance only | Owner approval and actual review outcome |

## Result record

- Owner and test date
- Plugin release/artifact SHA256 and dependency lock hash
- Obsidian version, operating system, device, and enabled core plugins
- Vault fixture, file count, data size, and exact reproduction steps
- Expected result, observed result, pass/fail/unknown
- Raw log, screenshot, profile, or recording path
- Remaining gap, next action, recovery procedure

## Static scanner limits

The scanner searches bounded source text. It does not parse the TypeScript AST, execute the plugin, invoke ESLint, inspect a compiled bundle, verify taint flow, or prove cleanup. Comments, wrappers, aliases, computed imports and dynamic configuration can change its accuracy. A clear static result means only that the implemented signals found no blocking pattern. Missing evidence remains unknown.

Related: [[Research Pack]] | [[Plugin Architecture Matrix]] | [[Claim Verification Flow]]
