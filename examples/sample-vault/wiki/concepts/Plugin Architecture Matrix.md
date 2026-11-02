---
type: "concept"
title: "Plugin Architecture Matrix"
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
  - "[[Research Pack]]"
  - "[[Runtime Acceptance Matrix]]"
  - "[[Index]]"
  - "[[Dashboard]]"
source_urls: []
---

# Plugin Architecture Matrix

[practitioner] Choose the smallest surface that lets the user complete the task. Combine scopes only where the same product needs them. The source notes establish public contracts; this matrix is engineering judgment.

| User task | Starting surface | Companion surface | First acceptance check |
|---|---|---|---|
| Invoke an action | Plugin command | Modal or suggest | Command is available only in the right context |
| Explore a persistent dashboard | ItemView | Commands and settings | Split panes retain independent state |
| Present a query of note properties | BasesView | Bases query/property model | Query changes update results correctly |
| Embed a small interactive widget in a note | Markdown processor | CodeMirror extension for editing parity | Reading and Live Preview agree |
| Annotate or transform an editing experience | CodeMirror 6 extension | Markdown processor | Selection, composition input, undo/redo remain correct |
| Share spatial document data | JSON Canvas | Custom SVG or Canvas renderer | Round-trip schema validation preserves IDs |
| Explore a rich 3D scene | ItemView with WebGL renderer | Searchable accessible list | Closing/hiding the pane releases or pauses owned work |
| Maintain a vault graph or index | Vault and MetadataCache services | ItemView or Bases presentation | Rename/delete events do not leave stale state |

## Implementation sequence

1. Write the user task, inputs, permissions, platform targets, and definition of done.
2. Open the matching concept and its dated official source notes.
3. Choose the minimum app version from the APIs actually used.
4. Draw lifecycle ownership for each view, observer, listener, framework root, worker, and GPU resource.
5. Build a minimal vertical slice with loading, empty, malformed input, and error states.
6. Run the static review, then the real build and official lint.
7. Complete [[Runtime Acceptance Matrix]] on the actual targets.
8. Refresh release policies and obtain owner approval before distribution.

## Required intake

Record plugin purpose, expected vault size, UI surfaces, minimum app version, desktop/mobile targets, network services, secret handling, persistent data, and release channel. Identify an existing plugin repository if one is being reviewed. Never import a private vault just to infer these requirements.

## Guided reading

- [[Plugin lifecycle, Component ownership, and cleanup discipline]]
- [[Workspace leaves, custom ItemView dashboards, and deferred views]]
- [[Obsidian Bases API, native dashboards, and query surfaces]]
- [[2D graphs, JSON Canvas 1.0, SVG diagrams, and interactive visualizations]]
- [[3D WebGL, Three.js, React Three Fiber, and spatial codex views]]
- [[CodeMirror 6 architecture, StateFields, ViewPlugins, and Live Preview]]
- [[Vault API, FileManager, atomic edits, and DataAdapter boundaries]]
- [[Community Store submission, eslint-plugin review gates, BRAT, and release CI]]
