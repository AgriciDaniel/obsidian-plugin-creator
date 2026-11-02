---
type: "concept"
title: "3D WebGL, Three.js, React Three Fiber, and spatial codex views"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/concept"
  - "confidence/practitioner"
related:
  - "[[Plugin lifecycle, Component ownership, and cleanup discipline]]"
  - "[[Workspace leaves, custom ItemView dashboards, and deferred views]]"
  - "[[Obsidian Bases API, native dashboards, and query surfaces]]"
  - "[[Source src-03-obsidian-css-graph-vars]]"
  - "[[Source src-03-obsidian-css-colors-vars]]"
  - "[[Source src-03-mdn-device-pixel-ratio]]"
  - "[[Source src-03-threejs-dispose-manual]]"
  - "[[Source src-03-threejs-cleanup-manual]]"
  - "[[Source src-03-threejs-webglrenderer]]"
  - "[[Source src-03-threejs-gltfloader]]"
  - "[[Source src-03-r3f-canvas-api]]"
  - "[[Source src-03-r3f-scaling-performance]]"
  - "[[Source src-03-r3f-performance-pitfalls]]"
  - "[[Source src-03-mdn-resize-observer]]"
  - "[[Source src-03-mdn-intersection-observer]]"
  - "[[Source src-03-mdn-page-visibility]]"
  - "[[Source src-03-mdn-webglcontextlost]]"
  - "[[Source src-03-mdn-webglcontextrestored]]"
  - "[[Source src-03-obsidian-dataadapter-resourcepath]]"
  - "[[Source src-03-obsidian-api-dts]]"
  - "[[Source src-03-obsidian-views-guide]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
source_urls:
  - "https://docs.obsidian.md/Reference/CSS+variables/Plugins/Graph"
  - "https://docs.obsidian.md/Reference/CSS+variables/Foundations/Colors"
  - "https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio"
  - "https://threejs.org/manual/pages/how-to-dispose-of-objects.html"
  - "https://threejs.org/manual/pages/cleanup.html"
  - "https://threejs.org/docs/pages/WebGLRenderer.html"
  - "https://threejs.org/docs/pages/GLTFLoader.html"
  - "https://r3f.docs.pmnd.rs/api/canvas"
  - "https://r3f.docs.pmnd.rs/advanced/scaling-performance"
  - "https://r3f.docs.pmnd.rs/advanced/pitfalls"
  - "https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver"
  - "https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API"
  - "https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API"
  - "https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/webglcontextlost_event"
  - "https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/webglcontextrestored_event"
  - "https://docs.obsidian.md/Reference/TypeScript+API/DataAdapter/getResourcePath"
  - "https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts"
  - "https://docs.obsidian.md/Plugins/User+interface/Views"
---

# 3D WebGL, Three.js, React Three Fiber, and spatial codex views

Give WebGL an explicit lifecycle budget.

## Verified source guidance

Paraphrases from the dated sources below. Repeated upstream origins are consistency checks, not independent corroboration.

### Obsidian Developer Documentation: Graph CSS Variables

- [evidence-based] The Graph CSS reference provides semantic variables for graph text, lines, and node categories. ([[Source src-03-obsidian-css-graph-vars]])

### Obsidian Developer Documentation: Foundations Color CSS Variables

- [evidence-based] Obsidian documents semantic background, border, interactive, and text colors for themed interfaces. ([[Source src-03-obsidian-css-colors-vars]])
- [evidence-based] The current color reference marks legacy RGB and HSL variables deprecated as of Obsidian 1.13 and recommends color-mix with the corresponding color variables. ([[Source src-03-obsidian-css-colors-vars]])

### MDN Web Docs: Window.devicePixelRatio Property

- [evidence-based] devicePixelRatio gives the ratio of physical pixels to CSS pixels; MDN demonstrates increasing a Canvas backing resolution for sharper output on high density displays. ([[Source src-03-mdn-device-pixel-ratio]])

### Three.js Manual: How to Dispose of Objects

- [evidence-based] Removing a Three.js object from a scene does not dispose its geometry, materials, or textures. Applications must release GPU resources explicitly. ([[Source src-03-threejs-dispose-manual]])
- [evidence-based] Disposing a material does not dispose its textures. ImageBitmap sources require their own close() handling when no longer shared. ([[Source src-03-threejs-dispose-manual]])
- [evidence-based] Controls and render targets may also require disposal; renderer.info can help inspect remaining GPU allocations. ([[Source src-03-threejs-dispose-manual]])

