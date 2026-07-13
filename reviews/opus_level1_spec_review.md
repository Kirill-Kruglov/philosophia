# Opus 4.8 review — Level 1 world and learner specification

Reviewer: Opus 4.8 (adversarial scientific + systems, X-line). Target:
`experiments/level_1_contact/SCIENTIFIC_SPEC_DRAFT.md` (`DRAFT_PRE_S_GATE`),
against the signed claim graph (`fable_levels1_3_claim_graph_v2.md` + v2.1,
`LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`). Stage: pre-S-gate. This review creates
no code, scout, lock, escrow, or outcome, chooses no numeric threshold, and
predicts no arm. It preserves every signed negative destination.

---

## Verdict

**`REVISE_LEVEL1_SPEC`**

The spec is careful, mostly right, and the *pure `Z/n` oracle and fail-closed
dataflow substrate is eligible to implement now*. But three deferred choices are
not the "config fields, freeze at S-gate" items the draft treats them as — each
one changes the world, the estimand, or the endpoint, and each gates a specific
substrate module the draft's §13 wants built immediately:

1. **The finite single-integer world cannot simultaneously supply disjoint
   target/donor/development blocks *and* keep size strata narrow enough to avoid
   a donor-distance confound.** The n-supply arithmetic (`≈ 2·N3 + N_dev` distinct
   usable `n` per stratum) is a pre-S-gate feasibility question that can change the
   world, not a downstream number. (O1)

2. **The candidate-pool contract is unresolved on raw-word vs semantic-class, so
   ACTIVE can win by syntactic multiplicity and RANDOM-STATIC samples a different
   effective geometry.** This changes the C1 estimand and it changes the pool
   substrate's representation — it is not safely deferrable to a config field.
   (O2)

3. **The certified-solve panel as specified (class-balanced YES/NO) is passable
   by displacement-difference memorization without recovering the hidden order.**
   That makes "certified solve" not certify what the endpoint needs it to. It
   gates evaluator-panel construction. (O4)

Plus a confidentiality defect in the escrow commitment (low-entropy world +
committed plaintext hash = a pre-outcome verification oracle; O5) and a closed-
form world constraint the draft states only qualitatively (O1). None is fatal:
the cyclic world is not blocked (so not `BLOCKED_CYCLIC_WORLD`), and C1 is
identifiable with narrowed scope (so not `REJECT_LEVEL1_IDENTIFIABILITY`). They
are revisions to close before the modules they touch and before the S-gate.

---

## Findings, ordered

### Critical

- **CR-1 (O1) — n-supply vs disjointness vs stratum width is a binding, unresolved
  world-level tension.** Target, donor, and development worlds are declared
  disjoint, and donors are one-to-one with `n_donor ≠ n_target`. So each size
  stratum must contain at least `2·N3 + N_dev` distinct usable `n`. Within a size
  band of width `W` integers, `W ≥ 2·N3 + N_dev`. But the donor breaks adaptivity
  only up to a residual YOKED disadvantage that scales with `|n_target − n_donor|`,
  whose distribution is fixed by `W` (§ MJ-2). Narrow band → clean contrast but
  few blocks (low `N3`, and a large finite-population sampling fraction);
  wide band → enough blocks but large donor-target distance, i.e. YOKED probing a
  grossly wrong modulus. The draft's §2 claim that `n_donor ≠ n_target` "breaks
  instance adaptivity without manufacturing an easy mismatch" is only half true and
  must be qualified. This arithmetic can change the world (it is the strongest
  non-aesthetic argument for a second observable parameter — see MJ-2), so it must
  be confronted **before the S-gate freezes N1/N2/strata**, not after.

