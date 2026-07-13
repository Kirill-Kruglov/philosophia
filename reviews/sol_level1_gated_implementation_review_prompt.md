# GPT-5.6 Sol review prompt: Level 1 gated implementation and Y-line fidelity

You are the Y-line scientific/software auditor for Philosophia Level 1. Work in
`/home/master/llm_projects/philosophia`. Do not commit. Write the full review to:

`reviews/sol_level1_gated_implementation_review.md`

Then return a concise chat summary with the verdict and blocking edits.

## Governing material

Read the Level 1 v3 scientific spec, every correction/addendum v3.1 through
v3.1.4.1, both author-signature records, and the Fable/Opus/Sol closure reviews.
At minimum inspect:

- `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md`
- `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md`
- `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md`
- `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_2_CORRECTION.md`
- `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_3_CORRECTION.md`
- `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_4_PANEL_ADDENDUM.md`
- `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_4_1_PANEL_CORRECTION.md`
- `experiments/level_1_contact/SCIENTIFIC_SPEC_SIGNATURES.md`
- `experiments/level_1_contact/PANEL_CONTRACT_SIGNATURE.md`

Audit all files under `src/philosophia/level1/` and all
`tests/test_level1_*.py`. Run the complete suite and `scripts/verify_all.py`.

## Required audit questions

1. Are the learner architecture, initialization, optimizer groups/order,
   acquisition scorer, one-step training primitive and committee aggregation
   faithful to the signed v3 lineage? Identify every trajectory-sensitive cell.
2. Are solve-window semantics, ABSTAIN/confident-lie/Brier rules, per-stratum
   thresholds and no-early-stop boundary encoded exactly, or explicitly still
   absent behind a gate? No absent piece may be treated as implemented.
3. Re-derive the finite-population paired estimator, FPC, Satterthwaite df,
   Bonferroni family, census/zero-variance labels, margin directions and the
   exact determinacy guards for SUP/EQ/NI/NONSUP. Check edge cases, especially
   one arm all-censored and equality at the margin.
4. Does `choose_n3` implement the frozen three-contrast projection, conservative
   fallback and census route without silently using comparative data to set a
   margin?
5. Is ACTIVE side-effect-free and oracle-blind while scoring? Are YOKED donor
   provenance, RANDOM-STATIC and total contact-mode routing represented
   faithfully where implemented, and otherwise still gated?
6. Is the v3.1.4 panel repair statistically inert: same 188 items, same
   per-stratum label counts and thresholds, no change to estimands/inference,
   and no anti-lookup authority assigned outside S4?
7. Does every current execution surface fail closed beyond one unit-test step?
   Confirm no entropy, real panel, feasibility/scout, N3, lock, escrow,
   trajectory or outcome can be reached accidentally.
8. Are tests capable of catching an estimator-direction reversal, missing FPC,
   wrong censoring guard, wrong CE/aggregation, or leakage through scoring?
9. Separate implementation defects from later-gate missing drivers. State the
   smallest next authorized implementation slice after fixes, if any.

## Verdicts

Return exactly one:

- `LEVEL1_GATED_IMPLEMENTATION_ACCEPTED`
- `REVISE_LEVEL1_GATED_IMPLEMENTATION`
- `BLOCKED_LEVEL1_SCIENTIFIC_CONTRACT`

Lead with Critical/Major/Minor findings and file:line references. List mandatory
edits, tests you independently ran, and the exact next gate. Acceptance permits
only committing reviewed code; it does not authorize the public-root draw,
real panel generation, feasibility/scout execution, N3 selection, lock, escrow,
learner trajectory or outcome.
