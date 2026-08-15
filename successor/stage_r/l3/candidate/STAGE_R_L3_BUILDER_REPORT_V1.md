# Stage-R L3 projection-only Builder report V1

Status: `CANDIDATE_READY_FOR_DRIVER_CODE_AUDIT`

Date: 2026-08-15

Builder: Claude Opus 5, bounded implementation role. No commit, no push.

## 1. Pins recomputed before work

Every pin below was recomputed from disk at the start of the session and matched.

| object | SHA-256 | result |
|---|---|---|
| `successor/stage_r/l3/STAGE_R_L3_PROJECTION_ONLY_EXECUTABLE_ANNEX_V1.md` | `a6848dd2a64b81783f59ef7aafcebe66bf1fb109aad2f2cb183f9d4d646829a0` | match |
| `successor/stage_r/l3/STAGE_R_L3_PROJECTION_ONLY_ANNEX_DRIVER_CLOSURE_V1.md` | `4d37b1fb648de442ebe484704b8e309d93c5b755aab04da4949f185401193811` | match |
| `successor/stage_r/PHILOSOPHIA_MINIMUM_CAUSAL_CONTRACT_R_V2_1.md` | `1c3cec3aa6bd7094e2d37b062a8f349df5b226e91bbdc4a7b21e80fb785172f3` | match |
| `successor/stage_r/STAGE_R_L3_PROJECTION_ONLY_ACTIVATION_V1.md` | `2539786a2b3954408a8fb98f0d8238636c0644900b56c74a2a6eec436da017b2` | match |
| accepted cumulative patch through L2 V5 | `3a570b2e35b15dc796d86cd8a997230c00bbf5aed3b5c06f3b14dca78b46b683` | match |
| L2 code-gate JSON | `8961b5a97ee0972d83a071e1b1c82869a9841f5f01c45add12a88dbfee1010f0` | match |
| exclusion ledger V3 | `a1f907ad6665b7c96d91496c5a91d32f0f0cae63da48b6b26da6b292d48f528d` | match |
| Stage-B charter v1.1.1 (`accepted_authority/`) | `703bf39cfe8f875f9be3781659a7365c1bc99c42f7523e43fef2c0a2c47b8311` | match |

- Annex commit `19e62a7eac6ca38a79da117ff86c1c8eba72516a`: exists (`git cat-file -t` = commit).
- MINIMO base commit `6066f482c6752915ad21119f93dc162f4cb9db72`: checked out in every fresh tree.
- Recovery manifest: `sha256sum -c SHA256SUMS` = **29/29 OK**, run before work and again at the end.

The archived unaccepted L3 draft was read for provenance only. No exact-plan identity,
V4 stage-6 seed, AC-1 choice or review schedule from it was restored.

## 2. Execution environment

- Execution directory: `mktemp -d` → `/tmp/tmp.qXkofdboYA` (disposable).
- `tree_a` — development tree: local clone of `/home/master/llm_projects/minimo`, no network,
  `git checkout 6066f482…`, then the accepted L2 V5 cumulative patch (`git apply --check` first).
  34 changed paths, matching the recovery verification record.
- After applying the accepted patch, all reconstructed L0–L2 sources were hash-verified against
  `SHA256SUMS` (11 files, all match), so the development base is the accepted Stage-B surface.
- Interpreter: the existing MINIMO virtualenv `/home/master/llm_projects/minimo/.venv/bin/python`.
  Nothing was installed, updated or removed.
- `route_a`, `route_b`, `route_c` — three further fresh clones used only for patch-route verification.

## 3. Delivered files

