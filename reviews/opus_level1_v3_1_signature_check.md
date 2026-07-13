# Opus 4.8 X-line — Level 1 v3.1 addendum, bounded signature check

Reviewer: Opus 4.8 (adversarial, bounded to the A1–A10 repairs). Target:
`experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md`, against the v3
spec, my v3 final review, Sol's v3 final review, and Fable's v3.1 closure. Scope:
only whether A1–A10 land the mandated repairs without a new contradiction. No
accepted v3 world/estimand choice is reopened. This review authorizes no entropy
draw, feasibility run, scout, lock, escrow, or outcome, and predicts no arm. The
S4 feature analysis below was computed independently at general even/odd `n` and
the `n = 125` table.

---

## Verdict

**`REVISE_LEVEL1_V3_1_ADDENDUM`**

A5–A9 are genuine bit-level closures and should not be reopened: bidirectional
attention with the all-masked-row pathology removed, the full transformer/optimizer
contract, per-stratum Brier, the divergence-timing and re-execution corrections,
the three metadata surfaces, the noninterference and shuffled protocols, the scorer
microbenchmark, and the exact estimator/determinacy/N3 machinery all land their
v3 findings. **But A1 does not repair the S4 leak — it relocates it.** The
mandated marginals are now balanced, yet the *joint* feature
`XOR(split-type, side-parity)` classifies all sixteen S4 items exactly, with the
offset equal to `parity(n)` — a quantity any contact learner already holds. The
addendum's own feature-null verifier checks only *marginal* mutual information and
therefore passes the broken panel. The certificate's sole tooth is still
defeated by a fixed non-modular rule. Plus two bounded generator gaps (A2/A3) that
let two conforming implementations diverge. Not signature-approvable; not blocked
(a bounded reconstruction path exists, below). **All Level 1 execution remains
forbidden.**

---

## Findings, ordered

### Critical

- **C-1 (O1) — S4 is separated by a joint XOR of two readable features; the
  verifier misses it.** From A1's endpoint table, define per item
  `split = [|a| = |b|]` and `side_parity = |a| mod 2` (both sides share parity by
  construction). Computed over the sixteen items:

  | `n` | marginal split | marginal side-parity | marginal `|a|=|b|` | `XOR(split, side_parity)` per label |
  |---|---|---|---|---|
  | even (100) | balanced 4/4 | balanced 4/4 | balanced 4/4 | **YES→1, NO→0** |
  | odd (99) | balanced 4/4 | balanced 4/4 | balanced 4/4 | **YES→0, NO→1** |
  | 125 (table) | balanced 4/4 | balanced 4/4 | balanced 4/4 | **YES→0, NO→1** |

  So `label = XOR(split, side_parity) XOR parity(n)`. All three inputs are
  available to a **difference-lookup** learner: `split` and `side_parity` are
  byproducts of the `net` skill, and `parity(n)` is known to any learner that
  found `d = n` in contact (which it must, to pass S2). Such a learner classifies
  S4 with a 2-bit XOR — **no period representation and no `d = 2n` extrapolation.**
  The A1 verifier's "each feature has zero mutual information with the label" is a
  *marginal* condition; the XOR of two zero-MI features carries full MI. The
  repair balanced the marginals and left the joint leak (indeed, symmetric items
  force it: a symmetric YES is always `parity(n)`, a symmetric NO always
  `parity(n ± 1)`, so `(sym, parity)` alone leaks). The verifier and the
  construction must both change.

### Major

- **MJ-1 (O2) — the allocation domains are not bit-reproducible.** `("L1","alloc",
  "dev")`, `("L1","alloc","role")`, and `("L1","alloc","sample", N3)` carry **no
  stratum (or pair) component**, and A2 does not state whether the PRF counter runs
  **continuously across the three strata** or resets per stratum. Two conforming
  implementations — one continuing the counter into stratum 2, one restarting —
  produce different development sets, role bits, and samples. Add an explicit
  stratum component to each allocation domain (e.g. `("L1","alloc","dev", h)`), or
  normatively fix a single processing order with a continuous counter. Until then
  the allocation is not reproducible.

