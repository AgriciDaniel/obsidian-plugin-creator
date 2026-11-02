# Creator plan

The public edition connects a source-backed knowledge vault to planning,
source-artifact creation, static review, and explicit verification records.

| Stage | Output |
| --- | --- |
| Discovery | A target user, useful task, and testable first slice |
| Architecture | Suitable API surface, lifecycle ownership, and data boundaries |
| Creation | One of eight small source starters with an exact dependency lock |
| Implementation | The actual product feature, including empty and error states |
| Verification | Compiler, lint, app, device, and performance results kept distinct |
| Release preparation | Reviewable assets, notices, policy checks, and support plan |
| Learning | Sources and reasoning retained in a separate working vault |

The new source directory must not exist and must be outside an active vault.
Generation is offline, refuses overwrite and unsafe destinations, and records
file hashes. It does not install dependencies, execute code, edit notes, install
an active plugin, or publish anything.

The public source catalog preserves the references needed by the creator and
reviewer. Private source captures and operational history are not distributed.
The `new` command creates private intake and Obsidian configuration locally in
a fresh working vault. See [Public distribution](PUBLIC_DISTRIBUTION.md).

Actual plugin functionality, app behavior, devices, integrations, and release
acceptance remain project-specific checks. A starter cannot satisfy an arbitrary
brief without implementation.
