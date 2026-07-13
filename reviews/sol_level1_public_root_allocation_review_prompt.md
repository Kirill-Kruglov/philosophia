# GPT-5.6 Sol Y-line review: Level 1 public-root allocation semantics

Work in `/home/master/llm_projects/philosophia`. Do not commit and **do not run
the public-root driver**. Write the full review to
`reviews/sol_level1_public_root_allocation_review.md` and return a concise verdict.

Read v3.1 A2/A5/A9, v3.1.1 C2/C3/C6/C7, the signature records, current
allocation/serialization code, and:

- `src/philosophia/level1/public_root.py`
- `scripts/level1_draw_public_root.py`
- `tests/test_level1_public_root.py`

Unit/full tests and static inspection are permitted; entropy execution and any
allocation artifact are forbidden.

## Required questions

1. Does one public 256-bit root plus the already reviewed HMAC/U/Fisher-Yates
   machinery restore the signed design-based randomization reading?
2. Does the transcript materialize exactly six development pairs (2/stratum)
   before development and all 24 outcome target/donor role assignments once,
   using the independent `dev/h` and `role/pair_slot` domains?
3. Is `R_h` mechanically absent/deferred until frozen N3, with no route for
   feasibility, censoring, loss or contrast information to regenerate D/roles?
4. Is publishing root+D+roles immediately scientifically valid under the signed
   procedural threat model and assignment-conditioned finite-frame estimand?
5. Does the transcript bind enough provenance to make later inclusion
   probabilities and the FPC auditable? Re-derive D/role counts from a fixed test
   root and check the golden transcript.
6. Could the root or transcript reveal any real evaluator-panel word/order/salt,
   or does the explicit public-root/escrow-secret separation remain intact?
7. Does any failure/invalidity state bias the design by allowing selection among
   roots? Check claim-before-draw and no-redraw behavior from a randomization
   perspective, not only software robustness.
8. Are environment/witness fields scientific metadata rather than new degrees of
   freedom? Is the witness statement limited to process facts?
9. State any missing pre-execution predicate, transcript assertion, or
   post-execution verification needed before the root may become the fixed source
   for feasibility/scout work.

Return exactly one verdict:

- `LEVEL1_PUBLIC_ROOT_ALLOCATION_ACCEPTED`
- `REVISE_LEVEL1_PUBLIC_ROOT_ALLOCATION`
- `BLOCKED_LEVEL1_RANDOMIZATION_PROTOCOL`

Classify findings with file:line references. If accepted, state the exact
conditions under which a single execution may be authorized. This review does
not authorize entropy, feasibility, comparative scout, N3 selection, lock,
escrow, trajectory or outcome.
