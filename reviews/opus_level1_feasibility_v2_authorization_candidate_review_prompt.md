# Opus review prompt: Level 1 feasibility v2 authorization candidate

Review only the non-executable authorization candidate at commit
`300dd9ee9fe38f4d0a2dc7d98c9ac85f60cb11b7`:

`experiments/level_1_contact/FEASIBILITY_V2_EXECUTION_AUTHORIZATION_CANDIDATE.md`

The reviewed implementation remains
`f025cf7fe981c8ae41f502d2e7608e6e9273fc25`, confirmed by
`LEVEL1_FEASIBILITY_V2_A6_XLINE_CONFIRMED` and
`LEVEL1_FEASIBILITY_V2_A6_YLINE_CONFIRMED`.

Audit:

1. The Markdown path cannot satisfy driver preflight and therefore asserts no
   live authorization. The actual canonical JSON path remains absent.
2. The embedded future JSON is canonical byte-for-byte and matches every field
   validated by `scripts/level1_run_feasibility_v2.py`: schema, token, arm,
   one-shot flag, scientific_outcome, caps, world, output, reviewed HEAD,
   signature/amendment hashes, and immutable v1 hashes.
3. The authorization-only future commit / `EXPECTED_HEAD` construction is
   non-self-referential, while source-byte comparison remains anchored at
   `f025cf7`. No source change can hide between review and execution.
4. All 13 source paths, lineage values, artifact absences, environment checks,
   clean-tree/index rules, and one-shot command agree with driver behavior.
5. Claim-before-step, report-after-valid-terminal, no-replace behavior, and
   stop-without-rerun handling are operationally exact.
6. Post-run checks correctly handle finite pass, finite censor, A6 non-finite
   terminal, and environment/resource/process/hash/seal invalidity.
7. The candidate does not authorize a probe, scout, N3, lock, real panel,
   escrow, outcome, or v1/v2 contrast.
8. Identify any field/order/hash/path mismatch that would either make the future
   JSON fail closed unexpectedly or authorize more than intended.

Current state: full suite 158 pass; inherited hashes match; admitted decisions
VALID; the embedded JSON template was independently canonicalized successfully.
No actual v2 authorization, claim/report, invalidity, probe, panel, N3, lock,
escrow, trajectory, or outcome exists. `essay/OUTLINE.md` is user-owned.

Do not create the JSON authorization, invoke the driver, create any artifact,
or run any scientific computation. Read-only tests/verifiers are allowed.

Write
`reviews/opus_level1_feasibility_v2_authorization_candidate_review.md`
without committing. Lead with exactly one verdict:

- `LEVEL1_FEASIBILITY_V2_AUTHORIZATION_CANDIDATE_XLINE_CONFIRMED`
- `REVISE_LEVEL1_FEASIBILITY_V2_AUTHORIZATION_CANDIDATE`

If confirmed, state whether Kirill may supply the exact one-shot token, after
which Codex may create and commit only the canonical JSON authorization but
still may not execute until that signature commit and all preflight predicates
are verified.
