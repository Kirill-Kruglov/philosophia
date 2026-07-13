# Level 1 scientific specification, v3

Status: `DRAFT_V3_FOR_FINAL_S_GATE_REVIEW` — standalone and complete;
supersedes v2 (preserved) after the Opus (`REVISE_LEVEL1_V2_SPEC`) and Sol
(`REVISE_LEVEL1_V2_INFERENCE`) S-gate reviews. Closure map:
`reviews/fable_level1_spec_v3_closure.md`.

Every value that can move a trajectory, solve event, interval predicate,
invalidity route, or estimand is **exact** in this document, with stated
non-comparative provenance. The single post-comparative-scout number is
`N3`, governed by the fully frozen rule in §9. No code, feasibility run,
comparative datum, scout, escrow, lock, or outcome is created here.

Governing authority: `reviews/LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`; the
claim graph v2 + v2.1; `canonical/CLAIM_LEDGER.md` / `KILL_MATRIX.md`; then
this document; then the eventual lock.

---

## 1. Question, scope, and the detector asymmetry

**C1, correctly named:** within the locked design below, does **online
responsiveness under near-matched probe scale** — coupling each next query
to the target learner's own evolving state and answer stream — reduce
budget-to-certified-solve relative to replaying an adjacent-modulus donor's
active geometry (YOKED), with RANDOM-STATIC locating untargeted geometry?

**Adjacent-only, with honest asymmetric scope (governing choice A).** The
donor is always the target's adjacent pair partner (`|Δn| = 1`). Why no
second distance axis in v3: C1 is a **modifier**, not a `PROOF_CORE`
conjunct; distance 1 is the strongest *positive* detector (a win over
near-ideal donated geometry cannot be a mismatch artifact), while a second
donor axis would multiply blocks, comparisons, and the one-week budget for
a claim the programme does not need. The cost is stated, not hidden:
**Level 1 is structurally a detector, not a falsifier, of choice benefit**
(Opus MJ-α). A resolved null supports only the scope-annotated
`BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1` carried by the canonical
`BOUNDARY_CONTACT_CHOICE`: it says nothing about larger donor distances or
active learning generally, and nothing against `PROOF_CORE`. The scale
axis is largely controlled out, not tested (Opus MJ-β). A C1 null is
additionally scoped to the locked acquisition policy of §5, whose early
behavior is near-random (§5). Signature:
`I_ACCEPT_ADJACENT_ONLY_C1_DETECTOR_SCOPE`; alternative:
`I_REQUIRE_LEVEL1_DISTANCE_AXIS` — a redesign reopening world supply,
arms, multiplicity, budget, and review.

## 2. Population, allocation, and estimand frame (governing choice B; closes Opus MJ-γ; Sol M1, M6, Y1)

World semantics: unchanged (states `0..n−1`, origin 0, `R:+1`, `L:−1`,
left-fold, one-bit EQ at cost 1; `n` is the world identity; the learner
receives only its own sequential contact).

- **`P`** = the 30 adjacent pairs `{(66,67), …, (124,125)}` over the
  registry `{66..125}`; strata `h ∈ {1,2,3}` = pairs 1–10, 11–20, 21–30.
- **`D`** (development): 2 pairs per stratum, drawn by the exact locked
  procedure: a SHA-256 counter stream keyed by the public string
  `"philosophia-L1v3-alloc/dev"` selects, within each stratum, 2 of the 10
  pair indices by rejection-free Fisher–Yates over the sorted index list.
  Committed at S-gate; permanently excluded from outcome and escrow.
- **`O = P \ D`**, `|O| = 24`, `N_h = 8` per stratum — **the outcome
  frame**.
- **Role assignment:** one bit per pair from the stream keyed
  `"philosophia-L1v3-alloc/role"`: 0 → lower `n` is target, 1 → higher.
  Assigned once, committed, conditioned on.
- **`R_h`:** `n_h = N3/3` pairs sampled from each `O_h` by stratified
  simple random sampling without replacement (stream key
  `"philosophia-L1v3-alloc/sample"`), inclusion probability `π_h = n_h/8`.
