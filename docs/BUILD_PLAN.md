# Obsidian Plugin Brain Completion Plan

Recovered 2026-11-01 after the research run stopped at a quota limit.

Build one local advisory brain that helps an author scope, implement, inspect,
and verify Obsidian plugins. The brain supplies dated sources, engineering
recipes, a read-only static review tool, and a navigable Obsidian vault.

## Scope

| Scope | Knowledge coverage | Required verification for a real plugin |
|---|---|---|
| Commands and lifecycle | Component ownership, event registration, settings, unload | Enable, disable, reload, command availability, listener cleanup |
| Dashboards and Bases | ItemView, workspace state, deferred leaves, BasesView | Split panes, reopen workspace, hidden panes, changing query results |
| 2D and 3D visuals | JSON Canvas, SVG, WebGL, resize, disposal | Theme change, resize, hide/show, context loss, GPU cleanup |
| Editor | CodeMirror 6 extensions, decorations, editor state | Source, Live Preview, composition input, large notes |
| Markdown | Reading view post-processors and code blocks | Re-render, embeds, unload, parity with editor output |
| Vault and metadata | Vault/FileManager, cached metadata, link resolution | Rename, delete, unresolved links, external edits, failure recovery |
| Platform and security | Mobile, startup, storage, secrets, network disclosure | Real devices, permission boundaries, network failures, malicious input |
| Release | Manifest, bundling, lint, policy, compatibility, packaging | Build and official lint, exact release assets, current submission process |

## Work and ownership

The primary session owns consolidation, canon, vault navigation, operating
guidance, deterministic demo generation, and final verification. Bounded workers
recover the two missing research reports, verify the three surviving reports,
and repair the static adapter. Each worker owns different files.

The current session model handles specification, integration, and review inline.
Workers inherit the session model. This uses the current Codex session; no paid
API calls or subscription changes are part of the build. Escalate on failed
checks, contradictory sources, or API behavior that cannot be established from
official documentation. Do not substitute confidence for runtime evidence.

## Acceptance

1. All eight scopes have useful source-cited guidance.
2. Research entries name an actual retrieved source, date, claim coverage, and
   refresh due date. Disputed and untested inferences remain visible.
3. All 16 canon topics are folded into linked wiki concepts.
4. The static adapter runs and tests healthy, flawed, malformed, and unsafe
   inputs. Reports identify heuristic limits and unperformed checks.
5. Template and sample vaults pass lint. Demo output reproduces from a fixed
   reference date and matches its retained SHA256 manifest.
6. Compilation, pipeline tests, adapter tests, and both local maturity and
   Brainstein structural audits are run. Preserve their actual results.
7. Local ZIP packaging and integrity scans are verified if authorized by the
   project's verification instructions. No installation into active agent
   configurations, commit, push, publication, or deployment is included.

## Evidence boundary

Structural audit scores measure the checks implemented by the audit. They do
not certify plugin behavior, security, market demand, or Obsidian acceptance.
The synthetic fixtures do not prove real desktop or mobile execution. Paid
demand remains unknown until buyer research exists. Runtime acceptance of an
actual plugin belongs to its own project and test matrix.
