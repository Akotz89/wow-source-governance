# WoW source governance

This repository is the public metadata and verification layer for the
maintained AzerothCore/Playerbots source line. It records which repositories
are direct upstreams, which are owned forks, which exact revisions are
selected, and which components are removed, deferred, compiled-disabled, or
candidate-only.

It contains no server runtime, database contents, credentials, client assets,
release artifacts, or restricted module source. The source repositories keep
their own upstream licenses and publication boundaries.

The exact source-only commit pins, parent bases, carried paths, and patch
hashes are recorded in [`github-source-delta-ledger.md`](research/cpi-225/github-source-delta-ledger.md).

## Use

```sh
python3 tools/verify_github_source_ownership.py --offline
python3 tools/verify_github_source_ownership.py
```

The live check requires an authenticated `gh` CLI. A passing source check only
proves GitHub ownership, parent-repository provenance, branch existence, and
exact revision pins. It does not prove build, SQL, startup, gameplay, load,
rollback, or release acceptance.

The maintained source line is `maintained/cpi217` across ten public source
repositories, including the paired AzerothCore fork recorded in the
Playerbots dependency. The Junk-to-Gold Plus repository remains candidate-only
on its separate candidate branch. Private or restricted material is
intentionally represented by disposition and license metadata rather than
published here.

## CodeGraph source checkouts

The following public repositories and revisions were present in the source graph
on 2026-10-31. They describe source navigation, not a compatible build or
release selection. Revisions are pinned so a checkout can be reproduced.

| Directory | Origin | Branch containing revision | Revision |
| --- | --- | --- | --- |
| `SahtoutCMS` | https://github.com/Akotz89/SahtoutCMS.git | `main` | `2017b388742fde2468ab2543636d46feb641c906` |
| `azerothcore-wotlk` | https://github.com/Akotz89/azerothcore-wotlk.git | `codex/p10-maintained` | `a61d82512553a9d4bf645f72063700d265421225` |
| `mod-TimeIsTime` | https://github.com/Akotz89/mod-TimeIsTime.git | `master` | `f35fea456be56b38f56636ec6328ce15c5867bd9` |
| `mod-ah-bot-plus` | https://github.com/Akotz89/mod-ah-bot-plus.git | `master` | `f685832994c825f90aa5a3dc0e1620aa568e875b` |
| `mod-autofish` | https://github.com/Akotz89/mod-autofish.git | `codex/core-module-repairs-20261011` | `cf5385a6a50571338bdec11958ccd327baef3cc7` |
| `mod-autoloot` | https://github.com/Akotz89/mod-autoloot.git | `codex/cpi225-accepted-source-f476-20261021` | `a82ce5b1fb5d7fb5969b58a3d59c673686c095ca` |
| `mod-dungeon-clear` | https://github.com/Akotz89/mod-dungeon-clear.git | `auto-playerbots` | `3d0926cb8e099ba60d4efc5bbcb84ae53f8d7428` |
| `mod-game-state-api` | https://github.com/Akotz89/mod-game-state-api.git | `maintained/cpi217` | `726a1de66f6149204cfd04f25fd93a41d8081227` |
| `mod-guildhouse` | https://github.com/Akotz89/mod-guildhouse.git | `master` | `0b3cc14e947a859f8a7751a10676107d6316275b` |
| `mod-instance-reset` | https://github.com/Akotz89/mod-instance-reset.git | `master` | `58c96398826af3a5e0e8e03b68c895ffa868aaac` |
| `mod-junk-to-gold-plus` | https://github.com/Akotz89/mod-junk-to-gold-plus.git | `codex/cpi225-accepted-source-f476-20261021` | `70c83cd118706d4c8898dea3f74c602eabe8e783` |
| `mod-morphsummon` | https://github.com/Akotz89/mod-morphsummon.git | `master` | `bfcdc52c04a76402635e0a2b6a566cebbd8068f1` |
| `mod-multibot-bridge` | https://github.com/Akotz89/mod-multibot-bridge.git | `main` | `13a476c8ba4a053a6636ce2bdd433e87598a7b01` |
| `mod-mythic-plus` | https://github.com/Akotz89/mod-mythic-plus.git | `master` | `bf7cdc536f161a892d17080a3b13b3a892648623` |
| `mod-playerbot-dungeon-sim` | https://github.com/Akotz89/mod-playerbot-dungeon-sim.git | `main` | `78a3da102bc503075943f1126d84541942df2a64` |
| `mod-playerbots` | https://github.com/Akotz89/mod-playerbots.git | `codex/p10-maintained` | `fb099724db7d226a1c99e55759a6dfab38ec14f3` |
| `mod-progression-system` | https://github.com/Akotz89/mod-progression-system.git | `codex/cpi225-accepted-source-f476-20261021` | `64edc08bfd0c7e77374324a47690f2e38c21a8ab` |
| `mod-python-engine` | https://github.com/Akotz89/mod-python-engine.git | `maintained/cpi217` | `c167c2c1d7578befca13a40ae119b0f513a48b95` |
| `mod-quest-loot-party` | https://github.com/Akotz89/mod-quest-loot-party.git | `master` | `c3955915c76d5a22a9d25a44482345d368a8de82` |
| `mod-rdf-expansion` | https://github.com/Akotz89/mod-rdf-expansion.git | `master` | `c7a91c5973cda4529495b52b89375913f98726d6` |
| `mod-rotation` | https://github.com/Akotz89/mod-rotation.git | `maintained/cpi217` | `c2b8fb766d3b8c67552835d78577baaa674c77ac` |
| `mod-talentbutton` | https://github.com/Akotz89/mod-talentbutton.git | `master` | `c5f0c46d2a986e06bd3701798982f6b40d43c029` |
| `mod-transmog` | https://github.com/Akotz89/mod-transmog.git | `master` | `85b035a9b512d43feec19a8e120f10d71a0850b0` |
| `mod-warlock-pet-rename` | https://github.com/Akotz89/mod-warlock-pet-rename.git | `main` | `4826c9b1948ac62f52827b2f79cda42864075bf1` |
| `mod-weather-vibe` | https://github.com/Akotz89/mod_weather_vibe.git | `maintained/cpi217` | `362a134c6b129aa160ef959c1e20aef8121c52f3` |
| `wow-population-controller` | https://github.com/Akotz89/wow-population-controller.git | `main` | `19e66ebfa18f88a7f5918cfc77131ac05ae5158b` |

Clone each origin into its listed directory, then check out the listed revision.
The separate operations graph also uses this governance repository. Local
CodeGraph workspace configuration and graph data are not included in these
repositories; configure workspace roots for the intended checkout and review
exclusions before indexing.
