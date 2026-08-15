# INDEPENDENT SCIENTIFIC REVIEW — PHILOSOPHIA_MINIMUM_CAUSAL_CONTRACT_V1

Read-only. No code, files, roots, runs, or commits were produced. Route decisions listed as adjudicated were not reopened.

**Scope limitation to record up front:** the five `/tmp/PHASE2_STAGE_B_L2_*` / `L3_*` files named as the accepted engineering boundary **do not exist on disk** (`/tmp` contains none of them; they are not committed anywhere in the repo). I reviewed the contract against the durable pins — driver decision 19, the line-13 ontology, IDEA_GATE, the essay, and the three prior findings. Finding M10 addresses the consequence.

---

## CRITICAL

### C1 — Stage-H design may legally be fixed after Stage-R outcomes exist

**Sections:** §5 first sentence; §6 last paragraph; §12 bullet 6. No section anywhere requires sealing.

**Consequence.** §5 defers H *implementation* until "Stage R reaches its prospectively defined positive terminal." §12 defers H's access budget, work-to-threshold definition, transfer families and representation change to `AUTHOR_CHOICE_BEFORE_IMPLEMENTATION`. Under the plain reading these compose to: *H's endpoint, treatment, population and margin are chosen after Stage-R's result is known.* That is precisely outcome-dependent redesign. It is worse than an unregistered H, because §1 presents H as a registered bounded claim. Compounding this, the contract contains **no sealing requirement at all** — driver §3.10's "sealed outputs" was dropped (see M1) — so there is no mechanism that could enforce a pre-unseal freeze even if intended.

**Smallest repair.** Insert a new §5.0:

