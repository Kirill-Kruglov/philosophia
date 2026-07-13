# Fable 5 — Level 1 spec v3 closure memo

Author: Fable 5. Companion to
`experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md`. v1 and v2 are
preserved unchanged. Inputs: Opus S-gate review (`REVISE_LEVEL1_V2_SPEC`)
and Sol S-gate review (`REVISE_LEVEL1_V2_INFERENCE`); the signed claim
graph and canonical files. Chat captures were provenance only.

## Verdict

**READY_FOR_FINAL_LEVEL1_S_GATE_REVIEW**

Every value that can move a trajectory, solve event, interval predicate,
invalidity route, or estimand is exact in v3 with stated non-comparative
provenance — architecture and optimizer constants, panel counts and count
thresholds, ABSTAIN/confident-lie/calibration rules, leakage tolerances,
window arithmetic, margins and predicate directions, estimator/df/census
rules, determinacy guards, failure routing, and allocation procedures.
Nothing endpoint-determining is deferred as a "signature confirmation."
`N3` alone remains a post-comparative-scout realized number under the
fully frozen §9 rule, which contains no clamp.

## 1. Finding-by-finding disposition

### Opus (S-gate review)

| Finding | Disposition | v3 section |
|---|---|---|
| CR-A (support arithmetic contradictory; anti-lookup misattributed) | **Adopted in full**: `A_word = 126` decoupled from `d_acq = 125`; strengthened inequalities `2·A_word ≥ 2·n_max + 1 = 251` and `n_max ≤ d_acq < 2·n_min − 1`; three-zone universe (acquisition / reserved raw-novel / extrapolation); stratum 4 draws from zone 3; "semantically never-contacted" withdrawn except for zone 3 | §3 |
| CR-B (panel algebraically wrong; corner confound irreducible) | **Adopted**: exact 188-item table; balance across classes/strata; per-residue balance impossibility stated; certificate meaning = period **plus** novel opposite-displacement composition; conservative endpoint (pass strong, failure = censoring, never "no `n`"); marginal-coverage-vs-corner statement | §3, §4 |
| CR-C(i) (endpoint quantities unset) | **Adopted**: every quantity now has an exact value with provenance (accuracy counts, Brier ≤ 0.10, ABSTAIN rule + cap, confident-lie caps, aggregation = mean-probability, loss, leakage tolerances, interval method) | §5, §6, §8 |
| CR-C(ii) (outcome-correlated failures excluded) | **Adopted and strengthened**: non-finite → censored-at-B, block retained; process failures → one verified outcome-independent re-execution or whole-level `PLATFORM_OR_DESIGN_INVALID`; survivor-FPC and "exclude ≤ 4" withdrawn entirely | §7 |
| MJ-α (detector, not falsifier) | **Adopted**: asymmetry stated in §1; null → `BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1`; distance-axis alternative put to Kirill as `I_REQUIRE_LEVEL1_DISTANCE_AXIS` | §1 |
| MJ-β (scope mislabel) | **Adopted**: estimand renamed "online responsiveness under near-matched probe scale"; scale axis noted as controlled out | §1 |
| MJ-γ (population inconsistency; FPC degeneracy) | **Adopted with the design-based frame** (see accepted disagreements): 24-pair outcome frame, known `π_h`, census degeneracy owned explicitly at `N3 = 24` | §2 |
| MJ-δ (architecture unjustified from Level 0) | **Adopted**: new named contract (2-layer pre-LN, left-pad 273, masked PAD, learned positions) justified as declared conservative requirements; Level 0 cited for engineering precedent only; feasibility risk handled by the defined non-comparative feasibility contract | §5 |
| MJ-ε (early-signal oversold) | **Adopted**: committee disagreement described as a locked randomized heuristic, near-random early; C1 null scoped to the policy | §1, §5 |
| MJ-ζ (aggregation/loss/calibration/ABSTAIN unset) | **Adopted**: mean-probability aggregation, softmax CE loss, Brier ≤ 0.10, ABSTAIN `|p̄ − 0.5| < 0.10`, all exact | §5, §6 |
| mn-i (shortlist variance; YOKED inherits donor draw) | **Adopted**: noted in the estimand; seed replicates span it; block-level inference absorbs it | §5, §8 |
| mn-ii (`d = 0` cap ambiguity) | **Adopted**: cap = the same fixed realization count (`m = 4` per cell); no per-class oversampling | §3 |
| mn-iii (panel metadata leak) | **Adopted**: world-independent exposed surface (188 items, fixed ids/ordering), byte-identity test; all target-specific structure sealed | §4, §12 |
| mn-iv (scoring dominates; sizing) | **Adopted**: selection compute reported separately; `B` and the wall sizable only from non-comparative development timing/censoring | §5 |

### Sol (S-gate review)