| path | SHA-256 | lines |
|---|---|---:|
| `learning/phase2_stageb_identity.py` | `1a04bed4366599bb3b542b6ae7bbc123dff9b56078c5552249dec31c875d0ffb` | 407 |
| `learning/test_phase2_stageb_identity.py` | `fd6948652bfa44ccdfd0da6ae1cd093312a6d09a0e4a7f6bbf430698427908c2` | 1294 |
| `STAGE_R_L3_CODE_GATE_EXCLUSIONS_V1.json` | `a64aaeb12176ab88755f9c8c08f26d9f9ee1df2af9147324373aacfdf43bd315` | 21612 bytes |
| `minimo_phase2_stageb_l3_projection_v1_delta.patch` | `9619264fc16c4222be190f350b9b873c1808358da3adc4f7897cc7c468c5e6d3` | 1713 |
| `minimo_phase2_stagea_stageb_l01_l2_l3_projection_v1_cumulative.patch` | `e44de3a37add3dcb71e6100a83f2eee9e6c42a50602bef95a237e2294b456c2e` | 12607 |
| `STAGE_R_L3_BUILDER_REPORT_V1.md` | this file | — |

The two `learning/` copies are byte-identical to the files verified in `route_a` and `route_b`.

## 4. Implementation summary (annex §§2–6)

Production exposes exactly the seven annex functions plus the closed `L3InvariantError`:
`canonical_theorem`, `theorem_identity`, `rule_skeleton`, `skeleton_identity`,
`public_projection`, `rederive_theorem`, `identify`.

- Imports are exactly `__future__`, `itertools.permutations`, `typing`,
  `phase2_stageb_canonical`, `phase2_stageb_render`, `phase2_stageb_schema`.
  The checker, generator, `json`, `hashlib`, `random`, `secrets`, filesystem and process
  APIs are absent; `SEQUENT_REDERIVATION_MISMATCH` is owned locally as a literal, so
  `phase2_stageb_causes` is not imported either.
- `identify` order is fixed: raw re-derivation → raw comparison → canonical theorem →
  identity/name → skeleton identity → public projection → success assembly.
- Raw theorem comparison happens **before** any canonicalization, on canonical bytes of
  each subobject, in the strict subcause order `THEOREM_KEYSET_MISMATCH`,
  `THEOREM_ATOMS_MISMATCH`, `THEOREM_HYPOTHESES_MISMATCH`, `THEOREM_GOAL_MISMATCH`.
- `canonical_theorem` enumerates **all** `k!` bijections via
  `itertools.permutations(range(k))` and takes the byte-lexicographic minimum candidate.
  There is no heuristic representative and no hypothesis matching search.
- Hypotheses are sorted by `canonical_bytes(formula)` only.
- `rule_skeleton` implements the annex table exactly: `ASSUME_GLOBAL`/`ASSUME_LOCAL` split
  retained; `AND_INTRO` children and the `OR_ELIM` branch pair sorted by canonical bytes;
  `OR_ELIM` major kept in first position; `NOT_ELIM` operand order kept; `AND_ELIM_*` and
  `OR_INTRO_*` direction erased; formulas, atoms, conclusions and identifiers erased.
- `public_projection` takes exactly one argument, accepts only a canonical theorem, and
  emits the five `PUBLIC_ITEM_KEYS` in the declared order, rendering the sequent solely
  through the accepted L0 `render_sequent`.
- Success and failure records carry the exact declared key tuples; failure records contain
  no identity field.
- All outputs are freshly constructed; no returned mutable object aliases an input or another
  returned position; inputs are byte-unchanged after every call.
- No retry, backtracking, random choice, `while`, `try`, `global`, filesystem access or
  mutable module global exists in production. Every module-level binding is a `str`, `int`,
  `tuple` or `frozenset`.

**One documented scoping decision.** Annex §7.1 says "verify every governing file hash
before fixture reconstruction". The gate verifies from disk every governing file it actually
consumes: the eight in-tree accepted L0–L2 sources plus the theory file, the V3 exclusion
ledger and the L2 code-gate JSON. The recovery-root location is resolved from
`PHILOSOPHIA_RECOVERY_DIR` with the pinned absolute default; a missing or mismatched file
fails the gate rather than skipping it. The contract, activation and charter hashes are
consumed as recorded documentary pins (they are not read by the gate and are asserted to be
well-formed 64-hex constants, and are embedded verbatim in the exclusion artifact).

## 5. Code gate coverage against annex §7

