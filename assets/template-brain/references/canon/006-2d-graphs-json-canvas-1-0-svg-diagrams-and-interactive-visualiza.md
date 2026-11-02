# 006. 2D graphs, JSON Canvas 1.0, SVG diagrams, and interactive visualizations

Distilled official documentation, retrieved 2026-11-01; confidence: practitioner for the integration recipe. All source statements are labeled paraphrases.

Core thesis: Keep document data separate from visual layout.

## How to use it

1. [practitioner] Represent graph data independently of Canvas, SVG, or a renderer.
2. [practitioner] Choose JSON Canvas for portable node/edge documents; choose a custom view for a live interaction model.
3. [practitioner] Validate imported data before creating nodes, labels, or links.
4. [practitioner] Preserve stable IDs and provide a useful empty graph and malformed-data message.

## Evidence and caveats

- [JSON Canvas Spec 1.0](https://jsoncanvas.org/spec/1.0/); retrieved 2026-11-01; source `src-03-jsoncanvas-spec-1-0`; verify the linked source note for exact supported claims.
- [Obsidian API TypeScript Definitions: canvas.d.ts](https://github.com/obsidianmd/obsidian-api/blob/master/canvas.d.ts); retrieved 2026-11-01; source `src-03-obsidian-api-canvas-dts`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation: Canvas CSS Variables](https://docs.obsidian.md/Reference/CSS+variables/Plugins/Canvas); retrieved 2026-11-01; source `src-03-obsidian-css-canvas-vars`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation: Graph CSS Variables](https://docs.obsidian.md/Reference/CSS+variables/Plugins/Graph); retrieved 2026-11-01; source `src-03-obsidian-css-graph-vars`; verify the linked source note for exact supported claims.
- [Obsidian Developer Documentation: Foundations Color CSS Variables](https://docs.obsidian.md/Reference/CSS+variables/Foundations/Colors); retrieved 2026-11-01; source `src-03-obsidian-css-colors-vars`; verify the linked source note for exact supported claims.
- [D3 by Observable: d3-force Force-Directed Graph Simulation](https://d3js.org/d3-force); retrieved 2026-11-01; source `src-03-d3-force`; verify the linked source note for exact supported claims.
- [D3 by Observable: d3-zoom Pan and Zoom Abstraction](https://d3js.org/d3-zoom); retrieved 2026-11-01; source `src-03-d3-zoom`; verify the linked source note for exact supported claims.
- [Cytoscape.js Graph Theory Network Library Documentation](https://js.cytoscape.org/); retrieved 2026-11-01; source `src-03-cytoscape-js`; verify the linked source note for exact supported claims.
- [MDN Web Docs: SVG viewBox Attribute](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/viewBox); retrieved 2026-11-01; source `src-03-mdn-svg-viewbox`; verify the linked source note for exact supported claims.
- [MDN Web Docs: Window.devicePixelRatio Property](https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio); retrieved 2026-11-01; source `src-03-mdn-device-pixel-ratio`; verify the linked source note for exact supported claims.
- [MDN Web Docs: CanvasRenderingContext2D.scale() and HiDPI Transforms](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/scale); retrieved 2026-11-01; source `src-03-mdn-canvas-scale`; verify the linked source note for exact supported claims.
- [MDN Web Docs: Optimizing HTML5 Canvas Performance](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Optimizing_canvas); retrieved 2026-11-01; source `src-03-mdn-optimizing-canvas`; verify the linked source note for exact supported claims.
- [MDN Web Docs: ResizeObserver Interface](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver); retrieved 2026-11-01; source `src-03-mdn-resize-observer`; verify the linked source note for exact supported claims.
- [MDN Web Docs: Intersection Observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API); retrieved 2026-11-01; source `src-03-mdn-intersection-observer`; verify the linked source note for exact supported claims.
- [Obsidian API TypeScript Definitions: obsidian.d.ts (DOM, SVG, and Popout Window Helpers)](https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts); retrieved 2026-11-01; source `src-03-obsidian-api-dts`; verify the linked source note for exact supported claims.

No fabricated quotations or page numbers. Source relationships do not establish independent corroboration. Runtime behavior remains untested here.

## Brain hooks

Folded into [[2D graphs, JSON Canvas 1.0, SVG diagrams, and interactive visualizations]]. Verify with [[Runtime Acceptance Matrix]] and [[Claim Verification Flow]].
