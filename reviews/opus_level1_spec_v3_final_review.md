# Opus 4.8 X-line — Level 1 v3 final pre-signature review

Reviewer: Opus 4.8 (adversarial scientific + systems). Target:
`experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md`, against the signed
claim graph, Sol's v2 S-gate review, and Fable's v3 closure memo. Stage: final
pre-signature. Standard: **bit-level implementability** — a separate implementer
must reproduce the same pool, panel, trajectory, event, and decision without an
unreviewed choice. This review creates no code, feasibility/comparative datum,
escrow, lock, or outcome, tunes no constant, and predicts no arm. All arithmetic
below was recomputed independently.

---

## Verdict

**`REVISE_LEVEL1_V3_CONTRACT`**

v3 closes every finding from the prior rounds at the design level, and the
three-zone arithmetic is now correct (independently verified: `A_word = 126` gives
`2·A_word = 252 ≥ 251`; `d_acq = 125` satisfies `125 < 2·n_min − 1 = 131`; the
`n = 125` near-miss `251` is realizable via `(126, −125)`; cell count `= 24,003`).
But it is not signable, for one scientific reason and two implementability
reasons, each requiring a **v3.1 addendum**:

1. **The certificate's sole anti-lookup stratum is defeated by a trivial
   feature (Critical, scientific).** In S4, YES items (`d = 2n`) are constructed
   symmetric (`|a| = |b| = n`, even total displacement) and NO items (`d = 2n ± 1`)
   asymmetric (`|a| ≠ |b|` by 1, odd total). Verified at both edges. A learner
   keying on **displacement-magnitude equality or parity** — both far easier than
   modular period recovery, and the magnitude comparison is a byproduct of the
   `net` skill the learner must acquire anyway — passes S4 with no representation
   of `n`. The teeth do not bite.

2. **The pool/panel/realization/allocation generators are not specified to the
   bit level (Critical, implementability).** The SHA-256→integer/permutation/
   sample algorithm is never given (and "rejection-free Fisher–Yates" is either
   modulo-biased or under-specified); the per-`|d|`-class 30 % rounding, cell
   enumeration/index order, raw-realization token construction (padding placement,
   RL vs LR, distinctness, collision rejection, `p`-distribution), and
   cross-stratum reserved-cell consumption order are all unfixed. Two faithful
   implementers produce different pools, panels, and learner inputs.

3. **The transformer/optimizer contract has bit-level gaps (Critical,
   implementability).** Attention direction (causal vs bidirectional), attention
   biases and scale, all-masked-row behavior, a final LayerNorm and its epsilon,
   weight-init draw order, dtype/device/determinism, gradient clipping, loss
   reduction, and the exact seed-key strings are unspecified. Two faithful
   implementers produce different trajectories.

None rejects the world or the design (not `BLOCKED_LEVEL1_WORLD`), and the
certificate is repairable (not `REJECT_LEVEL1_V3_CERTIFICATE`) — the S4 fix is a
one-line change to parity-matched symmetric near-misses. But as written the
contract fails the reproducibility standard and the teeth are compromised.
**All Level 1 execution — scout, lock, escrow, outcome — remains forbidden.**

---

## Findings, ordered

### Critical

- **C-1 (X2) — S4 near-misses leak the label through symmetry and parity.**
  Corner construction `a = ⌈d/2⌉, b = −⌊d/2⌋`: for `d = 2n`, `a = n, b = −n`
  (`|a| = |b|`, even); for `d = 2n ± 1`, magnitudes differ by 1 (odd). So the
  decisive stratum is separable by magnitude-equality/parity, not modular
  divisibility, and the accuracy (`≥ 15/16`) and zero-confident-lie caps do not
  catch it (a feature-classifier is *correct and confident* on S4). Because an
  odd `d` can never be realized symmetrically (`a = −b ⟹ d` even), the fix must
  make the negatives **even and symmetric**: replace `d = 2n ± 1` with
  `d = 2n ± 2` (`a = n ± 1, b = −(n ± 1)`), which is symmetric, even, still
  `≢ 0 mod n` (remainder 2 or `n − 2`), and realizable and uncontactable at both
  edges (`{130,134}` at `n=66`; `{248,252}` at `n=125`, the last via `(126,−126)`).
  Verified. Alternatively, decouple realization symmetry from the label across the
  stratum so no surface feature correlates — but the parity constraint makes the
  even-negative construction the clean solution.

