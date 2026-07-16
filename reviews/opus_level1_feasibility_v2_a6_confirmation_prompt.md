# Opus bounded confirmation: Level 1 feasibility v2 A6 closure

Re-review only the A6 parameter-finiteness blocker identified by Sol after your
initial implementation confirmation.

Reviewed closure commit:
`f025cf7fe981c8ae41f502d2e7608e6e9273fc25`

Original implementation anchor:
`d8c46637adf6f0caab039559c9031b1af65985b4`

Verify that the load-bearing source diff between those commits is limited to
`src/philosophia/level1/{train,feasibility}.py` and
`tests/test_level1_feasibility_v2.py`. Read
`reviews/sol_level1_feasibility_v2_scope_review.md`, especially its sole
Critical finding and three mandatory edits.

Confirm or reject:

1. `full_history_committee_step` distinguishes pre-update CE-loss finiteness
   from model-parameter finiteness scanned immediately after all AdamW steps.
   An optimizer-created Inf/NaN returns a scientific non-finite result before
   any panel evaluation or next oracle step.
2. The v2 payload reports separate `all_losses_finite` and
   `all_parameters_finite` flags. The v1 trajectory dataclass, v1 runner, and
   immutable v1 evidence semantics remain unchanged.
3. The first bad learner state stops the trajectory. A qualifying window
   completed before it still gives `censored_at_b:false`; otherwise the valid
   A6 terminal is censored. No per-step non-finiteness or panel series persists.
4. Tests create post-AdamW parameter Inf directly, cover a bad checkpoint before
   a window and the final bounded step after a complete window, prove no panel
   call occurs after the bad state, and prove process/resource/hash/seal
   exceptions install no report or binary.
5. The change closes A6 without reopening endpoint, cadence, persistence,
   learner policy, resource cap, paths, schemas, or interpretation.

Current evidence: focused v2+v1 tests 25 pass; full suite 158 pass; inherited
hashes match; admitted decisions VALID. No v2 authorization, claim/report,
probe, panel, N3, lock, escrow, trajectory, or outcome exists.
`essay/OUTLINE.md` is user-owned and out of scope.

Do not run the v2 driver or create authorization, claim/report, invalidity,
probe, entropy, panel, N3, lock, or trajectory. Tests/read-only verifiers only.

Write `reviews/opus_level1_feasibility_v2_a6_confirmation.md` without
committing. Lead with exactly one verdict:

- `LEVEL1_FEASIBILITY_V2_A6_XLINE_CONFIRMED`
- `REVISE_LEVEL1_FEASIBILITY_V2_A6`

If confirmed, state whether Codex may prepare the v2 authorization candidate
for separate review, but not execute it. Do not reopen optional G-1/G-2 unless
this closure makes either load-bearing.