- **Estimand:** the finite mean over **all 24 role-assigned outcome
  pair-blocks**, conditional on `D`, the role assignment, and the locked
  finite learner-seed schedule (§8):
  `Δ_AY = Σ_h (1/3) · mean_{p ∈ O_h}[Y_YOKED(p) − Y_ACTIVE(p)]`, with
  `Y_X = ` seed-aggregated `min(T_X, B)`; positive favors ACTIVE.

**Why not Opus's realized-`N3` population:** defining the population as
whatever was run would make the FPC and any generalization to the
registered outcome frame meaningless — inference would be descriptive of
an arbitrary subset with no design-based bridge to the frame the lock
registers. The design-based reading keeps `N3 < 24` inference honest
(known `π_h`, FPC) and degenerates gracefully: **at `N3 = 24` the outcome
frame is a census — world-sampling variance is exactly zero and the claim
is descriptive of those 24 role-assigned blocks under the conditioned
seed schedule.** No scope is implied over all 60 integers, unsampled
role-reassignments, or any algorithmic-seed superpopulation; seeds are
**conditioned on** (Sol M6), and this reading cannot be switched after
outcome.

## 3. Three-zone support with exact arithmetic (closes Opus CR-A, X2; Sol C1, C2; mandate §1)

Named quantities (exact):

| Quantity | Value | Constraint satisfied |
|---|---|---|
| `A_word` — max individual word displacement | **126** | `2·A_word = 252 ≥ 2·n_max + 1 = 251` ✓ |
| Max raw word length | **136** | `= A_word + 10` padding slack; a word of displacement `a` has length `|a| + 2p`, `p ∈ {0..5}` locked per-realization draw (parity: length ≡ `|a| mod 2`) |
| Model input | **273 tokens** | `= 2·136 + 1 (SEP)`; §5's positional contract covers 273 |
| `d_acq` — acquisition difference cap | **125** | `n_max = 125 ≤ d_acq` (every `d = n` contactable) and `d_acq < 2·n_min − 1 = 131` (every `2n−1 ≥ 131`, `2n`, `2n+1` outside acquisition support) ✓ |

**Zones** (cells are orientation-canonical `{a, b}`, `a, b ∈ [−126, 126]`):

1. **Acquisition cells:** `|d| ≤ 125`, non-reserved — the world-independent
   pool presented to arms. Cell count `253 + Σ_{d=1}^{125}(253 − d) =
   24,003`; 70 % non-reserved ≈ 16,802 × `m = 4` realizations ≈ **67,208
   raw pairs ≈ 33.6 × B** (exhaustion impossible).
2. **Reserved raw-novel cells:** the other 30 % (locked seeded draw within
   each `|d|` class, key `"philosophia-L1v3-pool/reserve"`), `|d| ≤ 125` —
   never realized for arms; used by the evaluator for **syntax/robustness
   strata. They are raw-novel but NOT difference-novel**: EQ depends only
   on `d mod n`, so a difference lookup over contacted support passes them
   (the v2 claim that all panel items are semantically never-contacted is
   withdrawn; it is true only of zone 3).
3. **Extrapolation cells:** `|d| ∈ (125, 252]` — **evaluator-only**, never
   admissible to any arm; contains every `2n ∈ [132, 250]` and every
   realizable `2n ± 1 ∈ [131, 251]` (`2n+1 = 251` at `n = 125` is realized
   by `a = 126, b = −125` — the v2 edge failure is closed by
   `A_word = 126`). Raw- **and** difference-novel.

**Marginal coverage vs corner composition.** Acquisition cells include
individual displacements up to `±126` (e.g. `{126, b}` with
`b ∈ [1, 126]` has `d ≤ 125`), so the **full marginal range of individual
displacements and word lengths used by zone 3 is contacted in
acquisition** wherever mathematically possible. What zone 3 alone
withholds is the **composition**: extreme opposite-sign displacement pairs
(`a ≈ +n, b ≈ −n`). The irreducible remaining scope (Opus CR-B): the
load-bearing test is novel **difference/composition**, not unseen token
length — and "certified solve" therefore jointly certifies a learned
period **and** extrapolation to a novel opposite-displacement composition.
This is intentionally conservative: **a pass is strong; a failure is
ambiguous and yields censoring — never a claim that the learner failed to
recover `n`.**