- **C-2 (X1) — the generators are not bit-reproducible.** Determiners of learner
  input that are currently prose, not algorithm: (a) the keyed-SHA-256 stream →
  unbiased integer / Fisher–Yates / without-replacement-sample method (byte
  consumption, rejection threshold, counter encoding) — used by *every* draw
  (dev/role/sample allocation, reserved partition, realization padding, shortlist,
  replay minibatch); "rejection-free Fisher–Yates" is a red flag (unbiased small-
  range integers generally require rejection). (b) The exact integer for "30 %
  reserved" per `|d|` class (floor/round/ceil of `0.3·(253−|d|)`). (c) The cell
  enumeration order that fixes the flat index (trajectory-relevant: RANDOM samples
  indices, ACTIVE tie-breaks on lowest index). (d) The raw-realization token
  generator: where cancelling pairs are inserted, RL vs LR, how the 4 distinct
  realizations and distinct `d=0` words are chosen, collision rejection, and the
  `p ∈ {0..5}` draw law. (e) The "lowest unused reserved index" cross-stratum
  consumption order. Until these are algorithms, no two implementers share a pool
  or panel.

- **C-3 (X3) — the model/optimizer contract is under-specified for
  reproducibility.** Unfixed and trajectory-determining: attention **direction**
  (causal vs bidirectional — different models); attention Q/K/V/O **biases** and
  the **scale** (`1/√32`); **all-masked-row** handling (under causal attention +
  left-pad, early PAD-query rows attend only to masked PAD keys → `softmax(−∞)` =
  NaN — undefined even if unused, and propagation is implementation-dependent);
  a **final LayerNorm** and every **LayerNorm epsilon**; the **weight-init draw
  order** (which tensor consumes the seed stream first — the core of per-member
  reproducibility); **dtype/device/determinism** (Level 0's "CPU float32, pinned,
  deterministic kernels" is not restated, yet §7's re-execution and the state-hash
  tests depend on it); **gradient clipping** (none? a norm?); **loss reduction**
  (mean vs sum over the minibatch); and the **exact seed-key string format** for
  `"replay/(block,arm,member)"`, `"shortlist/(block,arm-slot,step)"`, and the
  master seed value. "2-layer pre-LN, `d128`" is not enough.

### Major

- **MJ-1 (X2) — "hashes byte-identical across worlds" is contradictory.** Each
  world's escrowed panel content differs by `n`, so its integrity digest and
  ciphertext *must* differ across worlds (or they bind nothing). A byte-identical
  "hash" can only be a **schema** hash (of the world-independent 188-item skeleton),
  which provides no content integrity. Separate three surfaces explicitly:
  learner/acquisition-visible = ∅ (fully sealed); researcher-visible pre-outcome =
  the **per-world** ciphertext + salted digest (§10, necessarily different);
  world-independent schema (counts, ids, ordering, stratum names) = byte-identical.
  Drop "hashes" from the byte-identical surface.

- **MJ-2 (X5) — solve-then-non-finite is doubly classified.** §6 sets `T` = the
  first checkpoint of the earliest *completed* qualifying window; §7.1 routes any
  non-finite trajectory to censored-at-`B`. A run that certifies a persistent
  solve at `T = 800` and then diverges at 1,200 satisfies both. Resolve
  explicitly. Scientifically a *completed* certification before divergence should
  stand (truth was reached); if instead it is forced to censored, that is a
  conservative choice that discards a real solve and must be stated as such —
  either way, not left contradictory.

