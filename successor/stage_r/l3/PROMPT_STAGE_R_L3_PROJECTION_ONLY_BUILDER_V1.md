# Prompt — Stage-R L3 projection-only Builder V1

ROLE: bounded implementation Builder (Codex, Cursor or Claude Opus). Implement
the frozen Stage-R L3 projection-only annex exactly. Do not redesign it, request
an author choice or perform a scientific/architecture review. Do not implement
L4 or a future dev-root pipeline. Do not commit or push.

The focused-work limit is eight working hours. If the exact boundary cannot be
closed inside it, stop with evidence and `STAGE_R_L3_FOCUSED_DAY_KILL`, rather
than simplifying a predicate or expanding scope.

## Authority and pins

- Executable annex:
  `successor/stage_r/l3/STAGE_R_L3_PROJECTION_ONLY_EXECUTABLE_ANNEX_V1.md`,
  SHA-256
  `a6848dd2a64b81783f59ef7aafcebe66bf1fb109aad2f2cb183f9d4d646829a0`.
- Annex driver closure:
  `successor/stage_r/l3/STAGE_R_L3_PROJECTION_ONLY_ANNEX_DRIVER_CLOSURE_V1.md`,
  SHA-256
  `4d37b1fb648de442ebe484704b8e309d93c5b755aab04da4949f185401193811`.
- Annex commit:
  `19e62a7eac6ca38a79da117ff86c1c8eba72516a`.
- Accepted Stage-R contract:
  `successor/stage_r/PHILOSOPHIA_MINIMUM_CAUSAL_CONTRACT_R_V2_1.md`,
  SHA-256
  `1c3cec3aa6bd7094e2d37b062a8f349df5b226e91bbdc4a7b21e80fb785172f3`.
- L3 activation:
  `successor/stage_r/STAGE_R_L3_PROJECTION_ONLY_ACTIVATION_V1.md`,
  SHA-256
  `2539786a2b3954408a8fb98f0d8238636c0644900b56c74a2a6eec436da017b2`.
- Recovery manifest:
  `successor/recovery/phase2_stage_b_20260815/SHA256SUMS`.
- MINIMO base: `6066f482c6752915ad21119f93dc162f4cb9db72`.
- Accepted cumulative patch through L2 V5:
  `successor/recovery/phase2_stage_b_20260815/patches/minimo_phase2_stagea_stageb_l01_l2_v5_cumulative.patch`,
  SHA-256
  `3a570b2e35b15dc796d86cd8a997230c00bbf5aed3b5c06f3b14dca78b46b683`.
- Accepted L2 code-gate JSON SHA-256:
  `8961b5a97ee0972d83a071e1b1c82869a9841f5f01c45add12a88dbfee1010f0`.
- Accepted V3 ledger SHA-256:
  `a1f907ad6665b7c96d91496c5a91d32f0f0cae63da48b6b26da6b292d48f528d`.

Recompute every pin before work. The archived unaccepted L3 draft is not
authority and must not restore its exact-plan identity, V4 stage-6 seed, AC-1
choice or review schedule.

## Hard scope

The MINIMO delta adds exactly:

```text
learning/phase2_stageb_identity.py
learning/test_phase2_stageb_identity.py
```

No existing MINIMO file may change. Persist the final copies and all evidence
under:

```text
successor/stage_r/l3/candidate/
```

Do not modify the original `/home/master/llm_projects/minimo` checkout. Use a
fresh `mktemp -d` execution directory, clone the local repository without
network access, check out the pinned base and apply the accepted cumulative
patch. The existing MINIMO virtual environment may execute the fresh tree; do
not install or update dependencies.

Do not modify the annex, closure, activation, recovery files or accepted
artifacts. Do not run `select_l2_code_gate_rows` or any scan. Do not generate a
root, frame or new fixture; regenerate only the six literal frozen L2 rows.
No Peano, compile/replay, MCTS/search, query measurement, learner/selector,
training, disposable or scientific execution is permitted.

