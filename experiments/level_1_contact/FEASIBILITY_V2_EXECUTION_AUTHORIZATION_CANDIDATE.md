# Level 1 feasibility v2 execution authorization candidate

Status: `AWAITING_BOUNDED_REVIEW_AND_KIRILL_ONE_SHOT_TOKEN`.

This Markdown record is not the canonical authorization path and cannot pass
driver preflight. It authorizes no execution and creates no authorization,
claim, report, invalidity artifact, entropy, probe, panel, N3, lock, escrow,
trajectory, or outcome.

## Reviewed implementation

```text
REVIEWED_CODE_HEAD=f025cf7fe981c8ae41f502d2e7608e6e9273fc25
XLINE_VERDICT=LEVEL1_FEASIBILITY_V2_A6_XLINE_CONFIRMED
YLINE_VERDICT=LEVEL1_FEASIBILITY_V2_A6_YLINE_CONFIRMED
```

The driver source-pin set is:

```text
scripts/level1_run_feasibility_v2.py
src/philosophia/level1/feasibility.py
src/philosophia/level1/interlock.py
src/philosophia/level1/train.py
src/philosophia/level1/public_root.py
src/philosophia/level1/pool.py
src/philosophia/level1/panel.py
src/philosophia/level1/model.py
src/philosophia/level1/acquisition.py
src/philosophia/level1/config.py
src/philosophia/level1/serialization.py
src/philosophia/level1/scoring.py
src/philosophia/level1/world.py
```

## Future canonical authorization bytes

Only after bounded review accepts this candidate and Kirill supplies exactly

```text
I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2
```

may Codex create the new tracked file
`experiments/level_1_contact/FEASIBILITY_EXECUTION_AUTHORIZATION_V2.json`.
Its canonical JSON content must be exactly the following single line plus a
terminal newline:

```json
{"arm":"RANDOM-STATIC","caps":{"development_worlds":1,"scorer_steps":0,"trajectory_steps":2000,"wall_seconds":129600},"development_world":{"modulus":66,"pair_slot":0},"execution_once":true,"governing_amendment_sha256":{"FEASIBILITY_FLOOR_AMENDMENT_V2_1_CORRECTION.md":"d9ed5b562cbebef3e3b0a9c72d2d9dda35c834a044faf593d52b96b20c89ca14","FEASIBILITY_FLOOR_AMENDMENT_V2_2_CORRECTION.md":"5b413bc36e3468cb57c78b8832c471c51013bf160d71dc216c095907b2556c9b","FEASIBILITY_FLOOR_AMENDMENT_V2_DRAFT.md":"51d9833c79127c9a06b7e625b0f2af3c41cd0bdf54e5f63a950463ffc5c65fc8"},"governing_signature_sha256":"04a7c7c1ceac2a58c7469997d1fe25bdd5f80a9976e0b4838604b0e39252422b","output_directory":"experiments/level_1_contact/feasibility_v2","reviewed_code_head":"f025cf7fe981c8ae41f502d2e7608e6e9273fc25","schema":"philosophia.level1.feasibility-authorization.v2","scientific_outcome":false,"token":"I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2","v1_evidence_sha256":{"LEVEL1_NONCOMPARATIVE_FEASIBILITY.json":"1c3843ec66f57e8a7e05b88d5f942093113f11f5ac36746f202f1a6556820b7f","LEVEL1_NONCOMPARATIVE_FEASIBILITY_CLAIM.json":"357baef22226bfb92b909192d2264420923facd55115b9c272bb2cb848c106ab"}}
```

The commit adding that JSON must contain no source, spec, test, review, or other
artifact change. Its commit hash is the execution `EXPECTED_HEAD`. No tracked
commit or modification may occur between that authorization-only commit and the
single invocation. This avoids self-reference: `reviewed_code_head` remains
the independently reviewed closure commit, while `EXPECTED_HEAD` binds the
later Kirill-authorized repository state.

## Governing lineage

