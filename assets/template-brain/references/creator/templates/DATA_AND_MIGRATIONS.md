# Data, Migrations, and Integrations

## Inventory

| Data | Location | Schema/version | Sensitivity | Lifetime and recovery |
|---|---|---|---|---|
| User settings | Not selected | Not designed | Review required | Not designed |
| Derived cache | Not selected | Rebuildable by design | May reflect private notes | Not designed |
| Credentials | None by default | Secret identifiers only when supported | Secret | No value in logs/artifacts |
| Network payloads | None by default | Current provider contract required | Review required | Not designed |
| Note changes | None by default | Explicit write plan required | User content | Backup and rollback required |

## Migration contract

Record source and target schema, validation, preconditions, backup, interrupted
operation behavior, idempotency, downgrade limitations, and rollback. Test old,
malformed, partially migrated, repeated, and failed inputs. Keep the original
data until the result is verified.

## Concurrency and cache

Define cache keys, invalidation, rename/delete behavior, external edits, partial
metadata, cancellation, large-vault work, and rebuild costs. Do not settle unknown
data into zero. A cache miss and an empty source are different states.

## Network and cost

Specify each service, endpoint purpose, transmitted content, retention, account,
secret reference, timeout, cancellation, retry, rate limit, cost approval, and
user disclosure. Unknown billing remains unknown. Do not assume secret storage
encryption, OS keychain behavior, Sync, or isolation without specific evidence.
