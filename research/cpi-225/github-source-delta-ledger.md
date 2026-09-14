# GitHub source ownership ledger

Date: 2026-09-14

GitHub owner: `Akotz89` (verified with `gh auth status --hostname github.com`).
No pull requests, issues, deployments, realm restarts, database writes, or
client changes were made.

## Owned forks and exact source branches

Every branch below was created from the stated live cpi-217 base commit. The
branch commit is the reproducible pin for the source-only delta. The
Junk-to-Gold row is explicitly candidate-only because its source delta belongs
to the reviewed integration candidate, not the live release. Each isolated
clone has `origin` set to the `Akotz89` fork and `upstream` set to the named
parent.

| Component | Parent | Live base pin | Owned branch pin | License | Carried paths | Patch SHA-256 |
| --- | --- | --- | --- | --- | --- | --- |
| Core | `mod-playerbots/azerothcore-wotlk` | `9fb906bb7296212ff42fc95ff73a92aaf8554f0d` | `Akotz89/azerothcore-wotlk@463c3caf6f850e57de1c68f26da919b84216a234` | GPL-2.0 | 11 modified files under `src/` | `2195b275bb17f469b81e3f032bb9b5f39202b62b66d3fd18069a40086253e5f0` |
| Playerbots | `mod-playerbots/mod-playerbots` | `2f7d9f774987d0157c6a0d0cc08c40bec3db3945` | `Akotz89/mod-playerbots@b1163bc5ce4494176f03a1f4c97bceb21aed7c62` | GPL-2.0 | 20 modified files under `src/` | `64fde8c02dca2e2165512be6cb4fe56fdfa3a8e268a177873a1a13ac6b25d72b` |
| Python engine | `privatecore/mod-python-engine` | `700a4f75a2e550f17022665d7b5b009c24e46a40` | `Akotz89/mod-python-engine@c167c2c1d7578befca13a40ae119b0f513a48b95` | AGPL-3.0 | 9 modified files under `src/` | `4b0ae8e4667bc634ed11d7360191b5e0024c3fb6abd03d1e783c6c433c4a27bc` |
| AutoFish | `Flerp/mod-autofish` | `0f92215776017754355e1b5cfeec77cefc98b40b` | `Akotz89/mod-autofish@7a6dca219a3edf41420ee78d2565b80bed4ddcd5` | MIT | `src/mod_autofish.cpp` | `7827aeebc00d562764af56669b74621a548e78ca5facd66f301f3aa6a9938d28` |
| AutoLoot | `Grim-Batol/mod-autoloot` | `a4b855d61620f84004ef9d92cec728e63e9e3750` | `Akotz89/mod-autoloot@5edaa2bfe6caff8025d9de650fef1df0af411cce` | GPL-3.0 | `src/ALPlayer.cpp` | `f69ed3354b9ab3ca4d6fc5e5826d645a02b6480e47bcdaf9cfa0cd010ad6d656` |
| Game State API | `abutbul/mod-game-state-api` | `ca8a6c84a5fedd460a2011039d90dc4f573e30fd` | `Akotz89/mod-game-state-api@13740b317beb2a53100730fb6666412a1041183f` | AGPL-3.0 | `CMakeLists.txt` and 4 files under `src/` | `1ee855646fbdf3f261e81f41fc22a62bad2611af5eff2be287f1d6048d0f859a` |
| Progression System | `azerothcore/mod-progression-system` | `84a25e6df8497d83432e61aa38557a92c156e77d` | `Akotz89/mod-progression-system@abab641b4399102191d8ab1c07a2a1e4fc5070fc` | AGPL-3.0 | module `src/` plus its world migration SQL; no manual SQL | `2c8f9678c823f4bc341c4bf3ae0f72731813b446999df49e3cab3a44bd950dc0` |
| Reagent Bank | `ZhengPeiRu21/mod-reagent-bank` | `62c265338ceba10fb754394413e6c4c61cedf9de` | `Akotz89/mod-reagent-bank@d0bb184666209cebc0317b33765f91302b5b2b2b` | MIT | `src/ReagentBank.cpp`, `src/ReagentBank.h` | `3bcc9e0f2dce165d0981411e61dbeda8062a9836a30b73067d92e785eb5be9ee` |
| Rotation | `Maddnes95/mod-rotation` | `4166858e8f3fc9666700b64e6d36fa7b06490d24` | `Akotz89/mod-rotation@098a2ac44228cbf7baa07e818b2bcafdaccf3027` | GPL-2.0 | `src/Rotation.cpp`, `src/Rotation.h` | `325fa36feaad84ff27edf16b3666ed034420904edecafb8ee4d8af33b39ab01a` |
| Weather Vibe | `hermensbas/mod_weather_vibe` | `cb854eb96ef9fa7fa4fd1f6e2d3340fcadb945e8` | `Akotz89/mod_weather_vibe@cee081c0e743d46b55bd6c34b19c44b6a1bc1609` | AGPL-3.0 | `src/core/mod_wv_core.cpp`, `src/engine/mod_wv_engine.cpp` | `1f7fb8f795e7082e464e0f440de346209178c095914209a02c5b856b8465f7ac` |
| Junk to Gold Plus (candidate-only) | `eveletspb/mod-junk-to-gold-plus` | `f5a6acb334de3b6b19902a984eaaed89a32e8570` | `Akotz89/mod-junk-to-gold-plus@1cd2cc9ab0b1dda54813392eadc0305d8cca1c42` | AGPL-3.0 | `src/mod_junk_to_gold_plus.cpp` | `5763a189c326ee086841beea07e81eceb5a94e513c6e15ee4fc3b71be9455139` |