- **MJ-2 (O2) — S4 raw words are under-specified.** A1 fixes each S4 item's
  displacements `(a, b)` and its per-side **padding length**, but not **which word**
  of that `(displacement, length)` is used — there are `C(ℓ, #R)` such words, and
  A3's rank/unrank + realize-draw governs zone-1 cells, not the zone-3 S4 items.
  Two implementers pick different S4 words → different learner inputs. Route S4
  realizations through the A3 `("L1","pool","realize", a, b)` draw (with A1's fixed
  paddings) or specify the exact rank.

### Minor

- **mn-1 (O3)** — enumerate `fan_in` per tensor (obvious for most, but make it
  explicit for `head_W` and the MLP matrices); confirm `torch 2.9.1+cpu` is a
  real, pinnable build; the `uint64_be(PRF[0:8]) → manual_seed` range is fine
  (test-enforceable).
- **mn-2 (O2)** — the reserved-cell consumption rule matches on "required `d` and
  any length constraint," but S5's `length ≥ 100` items need cells with
  `|displacement| ≥ 90` (padding caps at `+10`); state that the consumption filter
  ranks on that constraint so the S-gate exhaustion proof is well-defined.

---

## Answers to the required checks

### O1 — S4 joint-feature leakage

**Fails.** The joint `(split-type, side-parity)` XOR classifies S4 at every
registry world including `n = 125` (verified above), while every marginal is
balanced. A fixed non-modular rule therefore classifies S4, so the signature
check fails even though the addendum's balance table is internally correct — the
balance is the wrong (marginal) condition. Realizability and acquisition
uncontactability are intact (`d ∈ {2n−2, 2n, 2n+2} ⊂ [130, 252]`, all `> d_acq`,
`252` via `(126, −126)`); the defect is purely the joint feature-null.

**Smallest bounded repair** (two parts, both required):
1. **Verifier:** replace the marginal-MI check with a **joint** feature-null — the
   label-conditional multiset of the *entire declared nuisance-feature vector*
   (split-type, side-parity, per-side lengths, magnitudes, padding pattern, and
   every pairwise/triple combination) must be **identical** for YES and NO, or an
   equally strong exact proof. Marginal balance is necessary, not sufficient.
2. **Construction:** the joint-null is **unreachable with symmetric items**
   (symmetric `d = 2m` forces `|a| = m`, so `parity` tracks the label). Rebuild S4
   from **offset-only** items, choosing offsets and paddings so that per-side
   parity, per-side length multiset, and every low-order combination are jointly
   label-balanced, leaving only the displacement sum `d = |a| + |b|` to separate
   YES from NO. Note the honest consequence (my v3 CR-B, now unavoidable): `d`
   itself is padding-invariant and readable, so the reconstructed S4 certifies
   "the learner recovered `n` **and** computes `d mod n` on a novel opposite-corner
   composition" — it does **not** separate that from difference-lookup-plus-
   arithmetic. If Kirill will not accept that scoped meaning, S4 cannot be made
   clean inside the cyclic world and the choice escalates to a scope decision (the
   `S-1`-adjacent concession) or a world change — not a silent table edit.

Do not accept a verifier that checks only individual mutual information.

### O2 — Generator and serialization exactness

A2's HMAC component encoding (`uint16_be(len) || UTF-8`, integers as decimal
ASCII), the `U(r)` rejection sampler (`limit = ⌊2²⁵⁶/r⌋·r`, redraw on `x ≥ limit`,
`r = 1 → 0`), descending Fisher–Yates, `floor(3·N_d/10)` reserve rounding, cell
canonical order, word rank/unrank (CNS, `R < L`), four-realization collision
rejection, the model-id/ASCII-byte split, and the three surfaces are all exact.
**Gaps that let implementations differ:** MJ-1 (allocation stratum/continuity) and
MJ-2 (S4 word rank); plus mn-2 (S5 length-constrained consumption). Everything
else is exact.

### O3 — Model trajectory uniqueness

**A5 closes C-3.** Bidirectional mask (all-masked-row pathology removed), scale
`1/√32`, softmax over keys, pre-LN residual order with a final LayerNorm,
`eps = 1e-5`, no QKVO bias / MLP+head bias, `randn × 1/√fan_in` with the canonical
tensor draw order and a fresh per-tensor CPU generator seeded by
`uint64_be(PRF[0:8])` (explicit big-endian — no ambiguity), the two parameter
groups, shared per-step minibatch, CPU/float32/`use_deterministic_algorithms`/
single-thread environment, checkpoint state, and the `{replicate, member, arm}`
identifiers are all specified. Residual: mn-1 only (enumerate `fan_in`; confirm the
torch build). This is a genuine bit-level contract.