| annex duty | where | outcome |
|---|---|---|
| 1 governing hashes verified first | `GoverningPinsTest` (4 tests) | pass |
| 2 five L1 builders + only six frozen L2 rows; canonical result hashes; scan helper untouched | `FrozenFixtureTest` (5 tests) | pass |
| 3 L1 re-check and all eleven V3 raw hashes reverified before identity | `_build_fixtures`, `FrozenFixtureTest.test_v3_raw_hashes_reverified_before_identity` | pass |
| 4 exhaustive `k!` bijections, re-checked, three invariances | `AtomBijectionInvarianceTest` (2 tests) | pass, **1854** transformed plans |
| 5 global permutation, global-ID rewrite, local relabel, ≥2 theorem-changing mutations | `HypothesisAndIdentifierInvarianceTest` (4 tests) | pass |
| 6 four subcauses, precedence, exact keys, no identity on failure | `RawMismatchTest` (7 tests) | pass |
| 7 all skeleton erasures and retentions | `SkeletonErasureAndRetentionTest` (13 tests) | pass |
| 8 projection signature, keys, renderer, 64-hex name, sealed-field refusals, order stability | `PublicProjectionTest` (5 tests) | pass |
| 9 inputs unchanged, no alias with inputs or within output | `FreshnessAndAliasTest` (3 tests) | pass |
| 10 every `L3InvariantError` injected at its real boundary; no fixture raises | `InvariantErrorTest` (8 tests) | pass |
| 11 two fresh processes, different `PYTHONHASHSEED` | `FreshProcessDeterminismTest` (1 test) | pass |
| 12 artifact written twice to separate temp paths, byte-identical, full structure | `ExclusionArtifactTest` (3 tests) | pass |
| 13 `ast` import allowlist, forbidden calls, retries, filesystem, mutable globals | `ProductionSourceDisciplineTest` (7 tests) | pass |
| 14 ordinary discovery, existing 67 green, both patch routes, no foreign-worktree evidence | §6 below + `GoverningPinsTest.test_gate_runs_inside_the_tree_under_test` | pass |

Exhaustive permutation counts are the real `k!` per fixture and are asserted as a total:
`5 × 3! + 2 × 6! + 4! + 3 × 5! = 30 + 1440 + 24 + 360 = 1854`. No sampling was used.
Boundary injections use real internal call sites (`_bijections(7)`, a 26-deep `NOT` chain,
a 40-deep `EXFALSO` chain, malformed and out-of-range theorems, a non-canonical theorem
passed to `public_projection`), not mocked public records.

## 6. Verification commands and measured results

All commands were run from the reconstructed trees, never from the original checkouts.

1. **Recovery manifest**
   `sha256sum -c SHA256SUMS` → **29/29 OK** (run at start and at end).
2. **Byte compile**
   `python -m py_compile phase2_stageb_identity.py test_phase2_stageb_identity.py` → OK.
3. **Ordinary Stage-B discovery, development tree**
   `python -m unittest discover -s learning -t learning -p 'test_phase2_stageb*.py'`
   → **Ran 131 tests in 30.579s, OK**.
   Baseline before this work was 67; the new file contributes **64**; 67 + 64 = 131,
   and the pre-existing 67 all remain green.
4. **Route A** — fresh clone at pinned base → accepted L2 V5 cumulative → L3 delta
   → same discovery command → **Ran 131 tests in 30.653s, OK**.
5. **Route B** — fresh clone at pinned base → final cumulative patch directly
   → same discovery command → **Ran 131 tests in 30.748s, OK**.
6. **Route C** — fresh clone at pinned base → the *persisted candidate* cumulative patch
   → same discovery command → **Ran 131 tests in 30.650s, OK**.
   This proves the delivered patch file, not only the working tree, reproduces the result.

Every patch passed `git apply --check` before application.

**Route manifest equality.** Non-`.git` path/mode/content manifest SHA-256:

```text
route_a = f636ca26237c1509061ef04e7345e4318ca99df68ae96c3791f251a39d8acb4f
route_b = f636ca26237c1509061ef04e7345e4318ca99df68ae96c3791f251a39d8acb4f
```