- **CR-2 (O2) — candidate cells: raw word pairs are the wrong substrate.** Every
  `{R,L}` word reduces to a net integer displacement; EQ depends only on
  `net(u) − net(v) (mod n)`. Under raw-word-pair cells: (i) ACTIVE can gain by
  *syntactic multiplicity* (many words realize the same informative displacement
  difference, so uncertainty-scored selection over word-space concentrates on
  dense regions — a syntactic artifact, not target adaptation); (ii) uniform
  RANDOM-STATIC over words induces a length-dependent, non-uniform distribution
  over displacement differences, so ACTIVE and RANDOM sample *different effective
  geometries* and the C1 contrast is confounded. Canonicalizing words to one
  representative per displacement removes multiplicity but *leaks the
  abelianization* (`net`, the hidden homomorphism to `Z`), which is forbidden
  truth. The resolution is a locked two-level design (see "Candidate-pool
  recommendation"). This is not a config field — the pool module and its
  enumeration verifier must be built to the two-level structure. Blocks §13's
  "canonical candidate-pool identity and arm equality" test.

- **CR-3 (O4) — certified solve does not certify order recovery.** High held-out
  EQ accuracy on a class-balanced YES/NO panel is achievable by *memorizing which
  displacement differences read equal* over the contacted range, without
  representing `n` as a modulus. Word-length and relation-type strata do not close
  this: a learner can pass by learning `net` (trivial, linear) plus a lookup of
  seen wrapping differences, and can hide the gap by abstaining on exactly the
  modulus-probing pairs while keeping ABSTAIN under its global cap. The minimum
  family-independent certificate must be built to be unpassable by
  difference-memorization (see O4 answer). This gates evaluator construction; the
  draft's §7 panel description is insufficient as the endpoint definition.

### Major

- **MJ-1 (O1) — state the exact wrap-coverage inequality.** The draft says the
  grammar must "admit word pairs whose displacement difference is `n`." Closed
  form: two words of length ≤ N2 realize every net-displacement difference in the
  integer interval `[−2·N2, +2·N2]`. To witness `n` and refute every shorter
  pseudo-period, the pool must realize differences covering `{1, …, n}`, so the
  identifiability floor is **`2·N2 ≥ n_max`, i.e. `N2 ≥ ⌈n_max/2⌉`** over the N1
  range (the smallest positive difference reading EQ-true is then exactly `n`,
  which pins `n` uniquely and excludes proper divisors, which read false).
  Headroom above the floor (many witnessing pairs per class, panel balance,
  solvability within budget `B`) is a separate S-gate resource choice. The S-gate
  enumeration proof (draft §2) should target this inequality.

- **MJ-2 (O1) — C1's scope and the distance confound.** Within the `{R,L}` /
  origin-EQ interface, `n` is provably the *only* learner-observable parameter: a
  hidden generator step `g` (`R: x↦x+g`) cancels under EQ on `{R,L}` words
  (`g` invertible ⇒ `net·g ≡ net·g` iff `net ≡ net`), and a hidden origin cancels
  because EQ compares endpoints symmetrically. So no second parameter is both
  hidden and identifiable in the cyclic world; any enrichment leaves the cyclic
  interface (a second independent generator = non-cyclic = Level-2 ontology).
  Consequences: (a) Level 1 C1 is inherently a test of *adapting probe scale to
  the target's modulus*, and its verdict must be scope-annotated as such, not as
  "chosen contact in a structured world"; (b) the ACTIVE-over-YOKED effect size
  scales with `|n_target − n_donor|` and therefore with stratum width — a design
  knob, not a pure property of choice — so donor-target distance must be a
  **reported mediator/diagnostic** and stratum width **justified on scientific
  grounds at the S-gate**, or a positive C1 is partly an artifact of a wide band.

- **MJ-3 (O3) — `|P̂(equal) − ½|` from a single head is not a meaningful
  uncertainty signal before calibration, exactly when it matters most.** Early in
  training the head is under-fit and its raw confidence is arbitrary; the first
  (most budget-consequential) ACTIVE choices would be driven by miscalibrated
  noise. Calibration is itself an unresolved S-gate item and needs data the online
  learner does not yet have — a circularity. A C1 null under a degenerate
  uncertainty signal is *not* a clean falsification of chosen contact (it is "this
  particular scalar carried no signal"). The uncertainty rule is outcome-
  determining, not a cosmetic "freeze candidate": the S-gate must justify it as
  providing real early signal (an ensemble/committee-disagreement scalar is a
  stronger default than single-head confidence) or scope the C1 claim explicitly
  to the weak rule chosen.

- **MJ-4 (O3) — selection compute and re-query pathology.** (a) ACTIVE evaluates
  the head over the candidate pool/shortlist each step; require that scoring be
  **provably side-effect-free on learner state** (eval mode; no parameter,
  optimizer, normalization-statistic, cache, or RNG-state mutation) — otherwise
  ACTIVE's extra inference contaminates its trajectory relative to YOKED/RANDOM.
  The draft separates *training* compute but does not guarantee *selection* is
  side-effect-free. (b) With slow online updates, argmin-uncertainty can re-select
  an already-answered pair repeatedly (same bit, no new information). Whether the
  rule excludes or down-weights answered pairs is outcome-relevant and must be
  frozen; a naive rule risks a pathological stall that nulls C1 for a mechanical
  reason.

- **MJ-5 (O5) — the committed plaintext hash is a pre-outcome verification oracle
  over a low-entropy world.** The escrow's only real entropy is the choice of
  hidden `n` values (and seeds); given the locked, public panel-construction rule,
  everything else is deterministic. Committing `hash(plaintext)` lets anyone who
  can enumerate candidate escrows confirm a guess — for a finite `Z/n` world that
  is tantamount to leakage. Confidentiality must rest on the encryption
  (Kirill's key) with the hash used for **integrity only**, and the commitment
  must be **salted with high-entropy secret salt carried inside the escrow and
  released at outcome**, so the pre-outcome hash is not a verification oracle. Also
  seal the plaintext enumeration-validator inside the generator environment (it
  reads plaintext; it must emit only a pass/fail proof), and run the generator on
  an isolated filesystem that is wiped. Correction 6 / §11 do not address the
  low-entropy hash weakness.

- **MJ-6 (O4/O5) — the evaluator must be post-hoc and blind to the researcher
  until outcome authorization.** The draft has the evaluator read frozen artifacts
  and never signal training/acquisition (good), but does not state that solve
  decisions are **sealed from the researcher** until the outcome is authorized. A
  concurrently-visible "solved at step t" is an analyst-side leak that enables
  post-hoc rule drift. Require: evaluator runs strictly on frozen post-B
  artifacts; its outputs are sealed until explicit outcome authorization (blind
  analysis).

- **MJ-7 (O1/estimand) — finite-population inference is mandatory, not optional.**
  Distinct `n` are drawn without replacement from a finite registered set, so
  blocks are not i.i.d. draws from an infinite superpopulation; the variance model
  needs a finite-population correction, and with a large sampling fraction (likely,
  given CR-1's supply squeeze) the uncorrected SE is anti-conservative. The draft
  §8 flags the need for "a finite-population or other valid block model" but does
  not commit one; the S-gate must, and must state that the claim is otherwise
  descriptive of the specific finite `n`-set used.

### Minor

- **mn-1 (O3) — within-block initialization must be paired.** For a clean paired
  contrast the three arms of one target block should share identical
  initialization weights, with per-arm domain separation only for stochasticity
  that must differ (tie-break, dropout). "Paired, domain-separated seeds" (§5) is
  ambiguous; state that init is shared within block and divergence comes only from
  queries + answers + locked stochasticity.

- **mn-2 (O2) — shortlist discipline.** Any tractability shortlist must be the
  full pool or a locked, arm-independent subsample; a learner-state-dependent
  shortlist is part of the ACTIVE treatment and must never be attributed to
  geometry or shared as "identically available" to RANDOM-STATIC.

- **mn-3 (O4) — control placement is correct; affirm and tighten.** The
  shuffled-answer null, parameter-stratum shift, and encoding-only probe are
  **design-invalidity / leakage gates computed on development worlds**, not
  scientific outcomes and not C-node results. Keep them there. The encoding-only
  probe must be strictly **pre-contact**: a probe reading `n` from a *post-contact*
  ACTIVE transcript is expected to succeed (legitimate mediation) and must never be
  used as a leakage test — the draft §4 states this distinction correctly; hold it.

- **mn-4 (O5) — affirm assignment-lock; add FS hygiene.** Donor-target assignment
  is randomized once at lock within strata and then conditioned on (Correction 5)
  — this correctly forecloses donor cherry-picking; affirm. Add the isolated-FS +
  wipe requirement for the generator (MJ-5).

- **mn-5 (governing-text drift) — the README and KILL_MATRIX still say "equal
  answer entropy."** The signed design replaced it with the yoked estimand, but
  `experiments/level_1_contact/README.md` and the `KILL_MATRIX` Level-1 row still
  carry the old matching rule. The loud signed amendment (draft §5 / v2 Sol-m1)
  must land **before any lock**; until it does, the governing files disagree with
  the design.

---

## Answers to the required attacks

### O1 — Is `Z/n` an adequate experimental world?

- **`n` is the complete world identity: confirmed.** Under fixed origin 0,
  `R:+1`, `L:−1`, and EQ = equality of net displacement mod `n`, two worlds with
  the same `n` have identical oracle truth tables. **Duplicate `n` are repeated
  measurements, confirmed** — `N3` cannot be manufactured from duplicate IDs
  (draft correct).
- **`n_donor ≠ n_target` within a stratum: partly refuted.** It breaks
  instance-adaptivity, but the residual YOKED disadvantage scales with
  `|n_target − n_donor|` (the donor probed a valid but wrong modulus). That is
  technically legitimate adaptivity, but its magnitude is a stratum-width artifact
  — so the "no easy mismatch" claim needs the MJ-2 qualification and distance-as-
  mediator reporting.
- **Enough heterogeneous blocks? — the binding worry (CR-1).** Heterogeneity
  across blocks is only "different cycle length." The disjointness requirements
  consume `≈ 2·N3 + N_dev` distinct `n` per stratum, in tension with the
  narrow-stratum requirement that keeps donor distance small. This must be
  resolved at the S-gate with the actual N1/N2 arithmetic.
- **Second hidden parameter?** Not possible within `{R,L}`/origin-EQ: a hidden
  generator step or origin is unobservable through EQ (MJ-2). A genuinely new
  observable parameter requires a second independent generator, which leaves the
  cyclic world for the Level-2 automaton ontology. So the honest options are:
  accept narrow "probe-scale-adaptation" scope for Level 1 in pure `Z/n`; or move
  the C1 test into a richer world (coupling L1 to the still-open Level-2 contract).
  This is a scientific decision, surfaced now because it can change the world.
- **N1/N2 coverage: `2·N2 ≥ n_max` (MJ-1).** State this closed form as the
  enumeration target.

**If the minimal world cannot identify C1:** it *can*, but only the probe-scale
form, and only if CR-1's supply arithmetic yields an adequate `N3` at a stratum
width whose induced donor-distance is scientifically defended. Smallest repair:
keep pure `Z/n`, resolve the supply arithmetic and stratum width at the S-gate,
report donor-target distance as a mediator, and scope-annotate the C1 verdict.
Do not enlarge the curriculum; if the supply arithmetic fails, the correct move
is to re-site C1 in the Level-2 world, not to widen `Z/n` cosmetically.

### O2 — Query grammar and geometry

Raw word pairs are the wrong cell (CR-2). Displacement-difference classes alone
lose the learner's task (recognizing that different words are equal *is* the
structure) and canonical single-representatives leak `net`. **Use a locked
two-level candidate contract** (see recommendation). This makes "ACTIVE wins by
syntactic multiplicity" impossible by construction, guarantees RANDOM-STATIC and
ACTIVE share the same semantic geometry, and keeps raw words in the learner's
input. `(u,u)` positives, inverse/cancellation pairs, and orientation collapse
into the difference-0 class, which must be capped/balanced, never oversampled.
Uniform sampling over differences yields extreme label imbalance (EQ-true only at
differences `≡ 0 mod n`, ~`1/n`), so the RANDOM design's difference distribution
is an outcome-relevant S-gate choice. A tractability shortlist changes the
estimand unless it is arm-independent (mn-2). **Require a canonical candidate-pool
contract and an enumeration verifier built to the two-level structure** — before
the pool module is written.

### O3 — Learner and acquisition behavior

Freeze at S-gate, shared across arms, and outcome-relevant (not cosmetic):
architecture, input encoding, initialization (paired within block, mn-1),
optimizer, online update count, replay/history view, calibration method, and the
RANDOM design. `|P̂(equal) − ½|` single-head is a weak, pre-calibration-dependent
uncertainty policy (MJ-3) — prefer an ensemble/disagreement scalar or justify the
weak one and scope C1 to it. Selection must be side-effect-free and the
already-answered-pair rule must be frozen (MJ-4). Selection compute reported
separately from oracle and matched-training compute is right, provided the
side-effect-free guarantee holds.

**Neutral to implement now:** `Z/n` oracle, word fold, EQ, truth-table
enumeration; the fail-closed learner/acquisition/evaluator process separation and
import interlocks; transcript serialization + (salted) hash + donor bookkeeping.
**Encodes a choice too early:** architecture, the uncertainty scalar, calibration,
update/replay schedule, RANDOM distribution, panel construction — and, because of
CR-2/CR-3, the **candidate-pool module** and the **evaluator-panel module** are
*not* neutral and must wait for O2/O4.

### O4 — Certified solve and negative controls

High EQ accuracy is achievable without recovering `n` (CR-3). **Minimum
family-independent certificate for the cyclic world:** the panel must (i) test EQ
on displacement-difference classes **held out** from the contacted set, spanning
all residue classes mod `n`; (ii) include explicit **periodicity probes** —
differences `k·n` (never contacted) must read true and `k·n ± 1` false —
demonstrating the learner represents the *period*, not a lookup; (iii) require the
accuracy, calibration, ABSTAIN, and confident-lie constraints to hold **within the
periodicity-probe stratum specifically**, not just globally (else the learner
abstains on exactly the modulus-probing pairs under a global cap and still
"passes"). Order probes stay secondary (draft correct).

The shuffled-answer null, parameter-stratum shift, and encoding-only probe are
**design-invalidity/leakage gates on development worlds, not scientific
outcomes** (mn-3). Post-contact query-sequence structure is legitimate mediation;
only *pre-contact* encoding leakage is a fault — the draft draws this line
correctly and it must be held.

### O5 — Donor and escrow sequencing

Sequencing is largely sound: full-B donor transcript hash-committed before YOKED
derivation; donor solve status never fed back; donor answers never transfer;
one-to-one/no-reuse; assignment locked pre-outcome (mn-4). Leak audit:

- Transplanted donor queries encode `n_donor`, not `n_target` — no forbidden
  target leak (and the near-modulus informativeness is the legitimate geometry
  effect).
- **Escrow hash is a verification oracle over a low-entropy world (MJ-5)** — the
  one real confidentiality hole; fix with a secret salt and encryption-only
  confidentiality.
- **Evaluator output must be sealed from the researcher until outcome
  authorization (MJ-6).**
- The plaintext validator must be sealed inside the generator; isolated FS +
  wipe (mn-4).

### O6 — Gate decision

| Gate | Status | Blocking closures |
|---|---|---|
| **Neutral substrate** (`Z/n` world, word fold, EQ oracle, truth-table enumeration checker; fail-closed learner/acquisition/evaluator process + import interlocks; transcript serialization + salted-hash commitment + donor-assignment bookkeeping with disjointness/one-to-one/no-reuse/equal-`n`-rejection) | **ELIGIBLE NOW**, on dummy non-escrow fixtures | none — but hashing must support salting (MJ-5) |
| **Candidate-pool module + enumeration verifier** | **BLOCKED** | CR-2 (two-level contract) — a world/estimand choice, not deferrable to config |
| **Evaluator-panel construction** | **BLOCKED** | CR-3 (memorization-proof certificate) — an endpoint choice |
| **Trajectory-bearing learner** (architecture, uncertainty scalar, calibration, update/replay schedule, ACTIVE scorer, RANDOM design) | **BLOCKED** | O3 S-gate freezes (MJ-3, MJ-4) |
| **S-gate signature** | **BLOCKED** | CR-1 (n-supply/stratum arithmetic), MJ-1 (N2 floor), MJ-2 (C1 scope + distance mediator + stratum-width justification), CR-2, CR-3, MJ-3, MJ-4, MJ-7 (finite-population model), N6 margins; README/KILL_MATRIX amendment (mn-5) |
| **Comparative scout driver** | **FORBIDDEN** | S-gate signature complete |
| **Level 1 lock + escrow** | **FORBIDDEN** | N3 from scout; salted escrow protocol (MJ-5); MJ-6 seal; full invalidity gates |

No item above is a "preregister later" deferral of a world/estimand/unit/
endpoint/arm choice: CR-1 touches the world, CR-2 the estimand and arm geometry,
CR-3 the endpoint, MJ-2/MJ-7 the unit and scope, MJ-3/MJ-4 arm behavior. Each is
placed before the module or gate it controls.

---

## Exact mandatory revisions

1. State the wrap-coverage floor `2·N2 ≥ n_max` (MJ-1) and add the n-supply
   inequality `W ≥ 2·N3 + N_dev` per stratum as an S-gate feasibility obligation
   (CR-1); resolve the stratum-width / donor-distance / N3 tension before freezing
   N1/N2/strata.
2. Replace the candidate-pool section with the two-level contract below (CR-2) and
   require its enumeration verifier.
3. Rewrite the certified-solve certificate to be memorization-proof: held-out
   residue classes + periodicity probes + per-periodicity-stratum accuracy/ABSTAIN
   caps (CR-3).
4. Fix the uncertainty scalar as an outcome-determining S-gate choice with a
   justification of early signal (ensemble/disagreement default), and freeze the
   answered-pair rule; require side-effect-free selection (MJ-3, MJ-4).
5. Salt the escrow commitment and rest confidentiality on encryption; seal the
   validator; seal evaluator output until outcome authorization (MJ-5, MJ-6).
6. Commit a finite-population block-variance model with FPC and state
   assignment-conditioned, finite-`n`-set scope (MJ-7).
7. Scope-annotate the C1 verdict as probe-scale adaptation and report donor-target
   distance as a mediator (MJ-2); land the README/KILL_MATRIX amendment before any
   lock (mn-5).

---

## Candidate-pool recommendation (the two-level contract)

- **Semantic level (the design geometry, balanced and identical across arms).**
  A cell is characterized by the oracle-relevant content: the displacement pair
  `(a, b)` with `a, b ∈ [−N2, N2]` and its difference `d = a − b`. The design
  geometry — which difference classes and displacement pairs are admissible, and
  the RANDOM-STATIC distribution over them — is locked at the S-gate, balanced
  over the periodicity structure, with the difference-0 (trivially-equal) class
  capped. ACTIVE scores *semantic cells* by evaluating the learner head on each
  cell's representative(s); its "choice" is over this meaningful axis only.
- **Syntactic level (realization, locked and arm-independent).** A seeded,
  committed, arm-independent map assigns each semantic cell a fixed set of raw
  `{R,L}` word realizations (a fixed multiplicity per class, drawn identically for
  every arm). The learner receives raw words (task preserved; no `net` leak),
  but no arm can gain from syntactic density and all arms draw syntax from one
  distribution.
- **Verifier.** An enumeration check proves: canonical cell identity; `(u,v)`/
  `(v,u)` orientation collapse; the difference-0 class contains all `(u,u)` and
  cancelling pairs and is capped; the admissible pool `≫ B`; and that ACTIVE,
  donor-ACTIVE, and RANDOM-STATIC all index the *same* semantic pool under the
  *same* syntactic map. Any shortlist is the full pool or a locked arm-independent
  subsample (mn-2).

This is the smallest structure that closes O2 without leaking the reduction, and
the pool substrate must be built to it.

---

## Precise next authorization

- **Codex — authorized now, dummy fixtures only:** (1) the `Z/n` world +
  left-fold word evaluation + EQ oracle + independent truth-table enumeration
  checker; (2) the fail-closed dataflow skeleton — separate learner / acquisition
  / read-only evaluator processes with mechanical import/dataflow interlocks
  proving the acquisition scorer cannot reach oracle truth, evaluator state, or
  escrow, and that no committed driver can run a scout/escrow/outcome before its
  capability exists; (3) transcript serialization + **salted** hash-commitment +
  donor-assignment bookkeeping with disjointness, one-to-one, no-reuse, and
  equal-`n`-rejection / duplicate-`n`-pseudoreplication checks. **Not authorized:**
  the candidate-pool geometry module, the RANDOM design, the ACTIVE scorer, any
  learner architecture, or evaluator-panel construction (blocked on CR-2 / CR-3 /
  O3 S-gate).
- **Cursor Compose — not yet.** There is no closed five-arm/bulk spec surface to
  hand it; it waits for the S-gate freeze (endpoint, margins, candidate contract,
  panel, learner). Handing Cursor the pool/panel/learner now would encode the very
  choices this review holds open.

---

## Preservation of signed negative destinations

This review adds constraints and removes none. Preserved intact: `PROOF_CORE` /
`PROOF_STRONG` two-layer split and the C6 annotation; the repaired B/D-conditioned
C4 cascade (`FALSIFIED_AT_C2`, `BOUNDARY_REPRESENTATION`, `BOUNDARY_WEIGHTS_ONLY`,
`BOUNDARY_INHERITED_LEDGER`, `BOUNDARY_REDUNDANT_MEMORY`, `FALSIFIED_AT_C4`); the
Level-1 `BOUNDARY_CONTACT_CHOICE`; `INSUFFICIENT` / censored / UNKNOWN never
success; the RANDOM-superior anomaly recorded but never rule-altering; and the
contact-mode scope annotation. My CR-1/MJ-2 additions *strengthen* the C1 scope
discipline; CR-3 *strengthens* the certified-solve certificate; none relaxes a
kill.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