| Finding | Disposition | v3 section |
|---|---|---|
| C1 (reserved cells cannot supply `2n` probes) | **Adopted** — identical repair to Opus CR-A: separate evaluator-only zone 3 with its own support, construction, and sealing | §3, §4 |
| C2 (`2n + 1 = 251` unrealizable) | **Adopted**: `A_word = 126`, `2·A_word = 252 ≥ 251`; realizability enumerated at both edges | §3, §4 |
| C3 (per-residue YES/NO balance impossible) | **Adopted**: balance across matched classes/strata; S1 is all-NO by algebraic necessity; per-stratum scoring | §4 |
| C4 (window arithmetic ambiguous) | **Adopted**: five checkpoints `t..t+200`, step-0 start legal, last start 1,800, past-B windows censored, missing checkpoint routed as process failure | §6 |
| M1 (population/sampling unspecified) | **Adopted**: `P/D/O/R_h` exact; locked keyed allocation procedures; `π_h = n_h/8`; estimand over all 24 role-assigned blocks conditional on `D`, roles, seeds | §2 |
| M2 (solve floor discards one-sided contrasts) | **Adopted**: predicate-specific determinacy guard — `SUP` floor-free; `EQ`/`NI`/`NONSUP` require ≥ 1 solve per compared arm; all-censored → `INSUFFICIENT` | §8 |
| M3 (interval method not frozen) | **Adopted**: Bonferroni-adjusted paired t primary (α = 0.05 familywise, Satterthwaite df); bootstrap sensitivity-only, cannot change predicates | §8 |
| M4 (N6 not numeric) | **Adopted**: `m = 60` frozen, one margin for all four predicates with the stated scientific reason; exact directions per the mandate | §8 |
| M5 (exclusion breaks design-based estimand) | **Adopted** — as Opus CR-C(ii): cause-class routing, no survivor population | §7 |
| M6 (census must not erase seed uncertainty by accident) | **Adopted**: seeds conditioned on (finite locked schedule); census reading stated pre-outcome and unswitchable | §2, §8 |
| m1 (adjacency fixes, not removes, mismatch) | **Adopted**: stated in §1's scope; distance-1 = mediator pinned at minimum | §1 |
| m2 (step-0 rule) | **Adopted**: `T = 0` legal; leakage gates cover the pathological case | §6 |
| m3 (missing checkpoint terminal classification) | **Adopted**: process-failure route, never a silent non-qualifying observation | §6, §7 |

Nothing in either review is unaddressed or silently dropped.

## 2. Frozen constants and provenance (compact)

| Constant | Value | Non-comparative provenance |
|---|---|---|
| Registry / pairs / strata | `{66..125}`, 30 adjacent pairs, 3×10 | supply arithmetic (v2, verified by Opus X1) |
| `D` / `O` / roles / `R_h` | 6 pairs; 24 pairs (8/stratum); keyed SHA-256 streams; `π_h = n_h/8` | design-based allocation; auditable public keys |
| `A_word` / word length / input | 126 / 136 / 273 | `2·126 = 252 ≥ 251 = 2·n_max + 1` |
| `d_acq` | 125 | `n_max ≤ 125 < 131 = 2·n_min − 1` |
| Reserved fraction / `m` / `d=0` cap | 30 % / 4 / 4 | pool headroom 33.6×B; multiplicity uniformity |
| Panel | 188 items; 124/16/16/16/16; 32 YES/156 NO | algebraic construction; world-independent surface |
| Solve counts | 118/124, 15/16, 15/16, 15/16, 14/16 | binomial tail bounds vs chance/lookup |
| ABSTAIN / confident lie / Brier | `|p̄−0.5|<0.10`, cap 2/stratum; 0 in S4, ≤1 elsewhere; ≤ 0.10 | certification semantics; finite-sample computability |
| Leakage tolerances | shuffled: 0 solves; encoding probe ≤ 1/6 | zero-tolerance certification; 2× chance |
| Cadence / window / starts | C=50; 5 checkpoints spanning 200; start 0 legal; last 1,800 | arithmetic consistency (Sol C4) |
| Learner | 2-layer pre-LN transformer, d128, 4×32, MLP 512, left-pad, masked PAD, learned positions, CE loss, mean-prob aggregation | declared conservative requirements for length-273 regime |
| AdamW | lr 1e-3 const, wd 0.01 (matrices only), betas (0.9,0.98), eps 1e-8, U=1, minibatch newest+31 | standard online-learning conservative defaults |
| `E` / shortlist / tie-break | 4 / 512 / lowest index | committee minimality; resource bound |
| `B` | 2,000 | ≥ 33× naive scan; ≤ 3 % pool |
| Seeds | 2 replicates per block-arm, conditioned | minimal noise averaging in the week budget |
| Estimator | stratified paired FP mean, `W_h = 1/3`, FPC, Satterthwaite df, census collapse at 24 | design-based inference (Sol Y4) |
| Intervals / α | Bonferroni paired t, familywise 0.05 | conservative, exact, pre-frozen |
| N6 | m = 60, all four predicates, directions per mandate | naive registry-scan cost |
| Determinacy guard | SUP floor-free; EQ/NI/NONSUP need ≥ 1 solve/arm | Sol M2 repair |
| N3 rule | smallest of {12,15,18,21,24} with projected half-width ≤ 30; no clamp | precision-only; fork to Kirill on failure |

