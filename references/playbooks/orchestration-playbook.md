# Obsidian Plugin Brain: Wizard Orchestration Playbook


> Use this playbook to coordinate multi-agent work via file-backed task
> packets at `references/orchestration/`.

## When to invoke

- Starting a multi-step gate transition with multiple agents.
- Coordinating human + AI work across timezones.
- Migrating between AI runtimes (the file-backed packets are runtime-neutral).

## Prerequisites

- `brainstein wizard --slug <slug> --out specs/<slug>.yaml` has been run.
- `brainstein orchestrate <repo>` has initialized `run.json`.

## Step-by-step

1. Read `references/orchestration/run.json` for current gate target.
2. For each role packet (research-scout, vault-architect, domain-adapter,
   demo-verifier, release-gate, brain-auditor, coach, playbook-writer), open
   the corresponding `tasks/<role>.json`.
3. Dispatch agents (or humans) to the open tasks.
4. As tasks complete, append a `result.json` under
   `references/orchestration/results/<task-id>.json`.
5. Run `brainstein gate <repo> --stage <gate>` to advance the gate.
6. Update `wiki/activity.md` with the gate transition.

## Outputs

- Updated `run.json` with the new gate state.
- Completed `results/*.json` for finished tasks.
- `wiki/activity.md` entry timestamped at the transition.

## Sources

- [[Wizard Orchestration]]
- [[Brain Factory Lifecycle]]
