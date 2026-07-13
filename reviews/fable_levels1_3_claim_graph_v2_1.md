# Fable 5 — Levels 1–3 claim graph, revision 2.1 (bounded correction)

Author: Fable 5. This is a narrow correction pass on
`fable_levels1_3_claim_graph_v2.md`; v1 and v2 are preserved unchanged as
review artifacts. Only the six mandated defects (plus the S1 wording) are
corrected; every section of v2 not replaced below carries over verbatim —
in particular the two proof layers (§1), the frozen contrast hierarchy and
budget statement (§2 table and closing paragraphs), the Level 1 common-
budget/blind-evaluator/full-B-donor construction and acquisition-rule
closure (§3), the world status (§4), the review disposition table (§6),
and the branching order (§5 last paragraphs). No accepted science is
redesigned; no code, numeric threshold, lock, scout, escrow, or outcome
prediction is created here.

## Verdict

**READY_FOR_LEVEL1_SPEC**

Secondary status: closed for signature — the eight corrections of v2 plus
the six below leave no known ambiguity that an outcome could exploit;
Level 1 specification work may begin, gated on the §8 signatures and the
§7 gate ledger. (v2's `CLOSED_FOR_SIGNATURE` was a status usurping the
verdict slot; the required token is emitted here and the status is
demoted to this sentence.)

---

## Correction 2 — executable, exclusive C4 cascade (replaces v2 §2 cascade)

**Benefit orientation, defined once and used everywhere.** For every arm
X, the primary benefit β(X) is oriented so that **larger β = better
performance = lower budget-to-certified-solve** (RMST-based at horizon B;
bounded-cost variant inherits the same orientation). Every `>`, `≈`, and
margin over arms A–E and over the Level 1 arms uses this one scale.

**Locked comparison predicates** (each resolved by the N6 interval/test
rule frozen at the S-gate — see Correction 4; a predicate is *resolved*
when its rule yields a determinate answer, else *unresolved*):

- `SUP(X, Y)` — superiority: β(X) exceeds β(Y) by the locked rule.
- `EQ(X, Y)` — equivalence: the locked two-sided interval for
  β(X) − β(Y) lies within the locked margin.
