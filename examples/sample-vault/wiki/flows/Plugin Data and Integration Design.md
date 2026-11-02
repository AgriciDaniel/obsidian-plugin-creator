---
type: "flow"
title: "Plugin Data and Integration Design"
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
  - "[[Plugin Implementation Workflow]]"
source_urls:
  - "https://docs.obsidian.md/Plugins/Vault"
  - "https://docs.obsidian.md/Reference/TypeScript+API/FileManager"
  - "https://docs.obsidian.md/Reference/TypeScript+API/MetadataCache"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Store%20secrets.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Developer%20policies.md"
---

# Plugin Data and Integration Design

[practitioner] The plugin will persist settings, maintain an index, write notes, use credentials, or contact external services.

## When to invoke

Use this playbook at the matching creator stage. It applies the cited official contracts; its sequence is engineering judgment.

## Prerequisites

Read [[Plugin Creator Studio]], the project brief, and the relevant technical concept. Record missing inputs as no data. Preserve unrelated work and immutable raw evidence.

## Step by step

1. Inventory settings, user content, derived caches, credentials, logs, and remote data. Give each a storage location, lifetime, owner, and sensitivity.
2. Keep derived indexes rebuildable and separate from compact settings. Record a cache key and invalidation rule for every input that changes a result.
3. Define a schema version and validate persisted data before use. Preserve a recovery copy before migration, and test interrupted, repeated, and failed migrations.
4. Use public Vault/FileManager surfaces for ordinary note operations and plan conflict handling for external edits, rename, and deletion.
5. Require an approved write scope, preview where appropriate, and rollback for note mutations. Generating source does not authorize changing user notes.
6. Use the supported secret API when available. Store identifiers rather than raw values in settings, and do not claim keychain, encryption, Sync, or plugin isolation guarantees without direct evidence.
7. List every remote service, request payload, transmitted note content, retention policy, and user-facing disclosure before adding integration code.
8. Handle offline mode, timeout, cancellation, rate limits, partial results, missing credentials, and unknown billing. Never report unknown cost as zero.
9. For external APIs, research the actual current provider contract separately and bind paid actions to an explicit approved plan.
10. Create malformed-data, old-schema, deleted-file, denied-request, missing-secret, and recovery fixtures without retaining credentials or customer content.

## Outputs

- DATA_AND_MIGRATIONS.md
- Storage and network disclosure inventory
- Migration, integration failure, and recovery acceptance cases

## Quality gates

- No write occurs without a defined scope and recovery path
- No secret or private content is embedded in distributable artifacts
- Cache loss and network failures preserve user content

## Failure modes

- Mixing large derived data with syncable settings by default
- Assuming all enabled plugins are isolated from secrets
- Treating a successful request as proof of correct data handling or billing

## Sources

Paraphrase and application; no independent corroboration is implied by repeated upstream works.

- [[Source SRC-04-021]]: [Obsidian Developer Documentation - Vault](https://docs.obsidian.md/Plugins/Vault), retrieved 2026-11-01.
- [[Source SRC-04-023]]: [Obsidian TypeScript API Reference - FileManager](https://docs.obsidian.md/Reference/TypeScript+API/FileManager), retrieved 2026-11-01.
- [[Source SRC-04-027]]: [Obsidian TypeScript API Reference - MetadataCache](https://docs.obsidian.md/Reference/TypeScript+API/MetadataCache), retrieved 2026-11-01.
- [[Source SRC-02-007]]: [Obsidian SecretStorage and SecretComponent guide](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Store%20secrets.md), retrieved 2026-11-01.
- [[Source SRC-01-005]]: [Obsidian Community directory developer policies](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Developer%20policies.md), retrieved 2026-11-01.

## Related

- [[Plugin Creator Studio]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
- [[Research Pack]]
- [[Plugin Discovery and Brief]]
- [[Plugin Architecture and API Contract]]
- [[Plugin UX and Accessibility]]
- [[Plugin Implementation Workflow]]
