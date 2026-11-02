# 007. 3D WebGL, Three.js, React Three Fiber, and spatial codex views

Distilled official documentation, retrieved 2026-11-01; confidence: practitioner for the integration recipe. All source statements are labeled paraphrases.

Core thesis: Give WebGL an explicit lifecycle budget.

## How to use it

1. [practitioner] Own renderer, scene, camera, controls, observers, and render scheduling in the view.
2. [practitioner] Resize against the actual container, cap pixel density where appropriate, and render on demand when possible.
3. [practitioner] Dispose owned resources and stop animation loops when the surface is released.
4. [practitioner] Provide a readable fallback and benchmark actual target devices before promising 3D support.

## Evidence and caveats

- [Obsidian Developer Documentation: Graph CSS Variables](https://docs.obsidian.md/Reference/CSS+variables/Plugins/Graph); retrieved 2026-11-01; source `src-03-obsidian-css-graph-vars`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation: Foundations Color CSS Variables](https://docs.obsidian.md/Reference/CSS+variables/Foundations/Colors); retrieved 2026-11-01; source `src-03-obsidian-css-colors-vars`; verify the linked source note for exact supported claims.
- [MDN Web Docs: Window.devicePixelRatio Property](https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio); retrieved 2026-11-01; source `src-03-mdn-device-pixel-ratio`; verify the linked source note for exact supported claims.
- [Three.js Manual: How to Dispose of Objects](https://threejs.org/manual/pages/how-to-dispose-of-objects.html); retrieved 2026-11-01; source `src-03-threejs-dispose-manual`; verify the linked source note for exact supported claims.
- [Three.js Manual: Freeing Resources and ResourceTracker Pattern](https://threejs.org/manual/pages/cleanup.html); retrieved 2026-11-01; source `src-03-threejs-cleanup-manual`; verify the linked source note for exact supported claims.
- [Three.js API Documentation: WebGLRenderer](https://threejs.org/docs/pages/WebGLRenderer.html); retrieved 2026-11-01; source `src-03-threejs-webglrenderer`; verify the linked source note for exact supported claims.
- [Three.js API Documentation: GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html); retrieved 2026-11-01; source `src-03-threejs-gltfloader`; verify the linked source note for exact supported claims.
- [React Three Fiber Documentation: Canvas API](https://r3f.docs.pmnd.rs/api/canvas); retrieved 2026-11-01; source `src-03-r3f-canvas-api`; verify the linked source note for exact supported claims.
- [React Three Fiber Documentation: Scaling Performance](https://r3f.docs.pmnd.rs/advanced/scaling-performance); retrieved 2026-11-01; source `src-03-r3f-scaling-performance`; verify the linked source note for exact supported claims.
- [React Three Fiber Documentation: Performance Pitfalls](https://r3f.docs.pmnd.rs/advanced/pitfalls); retrieved 2026-11-01; source `src-03-r3f-performance-pitfalls`; verify the linked source note for exact supported claims.
- [MDN Web Docs: ResizeObserver Interface](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver); retrieved 2026-11-01; source `src-03-mdn-resize-observer`; verify the linked source note for exact supported claims.
- [MDN Web Docs: Intersection Observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API); retrieved 2026-11-01; source `src-03-mdn-intersection-observer`; verify the linked source note for exact supported claims.
- [MDN Web Docs: Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API); retrieved 2026-11-01; source `src-03-mdn-page-visibility`; verify the linked source note for exact supported claims.
- [MDN Web Docs: HTMLCanvasElement webglcontextlost Event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/webglcontextlost_event); retrieved 2026-11-01; source `src-03-mdn-webglcontextlost`; verify the linked source note for exact supported claims.
- [MDN Web Docs: HTMLCanvasElement webglcontextrestored Event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/webglcontextrestored_event); retrieved 2026-11-01; source `src-03-mdn-webglcontextrestored`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation: DataAdapter.getResourcePath and Vault.getResourcePath](https://docs.obsidian.md/Reference/TypeScript+API/DataAdapter/getResourcePath); retrieved 2026-11-01; source `src-03-obsidian-dataadapter-resourcepath`; verify the linked source note for exact supported claims.
- [Obsidian API TypeScript Definitions: obsidian.d.ts (DOM, SVG, and Popout Window Helpers)](https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts); retrieved 2026-11-01; source `src-03-obsidian-api-dts`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation: Views (ItemView Lifecycle)](https://docs.obsidian.md/Plugins/User+interface/Views); retrieved 2026-11-01; source `src-03-obsidian-views-guide`; verify the linked source note for exact supported claims.

No fabricated quotations or page numbers. Source relationships do not establish independent corroboration. Runtime behavior remains untested here.

## Brain hooks

Folded into [[3D WebGL, Three.js, React Three Fiber, and spatial codex views]]. Verify with [[Runtime Acceptance Matrix]] and [[Claim Verification Flow]].
