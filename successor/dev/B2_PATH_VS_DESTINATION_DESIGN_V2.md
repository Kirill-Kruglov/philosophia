# B2 — Path-credit vs Destination-credit — DESIGN v2 (NON-CITABLE dev)

Supersedes v1 draft after one bounded design-review pass (Sol validity/stats;
Opus faithfulness/injection). v1's two invalidating flaws are fixed here:
(i) the negatives injected the FALSE wrap answer on the panel's 20 discriminative
items → **path is now positive-only**; (ii) v1 mis-framed displacement as a
"language-wall that dissolves" → it is a **false wall from correlated roads**
(the whole road family shares one blindness). All changes are local; the
experiment is unchanged in intent. Dev, non-citable. Floor/scoring/panel/config
reused verbatim; GPU via the equivalence-proven D0.1b1 runner (frozen
`ContactTransformer.forward` is CPU-only; execution goes through that runner).

## The three-level ladder (replaces v1's two-level framing)

1. **Particular word / arrangement** — dissolves under road change → wall of the
   *language*.
2. **Displacement (#R−#L)** — holds across every road the mind can generate
   (all roads are rearrangements; rearrangement never changes displacement =
   ONE shared blindness across the road family), yet is NOT the world's element
   → a **false wall**, exposed only by a road the mind cannot generate itself
   (an oracle-labeled wrap pair, diff 66 or 132).
3. **fold = displacement mod n** — holds under all roads including the ones only
   contact supplies → wall of the *world*. The input carries no modulus token;
   n is learnable only from oracle-labeled contact.

Governing line (essay): a coincidence counts as a wall only when the roads are
*known to differ*. Here the roads are known to differ in arrangement and known to
be identical in displacement — disclosed, not assumed away.

## Question / estimand (Sol C1)

Holding the number of distinct oracle labels fixed at K, what is the effect of
adding a fixed amount M of manufacturable, oracle-free relational contact (same
"sameness" only) before destination training, on held-out floor generalization?

Δ = E_block[ Q_{P+}(S_K, G_M, Z; H) − Q_D(S_K, Z; H) ], where S_K = the SAME K
labeled pairs in both arms; G_M = fixed path-contact curriculum (P+ only);
Z = init/order/sampling; H = fixed destination horizon; Q = frozen-floor
qualification. This is an oracle-label-efficiency claim, NOT matched-total-data
or matched-compute. Report oracle-stage and total-compute clocks separately;
`first_persistent_step` is measured on the oracle-stage clock.

## The path signal — positive-only, oracle-free (Opus C1, Sol C2)

Only "these roads reach the same place" is asserted; never "these differ."
Sameness is the only claim the mind's own roads license.

- On the PAIR channel (on-distribution; Opus C3b): sample a displacement d; draw
  distinct roads w₁,w₂ at displacement d (`unrank_word` + admissible paddings);
  the positive statement is the pair (w₁,w₂) "same place."
- Loss = alignment of paired road representations + a non-contrastive
  anti-collapse term that is a STATISTICAL constraint on the representation
  (variance + covariance, VICReg-style) — NOT a claim that any two named roads
  differ. No negatives. No InfoNCE.
- Path pipeline may read ONLY token counts and exact-displacement sameness. It
  may NEVER read n, residue/fold, oracle labels, panel membership, or panel
  results. Displacement support fixed independently of n=66. Ephemeral group
  ids/order randomized. (Sol C2)
- Statement of record (replaces "no answer-injection"): *oracle-free relational
  supervision — exact-displacement SAMENESS is supplied; neither the numeric
  displacement nor any modulus/residue information is supplied. Only positives
  are manufacturable.*
- **Length-matched batching (Opus C3a):** fix one target length ℓ per batch so
  length carries zero discriminative signal; same-d alignment must then use R/L
  structure, not the pad boundary.

## Arms

- **D** — destination-only: the SAME K oracle-labeled pairs → equality CE.
- **P0** — path-only (positive-only, 0 oracle): mechanism arm.
- **P0-neg** — the naive exact-d contrastive (same-d pull / different-d push),
  present ONLY to MEASURE the trained-in false wall on wrap items (the instrument
  turned on ourselves; Opus C1 optional arm). Not a path arm.
- **P+** — P0 frozen trunk + a read-out/head trained on the SAME K pairs
  (frozen-trunk primary: "did path build usable structure?"; `P+ft` fine-tune
  only if budget, Opus M4).
- **P_shuf** — fake-ledger control (Opus M2): identical objective & compute to
  P0, groupings randomized so NO true invariance exists, then + K pairs like P+.

**Positive call requires P+ > D AND P+ > P_shuf.**

## Fixed constants (register BEFORE any run; Sol C4/Opus M6)

- K = ⌊N_max/8⌋, N_max = the (already frozen) DIAG_04 curated distinct-labeled-
  pair count; compute once, report the number, do not sweep/select K.
- Lock: pair-sampling algorithm, the six block seeds, label-balance policy,
  K-pair-set hashes, m (roads per d), path horizon/updates, temperature-free
  anti-collapse coefficients, destination horizon H, the P+ transfer mode
  (frozen), ℓ batching schedule, d sampling distribution.
- d=0,p=0 yields the empty word — note it explicitly in the sampler.

## Metrics

- Primary: held-out panel `first_persistent_step` (censored if never qualified)
  + per-stratum, per arm, on the oracle-stage clock.
- Mechanism probes (read-only, frozen activations, no backprop, no
  model/checkpoint selection from probe results), run identically on
  init / D / P0 / P+ :
  - **displacement decodability** — call it "exact-displacement class
    decodability"; balance d classes; report macro acc vs exact chance; PLUS a
    **length-only control probe** and the displacement probe **within length
    strata**; PLUS a **sign(d) probe at matched |d|** (no length feature solves
    it) as the decisive readout (Opus C3a, Sol M1).
  - **residue decodability** — train/test on DISJOINT exact-d values and
    different wrap cycles, every residue in both; report the **P+-over-P0
    increase**; describe only as "linearly decodable residue structure," never
    "the model learned the modulus" (Sol M2).
- P0 panel row: do NOT score P0 through the random head (uninterpretable; Opus
  C3c). Instead evaluate a **read-only linear equality readout on the frozen P0
  trunk**, pre-registered per M3.
- Report **displacement-class overlap** between the path road-pool and the panel
  cells, beside the word-level ∩=0, with one sentence that word-level
  disjointness does not establish content independence (Opus M5).

## Pre-registered panel prediction (Opus M3) — falsifiable

For the positive-only path (read-only equality readout on frozen P0), because
panel equals sit at displacement-difference {0,66,132}:

| stratum | equals | positive-path predicts | prediction |
|---|---|---|---|
| S1 | 0 (diff 1–65) | correct on all 124 | qualifies (uninformative; always-≠ also passes) |
| S2 | 8 @ diff 66 | anti-correct on 8 | FAILS (≤8/16) |
| S3 | 8 @ diff 0 | correct on all 16 | QUALIFIES — the discriminating prediction |
| S4 | 8 @ diff 132 | anti-correct on 8 | FAILS (lies>0, lie_cap=0) |
| S5 | 4@0 + 4@66 | anti-correct on 4 | FAILS (≤12/16 < 14) |

Any deviation (S3 not qualifying, or S2/S4 qualifying) FALSIFIES the
displacement mapping. Payoff signature for P+: P+ retains S3 and BEGINS clearing
the wrap strata (S2/S4/S5) that pure path cannot, using the scarce K on a good
representation — while D clears essentially only S1.

## Kill / decision (dev-status; Opus M1, Sol C3)

- **Q1 (mechanism):** P0 sign(d)/displacement probe at chance within length strata
  → no measurable derived structure under THIS objective/world/probe; motivates a
  different objective family or a confirmatory instrument — NOT a thesis verdict.
- **Q2 (payoff):** over six paired blocks, if not all six strictly favor P+ over
  both D and P_shuf → inconclusive at this replication; do NOT read a noisy null
  as "manufactured experience does not help." A real negative needs a
  pre-registered effect margin with an upper confidence bound below it.
- All outcomes are **dev-candidate evidence bearing on Slot 4c/4b**; they do NOT
  fill or discharge the registered essay-slot kills, which require a signed
  confirmatory run. "Publish the negative" = a dev note, named as dev-status.
- Register the surprising branches (Opus M6): if P0 clears the floor → the panel
  is passable without the wrap and the FLOOR needs re-examination; if D clears at
  scarce K → DIAG_04's memorization read was budget-specific.

## Execution: staged (pilot validates the fixes, then the registered call)

- **Stage 1 — pilot (2 seeds, all arms), design-validation only, NOT the call.**
  Purpose: confirm the corrected pipeline reproduces the M3 prediction (S1,S3
  qualify; S2,S4,S5 fail for positive-path), that P0-neg exhibits the false wall
  on the 20 wrap items, and that the length controls hold (sign(d) probe carries
  the mechanism, length-only probe does not). If the pilot deviates from M3, a
  design bug remains → fix before spending the call. (This is why no second full
  review round is needed: the pilot is the empirical check.)
- **Stage 2 — the call: six paired blocks** (D/P+/P_shuf share K-set, init,
  order per block). Decision per the pre-registered rule above. Hardware for
  Stage 2 (stay on 4060 staged vs escalate to the RTX 5090 / cloud) is decided
  AFTER the pilot shows a signal worth the call.

## What this does NOT claim

Dev, non-citable, one world/modulus/architecture. No confirmatory datum, no C1,
no programme claim, no filling of a registered essay slot. Does not touch frozen
Level-0/1 records or the successor confirmatory line.