- **MJ-3 (X5) — global Brier is incoherent with the per-stratum certificate.**
  Verified: with 172 well-calibrated items and S4 at chance-calibration (0.25),
  global Brier = 0.021 ≤ 0.10 — the certificate passes while calibration on the
  decisive stratum is at chance. And excluding abstained items from Brier, plus
  the per-stratum ABSTAIN cap of 2, lets a learner drop its two worst-calibrated
  items in any stratum whose accuracy count still passes (e.g. S5 at 14/16). Move
  calibration to **per-stratum** (at minimum a separate S4 Brier bound) and score
  abstentions in Brier at a fixed penalty (e.g. 0.25) so abstention cannot improve
  calibration.

- **MJ-4 (X4) — the leakage gates are thresholds, not protocols.**
  Shuffled-answer "zero certified solves" omits the number of shuffled runs and
  their seeds (one run under-powers the leak test). The encoding probe "top-1
  ≤ 1/6 over 12 worlds" omits the probe model, the exact pre-contact feature
  bytes, the train/eval split (a probe trained and tested on the same 12 worlds
  memorizes → 12/12), repetitions, the null statistic, and the finite-sample
  decision (≤ 1/6 = ≤ 2 of 12 correct is coarse). Specify both as full protocols;
  they are design-invalidity determinants.

- **MJ-5 (X4) — feasibility does not exercise the dominant cost, and the
  censoring indicator can tune the endpoint.** RANDOM-STATIC does no scoring, so
  the §5 RANDOM-only feasibility check never measures the `B·S·E ≈ 4.1M`-forward
  ACTIVE scorer that dominates runtime (~16× training). The non-comparative check
  must add a **scorer-timing path** (a scorer-only microbenchmark or a single-arm
  ACTIVE *timing* run reporting runtime/memory only). And the single-arm censoring
  indicator may set `B`/architecture **only as a feasibility floor** (large enough
  that some solve occurs) via signed amendment — never tuned toward a target solve
  rate, which would select an endpoint parameter on outcome-like data.

- **MJ-6 (X5) — failure routing can mask outcome-related divergence, and the
  re-execution predicate is self-contradictory.** A missing checkpoint from a
  crash caused by non-finite state is outcome-related (§7.1, censored) but §6/§7.2
  route "missing checkpoint" straight to process-failure re-execution — check
  finiteness first. And "re-execute … reproducing identical prefix hashes" cannot
  hold for a genuine transient fault (the faulting run and the clean re-run diverge
  at the fault); it must mean identical hashes for the committed prefix **up to the
  last pre-fault checkpoint**. State both.

- **MJ-7 (X2) — S2/S5 zone-crossing makes the table's novelty columns
  inaccurate.** At `n = 125`, S2's `d = n + 1 = 126` and S5's `d = n + 2 = 127`
  fall in zone 3 (uncontactable, difference-novel), contradicting the "Diff novel:
  no" entries; S2/S5 difficulty is therefore `n`-dependent. Immaterial for
  anti-lookup (these are negatives a NO-defaulting lookup passes), but the table
  must be accurate and the non-uniformity noted.

### Minor

- **mn-1 (X3)** — pin loss reduction, attention/MLP bias existence, and residual/LN
  ordering explicitly.
- **mn-2 (X1)** — define the canonical byte serialization the "byte-identical"
  claim and the enumeration verifier depend on.
- **mn-3 (X2)** — S1 residue coverage is uneven across `n` (65 residues doubled at
  `n = 66`; 124 once at `n = 125`); acceptable, but note it.
- **mn-4 (X3)** — the 2-replicate master seed schedule is counted, not enumerated;
  commit the master seed value and exact per-stream key strings.

---

## Answers to the required attacks

### X1 — Three-zone enumeration and exact generators