Accepted unchanged from v2: the opaque flat index (policies see raw tokens
only; the cell↔index map lives offline in the enumeration verifier), fixed
multiplicity `m = 4` per cell (the `d = 0` class is capped at the same
**realization count = 4 per cell** and its cell count is whatever
enumeration gives; no oversampling), world-independent pool, offline-only
semantic map, side-effect-free policy boundary.

## 4. The panel: exact, algebraically valid, sealed (closes Opus CR-B, X3, mn-iii; Sol C3, M3; mandate §2)

EQ is YES **only** at residue `d ≡ 0 (mod n)`; every nonzero residue class
is single-label NO — balance is across matched classes/strata, never
within one residue. The panel has a **world-independent exposed surface**:
exactly **188 items** in 5 strata with fixed counts, fixed ordering
convention, and fixed ids for every world; all target-specific structure
(which `d` values, labels) exists only inside the sealed evaluator.

| Stratum | Count | Labels | `d` support and exact construction | Raw novel | Diff novel | Length rule | Role / anti-lookup force |
|---|---|---|---|---|---|---|---|
| S1 residue coverage | 124 | 124 NO | item `i`: residue `r_i = 1 + ((i−1) mod (n−1))`, `d_i = r_i ∈ [1,124]` (`< n`, so never ≡ 0 and never = `n`); zone-2 cell with difference `d_i`, lowest unused reserved index; covers every nonzero residue ≥ once for all `n ∈ [66,125]` (exactly once at `n = 125`) | yes | **no** | locked draw | breadth/false-space; **a difference lookup passes** |
| S2 single-wrap + near-miss | 16 | 8 YES / 8 NO | 8 × `d = n`; 4 × `d = n−1`; 4 × `d = n+1` (zone 2 except `n = 125`, where `d = 126` items come from zone 3 — deterministic, sealed) | yes | no (`d = n` was contactable) | NO items length-matched to YES | special-difference and neighbors; a lookup that contacted `d = n` passes |
| S3 syntactic identity | 16 | 8 YES / 8 NO | 8 × `d = 0` with `u ≠ v` (distinct realizations); 4 × `d = 1`, 4 × `d = 2` | yes | no | matched | defeats "unequal unless identical" |
| S4 extrapolation (**the sole anti-difference-lookup tooth**) | 16 | 8 YES / 8 NO | 8 × `d = 2n`; 4 × `d = 2n−1`; 4 × `d = 2n+1`; zone 3, corner construction `a = ⌈d/2⌉, b = −⌊d/2⌋` | **yes** | **yes** | matched within stratum | the certificate's teeth: uncontactable differences; tests period + corner composition jointly |
| S5 length/imbalance robustness | 16 | 8 YES / 8 NO | 4 × `d = 0` (both words length ≥ 100); 4 × `d = n` (length imbalance ≥ 60); 4 × `d = n+2`; 4 × locked `d ∈ [3,125] \ {n, n+2}` at length ≥ 100 | yes | no | as stated | robustness; no anti-lookup force |

Totals: 32 YES / 156 NO — the global imbalance is algebraically inherent
and harmless because **all solve conditions are per-stratum** (§6); no
global-accuracy criterion exists.

**Enumeration obligations (S-gate, at both registry edges):** at `n = 66`,
S4 uses `d ∈ {131, 132, 133}` — all `> 125` (zone 3) and realizable; at
`n = 125`, S4 uses `d ∈ {249, 250, 251}` — all `≤ 252` and realizable
(`251` via `(126, −125)`); S1's `d_i = r_i` rule is valid for every
`n ∈ [66, 125]`; S2's near-miss zone assignment is deterministic; every
item's words fit length 136 and the 273-token input; the exposed panel
surface (counts, ids, ordering, stratum names, hashes) is byte-identical
across worlds.

## 5. Fully executable learner contract (closes Opus MJ-δ, MJ-ε, MJ-ζ; mandate §3)

