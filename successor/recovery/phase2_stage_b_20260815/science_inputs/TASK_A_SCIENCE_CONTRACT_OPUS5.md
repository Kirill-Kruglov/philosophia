I'll read the source documents first.

# SCIENTIFIC_CONTRACT_V1

Independent scientific-method review, 2026-08-15. Read-only. Sources: status meeting 20260815, `ascesis/{README,IDEA_GATE}`, lines 12–13, `essay/{climbing-the-wall-of-experience,OUTLINE}`, `successor/dev/{B2_PATH_VS_DESTINATION_DESIGN_V2,B2_PILOT_08,PHASE1_TERMINAL_18,PHASE2_POST_REVIEW_DRIVER_DECISION_19,WALLB_POLICY_CHANNEL_AUDIT_14B(_PREREG)}`, `/tmp/PHASE2_STAGE_B_L2_*`.

---

## 1. Claim stack E/B/S

**E (programme, existential).** *There exists some world family, some learner class and some finite budget for which a learner earns a transferable reduction in future work from contact whose selection depends on its own state, beyond matched contact selected by another process.*

**B (bounded primary, next experiment).** *In the frozen audit-14b equational presentation family (world family), for CPU linear-logistic ranking policies trained from scratch as exact twins (learner class), under one frozen `best_first` frame with per-presentation calibrated work budget `B` and one selected batch followed by one aggregate update (budget), the reciprocal block contrast `D_j` on held-out evaluation-panel search work (endpoint) is positive by at least the registered margin.*

**S (stronger, not authorized now).** *For the same learner class, the advantage of own-state-selected contact persists on fresh presentations not used for selection or fitting (transfer), and is carried by a truthful retained record of that contact rather than by weights alone or by a size- and format-matched false record (retention).*

| level | world family | learner class | budget | endpoint |
|---|---|---|---|---|
| E | unrestricted | unrestricted | unrestricted | unrestricted |
| B | 40-unit audit-14b frame, screen-qualified subset (12/40, Wilson [0.181, 0.454]) | CPU linear logistic ranker, exact-twin pairs | frozen `best_first`, per-world `B` at CONTROL solve rate 0.40 ± 0.05; one selection + one update | restricted-mean ISWU work and solve rate on the disjoint evaluation panel |
| S | B's family **plus** fresh presentations drawn under the frame's frozen sampler | as B | as B, plus retention factor | as B, evaluated cross-presentation |

**Why no finite negative falsifies E.** E has the form `∃(w, l, b). P(w, l, b)`. A run evaluates `P` at one tuple. `¬P(w₀, l₀, b₀)` is consistent with E for every other tuple, so no finite negative can contradict it; E is confirmable by a single positive instance and unfalsifiable by any number of negatives. Only the universally quantified restriction inside a named cell — B — is falsifiable. The practical consequence is the stop rule in §7: after a negative B, "try a bigger model / longer budget / richer world" is not a repair, it is the beginning of an unbounded search for a witness to E, and it must be refused prospectively rather than resisted in the moment.

## 2. What is already earned

| item | register | precise content |
|---|---|---|
| Same-wall token channel (line 12) | **scientific, bounded** | correlated wrong-value failures expose shared derivation; H4 falsified world-portability of the token+journal blade |
| Modular-addition grokking (Level 0) | **replication, platform only** | 5/5 seeds, locked; no programme inference |
| Level 1 contact test | **process only** | `BLOCKED_LEVEL1_FEASIBILITY`; ACTIVE/YOKED never compared |
| B2 walk-world path manufacture | **void by construction** | invariant is `#R − #L`; pilot `M3_PASS=False`, five design bugs |
| Equational **library** carrier | **closed, sparse** | 2/40 vs preregistered 5 |
| Equational **policy** carrier | **development-valid instrument** | hard-oracle positive control fires (0.31→0.62, `p=1.2e-15`); learned ranker qualifies 12/40 under Holm + bootstrap |
| MINIMO Phase 1 | **artifact property** | ck1 saved 882.87 entered MCTS iterations on 30 items, one CPU-debug realization; explicitly no population/stability/SELF-YOKED claim |
| Phase-2 Stage A | **feasibility** | strict interface, 126/126 |
| Phase-2 Stage B L0–L2 | **feasibility** | schema, checker, generator + code gate accepted on excluded fixtures; **no element generated, no science** |

Nothing above is evidence for or against E. Feasibility artifacts (Stage A/B, Phase 1) are engineering acceptance, not results.

## 3. Primary estimand and controls

