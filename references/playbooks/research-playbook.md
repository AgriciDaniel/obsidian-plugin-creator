# Obsidian Plugin Brain: Research Playbook


> Use this playbook when running the **research-scout** role packet. It moves a brain
> from `scaffolded` to `researched` by filling the source pack and locking
> dated, official/primary sources.

## When to invoke

- The brain is at maturity `scaffolded` or has stale `refresh_due` entries.
- A high-stakes (accounting, tax, legal, medical, finance, compliance, security) or
  fast-moving (ads, platforms, APIs, social, AI) domain is in scope.
- `brainstein research-audit` reports placeholder content in `references/`.

## Prerequisites

- `specs/<slug>.yaml` exists and validates with `brainstein validate`.
- `references/research-plan.md` exists (written by `brainstein research-plan`).
- Operator has read access to the source materials enumerated in the spec's
  `raw_sources` and `enrichment_sources`.

## Step-by-step

1. Open `references/research-plan.md` and confirm the buyer questions and
   official-source checklist for this domain.
2. For each official/primary source, capture: URL, retrieval date, version,
   confidence, and 2-3 claims. Write to `references/public-sources.json`.
3. Update `references/current-requirements.md` with dated bullets pointing to
   source-ledger entries.
4. Update `references/market-research.md` with practitioner / market signals.
5. Run `brainstein research-audit <repo>` and resolve every critical failure.
6. Update `wiki/activity.md` with the date and the list of new sources.

## Outputs

- `references/public-sources.json` with ≥2 official sources (high-stakes/fast-moving)
  or ≥1 (stable domain), each with `retrieved`, `refresh_due`, `source_type`, and
  `claims`.
- `references/current-requirements.md` with no placeholders.
- `wiki/sources/*` notes (one per source) with frontmatter and wikilinks.

## Quality gates

- [[Quality Gate Matrix|Quality Gate Matrix]] entry: **Research Gate**.
- All dated claims cite a source-ledger entry.
- No URL points to `example.com`, `localhost`, or similar placeholder hosts.

## Failure modes

- **Source paywalled or unavailable**: capture archive.org snapshot, mark
  `confidence: low`, and add a refresh task in orchestration.
- **Contradictory official sources**: split into `claims` array with both;
  add a [[risks/_index|risk]] note.
- **Stale `refresh_due`**: a future-dated `refresh_due` ≤ today triggers
  research-audit failure. Refresh or remove.

## Sources

- [[No Source No Claim|No Source No Claim doctrine]]
- [[researching-a-domain|Researching a domain playbook]]
- Safety risks driving stricter sourcing: Stale Obsidian API or submission review claims due to new desktop, mobile, or Bases releases, DOM XSS vulnerabilities when rendering untrusted Markdown, frontmatter, JSONL traces, or external responses via innerHTML, Mobile crashes on iOS and Android caused by unguarded Node.js or Electron imports when isDesktopOnly is false.