Arithmetic **confirmed**: `A_word = 126`, `d_acq = 125`, `2n ± 1` realizable at
both edges (`251` via `(126, −125)`), `24,003` cells, `≈ 33.6× B` headroom. The
zone structure is correct and should not be reopened. But the **generators are
not specified** (C-2): the SHA-256→sample algorithm, per-class 30 % rounding, cell
index order, realization token construction, and reserved-cell consumption order
all remain implementation choices that change learner input. Approximate
cardinality is fine for headroom; none of the input-determining rules may stay
approximate or "locked draw" placeholders. Every one is a remaining choice that
changes a trajectory.

### X2 — Panel constructibility and metadata sealing

Constructed at both edges. S1's 124 reserved items are **available** even under
repeated residues (`n = 66`: residues 1–59 doubled, ~56 reserved cells per `|d|`
class — ample), *given* the C-2 consumption rule. The **S2 `n = 125` zone crossing
is real and its "difference novelty" column is inaccurate** (MJ-7). S3 distinct
`d = 0` words need the C-2 realization generator. **S4 is defeated (C-1).** S5's
`length ≥ 100` needs `|a| ≥ ~90` cells (padding maxes at `+10`), realizable, and
`d = n + 2` crosses zones at `n ≥ 124` (MJ-7). The phrases "lowest unused reserved
index," "locked draw," "length-matched," "matched," and "locked `d`" are
**unresolved generator choices, not executable rules** until C-2 fixes them. The
"hashes byte-identical across worlds" claim is contradictory (MJ-1); require the
three-surface separation.

### X3 — Model and optimizer bit-level contract

The transformer is not traceable to a unique trajectory (C-3): attention
direction, biases, scale, all-masked rows, final LN + epsilon, init draw order,
dtype/device/determinism, clipping, loss reduction, and seed-key strings are all
unfixed. "2-layer pre-LN transformer" admits materially different implementations.
The 2-replicate seed schedule is counted, not enumerated (mn-4). Committee
disagreement at initialization is honestly characterized as near-random (the MJ-ε
disposition holds) — that is a scope statement, correctly made.

### X4 — Controls and feasibility contract

Both leakage gates are thresholds without protocols (MJ-4). RANDOM-STATIC
feasibility misses the dominant scorer (MJ-5); add a scorer-timing path and bound
the censoring indicator's use to a feasibility floor via signed amendment.

### X5 — Failure and endpoint semantics

The one-re-execution rule is close to audit-safe but has two gaps (MJ-6:
finiteness-before-routing; the "identical prefix hashes" predicate). Solve-then-
non-finite is contradictorily classified (MJ-2). Global Brier is incoherent with
the per-stratum design and abstention-exclusion permits limited selective
calibration (MJ-3). Classification-by-cause-fixed-pre-outcome is otherwise sound
and must be kept.

### X6 — Gate verdict

**Accepted v3 closures — do not reopen:** the three-zone arithmetic; the
design-based population/estimand frame with the census degeneracy owned at
`N3 = 24`; the detector-not-falsifier scope (S-1) and the honest committee
characterization; the determinacy guard (SUP floor-free; EQ/NI/NONSUP require
≥ 1 solve per compared arm); Bonferroni-primary/bootstrap-sensitivity; `N6 = 60`
provenance and predicate directions; the failure cause-class structure
(non-finite → censored, no survivor FPC, no "exclude ≤ 4"); the salted-encryption
escrow; the estimand sign; the opaque flat index with `m = 4`; and `N3`'s
no-clamp precision rule.

**Distinguished:**
- *Genuine blockers needing a v3.1 addendum before signature:* C-1, C-2, C-3,
  MJ-1, MJ-2, MJ-3, MJ-4, MJ-6, MJ-7.
- *Implementation details safely delegable under an exact verifier — after the
  addendum:* the concrete pool/panel/model code, once C-2/C-3 fix the algorithms,
  under the enumeration checker + state-hash tests + the byte-serialization
  (mn-2). Not delegable before, because the rules themselves determine learner
  input and trajectory.
