---
type: "flow"
title: "Plugin Release and Maintenance"
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
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/Manifest.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Submit%20your%20plugin.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Developer%20policies.md"
  - "https://github.com/obsidianmd/eslint-plugin/blob/837b01dc1647cb3f0c532becb60ea83bec137656/docs/configuration.md"
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Submission%20requirements%20for%20plugins.md"
---

# Plugin Release and Maintenance

[practitioner] A tested artifact is being prepared for local distribution or an approved public release.

## When to invoke

Use this playbook at the matching creator stage. It applies the cited official contracts; its sequence is engineering judgment.

## Prerequisites

Read [[Plugin Creator Studio]], the project brief, and the relevant technical concept. Record missing inputs as no data. Preserve unrelated work and immutable raw evidence.

## Step by step

1. Refresh the actual directory submission guide, developer policies, lint configuration, and API compatibility before deciding release readiness.
2. Inspect the exact main.js, manifest.json, optional styles.css, compatibility map, package version, tag plan, and distribution archive.
3. Decide the plugin license and include required third-party notices for bundled dependencies. Development-only dependency presence is not the same as bundled code.
4. Ensure the visible README describes network requests, note writes, external file access, accounts, payment, and server-side telemetry where applicable.
5. Link the exact artifact to its product acceptance, runtime/device, accessibility, security, and performance evidence. Preserve known limitations.
6. Prepare update and data migration instructions, recovery copies, rollback assets, and support diagnostics that exclude secrets and private note content.
7. Use the current Community directory workflow. Historical registry pull-request instructions are not sufficient evidence for the current channel.
8. Obtain the owner's explicit approval immediately before any tag, push, public release, submission, account change, or active-vault installation.
9. After an approved release, retain the actual directory/review outcome. A clean local lint run does not establish acceptance.
10. Maintain a refresh cadence for APIs, toolchain peers, policies, dependencies, bugs, migration behavior, and regression fixtures.

## Outputs

- RELEASE_CHECKLIST.md
- Exact local artifact manifest and notices
- Maintenance, support, and rollback plan

## Quality gates

- Only the tested and hashed artifact is proposed for release
- Disclosures and license match the actual behavior and bundle
- Publication is an owner-authorized action with retained outcome

## Failure modes

- Treating a structural brain score as plugin directory acceptance
- Updating the binary without considering the persisted schema
- Shipping a dependency or runtime behavior that the README does not disclose

## Sources

Paraphrase and application; no independent corroboration is implied by repeated upstream works.

- [[Source SRC-01-003]]: [Obsidian manifest specification](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Reference/Manifest.md), retrieved 2026-11-01.
- [[Source SRC-01-004]]: [Submit a plugin to the Obsidian Community directory](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Releasing/Submit%20your%20plugin.md), retrieved 2026-11-01.
- [[Source SRC-01-005]]: [Obsidian Community directory developer policies](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Developer%20policies.md), retrieved 2026-11-01.
- [[Source SRC-01-006]]: [Official Obsidian ESLint configuration guide](https://github.com/obsidianmd/eslint-plugin/blob/837b01dc1647cb3f0c532becb60ea83bec137656/docs/configuration.md), retrieved 2026-11-01.
- [[Source SRC-01-009]]: [Obsidian plugin submission requirements](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Community%20directory/Submission%20requirements%20for%20plugins.md), retrieved 2026-11-01.

## Related

- [[Plugin Creator Studio]]
- [[Plugin Architecture Matrix]]
- [[Runtime Acceptance Matrix]]
- [[Research Pack]]
- [[Plugin Discovery and Brief]]
- [[Plugin Architecture and API Contract]]
- [[Plugin UX and Accessibility]]
- [[Plugin Data and Integration Design]]
