---
type: "concept"
title: "2D graphs, JSON Canvas 1.0, SVG diagrams, and interactive visualizations"
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
  - "[[Source src-03-jsoncanvas-spec-1-0]]"
  - "[[Source src-03-obsidian-api-canvas-dts]]"
  - "[[Source src-03-obsidian-css-canvas-vars]]"
  - "[[Source src-03-obsidian-css-graph-vars]]"
  - "[[Source src-03-obsidian-css-colors-vars]]"
  - "[[Source src-03-d3-force]]"
  - "[[Source src-03-d3-zoom]]"
  - "[[Source src-03-cytoscape-js]]"
  - "[[Source src-03-mdn-svg-viewbox]]"
  - "[[Source src-03-mdn-device-pixel-ratio]]"
  - "[[Source src-03-mdn-canvas-scale]]"
  - "[[Source src-03-mdn-optimizing-canvas]]"
  - "[[Source src-03-mdn-resize-observer]]"
  - "[[Source src-03-mdn-intersection-observer]]"
  - "[[Source src-03-obsidian-api-dts]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
source_urls:
  - "https://jsoncanvas.org/spec/1.0/"
  - "https://github.com/obsidianmd/obsidian-api/blob/master/canvas.d.ts"
  - "https://docs.obsidian.md/Reference/CSS+variables/Plugins/Canvas"
  - "https://docs.obsidian.md/Reference/CSS+variables/Plugins/Graph"
  - "https://docs.obsidian.md/Reference/CSS+variables/Foundations/Colors"
  - "https://d3js.org/d3-force"
  - "https://d3js.org/d3-zoom"
  - "https://js.cytoscape.org/"
  - "https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/viewBox"
  - "https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio"
  - "https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/scale"
  - "https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Optimizing_canvas"
  - "https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver"
  - "https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API"
  - "https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts"
---

# 2D graphs, JSON Canvas 1.0, SVG diagrams, and interactive visualizations

Keep document data separate from visual layout.

## Verified source guidance

Paraphrases from the dated sources below. Repeated upstream origins are consistency checks, not independent corroboration.

### JSON Canvas Spec 1.0

- [evidence-based] JSON Canvas 1.0 represents an infinite canvas as optional nodes and edges arrays; nodes carry IDs, types, geometry, and optional colors. ([[Source src-03-jsoncanvas-spec-1-0]])
- [evidence-based] The specification distinguishes text, file, link, and group nodes; edges connect node IDs and may specify sides, ends, colors, and labels. ([[Source src-03-jsoncanvas-spec-1-0]])

### Obsidian API TypeScript Definitions: canvas.d.ts

- [evidence-based] The official canvas.d.ts defines serialized CanvasData, node variants, and CanvasEdgeData. These types describe persisted JSON rather than a public interactive Canvas controller. ([[Source src-03-obsidian-api-canvas-dts]])

### Obsidian Developer Documentation: Canvas CSS Variables

- [evidence-based] The Canvas CSS reference exposes canvas background, card label, dot pattern, and six preset color variables. ([[Source src-03-obsidian-css-canvas-vars]])

### Obsidian Developer Documentation: Graph CSS Variables

- [evidence-based] The Graph CSS reference provides semantic variables for graph text, lines, and node categories. ([[Source src-03-obsidian-css-graph-vars]])

### Obsidian Developer Documentation: Foundations Color CSS Variables

- [evidence-based] Obsidian documents semantic background, border, interactive, and text colors for themed interfaces. ([[Source src-03-obsidian-css-colors-vars]])
- [evidence-based] The current color reference marks legacy RGB and HSL variables deprecated as of Obsidian 1.13 and recommends color-mix with the corresponding color variables. ([[Source src-03-obsidian-css-colors-vars]])

### D3 by Observable: d3-force Force-Directed Graph Simulation

- [evidence-based] d3-force exposes a simulation that updates node positions through forces. simulation.stop() stops its internal timer. ([[Source src-03-d3-force]])

### D3 by Observable: d3-zoom Pan and Zoom Abstraction

- [evidence-based] d3-zoom provides pan and zoom behavior for HTML, SVG, or Canvas, with scale and translation bounds and an event filter. ([[Source src-03-d3-zoom]])

### Cytoscape.js Graph Theory Network Library Documentation

- [evidence-based] Cytoscape.js supports graph visualization, analysis, layouts, and styling. cy.resize() updates container sizing and cy.destroy() releases the instance. ([[Source src-03-cytoscape-js]])

### MDN Web Docs: SVG viewBox Attribute

- [evidence-based] SVG viewBox defines a user coordinate rectangle whose mapping to the viewport controls how the graphic scales. ([[Source src-03-mdn-svg-viewbox]])

### MDN Web Docs: Window.devicePixelRatio Property

- [evidence-based] devicePixelRatio gives the ratio of physical pixels to CSS pixels; MDN demonstrates increasing a Canvas backing resolution for sharper output on high density displays. ([[Source src-03-mdn-device-pixel-ratio]])

### MDN Web Docs: CanvasRenderingContext2D.scale() and HiDPI Transforms