Recipient state `r ∈ {A, B}` (exact independently seeded twins), batch source `q ∈ {A, B}` (which twin's state scored a common verified reservoir). Work outcome `X_{r←q}` (lower is better).

`D_j = mean_g[(X_{A←B} − X_{A←A} + X_{B←A} − X_{B←B}) / 2]`, registered stratum weights; one twin pair with all four valid branches = one independent unit.

**Why ACTIVE vs RANDOM-STATIC does not identify the effect.** That contrast varies three things at once: the marginal difficulty distribution of the selected batch, the realized answer information, and the state-match. A one-directional yoke fixes the batch content but not the donor's systematic quality (a stronger donor's batch is better for everyone). Only the reciprocal form cancels: additive recipient competence and additive batch quality drop out algebraically; the residue is the recipient×source interaction, which is exactly "selected by *this* state."

| target contrast | arm | isolates | status in B |
|---|---|---|---|
| own-state selection | `X_{A←A}`, `X_{B←B}` | state-matched contact | **in B** |
| honestly yoked / donated | `X_{A←B}`, `X_{B←A}` | same selector, wrong state | **in B** |
| weights-only retention | recipient keeps weights, record withheld | history-in-parameters | **deferred to S** |
| truthful ledger retention | weights + verbatim record of own contact | history-as-record | **deferred to S** |
| false / content-destroyed ledger | weights + size- and format-matched shuffled record | rules out format/volume effects | **deferred to S** |

Retention is a second factor crossed with selection; folding it into B triples the block count and is the main reason B is scoped to selection only.

**Mandatory controls, all prospective.**

| control | fails ⇒ |
|---|---|
| COLD-SELF zero-divergence (identical cold twins select identically ⇒ `D ≡ 0`) | harness bug, run INVALID |
| state-divergence gate (twin selections differ by a registered floor on a disposable block) | cell cannot host the estimand for this learner class; **do not scale** |
| injected-coupling synthetic fixture (recovers a known positive `D`) | analysis cannot detect the effect it claims to test; INVALID |
| statement-only surface predictor (selection value beyond length/n-gram features) | selector route closes; no post-outcome replacement |
| exact replay / metamorphic determinism (same state + same batch ⇒ byte-identical outcome) | design invalid, returns to statistical review |
| attrition ledger, whole-block retry, no replacement seeds, worst-case missing-`D_j` bounds | run INVALID |

**Named residual confound, not removed by the reciprocal design.** If selection produces difficulty-matched batches, a positive `D_j` shows contact value is state-dependent, not that the state carries anything epistemic. B claims the former only.

## 4. Route comparison

| | **R1 — resume B2** | **R2 — Phase-2 reciprocal slice** | **R3 — smaller compositional cell** |
|---|---|---|---|
| exact claim answerable | whether a positive-only road-equivalence objective builds usable structure in the walk world | B, in the erased-proof-plan MINIMO carrier | B, in the equational policy cell |
| identifiability | **absent**: the class invariant of the road-equivalence *is* `#R − #L`, a linear readout of input token counts; the non-trivial factor `n` is invariant under every road the mind can lay | adequate in principle; contingent on a selector that must first qualify, and on the carrier not being cheap for a complete prover | adequate; word-problem normal forms are not counting functions of the input, so the compositional invariant is non-trivial |
| smallest decisive measurement | none — the obstruction is analytic, not empirical | one complete disposable block, after L3+L4+Stage C exist | state-divergence probe on one disposable presentation (hours) |
| invalidity conditions | already invalid: `M3_PASS=False`, `sign(d)=1.0 at init`, `d_within_len=nan`, VICReg stalled 15–18 vs 22 | selector qualification fails; `COMPILER_FAMILY_UNREACHABLE`; complete prover makes the fragment cheap; twins not byte-replayable | twins do not diverge; injected-coupling fixture not recovered; frame drift |
| remaining engineering | modest (repair `M_PATH`, probe layer) — and it buys nothing | **largest in the project**: L3 identity annex + code, L4 compiler, root minting, Stage C selector qualification, scientific harness, coupling fixture, blocks; each gated on X/Y review | reciprocal harness + preregistration on an instrument already calibrated and powered |
| scientific failure mode | measuring a void quantity with a repaired instrument; sunk cost mistaken for progress | months of accepted paper contracts that terminate on a selector or prover verdict, with no measurement of the scientific question; the design-circling signature the project's own rules name | learner class too weak to be interesting; boundary result reads as "linear rankers don't have enough state," not as a claim about learners |

**VOID BY CONSTRUCTION stands; I cannot refute it.** A counterexample would need a road-equivalence in the walk world whose class invariant is *not* a function of an input-visible statistic. There is none: roads are rearrangements of a word, rearrangement preserves `#R − #L` exactly, and `#R − #L` is already in the input. Every modulus survives every rearrangement, so no self-generated road distinguishes one. This is a theorem about the cell, and the pilot corroborates it — `sign(d) = 1.0` at initialization, before any training. Bug #4 (VICReg under-trained) is a real instrument defect; repairing it makes the instrument correctly measure a quantity the design cannot contain. **R1 is refused on identifiability, not on its pilot's failure.** Note the contrast that selects R3: in the equational cell the analogous invariant is a rewriting normal form, which is not a counting function of the input.

