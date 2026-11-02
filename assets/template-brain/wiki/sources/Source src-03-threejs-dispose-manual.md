---
type: "source"
title: "Source src-03-threejs-dispose-manual"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "src-03-threejs-dispose-manual"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[3D WebGL, Three.js, React Three Fiber, and spatial codex views]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://threejs.org/manual/pages/how-to-dispose-of-objects.html"
---

# Source src-03-threejs-dispose-manual

Original paraphrase of [Three.js Manual: How to Dispose of Objects](https://threejs.org/manual/pages/how-to-dispose-of-objects.html); reviewed 2026-11-01.

- Removing a Three.js object from a scene does not dispose its geometry, materials, or textures. Applications must release GPU resources explicitly.
- Disposing a material does not dispose its textures. ImageBitmap sources require their own close() handling when no longer shared.
- Controls and render targets may also require disposal; renderer.info can help inspect remaining GPU allocations.

Public reference ID: `src-03-threejs-dispose-manual`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
