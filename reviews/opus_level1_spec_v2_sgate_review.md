# Opus 4.8 X-line review — Level 1 v2 spec, S-gate readiness

Reviewer: Opus 4.8 (adversarial scientific + systems). Target:
`experiments/level_1_contact/SCIENTIFIC_SPEC_V2_DRAFT.md`, against the signed
claim graph, Sol's Y-line spec review, and Fable's v2 closure memo. Stage:
pre-S-gate. This review creates no code, scout, escrow, lock, or outcome, chooses
no threshold from imagined results, and predicts no arm. All cardinalities and
support inequalities below were recomputed independently from the registry, not
taken from the draft's summary.

---

## Verdict

**`REVISE_LEVEL1_V2_SPEC`**

v2 is a large, genuine advance — the adjacent-pair supply arithmetic, committee
acquisition, side-effect-free scorer, salted escrow, sealed post-B evaluator, and
finite-population framing all land. But the certificate that the whole level's
endpoint rests on contains **three confirmed internal contradictions** and its
anti-lookup guarantee is **misattributed**, and several **endpoint-determining
quantities are still unset**, so signing the S-gate now would freeze an
inconsistent endpoint. Independently recomputed:

- **The reserved-cell universe (`|d| ≤ 125`) cannot supply the §7 double-wrap
  probes (`d = 2n ∈ [132, 250]`).** Confirmed: every `2n` for `n ∈ [66,125]`
  exceeds 125, so the panel cannot be "built from evaluator-reserved cells only."
  (X2.1)
- **`N2 = 125` cannot realize the near-miss `2n+1 = 251` at `n = 125`** (max
  realizable `|d| = 2·N2 = 250 < 251`). The strengthened inequality is
  `2·N2 ≥ k_max·n_max + 1 = 251 ⟹ N2 ≥ 126`, decoupled from the acquisition cap.
  (X2.2)
- **Reserving cells *within* every `|d|` class does not close difference-lookup
  memorization** — EQ depends only on `d mod n`, so a learner that contacted any
  cell of difference `d` knows the label for every held-out cell of the same `d`.
  Only the uncontactable double-wrap stratum (4) carries anti-lookup power; the
  claim "every panel item is semantically never-contacted" is false for strata
  1–3, 5. (X2.3)
- **"For each residue class … YES/NO balanced" is mathematically impossible:** for
  fixed `n`, EQ is constant within a residue class (all YES at `r=0`, all NO at
  `r≠0`). Confirmed by enumeration. (X3)

None of these rejects the world (the registry/pairing is sound; not
`BLOCKED_LEVEL1_WORLD`) and none rejects the certificate in principle — each is
repairable by decoupling `N2` from the acquisition cap, defining a three-zone
evaluator universe, rebuilding the panel table, and restating the anti-lookup
basis (not `REJECT_LEVEL1_CERTIFICATE`). But they change the endpoint's support
and construction, so the S-gate cannot be signed as a confirmation of v2 as
written. **All Level 1 execution — scout, lock, escrow, outcome — remains
forbidden.**

---

## Findings, ordered

### Critical

- **CR-A — the certificate's support arithmetic is internally contradictory and
  the anti-lookup basis is misattributed (X2.1–2.3).** Three defects compound:
  (i) reserved cells are `|d| ≤ 125` but stratum-4 needs `|d| = 2n ≥ 132`, so §7's
  "reserved cells only" is impossible; (ii) `N2 = 125` cannot realize `2n+1 = 251`
  at `n = 125`; (iii) within-`|d|`-class reservation gives only *raw* novelty, not
  *difference* novelty, so a difference-lookup learner passes every stratum except
  the uncontactable double-wrap one. **Repair:** decouple the word-displacement
  bound `N2` from the acquisition difference cap `d_acq`; set `N2 ≥ 126` (so
  `2·N2 ≥ 252 ≥ 251`), keep `d_acq = 125` (single-wrap `d=n ≤ 125` contactable;
  double-wrap `d = 2n ≥ 132 > d_acq` uncontactable — the constraint is
  `n_max ≤ d_acq ≤ 2·n_min − 2 = 130`); define a **three-zone evaluator
  universe** — acquisition (non-reserved, `|d| ≤ d_acq`), reserved (`|d| ≤ d_acq`,
  raw-novel), and **extrapolation** (`d ∈ (d_acq, 2·N2]`, the true difference-novel
  zone the reserved partition never covered); and restate that the anti-lookup
  guarantee rests on stratum 4 alone.

