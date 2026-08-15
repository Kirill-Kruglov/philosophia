# PHASE2_MINIMUM_SLICE_AUDIT_V1

**Auditor role:** independent engineering-scope, read-only.  
**Authority pins used:** L2 V5 closure (`L2_ACCEPTED_READY_FOR_L3_IDENTITY_PROJECTION_ANNEX`); driver decision `PHASE2_POST_REVIEW_DRIVER_DECISION_19`; charter v1.1.1; L3 annex v1 draft + driver pre-review (not X/Y-accepted).  
**Inspection tree:** `/tmp/minimo_phase2_stageb_l2_final` (quoted only where behavior is pinned; patches remain evidence of record).

---

## 1. Current executable boundary

**Exists and gate-accepted (instrument / carrier up to L2):**

| Layer | What runs | Limit |
|---|---|---|
| Stage A | Spec/manifest learner, no-truncation codec, canonical action sort, MCTS counters, isolated whole-item search | No training, no selector, no SELF/YOKED |
| L0–L1 | Schema, canonical JSON, Peano-surface render, ND checker | No identity, no compile |
| L2 | `generate_draw` → checked ND plans on A/B/C scaffolds | No public projection, no Peano compile, no roots |

Concrete surfaces:

- Generator entry: `generate_draw` at `phase2_stageb_generator.py:723–741`.
- Checker rederives theorem and renders sequent: `phase2_stageb_checker.py:450–538`.
- Public surface render only (no alpha): `phase2_stageb_render.py:9–48`.
- Action order canon: unique ASCII + sort before children: `phase2_actions.py:157–193`, `334–348`.
- Scientific search root / isolation: `phase2_root.py:40–105`, `phase2_isolated.py:509–528`.
- Hindsight repair exists (`phase2_hindsight.py:5–10`; bootstrap still uses `h.statement` at `bootstrap.py:183–233`) but Phase-1 checkpoints are explicitly disqualified for selector work (driver §3.6).

**Does not exist as accepted code:** L3 identity/projection; L4 compile/replay; equal-prior selector; branch-isolated reciprocal harness; sealed scientific reservoir (fixture plans are permanently ineligible for science).

**Paper boundary:** L3 annex v1 is *not* review-ready (driver D1–D5). Meeting acceptance of AC-1 `(a)` is not yet an accepted annex. Charter §10 eight-root `DEV_CORE_FEASIBLE_FOR_AUDIT_CONTRACT` is **feasibility infrastructure**, not a prerequisite for one scientific contrast if a narrower contract says so — and no such min-slice contract exists.

---

## 2. Minimum end-to-end path

Shortest *causal* path to one reciprocal SELF/YOKED unit (driver §2):

```text
verified ND plan (L1✓, not a scientific-excluded fixture)
  → alpha-canonical theorem + public projection (erasure)
  → Peano action sequence via semantic compile + fresh replay
  → sealed public reservoir R (tasks = public sequents only)
  → twin learners A,B from sealed fresh inits
  → freeze state; score R with registered selector on elaborate(g)
  → stratum-normalized item-addressed Gumbel → batches
  → 2×2: A←A, A←B, B←B, B←A  (equal assigned budgets)
  → one aggregate update per branch
  → held-out work endpoint X (capped entered MCTS iterations primary)
  → D_j = mean_g[(X_A←B − X_A←A + X_B←A − X_B←B)/2]
```

What this path **does not** require: eight domain-separated roots, 4×4 band quotas, full mutual multi-scope skeleton disjointness machinery, G4ip/inverse/statement-model audit suite, catalogue extensibility, or L3/L4 “universality completeness.”

What it **does** require that L2 alone cannot supply: public identity/erasure, executable Peano traces for reservoir membership (solvability witness), selector, twin harness, held-out panel disjoint from reservoir and from all exclusions.

---

## 3. Component disposition table

