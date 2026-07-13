Written to `reviews/opus_level1_spec_v2_sgate_review.md`.

## Verdict: `REVISE_LEVEL1_V2_SPEC`

v2 is a real advance, but I independently recomputed the arithmetic and **all three suspected contradictions are confirmed**, plus the panel algebra is impossible and several endpoint-determining values are still unset. Signing the S-gate now would freeze an inconsistent endpoint.

**Critical**
- **CR-A — the certificate's support arithmetic is self-contradictory (X2.1–2.3, all confirmed by enumeration):**
  - Reserved cells are `|d| ≤ 125`, but stratum-4 needs `d = 2n ∈ [132,250]` — every value exceeds 125, so the panel *cannot* be "built from reserved cells only."
  - `N2 = 125` gives max realizable `|d| = 250`, but the near-miss `2n+1 = 251` at `n=125` needs 251 → unrealizable. Correct floor: `2·N2 ≥ k_max·n_max + 1 ⟹ N2 ≥ 126`, **decoupled** from the acquisition cap `d_acq ∈ [125,130]`.
  - Reserving cells *within* each `|d|` class gives only syntactic novelty; since EQ depends only on `d mod n`, a difference-lookup learner passes everything except the uncontactable double-wrap stratum. The anti-lookup guarantee rests on **stratum 4 alone**, not the reserved partition.
- **CR-B — the panel table is algebraically wrong:** "YES/NO balanced within each residue class" is impossible (for fixed `n`, EQ is *constant* within a class — verified). And the sole anti-lookup stratum (`d=2n`) structurally requires the extreme-opposite displacement corner, so "certified solve" irreducibly conflates period-recovery with corner-extrapolation. I supplied a corrected 5-stratum panel table.
- **CR-C — endpoint/decision quantities unset** (calibration bound, ABSTAIN/confident-lie caps, panel counts, evaluator ensemble aggregation, interval method) so the S-gate can't be a rubber-stamp; and **non-finite block failures are outcome-correlated → must be censored, not excluded** (excluding + FPC biases toward non-diverging arms).

**Major**
- **The distance-1 donor is one-sided:** it strongly powers a *positive* C1 but a *null* is nearly uninformative (adjacent moduli give near-identical geometry). Level 1 is a detector, not a falsifier, of choice benefit — a Kirill decision.
- The `§1` scope label ("probe-**scale** adaptation") mislabels what distance-1 isolates (online **responsiveness**).
- Population inconsistency: §8 says "Ω (60 worlds)" but the estimator only touches ≤24 realized target worlds, and FPC degenerates to zero variance at `N3=24`.
- Architecture is an unjustified extrapolation from Level 0 (3-token grokking → 271-token, modulus-125 inputs); committee disagreement's "early signal" is oversold at random init.

I confirmed the cardinality (23,751 cells, ~33× headroom) and credited the genuinely-solid v2 constructions (adjacent-pair arithmetic, opaque index, salted escrow, sealed evaluator, side-effect-free scorer). The review gives full X1–X6 answers, mandatory revisions, a gate table, and a precise Codex authorization: gate-1 neutral substrate stays eligible **but `N2`/`d_acq`/zone bounds must be parameters asserting the corrected inequalities, not the current `N2 = d_acq = 125`**. **All Level 1 execution remains forbidden**; every signed negative destination is preserved. File is uncommitted per the pre-lock discipline.
