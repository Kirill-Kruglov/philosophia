# Fable 5 — Level 1 spec v2 closure memo

Author: Fable 5. Companion to
`experiments/level_1_contact/SCIENTIFIC_SPEC_V2_DRAFT.md` (v2), which
supersedes the v1 draft (preserved unchanged). Inputs: Opus X-line
(`REVISE_LEVEL1_SPEC`) and Sol Y-line
(`INFERENCE_SPEC_ELIGIBLE_FOR_CLOSURE`) formal reviews; the signed claim
graph and its v2/v2.1 corrections. The chat captures were treated as
provenance only. Governing-text check against HEAD performed: the Level 1
README and KILL_MATRIX row already carry the ACTIVE/YOKED/RANDOM design and
mediator treatment of answer entropy (verified by inspection), so Opus mn-5
is recorded **already closed**; no old language is reintroduced.

## Verdict

**READY_FOR_LEVEL1_S_GATE_REVIEW**

The v2 document is executable as a scientific contract: the world (registry,
pairing, strata, coverage inequalities), estimand (adjacent-donor yoke with
degenerate distance-1 distribution, assignment-conditioned scope), unit
(pair-block), endpoint (right-censored budget-to-certified-solve with the
first-qualifying-window convention and RMST-as-bounded-cost identity), arm
behavior (committee acquisition, side-effect-free scorer, without-replacement
selection, matched capacity/updates), decision rules (predicates, solve-count
floor, invalidity cascade, total selector), N3 precision rule and ceiling,
and escrow protocol are all closed with exact candidate values of stated
non-comparative provenance. The remaining blanks — final numeric
confirmations at signature, panel stratum counts and per-stratum thresholds,
seed schedule, leakage tolerances, the Bonferroni-vs-bootstrap choice, the
resource wall, and the realized `N3` — cannot change the world, estimand,
unit, endpoint, arm behavior, or decision rule: each is a value inside an
already-frozen structure, each is barred from comparative provenance by the
document itself, and `N3` is clamped by a frozen rule to a frozen ceiling.

## 1. Finding-by-finding disposition

### Opus X-line

| Finding | Disposition | v2 section |
|---|---|---|
| CR-1 n-supply vs stratum width vs donor distance | **Adopted, resolved by design change**: adjacent disjoint pairs fix donor distance at 1 (maximally conservative), supply arithmetic exact (30 pairs; `N3_max = 24`; `N_dev = 6`), overflow fork named (signed registry extension voiding scout, or `INSUFFICIENT`) | §2 |
| CR-2 raw-word cells wrong; two-level contract | **Adopted with one strengthening**: semantic cells offline-only; fixed multiplicity `m = 4`; flat opaque index to all arms. Strengthened per the v2-prompt: ACTIVE scores **opaque raw realizations** — Opus's "ACTIVE scores semantic cells" would itself leak the abelianization, so cell grouping is invisible to every policy and auditable only by the offline enumeration verifier | §3 |
| CR-3 certificate passable by difference-memorization | **Adopted, made provable**: registry `[66,125]` + pool support `|d| ≤ 125` makes the `d = 2n` stratum *uncontactable by construction* for every world; reserved-cell partition gives semantic held-out; per-stratum accuracy/ABSTAIN/confident-lie caps close the abstain-on-probes exploit; four anti-lookup proof obligations enumerated | §2, §7 |
| MJ-1 wrap-coverage closed form | **Adopted and strengthened** to the multi-period form `2·N2 ≥ k_max·n_max` (= 250, met) as the v2 prompt requires | §2 |
| MJ-2 C1 = probe-scale scope; distance mediator; width justification | **Adopted**: scope annotation in §1; distance degenerate at 1 by design, still reported; width justification replaced by the pairing construction | §1, §2 |
| MJ-3 single-head uncertainty degenerate pre-calibration | **Adopted**: committee disagreement (E = 4) replaces `|p̂ − ½|`; early-signal justification stated; calibration circularity dissolved | §5 |
| MJ-4 side-effect-free scorer; answered-pair rule | **Adopted**: no-grad/eval/state-hash contract; without-replacement selection uniform across arms; selection compute reported separately | §5 |
| MJ-5 plaintext hash = verification oracle | **Adopted**: encryption-only confidentiality; 256-bit secret salt inside ciphertext, released at outcome; sealed validator; isolated FS + wipe | §11 |
| MJ-6 evaluator sealed until authorization | **Adopted**: post-B evaluation over frozen checkpoints; panel/labels/thresholds/decisions sealed from researchers too | §7 |
| MJ-7 finite-population correction mandatory | **Adopted**: stratified FPC estimator committed; i.i.d. superpopulation reading rejected; scope = finite registered Ω, assignment-conditioned | §8 |
| mn-1 paired within-block init | **Adopted**: identical init per ensemble member across the three arms; domain-separated stochasticity only | §4 |
| mn-2 shortlist discipline | **Adopted**: seeded, learner-state-independent `S = 512` subsample, identical in law for target and donor ACTIVE; estimand-preservation argument stated | §3 |
| mn-3 control placement | **Affirmed**: dev-world design-invalidity gates; pre-contact vs post-contact line held | §10 |
| mn-4 assignment lock + FS hygiene | **Affirmed/adopted**: role assignment committed at S-gate; isolated FS + wipe in escrow | §2, §11 |
| mn-5 stale governing text | **Recorded already closed** (verified at HEAD); no reintroduction | this memo |