Equal. Both trees contain 98 non-`.git` files and report 36 changed paths against the base.

**Path scope.**

- Delta: exactly two `diff --git` entries, both new files —
  `learning/phase2_stageb_identity.py`, `learning/test_phase2_stageb_identity.py`.
  No existing MINIMO file is touched.
- Cumulative: exactly 36 `diff --git` entries — the 34 already-accepted Stage-A/L0–L2 paths
  plus the two new L3 files.
- Neither patch contains any candidate-package path
  (`grep -c 'successor/stage_r\|candidate/learning'` = 0 in both). The word "candidate"
  appears only as a local variable name inside the added source lines.

**Timing.** Elapsed wall time per full discovery run: 30.6–30.8 s. The dominant cost is the
1854-plan exhaustive bijection sweep (~28.6 s), which the annex forbids reducing to a sample.

## 7. Required confirmations

- **Selector scan not called.** `select_l2_code_gate_rows` (the L2 test-module helper) is
  neither imported nor invoked. Its name does not occur in either delivered file — the gate
  asserts this by assembling the string from parts so its own bytes stay clean — and only the
  six literal `(key_hex, draw_index)` rows already frozen in the L2 code-gate JSON were
  regenerated. No key range was scanned, no key was minted or derived, and no row outside
  those six exists anywhere in the deliverables.
- **Original worktrees untouched and not used as evidence.** `/home/master/llm_projects/minimo`
  was recorded before and after work (`git status --porcelain`, `HEAD`, and SHA-256 of its two
  pre-existing modified files); the states are identical (`diff` clean), and
  `learning/phase2_stageb_identity.py` does not exist there. Its pre-existing dirty changes to
  `problems.py`/`proofsearch.py` were neither modified nor used as implementation evidence.
  All work happened in `mktemp -d` clones. The Philosophia worktree received only the six
  candidate-package files listed in §3.
- **Still unauthorized, and not performed.** No L4 compile or replay; no dev-root pipeline;
  no key, root or frame generation; no reservoir or held-out selection; no exact-plan identity;
  no stage-6 collision seed; no quota accounting; no Peano, MCTS, search or query-measurement
  execution; no learner or selector call; no training; no disposable or scientific execution;
  no Stage-H work; no commit; no push.

## 8. Limitations

- No failing test remains; the gate is green on all three routes.
- The gate reads two governing artifacts from the Philosophia recovery checkpoint at a
  resolvable path (`PHILOSOPHIA_RECOVERY_DIR`, pinned absolute default). This is deliberate:
  the annex requires governing-hash verification, and hash-checking a file requires reading it.
  A driver may relocate the checkpoint by setting that variable. This is the only external
  dependency of the new test file.
- `sort` on hypothesis canonical bytes assumes distinct global hypothesis formulas, which the
  accepted L1 checker already enforces; `public_projection` independently requires strict
  ordering and raises `CANONICAL_THEOREM_PRECONDITION_VIOLATED` otherwise.

## 9. Focused time

Focused working time used: approximately **1 hour 25 minutes** (session start 13:41:32+03:00,
deliverables complete 15:06:46+03:00), against the eight-hour §4.3 kill. The kill did not fire.

```text
L3_SCOPE=THEOREM_IDENTITY_PUBLIC_PROJECTION_RESERVOIR_LOCAL_SKELETON
EXACT_PLAN_IDENTITY_IMPLEMENTED=NO
STAGE6_SEED_IMPLEMENTED=NO
L4_AUTHORIZED=NO
ROOT_OR_FRAME_GENERATION_AUTHORIZED=NO
SCIENTIFIC_EXECUTION_AUTHORIZED=NO
NEW_MINIMO_FILES=2
EXISTING_MINIMO_FILES_CHANGED=0
STAGE_B_DISCOVERY_TESTS=131
NEW_L3_GATE_TESTS=64
PATCH_ROUTES_EQUAL=YES
COMMITTED_OR_PUSHED=NO
```

READY_FOR_STAGE_R_L3_DRIVER_CODE_AUDIT_V1
