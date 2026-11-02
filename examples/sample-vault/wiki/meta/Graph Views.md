---
type: "meta"
title: "Graph Views"
domain: "Obsidian plugin engineering"
status: "evergreen"
created: "2026-11-01"
updated: "2026-11-01"
confidence: "practitioner"
tags:
  - "domain/architecting-building-styling-optimizing-testing-auditing-and-sh"
  - "type/meta"
  - "confidence/practitioner"
related:
  - "[[Start Here]]"
  - "[[Tag Taxonomy]]"
  - "[[Plugin Creator Studio]]"
  - "[[Index]]"
source_urls:
  - "https://help.obsidian.md/plugins/graph"
  - "https://help.obsidian.md/plugins/search"
  - "https://help.obsidian.md/plugins/bookmarks"
---

# Graph Views

Explore the Plugin Creator brain by note type. The local graph configuration uses
an Obsidian-inspired palette with quiet links and distinct category colors.
These are navigation preferences, not confidence or completion ratings.

## Activate the public graph defaults

From the complete source checkout, create a new working vault:

```bash
python3 -m obsidian_plugin_brain new my-plugin-brain --owner "Your name" --out-dir ../my-plugin-vaults
```

Open `../my-plugin-vaults/my-plugin-brain/` as the vault. It receives the reviewed
palette, graph bookmarks, and graph CSS locally. The checked-in template and sample
are public knowledge snapshots without `.obsidian/` state; opening them directly
lets you read the notes but does not activate the graph defaults. Keep working
vaults outside the public source checkout.

## Choose a view

Open **Bookmarks** in Obsidian and expand **Plugin Creator graph views**. Select:

- **The whole brain** for all curated wiki notes.
- **Creator playbooks** for notes with Plugin in their filename.
- **Concepts and architecture** for concept notes.
- **Source notes** for the research references.
- **Decisions and outputs** for decisions, deliverables, and reports.
- **Questions and experiments** for unresolved work and investigations.
- **Show tag connections** for the same overview with tag nodes visible.

The saved views keep the same palette. The default overview hides attachments,
unresolved link targets, and tag nodes, while retaining existing notes without
links. References and source captures outside `wiki/` stay outside this view.

## Color key

| Category | Color | Existing tags |
| --- | --- | --- |
| Navigation | `#A882FF` | `#type/meta`, `#type/hot`, `#type/index`, `#type/overview`, `#type/log`, `#type/hub`, `#type/dashboard` |
| Workflows | `#65D6B4` | `#type/flow` |
| Concepts | `#7DB7F1` | `#type/concept` |
| Sources | `#B49BDD` | `#type/source` |
| Decisions | `#E8BB74` | `#type/decision` |
| Deliverables and reports | `#E6A0C4` | `#type/deliverable`, `#type/report` |
| Entities and platforms | `#91A5D8` | `#type/account`, `#type/platform`, `#type/entity` |
| Questions and gaps | `#ED9690` | `#type/question`, `#type/gap` |
| Experiments | `#BACC8C` | `#type/experiment` |

The muted `#938A9F` domain group is a final fallback. Specific note types appear
first so the shared domain tag cannot give every note the same color. Notes keep
their existing tags; no new type or confidence classification is inferred.

## Filter it yourself

In the graph settings, use **Search files**. Copy one of these queries:

```text
path:"wiki/"
path:"wiki/" tag:#type/source
path:"wiki/" tag:#type/concept
path:"wiki/" tag:#type/flow
path:"wiki/" file:"Plugin"
path:"wiki/" (tag:#type/question OR tag:#type/gap OR tag:#type/experiment)
```

Turn **Tags** on when you want to inspect the tag connections. A saved view opens
with its own filter; the underlying notes and links remain intact.

These settings belong to the vault folder containing this note, not a surrounding
repository or another vault. Existing graph tabs may retain their prior options;
close and reopen the graph or choose one of the saved views to load these settings.

## Sources

Obsidian help for [Graph view](https://help.obsidian.md/plugins/graph),
[Search](https://help.obsidian.md/plugins/search), and
[Bookmarks](https://help.obsidian.md/plugins/bookmarks), checked 2 November 2026.
The serialized graph bookmark structure was also inspected in the installed
Obsidian 1.15.0 application. Native visual appearance still requires a check in
Obsidian on the opened vault.

## Related

- [[Start Here]]
- [[Tag Taxonomy]]
- [[Plugin Creator Studio]]
- [[Index]]
