# GPT-5.6 Sol Y-line review: Officina WP-3 finite-frame contract v1

Work in `/home/master/llm_projects/philosophia`. Review the committed WP-3
draft at commit `2bc781d` against the signed charter and author selections.
The later commit containing this prompt must differ from `2bc781d` only by
review prompts. Read the repository, not only this prompt.

Create exactly one new file:

`reviews/sol_officina_wp3_population_contract_review.md`

Do not edit existing files and do not commit. Do not create entropy, a world,
sample, panel, candidate, ledger event, root, lock, escrow artifact, datum, or
outcome. Do not activate T or execute any T/Q/C process. Read-only arithmetic,
static checks, tests, and the inactive bootstrap verifier are permitted.

## Governing files

- `successor/CHARTER_V2_DRAFT.md`
- `successor/CHARTER_V2_1_CORRECTION.md`
- `successor/CHARTER_SIGNATURE.md`
- `successor/AUTHOR_SELECTIONS_V1_SIGNATURE.md`
- `successor/OFFICINA_WP1_WP2_CLOSURE.md`
- `successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V1_DRAFT.md`
- `reviews/fable_officina_wp3_population_contract.md`

The fixed-finite-frame probability-sample interpretation is signed and closed.
CH-1 and CH-2 remain unselected proposals.

## Review mandate

Take an adversarial statistical/design-based stance. Decide whether the draft
defines a coherent finite-population estimand and sampling design under both
CH-2 branches, and whether a future non-comparative Q pass can license C spend
without entering the C evidence.

Audit at least these surfaces:

1. **Recompute membership and weights under both splits.** Under Split-1,
   `b_p={24+2p,25+2p}` and `j in {2,4}` imply Q worlds
   `{28,29,32,33,38,39,42,43,48,49,52,53,58,59,62,63}`. The printed list differs
   and overlaps printed C membership. Determine all consequences. For CH-2b,
   independently derive `N_h`, Q reserve size, `W_h`, admissible `n_h`,
   inclusion probabilities, and FPC. Require branch-complete formulas rather
   than values that are true only for the recommended split.
2. **Define the finite population precisely.** The frame unit is an unordered
   adjacent block, but the observed potential outcome depends on a randomized
   target/donor orientation. Decide whether the estimand is over blocks,
   block-orientation pairs, or the orientation-averaged block outcome. Check
   whether one realized orientation per sampled block identifies it and whether
   the variance must include both SRSWOR and orientation randomization. Require
   a single explicit two-stage design if needed.
3. **Small-stratum inference.** Analyze `N_h=3` (or 2 under CH-2b) with
   `n_h` possibly 1. Determine when design variance is identifiable, what
   happens at census, whether zero estimated variance can be narrated, and
   whether WP-3 must exclude any sample sizes before WP-9 chooses final N.
   Distinguish an exact finite-frame fact from a t/asymptotic approximation.
4. **Censored outcome estimand.** Check whether
   `[0,B] U {censored-at-B}` is mathematically single-valued and compatible with
   the intended restricted-mean/budget-to-competence contrast. Require WP-3 to
   freeze only the outcome type it owns while leaving WP-9 endpoint numerics
   open.
5. **Q-to-C spendability.** Q samples single worlds; C samples paired blocks and
   first exercises donor/yoke machinery. Decide whether declared within-stratum
   exchangeability of deterministic, publicly enumerated moduli is a coherent
   design premise, an untestable author assumption needing a token, or
   insufficient to license C. State what Q must cover to establish target-side
   competence without testing the treatment contrast and without becoming C
   evidence.
6. **Selection and exhaustion.** Check global Q sampling without replacement,
   serial first-valid promotion, E2=12, and the structural reserve inequality.
   Do not choose WP-6 caps or alpha spending, but determine whether either CH-2
   branch makes the signed selection procedure infeasible or silently changes
   the selection-conditional estimand.
7. **Heterogeneity and multiplicity.** Decide whether putting every
   claim-bearing stratum statement in C1 is correct when later C2-C5 may use
   their own frames and families. Separate descriptive finite-frame strata from
   inferential interaction claims and prevent post-hoc subgroup narration.
8. **Claim boundary.** Verify that design-based generalization is exactly to the
   registered C frame, not to Q, T, the 40-world pre-partition set, or a
   superpopulation. Check whether the public deterministic Q/C partition creates
   a finite-frame selection effect that the proposed weights do not address.
9. **Author cells.** Evaluate CH-1 and CH-2 as pre-data scientific choices. State
   whether their recommendations have non-outcome provenance and whether any
   additional bounded author token is required for the Q-to-C transport premise
   or orientation estimand.

## Required output

Lead with exactly one verdict token:

- `OFFICINA_WP3_YLINE_ACCEPTED_FOR_AUTHOR_SELECTION`; or
- `REVISE_OFFICINA_WP3_CONTRACT`; or
- `BLOCKED_OFFICINA_WP3_CONTRACT`.

Then provide findings ordered Critical/Major/Minor with file and line anchors;
the corrected formulas for both CH-2 branches; exact mandatory repairs; a clear
answer on orientation randomization and `n_h=1`; a clear answer on whether the
Q-to-C premise is sufficient for spendability; and negative space. If revision
is required, authorize only bounded Fable revision, not author selection, WP-4,
entropy, or execution. If accepted, state which author tokens become eligible
without signing them.

Do not predict qualification, contrast direction, or any scientific outcome.