### Sol Y-line

| Finding | Disposition | v2 section |
|---|---|---|
| M1 event-time convention | **Adopted, closed**: first-qualifying-observation convention; window must complete by B; checkpoint-granularity interval convention stated | §8 |
| M2 finite-population model before N3 | **Adopted**: FPC model committed pre-N3; seed aggregation = block-arm mean before block-level inference | §8, §9 |
| M3 panel forces cyclic structure | **Adopted and strengthened** by CR-3's provable extrapolation stratum; all Sol S3 strata present; panel serialization leak-proofing under the escrow seal | §7 |
| M4 N6 = relevance margins, not scout products | **Adopted**: margins frozen at S-gate with a named mathematical anchor (stratum-scan cost, 60 queries); scout barred from margin provenance | §8 |
| m1 narrow estimand | **Adopted**: scope annotation (probe-scale adaptation vs adjacent-modulus active geometry) | §1, §2 |
| m2 RANDOM-superior anomaly | **Affirmed**: registered anomaly; selector unchanged; C1 never rewritten | §8 |
| m3 repeated-query rules | **Affirmed with a design choice**: all arms select without replacement (locked, uniform), repeat-cost rule retained for robustness | §3, §5 |
| S2 estimator family / assignment permutation not primary | **Adopted**: paired stratified FP mean of `min(T,B)`; permutations restricted to pre-treatment balance diagnostics | §8 |
| S5 N3 by precision, not invented effect | **Adopted**: frozen rule targeting simultaneous half-width ≤ N6/2, clamped to `[12, 24]` | §9 |
| S6 invalidity taxonomy | **Adopted**: four-class executable cascade; no silent exclusion; no blinded replacement (finite registry, selection risk) — excluded-with-record, floors, escalation count | §10 |
| Implementation boundary ("pool machinery now") | **Rejected in part, conservatively**: overridden by Opus CR-2 as the v2 prompt directs — pool/evaluator/learner wait for v2 review; only the neutral substrate is eligible now | §12 |

