# Architecture Decision

Decision owner and date: not supplied.

## Problem and constraints

Record the user task, input sizes, target platforms, required app version,
performance budget, state lifetime, and recovery needs.

## Alternatives and decision

Compare the smallest plausible command, view, Bases, editor, Markdown, visual,
or service surface. Name the selected option and its tradeoff. Record why any
framework, renderer, worker, cache, or backend is needed.

## Contracts

| Boundary | Owner | API and source | Failure and cleanup |
|---|---|---|---|
| Domain state | Not selected | Not selected | Not specified |
| Per-leaf UI | Not selected | Not selected | Not specified |
| Vault/metadata access | Not selected | Not selected | Not specified |
| Settings and storage | Not selected | Not selected | Not specified |
| Background resources | Not selected | Not selected | Not specified |
| External services | None by default | Not selected | Not specified |

## Verification and change

Map criteria to modules and tests. Record every relevant API symbol's source and
version assumption. Define a migration or rollback when this decision changes.
Keep an exact artifact/dependency hash with observed acceptance results.
