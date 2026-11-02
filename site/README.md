# Obsidian Plugin Brain Site

`site/` is the sanitized [Quartz](https://quartz.jzhao.xyz/) publish surface for the public subset of a vault.

Do not publish `.raw/`, source captures, internal ledgers, credentials, local paths, or private client data. Review `PUBLISHING_NOTICE.md` first.

Public exclusions: .raw, .obsidian, _templates, home.md, activity.md, references/public-sources.json, references/public-sources.json.

Quartz is a git repository, not an npm package, and needs Node 22 or later. The scripts use a POSIX shell. From the repository root:

```bash
npm --prefix site run setup                                          # clones Quartz v4.5.2 into site/.quartz
QUARTZ_CONTENT="$PWD/examples/sample-vault" npm --prefix site run build    # any vault root works
```

`build` copies `quartz.config.ts` into the Quartz checkout, renders the vault into `site/public/`, then runs `scripts/sanitize-public.mjs`, which removes excluded pages and rewrites private paths. Publish only `site/public/`.