## Implementation duties

Read the production dependency files line by line before coding. Implement
every API, schema, algorithm, bound, precedence and no-alias rule in annex
§§2–6. In particular:

- production must not import checker or generator;
- raw theorem comparison occurs before canonicalization;
- theorem minimization enumerates all `k!`, never a heuristic representative;
- hypotheses sort by formula canonical bytes only;
- skeleton erases and retains exactly the named distinctions;
- public projection accepts only the canonical theorem and emits exactly five
  keys via the accepted renderer;
- success/failure records have exact keys and mismatch precedence;
- internal defects raise only the closed `L3InvariantError` codes;
- all outputs are fresh and inputs remain byte-unchanged;
- no retry, backtracking, random choice, filesystem or mutable global exists in
  production.

Implement every mandatory annex §7 test. Tests may reconstruct the five L1
fixtures and call `generate_draw` on exactly the six frozen JSON rows. Before
identity computation, reverify the V3 raw plan/theorem hashes. The test-only
artifact helper must take an explicit output path and write canonical JSON plus
one newline. Ordinary discovery may use temporary paths only; after it passes,
invoke the helper once for the durable candidate artifact.

Do not reduce exhaustive atom-permutation tests to samples. Do not replace real
boundary injections with mocked public records. Do not omit fresh-process,
alias, invariant-injection, source-discipline or artifact-reproducibility tests.

## Verification and patch routes

Run, at minimum:

1. recovery `sha256sum -c`;
2. `py_compile` on the two new files;
3. ordinary Stage-B unittest discovery with pattern
   `test_phase2_stageb*.py` from the reconstructed tree;
4. a second clean application of the L3 delta atop the accepted L2 route and
   the same discovery command;
5. a clean application of the final cumulative patch directly atop the pinned
   base and the same discovery command;
6. exact path-scope, source-import, patch-coherence and original-worktree
   no-drift checks.

The two routes must have the same non-`.git` path/mode/content manifest. Record
the measured test count; do not assume it in advance. A failure is repaired only
inside the two files and rerun. If repair would require another path or annex
change, stop as blocked.

Create:

```text
successor/stage_r/l3/candidate/learning/phase2_stageb_identity.py
successor/stage_r/l3/candidate/learning/test_phase2_stageb_identity.py
successor/stage_r/l3/candidate/STAGE_R_L3_CODE_GATE_EXCLUSIONS_V1.json
successor/stage_r/l3/candidate/minimo_phase2_stageb_l3_projection_v1_delta.patch
successor/stage_r/l3/candidate/minimo_phase2_stagea_stageb_l01_l2_l3_projection_v1_cumulative.patch
successor/stage_r/l3/candidate/STAGE_R_L3_BUILDER_REPORT_V1.md
```

The delta is a Git patch relative to the accepted L2 tree and adds exactly the
two L3 files. The cumulative patch is relative to the pinned base. Neither
patch may contain candidate-package paths.

## Report and stop

The report must contain:

- every input and output SHA-256;
- exact production/test line counts;
- test commands, measured counts and elapsed times;
- focused working time used against the eight-hour limit;
- exact delta and cumulative path scopes;
- both route manifests and their equality;
- confirmation that the selector scan was not called and only six literal rows
  were regenerated;
- confirmation that the original MINIMO worktree's pre-existing changes were
  neither modified nor used as evidence;
- confirmation that L4, roots, frame selection and all execution stages remain
  unauthorized;
- any limitation or failing test with exact evidence.

Do not commit or push. If all requirements pass, end both the report and chat
response with:

```text
READY_FOR_STAGE_R_L3_DRIVER_CODE_AUDIT_V1
```

Otherwise end with exactly one:

```text
BLOCKED_STAGE_R_L3_PROJECTION_ONLY_V1
STAGE_R_L3_FOCUSED_DAY_KILL
```