The branch name for all maintained rows is `maintained/cpi217`. The explicitly
candidate-only Junk-to-Gold row remains on
`codex/candidate-cpi225-junk-to-gold-party-white-20260913`. Local verification
clones are retained in the task work area for source-only checks; the public
governance repository publishes metadata and hashes, not local filesystem
paths. All eleven clones were clean after push.

## Python controller ownership

`Akotz89/wow-population-controller` is a private, non-fork repository. Its
`main` pin is `4db9f9e068b93e011a0725abbcedda12e71fb8a4`, containing the 17
source-only Python files that match the live v30 release. The corresponding
native boundary is the owned Python-engine fork at
`700a4f75a2e550f17022665d7b5b009c24e46a40` plus its source-only branch above.

The controller snapshot intentionally excludes the release-only
`scripts/login.py`, `__pycache__` bytecode, population snapshots, credentials,
database data, server configs, and release artifacts. `python3 -m compileall`
passes against the snapshot. The live release's same 17 files were hash-equal
to the snapshot before publication.

## Deliberately excluded

- `mod-ah-bot-plus`, `mod-multibot-bridge`, and `mod-playerbot-dungeon-sim`
  have no current GitHub license endpoint result; they were not forked or
  published.
- `mod-dungeon-clear` returned GitHub `NOASSERTION` for its license despite an
  older local classification; it was not forked pending a current license
  decision.
- `mod-fly-anywhere` has only a candidate `data/patch/client/Patch-O.mpq`
  delta; client assets are out of scope.
- `mod-improved-bank` has a source delta only in the active integration
  candidate, so it remains with that writer until review completes.
- `mod-playerbots`/`mod-python-engine` candidate commits from the integration
  checkout, including `ff5fd16...` and `c268e72...`, are not published. The
  owned branches above contain the live cpi-217 line, not the unaccepted
  candidate.
- `eveletspb/mod-junk-to-gold-plus` is licensed AGPL-3.0. Its exact upstream
  base is `f5a6acb334de3b6b19902a984eaaed89a32e8570`; the reviewed on-loot
  common-gear delta is owned separately at
  `Akotz89/mod-junk-to-gold-plus@1cd2cc9ab0b1dda54813392eadc0305d8cca1c42`
  on the candidate-only branch above and is not a live-release claim.

The primary canonical manifest now carries `maintained/cpi217` for owned
source-line rows. The public governance repository publishes this ledger with
the manifest, maintenance policy, and verifier. This remains source-only
ownership evidence; it is not build, runtime, gameplay, rollback, or release
acceptance.
