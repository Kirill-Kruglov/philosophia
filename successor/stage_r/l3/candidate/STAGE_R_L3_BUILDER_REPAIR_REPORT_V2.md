# Stage-R L3 projection-only Builder repair report V2

Status: `CANDIDATE_READY_FOR_DRIVER_REAUDIT`

Date: 2026-08-15

Builder: Claude Opus 5, same bounded implementation role. One bounded repair pass
against the two driver findings. No annex edit, no redesign, no new file, no commit, no push.

## 1. Pins recomputed before editing

| object | SHA-256 | result |
|---|---|---|
| executable annex | `a6848dd2a64b81783f59ef7aafcebe66bf1fb109aad2f2cb183f9d4d646829a0` | match |
| driver audit V1 | `1375d71b7dd1a52c6e2915d95e878fcf2df99682c2fd3b3b06b3b503551fc374` | match |
| V1 production | `1a04bed4366599bb3b542b6ae7bbc123dff9b56078c5552249dec31c875d0ffb` | match |
| V1 test | `fd6948652bfa44ccdfd0da6ae1cd093312a6d09a0e4a7f6bbf430698427908c2` | match |
| frozen exclusion JSON | `a64aaeb12176ab88755f9c8c08f26d9f9ee1df2af9147324373aacfdf43bd315` | match |
| V1 Builder report | `701af4e4cf7f0706ad51bdf580f89075960d658bebb2036cd5d3ec9a3c670eec` | match |
| recovery manifest `sha256sum -c SHA256SUMS` | — | **29/29 OK** (start and end) |

Work happened in a fresh `mktemp -d` tree (`/tmp/tmp.pV3QNqMI5p`): local clone of MINIMO,
`git checkout 6066f482c6752915ad21119f93dc162f4cb9db72`, accepted L2 V5 cumulative patch,
then the V1 candidate files copied in and verified at their V1 hashes before editing.

## 2. Outputs

| path | V1 SHA-256 | V2 SHA-256 |
|---|---|---|
| `learning/phase2_stageb_identity.py` | `1a04bed4…0ffb` | `ee1be7afef332d8ce87b37c885760dfddcdcb911525cc377aec940b02ac07860` |
| `learning/test_phase2_stageb_identity.py` | `fd694865…08c2` | `2d71a629acb8dfa5bd8d42eef57b87746e9e6df28a80b514e950515e506dd45e` |
| `minimo_phase2_stageb_l3_projection_v1_delta.patch` | `9619264f…e6d3` | `4f4b692a0ae8f3e989a6e353618cab19d20becc05d7dfe2007f6d58e7f354b71` |
| `…_l3_projection_v1_cumulative.patch` | `e44de3a3…6c2e` | `6194d40cecb7b5b70825ef3d4122a215a9706fa17b449b45126dc63070e6d14c` |
| `STAGE_R_L3_CODE_GATE_EXCLUSIONS_V1.json` | `a64aaeb1…d315` | **`a64aaeb12176ab88755f9c8c08f26d9f9ee1df2af9147324373aacfdf43bd315` — unchanged** |
| `STAGE_R_L3_BUILDER_REPORT_V1.md` | `701af4e4…0eec` | preserved, unmodified |

Line counts: production 407 → **413**; test 1294 → **1679**. Both files remain pure ASCII.

## 3. Repair 1 — real canonical-theorem precondition

**Production.** `public_projection` retains every V1 structural check (exact three-key shape,
canonical atom spelling and order, cardinality 3..6, strictly sorted hypotheses, well-formed
formulas, no undeclared occurrence) and then adds one check before hashing or rendering:

```python
if canonical_bytes(canon_theorem) != canonical_bytes(
        canonical_theorem(canon_theorem)):
    _raise(code)
```

Six added lines including the comment. The precondition is on the **full renaming orbit**, not
on atom spelling or hypothesis sorting. There is no normalization on the caller's behalf and no
second public output: a non-minimal input is refused with
`L3InvariantError('CANONICAL_THEOREM_PRECONDITION_VIOLATED')`, never silently repaired.

**Gate.** New class `CanonicalPreconditionTest` (7 tests):

1. `canonical_three_atom_theorem` is replaced by a hard-coded theorem
   (`atoms a0,a1,a2`; hypotheses `AND(a0,a1)`, `OR(a1,a2)`; goal `AND(a0,a1)`) and its
   minimality is **asserted, not assumed** — against `orbit_minimum_bytes`, an independent
   full-orbit sweep written in the gate without calling production, and then against
   `canonical_theorem`.
2. The driver counterexample is preserved verbatim as `driver_counterexample_theorem`
   (same object, goal `AND(a2,a0)`), with explicit assertions that it passes every V1
   structural check — canonical atom names, strictly sorted distinct hypotheses.
