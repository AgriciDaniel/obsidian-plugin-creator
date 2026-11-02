# Obsidian Plugin Creator

Use this brain to design and build a specific plugin through a clear brief,
appropriate architecture, implementation, actual acceptance checks, and a
maintainable release. Open `assets/template-brain/` in Obsidian and begin with
**Plugin Creator Studio**.

## Choose the starting surface

| Archetype | Starting example | Use when |
|---|---|---|
| command | Show Markdown note count | A quick action completes the task |
| dashboard | Independent workspace views | The user needs a persistent workspace |
| bases | A bounded list of matching files | The task is a view of a Bases query |
| editor | TODO decorations | The feature belongs to Source/Live Preview editing |
| markdown | A refreshable count code block | A note should contain a Reading view widget |
| canvas | A responsive 2D snapshot chart | A custom 2D display is appropriate |
| webgl | An on-demand Three.js scene | The product has a justified 3D interaction need |
| vault-index | Cached heading summaries | The task depends on vault/metadata services |

These are small examples with source-backed API choices. The brief's actual
features still need implementation. The technical concepts cover further UI,
framework, rendering, storage, secret, integration, platform, and release choices.

## Generate a source artifact

Copy `references/creator/example-brief.json` into your project planning area and
fill its ID, name, author, purpose, archetype, platform intent, and acceptance
criteria. Use the full product and design templates for the remaining decisions.

From the complete source checkout:

```bash
python3 -m obsidian_plugin_brain starters
python3 -m obsidian_plugin_brain create-plugin --brief references/creator/example-brief.json --out created-projects/heading-compass --dry-run
python3 -m obsidian_plugin_brain create-plugin --brief references/creator/example-brief.json --out created-projects/heading-compass
```

Use `--workspace /path/to/source-workspace` when selecting another existing
workspace. Output paths are bounded below it and must not exist. Choose a source
workspace outside active vaults, including vaults with custom configuration.
The creator refuses known vault markers and records a hash receipt.

## Implement and verify

Read the generated instructions, product brief, architecture, source list, and
acceptance record. In the generated directory, with Node.js 24:

```bash
npm ci --ignore-scripts --no-audit --no-fund
npm run check
npm run build
npm run lint
```

The creator itself performs none of those commands. Their execution is an
explicit local development step. The exact lock pins Obsidian, CodeMirror,
TypeScript, esbuild, Three.js, and the lint toolchain. The Obsidian lint package's
older Obsidian peer is overridden explicitly and the exact resulting tree is
tested. Upstream lint dependencies still include ESLint 9 beneath the ESLint 10
runner; reevaluate that dependency on refresh.

Complete one product criterion at a time, including its error/empty state and
cleanup. Retain meaningful domain tests. Inspect the compiled bundle and run the
read-only scanner on the actual project as a preliminary review.

Use a separately selected disposable development vault for actual Obsidian work.
Do not copy into an active vault as part of generation. Record desktop, rendering,
accessibility, performance, physical-device, and release outcomes separately.

## What to provide for a future plugin

The useful inputs are the target user and task, a representative example,
desired UI surface, platform targets, vault size, input/output format, persistence
and note-write needs, external services and secrets, performance expectations,
release channel, and observable acceptance criteria. Missing details remain
explicit unknowns until a decision is needed.

A useful starting request is:

> Use Obsidian Plugin Creator to build [idea] in [source workspace]. Start with
> the product brief, choose the smallest suitable surface, implement a complete
> first slice, and retain build and actual-runtime evidence separately.

Generation does not authorize active-vault installation, note changes, paid
provider calls, commits, pushes, publication, or directory submission.
