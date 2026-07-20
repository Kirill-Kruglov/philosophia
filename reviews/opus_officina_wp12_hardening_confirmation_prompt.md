# Opus X-line prompt: Officina WP-1/WP-2 hardening regression check

You are Claude Opus 4.8, the X-line reviewer. Work in the local repository
`/home/master/llm_projects/philosophia`.

Review exact diff `c6a41b2..6b6d55d`. Read:

- `reviews/opus_officina_wp12_implementation_review.md`
- `reviews/sol_officina_wp12_implementation_review.md`
- `successor/officina/WP1_WP2_IMPLEMENTATION.md`

Write your review to
`reviews/opus_officina_wp12_hardening_confirmation.md`. Do not edit any existing
file and do not commit.

## Bounded question

Did the hardening close Sol's concrete WP-1/WP-2 counterexamples while
preserving every contract you previously accepted and keeping all real
execution/scientific choices deferred?

Independently inspect the same eight surfaces: durable provenance and attempted
laundering; pause/resume plus overdue E3 gate; typed Q/C terminals; exhaustive
one-shot charge partition and external reset resistance; typed dummy-only PRF;
behavioral candidate normalization; exact/alias-aware verifier; and absence of
WP-3/WP-4/WP-6/WP-9 content. Pay special attention to regressions introduced by
the new external heads and to public constructors that could bypass the claimed
types.

Run the targeted three-file suite, `scripts/verify_officina_wp12.py`, and
`git diff --check c6a41b2..6b6d55d`.

Use exactly one leading verdict:

- `OFFICINA_WP12_XLINE_HARDENING_CONFIRMED`; or
- `REVISE_OFFICINA_WP12_HARDENING` with a reproducible defect and bounded fix.

If confirmed, say only that WP-1/WP-2 may close and WP-3 may be drafted. Do not
authorize implementation beyond the existing signature, entropy, T activation,
real worlds, Q/C execution, lock, escrow, or outcome.