3. Its canonical bytes are proved to differ from both `orbit_minimum_bytes` and
   `canonical_theorem(...)`, and the **real unmodified** `public_projection` is proved to
   refuse it with the exact invariant code.
4. `test_two_names_for_one_class_is_no_longer_reachable` sweeps all six bijections of the
   counterexample's orbit and proves the accepted public names collapse to exactly one.
5. `test_precondition_is_not_weakened_to_spelling_or_sorting` parses production with `ast`
   and requires `public_projection` to call `canonical_theorem`.
6. `test_all_eleven_fixture_outputs_are_unchanged_from_v1` pins the V1 theorem identity,
   theorem name, public-projection hash and skeleton identity of all eleven fixtures as an
   in-gate constant map and asserts byte equality.
7. `test_every_fixture_canonical_theorem_survives_its_own_projection` proves each fixture's
   canonical theorem equals its independent orbit minimum and is idempotent under
   re-canonicalisation.

**Standalone reproduction of the former counterexample**, run outside the gate:

```text
V1 production: public_projection(bad) accepted
               -> t_48a7c724c863a635a65360d28981db16fcdc9c63b1771f8124d292177e5c874d
V2 production: public_projection(bad) raises CANONICAL_THEOREM_PRECONDITION_VIOLATED
               public_projection(canonical_theorem(bad))
               -> t_c77e2e5f73a745ae9792e68688fc1eeda6b45678d82bb79fd3c221c84f1ca558
```

Both names match the driver audit's reported values exactly. The two-name defect is closed.

## 4. Repair 2 — gate seams

### 2a. Authority binding before fixture reconstruction

Added one configurable project-root resolver, `PHILOSOPHIA_PROJECT_ROOT`, default
`/home/master/llm_projects/philosophia`. The existing `PHILOSOPHIA_RECOVERY_DIR` override is
kept and, when unset, the recovery root is derived from the project root.

`verify_authority()` hash-checks **17** governing files from disk and is called as the first
statement of `_load_governing`, so nothing can populate `_FIXTURE_CACHE` before it passes:

- project root: Stage-R contract, L3 activation, executable L3 annex, annex driver closure;
- recovery root: accepted Stage-B charter (`accepted_authority/`), accepted L2 annex,
  accepted cumulative patch through L2 V5, V3 ledger, L2 code-gate JSON;
- in-tree: the eight accepted L0–L2 sources plus the theory file, now including
  `test_phase2_stageb_generator.py` at `01adece50de5dc4cece3acfed80b21725ca7400e5d375204d5010eaae0dca4e8`.

A missing file raises `governing file missing: <label>`; differing bytes raise a mismatch
naming expected and actual. Both fail closed. The hex-syntax-only documentary test is deleted
and replaced by:

- `test_every_governing_file_is_hash_checked_from_disk` — all 17 bindings read and compared;
- `test_contract_activation_annex_and_charter_are_bound` — the eight newly required labels
  asserted individually;
- `test_authority_verification_fails_closed` — repoints the project root at an empty
  directory and requires `verify_authority()` to raise, then restores the environment;
- `test_authority_is_bound_before_fixtures_exist` — parses the gate with `ast` and asserts
  `verify_authority()` is literally the first statement of `_load_governing`, and that
  `_build_fixtures` calls `_load_governing`. In-tree pins are verified from that same
  pre-fixture path, not from a test whose alphabetical position might run later.

The constants embedded in the exclusion JSON are unchanged, so the artifact bytes cannot move.

### 2b. Every sealed-field refusal

`test_rejects_every_sealed_field_category` iterates a closed 20-entry tuple —
`root, root_id, draw, draw_index, band, target_band, node_count, plan, trace, skeleton,
skeleton_identity, scaffold, direction, source, branch, held_out, certificate, rejection,
subcause, fixture_name` — attaching each key separately to a fresh genuinely canonical
theorem and asserting the real `public_projection` raises exactly
`CANONICAL_THEOREM_PRECONDITION_VIOLATED`. The tuple's length and distinctness are asserted.
The V1 malformed / naming / ordering / cardinality / undeclared-atom refusals are retained
in `test_rejects_every_sealed_field_mutation`, and the emitted-byte substring check is kept
as a separate output-side check.

### 2c. `OR_ELIM` assumption erasure

`test_or_elim_assumption_record_is_erased` changes only `left_assumption['formula']`, asserts
the assumption record genuinely differs, asserts `major`, `left_branch` and `right_branch`
are byte-identical, and proves `rule_skeleton` output is byte-identical.
`test_not_intro_assumption_record_is_erased` does the same for the `NOT_INTRO` assumption
record. No production change was needed, as the driver predicted.

## 5. Frozen-output conditions