| Component | Class | Note |
|---|---|---|
| Stage A learner/codec/actions/search/isolation | EXISTS_AND_REUSABLE | Closed 126/126; deferred full training-branch byte replay remains a harness risk (§5) |
| L0 schema/canonical/render/theory + L1 checker | EXISTS_AND_REUSABLE | Carrier verification |
| L2 A/B/C generator | EXISTS_AND_REUSABLE | Use to *mint* scientific items; six gate fixtures stay excluded |
| Premise enumerability table | EXISTS_AND_REUSABLE | L0 regression only; not a compiler (`test_phase2_stageb_theory_enumerability.py`) |
| Codec selector string formats | EXISTS_AND_REUSABLE / incomplete | `format_selector_query` / `format_provable_goal` at `phase2_codec.py:133–163`; **not** the registered log-odds selector |
| Legacy MINIMO mean-logprob / bootstrap conjecturer | REMOVE_FROM_SLICE | Driver §3.7 forbids; `bootstrap.py` is not the scientific route |
| L3 alpha-canonical theorem identity | MUST_BUILD | Needed so SELF/YOKED share one public name/bytes |
| L3 `public_projection` + sealed-field proof | MUST_BUILD | Causal: no plan/band/root leakage into learner view |
| L3 D1 canonical-minimum precondition | MUST_BUILD | Pre-review Major; without it public bytes can drift |
| L3 exact plan identity (full MINSET) | CAN_SIMPLIFY | For one sealed reservoir, checked-plan SHA-256 provenance suffices |
| L3 rule-skeleton identity + stage-6 collision seed / V4 ledger completeness | DEFER | Serves multi-root quota hygiene & universality, not one block |
| Charter §10 8-root × 4-band quota fill | REMOVE_FROM_SLICE | Dev-core terminal, not scientific estimand |
| L4 semantic compile + fresh empty-goal replay | MUST_BUILD (min) | Reservoir membership / positive-control solvability; annex nonexistent |
| L4 ambient-arrow family completeness / COMPILER_FAMILY_UNREACHABLE suite | DEFER | Universality |
| Stage-B audit extras (G4ip, inverse, statement models, alt-proof) | REMOVE_FROM_SLICE | Post-`DEV_CORE` by charter §11.8 |
| Equal-prior label posterior selector + stratum Gumbel | MUST_BUILD | Driver §3.7–3.8 |
| Fresh-from-scratch learner (Stage C) | MUST_BUILD | Phase-1 ckpts invalid for repaired selector |
| Reciprocal 2×2 harness + attrition/worst-case missing D_j | MUST_BUILD | Driver §2–3 |
| Injected-coupling positive-control fixture | MUST_BUILD | Driver §3.11; **before** freezing margins/N |
| Statement-only difficulty regressor / surface-feature incremental tests | MUST_BUILD (qual) | Closes surface masquerade; not a fifth arm |
| NOISE-YOKE / COLD-SELF / SURFACE-YOKE arms | REMOVE_FROM_SLICE | Explicitly not adopted |
| Governance/plugin/registry harness | REMOVE_FROM_SLICE | Already forbidden |

**L3/L4 split for one block:** necessary = theorem canon + projection + compile/replay on a *small sealed set*. Optional/universality = skeleton collision economy, eight-root ledger, band reachability proofs, full cause taxonomy exercised on thousands of draws.

---

## 4. Causal integrity risks

1. **Non-equivalent SELF/YOKED information**  
   - Public item carries sealed metadata (plan size, scaffold, skeleton, draw) → projection failure.  
   - Different elaboration/codec paths or truncation → Stage A forbids truncation, but any second serializer breaks pairing (`phase2_stageb_canonical.py:11–20` is the only Stage-B serializer).  
   - Branch order / shared RNG / non-isolated counter keys → driver requires isolated counter-keyed randomness.

2. **Recipient competence as selector value**  
   - Additive competence cancels in D_j *algebraically* only if all four branches are valid and identically protocolled. Attrition without worst-case bounds reintroduces bias (driver §3.10).

3. **Surface formula features as “state-dependent” selection**  
   - Selector that is mostly length/connective/n-gram will yoke on statement difficulty, not own-state. Qualification must demand incremental predictive value beyond statement-only regressor (driver §3.8–3.9, §4 SURFACE-YOKE).

4. **Replay / compilation nondeterminism breaks exact pairing**  
   - Raw Peano action order varies (Phase-1 terminal; mitigated by sort in `phase2_actions.py:157–193`) but compile-by-list-position would reintroduce it — L4 must match by semantic identity (charter §9).  
   - Stage A still defers byte-identical full training-branch optimizer replay (`PHASE2_STAGE_A_DRIVER_CLOSURE_19.md` deferred gates) — if that metamorphic fails, the design is invalid (driver §4 NOISE-YOKE), not patchable by an arm.

5. **Training success with invalid contrast**  
   - Using excluded fixtures in science.  
   - Reporting solve-rate or leaf expansions as primary after outcomes (driver §3.5).  
   - Qualifying selector on Phase-1 checkpoints or non-disjoint data.  
   - Running reciprocal before injected-coupling recovers known positive interaction.  
   - Treating `DEV_CORE_FEASIBLE` or generator yield as evidence of D_j.

---

## 5. E1 versus E2 cost/risk comparison