- `NONSUP(X, Y)` — **non-superiority upper bound**: the upper bound of
  the locked interval for β(X) − β(Y) is below the locked non-superiority
  margin — X's benefit does not meaningfully exceed Y's. (Replaces v2's
  directionally incorrect "E not greater than B, margin-locked
  non-inferiority.")

Composite predicates (all on same-presentation escrow unless stated):

- `P_C2` = SUP(C, A).
- `P_C3` = SUP(C, A) on the destination presentation, both presentation
  anchors green.
- `P_W` (weights sufficiency) = EQ(B, C) ∧ SUP(B, A).
- `P_L` (inherited-ledger sufficiency) = EQ(D, C) ∧ SUP(D, A).
- `P_PLACEBO` = EQ(E, C) ∧ EQ(B, A) ∧ EQ(D, A) — ledger *form* reproduces
  the effect with no content-bearing channel.
- `P_C4` (traceability earned) = SUP(C, B) ∧ SUP(C, E) ∧ NONSUP(E, B).

**Priority cascade — evaluated strictly top-down; the first matching row
fires and evaluation stops; any row whose required predicates are
unresolved, and any simultaneous interval pattern not matching a row
(equivalence is not transitive — overlapping `EQ` sets, cyclic or
incoherent intervals), routes to `INSUFFICIENT` and is never resolved by
narration:**

| Priority | Condition | Verdict |
|---|---|---|
| 0 | any locked invalidity | `PLATFORM_OR_DESIGN_INVALID` |
| 1 | ¬P_C2 (resolved false) | `FALSIFIED_AT_C2` |
| 2 | ¬P_C3 (resolved false) | `BOUNDARY_REPRESENTATION` |
| 3a | P_W ∧ P_L | `BOUNDARY_REDUNDANT_MEMORY` |
| 3b | P_W ∧ ¬P_L | `BOUNDARY_WEIGHTS_ONLY` |
| 3c | ¬P_W ∧ P_L | `BOUNDARY_INHERITED_LEDGER` |
| 3d | P_PLACEBO | `FALSIFIED_AT_C4` |
| 3e | P_C4 | C4 earned → proof layers of v2 §1 |
| 3f | anything else | `INSUFFICIENT` |

The joint predicate (3a) is evaluated **before** either component (3b,
3c), so the joint branch is reachable — v2's listing order made it dead
under literal sequential evaluation. The sufficiency branches (3a–3c)
are evaluated **before** the placebo branch (3d), so evidence for a
content-bearing weights or ledger channel is never erased by a
ledger-form placebo overlap: if EQ(B, C) and EQ(E, C) both hold under
their locked intervals, row 3b fires and the placebo row is never
reached (P_PLACEBO additionally requires EQ(B, A) ∧ EQ(D, A) as
belt-and-suspenders, so the two rows cannot truthfully co-hold; the
priority resolves any interval overlap deterministically anyway).

## Correction 3 — total contact-mode selection rule (replaces v2 §3 map)

**Selection procedure over all three Level 1 arms** {ACTIVE,
YOKED-GEOMETRY, RANDOM-STATIC} on the locked primary benefit scale β,
committed before the Level 1 outcome:

1. Any invalid run or unresolved *required* comparison → **Level 2
   blocked**. No default mode exists.
2. If one arm is uniquely superior (SUP against **both** others) →
   select it.
3. If a set S of arms is mutually equivalent at the locked margin
   (EQ within S) and every member of S is superior or non-inferior (per
   the locked rule) to every arm outside S → select the **least adaptive
   member of S** under the preregistered priority
   `RANDOM-STATIC` ≻ `YOKED-GEOMETRY` ≻ `ACTIVE`.
4. Non-transitive, cyclic, or otherwise unclassifiable simultaneous
   intervals → `INSUFFICIENT`, **Level 2 blocked**.

This is total over every statistically classifiable three-arm result,
including the configurations v2 omitted (`RANDOM > ACTIVE > YOKED` falls
under rule 2; `RANDOM ≈ ACTIVE > YOKED` under rule 3 selecting
RANDOM-STATIC; and so on). **Anomaly reporting:** any outcome in which
RANDOM-STATIC is selected over, or uniquely superior to, ACTIVE is
recorded as a registered anomaly (active geometry unhelpful or harmful
in this family) in the decision artifact; the report never alters the
selection.

**C1 is read separately and is not rewritten by selection.** The C1
verdict comes only from the locked paired ACTIVE-vs-YOKED contrast
(Δ_choice = E[RMST_YOKED(B) − RMST_ACTIVE(B)], positive = ACTIVE better),
with RANDOM-STATIC informing the geometry reading exactly as in v2 §3.
Contact-mode selection is a downstream operational decision consuming
all three arms; it has no authority over the C1 estimand, its margins,
or its verdict, and the two may disagree (e.g., C1 positive while rule 3
still selects a simpler mode is impossible under rule 2, but C1
`INSUFFICIENT` with a classifiable three-arm ordering still blocks
Level 2 via rule 1 — the *required* comparisons include those C1 needs).

## Correction 4 — margins freeze before any comparative data (amends v2 §5, §7, S2/S5)

Equivalence and non-superiority margins are statements of the minimum
scientifically meaningful effect. They are **not** sampling-variance
outputs and may never be informed by observed arm differences.

Per level:

- **S-gate (before any comparative scout):** endpoint, benefit
  orientation, comparison family, **all N6 margins**, and the
  interval/test rules freeze. N6 is justified only from the scientific
  claim, external anchors, or a declared conservative bound.
- The comparative development scout may estimate **variance, censoring,
  feasibility, and the block-count precision rule only**. It cannot
  touch margins, endpoints, rules, or policies (any such change voids
  the scout and reopens the S-gate — unchanged from v2).
- **N3** (Level 1 block count) follows the Level 1 scout.
- **N4** (Level 2 block count) follows a **distinct Level 2 development
  calibration**, run only after the five-arm endpoint, contrast family,
  and **N6-L2** margins are frozen at the Level 2 S-gate. The Level 1
  scout cannot estimate N4 (different arms, different contrasts,
  different variance structure).

v2's gate-ledger line "N3 + N6-L1 from scout precision logic" is
**withdrawn**. Corrected gate ledger rows:

| Gate | Must be closed |
|---|---|
| **S-gate L1** (before any comparative scout) | acquisition rule (v2 §3 list); endpoint + orientation + censoring; comparison family; **N6-L1 margins + interval/test rules**; analysis plan; roadmap/README/kill-matrix amendment |
| Before **L1 lock** | **N3** from scout precision logic (variance/censoring/feasibility only); donor-assignment scheme + inference plan (Correction 5); arm-independent balanced panel; invalidity gates; first-hand criterion; total contact-mode rule (Correction 3) |
| **S-gate L2** (before L2 development calibration) | five-arm endpoint + contrast hierarchy; **N6-L2 margins + rules**; false-ledger indistinguishability protocol; compute/replay neutralization |
| Before **L2 lock** | contact mode from L1; **N4** from the L2 calibration; Cayley contract closed per v2 §4(c) or C3 descoped by signature; per-rung grammar tables |

Signature lines S2 and S5 are re-worded accordingly in §8 below.

## Correction 5 — operational donor variance unit (amends v2 §3 inference)

With disjoint one-to-one donors, the **inferential block** is: one
evaluated target world **plus** its uniquely assigned donor
transcript/world. Blocks are disjoint across the primary analysis — no
donor serves two targets, no target consumes two donors, and no world
appears in two blocks.

**Role of assignment randomization, stated honestly:** the one-to-one
assignment is randomized once at lock, within strata, for **design
balance**. It is *not* a randomization-inference engine for the primary
endpoint: re-randomizing the assignment would require training new YOKED
learners on transcripts that were never run, and no test may claim to
observe unrun counterfactual YOKED training trajectories. v2's
"randomization inference over the locked assignment ensemble as primary"
is **withdrawn**. Primary inference is **ordinary block-level inference
under the declared independent-block sampling model** (blocks sampled
i.i.d. from the locked stratum distribution), with the scope stated as
**assignment-conditioned** when, as planned, exactly one assignment is
realized. Assignment-permutation computations that require no new
training (e.g., balance diagnostics on pre-treatment stratum variables)
may be reported as **sensitivity/balance checks only**. Seeds remain
repeated measures inside blocks; nothing about units elsewhere in v2
changes.

## Correction 6 — honest escrow roles (replaces v2 §5 escrow custody and S6)

Gemini, Grok, or a local llama.cpp process can serve as a clean-room
**generator/witness**. None of them can hold a key: they retain no
persistent secret and cannot be a second cryptographic custodian.
Corrected protocol:

- The named clean-room generator receives the locked generator contract
  and a **precommitted public key**; generates the holdout **once**;
  returns only ciphertext + plaintext hash + a generation attestation;
  and never exposes plaintext in any research channel.
- **Kirill holds the decryption key** under an explicitly **procedural**
  escrow threat model: the protections are the pre-outcome hash
  commitment, the single-generation rule, the attestation, and the
  signed-amendment discipline — not cryptographic independence from
  Kirill, and no such independence is claimed. Alternatively, a real
  named human or service may be separately designated as key holder.
- A malformed single generation still ends the holdout. Generator spec
  and seed commitment remain bound inside the level lock; ciphertext and
  plaintext hash are committed before any outcome (unchanged from v2).

## S1 wording correction (amends v2 §8, line S1)

The essay's §VII Proof paragraph *literally* makes C6-null survival a
condition of Proof. Moving it out of the conjunct is scientifically
justified by R5, but it is an **explicit authorial amendment to the
essay's published Proof definition**, not an annotation clarification,
and the signature must say so.

## §8 — corrected signature lines (S1, S2, S5, S6 replace v2's; S3, S4, S7 unchanged except S7's referent)

1. **S1 — Two-layer proof and essay amendment.**
   `I_ACCEPT_TWO_LAYER_PROOF_AND_AMEND_ESSAY_C6` — `PROOF_CORE` =
   C2∧C3∧C4; `PROOF_STRONG` = core ∧ C1 ∧ C5; the essay's unqualified
   "Proof" = `PROOF_STRONG`; **and the essay's §VII Proof paragraph is
   amended by this signature** to move C6-null survival from a Proof
   condition to a mandatory annotation (justified by R5).
   *Alternative:* `I_AMEND_ESSAY_PROOF_TO_CORE` (weakens the essay; not
   recommended), or `I_KEEP_C6_AS_CONJUNCT` (rejects R5; contradicts the
   accepted direction and must be named as such).
2. **S2 — Repaired verdict cascade.**
   `I_ACCEPT_REPAIRED_C4_CASCADE` — Correction 2's predicate definitions,
   benefit orientation, and priority table, **with all N6 margins and
   interval/test rules frozen at the S-gate before any comparative
   data** (Correction 4).
3. **S3 — Level 1 endpoint.** Unchanged from v2:
   `I_ACCEPT_L1_ENDPOINT_CENSORED_BTCS` / alt `I_SELECT_ACCURACY_AT_B`.
4. **S4 — Donor construction.** Unchanged from v2
   (`I_ACCEPT_INDEPENDENT_DONOR_YOKE` / alt derangement-conditioned),
   now carrying Correction 5's block definition and inference scope.
5. **S5 — Scout route.**
   `I_ACCEPT_DEV_CONTRAST_SCOUT` — frozen-first (including N6),
   non-citable, variance/censoring/feasibility/precision only; **N3 from
   the L1 scout; N4 only from the distinct L2 calibration after the L2
   S-gate**. *Alternative:* `I_SELECT_FEASIBILITY_ONLY_SCOUT`.
6. **S6 — Escrow generator and custody model.**
   `I_NAME_ESCROW_GENERATOR_<GEMINI|GROK|LOCAL_LLAMA>_AND_ACCEPT_PROCEDURAL_CUSTODY`
   — names the clean-room generator/witness under Correction 6's
   protocol, with Kirill as key holder under the procedural threat
   model; *optionally* `..._WITH_KEYHOLDER_<NAMED_HUMAN_OR_SERVICE>`
   designates a real second key holder. (No AI key custody; no claimed
   cryptographic independence.)
7. **S7 — Total contact-mode rule.**
   `I_ACCEPT_TOTAL_CONTACT_MODE_RULE` — Correction 3's four-step
   selection procedure, least-adaptive priority, anomaly reporting, and
   the separation of C1 reading from mode selection.
   *Alternative:* a named replacement procedure, committed before the L1
   outcome.

## Updated unresolved numerics

N1 sampler range; N2 word-length cap; **N3** L1 block count (post-L1-scout
precision rule); **N4** L2 block count (post-L2-calibration, never from
the L1 scout); N5 resampled-path divergence threshold (pre-2.5); **N6-L1
and N6-L2** equivalence/non-superiority margins + interval/test rules —
**frozen at each level's S-gate before any comparative data, justified
never from observed arm differences**; S-gate freeze items (persistence
cadence, calibration bounds, panel sizes) unchanged from v2.

---

*Six defects, one pass: the missing verdict token, a dead branch and a
mislabeled margin in the cascade, an incomplete contact map, margins
placed after the data that could bend them, an inference claim over
counterfactuals no one will run, and a key that an AI cannot actually
hold. All were mine, all are now closed the same way as before — while
they are still words, not numbers. v1 and v2 stand as the record of how
they got here.*