- Exclusion artifact regenerated from the repaired tree for comparison only:
  SHA-256 `a64aaeb12176ab88755f9c8c08f26d9f9ee1df2af9147324373aacfdf43bd315`,
  and `cmp` against the frozen candidate copy reports **byte-identical**. The file in the
  candidate package was not rewritten.
- All eleven fixture theorem identities, theorem names, public items, public-projection
  hashes and skeleton identities are unchanged, asserted inside the gate against pinned V1
  values and re-confirmed by the identical artifact bytes.
- No fixture, ledger row or JSON value was tuned to the new code.

## 6. Verification

| step | result |
|---|---|
| recovery manifest `sha256sum -c` | 29/29 OK, before and after |
| `py_compile` both files (dev, route A, route B) | OK |
| ASCII check on both files | 0 non-ASCII bytes |
| ordinary Stage-B discovery, dev tree | **Ran 144 tests in 59.573s, OK** |
| route A: base → accepted L2 V5 cumulative → repaired L3 delta | **Ran 144 tests in 59.215s, OK** |
| route B: base → repaired final cumulative | **Ran 144 tests in 59.175s, OK** |
| route C: base → *persisted candidate* cumulative | **Ran 144 tests in 59.130s, OK** |
| standalone counterexample reproduction | V1 accepts, V2 refuses (see §3) |

Every patch passed `git apply --check` before application. Route C's two files hash-match the
persisted candidate copies exactly.

**Test counts.** 67 pre-existing Stage-B tests + 77 L3 gate tests = 144.
The L3 gate grew from 64 to 77 (+13: 4 authority, 7 canonical-precondition, 1 sealed-field
loop, 2 assumption-record erasure, minus 1 deleted documentary test). The pre-existing 67
remain green and untouched.

**Route manifests.** Non-`.git` path/mode/content manifest SHA-256:

```text
route_a = 499093d067cee7b01a71c56ac4a57ca85f7ed05882758965b723ebe6cf0e21da
route_b = 499093d067cee7b01a71c56ac4a57ca85f7ed05882758965b723ebe6cf0e21da
```

Equal.

**Patch scope.** The delta has exactly two `diff --git` entries, both new files
(`learning/phase2_stageb_identity.py`, `learning/test_phase2_stageb_identity.py`); no existing
MINIMO file changes. The cumulative has exactly 36 entries — the accepted 34 Stage-A/L0–L2
paths plus those two. `grep -c 'candidate/'` is 0 in both patches. The strings
`successor/stage_r/...` appear only as governing-file *content* inside the added source, as
Repair 2a requires; no candidate-package path is present.

**Runtime note.** Discovery went from ~30 s to ~59 s. This is the honest cost of Repair 1:
`public_projection` now performs a `k!` orbit minimisation on every call, and it is called
inside `identify` on all 1854 exhaustive bijection transformations. No test was sampled or
weakened to recover the time.

## 7. Scope confirmations

- Only the two candidate source files and the two patch files were replaced. The frozen
  exclusion JSON and the V1 Builder report are byte-preserved.
- No annex, closure, activation, contract, recovery artifact or accepted L0–L2 file was
  modified. Recovery manifest still verifies 29/29.
- `/home/master/llm_projects/minimo` is byte-identical before and after this repair
  (`git status --porcelain`, `HEAD` and the SHA-256 of its two pre-existing modified files all
  unchanged); it was never used as implementation evidence.
- The selector helper name occurs in neither delivered file (the gate asserts this by
  assembling the string from parts); no scan was run; only the six literal frozen L2 rows
  were regenerated; no new fixture exists.
- No key, root or frame generation; no L4; no Peano, MCTS or search execution; no learner or
  selector run; no disposable or scientific execution; no commit; no push.

## 8. Focused time

- V1 pass: 1 h 25 min.
- V2 repair pass: 34 min (15:24:26 → 15:58:10 +03:00).
- **Cumulative focused time: 1 h 59 min** against the eight-hour §4.3 kill. The kill did not fire.

```text
L3_SCOPE=THEOREM_IDENTITY_PUBLIC_PROJECTION_RESERVOIR_LOCAL_SKELETON
DRIVER_MAJOR_1_CLOSED=YES
DRIVER_MAJOR_2A_CLOSED=YES
DRIVER_MAJOR_2B_CLOSED=YES
DRIVER_MAJOR_2C_CLOSED=YES
FROZEN_EXCLUSION_JSON_CHANGED=NO
FIXTURE_OUTPUTS_CHANGED=NO
NEW_MINIMO_FILES=2
EXISTING_MINIMO_FILES_CHANGED=0
STAGE_B_DISCOVERY_TESTS=144
L3_GATE_TESTS=77
PATCH_ROUTES_EQUAL=YES
COMMITTED_OR_PUSHED=NO
```

READY_FOR_STAGE_R_L3_DRIVER_REAUDIT_V2
