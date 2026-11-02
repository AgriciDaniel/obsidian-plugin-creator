---
type: "gap"
title: "SecretStorage and OS keychain availability across desktop vs iOS and Android plu"
domain: "Obsidian plugin engineering"
status: "open"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/gap"
  - "confidence/practitioner"
related:
  - "[[Plugin Data and Integration Design]]"
  - "[[Plugin Creator Studio]]"
  - "[[Research Pack]]"
  - "[[Claim Verification Flow]]"
  - "[[Source SRC-02-007]]"
  - "[[Source SRC-01-002]]"
source_urls:
  - "https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Store%20secrets.md"
  - "https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts"
---

# SecretStorage and OS keychain availability across desktop vs iOS and Android plu

[evidence-based] The source pack includes the public SecretStorage/SecretComponent guide. [practitioner] Do not infer OS keychain, encryption, synchronization, or protection from other enabled plugins. The cross-device security properties named by this gap still require specific evidence.

## Evidence and next action

Keep the evidence class, exact artifact, app/device, source date, expected/observed result, and remaining gap visible. Use the matching creator playbook for the next project-specific task.

## Sources

- [[Source SRC-02-007]]: [Obsidian SecretStorage and SecretComponent guide](https://github.com/obsidianmd/obsidian-developer-docs/blob/1c26772ac13d6e9870c865936d389fdfe694e742/en/Plugins/Guides/Store%20secrets.md), retrieved 2026-11-01.
- [[Source SRC-01-002]]: [Obsidian public TypeScript API declarations](https://github.com/obsidianmd/obsidian-api/blob/9abd9605ce081383674aae1ed111c456edde0688/obsidian.d.ts), retrieved 2026-11-01.

## Related

- [[Plugin Data and Integration Design]]
- [[Plugin Creator Studio]]
- [[Research Pack]]
- [[Claim Verification Flow]]
- [[Source SRC-02-007]]
- [[Source SRC-01-002]]