```text
9f642a55d581309cc024182a3c5e149a052de13d14622c7fd96744d4b4e77f6e  allocation/PUBLIC_ROOT_TRANSCRIPT.json
04a7c7c1ceac2a58c7469997d1fe25bdd5f80a9976e0b4838604b0e39252422b  SCIENTIFIC_SPEC_SIGNATURES.md
51d9833c79127c9a06b7e625b0f2af3c41cd0bdf54e5f63a950463ffc5c65fc8  FEASIBILITY_FLOOR_AMENDMENT_V2_DRAFT.md
d9ed5b562cbebef3e3b0a9c72d2d9dda35c834a044faf593d52b96b20c89ca14  FEASIBILITY_FLOOR_AMENDMENT_V2_1_CORRECTION.md
5b413bc36e3468cb57c78b8832c471c51013bf160d71dc216c095907b2556c9b  FEASIBILITY_FLOOR_AMENDMENT_V2_2_CORRECTION.md
357baef22226bfb92b909192d2264420923facd55115b9c272bb2cb848c106ab  feasibility/LEVEL1_NONCOMPARATIVE_FEASIBILITY_CLAIM.json
1c3843ec66f57e8a7e05b88d5f942093113f11f5ac36746f202f1a6556820b7f  feasibility/LEVEL1_NONCOMPARATIVE_FEASIBILITY.json
```

Paths are relative to `experiments/level_1_contact/`. The transcript SHA is an
operator cross-check; the driver additionally verifies its tracked canonical
content, frozen world, forbidden derivations, internal environment fingerprint,
and live exact-environment match.

## Pre-execution predicates

All must pass immediately before the one invocation:

1. `EXPECTED_HEAD == git rev-parse HEAD`.
2. The canonical authorization JSON exists, is Git-tracked, and its bytes equal
   the block above.
3. `git diff --quiet REVIEWED_CODE_HEAD EXPECTED_HEAD -- <13 source paths>`
   succeeds.
4. Tracked working tree and index are clean. The sole allowed untracked path is
   the user-owned `essay/OUTLINE.md`; any additional untracked path blocks.
5. The governing hashes above rederive exactly. The driver-pinned signature,
   amendments, and immutable v1 evidence hashes must match.
6. Neither v2 claim nor report nor their same-directory temporary file exists.
7. No comparative scout, N3 selection, preregistration lock, real panel,
   escrow, or outcome decision artifact exists.
8. Canonical runtime is CPython 3.12.3, torch 2.9.1+cpu, CPU/float32,
   deterministic algorithms, one intra-op and one inter-op thread, with the
   exact public-root environment fingerprint.
9. At least 158 full-suite tests pass; focused v2+v1 tests pass; inherited hashes
   match; admitted inherited and Level 0 decisions are VALID.

## Single command

With the authorization-only commit checked out at HEAD:

```bash
.venv/bin/python scripts/level1_run_feasibility_v2.py \
  --expected-head "$(git rev-parse HEAD)" \
  --output-dir experiments/level_1_contact/feasibility_v2
```

Invoke exactly once. On any exception, stop. Do not delete, replace, or rerun
anything. A claim without a valid report leaves `censored_at_b` unset and
requires a signed invalidity disposition; no invalidity subtype pre-authorizes
a rerun.

## Post-run verification

If and only if a valid report is installed:

1. Claim and report both exist; no temporary file exists.
2. Report schema is `philosophia.level1.noncomparative-feasibility.v2`,
   `scientific_outcome:false`, `validity:valid-scientific-terminal`, arm is
   `RANDOM-STATIC`, replicate is 1, world is `{pair_slot:0, modulus:66}`, and
   caps are exactly `{1,2000,0,129600}`.
3. Measurements contain only trajectory aggregates, separate terminal
   `all_losses_finite` / `all_parameters_finite`, panel computability,
   `censored_at_b`, checkpoint-size estimate, and the projection-scope text.
   No query/loss/solve/checkpoint series or scorer/contrast field exists.
4. Every contamination guard is false; no real panel, N3, lock, escrow, or
   outcome artifact was created.
5. Authorization, signature, amendment, v1 evidence, transcript, Git HEAD, and
   reviewed-code bindings rederive exactly.
6. If either finiteness flag is false, apply signed A6: a completed qualifying
   window before divergence stands; otherwise the valid scientific terminal is
   censored. Never relabel it process invalidity.
7. `censored_at_b:false` permits comparative-scout review only.
   `censored_at_b:true` routes to `BLOCKED_LEVEL1_FEASIBILITY`, C1 untested,
   with no third learner-policy intervention.
8. Only after verification may claim and report be archived in a dedicated
   evidence commit with the agreed co-author trailers and pushed. No subsequent
   gate begins under this token.

## Authorization boundary

This future token authorizes one v2 noncomparative feasibility execution only.
It does not authorize a resource probe, comparative scout, N3 selection,
preregistration lock, real panel generation, escrow, Level 1 outcome run, or any
v1/v2 effect claim. This candidate itself authorizes none of those actions.
