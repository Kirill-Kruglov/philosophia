# Level 1 scientific specification, v2

Status: `DRAFT_V2_PRE_S_GATE` — standalone; supersedes
`SCIENTIFIC_SPEC_DRAFT.md` (v1, preserved unchanged) after the Opus
(`REVISE_LEVEL1_SPEC`) and Sol (`INFERENCE_SPEC_ELIGIBLE_FOR_CLOSURE`)
reviews. Closure map: `reviews/fable_level1_spec_v2_closure.md`.

This document creates no comparative datum, scout, escrow, lock, or outcome.
Every number in it is a **pre-scout candidate with stated non-comparative
provenance**, final only at the S-gate signature; none derives from an
observed arm difference, and none is an outcome. `N3` is the single intended
post-scout scientific number: its precision rule and capacity ceiling are
frozen here; its realized value is not invented here.

Governing authority, in order: `reviews/LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`;
`fable_levels1_3_claim_graph_v2.md` + `v2_1.md`; `canonical/CLAIM_LEDGER.md`
and `canonical/KILL_MATRIX.md`; then this specification; then the eventual
Level 1 preregistration/lock. A conflict with a signature invalidates this
draft, not the signature.

---

## 1. Scientific question and honest scope

**C1 (chosen contact), scoped honestly:** within the locked finite cyclic
family, learner class, budget, and acquisition rule below, Level 1 tests
whether **target-adaptive probe-scale choice for a hidden modulus** — query
selection coupled to the target learner's own state and answers — reduces
budget-to-certified-solve relative to the same acquisition rule's geometry
donated by an **adjacent-modulus** world (YOKED), with RANDOM-STATIC locating
whether active geometry transfers without any adaptivity.

This is **not** a test of active learning in general. In the `{R,L}`/origin-EQ
interface the modulus `n` is provably the only learner-observable world
parameter (a hidden generator step or hidden origin cancels under EQ — Opus
MJ-2), so "instance adaptation" here *means* probe-scale adaptation to `n`,
and every C1 verdict carries that scope annotation. A negative C1 yields
`BOUNDARY_CONTACT_CHOICE`; it cannot prove or falsify `PROOF_CORE`, forward
shortening, ledger causality, transfer, path credit, or C6. `UNKNOWN` is never
success; a Level 1 success is never evidence for `PROOF_CORE`.

## 2. World, registry, and finite supply (closes Opus CR-1, MJ-1, MJ-2; Sol M2, m1)

World semantics are v1 §2 unchanged (states `0..n−1`, origin 0, `R:+1`,
`L:−1`, left-fold evaluation, one-bit EQ at cost 1, repeats cost 1 and return
the same bit; `n` is the complete world identity; duplicate `n` is never a new
block; the learner receives nothing but its own sequential contact).

**Registered population (candidate, exact).**

- `n ∈ Ω = {66, 67, …, 125}` — 60 consecutive integers, `n_max = 125`.
- **Adjacent disjoint pairs:** Ω is partitioned into 30 fixed pairs
  `(66,67), (68,69), …, (124,125)`. Every inferential block consumes exactly
  one pair: one member is the **target**, the other the **donor**.
- **Size strata (3):** pairs 1–10 (`n ∈ [66,85]`), 11–20 (`[86,105]`),
  21–30 (`[106,125]`). Strata exist for balanced allocation, reporting, and
  finite-population accounting; they are not separate claims.
- **Allocation (locked seeded draws at S-gate):** `N_dev = 6` pairs
  (2 per stratum) → development, permanently excluded from outcome and
  escrow; the remaining **24 pairs are the outcome registry** →
  `N3_max = 24` (8 per stratum).