Nothing else in either review is unaddressed; the one partial rejection
(Sol's implementation boundary) is reasoned above and mandated by the
governing prompt.

## 2. Choices still requiring Kirill's authorial signature (at S-gate)

1. Confirmation (or amendment) of every candidate value: registry
   `Ω = [66,125]` + adjacent pairing + strata; `N_dev = 6`; `N2 = 125`;
   reserved fraction 30 %; `m = 4`; `S = 512`; `L_word = 135`; `B = 2,000`;
   `E = 4`; `U = 1`; `C = 50`; `W_p = 200`; solve-count floor; block-
   invalidity escalation count.
2. Per-stratum panel thresholds: accuracy, calibration statistic and bound,
   ABSTAIN caps, confident-lie caps; panel stratum counts.
3. N6-L1 margins from the named non-comparative anchors.
4. Simultaneous-interval method: Bonferroni (default) vs studentized block
   bootstrap.
5. Seed schedule and leakage-gate tolerances; the outcome-independent
   resource wall.
6. The overflow fork policy if `N3 > 24` or the solve-count floor is
   infeasible at `B` (registry extension vs `INSUFFICIENT`).
7. Acceptance that the C1 verdict is scope-annotated as probe-scale
   adaptation against adjacent-modulus donors (the honest-scope clause).

## 3. Negative space: what Level 1 can never establish

- Not manufactured experience, `PROOF_CORE`, or any C2–C6 node — in either
  direction. A Level 1 success is **never** evidence for `PROOF_CORE`.
- Not "active learning works/fails" in general — only the locked family,
  learner, committee rule, budget, and adjacent-donor contrast.
- A C1 negative is `BOUNDARY_CONTACT_CHOICE`, never programme falsification;
  an UNKNOWN/`INSUFFICIENT` is never a boundary, never equivalence.
- "All arms censored at B" is arithmetic, not equivalence (solve-count floor).
- RANDOM-superior licenses only an anomaly report, never a claim that static
  contact "beats" choice in general and never a C1 rewrite.
- Donor transcripts encode `n_donor`, not `n_target`; nothing about target
  leakage can be inferred from their informativeness.
- Development-scout contrasts are non-citable forever.

## 4. Reviewer handoff — precise questions

**To Opus (X-line):** (1) Does the adjacent-pair construction fully
discharge CR-1, or does distance-1 create a *too-conservative* C1 whose
negative is uninformative — and if so, is that a scope caveat or a design
change? (2) Does the flat-opaque-index resolution of CR-2 (policies see raw
words only; cells offline) close your leak concern without reintroducing
syntactic-multiplicity bias, given fixed `m`? (3) Is the `d = 2n`
uncontactability argument (`pool |d| ≤ 125`, `n ≥ 66`) airtight against a
learner that composes contacted facts (e.g., transitivity over chained EQ
bits) — and if a compositional learner *can* pass stratum 4 legitimately,
is that a certificate feature or a hole? (4) Does the salted-commitment
protocol close MJ-5 for a 60-world registry?

**To Sol (Y-line):** (1) Is the stratified FPC paired estimator with
Bonferroni-simultaneous intervals over three contrasts acceptable as the
locked default, or do you require the bootstrap named as primary? (2) Is
the solve-count floor (≥ 25 % of blocks solving in each compared arm) the
right guard against arithmetic equivalence, or should the floor be defined
on interval determinacy instead? (3) Does the N3 rule (half-width ≤ N6/2,
clamp [12, 24]) survive your S5 concerns given FPC and the degenerate
distance? (4) Any objection to *all-arms without-replacement* selection as
the resolution of the repeat asymmetry?

## 5. Implementation authorization (Codex/Cursor)

**Codex — authorized now (gate 1, dummy fixtures only):** pure `Z/n` world +
left-fold + EQ oracle + truth-table enumeration checker; fail-closed
learner/acquisition/evaluator process separation and import interlocks;
transcript serialization with **salt-capable** commitments; donor/pair
bookkeeping (adjacency, disjointness, one-to-one, no-reuse, duplicate-`n`
rejection, role-assignment commitment). **Codex — after this v2 passes
S-gate review (gate 2):** the two-level pool + enumeration verifier +
reserved-cell partition; certificate builder on dummy worlds; committee
learner + side-effect-free scorer with state-hash tests. **Codex —
forbidden regardless:** comparative scout driver (gate 4), lock tooling
execution (gate 5), real escrow (gate 6), outcome driver (gate 7).

**Cursor Compose — not yet.** No closed bulk surface exists until the
S-gate signature; handing Cursor the pool/panel/learner now would encode
open choices. Eligible after gate 3 for mechanical breadth (tests,
serialization, harness plumbing) under Codex verification.

## 6. Confirmation

No comparative datum exists or was created; no scout, escrow, lock, or
outcome artifact exists or was created; no threshold or margin was derived
from any observed arm difference (none has ever been run). The signed
negative destinations and the two-layer Proof definition are preserved
verbatim: `PROOF_CORE`/`PROOF_STRONG`, C6 as annotation, the repaired C4
cascade, `BOUNDARY_CONTACT_CHOICE` for a C1 negative, `INSUFFICIENT` never
success, and the total contact-mode selector with C1 read separately.
