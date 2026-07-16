# Opus review prompt: Level 1 feasibility v2 implementation

Review the **signed floor-amendment implementation only** at reviewed-code
commit `d8c46637adf6f0caab039559c9031b1af65985b4`. Current HEAD may add
review-only files; verify that load-bearing source bytes are unchanged.

Governing chain: `FEASIBILITY_FLOOR_AMENDMENT_V2_DRAFT.md`, its v2.1 and
v2.2 corrections, `SCIENTIFIC_SPEC_SIGNATURES.md`, and immutable v1 evidence
under `experiments/level_1_contact/feasibility/`.

Audit `scripts/level1_run_feasibility_v2.py`,
`src/philosophia/level1/{feasibility,interlock,train,public_root}.py`, every
`REVIEWED_SOURCE_PATHS` entry, `tests/test_level1_feasibility_v2.py`, and
v1 regressions.

The only policy change is one mean-CE AdamW update per answer over all `t`
own-history pairs, in contact order, as one shared unchunked tensor for all four
members. Scope remains one RANDOM-STATIC development trajectory at
`pair_slot=0, n=66`, one replicate, `B=2000`, zero scorer, 36-hour wall,
and unchanged dummy panel, cadence, persistence, and binary criterion.

Verify independently:

1. Exact full-history order and shared four-member update; no replay, chunking,
   accumulation, extra updates, post-collection training, or early success stop.
2. v1 behavior/evidence unchanged; distinct v2 capability exactly
   `2000/0/129600`; no comparative/outcome capability.
3. v1-faithful schedule/world, model/optimizer/init, step-0/every-50 panel,
   five checkpoints spanning 200, non-finite route, and checkpoint-size surface.
4. Exact schemas, paths, token, hashes, source pins, tracked canonical lineage,
   clean tree/index, exact HEAD, existing-artifact and later-gate refusals.
5. Transcript fingerprint consistency and actual canonical runtime match before
   claim creation.
6. Race-safe durable no-replace claim: same-directory temp, file fsync,
   no-replace install, parent fsync; claim before step 1, report only after valid
   terminal, no automatic rerun after an intervening failure.
7. Report has only allowed aggregates, size, flags, and one censoring bit; no
   series, scorer, second arm, contrast, N3, lock, real panel, escrow, outcome.
8. Tests detect policy/replay/scorer/source/evidence/environment/output/repeat
   drift and replacement races.

Evidence: 152 tests pass; 71 inherited hashes match; admitted decisions VALID.
No v2 authorization, claim, report, probe, comparative datum, N3, lock, panel,
escrow, trajectory, or outcome exists. `essay/OUTLINE.md` is user-owned.

Do not run the v2 driver or create any authorization, claim/report/invalidity,
probe, entropy, panel, N3, lock, or trajectory. Tests/read-only verifiers only.

Write `reviews/opus_level1_feasibility_v2_implementation_review.md` without
committing. Verdict exactly one of:

- `LEVEL1_FEASIBILITY_V2_IMPLEMENTATION_CONFIRMED`
- `REVISE_LEVEL1_FEASIBILITY_V2_IMPLEMENTATION`

List severity findings, mandatory edits, future guards, and negative space.
Answer whether Codex may prepare a v2 authorization candidate for separate
review, but not execute it.