No "Level 0 hyperparameters" placeholder; this is a **new architecture
contract for the length-273 / modulus-125 regime**, chosen from declared
conservative design requirements. Level 0's 3-token success is cited only
as engineering (determinism/cadence) precedent, never as capacity
evidence.

- **Tokenization:** vocabulary `{PAD=0, R=1, L=2, SEP=3}`. Input
  `u SEP v`, **left-padded** with PAD to exactly 273 tokens; readout
  always at position 272 (fixed). PAD key positions are masked out of
  attention (score = −∞).
- **Positional scheme:** learned positional embeddings, 273 positions.
- **Architecture:** **2 transformer layers** (composition depth for
  segment comparison — a declared conservative requirement; 1 layer is
  not asserted sufficient at this length), `d_model = 128`, 4 heads × 32,
  MLP 512, ReLU, **pre-LayerNorm** (training stability at depth 2 and
  length 273 — a deliberate departure from Level 0, justified by the new
  regime), no dropout (determinism), untied embeddings.
- **Output head:** linear `d_model → 2` logits at position 272; softmax;
  `p̂_equal` = the YES probability. **Training loss:** softmax
  cross-entropy against the oracle bit.
- **Initialization:** every weight matrix `~ Normal(0, 1/√fan_in)`;
  biases and LayerNorm offsets 0, LayerNorm gains 1; head
  `Normal(0, 1/√d_model)`. Committee `E = 4` members with distinct member
  inits; **member inits are shared across the three arms within a block**
  (identical per member), divergence arising only from queries, answers,
  and locked domain-separated streams.
- **Evaluator ensemble aggregation (exact):** `p̄ = mean of the 4 members'
  p̂_equal`. Predicted label = YES iff `p̄ ≥ 0.5`; **ABSTAIN iff
  `|p̄ − 0.5| < 0.10`** (an ABSTAIN is never a correct answer).
- **Optimizer:** AdamW, `lr = 1e-3` (constant; no scheduler/warmup — a
  declared conservative online-learning choice), `weight_decay = 0.01` on
  weight matrices only (no decay on biases, LayerNorm parameters, or
  embeddings), betas `(0.9, 0.98)`, `eps = 1e-8`.
- **Online step at oracle step `t` (exact order):** receive bit → each
  member records pre-update `p̂` → minibatch = the newest pair **plus**
  `min(31, t−1)` distinct history pairs drawn uniformly without
  replacement (stream `"replay/(block,arm,member)"`) → per member:
  forward, backward, `optimizer.step`, `zero_grad` (`U = 1`) → optional
  checkpoint. No batch training after collection; no early stop; all arms
  run to common `B`.
- **Acquisition rule (ACTIVE and donor ACTIVE, identical):** score each
  shortlist candidate by the **population variance across the 4 members'
  `p̂_equal`**; select the argmax; tie-break = lowest pool index.
  Shortlist = 512 not-yet-answered indices drawn uniformly by the
  learner-state-independent stream `"shortlist/(block,arm-slot,step)"`;
  target ACTIVE and donor ACTIVE draw from their own streams, identical
  in law; YOKED inherits the donor's realized draw inside the committed
  transcript (matched in law, noted in the estimand). Selection is
  without replacement; answered indices are excluded.
- **Honest characterization (Opus MJ-ε):** committee disagreement at or
  near initialization is **noise, not knowledge** — the rule is a locked
  randomized heuristic whose early selections are near-random and which
  may become epistemic only after contact. A C1 null is scoped to this
  policy.
- **Side-effect-free scorer:** no-grad, eval mode, no dropout/BN state,
  domain-separated scorer RNG, no caches; state-hash equality of
  (parameters, optimizer, training RNG) before/after scoring is a
  required test. Selection compute (`≤ B·512·4` forwards/run) is reported
  separately and can never mutate the learner.
- **Checkpointed state / deterministic resume:** all 4 members'
  parameters + optimizer moments, every named RNG stream state, contact
  history, answered-index set, step counter; resume must reproduce
  identical subsequent state hashes or route to §7's process-failure
  rule.
- **`B = 2,000`** (declared conservative: ≥ 33× naive 60-query registry
  scan; ≤ 3 % of pool).