### Three.js Manual: Freeing Resources and ResourceTracker Pattern

- [evidence-based] The Three.js cleanup guide demonstrates tracking disposable resources explicitly, including objects removed from the scene. ([[Source src-03-threejs-cleanup-manual]])

### Three.js API Documentation: WebGLRenderer

- [evidence-based] WebGLRenderer exposes setPixelRatio, setSize, dispose, and forceContextLoss. The current renderer uses WebGL 2. ([[Source src-03-threejs-webglrenderer]])

### Three.js API Documentation: GLTFLoader

- [evidence-based] GLTFLoader loads glTF assets and supports separately configured decoders. Its documentation warns that image bitmaps require special disposal handling. ([[Source src-03-threejs-gltfloader]])

### React Three Fiber Documentation: Canvas API

- [evidence-based] React Three Fiber Canvas exposes frameloop, pixel ratio, renderer options, and fallback content; it sizes its rendering surface to its parent. ([[Source src-03-r3f-canvas-api]])

### React Three Fiber Documentation: Scaling Performance

- [evidence-based] React Three Fiber supports demand rendering through frameloop="demand" and invalidate(); its performance guide discusses resource reuse and adaptive pixel ratios. ([[Source src-03-r3f-scaling-performance]])

### React Three Fiber Documentation: Performance Pitfalls

- [evidence-based] React Three Fiber recommends mutating object refs for rapid animation updates instead of scheduling React state updates in useFrame, and reusing resources rather than allocating every frame. ([[Source src-03-r3f-performance-pitfalls]])

### MDN Web Docs: ResizeObserver Interface

- [evidence-based] ResizeObserver reports changes in an observed element size and supports disconnect() to stop observation. ([[Source src-03-mdn-resize-observer]])

### MDN Web Docs: Intersection Observer API

- [practitioner] IntersectionObserver reports changes in geometric intersection with a viewport or ancestor. Geometric intersection alone does not prove that a workspace tab is actually visible. ([[Source src-03-mdn-intersection-observer]])

### MDN Web Docs: Page Visibility API

- [practitioner] The Page Visibility API exposes document visibility state and a visibilitychange event. It does not measure visibility of individual Obsidian panes. ([[Source src-03-mdn-page-visibility]])

### MDN Web Docs: HTMLCanvasElement webglcontextlost Event

- [evidence-based] webglcontextlost is dispatched on a canvas when its drawing context is lost; the event can be canceled to permit restoration. ([[Source src-03-mdn-webglcontextlost]])

### MDN Web Docs: HTMLCanvasElement webglcontextrestored Event

- [evidence-based] After WebGL context restoration, resources created before the loss are invalid and must be created again. ([[Source src-03-mdn-webglcontextrestored]])

### Obsidian Developer Documentation: DataAdapter.getResourcePath and Vault.getResourcePath

- [practitioner] DataAdapter.getResourcePath(normalizedPath) returns a URL for loading a resource into DOM elements. This API reference alone does not establish release distribution support for extra asset files. ([[Source src-03-obsidian-dataadapter-resourcepath]])

### Obsidian API TypeScript Definitions: obsidian.d.ts (DOM, SVG, and Popout Window Helpers)

- [practitioner] The public typings include createFragment, DOM creation options, and document/window helpers for DOM nodes. Use the owning document and window when handling popout views. ([[Source src-03-obsidian-api-dts]])

### Obsidian Developer Documentation: Views (ItemView Lifecycle)

- [evidence-based] The Views guide registers an ItemView factory, builds content in onOpen, and assigns resource cleanup to onClose; it warns against retaining view references in the plugin. ([[Source src-03-obsidian-views-guide]])

## Engineering recipe

[practitioner] This sequence applies the cited contracts; it is not a tested plugin implementation.

1. Own renderer, scene, camera, controls, observers, and render scheduling in the view.
2. Resize against the actual container, cap pixel density where appropriate, and render on demand when possible.
3. Dispose owned resources and stop animation loops when the surface is released.
4. Provide a readable fallback and benchmark actual target devices before promising 3D support.

## Verification

