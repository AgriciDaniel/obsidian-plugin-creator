---
type: "meta"
title: "Plugin Creator Studio"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/meta"
  - "confidence/practitioner"
related:
  - "[[Plugin Discovery and Brief]]"
  - "[[Plugin Architecture and API Contract]]"
  - "[[Plugin UX and Accessibility]]"
  - "[[Plugin Data and Integration Design]]"
  - "[[Plugin Implementation Workflow]]"
  - "[[Plugin Verification and Performance]]"
  - "[[Plugin Release and Maintenance]]"
  - "[[Plugin Debugging and Learning]]"
  - "[[Plugin Advanced Surfaces]]"
  - "[[Plugin Creator Quality Rubric]]"
  - "[[Research Pack]]"
source_urls: []
---

# Plugin Creator Studio

Turn an idea into a specified, implemented, tested, and maintainable plugin. Start with a brief, choose one surface, generate a local source artifact, then complete its actual product criteria.

## Working path

1. [[Plugin Discovery and Brief]]
2. [[Plugin Architecture and API Contract]]
3. [[Plugin UX and Accessibility]]
4. [[Plugin Data and Integration Design]]
5. [[Plugin Implementation Workflow]]
6. [[Plugin Verification and Performance]]
7. [[Plugin Release and Maintenance]]
8. [[Plugin Debugging and Learning]]
9. [[Plugin Advanced Surfaces]]

## Source starters

The complete source checkout supports command, dashboard, Bases, editor, Markdown, 2D Canvas, Three.js, and vault-index starters. Generated projects contain source, an exact dependency lock, build/lint configuration, product and acceptance records, sources, and a file-hash receipt.

```bash
python3 -m obsidian_plugin_brain starters
python3 -m obsidian_plugin_brain create-plugin --brief references/creator/example-brief.json --out created-projects/heading-compass --dry-run
```

Remove --dry-run to create a new source folder within the selected workspace. The generator refuses existing outputs, symlink destinations, and active/deployed vault locations. It performs no network calls, dependency installation, plugin execution, or active-vault installation.

## Reusable contracts

The vault's references/creator/templates folder supplies a product brief, architecture decision, UI state specification, data/migration design, acceptance record, release checklist, session handoff, and change request. Keep each project's filled contracts beside its source.

## Quality and evidence

Use [[Plugin Creator Quality Rubric]] and [[Runtime Acceptance Matrix]]. Generated example source is not the completed product. A generic build result does not establish another project's runtime, mobile, performance, security, market demand, or submission acceptance.

## Grounding

Read [[Research Pack]] and the linked official source before making domain claims. Refresh sources monthly and before release. Practitioner decisions must name their tradeoffs.

## Explore the graph

See [[Graph Views]] for the palette and seven saved views. Create a new working vault from the complete source checkout to activate these settings locally.
