# Obsidian Plugin Brain: Runtime Portability Playbook


> Use this playbook to verify a brain runs across multiple AI runtimes:
> Claude Code, OpenAI Codex, Gemini CLI, and OpenClaw.

## When to invoke

- A brain is `domain-adapted` or later and must publish portable agent docs.
- Adding a new runtime target to the installer.

## Prerequisites

- `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` exist at the brain root.
- The brain's `SKILL.md` is self-contained and references only public docs.

## Step-by-step

1. Read [[Runtime Portability Matrix|the matrix]] for current runtime status.
2. For each target runtime, run the installer with the corresponding `--target`.
3. Open the brain in that runtime and verify the SKILL.md description triggers.
4. Run the brain's primary command (e.g. `/<slug> audit .`).
5. Capture screenshots into `assets/screenshots/` as evidence of the check.
6. Update [[Runtime Portability Matrix]] with the verification date.

## Outputs

- Verified install on all four runtimes.
- Updated matrix with dates.
- Screenshots committed (or placeholders if matrix entry is deferred).

## Sources

- [[Runtime Portability Matrix]]
- [[Wizard Orchestration]]
