# WoW source governance

This repository is the public metadata and verification layer for the
maintained AzerothCore/Playerbots source line. It records which repositories
are direct upstreams, which are owned forks, which exact revisions are
selected, and which components are removed, deferred, compiled-disabled, or
candidate-only.

It contains no server runtime, database contents, credentials, client assets,
release artifacts, or restricted module source. The source repositories keep
their own upstream licenses and publication boundaries.

## Use

```sh
python3 tools/verify_github_source_ownership.py --offline
python3 tools/verify_github_source_ownership.py
```

The live check requires an authenticated `gh` CLI. A passing source check only
proves GitHub ownership, parent-repository provenance, branch existence, and
exact revision pins. It does not prove build, SQL, startup, gameplay, load,
rollback, or release acceptance.

The maintained source line is `maintained/cpi217`. The Junk-to-Gold Plus
repository remains candidate-only on its separate candidate branch. Private or
restricted material is intentionally represented by disposition and license
metadata rather than published here.