- [evidence-based] CanvasRenderingContext2D.scale changes the current transformation matrix; repeated scaling is cumulative. ([[Source src-03-mdn-canvas-scale]])

### MDN Web Docs: Optimizing HTML5 Canvas Performance

- [evidence-based] MDN recommends techniques including prerendering repeated content, layered canvases, and batching drawing operations where appropriate. ([[Source src-03-mdn-optimizing-canvas]])

### MDN Web Docs: ResizeObserver Interface

- [evidence-based] ResizeObserver reports changes in an observed element size and supports disconnect() to stop observation. ([[Source src-03-mdn-resize-observer]])

### MDN Web Docs: Intersection Observer API

- [practitioner] IntersectionObserver reports changes in geometric intersection with a viewport or ancestor. Geometric intersection alone does not prove that a workspace tab is actually visible. ([[Source src-03-mdn-intersection-observer]])

### Obsidian API TypeScript Definitions: obsidian.d.ts (DOM, SVG, and Popout Window Helpers)

- [practitioner] The public typings include createFragment, DOM creation options, and document/window helpers for DOM nodes. Use the owning document and window when handling popout views. ([[Source src-03-obsidian-api-dts]])

## Engineering recipe

[practitioner] This sequence applies the cited contracts; it is not a tested plugin implementation.

1. Represent graph data independently of Canvas, SVG, or a renderer.
2. Choose JSON Canvas for portable node/edge documents; choose a custom view for a live interaction model.
3. Validate imported data before creating nodes, labels, or links.
4. Preserve stable IDs and provide a useful empty graph and malformed-data message.

## Verification

[practitioner] Round-trip a small document and check missing nodes, invalid types, and large coordinates.

Record app version, operating system, plugin artifact hash, input size, observed outcome, and evidence path in [[Runtime Acceptance Matrix]].

## Limits

This brain has no physical-device result for this recipe. A static scan cannot prove lifecycle correctness, mobile support, rendering performance, or submission acceptance. Refresh policy and API claims before release.

## Sources

- [JSON Canvas Spec 1.0](https://jsoncanvas.org/spec/1.0/), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian API TypeScript Definitions: canvas.d.ts](https://github.com/obsidianmd/obsidian-api/blob/master/canvas.d.ts), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation: Canvas CSS Variables](https://docs.obsidian.md/Reference/CSS+variables/Plugins/Canvas), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation: Graph CSS Variables](https://docs.obsidian.md/Reference/CSS+variables/Plugins/Graph), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian Developer Documentation: Foundations Color CSS Variables](https://docs.obsidian.md/Reference/CSS+variables/Foundations/Colors), retrieved 2026-11-01, refresh due 2026-12-01.
- [D3 by Observable: d3-force Force-Directed Graph Simulation](https://d3js.org/d3-force), retrieved 2026-11-01, refresh due 2026-12-01.
- [D3 by Observable: d3-zoom Pan and Zoom Abstraction](https://d3js.org/d3-zoom), retrieved 2026-11-01, refresh due 2026-12-01.
- [Cytoscape.js Graph Theory Network Library Documentation](https://js.cytoscape.org/), retrieved 2026-11-01, refresh due 2026-12-01.
- [MDN Web Docs: SVG viewBox Attribute](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/viewBox), retrieved 2026-11-01, refresh due 2026-12-01.
- [MDN Web Docs: Window.devicePixelRatio Property](https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio), retrieved 2026-11-01, refresh due 2026-12-01.
- [MDN Web Docs: CanvasRenderingContext2D.scale() and HiDPI Transforms](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/scale), retrieved 2026-11-01, refresh due 2026-12-01.
- [MDN Web Docs: Optimizing HTML5 Canvas Performance](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Optimizing_canvas), retrieved 2026-11-01, refresh due 2026-12-01.
- [MDN Web Docs: ResizeObserver Interface](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver), retrieved 2026-11-01, refresh due 2026-12-01.
- [MDN Web Docs: Intersection Observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API), retrieved 2026-11-01, refresh due 2026-12-01.
- [Obsidian API TypeScript Definitions: obsidian.d.ts (DOM, SVG, and Popout Window Helpers)](https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts), retrieved 2026-11-01, refresh due 2026-12-01.

## Related

- [[Source src-03-jsoncanvas-spec-1-0]]
- [[Source src-03-obsidian-api-canvas-dts]]
- [[Source src-03-obsidian-css-canvas-vars]]
- [[Source src-03-obsidian-css-graph-vars]]
- [[Source src-03-obsidian-css-colors-vars]]
- [[Source src-03-d3-force]]
- [[Source src-03-d3-zoom]]
- [[Source src-03-cytoscape-js]]
- [[Source src-03-mdn-svg-viewbox]]
- [[Source src-03-mdn-device-pixel-ratio]]
- [[Source src-03-mdn-canvas-scale]]
- [[Source src-03-mdn-optimizing-canvas]]
- [[Source src-03-mdn-resize-observer]]
- [[Source src-03-mdn-intersection-observer]]
- [[Source src-03-obsidian-api-dts]]
- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[Obsidian Bases API, native dashboards, and query surfaces]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