**Feasibility risk and its contract (not run, not implemented).** Whether
this architecture certifies anything within `B` is a real unknown (Opus
MJ-δ). If observation is genuinely required before signature, the only
permitted instrument is the **non-comparative feasibility check**:
development worlds only; **one arm class only (RANDOM-STATIC schedule)**;
no second arm, no contrast, no escrow; permitted outputs — runtime,
memory, artifact sizes, loss finiteness, panel computability, and the
single-arm censoring indicator; hard cap ≤ 2 development pairs × 1 seed
× B steps and ≤ 12 h wall; no effect or margin tuning of any kind; any
resulting change to architecture/`B` is a **signed pre-S-gate amendment**.
This document defines the contract and does not execute it.

## 6. Exact solve event (closes Opus CR-C endpoint half, MJ-ζ; Sol C4, Y3; mandate §4)

All values below are finite-sample count rules, unit-testable, with
non-comparative provenance ("certified" = near-perfect performance on the
decisive structure, argued from binomial tail bounds against chance and
lookup baselines — never expected model performance, never a scout
product).

- **Per-stratum accuracy (counts):** S1 ≥ **118/124**; S2 ≥ **15/16**;
  S3 ≥ **15/16**; S4 ≥ **15/16**; S5 ≥ **14/16**. (Chance at `p = 0.5`
  passes S4 with probability ≈ 2.6·10⁻⁴; a difference lookup scores ≈ the
  NO base rate on S4's YES items and fails; provenance = these tail
  bounds plus the certificate role, S4/S2/S3 strict, S5 marginally looser
  as robustness.)
- **ABSTAIN:** never correct; counted as incorrect in the accuracy
  counts; **additional per-stratum cap = 2 ABSTAINs** (prevents
  abstain-flooding a stratum while the count rule is met elsewhere).
- **Confident lie:** a non-abstained wrong prediction with `p̄ ≥ 0.9` or
  `p̄ ≤ 0.1`. **Cap: 0 in S4; ≤ 1 in each other stratum.** (Certification
  excludes confident falsehood exactly where the modulus is tested.)
- **Calibration:** Brier score of `p̄` over non-abstained panel items
  **≤ 0.10** (perfect ≈ 0, chance = 0.25; finite-sample computable).
- **Leakage tolerances (development gates):** shuffled-answer runs —
  **zero** certified solves tolerated (any = design invalid);
  pre-contact encoding probe predicting `n` from serialized pre-contact
  artifacts — top-1 accuracy must be **≤ 1/6** (= 2× chance over the 12
  development worlds; above = design invalid). **Parameter-shift report:
  diagnostic only, no hard threshold** (stated explicitly).
- **Persistence arithmetic (exact; closes Sol C4):** cadence `C = 50`
  (checkpoints at steps 0, 50, …, 2000); a qualifying window is **five
  consecutive checkpoints `t, t+50, t+100, t+150, t+200`** (inclusive
  200-step span), all satisfying every condition above. **Step 0 may
  start an event** (`T = 0` is legal; an untrained pass would indict the
  leakage gates, which are separately tested). **Last eligible start:**
  `t = B − 200 = 1,800`. A window extending past `B` never qualifies
  (censored). **Missing checkpoint** inside a candidate window: a
  process failure routed by §7 (never a silent non-qualifying
  observation). `T` = the first checkpoint of the earliest complete
  qualifying window, computed **post-B from sealed evaluation only**;
  non-solve at `B` is right-censored/UNKNOWN, never success.

## 7. Failure routing without survivor bias (closes Opus CR-C censoring half; Sol M5, Y5; mandate §6)

Cause classes and deterministic routes, frozen before outcome:

1. **Outcome-related scientific failure** — a non-finite learner
   trajectory (loss/parameter divergence): the arm is recorded
   **censored at `B`** (cost `B`, no solve); the block is **retained**.
   Never excluded, never invalidating.
