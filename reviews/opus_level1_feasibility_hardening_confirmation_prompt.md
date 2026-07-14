# Opus bounded confirmation: Level 1 feasibility hardening

Re-review only the closure of your `FS-1` through `FS-6` findings from
`reviews/opus_level1_feasibility_implementation_review.md`.

Reviewed hardening commit:
`be53fdd64495698c74446a4cc2ddd3aabc9aeb22`

The original implementation anchor remains
`308aa6fcfd165b1742a1ec4988a660d9a6c21333`. Verify the exact diff between those
commits and inspect:

- `tests/test_level1_feasibility.py`;
- `src/philosophia/level1/{feasibility,interlock,pool,train}.py`;
- `scripts/level1_run_feasibility.py`.

Please confirm or reject, without reopening signed scientific constants:

1. `feasibility_committee_step` is now exercised with four actual tiny models,
   one shared minibatch, one capability spend, updates to all members,
   post-step zeroed gradients, and a non-finite no-update case.
2. The bounded wiring test exercises the production loop with injected fixtures
   and pins step 0 + cadence, a five-checkpoint qualifying window, one
   oracle-step spend per loop, non-finite break/censoring, checkpoint-size
   plumbing, and scorer mutation failure. Confirm that raising the test-only cap
   from two to five cannot authorize the production path.
3. Scorer latency now includes shortlist realization/encoding; trajectory step
   latency includes scheduled checkpoint evaluation. The report states the
   remaining projection exclusions explicitly and does not become a full Level 1
   runtime forecast.
4. `public_root.py` is included in `REVIEWED_SOURCE_PATHS` and regression-pinned.
5. `realize_cell` now fails closed after 10,000 rejected attempts and the forced
   exhaustion path is tested; decide whether this cap is acceptable as a
   process/design-invalidity guard.
6. The contamination block is explicitly labelled a declarative attestation of
   structural guards, not runtime-derived evidence.

Current local evidence before this request: targeted feasibility suite 10 pass,
full suite 143 pass, inherited hash verifier OK, both admitted decisions VALID;
no authorization, claim, report, real panel, N3, lock, escrow, trajectory, or
outcome exists.

Do **not** run `scripts/level1_run_feasibility.py`, create an authorization,
claim/report, real panel, lock, or any scientific trajectory. Unit tests and
verifiers are allowed.

Write the response to
`reviews/opus_level1_feasibility_hardening_confirmation.md` without committing
it. Lead with exactly one verdict:

- `LEVEL1_FEASIBILITY_HARDENING_CONFIRMED`, or
- `REVISE_LEVEL1_FEASIBILITY_HARDENING`.

If confirmed, state whether Codex may prepare the authorization candidate for
Kirill's explicit token, while still not executing it.