- **CR-B — the panel table is algebraically wrong and its only anti-lookup stratum
  carries a structural confound (X3).** "YES/NO balanced within each residue
  class" is impossible (EQ is constant within a class); balance must be *across*
  classes (YES from `d ∈ {0, n, 2n}` vs NO elsewhere). Worse: within the
  contactable range `|d| ≤ d_acq`, the only nonzero true difference is `d = n`
  itself, so "found the modulus" and "memorized that `d=n` is the one special
  difference" are **observationally identical** — the distinction is visible only
  at `d = 2n`, which structurally requires the **extreme-opposite displacement
  corner** (`a ≈ n, b ≈ −n`, a region absent from the `|d| ≤ d_acq` pool). So
  stratum 4 conflates period-representation with corner-extrapolation, and this is
  *irreducible* in the cyclic world. "Certified solve" therefore means "represents
  the period well enough to extrapolate to the uncontacted `2n` corner" — a
  broader claim than pure modulus-recovery, which must be stated as the endpoint's
  meaning (or the world enriched). Provide the corrected panel table (below).

- **CR-C — endpoint- and decision-determining quantities are unset or
  under-justified, and outcome-correlated block failures are mishandled (X5).**
  (i) Per-stratum accuracy (0.95 is a bare "platform precedent"), the calibration
  statistic **and bound**, ABSTAIN caps, confident-lie caps, panel stratum counts,
  the **evaluator ensemble aggregation rule** (how 4 members → one panel
  prediction), and the interval method (Bonferroni vs bootstrap) each change the
  solve event or the resolved predicate. Several have **no candidate value at
  all**. A signature that merely "confirms candidates" would leave the endpoint
  and decision rule open — so v2 is not confirmation-ready; the revised spec must
  supply justified non-comparative values for every endpoint-determining quantity
  *before* the S-gate. (ii) §10 routes "non-finite state" to **block exclusion**,
  but non-finite optimization states are outcome-correlated (harder worlds diverge
  more often); excluding them and re-applying FPC to survivors biases the
  finite-population estimand toward the arms/worlds that don't diverge. Such a
  block must be **censored** (arm did not solve by `B`), not excluded. Only
  verifiably outcome-*independent* faults (hash mismatch, hardware, determinism
  bug) may be excluded-with-record; the "exclude ≤ 4 + FPC survivors" rule is
  identifiable only under that restriction.

### Major

- **MJ-α — the adjacent distance-1 donor is one-sided: it powers a positive C1 but
  nearly cannot support a negative one (X1).** Fixing `|n_target − n_donor| = 1`
  removes CR-1's mismatch confound for a *positive* result (adaptivity beating
  near-identical geometry is strong evidence). But adjacent moduli induce
  near-identical optimal probe geometry, so a *null* is the expected result
  whether or not choice matters at larger distances — `BOUNDARY_CONTACT_CHOICE`
  from a distance-1 null is a very thin boundary. Level 1 is thus structurally a
  **detector, not a falsifier**, of choice benefit. For a programme that treats
  negatives as first-class, this asymmetry must be stated, and Kirill should
  decide: accept the one-sided scope, or add a distance axis (a second donor per
  target at larger distance) to make the null informative.