## 5. Selected route

**R3 — smaller compositional cell**, instantiated as the **existing audit-14b equational policy cell**, not a newly constructed proof-DAG world.

Deviation from R3 as posed, stated plainly: reusing the frozen `best_first` frame is strictly cheaper than building a new world and preserves R3's intent. The instrument already has what neither alternative has — a positive control that fires, a per-world calibration procedure, a Holm-corrected screen, and a measured base rate (12/40) with which to power the block count.

Grounds, in order: (i) R1 is analytically void; (ii) R2's decisive measurement is unreachable without the largest remaining build in the project, and can be closed *after* that build by a selector or prover verdict; (iii) R3's decisive measurement — do twins diverge enough to select differently — costs hours and gates everything downstream. IDEA_GATE rule 5 selects R3. Sunk cost in Stage A/B and elegance of the erased-proof-plan carrier are not evidence and were not counted.

**Named cost of choosing R3.** The equational cell's library carrier is closed as sparse (2/40), so this cell cannot host S's retention arms in their compositional-reuse form. B is answerable here; S is not. Stage A/B remain accepted paper contracts, frozen and resumable, not deleted.

## 6. Outcome/invalidity decision table

| outcome | condition | reading |
|---|---|---|
| **POSITIVE SUPPORT** | all controls green; `D_j` lower confidence bound above the registered margin | B holds in this cell; E gains one witness; nothing about scale, transfer, or retention |
| **BOUNDED FALSIFICATION** | all controls green; `D_j` upper confidence bound **below** the registered margin | in this world family, learner class, budget and endpoint, own-state selection carries no advantage over honestly yoked contact. E untouched |
| **INFORMATIVE BOUNDARY** | controls green; interval spans the margin at the registered block count | effect, if present, is smaller than the preregistered margin; publish the interval; do not extend the run |
| **INVALID / UNRESOLVED** | any of: COLD-SELF nonzero; state-divergence gate fails; injected-coupling fixture not recovered; replay non-determinism; surface predictor explains selection; attrition beyond the registered bound; ranker fails to reach calibration on its own panel | says nothing about B or E; a failed learner or a failed positive control is an instrument verdict |

A ranker that never learns, a frame that fails calibration, or twins that never diverge are **INVALID**, never evidence against the scientific claim.

## 7. Stop rule

Registered before any run, prospective, one page, signed:

1. **Gate 0 (hours).** Disposable state-divergence probe on one excluded presentation. If twins select batches whose overlap exceeds the registered ceiling, the branch ends as `CELL_CANNOT_HOST_ESTIMAND_FOR_THIS_LEARNER_CLASS`.
2. **Gate 1 (one block).** Injected-coupling fixture must recover a known positive `D`. Failure ends the branch as `ANALYSIS_CANNOT_DETECT_ITS_OWN_EFFECT`.
3. **The call.** One preregistered block count sized from the 12/40 base rate and one registered margin. Executed once.

**What ends this branch without rescue.** A **BOUNDED FALSIFICATION** or an **INFORMATIVE BOUNDARY** at the registered block count terminates the own-state-selection line. It may not be followed by a larger ranker, a neural policy, a longer budget, more blocks, a richer presentation family, or a return to MINIMO "because the cell was too small." Any of those is a new line requiring its own IDEA_GATE pass and its own contract. The margin, block count, endpoint and stratum weights are frozen before the first scientific block and may not be changed after any outcome exists.

## 8. Claims explicitly not authorized

- No claim about E from any outcome of B.
- No claim that experience "transfers," "compresses," or "shortens work on new families" — S is not run.
- No claim distinguishing weights-only, truthful-ledger and false-ledger retention — that factor is not in B.
- No claim about autonomous conjecture invention, theorem discovery, curriculum self-design, or information acquisition; the construct is self-calibrated selection from a supplied verified reservoir.
- No claim about neural learners, larger models, or scale.
- No essay slot (4a–4d) is filled or discharged by B.
- No upgrade of Stage A/B/Phase-1 feasibility artifacts to scientific results, and no MINIMO effect size inferred from Phase-1's single realization.
- No claim that the walk world, the library carrier, or MINIMO cannot host the question — R1 is void for its design, R2 is deferred on cost, and both remain resumable.

---

SCIENTIFIC_ROUTE=SMALLER_COMPOSITIONAL_CELL
