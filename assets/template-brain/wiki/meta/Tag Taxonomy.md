---
type: "meta"
title: "Tag Taxonomy"
domain: "Architecting, building, styling, optimizing, testing, auditing, and shipping Obsidian plugins across all plugin scopes: core commands, multi-pane dashboards and Bases views, 2D and 3D WebGL visuals and canvases, CodeMirror 6 editor extensions, Markdown processors, vault and MetadataCache engines, mobile compatibility, and Community Store releases."
status: "evergreen"
created: "{{date}}"
updated: "{{date}}"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/meta"
  - "confidence/practitioner"
confidence: "practitioner"
related:
  - "[[CONVENTIONS]]"
  - "[[Start Here]]"
  - "[[Index]]"
  - "[[Overview]]"
  - "[[Home]]"
  - "[[Activity]]"
  - "[[Dashboard]]"
  - "[[Tag Taxonomy]]"
  - "[[Source Intake Workflow]]"
  - "[[Research Refresh Workflow]]"
  - "[[Claim Verification Flow]]"
  - "[[Synthesis Workflow]]"
  - "[[Reporting Workflow]]"
  - "[[Source Manifest Guide]]"
  - "[[Best Practices Kernel]]"
  - "[[Health Scorecard]]"
  - "[[Action Roadmap]]"
  - "[[Weekly Report]]"
  - "[[Approval Queue]]"
  - "[[wiki/flows/_index|Flows Hub]]"
  - "[[wiki/sources/_index|Sources Hub]]"
  - "[[wiki/concepts/_index|Concepts Hub]]"
  - "[[wiki/decisions/_index|Decisions Hub]]"
  - "[[wiki/deliverables/_index|Deliverables Hub]]"
  - "[[wiki/reports/_index|Reports Hub]]"
  - "[[wiki/questions/_index|Questions Hub]]"
  - "[[wiki/gaps/_index|Gaps Hub]]"
  - "[[wiki/experiments/_index|Experiments Hub]]"
source_urls: []
---

# Tag Taxonomy

Lowercase hierarchical tags govern graph colors, Bases views, and note maintenance. Every wiki note carries one domain tag, one type tag, and one confidence tag in frontmatter.

In frontmatter, list tags without the leading `#` (for example `type/concept`), as Obsidian's properties expect. The `#` form below is how you type tags in a note body and how you search for them.

## Domain tags

- `#domain/architecting-building-styling-optimizing-testing-auditing-and-sh` for Architecting, building, styling, optimizing, testing, auditing, and shipping Obsidian plugins across all plugin scopes: core commands, multi-pane dashboards and Bases views, 2D and 3D WebGL visuals and canvases, CodeMirror 6 editor extensions, Markdown processors, vault and MetadataCache engines, mobile compatibility, and Community Store releases. notes. This tag supplies the final fallback graph color; specific note types have priority.

If a generated brain later adds a real subdomain, add the new `#domain/<subdomain>` tag here first, then add graph color coverage, then update the affected notes.

## Type tags

`#type/hot`, `#type/index`, `#type/overview`, `#type/log`, `#type/meta`, `#type/hub`, `#type/flow`, `#type/source`, `#type/concept`, `#type/entity`, `#type/account`, `#type/platform`, `#type/decision`, `#type/deliverable`, `#type/report`, `#type/question`, `#type/gap`, `#type/experiment`, `#type/dashboard`

The type tag mirrors the `type` frontmatter field and powers dashboard grouping.

## Confidence tags

`#confidence/evidence-based`, `#confidence/practitioner`, `#confidence/contested`, `#confidence/folklore`

Use the same lowercase value in the `confidence` field. Source-ledger confidence maps as follows:

| Ledger value | Note confidence | Tag |
|---|---|---|
| high | evidence-based | `#confidence/evidence-based` |
| med | practitioner | `#confidence/practitioner` |
| low | contested | `#confidence/contested` |

## Graph discipline

Graph color groups use `#type/*` tags first and the shared `#domain/*` tag last as a fallback. The graph search limits the view to `wiki/`. Generic defaults are in `assets/vault-defaults/` in the complete source checkout and become local `.obsidian/` settings in a new working vault. Keep existing note types accurate rather than adding tags only for decoration. See [[Graph Views]] for the palette, saved views, and filters.

## Related

- [[CONVENTIONS]]
- [[Dashboard]]
- [[Index]]
- [[Start Here]]
