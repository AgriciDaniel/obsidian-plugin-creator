---
type: "concept"
title: "Best Practices Kernel"
domain: "Architecting, building, styling, optimizing, testing, auditing, and shipping Obsidian plugins across all plugin scopes: core commands, multi-pane dashboards and Bases views, 2D and 3D WebGL visuals and canvases, CodeMirror 6 editor extensions, Markdown processors, vault and MetadataCache engines, mobile compatibility, and Community Store releases."
status: "active"
created: "{{date}}"
updated: "{{date}}"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/concept"
  - "confidence/practitioner"
confidence: "practitioner"
related:
  - "[[Index]]"
  - "[[Dashboard]]"
  - "[[Tag Taxonomy]]"
  - "[[Source Intake Workflow]]"
  - "[[Synthesis Workflow]]"
  - "[[Claim Verification Flow]]"
  - "[[CONVENTIONS]]"
  - "[[Research Refresh Workflow]]"
  - "[[Reporting Workflow]]"
  - "[[Source Manifest Guide]]"
  - "[[Best Practices Kernel]]"
  - "[[Health Scorecard]]"
  - "[[Action Roadmap]]"
  - "[[Weekly Report]]"
  - "[[Approval Queue]]"
  - "[[wiki/flows/_index|Flows Hub]]"
  - "[[wiki/sources/_index|Sources Hub]]"
  - "[[wiki/concepts/_index|Concepts Hub]]"
  - "[[wiki/decisions/_index|Decisions Hub]]"
  - "[[wiki/deliverables/_index|Deliverables Hub]]"
  - "[[wiki/reports/_index|Reports Hub]]"
  - "[[wiki/questions/_index|Questions Hub]]"
  - "[[wiki/gaps/_index|Gaps Hub]]"
  - "[[wiki/experiments/_index|Experiments Hub]]"
source_urls: []
---

# Best Practices Kernel

[practitioner] Begin with the user task, select the narrowest surface, and give every resource one lifecycle owner. Read [[Plugin Architecture Matrix]] before adding frameworks or multiple UI scopes.

## Working rules

1. Cite the actual source note and official URL for domain facts.
2. Treat a static scan as a bounded heuristic. Run the actual build and official lint.
3. Keep per-leaf state in the view and shared domain state outside visual rendering.
4. Treat metadata gaps, malformed input, offline requests, and missing secrets as normal states.
5. Separate compact settings from derived caches and measure large-vault work.
6. Plan keyboard access, empty/error states, theme behavior, and cleanup with the first vertical slice.
7. Retain runtime/device evidence in [[Runtime Acceptance Matrix]] before making platform or performance claims.
8. Refresh official submission policies before a release.

## Sources and guidance

- [[Research Pack]]
- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[CodeMirror 6 architecture, StateFields, ViewPlugins, and Live Preview]]
- [[Security, XSS prevention, Sync storage limits, and network disclosure]]
- [[Community Store submission, eslint-plugin review gates, BRAT, and release CI]]
- [[Claim Verification Flow]]
- [[Action Roadmap]]