- *Non-comparative feasibility facts observable only after a reviewed driver:* the
  ACTIVE-scorer runtime/memory (MJ-5), single-arm censoring — via the capped
  gate-3 driver, signed amendment, no contrast.
- *Authorial scope already isolated in S-1:* adjacent-only detector scope — a
  Kirill choice, not a blocker.

---

## Exact mandatory edits (v3.1 addendum)

1. **S4 (C-1):** replace `d = 2n ± 1` with symmetric even near-misses
   `d = 2n ± 2` (`a = n ± 1, b = −(n ± 1)`), or otherwise make YES/NO in S4
   matched on parity, magnitude-symmetry, and length so only `d ≡ 0 mod n`
   separates them; re-verify uncontactability and realizability at both edges.
2. **Generators (C-2):** specify the keyed-stream→unbiased-integer/permutation/
   sample algorithm (byte layout, rejection rule, counter), the per-class reserve
   rounding, the cell index order, the realization token construction and
   collision rejection, and the reserved-cell consumption order.
3. **Model (C-3):** fix attention direction, biases, scale, all-masked-row rule,
   final LN + all epsilons, init draw order, dtype/device/determinism, clipping,
   loss reduction, and the exact seed-key strings + master seed.
4. **Sealing (MJ-1):** three-surface separation; remove content "hashes" from the
   byte-identical surface.
5. **Endpoint (MJ-2, MJ-3, MJ-6):** resolve solve-then-non-finite; move
   calibration per-stratum with an abstention penalty; add finiteness-before-
   routing and correct the re-execution prefix predicate.
6. **Controls (MJ-4, MJ-5):** full shuffled-answer and encoding-probe protocols;
   a scorer-timing feasibility path; bound the censoring indicator to a signed
   feasibility floor.
7. **Table accuracy (MJ-7):** correct the S2/S5 novelty columns and note the
   `n`-dependence.

---

## Implementation / gate authorization

- **Codex — authorized now (gate 1, dummy fixtures only):** the parameterized
  `Z/n` world + left-fold + EQ oracle + truth-table enumeration checker; the
  fail-closed process/import interlocks; salt-capable commitments; pair/role/donor
  bookkeeping and the keyed allocation streams — **with `A_word`, `d_acq`, and the
  zone bounds as parameters and the §3 inequalities asserted by the enumeration
  checker.** The keyed-stream algorithm itself (C-2a) must be pinned even for the
  allocation bookkeeping, so specify it in the addendum before that code is
  considered reproducible.
- **Codex — blocked until the v3.1 addendum is reviewed (gate 2):** the three-zone
  pool + verifier, the 188-item panel builder, and the §5 learner + scorer — each
  depends on C-1/C-2/C-3.
- **Feasibility driver (gate 3):** blocked until MJ-5 (scorer-timing path) is in
  the addendum; then optional, single capped execution, signed amendment.
- **Cursor Compose — not yet.** Only after Kirill's S-gate signatures, for
  mechanical breadth under Codex verification.

---

## Negative-space preservation and execution status

Preserved and only strengthened: `PROOF_CORE` / `PROOF_STRONG` and the C6
annotation; C1 as a non-core modifier; the **adjacent-only, distance-1 detector
scope** and `BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1` as a thin, non-falsifying
boundary (S-1); Level 1 never evidence for `PROOF_CORE` in either direction;
`UNKNOWN` / censored / all-censored never equivalence, boundary, or success; a
certificate **failure is censoring, never evidence the learner lacks `n`** (C-1's
fix keeps this honest by making a *pass* mean what it claims); the RANDOM-superior
anomaly never rewrites C1; donor transcripts encode `n_donor`, never `n_target`;
development contrasts non-citable forever.

**No Level 1 execution is authorized by this review.** No comparative scout, lock,
real escrow, or outcome exists or is permitted; the v3.1 addendum returns for a
final signature check before any comparative datum is created.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