2. **Process failures** — missing/corrupt artifacts, hardware failure,
   deterministic-replay mismatch, missing checkpoint, evaluator-seal
   breach, unequal realized budgets, non-resumable run: if the failure
   is **verifiably outcome-independent by mechanical evidence recorded
   before any unsealing** (hash mismatch log, hardware fault record)
   **and** the affected run can be deterministically re-executed from
   committed inputs reproducing identical prefix hashes, **exactly one
   logged re-execution is permitted**; a second failure, a failure that
   cannot be shown outcome-independent, or any seal breach →
   **`PLATFORM_OR_DESIGN_INVALID`** (whole level, fail-closed). No block
   exclusion, no survivor FPC recomputation, no replacement, no
   discretionary "up to four" — those v2 rules are withdrawn.
3. **Design invalidity** (as in v2 §10: leakage-gate failure, pool
   mismatch, post-freeze change, escrow violation, systematic assignment
   failure) → `PLATFORM_OR_DESIGN_INVALID`.
4. **Incomplete evidence** → `INSUFFICIENT` (unresolved predicates,
   determinacy guard unmet, non-transitive intervals).
5. **Resolved negative** → `BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1` under
   §8's predicates — a first-class destination.

Classification is by **cause, fixed pre-outcome — never reclassified from
observed performance**.

## 8. Exact estimator, predicates, and selector (closes Opus MJ-γ; Sol M2, M3, M4, M6, Y4, Y6; mandate §5)

- **Seed schedule (conditioned, finite):** 2 seed replicates per
  block-arm (replicate = fresh member-init set + streams, shared across
  the three arms within the block as always); block-arm cost `Y` = the
  mean of the 2 replicates' `min(T, B)`. Committee members are one
  learner, never extra seeds. Provenance: minimal replication that
  averages seed noise inside the one-week budget; declared conservative.
- **Estimator (stratified paired finite-population over `O`):** stratum
  weights `W_h = 8/24 = 1/3` exactly; block difference for contrast
  "X beats Y" `D = Y_Y − Y_X` (cost scale; positive favors X);
  `Δ̂_{X,Y} = Σ_h (1/3)·mean_{R_h}(D)`; variance
  `Σ_h (1/9)·(1 − n_h/8)·s_h²/n_h` (FPC explicit); **degrees of freedom
  by Satterthwaite** across the three strata (exact formula frozen);
  **census rule:** at `N3 = 24`, FPC = 0, intervals collapse to points,
  and predicates compare point values to margins — the decision is an
  exact descriptive statement about the 24-block frame under the
  conditioned seed schedule.
- **Primary simultaneous method:** **Bonferroni-adjusted paired
  t-intervals, familywise α = 0.05 (α/3 = 0.0167 two-sided per
  contrast)** over the family {A−Y, Y−R, A−R}. The studentized block
  bootstrap is **sensitivity only** and can never change a predicate.
- **N6 margin (single, frozen):** `m = 60` queries on the benefit scale —
  the cost of one naive full-registry-band scan; a benefit smaller than
  one naive scan is not meaningful contact-choice value, and the same
  relevance quantum symmetrically defines "operationally equivalent."
  One margin governs all four predicates for that stated scientific
  reason. Exact predicate rules (benefit scale, `β_X − β_Y`):
  - `SUP(X, Y)`: lower simultaneous bound **> +60**;
  - `EQ(X, Y)`: full simultaneous interval **⊂ [−60, +60]**;
  - `NI(X, Y)`: lower simultaneous bound **> −60**;
  - `NONSUP(X, Y)`: upper simultaneous bound **< +60**.
- **Determinacy guard (replaces the blunt 25 % floor; closes Sol M2):**
  - all-censored compared arms resolve **no** predicate (their interval
    is degenerate at 0 by arithmetic; the guard, not the arithmetic,
    routes them): → `INSUFFICIENT`;
  - `SUP` has **no solve floor**: one arm solving while the other is
    censored yields real `D > 0` differences, and if the locked interval
    clears `+60`, `SUP` resolves — informative one-sided bounded-cost
    contrasts are kept;
  - **`EQ`, `NI`, and `NONSUP` each additionally require ≥ 1 observed
    solve event in each compared arm** across the battery — an
    administrative tie at `B` can never earn equivalence or a
    boundary-supporting predicate;
  - every guard is pre-data, mechanical, and evaluated before the total
    selector consumes the predicates.
