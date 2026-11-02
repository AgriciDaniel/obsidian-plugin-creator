---
type: "flow"
title: "Plugin Advanced Surfaces"
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
  - "https://jsoncanvas.org/spec/1.0/"
  - "https://threejs.org/docs/pages/WebGLRenderer.html"
  - "https://threejs.org/manual/pages/how-to-dispose-of-objects.html"
  - "https://codemirror.net/docs/ref/"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Developer%20policies.md"
---

# Plugin Advanced Surfaces

[practitioner] A clear product need requires frameworks, Canvas documents, WebGL, workers, large indexes, or external APIs.

## When to invoke

Use this playbook at the matching creator stage. It applies the cited official contracts; its sequence is engineering judgment.

## Prerequisites

Read [[Plugin Creator Studio]], the project brief, and the relevant technical concept. Record missing inputs as no data. Preserve unrelated work and immutable raw evidence.

## Step by step

1. Prove the user benefit and select the smallest vertical slice before adding a framework, renderer, worker, or backend.
2. For React/Svelte/Vue, keep the mount root view-owned, define cleanup, and preserve Obsidian-native settings and semantic controls where useful.
3. For 2D graphs, separate data, layout, hit testing, selection, and rendering. Preserve stable IDs and validate imported geometry and labels.
4. Treat JSON Canvas as a document format rather than assuming access to Obsidian's internal live Canvas implementation.
5. For WebGL, own renderer, scene, controls, resources, observers, and scheduling. Plan unsupported contexts, context loss, readable alternatives, and actual GPU observations.
6. For editor widgets, use supported extension APIs and transaction/state boundaries. Avoid direct mutation of the editor DOM.
7. For workers and large caches, test packaging, origin/storage behavior, cancellation, cleanup, and rebuildability on actual targets. Do not infer cross-platform behavior from browser documentation alone.
8. For external services and AI APIs, research current official provider contracts separately, specify transmitted content, cap approved cost, and preserve actual usage/billing uncertainty.
9. Never add runtime-downloaded code or self-updating dependencies based on generic web-app conventions. Check current Obsidian policies first.
10. Measure the resulting bundle, interaction latency, startup, heap, and device behavior with the exact feature set enabled.

## Outputs

- An advanced-surface architecture decision
- Resource, packaging, and fallback inventory
- Measured acceptance and remaining platform gaps

## Quality gates

- The advanced surface solves a stated product task
- Every new resource and external service has an owner and boundary
- Fallback and cleanup behavior have actual target evidence before release

## Failure modes

- Assuming a normal browser deployment works unchanged inside Obsidian
- Promising smooth rendering from a bundle-size check
- Using private APIs as a compatibility contract

## Sources

Paraphrase and application; no independent corroboration is implied by repeated upstream works.

- [[Source src-03-jsoncanvas-spec-1-0]]: [JSON Canvas Spec 1.0](https://jsoncanvas.org/spec/1.0/), retrieved 2026-11-01.
- [[Source src-03-threejs-webglrenderer]]: [Three.js API Documentation: WebGLRenderer](https://threejs.org/docs/pages/WebGLRenderer.html), retrieved 2026-11-01.
- [[Source src-03-threejs-dispose-manual]]: [Three.js Manual: How to Dispose of Objects](https://threejs.org/manual/pages/how-to-dispose-of-objects.html), retrieved 2026-11-01.
- [[Source SRC-04-011]]: [CodeMirror 6 Documentation - Reference Manual](https://codemirror.net/docs/ref/), retrieved 2026-11-01.
- [[Source SRC-01-005]]: [Obsidian Community directory developer policies](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Developer%20policies.md), retrieved 2026-11-01.

## Related

- [[Plugin Creator Studio]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
- [[Research Pack]]
- [[Plugin Discovery and Brief]]
- [[Plugin Architecture and API Contract]]
- [[Plugin UX and Accessibility]]
- [[Plugin Data and Integration Design]]
