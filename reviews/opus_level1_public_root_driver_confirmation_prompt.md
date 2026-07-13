# Opus 4.8 bounded confirmation: Level 1 public-root driver

Work in `/home/master/llm_projects/philosophia`. Do not commit and **do not invoke
the driver** with a valid HEAD. Write the full confirmation to
`reviews/opus_level1_public_root_driver_confirmation.md`.

Read:

- `reviews/opus_level1_public_root_driver_review.md`
- `reviews/sol_level1_public_root_allocation_review.md`
- `reviews/codex_level1_public_root_review_closure.md`
- current `src/philosophia/level1/public_root.py`
- current `scripts/level1_draw_public_root.py`
- current `tests/test_level1_public_root.py`
- `experiments/level_1_contact/PUBLIC_ROOT_EXECUTION_PROTOCOL.md`

Run only unit/full tests, `--help`, static inspection and temp-repo simulations.
Never create a real allocation artifact or call the entropy path.

Confirm only the prior findings:

1. A canonical durable transcript plus git failure routes to COMMIT_PENDING and
   preserves the root; invalidity is reserved for a missing/corrupt/mismatched
   transcript. Neither route can quietly redraw.
2. The reachable-module entropy scan genuinely covers every imported path used
   before/after the call and admits exactly one literal `token_bytes(32)`.
3. Temp-repo tests exercise HEAD mismatch, byte drift, dirty tree, staged index
   and existing artifact refusal before entropy.
4. `_commit_transcript` rechecks an empty index, stages exactly claim+transcript,
   verifies that staged set, and has fixed commit trailers.
5. Claim irreversibility and commit-pending recovery are documented honestly
   under the procedural threat model. No recovery command is silently authorized.
6. `--reviewed-code-head` plus `--expected-head` mechanically permits only
   docs/review changes between reviewed code and final execution HEAD for the
   five load-bearing source paths.
7. D/roles/R_h semantics accepted by Sol remain byte/scientifically unchanged.
8. No entropy, real panel, feasibility/scout, N3, lock, escrow, trajectory or
   outcome was produced or newly authorized.

Return exactly one verdict:

- `LEVEL1_PUBLIC_ROOT_DRIVER_CONFIRMED`
- `REVISE_LEVEL1_PUBLIC_ROOT_DRIVER`

If revising, name only a concrete failure of M1/M2/m1-m3 closures. If confirmed,
state the exact fields/checks a later execution authorization record must bind.
Confirmation alone still does not authorize the draw.