- **C1 reading:** `SUP(ACTIVE, YOKED)` → C1 earned (scope §1); resolved
  `NONSUP(ACTIVE, YOKED)` → the boundary of §7.5; anything unresolved →
  `INSUFFICIENT`. The signed total three-arm selector is unchanged;
  RANDOM-superior remains a registered anomaly that never rewrites C1;
  non-transitive or incoherent simultaneous patterns route to
  `INSUFFICIENT` and block Level 2.

## 9. N3: frozen rule (closes Sol Y5; mandate §5)

`N3 ∈ {12, 15, 18, 21, 24}` (multiples of three, balanced). After the
S-gate and the comparative development scout, `N3` = the **smallest**
balanced value whose projected Bonferroni simultaneous half-width for the
primary contrast — from scout-estimated block-difference variability under
the frozen estimator with FPC — is **≤ 30 (= m/2)**. **There is no clamp:**
if the projection fails at `N3 = 24`, no lock may be created; the only
routes are the already-named signed redesign
(`I_REQUIRE_LEVEL1_DISTANCE_AXIS`-class registry/world amendment, voiding
the scout) or recording Level 1 `INSUFFICIENT` by design — Kirill's
decision. The scout may inform this rule with variance, covariance,
censoring, and feasibility only.

## 10. Escrow and sealing (unchanged from v2 §11, restated as binding)

Public-key-encryption confidentiality (Kirill's precommitted key);
`H(salt ‖ plaintext)` integrity with a 256-bit secret salt inside the
ciphertext, released only at authorized outcome; sealed in-generator
validator emitting only the locked attestation surface; sealed evaluator
outputs (§6) until outcome authorization; isolated filesystem, wipe,
one-generation rule, malformed generation = terminal; LOCAL_LLAMA is
generator/witness only; Kirill holds procedural custody; no cryptographic
independence is claimed.

## 11. Gate sequence (mandate §7)

| # | Gate | Status |
|---|---|---|
| 1 | Neutral parameterized substrate (Z/n world, fold, EQ, truth enumeration; fail-closed process/import interlocks; salt-capable commitments; pair/role/donor bookkeeping) — `A_word`, `d_acq`, zone bounds as **parameters** with the §3 inequalities asserted by the enumeration checker | **ELIGIBLE NOW** (dummy fixtures) |
| 2 | Corrected pool/panel/learner implementation (three-zone pool + verifier; 188-item panel builder; §5 learner + scorer) | **AFTER final v3 review** |
| 3 | Non-comparative feasibility driver + its single capped execution (§5 contract) | **OPTIONAL, after gate 2; before gate 5 if used; any change = signed pre-S-gate amendment** |
| 4 | Final v3 S-gate review (Opus X, Sol Y) | **THIS document's next step** |
| 5 | Kirill's S-gate signatures (§ closure memo packet) | after 4 |
| 6 | Comparative development scout (capped, non-citable) | after 5 |
| 7 | N3 closure + preregistration lock | after 6 |
| 8 | Real escrow (§10) | after 7 |
| 9 | Outcome driver + execution | after 8, explicit authorization |

No comparative scout, lock, real escrow, or outcome is authorized by v3.

## 12. Implementation tests (delta over v2 §13)

Add: three-zone boundary enumeration (`2n ± 1` outside acquisition for all
`n ∈ Ω`; `251` realizable; S1 residue rule at both edges); 188-item
world-independent exposed panel surface (byte-identity across worlds);
five-checkpoint window arithmetic incl. step-0 start, last start 1,800,
and past-B censoring; per-stratum count rules, ABSTAIN cap, confident-lie
caps, and Brier bound as pure functions of frozen observations; the §7
routing table incl. the one-re-execution rule; the §8 predicates incl. the
determinacy guard and census collapse; allocation streams reproducibility
(dev/role/sample draws from the committed keys).

---

*Every constant above is exact and non-comparative in provenance; the
closure memo carries the full constants table, the disposition of every
review finding, and the signature packet. `N3` alone waits for the scout,
under §9's rule, which contains no clamp.*