### O4 — Endpoint, routing, and controls

Per-stratum Brier over **all** items (abstentions at ≈ 0.25) is jointly satisfiable
with the count/ABSTAIN/confident-lie rules — the worked examples check
(S5: `(14·0.0025 + 2·0.25)/16 ≈ 0.033`; S4: `≈ 0.021`). Solve-before-divergence vs
divergence-before-window is made exclusive by "complete window before first
non-finite state." Pre-fault re-execution ("hashes through the last committed
pre-fault checkpoint") and seal-breach (whole-level invalidity, no re-exec) are
deterministic. The noninterference bundle handles the world-slot concern by
**alpha-renaming world handles to schedule-position slot indices** before requiring
byte-identity — the correct fix. Shuffled controls are fully reproducible (12
worlds × 2 replicates, named FY permutation domain, zero-solve invalidity). The
scorer feasibility records only latency/memory/finiteness and the binary
censoring floor — no scientific series. All land.

### O5 — Signature and implementation boundary

1. **Signature-blocking scientific/trajectory ambiguity:** C-1 (S4 joint XOR — the
   blocker), MJ-1 (allocation domains), MJ-2 (S4 word rank).
2. **One-paragraph v3.1 corrections:** MJ-1 (add stratum components / fix counter
   continuity) and MJ-2 (route S4 words through the realize draw). C-1 is **not**
   one paragraph — it needs the joint-null verifier, an offset-only reconstruction,
   and a scope confirmation.
3. **Enforceable by implementation tests without contract change:** mn-1 (`fan_in`
   enumeration, version pin) and mn-2 (consumption filter wording).

---

## Exact bounded edits

1. **A1 (C-1):** (a) redefine the feature-null verifier as a **joint** label-
   conditional multiset identity over the full nuisance vector and all low-order
   combinations; (b) reconstruct S4 offset-only so the joint-null holds and only
   `d` separates the labels; (c) state the scoped certificate meaning ("recovers
   `n` and checks a novel multiple") and route it to Kirill's scope signature; if
   the joint-null is unreachable, escalate rather than weaken silently.
2. **A2 (MJ-1):** add an explicit stratum component to `alloc/dev`, `alloc/role`,
   `alloc/sample`, or fix a normative continuous-counter order.
3. **A1/A3 (MJ-2):** specify S4 raw-word selection via the realize domain (with
   A1's fixed paddings) or an exact rank.
4. **A3 (mn-2):** state the length-constrained reserved-cell consumption filter.
5. **A5 (mn-1):** enumerate `fan_in`; confirm the pinned torch build.

Nothing in A5–A9's landed content should be reopened.

---

## Gate authorization

- **Gate 1 (neutral parameterized substrate) — still eligible now**, dummy fixtures
  only, exactly as authorized in the v3 review, provided the keyed-PRF algorithm
  (A2) is implemented as written; **but the allocation bookkeeping must wait on
  MJ-1** (its domains are not yet reproducible).
- **Gate 3 (exact generators/model + verifiers) — blocked** until a v3.1.1
  correction lands C-1 (including the joint-null verifier), MJ-1, and MJ-2 and is
  re-reviewed. The A5 learner/scorer and A6–A9 machinery may be implemented once
  that correction is signed, since they are otherwise exact.
- **Gates 4–10 (root-entropy draw, feasibility, scout, lock, escrow, outcome) —
  forbidden.** This review authorizes **no entropy draw** and no execution.

---

## Negative-space preservation

Preserved and unweakened: adjacent-only distance-1 detector scope and its thin
`BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1`; the 24-pair outcome frame with the
census reading at `N3 = 24`; `PROOF_CORE`/`PROOF_STRONG` and C6-as-annotation;
C1 as a non-core modifier; `UNKNOWN`/censored/all-censored never equivalence,
boundary, or success; a certificate **failure is censoring, never evidence the
learner lacks `n`** (the C-1 fix is what keeps a *pass* meaning what it claims);
RANDOM-superior an anomaly, never a C1 rewrite; donor transcripts encode
`n_donor`, never `n_target`; development contrasts non-citable forever.

**No Level 1 execution is authorized.** The v3.1.1 correction returns for a final
bounded check — the S4 joint-null is the one remaining scientific blocker; the two
generator gaps are one-paragraph each.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