[practitioner] Observe GPU and heap behavior across repeated open/close, hide/show, and context-loss recovery.

Record app version, operating system, plugin artifact hash, input size, observed outcome, and evidence path in [[Runtime Acceptance Matrix]].

## Limits

This brain has no physical-device result for this recipe. A static scan cannot prove lifecycle correctness, mobile support, rendering performance, or submission acceptance. Refresh policy and API claims before release.

## Sources

- [Obsidian Developer Documentation: Graph CSS Variables](https://docs.obsidian.md/Reference/CSS+variables/Plugins/Graph), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation: Foundations Color CSS Variables](https://docs.obsidian.md/Reference/CSS+variables/Foundations/Colors), retrieved 2026-11-01, refresh due 2026-12-01.
- [MDN Web Docs: Window.devicePixelRatio Property](https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio), retrieved 2026-11-01, refresh due 2026-12-01.
- [Three.js Manual: How to Dispose of Objects](https://threejs.org/manual/pages/how-to-dispose-of-objects.html), retrieved 2026-11-01, refresh due 2026-12-01.
- [Three.js Manual: Freeing Resources and ResourceTracker Pattern](https://threejs.org/manual/pages/cleanup.html), retrieved 2026-11-01, refresh due 2026-12-01.
- [Three.js API Documentation: WebGLRenderer](https://threejs.org/docs/pages/WebGLRenderer.html), retrieved 2026-11-01, refresh due 2026-12-01.
- [Three.js API Documentation: GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html), retrieved 2026-11-01, refresh due 2026-12-01.
- [React Three Fiber Documentation: Canvas API](https://r3f.docs.pmnd.rs/api/canvas), retrieved 2026-11-01, refresh due 2026-12-01.
- [React Three Fiber Documentation: Scaling Performance](https://r3f.docs.pmnd.rs/advanced/scaling-performance), retrieved 2026-11-01, refresh due 2026-12-01.
- [React Three Fiber Documentation: Performance Pitfalls](https://r3f.docs.pmnd.rs/advanced/pitfalls), retrieved 2026-11-01, refresh due 2026-12-01.
- [MDN Web Docs: ResizeObserver Interface](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver), retrieved 2026-11-01, refresh due 2026-12-01.
- [MDN Web Docs: Intersection Observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API), retrieved 2026-11-01, refresh due 2026-12-01.
- [MDN Web Docs: Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API), retrieved 2026-11-01, refresh due 2026-12-01.
- [MDN Web Docs: HTMLCanvasElement webglcontextlost Event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/webglcontextlost_event), retrieved 2026-11-01, refresh due 2026-12-01.
- [MDN Web Docs: HTMLCanvasElement webglcontextrestored Event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/webglcontextrestored_event), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation: DataAdapter.getResourcePath and Vault.getResourcePath](https://docs.obsidian.md/Reference/TypeScript+API/DataAdapter/getResourcePath), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian API TypeScript Definitions: obsidian.d.ts (DOM, SVG, and Popout Window Helpers)](https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation: Views (ItemView Lifecycle)](https://docs.obsidian.md/Plugins/User+interface/Views), retrieved 2026-11-01, refresh due 2026-12-01.

## Related

- [[Source src-03-obsidian-css-graph-vars]]
- [[Source src-03-obsidian-css-colors-vars]]
- [[Source src-03-mdn-device-pixel-ratio]]
- [[Source src-03-threejs-dispose-manual]]
- [[Source src-03-threejs-cleanup-manual]]
- [[Source src-03-threejs-webglrenderer]]
- [[Source src-03-threejs-gltfloader]]
- [[Source src-03-r3f-canvas-api]]
- [[Source src-03-r3f-scaling-performance]]
- [[Source src-03-r3f-performance-pitfalls]]
- [[Source src-03-mdn-resize-observer]]
- [[Source src-03-mdn-intersection-observer]]
- [[Source src-03-mdn-page-visibility]]
- [[Source src-03-mdn-webglcontextlost]]
- [[Source src-03-mdn-webglcontextrestored]]
- [[Source src-03-obsidian-dataadapter-resourcepath]]
- [[Source src-03-obsidian-api-dts]]
- [[Source src-03-obsidian-views-guide]]
- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[Obsidian Bases API, native dashboards, and query surfaces]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
