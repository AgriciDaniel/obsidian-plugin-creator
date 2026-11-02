# Release Checklist

## Product

- [ ] README states buyer, promise, outputs, boundaries, and quick start.
- [ ] `SKILL.md` maps commands accurately.
- [ ] License and distribution stance is explicit.
- [ ] Third-party notices are current.

## Research

- [ ] Maturity is documented and not overstated.
- [ ] `references/current-requirements.md` has dated official/primary sources.
- [ ] `references/public-sources.json` lists dated official/primary sources,
      refresh dates, source types, and supported claims.
- [ ] `references/source-map.md` explains import strategy and source schemas.
- [ ] `references/safety-gates.md` lists refusal rules and failure paths.
- [ ] Stale source claims were browsed and refreshed before release.

## Vault

- [ ] Template vault opens in Obsidian.
- [ ] Hot/Index/Wiki notes and hubs are connected.
- [ ] Private runtime sources stay immutable in separate working vaults; none are distributed.
- [ ] Deliverables cite source notes or raw-file hashes.
- [ ] `PUBLISHING_NOTICE.md` has been reviewed before public publish or ZIP release.

## Verification

- [ ] `python3 -m compileall scripts obsidian_plugin_brain tests`
- [ ] `python3 tests/test_pipeline.py`
- [ ] `python3 scripts/build_demo_vault.py`
- [ ] `python3 scripts/package_release.py --version 0.2.0`
- [ ] No secrets, private client data, or local absolute paths in artifacts.
- [ ] Market-ready release is blocked unless audit score is at least 90 with no critical failures.
- [ ] `references/adapter-manifest.json` names real schemas, importer paths,
      synthesis modules, report renderers, fixtures, and tests before
      domain-adapted or market-ready release.