> All Stage-H design quantities are frozen, signed and sealed **before the first Stage-R scientific block is run**, and may not be altered after any Stage-R outcome is unsealed. The frozen set is exactly: (i) the arm list (§5, as disambiguated); (ii) the truthful- and false-history transformations, as named algorithms; (iii) access and byte/token budgets; (iv) held-out family identities and their disjointness criterion; (v) the representation transformation, as a named map; (vi) primary and companion endpoints; (vii) the margin and decision rule; (viii) the independent unit; (ix) the analysis, attrition and missing-data rules. Disposable Stage-H calibration is permitted only on split-disjoint disposable data and must complete before the first Stage-R scientific block. `work-to-threshold` is registered as a **functional of a named reference arm** (e.g. a fixed quantile of the weights-only arm's own held-out curve), never as a numeral chosen later. No Stage-R scientific outcome may enter any Stage-H choice.

If the author is unwilling to pay that cost now, the equivalent bounded alternative — and the cheaper one — is to **demote H**: delete H from §1's claim stack and from §9, and state that Stage H is an unregistered conditional successor requiring its own prospective contract, itself signed and sealed before any Stage-R outcome is unsealed. R then stands alone, which the contract already permits (§3, §10).

**Changes route?** No. **New implementation?** No (text only; alternative (a) front-loads H design authoring, alternative (b) removes it).

### C2 — `R_BOUNDED_NEGATIVE` has no prospective margin or decision rule

**Sections:** §9 rows 1–3; §6 paragraph 3; §1 line 21.

**Consequence.** §9 defines the positive terminal as "registered `D_j` positive terminal met" and the negative terminal as "registered negative/null terminal met," but neither terminal is defined anywhere in the contract, and §6 defers only "threshold, margin, block count." With no equivalence/futility rule, the default reading of a null run is *failure to reject a positive effect*, which the contract would then publish as "own-state-selection branch closes in this cell" (§9) and which §10 makes irreversible ("R null/negative closes the own-state-selection branch"). An underpowered run would thereby terminate the line's central question on absence of evidence. This was correct in the earlier `SCIENTIFIC_CONTRACT_V1` (upper confidence bound below the registered margin) and was lost in V1 of this contract. Related wording defect: §1's R sentence quantifies the claim "by the prospectively registered Stage-R **endpoint**" — an endpoint is the measured quantity, not a decision threshold, so R as written names no effect size at all.

**Smallest repair.** Add to §6 and rewrite §9's first three conditions:

> A margin `δ > 0` on the registered analysis scale, a two-sided interval procedure, and the block count are registered before the first scientific block. Terminals: `R_POSITIVE` iff the lower bound of the interval for `D` exceeds `δ`; `R_BOUNDED_NEGATIVE` iff the upper bound lies below `δ` (an equivalence/non-inferiority decision, never a failure to reject); `R_INFORMATIVE_BOUNDARY` iff the interval spans `δ` at the frozen `N`. Absence of a significant positive effect is never, by itself, `R_BOUNDED_NEGATIVE`.

And in §1, replace "by the prospectively registered Stage-R endpoint" with "by at least the registered margin `δ` on the population-mean block contrast `D`." Apply the same margin construction to §9's four `H_*` rows.

**Changes route?** No. **New implementation?** No.

---

## MAJOR

### M1 — Prospective-integrity controls from driver §3.10 dropped; no exclusion import

**Section:** §4 bullet 7.

Driver 19 §3.10 mandates "whole-block retry, attrition ledger, no replacement seeds, worst-case missing `D_j` bounds, **balanced branch/evaluation order, sealed outputs, and block-level inference**." §4 carries the first four and silently drops the last three. Sealed outputs is the mechanism C1's repair depends on; balanced branch/evaluation order is what prevents order effects from entering `γ`; block-level inference is what stops theorem-level `N` inflation the contract forbids elsewhere (§11). Separately, Cursor's audit required "exclusion import" in any min-slice contract: the six L2 gate fixtures and every calibration item are permanently ineligible for science, and §7's "small sealed scientific reservoir and held-out panel" states no exclusion rule.

**Repair.** Restore the three dropped clauses verbatim to §4, and add to §7: "the sealed reservoir and held-out panel exclude every item used in any L0–L2 gate, generator calibration, selector qualification, divergence probe or injected-coupling fixture; the exclusion list is imported and hash-pinned before sealing." Add that whole-block retry triggers are control-based and evaluated blind to `X`.

**Route?** No. **Implementation?** No new component; constrains sealing procedure.

### M2 — Capping censors the endpoint, so the additive cancellation is only approximate

**Sections:** §3 (estimand); §6 (primary endpoint).

The cancellation is real and I re-derive it below, but it holds on a scale where `X` is additive. The registered primary is **capped** entered MCTS iterations, i.e. `X = min(W, C)`. Censoring is nonlinear: a branch with more mass at the cap has compressed differences, so differential censoring between branches produces a nonzero `D_j` with no interaction present, and equally can mask one. §3 asserts the cancellation without stating either the algebra or the scale assumption.

**Repair.** Add to §3: the additive-cancellation derivation; a statement that cancellation of the batch-source effect is a *between-recipient* cancellation requiring additivity on the registered analysis scale; a requirement to report per-branch censoring (cap-hit) rates; and a prospective rule that differential censoring beyond a registered bound forces `R_INFORMATIVE_BOUNDARY` or `R_INVALID` rather than a positive reading.

**Route?** No. **Implementation?** No — cap-hit counts and solve rate are already mandatory companions (§6).

### M3 — The named residual confound was deleted

**Section:** §3, final paragraph.

`SCIENTIFIC_CONTRACT_V1` §3 named it explicitly: if selection produces difficulty-matched batches, a positive `D_j` shows contact value is **state-dependent**, not that the state carries anything epistemic. This matters because difficulty×competence is an *interaction* and therefore does **not** cancel — it is a fully admissible mechanism for a positive `D_j`. §3 of the present contract says only "bounded recipient-state-specific task value in this cell," which a reader will over-read. §11 forbids "autonomous conjecture invention" but not the epistemic-content reading.

**Repair.** Restore one sentence to §3: "A positive `D_j` is consistent with the selector matching item difficulty to recipient competence. R does not distinguish that mechanism from any epistemic one, and no such distinction may be claimed." Add the corresponding bullet to §11.

**Route?** No. **Implementation?** No.

### M4 — Stage-H arms: "weights-only" and "no-history" are ambiguous, and the scratch reference is missing

**Section:** §5 (arm list vs. control list).

The arm list names three arms; the control list names "weights-only **and** no-history baselines" as if they were two. As stated they are the same arm. Two readings, with different identification consequences: if "no-history" means a scratch (no inherited weights, no history) arm, then `H_WEIGHTS_ONLY` in §9 — "inherited weights explain the benefit" — is identified; if it is a duplicate name, `H_WEIGHTS_ONLY` has no no-inheritance reference and cannot be concluded.

**Repair.** Name the arms explicitly and state which are required: `A0` scratch (no weights, no history) as the reference for any weights-only conclusion; `A1` weights-only; `A2` weights + truthful history; `A3` weights + matched false history. Delete the duplicate control-list phrasing.

**Route?** No. **Implementation?** Adds one Stage-H arm if `A0` is required; nothing before Stage R.

### M5 — The false-history arm is not constrained to be well-formed or non-self-revealing

**Section:** §5, arm 3 and control 3.

"False, permuted or content-destroyed history with identical public schema and interface" is matched on *schema*, not on *well-formedness*. A permuted or content-destroyed derivation ledger is typically an ill-typed, self-evidently contradictory derivation: it reveals arm identity, and it acts as a poison rather than a neutral control, so `H_LEDGER_FORM_ONLY` versus `H_TRUTH_SPECIFIC_TRANSFER` becomes unidentifiable. "Content-destroyed" is in direct tension with "matched in public form." The transformation family is a *design decision*, not a numeral, and is currently deferred by §12.

**Repair.** Add to §5: the false-history transformation must be a named algorithm producing records that are schema-valid, individually well-formed, and free of trivial contradiction — e.g. truthful verified records drawn from a disjoint, unrelated theorem set (mismatched-but-true), rather than token permutation of the recipient's own records; and register a disposable arm-identity discriminability probe (a classifier must not separate `A2` from `A3` records beyond a registered ceiling) run before Stage H. Fold the choice of transformation into C1's frozen set.

**Route?** No. **Implementation?** Nothing before Stage R; constrains the Stage-H build.

### M6 — Dependency contradiction: held-out validity needs the split machinery §7/§8 defer

**Sections:** §7 required list; §8 deferral 3.

Driver 19 §3.9 requires that "carrier splits are canonical rule-skeleton-disjoint." §8 defers "universal skeleton-collision economy **except reservoir-local needs**," but §7's required list contains no skeleton-identity component at all, and Cursor's disposition table classifies rule-skeleton identity as DEFER. Without reservoir-local skeleton identity, the "held-out panel" may be re-skinned reservoir items, and R's endpoint measures memorization of the frame rather than held-out work. This is the concrete dependency contradiction: **split disjointness** silently requires a deferred component.

**Repair.** Add to §7's required list: "canonical rule-skeleton identity computed over the sealed reservoir and held-out panel only, sufficient to certify split disjointness." Narrow §8's deferral to "skeleton-collision economy and quota-filling beyond the sealed reservoir."

**Route?** No. **Implementation?** Yes — small, and scoped to the sealed set rather than the universal catalogue.

### M7 — Deferring the complete-prover frame audit is not accompanied by its inferential price

**Sections:** §8 deferral 5; §11.

Driver 19 §3.9 makes a complete subformula-bounded normal-form prover a **frame-acceptance** condition and states the claim remains instrument-relative if a complete prover makes the fragment cheap. §8 defers the G4ip/inverse audits procedurally (ratification required) but never states the consequence. If the fragment is trivially decidable, "reduces held-out capped entered MCTS work" is a statement about one search algorithm's inefficiency on an easy fragment, not about acquired competence.

**Repair.** Add to §8 and §11: "Deferring the complete-prover frame audit makes every Stage-R result explicitly instrument-relative. No claim that the measured work reduction reflects theorem difficulty, or generalizes beyond the MCTS prover as configured, is authorized." (Alternative, at real cost: reinstate the complete-prover check as a §7 requirement.)

**Route?** No. **Implementation?** No, under the claim-restriction option.

### M8 — Companions are not forbidden from replacing the primary after outcomes

**Section:** §6.

Driver 19 §3.5 states companions "cannot replace the primary after outcomes." §6 lists them as mandatory but omits the prohibition, while explicitly allowing the primary itself to be superseded by "an accepted driver … before implementation" — asymmetric protection.

**Repair.** Append to §6: "Companion endpoints are reported in every outcome and may not replace, rescue or reinterpret the primary after any outcome exists."

**Route?** No. **Implementation?** No.

### M9 — The stop rule does not close the review loop as specified

**Section:** §10, bullets 1–3.

"One authoring pass and one independent contract review. At most one bounded repair pass. **No fourth general review.**" The arithmetic is loose — "no fourth" does not forbid a third — and nothing restricts post-repair confirmation to the repaired blockers, which is the exact gap through which the project's named design-circling failure mode returns (IDEA_GATE termination rule).

**Repair.** Replace with: "This review is the last general scientific or architecture review of this contract: `GENERAL_REVIEWS_REMAINING=0`. At most one bounded repair pass is authorized, addressing only the enumerated blockers. Confirmation after repair is limited to verifying those enumerated repairs and may not raise new findings. Any request for a further general review is refused; disagreement is resolved by author ratification, not by another reviewer."

**Route?** No. **Implementation?** No.

### M10 — Authority pins are non-durable, and required L3 has no timed kill

**Sections:** §7 bullet 1; §10 bullet 4.

The five annexes constituting the accepted engineering boundary exist only in `/tmp` and are gone; none is committed. The line-13 ontology records Stage-B L2 as **grey** (joint code review not complete), and Cursor's audit records that L3 annex v1 is **not review-ready** (driver D1–D5 open). Yet §7 makes "L3 alpha-canonical public identity and sealed public projection" a Stage-R prerequisite, and §10's three-day timed kill covers **only** L4. The single largest-cost prerequisite whose paper boundary is not accepted is therefore the one component with no bounded exit.

**Repair.** (i) Add to §7/§8: "Annex identity is pinned by SHA-256 in a durable committed location; a pin that cannot be resolved suspends the contract." (ii) Extend §10: "L3 repair to the projection-only subset actually required must be accepted within a bounded, registered window; failure closes the MINIMO route on the same terms as the L4 kill."

**Route?** No. **Implementation?** No new component; adds a durability/pinning obligation and a deadline.

---

## MINOR

1. **§0/§10 — E's asymmetry unstated.** E is unfalsifiable by any number of negatives *and confirmable by a single witness*. §10's "No result universally proves or falsifies E" understates the first half and misstates the second; state the asymmetry so bounded negatives are legible as what they are.
2. **§4 — divergence failure is not a bug.** Below-floor acquired-state divergence is a substantive verdict about the learner class in this cell, not `R_INVALID`. Give it its own terminal (`CELL_CANNOT_HOST_ESTIMAND_FOR_THIS_LEARNER_CLASS`) and state it is publishable.
3. **§4 — qualification data not pinned.** State that divergence measurement, selector qualification and injected-coupling all run on disposable, split-disjoint data, never on the sealed reservoir/held-out panel, and never using scientific outcomes.
4. **§4 — projection sealing is not an R control.** Add: "the learner and selector observe only the sealed public projection; any plan, band, root, or witness leakage → `R_INVALID`."
5. **§12 — envelope chronology.** Driver §3.12 requires pinning the envelope only after one complete disposable block; say so, and say it is pinned before the first scientific block.
6. **§12 — injected coupling.** Register the injected effect magnitude, not only the recovery threshold.
7. **§8 — no terminal for refusal.** State what happens if the author declines to ratify a deferral (the component re-enters §7 as required, or the route closes).
8. **§3/§6 — frame-level scope.** With one sealed reservoir and one held-out panel, item/frame variance is not estimated; state that inference is conditional on the single sealed frame, with no frame-level generalization.
9. **§1 — H compute envelope.** H names an access budget but no compute envelope; add it or state it inherits the signed Phase-2 envelope.

---

## REQUIRED-CHECK VERDICTS

**1. Claim quantification — PASS with C2/M11-wording.** E existential and unfalsifiable-by-negatives (§0, §19); R bounded on world family, learner class, envelope and endpoint (§1); H conditional and not an automatic consequence of R (§1, §10 hierarchy). No wording converts a bounded negative into universal falsification (§9, §10) or a bounded positive into universal proof (§3, §10, §11). Defect: R names no effect size (C2).

**2. Reciprocal estimand — PASS on derivation, incomplete in text.** With `X_{r←q} = μ + ρ_r + β_q + γ_{rq} + ε`:

- `X_{A←B} − X_{A←A} = (β_B − β_A) + (γ_{AB} − γ_{AA})` — `ρ_A` cancels within recipient A.
- `X_{B←A} − X_{B←B} = (β_A − β_B) + (γ_{BA} − γ_{BB})` — `ρ_B` cancels within recipient B.
- Sum: the `β` terms annihilate across the two differences.
- `D_j = [(γ_{AB} − γ_{AA}) + (γ_{BA} − γ_{BB})] / 2`.

Since `X` is work and lower is better, `D_j > 0` ⟺ mismatched selection costs more ⟺ matched selection reduces work. **Sign convention confirmed.** Additive recipient competence cancels *within* each recipient's difference; additive batch-source quality cancels *between* the two differences — the latter is the assumption-heavier of the two (M2). One complete twin pair = one independent unit and theorems are repeated measurements (§3, §6): correct. All four branches required, no post-hoc replacement of invalid branches (§4): present. The estimand identifies recipient×source interaction only — correct, but the admissible difficulty×competence mechanism must be named (M3).

**3. R terminals — FAIL.** See C2.

**4. Selector identification — PARTIAL.** Surface masquerade (§4 incremental predictive value) ✔ but structural-stratum matching from driver §4 is not carried over; leakage ✖ as a control (Minor 4); recipient competence / batch quality ✔ algebraically, ✖ textually (M2); degenerate twins ✔ (§4, COLD-SELF); nondeterministic replay ✔ (§4). Divergence is measured before the scientific block and does not use scientific outcomes ✔, but the data restriction is unstated (Minor 3).

**5. Sequential R→H — FAIL.** See C1; the exhaustive freeze list and the disposable-calibration boundary are given there.

**6. Stage-H identification — FAIL.** See M4 (arm ambiguity, missing scratch reference) and M5 (false arm constructibility).

**7. Endpoint coherence — PARTIAL.** Capped entered MCTS iterations is legitimate as the assigned-work primary under driver §3.5; companions are not protected from post-outcome substitution (M8); censoring must be registered (M2); H's `work-to-threshold` is not prospectively definable as written (C1).

**8. Minimum engineering boundary — FAIL on one dependency.** Every §7 component is necessary for R. Deferred components are correctly out of the causal path **except** rule-skeleton identity, which split disjointness silently requires (M6); the complete-prover audit is legitimately deferrable only with a stated price (M7).

**9. Charter compatibility — PASS.** §8 treats deferrals as requiring explicit author ratification or boundary correction and does not silently override the charter; accepted L0–L2 predicates are unchanged and explicitly not upgraded to evidence. Gaps: no terminal for refusal (Minor 7), non-durable pins (M10), and §8's list should absorb M6/M7.

**10. Review-loop closure — FAIL.** See M9.

**11. Implementability after author choices — PARTIAL.** Classification of §12:

| Choice                                                                                                                                        | Class                                                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| R compute envelope; reservoir/held-out sizes; stratum weights; block count; selector thresholds; injected-coupling threshold; H access budget | legitimate prospective numerical/statistical                           |
| Selector qualification test set; branch/attrition/analysis rules; primary endpoint                                                            | derivable from driver 19                                               |
| R margin **plus its decision rule**                                                                                                           | missing (C2)                                                           |
| H `work-to-threshold` as a functional; H held-out family criterion                                                                            | missing (C1)                                                           |
| H false-history transformation family; H representation transformation                                                                        | **missing scientific design decisions — new treatments, not numerals** |
| Eight-root quota, 4×4 bands, universal skeleton economy, compiler catalogue, L3/L4 extensibility                                              | unnecessary universality                                               |

For **Stage R**, filling the legitimate prospective choices requires no new treatment, endpoint, population or claim — the contract is implementable. For **Stage H** it does: the representation change and the false-history transformation are treatments that exist nowhere. This is why C1's repair must be resolved by *either* freezing those designs now *or* demoting H out of this contract's claim stack.

---

## DISPOSITION

Two Critical findings, both textual and both closable inside one bounded revision; no finding requires a route change, and only M6 adds implementation work (small, scoped to the sealed set). The contract's spine — the reciprocal estimand, its cancellation algebra, the independent unit, the R-before-H ordering, the deferral of Stage-B universality — is scientifically coherent and survives review. It is not yet closed, because a null Stage R would currently be publishable as a bounded kill without a margin, and Stage H's design is currently free to be written after Stage R's answer is known.

**BOUNDED_REPAIR_PHILOSOPHIA_MINIMUM_CAUSAL_CONTRACT_V1**

The repair pass is confined to: C1, C2, M1–M10, and the nine Minors. No new sections, no annex, no reviewer.

GENERAL_REVIEWS_REMAINING=0
BOUNDED_REPAIR_PASSES_REMAINING=1
IMPLEMENTATION_AUTHORIZED=NO
