# Obsidian Plugin Creator Product Spec

## Buyer

Indie makers, developer-creators, tool builders, and AI engineering teams who build vault-specific or Community Store Obsidian plugins and need source-cited official APIs, review rules, and scope-specific architecture patterns instead of outdated forum folklore.

## Domain

Architecting, building, styling, optimizing, testing, auditing, and shipping Obsidian plugins across all plugin scopes: core commands, multi-pane dashboards and Bases views, 2D and 3D WebGL visuals and canvases, CodeMirror 6 editor extensions, Markdown processors, vault and MetadataCache engines, mobile compatibility, and Community Store releases.

## Core Workflows

- Plugin scope classification and architecture selection across commands, custom views, Bases views, 2D and 3D visuals, CodeMirror 6 extensions, Markdown processors, and vault indexers
- Lifecycle, Component ownership, and cleanup design for onload, onunload, registered events, intervals, and deferred workspace leaves
- Dashboard, ItemView, Bases view, modal, suggest, and settings UX engineering with theme-native Obsidian CSS variables
- 2D Canvas, SVG, and 3D WebGL or Three.js visual engineering with ResizeObserver sizing, tab-visibility render throttling, and GPU disposal
- Editor and Markdown pipeline engineering across Source mode, Live Preview (CodeMirror 6), and Reading view post-processors
- Vault, FileManager, MetadataCache, atomic background edits, and deep subpath or URI interlinking
- Cross-platform mobile hardening (iOS and Android), startup performance profiling, Sync-safe storage, and XSS security review
- Pre-submission static review against obsidianmd/eslint-plugin, obsidian-releases bot checks, versions.json parity, and GitHub Actions release packaging

## Deliverables

- Plugin scope and architecture decision matrix mapping product goals to Obsidian API surfaces
- Community Store submission and eslint-plugin readiness scorecard
- Lifecycle, memory-leak, and deferred-view audit checklist
- Visuals, dashboards, Bases, and 3D WebGL engineering runbook
- CodeMirror 6 Live Preview and Reading view parity guide
- Mobile compatibility, Sync storage budget, and security hardening report

## Promise

Turn raw sources and recurring decisions into a persistent, source-cited
operating brain.

## Non-Promises

- No unsourced Obsidian API, submission policy, or version claims
- No guidance that violates official Obsidian Plugin Guidelines such as calling detachLeavesOfType in onunload or injecting unsanitized innerHTML
- No recommendation to bundle duplicate @codemirror/* or obsidian runtime modules into main.js
- No credentials, API keys, sync tokens, or private vault content in repo artifacts or sample fixtures
- No account, registry, or host-system mutation in V1
- No irreversible recommendation without owner, confidence, source, and rollback note

## Creator Workflow and Artifacts

Version 0.2.0 adds discovery, product acceptance, API/lifecycle contracts, UX and accessibility, data/migrations, implementation, verification/performance, release/maintenance, debugging, and advanced-surface playbooks. Reusable contracts and a source-artifact generator connect those decisions to a real project.

The generator supports eight small reference surfaces and an exact dependency lock. Each generated project requires its own implementation of the product brief and its own runtime/device acceptance. Generation does not authorize note mutation, active installation, external service spending, or publication.

Source artifacts are written only to new directories below an explicitly selected workspace, with dry-run and SHA256 receipts. Recovery preserves any subsequent user edits. Full details and acceptance are in docs/CREATOR_PLAN.md.