## 3. Accepted disagreements (explicit)

1. **24-pair outcome frame, not realized-`N3` population** (vs Opus MJ-γ's
   suggestion): a realized-`N3` population makes FPC and frame
   generalization meaningless; the design-based frame keeps `N3 < 24`
   inference honest and owns the census degeneracy at 24 (variance
   exactly zero; descriptive of the 24 blocks under conditioned seeds).
2. **Adjacent-only detector scope, no second donor axis** (vs Opus MJ-α's
   distance-axis option): C1 is a modifier, not a `PROOF_CORE` conjunct;
   distance 1 maximizes positive-detector strength at the stated cost of
   a thin null — put to Kirill as S-1 below, with the redesign
   alternative named.

## 4. Signature packet

- **S-1:** `I_ACCEPT_ADJACENT_ONLY_C1_DETECTOR_SCOPE` — adjacent-only
  donors; detector-not-falsifier asymmetry; null =
  `BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1`.
  *Alternative:* `I_REQUIRE_LEVEL1_DISTANCE_AXIS` (redesign: reopens
  world supply, arms, multiplicity, budget, and review).
- **S-2:** `I_ACCEPT_LEVEL1_V3_SCIENTIFIC_SPEC` — consolidated acceptance
  of every frozen constant, table, predicate, routing rule, and gate in
  v3 (any single-value amendment is a named, signed edit before the
  S-gate, never a silent change).

## 5. Questions for the final reviews

**Opus:** (1) Does the three-zone arithmetic close CR-A at both registry
edges, including the `n = 125` near-miss via `(126, −125)` and the
`n = 66` floor `131 > 125`? (2) Is S4's joint meaning (period + corner
composition) now stated strongly enough that a conservative failure
cannot be over-read — and is 0 confident lies in S4 the right severity?
(3) Does §7's one-re-execution rule close the survivor-bias hole without
reopening a resource-exhaustion denial-of-service on the level? (4) Any
remaining endpoint-determining quantity you judge unset?

**Sol:** (1) Is the determinacy guard (SUP floor-free; EQ/NI/NONSUP need
≥ 1 solve per compared arm) the correct repair of M2, or does SUP need a
minimum-information guard too? (2) Satterthwaite df across three strata
with `n_h ∈ {4..8}` — acceptable as frozen, or do you require a stated
small-sample fallback? (3) Does the census-collapse rule (points vs
margins at `N3 = 24`) preserve predicate coherence with the `N3 < 24`
interval rules? (4) Is one margin `m = 60` for all four predicates
adequately justified, or should `EQ` carry its own tighter margin?

## 6. Codex/Cursor authorization and negative space

**Codex now (gate 1, dummy fixtures):** parameterized substrate — `Z/n`
world/fold/EQ/truth enumeration with `A_word`, `d_acq`, zone bounds as
parameters and the §3 inequalities asserted in the enumeration checker;
fail-closed process/import interlocks; salt-capable commitments;
pair/role/donor bookkeeping and the keyed allocation streams. **Codex
after the final v3 review (gate 2):** three-zone pool + verifier; 188-item
panel builder; §5 learner + scorer with state-hash tests. **Gate 3
(optional):** the feasibility driver may be implemented after gate 2 and
executed **once** under its §5 contract. **Cursor:** only after Kirill's
S-gate signatures, for mechanical breadth under Codex verification.
**Forbidden regardless:** comparative scout, lock, real escrow, outcome.

**Negative space:** Level 1 never evidences `PROOF_CORE` in either
direction; a C1 null is the thin distance-1 boundary only; `UNKNOWN`/
censored/all-censored is never equivalence, boundary, or success; a
certificate failure is censoring, never evidence the learner lacked `n`;
RANDOM-superior is an anomaly, never a C1 rewrite; development contrasts
are non-citable forever; donor transcripts encode `n_donor`, never
`n_target`.

## 7. Confirmation

No code was written; no feasibility or comparative check was run; no
datum, scout, escrow, lock, or outcome was created; no threshold came
from any observed comparison (none exists). `PROOF_CORE`/`PROOF_STRONG`,
C6 as annotation, C1 as non-core modifier, the total selector, and every
signed negative destination are preserved verbatim.