**E1 — minimum slice on current MINIMO/Stage-B**  
Reuse Stage A + L0–L2; build thin L3 projection, thin L4 compile, Stage C selector, reciprocal cell; **explicitly refuse** eight-root universality.

| Work | Effort |
|---|---|
| L3 v1.1 (D1–D5) + projection-only code gate | SMALL |
| L4 annex + semantic compile/replay on excluded fixtures | MEDIUM (cliff risk: Peano action semantics) |
| Seal small scientific reservoir + held-out + strata | SMALL–MEDIUM |
| Selector + disposable qualification | MEDIUM |
| Reciprocal harness + injected positive control | MEDIUM |
| Reviews / disposable calibration | SMALL–MEDIUM |
| **E1 total if L4 closes cleanly and universality stays deferred** | **MEDIUM** |
| **E1 if charter §10/L3 skeleton economy re-enters or L4 stalls** | **LARGE** |

**E2 — purpose-built compositional proof-DAG cell**  
Fixed small DAG world: verified compositional proofs, deterministic actions, public erasure, same D_j estimand; no Peano enumeration, no ND→Peano compiler, no eight-root generator politics.

| Work | Effort |
|---|---|
| Cell + checker + public items | SMALL–MEDIUM |
| Learner interface (reuse Stage A codec/search ideas or simplify) | MEDIUM |
| Selector + reciprocal + positive control | MEDIUM |
| **E2 total** | **MEDIUM** |
| Risk | Loses MINIMO “fractal self-extension” story; gains causal clarity and IDEA_GATE cheapness |

Sunk L2 cost must not prefer E1. Prefer E1 only if L4 compile is treated as a **timed kill**, not an open research programme.

---

## 6. Recommended envelope

Do **not** implement further Stage-B universality (L3 skeleton/V4 stage-6, L4 full family, eight roots) under the present charter as if it were the path to D_j.

Recommended: **stop implementation until a one-page min-slice scientific contract** freezes:

- reservoir size, strata, held-out rule, exclusion import;
- which L3 duties are in/out (projection in; skeleton economy out);
- L4 success criterion on excluded fixtures only;
- positive-control threshold before any reciprocal run;
- hard refusal of §10 quota as a science prerequisite.

If that contract is signed and L4 is timed: **E1 MEDIUM**. If L4 exceeds the hard stop below: **E2**. If author scope remains essay Level-1 / Slot 4c vs Phase-2 undecided: do not spend L4 at all.

---

## 7. Hard stop before implementation

**Hard stop (any one fires → no silent scope growth):**

1. No accepted min-slice scientific contract that **defers** charter §10 eight-root feasibility and L3 skeleton-quota universality.  
2. L3 annex not repaired (D1–D5) and X/Y-accepted for the *projection subset* actually required.  
3. After L4 annex acceptance, semantic compile+replay on the frozen excluded valid plans is not closed in **≤ 3 focused implementation days** → abandon E1 L4 path; choose E2 or stop.  
4. Injected-coupling positive control fails to recover known positive interaction → do not freeze or run reciprocal science.  
5. Selector qualification fails sign / surface-incremental / identical-state equality tests → close this selector route (driver §3.8); do not substitute post hoc.  
6. Exact same-state + same-batch replay fails byte-identity on weights/opt/examples → design invalid; return to statistical review (driver §4).

Exceeding (3) or refusing (1) while continuing L3→L4→quota is the failure mode IDEA_GATE names: harness larger than the probe.

---

## 8. Questions that require an author decision

1. **Scope:** Is Phase-2 still authorized as the next scientific probe, or does essay Level-1 / Wall-B (status meeting options a/b/c) reclaim WIP before any L4?  
2. **Min-slice waiver:** Will you sign a contract that **removes** charter §10 eight-root `DEV_CORE_FEASIBLE` from the critical path to one D_j estimate?  
3. **L3 breadth:** After AC-1 `(a)`, do you authorize a **projection-only** L3 code gate for the scientific slice, deferring skeleton/stage-6, or must full annex L3 ship first?  
4. **L4 kill:** Do you accept the ≤3-day compile hard stop (§7.3), with automatic switch to E2/stop?  
5. **Reservoir scale:** What is the smallest sealed |R| and stratum count you will call “one valid block” (one twin pair vs multi-block freeze)?  
6. **Quality idea:** Should the positive-control injected coupling be specified *before* L4 annex writing, so compile work is sized to the probe rather than to generator completeness?

---

ENGINEERING_ROUTE=STOP_UNTIL_SCIENTIFIC_CONTRACT