**Donor distance controlled by design (resolves CR-1's tension).** The
donor is always the target's pair partner, so `|n_target − n_donor| = 1` for
every block — the distance distribution is degenerate at 1 by construction,
not narrated after a broad band. Scientific justification: this is the
**maximally conservative** C1 test — YOKED receives active geometry adapted
to an adjacent modulus, the hardest donated geometry to beat; a positive C1
cannot be an artifact of donor mismatch, and the stratum-width/donor-distance
confound (CR-1) is removed rather than tuned. The distance is still reported
as a (constant) mediator with per-block verification. **Role randomization:**
within each pair, target/donor roles are assigned by one locked seeded coin
per pair at S-gate; the realized assignment is committed and conditioned on
(assignment-conditioned scope, per the signatures).

**Capacity arithmetic (exact).** Disjointness demands
`2·N3 + 2·N_dev ≤ |Ω|`: with pairs, `N3 + N_dev ≤ 30` → `N3 ≤ 24` given
`N_dev = 6`. Per stratum: `N3/3 + 2 ≤ 10` ✓. **If the N3 precision rule
(§9) demands more than 24 blocks:** no lock may be created; the named
options are (a) a **signed registry-extension amendment** (a world change:
new S-gate review; any comparative scout data collected under the old
registry is void and must be re-run), or (b) Level 1 recorded as
`INSUFFICIENT` by design, Kirill deciding. Never a quiet widening.

**Grammar coverage (exact inequalities, closes MJ-1 strengthened).**
`N2 = 125` is the displacement bound (candidate). Two words with
displacements `a, b ∈ [−N2, N2]` realize every difference
`d = a − b ∈ [−2N2, 2N2] = [−250, 250]`.

- **One-period witness:** `2·N2 = 250 ≥ n_max = 125` ✓ (v1's floor).
- **Multi-period evaluator probes (k_max = 2):** the certificate (§7) probes
  `d = k·n` and `k·n ± 1` for `k ∈ {1, 2}`; the strengthened requirement is
  `2·N2 ≥ k_max·n_max = 250` ✓ (met with equality; the extreme cell
  `(125, −125)` realizes `d = 250 = 2·125`).
- **Provable extrapolation stratum:** the **acquisition pool is restricted
  to `|d| ≤ N2 = 125`** (§3). Since `n ≥ 66`, every `k = 2` probe has
  `d = 2n ≥ 132 > 125`, so the double-wrap stratum is **semantically outside
  the contacted difference support for every world in Ω** — by construction,
  not by chance. Single-wrap `d = n ≤ 125` remains contactable (the period is
  learnable from contact). This pair of facts is the anti-lookup engine of §7.

S-gate enumeration obligations: verify pool support `|d| ≤ 125`; verify
`{2n−1, 2n, 2n+1} ∩ [−125, 125] = ∅` for all `n ∈ Ω`; verify wrap-positive
`d = n` realizable for all `n ∈ Ω`; verify residue coverage (§7).

## 3. Candidate pool: one pool, two levels, no semantic leak (closes Opus CR-2, mn-2; mandate §2)

**Semantic level (design geometry; offline only).** A **cell** is an
orientation-canonical displacement pair `{a, b}` with `a, b ∈ [−125, 125]`
and `|d| = |a − b| ≤ 125`. `(u,v)/(v,u)` collapse into one cell; all `(u,u)`
and cancelling constructions live in the `d = 0` class, which is **capped**
at the same per-class realization count as every other class (no trivial-
equality oversampling). The design guarantees, by enumeration, at least
`c_min = 8` cells for every difference magnitude `|d| ∈ [0, 125]`
(candidate; trivially satisfiable — the cell count per `|d|` is
`≈ 251 − |d| ≥ 126`).

**Held-out cell partition (world-independent).** One locked seeded draw
marks **30 %** of cells (uniformly within each `|d|` class) as
**evaluator-reserved**: never realized in the acquisition pool, available
only to the escrowed panel builder (§7). The partition depends only on the
seed and `N2` — never on any `n` — so the pool cannot leak the target.

**Syntactic level (what arms actually see).** A locked, seeded,
arm-independent realization map assigns each non-reserved cell exactly
`m = 4` raw word-pair realizations (candidate): words over `{R, L}` with the
cell's displacements, lengths drawn from a locked padding distribution
(cancelling `RL` insertions), word length ≤ `L_word = 135` tokens
(= N2 + 10 slack). The learner-facing pool is the resulting **flat indexed
list of raw word pairs** — one stable query index shared verbatim by target
ACTIVE, donor ACTIVE, YOKED, and RANDOM-STATIC.

**No privileged semantic metadata.** No arm, policy, or learner ever
receives displacements, difference classes, cell identity, grouping,
multiplicity structure, or any aggregation over the pool: the acquisition
policy sees only raw token sequences plus its own learner state (grouping
visible to a policy would be an abelianization/`net` leak — removed, not
defended). ACTIVE therefore **scores opaque raw realizations**; because
every cell carries exactly `m = 4` realizations, uniform index sampling is
uniform cell sampling and **syntactic multiplicity cannot bias any arm** —
this is the mechanical defense, auditable **offline** by the enumeration
verifier, which alone holds the cell↔index correspondence.

Resolution of "balanced over the periodicity structure": the *pool* is
world-independent and balanced only over world-free difference classes;
periodicity-specific structure (which differences wrap for a given `n`)
lives **only** in the escrowed per-world evaluator panel (§7). Realized
answer balance and answer entropy remain mediators, reported, never matched.

**Shortlist rule (arm-independent).** Each ACTIVE step scores a seeded,
learner-state-independent uniform subsample of `S = 512` not-yet-answered
indices (candidate; resource provenance). The subsample stream is domain-
separated per (block, arm-slot, step) and identical in law for target and
donor ACTIVE. Since the subsample is state- and outcome-independent and the
full support remains reachable in law, the estimand ("argmin-uncertainty
over a locked random S-subset each step") is unchanged by construction —
the shortlist is *part of* the locked acquisition rule, identically for
every ACTIVE run.

**Exhaustion proof.** Non-reserved cells ≈ 0.7 × Σ_{|d|≤125}(251−|d|)
≈ 0.7 × 23,750 ≈ 16,600; realized pairs ≈ 16,600 × 4 ≈ **66,000 ≫ B =
2,000** (33× headroom). All arms select **without replacement** at the raw
index level (a locked design choice, uniform across arms — Sol m3's
repeat-cost rule remains in force for robustness, but by design no arm
repeats). Enumeration verifier obligations: pool cardinality; exact
multiplicity `m` per cell; `d = 0` cap; reserved-cell exclusion; index
stability; identical pool hash across arms; `pool ≫ B`.

## 4. Blocks, arms, and execution (closes Opus mn-1, mn-4; Sol S1)

An **inferential block** = one pair: the target world (three arms: ACTIVE,
YOKED-GEOMETRY, RANDOM-STATIC) + its unique adjacent donor world and the
donor's full-B ACTIVE transcript. Blocks are disjoint (no world in two
blocks, no donor reuse, no duplicate-`n` pseudo-blocks). Seeds and ensemble
members are repeated measures inside a block; queries and checkpoints are
never units.

- **Donor ACTIVE:** the identical acquisition rule for the full `B` steps on
  the donor world; donor solve status never consulted; the complete query-
  index sequence is serialized and **hash-committed (salted) before any
  YOKED derivation**; donor answers and state never transfer.
- **YOKED-GEOMETRY:** replays the donor's committed indices in order against
  its own target oracle, training online on its own answers.
- **RANDOM-STATIC:** a seeded uniform without-replacement index sequence of
  length `B` from the same flat pool.
- **Within-block pairing (mn-1):** the three target arms share **identical
  initialization weights per ensemble member**; all stochastic streams are
  domain-separated by (block, arm, member, purpose); divergence between arms
  comes only from queries, answers, and locked stochasticity.
- Execution order inside a block: donor first (commit), then target arms in
  a fixed committed order. A partial donor, donor reuse, or hash mismatch
  invalidates the block (§10).

## 5. Learner, committee acquisition, and side-effect-free scoring (closes Opus MJ-3, MJ-4; mandate §3)

**Learner (candidate, platform provenance).** The Level 0 earned platform,
minimally adapted: one-layer transformer, `d_model 128`, 4 heads × 32,
MLP 512, no LayerNorm, untied embeddings; vocabulary `{R, L, SEP, PAD}`;
input `u SEP v` (≤ 271 tokens); a binary EQ head (with ABSTAIN derived from
the locked probability rule, §7) read at the final token. Optimizer AdamW,
platform hyperparameters as Level 0 candidates; exact values confirmable at
S-gate from platform precedent only.

**Committee (E = 4, candidate).** Every arm trains an ensemble of `E = 4`
models from paired distinct member inits (shared across arms within a
block). This is the acquisition signal and the capacity unit: **all three
arms carry identical capacity and identical training work** (E models × the
same update schedule), whether or not they use the committee for selection.

**Online update schedule (all arms identical).** At each oracle step: query
issued/received → answer bit → each member records its pre-update
`p̂_equal` → each member takes `U = 1` optimizer step on a seeded minibatch
of `min(32, t)` pairs drawn uniformly from the arm's **own full contact
history** (the locked replay view). No batch training after collection; no
early stop; training always reaches common `B`.

**ACTIVE uncertainty rule (committee disagreement).** Score every candidate
in the step's shortlist by the **committee disagreement** on `p̂_equal`
(variance across the E members); select the maximum; deterministic
tie-break = lowest pool index. Early-signal justification (MJ-3): distinct
member inits disagree on unconstrained inputs from step 0, so the signal
requires no calibration and no data the online learner lacks — the
single-head `|p̂ − ½|` scalar and its calibration circularity are dropped.
Answered-query rule (MJ-4b): already-answered indices are excluded from the
shortlist (without-replacement selection, uniform across arms by design).

**Side-effect-free scorer (MJ-4a, mechanical).** Scoring runs under
no-grad in eval mode; the architecture carries no normalization or dropout
state; scorer RNG is a domain-separated stream that never touches training
streams; caches are forbidden. The contract is enforced by a state-hash
test: (parameters, optimizer state, training-RNG states) hash-identical
before and after a scoring pass. Selection compute (E × S forward passes
per step) is reported separately from oracle cost and training compute and
can never mutate the learner. A fail-closed dataflow test proves the scorer
reaches learner state and raw candidate encodings only — never oracle
truth, evaluator state, hidden `n`, panel structure, or escrow.

**B = 2,000 (candidate, non-comparative provenance).** Resource bound plus
coverage logic: a naive period scan across a stratum needs ≤ 60 queries
(one per candidate `n` in the registry band); `B = 2,000` gives > 30×
headroom for learning inefficiency while consuming ≤ 3 % of the pool.
Confirmed or revised at S-gate only from non-comparative resource evidence
(runtime scouting on development worlds without arm comparisons).

## 6. What the learner never receives (unchanged, restated)

`n`, state identifiers, displacements, difference classes, cell or grouping
structure, sampler metadata, evaluator labels/structure/decisions, donor
answers or state, escrow content, other arms' anything. Enforced by the
fail-closed process/import separation inherited from Level 0 discipline.

## 7. Certified solve: a certificate a lookup table cannot pass (closes Opus CR-3, MJ-6; Sol M1, M3; mandate §4)

**Panel (per target world, escrowed, arm-independent).** Built after lock by
the escrow generator from **evaluator-reserved cells only** (§3), so every
panel item is *semantically* never-contacted (its cell was never realizable
in any arm's pool); raw-word novelty is therefore guaranteed a fortiori.
"Never contacted" is thus defined at both levels: raw (checkable per
transcript) and semantic (guaranteed by the reserved partition).

Strata (all present for every world; counts locked at S-gate):

1. **Residue coverage:** for each residue class `r mod n`, held-out items
   with `d ≡ r (mod n)`, YES/NO balanced within the locked construction.
2. **Wrap positives:** `d = n` (and `d = 2n`, see 4) — true equalities whose
   witnessing difference wraps; **matched near-miss negatives** `d = n ± 1`
   at matched word lengths.
3. **Syntactic-identity controls:** length-matched pairs defeating
   "unequal unless identical."
4. **Periodicity/extrapolation stratum (the teeth):** probes at `d = 2n`
   (must read EQ-true) vs `d = 2n ± 1` (must read EQ-false), `k ∈ {1, 2}`
   selected; by §2 these lie **provably outside every arm's contacted
   difference support** (`2n ≥ 132 > 125`). Correct behavior here requires
   representing the *period*; a displacement-difference lookup over
   contacted support has never seen these classes and cannot answer them.
5. **Symmetry/orientation, word-length, and length-imbalance strata** as
   listed by Sol S3.

**Solve event.** All locked conditions hold at every evaluator checkpoint in
a persistence window: per-stratum accuracy (candidate 0.95, platform
precedent, signature-confirmable), calibration within the locked bound,
ABSTAIN within its per-stratum cap, confident-lie rate under its per-stratum
cap — **with the periodicity stratum (4) carrying its own accuracy, ABSTAIN,
and confident-lie constraints**, so a global average or a global ABSTAIN
budget cannot hide failure exactly where the modulus is tested (CR-3's
abstain-on-the-probes exploit is closed per-stratum). ABSTAIN is never
correct; a non-solve at `B` is right-censored/UNKNOWN, never success.

**Anti-lookup proof obligations (S-gate, by enumeration/construction):**
(i) syntax memorization fails — all panel items are raw-novel;
(ii) displacement lookup over contacted support fails — stratum 4 classes
are uncontactable by §2's inequality; (iii) "unequal unless identical"
fails — stratum 2/3 positives; (iv) `net`-only learners fail — wrap
positives require modular, not integer, equality. The extrapolation to
`d ∈ (125, 250]` is **part of the claimed certificate** — "certified solve"
*means* the period is represented well enough to extrapolate to uncontacted
multiples — and the learner input contract supports it (same grammar,
`L_word` covers `|a|,|b| ≤ 125`; no `n` exposure).

**Evaluator process and sealing (MJ-6).** The evaluator runs **post-B over
frozen checkpoints** at locked cadence; it can signal nothing to training or
acquisition (they have terminated). Its panel, labels, thresholds, and solve
decisions are **sealed** — inaccessible to learners, policies, and
researchers — until explicit outcome authorization. No concurrent
"solved at t" is ever visible during execution.

## 8. Event time, censoring, estimand, inference (closes Opus MJ-7; Sol M1, M2, S2, S4; mandate §5)

- **Cadence and window (candidates):** evaluator checkpoints every
  `C = 50` steps plus step 0 and `B`; persistence window `W_p = 200` steps
  (4 consecutive checkpoints).
- **Event-time convention (closed):** `T` = the step index of the **first
  checkpoint of the earliest window** all of whose checkpoints qualify —
  the first-qualifying-observation convention (Level 0 precedent), with the
  window required to **complete by B**: a qualifying start whose window
  would extend past `B` is censored, not solved. Interval convention: event
  times are known only at checkpoint granularity; `T` is recorded at the
  checkpoint index, and this granularity is part of the locked endpoint.
- **Censoring:** administrative only, at common fixed `B`, for every arm.
  Observed data per arm run: `(min(T, B), δ)`.
- **RMST is exact here (mandate §5 question answered):** with censoring
  only at the common horizon, `RMST_X(B) = E[min(T_X, B)]` exactly — the
  finite-population mean of the bounded cost. Consequence embraced: the
  primary estimator is the stratified finite-population mean of block-level
  `min(T, B)` differences. Consequence guarded: if **no or few solves occur,
  Δ ≈ 0 by arithmetic**; therefore a locked **solve-count floor** (candidate:
  ≥ 25 % of blocks with an observed solve in *each* compared arm) gates every
  predicate — below the floor the comparison is **unresolved →
  `INSUFFICIENT`**, and "all arms reached B" is never equivalence.
- **Benefit scale (one, everywhere):** `β_X = −(stratified FP mean of
  min(T_X, B))`; larger β = better. `SUP`, `EQ`, `NI`, `NONSUP` exactly as
  defined in the signed claim graph, all on β.
- **Seed/member aggregation:** within a block, each arm's replicate runs
  (seed schedule locked at S-gate) reduce to one block-arm summary (mean of
  `min(T,B)`); inference is over blocks only.
- **Estimator (closed):** stratified paired block differences with
  **finite-population correction** per stratum (sampling fraction =
  blocks used / 8 per stratum; MJ-7 — i.i.d. superpopulation reading is
  rejected); simultaneous uncertainty for the **three pairwise contrasts**
  (A−Y, Y−R, A−R) as one family by a locked conservative rule (candidate:
  Bonferroni-adjusted paired intervals; a studentized block bootstrap is the
  named alternative — one is chosen at S-gate). Scope: assignment-
  conditioned, finite registered population Ω, realized role assignment.
- **Selector and routing:** the signed total three-arm selector consumes
  the simultaneous intervals; unresolved, non-transitive, all-censored, or
  incoherent patterns route to `INSUFFICIENT` (Level 2 blocked); the
  RANDOM-superior anomaly is registered, never rule-altering; C1 is read
  only from ACTIVE-vs-YOKED and is never rewritten by selection.
- **N6-L1 margins (provenance, not values from data):** the candidate
  relevance anchor is the **stratum-scan cost** — 60 queries, the price of
  naively probing every candidate modulus in the registry band; a
  contact-choice benefit smaller than one naive scan is a defensible
  "not meaningful" bound, and margins are set at S-gate from this and
  resource anchors, **never** from scout variance or arm differences.

## 9. N3: frozen precision rule and ceiling (closes Sol S5; mandate §1/§5)

- **Ceiling:** `N3_max = 24` blocks (8 per stratum), from §2 capacity.
- **Floor:** `N3_min = 12` (4 per stratum) — the minimum for stratified
  block-variance estimation with FPC (declared design requirement).
- **Frozen precision rule:** after the S-gate and the non-citable
  development contrast scout, `N3` = the smallest block count (balanced
  across strata) whose projected simultaneous interval half-width for the
  primary contrast — computed from scout-estimated block-difference
  variability under the locked estimator with FPC — is ≤ **half the locked
  N6-L1 equivalence margin**, clamped to `[N3_min, N3_max]`.
- The scout may inform this rule with variance, covariance, censoring, and
  feasibility only. If the rule demands `N3 > 24`: no lock; §2's two named
  options (signed registry extension voiding the scout, or `INSUFFICIENT`
  by design), Kirill deciding. If censoring in the scout is so high the
  solve-count floor is unreachable at `N3_max`, the same fork applies to
  `B`/endpoint feasibility **before** any lock — resolved by signed
  amendment, never by post-scout threshold motion.

## 10. Invalidity cascade, executable (closes Sol S6; mandate §6)

Four disjoint classes, evaluated in order:

1. **Design invalidity → `PLATFORM_OR_DESIGN_INVALID`** (whole level, no
   scientific verdict): shuffled-answer certified solve on development
   beyond the locked null tolerance (candidate: zero events); **pre-contact**
   encoding-probe recovery of `n` beyond locked tolerance; global candidate-
   pool mismatch across arms; post-scout change to any frozen item; escrow
   plaintext exposure, regeneration, or malformed generation; systematic
   donor-assignment failure; arm-dependent panel or thresholds.
2. **Block invalidity** (recorded, never silent): donor reuse/partial
   transcript/hash mismatch; target-donor overlap; duplicate-`n` block;
   unequal oracle or update budgets within the block; missing arm run;
   non-finite state; nondeterministic replay divergence; evaluator-seal
   breach local to the block. **Rule:** no blinded replacement exists (the
   registry is finite and replacement invites selection); invalid blocks
   are excluded **with their pair listed in the decision artifact**; if
   valid blocks fall below `N3_min` or below the solve-count floor, the
   outcome is `INSUFFICIENT`; if block invalidity exceeds a locked count
   (candidate: > 4 blocks) it escalates to design invalidity.
3. **Incomplete evidence → `INSUFFICIENT`:** unresolved predicates,
   solve-count floor unmet, all-censored comparisons, non-transitive or
   incoherent simultaneous intervals.
4. **Resolved negative result:** a determinate not-`SUP(ACTIVE, YOKED)`
   under the locked rule → `BOUNDARY_CONTACT_CHOICE` — a first-class
   destination, never conflated with 1–3.

**Post-contact transcript structure remains a legitimate mediator** (never a
leakage gate); only pre-contact encoding leakage invalidates (Opus mn-3
affirmed). Development-world gates (shuffled-answer, pre-contact probe,
parameter-shift report) run before any outcome authorization; the
parameter-shift report is diagnostic unless its locked hard threshold fires.

**Scout boundary (restated exactly):** the development contrast scout may
record endpoint computability, censoring rates, block-level contrast
variance/covariance, seed-within-block variability, runtime/memory/storage,
donor-balance diagnostics — under the outcome-independent resource wall
locked at S-gate. It may not touch margins, thresholds, policies, endpoint,
estimator, arm meanings, N1/N2/B, or strata after any comparison is seen;
violation voids the scout and reopens the S-gate.

## 11. Escrow for a low-entropy world (closes Opus MJ-5, mn-4; mandate §6)

The world registry is finite and the panel rule public, so a bare plaintext
hash is a pre-outcome verification oracle. Corrected protocol (LOCAL_LLAMA
remains generator/witness only; Kirill retains procedural custody; **no
cryptographic independence from Kirill is claimed**):

1. Confidentiality rests on **public-key encryption** to Kirill's
   precommitted key — never on hash secrecy.
2. The integrity commitment is `H(salt ‖ plaintext)` with a **256-bit
   secret salt generated inside the generator environment, stored inside
   the ciphertext, and released only at authorized outcome** — the
   committed digest is useless as a guessing oracle before then.
3. The **plaintext validator runs inside the isolated generator
   environment** (audited deterministic code, not free-form model output);
   it emits only the locked proof/attestation surface (pass/fail, counts,
   salted digests) — plaintext never reaches stdout, logs, shell history,
   research chat, or committed files.
4. **Evaluator output is sealed** (§7) under the same authorization gate.
5. Isolated filesystem; wipe after generation; **one-generation rule**;
   any malformed generation, plaintext exposure, or second generation is
   terminal holdout invalidity.
6. The generator binds: locked generator code/spec hash, seed commitment,
   model identity, prompt, public-key fingerprint, one-generation rule —
   all inside the level lock.

## 12. Gate ledger and implementation boundary (closes Opus O6; mandate §7)

Conservative reconciliation: Sol's "candidate-pool machinery may be
implemented now" is **overridden by Opus CR-2** — until this v2 is reviewed
and the S-gate signed, the pool embeds an open estimand choice. The ledger:

| # | Gate | Status | Contents / closure |
|---|---|---|---|
| 1 | Neutral dummy-fixture substrate | **ELIGIBLE NOW** | pure `Z/n` world + fold + EQ oracle + truth-table enumeration checker; fail-closed learner/acquisition/evaluator process + import interlocks; transcript serialization + **salt-capable** commitment; donor bookkeeping (disjointness, one-to-one, no-reuse, adjacent-pair, duplicate-`n` rejection) — dummy fixtures only |
| 2 | Pool / evaluator / learner implementation | **AFTER v2 REVIEW** | two-level pool + enumeration verifier (§3); reserved-cell partition; certificate builder skeleton (§7, dummy worlds); committee learner + side-effect-free scorer (§5) with state-hash tests |
| 3 | S-gate signature | **OPEN** | every candidate value in this document confirmed or amended; Sol's pre-scout freeze list closed in one signed artifact |
| 4 | Comparative scout driver + execution | **FORBIDDEN** until 3 | capped, non-citable, development-only; records §10 list only |
| 5 | N3 closure + Level 1 lock | **FORBIDDEN** until 4 | §9 rule applied; full preregistration + verifier |
| 6 | Real escrow | **FORBIDDEN** until 5 | §11 protocol, bound in the lock |
| 7 | Outcome driver + execution | **FORBIDDEN** until 6 | explicit execution authorization; all gates green |

## 13. Required implementation tests (delta over v1 §13)

All v1 §13 tests remain, plus: fixed multiplicity `m` per cell and `d = 0`
cap; reserved-cell exclusion from the pool; pool support `|d| ≤ 125` and
stratum-4 uncontactability (`2n > 125` for all `n ∈ Ω`) by enumeration;
scorer state-hash invariance (before/after scoring); committee-disagreement
determinism under fixed seeds; adjacent-pair integrity and role-assignment
commitment; salted-commitment round trip and salt secrecy; evaluator seal
(no read path before authorization); solve-count floor and per-stratum
constraint enforcement as pure functions of frozen observations; the
`INSUFFICIENT` routes of §10 (all-censored, non-transitive, floor-unmet).

## 14. Pre-S-gate choice register (superseding v1 §15)

Closed by this document (candidate values, signature-confirmable): registry
Ω and pairing; strata; `N_dev`; `N3_min/N3_max` and the N3 precision rule;
`N2 = 125`; pool support bound; reserved fraction 30 %; `m = 4`; `S = 512`;
`L_word = 135`; `B = 2,000`; `E = 4`; `U = 1`; replay view; committee-
disagreement rule + tie-break + without-replacement; RANDOM design;
event-time convention; `C = 50`; `W_p = 200`; RMST-as-bounded-cost
identity + solve-count floor; stratified FPC estimator + simultaneous
family; benefit orientation; N6 provenance anchor; invalidity cascade;
escrow protocol. **Still open for the S-gate signature:** final numeric
confirmations of every candidate above; exact panel stratum counts and
per-stratum thresholds (accuracy, calibration statistic and bound, ABSTAIN
and confident-lie caps); seed schedule; leakage-gate tolerances;
Bonferroni-vs-bootstrap choice; resource wall; and the signed README/
KILL_MATRIX text (already amended at HEAD — verified, Opus mn-5 closed).

No number in this document is an outcome; none was chosen from a
comparison; the only post-scout scientific number is `N3`, and its rule and
ceiling are frozen above.
