---
type: "gap"
title: "WebGPU availability vs WebGL2 fallback behavior across Electron Chromium version"
domain: "Obsidian plugin engineering"
status: "open"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/gap"
  - "confidence/practitioner"
related:
  - "[[Plugin Advanced Surfaces]]"
  - "[[Runtime Acceptance Matrix]]"
  - "[[Plugin Creator Studio]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
  - "[[Source src-03-threejs-webglrenderer]]"
  - "[[Source src-03-threejs-dispose-manual]]"
source_urls:
  - "https://threejs.org/docs/pages/WebGLRenderer.html"
  - "https://threejs.org/manual/pages/how-to-dispose-of-objects.html"
---

# WebGPU availability vs WebGL2 fallback behavior across Electron Chromium version

[practitioner] The retained WebGL starter builds successfully, but no WebGPU or WebGL device-support matrix has been executed in Obsidian. Record actual renderer capabilities, context loss/recovery, fallback, lifecycle disposal, app version, and physical-device outcomes for the promised feature.

## Evidence and next action

Keep the evidence class, exact artifact, app/device, source date, expected/observed result, and remaining gap visible. Use the matching creator playbook for the next project-specific task.

## Sources

- [[Source src-03-threejs-webglrenderer]]: [Three.js API Documentation: WebGLRenderer](https://threejs.org/docs/pages/WebGLRenderer.html), retrieved 2026-11-01.
- [[Source src-03-threejs-dispose-manual]]: [Three.js Manual: How to Dispose of Objects](https://threejs.org/manual/pages/how-to-dispose-of-objects.html), retrieved 2026-11-01.

## Related

- [[Plugin Advanced Surfaces]]
- [[Runtime Acceptance Matrix]]
- [[Plugin Creator Studio]]
- [[Research Pack]]
- [[Claim Verification Flow]]
- [[Source src-03-threejs-webglrenderer]]
- [[Source src-03-threejs-dispose-manual]]
