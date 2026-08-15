# Prompt — final independent Stage-R L3 projection-only code review X

ROLE: independent X code reviewer (Codex/GPT 5.5 or Claude Opus 4.8; not the
Opus 5 Builder). Read-only. Review the repaired L3 implementation against the
frozen executable annex. Do not edit, commit or push. Do not perform a general
scientific or architecture review and do not propose exact-plan identity,
stage-6 seed, L4 or a larger pipeline.

## Governing objects

- Executable annex:
  `successor/stage_r/l3/STAGE_R_L3_PROJECTION_ONLY_EXECUTABLE_ANNEX_V1.md`,
  SHA-256
  `a6848dd2a64b81783f59ef7aafcebe66bf1fb109aad2f2cb183f9d4d646829a0`.
- Driver V1 finding:
  `successor/stage_r/l3/STAGE_R_L3_DRIVER_CODE_AUDIT_V1.md`, SHA-256
  `1375d71b7dd1a52c6e2915d95e878fcf2df99682c2fd3b3b06b3b503551fc374`.
- Driver V2 re-audit:
  `successor/stage_r/l3/STAGE_R_L3_DRIVER_CODE_REAUDIT_V2.md`, SHA-256
  `151b5fc8b3c1ff09b3b27918f8ca349ba56e21829a36491734d4ec590c37f59e`.
- Builder V2 report:
  `successor/stage_r/l3/candidate/STAGE_R_L3_BUILDER_REPAIR_REPORT_V2.md`,
  SHA-256
  `92752e0bae86a5c4d5db5d77a56457693b5467c87c766f949722be9ac085cf9c`.
- Production:
  `successor/stage_r/l3/candidate/learning/phase2_stageb_identity.py`,
  SHA-256
  `ee1be7afef332d8ce87b37c885760dfddcdcb911525cc377aec940b02ac07860`.
- Test:
  `successor/stage_r/l3/candidate/learning/test_phase2_stageb_identity.py`,
  SHA-256
  `2d71a629acb8dfa5bd8d42eef57b87746e9e6df28a80b514e950515e506dd45e`.
- Frozen exclusion JSON:
  `successor/stage_r/l3/candidate/STAGE_R_L3_CODE_GATE_EXCLUSIONS_V1.json`,
  SHA-256
  `a64aaeb12176ab88755f9c8c08f26d9f9ee1df2af9147324373aacfdf43bd315`.
- L3 delta SHA-256:
  `4f4b692a0ae8f3e989a6e353618cab19d20becc05d7dfe2007f6d58e7f354b71`.
- Cumulative patch SHA-256:
  `6194d40cecb7b5b70825ef3d4122a215a9706fa17b449b45126dc63070e6d14c`.
- MINIMO base:
  `6066f482c6752915ad21119f93dc162f4cb9db72`.

Recompute every pin. Builder and driver reports are inputs, not substitutes for
line-by-line review.

## Hard execution boundary

Do not call or import `select_l2_code_gate_rows` and do not run any scan. You may
run ordinary Stage-B discovery; it reconstructs only the five L1 fixtures and
the six literal frozen L2 rows. You may use explicit constructed inputs and a
fresh local clone at the pinned base. Do not modify the original MINIMO or
Philosophia worktree. No L4, root, frame selection, Peano, MCTS/search, query
measurement, learner/selector, training, disposable or scientific execution.

## Review duties

1. Verify patch scope: the delta adds exactly the two authorized files; the
   cumulative route is the accepted 34 paths plus those two; both apply cleanly
   and produce the candidate bytes.
2. Read production line by line. Independently prove full `k! <= 720` theorem
   normalization, formula/proof bounds, hypothesis ordering, raw mismatch
   precedence, exact schemas, fresh construction and absence of hidden state,
   retry, randomness, filesystem and layer coupling.
3. Construct independently a theorem with canonical atom spelling and sorted
   hypotheses that is not its alpha-orbit byte minimum. Confirm direct
   `public_projection` refuses it before hashing/rendering, while its true
   minimum is accepted. Confirm `identify` has exactly one public output for
   every alpha-equivalent input.
4. Type- and scope-check every skeleton case. Verify the two sorted positions,
   preserved positions, global/local leaf distinction, direction erasures and
   erasure of both `OR_ELIM` and `NOT_INTRO` assumption records.
5. Verify public projection has one argument, exact five keys, accepted renderer
   only, all 64 identity hex characters and no route for sealed metadata.
6. Verify authority binding occurs before fixture-cache population and hashes
   every governing file from the configurable project/recovery roots. Check
   missing/mismatched authority fails closed and does not silently use an
   alternate artifact.
7. Audit all 77 L3 tests against annex §7. Confirm exhaustive 1854 transformed
   plans, real mismatch/invariant seams, all twenty sealed-field injections,
   fresh-process determinism, no aliasing, import/source discipline and the V1
   output-regression pins. Do not infer coverage from class/test names.
8. Independently rederive the exclusion artifact shape and verify embedded V3
   equality, all eleven valid-plan mappings, the one raw alias group, absence of
   identities for renderer/enumerability rows and deliberate absence of root,
   quota, seed and collision-precedence fields. If invoking the artifact helper,
   use only a caller-supplied temporary path.
9. Verify the frozen JSON is a legitimate post-gate artifact, not retuned after
   repair, and that its unchanged hash follows from unchanged valid outputs.
10. Run ordinary Stage-B discovery if useful and report the independently
    measured count. Confirm the original worktrees remain untouched.

Do not reopen the accepted omission of exact-plan identity or the archived AC-1
choice: they are outside this Stage-R L3 boundary unless the repaired code has
actually introduced them.

## Findings and verdict

Findings first, ordered Critical/Major/Minor. Every finding must cite exact
candidate file:line and annex clause, give a behavioral consequence and the
smallest bounded repair, and say whether the frozen JSON would change. Do not
report style or hypothetical future extensibility.

Answer explicitly:

1. Is production code-faithful to the executable annex?
2. Does the gate cover every mandatory §7 seam?
3. Are both patch routes and the unchanged exclusion JSON coherent?
4. May projection-only L3 close while L4 and all execution remain unauthorized?

Return exactly one verdict token:

```text
ACCEPT_STAGE_R_L3_PROJECTION_ONLY_CODE_X
REPAIR_REQUIRED_STAGE_R_L3_PROJECTION_ONLY_CODE_X
BLOCKED_STAGE_R_L3_PROJECTION_ONLY_CODE_X
```

Either verdict authorizes no L4, key/root/frame generation, learner/selector,
disposable work or scientific execution.
