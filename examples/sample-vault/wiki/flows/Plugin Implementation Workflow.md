---
type: "flow"
title: "Plugin Implementation Workflow"
domain: "Obsidian plugin engineering"
status: "active"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/flow"
  - "confidence/practitioner"
related:
  - "[[Plugin Creator Studio]]"
  - "[[Plugin Architecture Matrix]]"
  - "[[Runtime Acceptance Matrix]]"
  - "[[Research Pack]]"
  - "[[Plugin Discovery and Brief]]"
  - "[[Plugin Architecture and API Contract]]"
  - "[[Plugin UX and Accessibility]]"
  - "[[Plugin Data and Integration Design]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-sample-plugin/blob/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/esbuild.config.mjs"
  - "https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/package.json"
  - "https://registry.npmjs.org/obsidian/1.14.4"
  - "https://registry.npmjs.org/eslint-plugin-obsidianmd/0.4.2"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md"
---

# Plugin Implementation Workflow

[practitioner] A brief and architecture contract are ready for a local implementation slice.

## When to invoke

Use this playbook at the matching creator stage. It applies the cited official contracts; its sequence is engineering judgment.

## Prerequisites

Read [[Plugin Creator Studio]], the project brief, and the relevant technical concept. Record missing inputs as no data. Preserve unrelated work and immutable raw evidence.

## Step by step

1. Select an archetype with the starter catalog and review the example brief. Preserve existing projects; the generator creates only a new source folder.
2. Run create-plugin with --dry-run first when inspecting the output contract, then generate into an explicit workspace outside active vaults.
3. Read the generated product brief, architecture, acceptance record, source list, and file-hash receipt before editing.
4. Use the included exact dependency lock. The initial toolchain is Node 24, and the current lint peer override is explicit in package.json.
5. Install dependencies only in the chosen local source project. Run the actual TypeScript check, build, and official lint; retain failures instead of suppressing rules to obtain a green result.
6. Implement one product criterion end to end, including its empty/error state and cleanup. The example starter behavior is not the completed product.
7. Add domain tests for meaningful behavior and failure cases. Avoid tests that merely repeat implementation constants.
8. Run the brain's preliminary static review, then inspect the actual compiled bundle and external imports. Resolve heuristic false positives manually with evidence.
9. Use an explicitly chosen disposable development vault for runtime work. Source generation does not copy or enable a plugin in any vault.
10. Record the change, checked criteria, source/API decisions, artifact hashes, and remaining unknowns before expanding the slice.

## Outputs

- A new source project with a receipt
- A product-specific implemented vertical slice
- Build/lint outputs and a bounded next implementation task

## Quality gates

- Existing work is never overwritten by generation
- The generated source can be checked with the exact retained lock
- Product-specific criteria still show their actual status

## Failure modes

- Equating generation with feature completion
- Installing into the main vault to speed up development
- Using force or legacy peer resolution to hide an unexplained dependency conflict

## Sources

Paraphrase and application; no independent corroboration is implied by repeated upstream works.

- [[Source SRC-01-007]]: [Official sample plugin esbuild configuration](https://github.com/obsidianmd/obsidian-sample-plugin/blob/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/esbuild.config.mjs), retrieved 2026-11-01.
- [[Source SRC-06-001]]: [Official sample plugin package and scripts](https://raw.githubusercontent.com/obsidianmd/obsidian-sample-plugin/07ceb81d1fb3384af611ebf665a1ec42a7e5926d/package.json), retrieved 2026-11-01.
- [[Source SRC-06-002]]: [Obsidian npm API package 1.14.4 metadata](https://registry.npmjs.org/obsidian/1.14.4), retrieved 2026-11-01.
- [[Source SRC-06-003]]: [Official Obsidian ESLint package 0.4.2 metadata](https://registry.npmjs.org/eslint-plugin-obsidianmd/0.4.2), retrieved 2026-11-01.
- [[Source SRC-01-001]]: [Obsidian plugin guidelines](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Plugin%20guidelines.md), retrieved 2026-11-01.

## Related

- [[Plugin Creator Studio]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
- [[Research Pack]]
- [[Plugin Discovery and Brief]]
- [[Plugin Architecture and API Contract]]
- [[Plugin UX and Accessibility]]
- [[Plugin Data and Integration Design]]
