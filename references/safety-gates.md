# Safety Gates

V1 is read-only and advisory unless a future release explicitly adds approved,
reversible mutation.

## Refusal Rules

- No unsourced Obsidian API, submission policy, or version claims
- No guidance that violates official Obsidian Plugin Guidelines such as calling detachLeavesOfType in onunload or injecting unsanitized innerHTML
- No recommendation to bundle duplicate @codemirror/* or obsidian runtime modules into main.js
- No credentials, API keys, sync tokens, or private vault content in repo artifacts or sample fixtures
- No account, registry, or host-system mutation in V1
- No irreversible recommendation without owner, confidence, source, and rollback note

## Safety Risks

- Stale Obsidian API or submission review claims due to new desktop, mobile, or Bases releases
- DOM XSS vulnerabilities when rendering untrusted Markdown, frontmatter, JSONL traces, or external responses via innerHTML
- Mobile crashes on iOS and Android caused by unguarded Node.js or Electron imports when isDesktopOnly is false
- Sync traffic, conflicts, and storage constraints when large derived caches are stored with plugin settings
- Memory leaks, detached DOM trees, and background WebGL GPU drain when views close or hide without disposal
- Secret leakage when storing plaintext API keys inside git-tracked vault plugin data files

## Release-Blocking Gates

- Current trustworthy sources are missing.
- Raw source provenance is missing.
- Deliverables contain unsupported claims.
- Credentials or private client data are present.
- A mutation path exists without approval and rollback.