- **MJ-β — the §1 scope annotation mislabels what distance-1 isolates (X1).** §1
  scopes C1 as "probe-**scale** adaptation to `n`," but distance-1 nearly
  *equalizes* scale between target and donor; what remains is **online
  responsiveness** (coupling to the target's own answer stream vs replaying a
  donor's). That is arguably the purer notion of chosen contact, but it is not
  "scale adaptation." Correct the scope wording to "online responsiveness under a
  near-matched scale," and note the scale axis is largely controlled out, not
  tested.

- **MJ-γ — the population/scope statement is internally inconsistent and the FPC
  degenerates at the ceiling (X1).** §8 calls the scope "the finite registered
  population Ω" (60 worlds), but the estimator only ever touches the ≤ 24 realized
  **target** worlds (one role-assigned member per outcome pair); donor worlds and
  the 60-world Ω are not the estimand's population. The FPC "blocks used / 8 per
  stratum" implies sampling from the 8-per-stratum frame — but the N3 rule can
  clamp to `N3_max = 24`, at which point the whole frame is enumerated, the
  sampling fraction is 1, world-level variance → 0, and only seed noise remains
  (a purely descriptive claim about those 24 worlds). Fix a single population —
  **the N3 realized target worlds, assignment-conditioned** — and state the
  `N3 = 24` degeneracy explicitly rather than implying generalization to Ω.

- **MJ-δ — the learner architecture is an unjustified extrapolation from Level 0
  (X4).** Level 0's one-layer, `d_model 128`, no-LayerNorm model grokked
  ~3-token modular addition; here inputs are `u SEP v` up to **271 tokens** over
  moduli to 125. "Level 0 platform hyperparameters as candidates" is not an
  executable contract for this task: the positional scheme, maximum supported
  length, and capacity for length-271 / modulus-125 EQ are **new** scientific
  choices with a real feasibility risk (if nothing solves within `B`, the
  solve-count floor forces `INSUFFICIENT`). Name and justify the imported
  architecture contract for *this* input regime, not by reference to Level 0.

- **MJ-ε — the committee-disagreement early-signal claim is oversold (X4).** At or
  near random initialization, 4 distinct-init members disagree as *noise*, so
  argmax-disagreement over the shortlist selects near-randomly exactly when the
  budget is scarcest and each query matters most; meaningful disagreement (signal
  vs genuine uncertainty) emerges only after some training. The MJ-3 resolution
  ("no calibration, no data needed") is only asymptotically true. This does not
  break the design, but a C1 null could still be a weak-early-signal artifact, and
  the scope annotation must say so.

- **MJ-ζ — evaluator aggregation, loss, calibration, and ABSTAIN are
  endpoint-determining and unspecified (X4/X5).** The map from the 4-member
  committee to a single panel prediction (majority? mean-probability? min?), the
  training loss, the calibration statistic and its bound, and the ABSTAIN
  probability rule all change which runs certify solve and when. They must be
  fixed with justified non-comparative values before signature, not deferred as
  "locked at S-gate."

### Minor

- **mn-i (X4)** — shortlist exogenous randomness adds ACTIVE-run variance; ensure
  seed replicates span it and block-level inference absorbs it. YOKED inherits the
  donor's shortlist draw (fixed in the committed transcript) while target-ACTIVE
  draws its own — matched in law, worth noting in the estimand.
- **mn-ii (X2)** — the `d = 0` cap "same per-class realization count as every
  other class" is ambiguous (classes have different cell counts, `251 − |d|`);
  specify the cap value.
- **mn-iii (X3)** — affirm and enforce serialization leak-proofing: the per-world
  panel *structure* encodes `n` (which differences are true), so an enumeration
  proof must show no panel artifact (counts, ids, ordering, stratum names,
  hashes) reaches learner/acquisition code; sealed-until-authorization is affirmed
  and sufficient only if it covers all metadata.
- **mn-iv (X6)** — `B·S·E` scoring dominates cost (~16× training; see X6); it may
  be sized from development *timing and censoring rate*, never from arm contrasts.

---

## Answers to the required attacks

### X1 — Registry, pairing, and scope

Recomputed: Ω = {66,…,125} = 60 integers = 30 adjacent pairs = 3 strata × 10
pairs; `N_dev = 6` (2/stratum) → 24 outcome pairs → `N3_max = 24` (8/stratum).
Capacity `2·N3 + 2·N_dev ≤ 60 ⟹ N3 ≤ 24`; per stratum `N3/3 + 2 ≤ 10 ⟹ N3 ≤ 24`.
All exact. ✓

- **Distance 1 does not remove the confound symmetrically (MJ-α):** it removes it
  for positive C1 (strong) and nearly voids negative C1 (a null is expected
  regardless). It is the *narrowest possible version of the donor-distance
  mediator*, not the mediator's elimination — the mediator is pinned to its
  minimum, which is exactly why a null is uninformative.
- **What a negative C1 supports under distance-1:** only "online responsiveness to
  the target's own answers adds nothing beyond geometry adapted to an adjacent
  modulus" — a thin boundary that says nothing about scale-adaptation or
  larger-distance choice. `BOUNDARY_CONTACT_CHOICE` here must be scope-annotated
  accordingly.
- **Which finite population (MJ-γ):** after 6 pairs → development and one member
  of each of the 24 outcome pairs → target, the estimator describes **the N3 ≤ 24
  realized target worlds**, assignment-conditioned — *not* all 60 `n`, *not* the
  30 pairs, *not* the 48 outcome-pair worlds, *not* the donor worlds. §8's "finite
  registered population Ω" is a silent switch and must be corrected. At `N3 = 24`
  the population is fully enumerated and world-level uncertainty vanishes; the
  spec must own that degeneracy.

### X2 — Candidate and evaluator support arithmetic (independently recomputed)

Exact universes:
- **Endpoint / word displacements:** `a, b ∈ [−N2, N2]`; realizable difference
  `d ∈ [−2·N2, 2·N2]`. With `N2 = 125`, `d ∈ [−250, 250]`.
- **Acquisition semantic cells:** orientation-canonical `{a,b}` with
  `|d| ≤ d_acq`. Total for `d_acq = 125`: `251 + Σ_{d=1}^{125}(251−d) = 23,751`
  cells (recomputed). Non-reserved ≈ 0.7 × 23,751 ≈ 16,626 × `m=4` ≈ 66,503
  realizations ≈ 33× `B` — headroom confirmed.
- **Evaluator-reserved cells:** 30 % within each `|d|` class — all `|d| ≤ d_acq`.
- **Acquisition vs evaluator-only differences:** contactable `|d| ≤ d_acq`;
  double-wrap `|d| = 2n ∈ [132, 250]` uncontactable (since `2·66 = 132 > d_acq`).

**Suspected contradictions — tested, all confirmed:**
1. **§3 (`|d| ≤ 125`) vs §7 (`d = 2n`, `2n±1`):** `2n ∈ [132,250]`, all `> 125`.
   The panel *cannot* be drawn "from reserved cells only." Confirmed. Repair: the
   evaluator draws stratum 4 from the **extrapolation zone** `d ∈ (d_acq, 2·N2]`,
   a third zone the reserved partition never covered.
2. **`N2 = 125` vs `2n+1 = 251` at `n = 125`:** `2·N2 = 250 < 251` → the high
   near-miss is unrealizable. Confirmed. Strengthened inequality:
   `2·N2 ≥ k_max·n_max + 1 = 251 ⟹ N2 ≥ 126`. Decouple from the acquisition cap:
   `d_acq ∈ [n_max, 2·n_min − 2] = [125, 130]` keeps single-wrap contactable and
   every double-wrap probe (down to `2·66 − 1 = 131`) uncontactable. `L_word = 135`
   already admits length-126 words, so `N2 = 126` costs nothing.
3. **Within-class reservation vs held-out semantic classes:** EQ depends only on
   `d mod n`, so contacting *any* cell of difference `d` fixes the label for every
   held-out cell of that `d`. Within-class reservation closes only *syntactic*
   memorization; the **double-wrap stratum alone** closes difference-lookup.
   Confirmed. Repair the claim language ("semantically never-contacted" is true
   only for stratum 4) and rest the anti-lookup proof on stratum 4.

**Opaque-index / no-semantic-leak:** the flat opaque index with fixed `m = 4`
(uniform index sampling = uniform cell sampling) does close CR-2's leak and
multiplicity concerns — policies see raw tokens only; the cell↔index map lives
offline in the enumeration verifier. Accepted, provided serialized artifacts
carry no grouping/`n` signal (mn-iii).

### X3 — Panel logic and anti-lookup certificate

"For each residue class … YES/NO balanced" is impossible: enumerated, each
residue class has a **singleton** label ({True} at `r=0`, {False} at `r≠0`).
Balance is across classes. Corrected panel table:

| Stratum | Label rule | Support `d` | Novelty | Anti-lookup role |
|---|---|---|---|---|
| 1 False-space coverage | NO (`d ≢ 0 mod n`) | `d ∈ [1, d_acq] \ {n}`, spanning many residues | raw-novel (reserved); **not** difference-novel | none — a difference-lookup passes; calibration/breadth only |
| 2 Single-wrap + near-miss | YES `d = n`; NO `d = n ± 1`, length-matched | `n ≤ n_max` | raw-novel; `d = n` was contactable | none alone — tests the special-difference and neighbours |
| 3 Syntactic-identity / orientation | YES/NO | small `|d|` | raw-novel | defeats "unequal unless identical" |
| 4 Double-wrap extrapolation (**the teeth**) | YES `d = 2n`; NO `d = 2n ± 1` | `d ∈ (d_acq, 2·N2]` | difference-novel **and** raw-novel; uncontactable | **the only** anti-lookup stratum; structurally corner-confounded |
| 5 Length / imbalance / symmetry | YES/NO | varied | raw-novel | robustness |

Balance across the panel between YES (`d ∈ {0, n, 2n}`) and NO items.

- **Does `d = 2n` certify a learned period?** Only jointly with input-corner
  extrapolation (CR-B): `d = 2n` forces the extreme-opposite displacement corner
  absent from the pool, so it tests period-representation *and* corner
  generalization together, irreducibly. A pass is strong (a pure lookup has no
  entry for uncontacted `2n`); a *failure* is ambiguous (no period, or cannot
  reach the corner) — acceptable for a conservative certificate (failure →
  censored), but the endpoint's meaning is the broader joint claim.
- **What passes / fails:** syntax memorization fails (raw-novel panel);
  "unequal unless identical" fails (strata 2/4 positives); abstain-on-probes is
  closed by the per-stratum ABSTAIN cap on stratum 4 (keep it); `net`-only
  learners fail (wrap requires modular, not integer, equality); **difference
  lookup over contacted support fails only at stratum 4** — so stratum 4 is
  load-bearing and must survive the CR-A arithmetic fix. Serialization leakage is
  closed only if all panel metadata is sealed (mn-iii).

### X4 — Learner and arm trajectory completeness

One target step (`E = 4`): select query (ACTIVE: score `S = 512` shortlist by
committee `p̂` variance, argmax, tie = lowest index; YOKED/RANDOM: next committed
index) → oracle bit → each member records pre-update `p̂` → each takes `U = 1`
AdamW step on a seeded `min(32, t)` minibatch from own history → optional
checkpoint. State mutated: 4× parameters, 4× optimizer moments, contact history,
answered-index set, selection/minibatch RNG, step counter.

Frozen vs candidate-only: **not** genuinely frozen — positional scheme and max
supported length (MJ-δ); evaluator ensemble aggregation, loss, calibration, and
ABSTAIN rule (MJ-ζ); AdamW lr/wd/betas/eps/scheduler ("Level 0 candidates" —
shared across arms so not a C1 bias, but a feasibility risk under MJ-δ). Genuinely
frozen: init pairing (identical per member across arms), update count `U=1`,
replay view, without-replacement + answered-pair exclusion, side-effect-free
scorer (state-hash contract — accepted), tie-break. Committee disagreement at
random init does **not** provide the claimed early signal (MJ-ε); it scopes C1 to
a heuristic that is weak early. Shortlist randomness is exogenous and matched in
law across ACTIVE runs (mn-i) — acceptable, variance noted.

### X5 — Endpoint closure and invalidity

Open quantities that **do** change the endpoint or decision (so cannot be called
harmless confirmations): per-stratum accuracy, calibration statistic+bound,
ABSTAIN caps, confident-lie caps, panel stratum counts, evaluator aggregation
(MJ-ζ), solve-count floor value, N6 margin, interval method, leakage tolerances,
seed schedule. These must be **resolved with justified non-comparative values in
the revised spec before signature** (CR-C). The resource wall is
outcome-independent and may be set from resource evidence.

Block exclusion (CR-C): missing-arm, non-finite, and replay failures are **not
uniformly outcome-independent**. Non-finite optimization states are
outcome-correlated and must be **censored** (non-solve at `B`), never excluded;
excluding them and FPC-ing survivors biases toward non-diverging arms. Only
verifiably outcome-independent faults (hash mismatch, hardware, determinism bug)
may be excluded-with-record. "Exclude ≤ 4 then FPC" yields an identifiable
finite-population estimand only under that restriction, established per exclusion,
not assumed. Otherwise route to `INSUFFICIENT` under the stricter rule.

### X6 — Resource and gate

Dominant work per ACTIVE run ≈ `B·S·E` scoring forwards = `2000·512·4 ≈ 4.1M`,
vs training ≈ `E·B·U·|minibatch| ≈ 4·2000·32 ≈ 2.6×10⁵` — **scoring dominates
~16×**. Per block ≈ 2 scoring runs (target + donor ACTIVE) + 4 training arms;
across 24 blocks × `R` seeds the leading term is `≈ 24·R·2·B·S·E ≈ 2×10⁸·R`
forwards on a 1-layer/`d128`/seq-271 model — feasible on the platform, bottleneck
is `S·E`. Non-comparative evidence that may set `B` and the resource wall:
development-world **timing, memory, throughput, endpoint computability, and
censoring rate** (single-arm feasibility) — never arm **contrasts**. The line is
correct in §5/§10; affirm it.

**Gate table:**

| Gate | Status | Blocking closures |
|---|---|---|
| Neutral dummy-fixture substrate (`Z/n` world + fold + EQ + truth enumeration; fail-closed process/import interlocks; salt-capable commitment; adjacent-pair/disjointness/one-to-one/no-reuse/duplicate-`n`/role-commitment bookkeeping) | **ELIGIBLE NOW** — but do **not** hardcode `N2`, `d_acq`, or the difference zones; parameterize and let the enumeration checker assert the CR-A inequalities |
| Full implementation (two-level pool + verifier; reserved + extrapolation zones; certificate builder; committee learner + scorer) | **BLOCKED** | CR-A, CR-B (corrected universe + panel), MJ-δ/ζ (architecture, aggregation) |
| Resource check | **ELIGIBLE** on development worlds | timing/memory/censoring only; no arm contrast |
| S-gate signature | **BLOCKED** | CR-A, CR-B, CR-C, MJ-α/β/γ/δ/ε/ζ; justified values for every endpoint-determining quantity |
| Comparative scout driver | **FORBIDDEN** | S-gate signed |
| Level 1 lock | **FORBIDDEN** | N3 from scout; full prereg |
| Real escrow | **FORBIDDEN** | lock committed; §11 salted protocol |
| Outcome | **FORBIDDEN** | all gates green; explicit authorization |

---

## Exact mandatory revisions

1. **CR-A:** decouple `N2 ≥ 126` from `d_acq ∈ [125, 130]`; define the three-zone
   universe (acquisition / reserved / extrapolation); state the strengthened
   inequalities `2·N2 ≥ k_max·n_max + 1` and `d_acq < k_min·n_min`; rewrite §7 so
   stratum 4 draws from the extrapolation zone, not "reserved cells only"; correct
   "semantically never-contacted" to apply only to stratum 4.
2. **CR-B:** replace the panel table with the corrected one (balance across
   classes, not within); state that "certified solve" means period-representation
   *plus* `2n`-corner extrapolation, and that within-support the certificate
   cannot separate modulus-recovery from single-special-difference memorization —
   a scoped endpoint (or a world-change decision for a cleaner certificate).
3. **CR-C:** supply justified non-comparative values for every
   endpoint/decision-determining quantity before the S-gate; reclassify
   outcome-correlated block failures (non-finite) as censored, not excluded, and
   gate "exclude + FPC" on verified outcome-independence.
4. **MJ-α/β:** state Level 1's detector-not-falsifier asymmetry; correct the scope
   annotation to "online responsiveness under near-matched scale"; put the
   distance-axis option to Kirill.
5. **MJ-γ:** fix the estimand's population to the N3 realized target worlds
   (assignment-conditioned) and state the `N3 = 24` FPC degeneracy.
6. **MJ-δ/ε/ζ:** name and justify the architecture/positional contract for
   length-271/modulus-125; correct the committee early-signal claim; fix
   evaluator aggregation, calibration, and ABSTAIN with values.

---

## Accepted v2 constructions (do not relitigate)

Adjacent-pair supply arithmetic (resolves CR-1's positive-side confound; exact
cardinalities verified); committee disagreement as the acquisition signal (sound
asymptotically; scope only, per MJ-ε); the side-effect-free scorer state-hash
contract; without-replacement selection uniform across arms; the flat opaque
index with fixed `m = 4` (closes CR-2's leak and multiplicity concern); the
salted-commitment escrow (closes MJ-5) and post-B sealed evaluator (MJ-6); the
RMST-as-bounded-cost identity with a solve-count floor; the four-class invalidity
cascade (with the CR-C censoring correction); the N3 precision rule and ceiling;
and the honest negative-space section.

---

## Precise Codex / Cursor authorization

- **Codex — authorized now (gate 1, dummy fixtures only):** the pure `Z/n` world
  + left-fold + EQ oracle + truth-table enumeration checker; the fail-closed
  learner/acquisition/evaluator process separation + import interlocks;
  transcript serialization with salt-capable commitments; adjacent-pair/donor
  bookkeeping (adjacency, disjointness, one-to-one, no-reuse, duplicate-`n`
  rejection, role-assignment commitment). **Constraint:** `N2`, `d_acq`, and the
  difference-zone boundaries must be **parameters**, and the enumeration checker
  must assert the corrected CR-A inequalities — not the current `N2 = d_acq = 125`.
- **Codex — blocked until this v2 is revised and S-gate-reviewed:** the two-level
  pool + verifier (needs the three-zone universe), the certificate builder (needs
  the corrected panel), the committee learner (needs the justified architecture
  and aggregation).
- **Cursor Compose — not yet.** No closed bulk surface until the S-gate signature;
  eligible afterward for mechanical breadth under Codex verification.

---

## Negative-space preservation and execution status

Every signed negative destination is preserved and only strengthened:
`PROOF_CORE` / `PROOF_STRONG` and the C6 annotation; the repaired C4 cascade;
`BOUNDARY_CONTACT_CHOICE` for a C1 negative (now further scope-annotated by MJ-α
as a thin, detector-side boundary); `INSUFFICIENT` / censored / UNKNOWN never
success (now enforced for non-finite blocks by CR-C's censoring rule); the total
three-arm selector with C1 read separately; the RANDOM-superior anomaly recorded,
never rule-altering; donor transcripts encode `n_donor`, never `n_target`; Level 1
never evidence for `PROOF_CORE`.

**All Level 1 execution remains forbidden:** no comparative scout, no lock, no
escrow, no outcome is authorized by this review, and none exists. The revised spec
returns for S-gate review before any comparative datum is created.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
