---
type: "source"
title: "Source src-03-r3f-performance-pitfalls"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
source_id: "src-03-r3f-performance-pitfalls"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/source"
  - "confidence/practitioner"
related:
  - "[[3D WebGL, Three.js, React Three Fiber, and spatial codex views]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
source_urls:
  - "https://r3f.docs.pmnd.rs/advanced/pitfalls"
---

# Source src-03-r3f-performance-pitfalls

Original paraphrase of [React Three Fiber Documentation: Performance Pitfalls](https://r3f.docs.pmnd.rs/advanced/pitfalls); reviewed 2026-11-01.

- React Three Fiber recommends mutating object refs for rapid animation updates instead of scheduling React state updates in useFrame, and reusing resources rather than allocating every frame.

Public reference ID: `src-03-r3f-performance-pitfalls`. The public catalog retains dates, confidence, and upstream references. Private research captures are not distributed.

Related: [[Source Manifest Guide]] | [[Claim Verification Flow]] | [[wiki/sources/_index|Sources Hub]]
