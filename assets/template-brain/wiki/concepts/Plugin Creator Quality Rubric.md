---
type: "concept"
title: "Plugin Creator Quality Rubric"
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
  - "[[Plugin Creator Studio]]"
  - "[[Runtime Acceptance Matrix]]"
  - "[[Research Pack]]"
  - "[[Plugin Discovery and Brief]]"
  - "[[Plugin Architecture and API Contract]]"
  - "[[Plugin UX and Accessibility]]"
  - "[[Plugin Data and Integration Design]]"
  - "[[Plugin Implementation Workflow]]"
source_urls: []
---

# Plugin Creator Quality Rubric

[practitioner] Review the actual plugin against user outcomes and retained evidence. This is a project review aid, separate from the Brainstein structural score.

| Category | Weight | What earns credit | Required evidence |
|---|---|---|---|
| Product usefulness | 20 | A clear recurring task and fulfilled acceptance criteria | Actual task completion and user review |
| Architecture and lifecycle | 15 | Appropriate surfaces, clean ownership, compatibility and cleanup | Sources, implementation review, runtime lifecycle cases |
| UX and accessibility | 15 | Native themes, useful states, keyboard/touch and readable alternatives | Actual interface and input-method checks |
| Data and integrations | 15 | Validated data, recovery, safe writes, correct disclosures and secrets | Malformed/failure/migration cases and observed storage/requests |
| Performance | 10 | Agreed startup, interaction, memory, bundle and storage budgets | Representative measured runs with samples and conditions |
| Verification | 15 | Meaningful regressions and the promised platform/mode coverage | Exact artifact, commands, raw results, actual devices |
| Release and maintainability | 10 | Current policy, license, exact assets, rollback and support | Reviewable package, source dates, notices, maintenance plan |

## Scoring rule

Record earned points, assessed points, and evidence coverage separately. Unknown categories are unscored, never silently treated as passed. Do not report a release-ready score until every mandatory evidence class is assessed. Record n = 0 as no data.

Example: 15 points earned out of 20 assessed is 75% of assessed points with only 20% of total rubric coverage. It does not mean the plugin is 75% ready for release.

## Blocking findings

- Destructive note writes without a defined scope, recovery copy, and verified rollback.
- Leaked credentials, undisclosed remote content transmission, or unsafe handling of untrusted input.
- False claims about runtime, mobile, security, measured performance, review outcomes, or market evidence.
- A broken primary task or inaccessible primary action with no usable alternative.
- Distribution of an artifact that differs from the tested artifact or lacks required licensing decisions.

## Review record

For each finding, record severity, file and line, user trigger, expected/observed behavior, evidence class, practical fix, owner, and recheck result. Preserve dissent and unresolved uncertainty.

## Next action

Use [[Plugin Verification and Performance]] to close the highest-impact evidence gap, then [[Plugin Release and Maintenance]] for a concrete release candidate. Technical contracts remain in [[Research Pack]].
