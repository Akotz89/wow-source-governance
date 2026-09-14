# GitHub source maintenance

This is the source-ownership layer for CPI-225. It is deliberately separate
from build, SQL, runtime, gameplay, rollback, and release acceptance.

## Source of truth

- Inventory and disposition: [`canonical-module-manifest.csv`](canonical-module-manifest.csv)
- Live GitHub check: `python3 tools/verify_github_source_ownership.py`
- Offline manifest check: `python3 tools/verify_github_source_ownership.py --offline`

The manifest records the upstream repository, selected fork, branch, exact
revision, license scope, local-delta owner, disposition, and remaining gate.
No module becomes release authority merely because a directory or GitHub
repository exists.

## Current GitHub layout

- The ten maintained source-line repositories use the stable
  `maintained/cpi217` branch and that branch is the default branch on GitHub.
- `mod-junk-to-gold-plus` remains candidate-only on
  `codex/candidate-cpi225-junk-to-gold-party-white-20260913`; it was not
  promoted to the maintained line.
- `wow-population-controller` remains a private repository and contains only
  source-only Python; credentials, database data, server configuration,
  release artifacts, and login automation are excluded.
- Direct-upstream and private-home-use components remain represented in the
  manifest without being copied into a public fork; a source fork for a
  removed, deferred, or compiled-disabled component does not change that
  release disposition.

## Maintenance rule

1. Read the manifest disposition and license scope before touching a fork.
2. Keep `origin` on the owned GitHub repository and `upstream` on the parent.
3. Fetch upstream read-only, review the exact divergence, and create named
   commits for accepted local deltas. Do not force-push or merge donor history
   wholesale.
4. Run the offline and live verifier, then update the manifest revision and
   evidence fields in the same source-only change.
5. Run build, ABI, SQL, startup, gameplay, load, rollback, and promotion gates
   separately before calling a source pin a release pin.

Never publish credentials, database contents, server configuration, client
assets, release artifacts, or code whose license only permits private-home use.
