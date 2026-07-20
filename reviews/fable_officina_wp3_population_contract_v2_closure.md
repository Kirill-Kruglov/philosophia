# Fable 5 — Officina WP-3 contract v2 closure memo

Author: Fable 5. Companion to
`successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V2_DRAFT.md`
(complete replacement; the v1 draft and both reviews preserved
unedited). Inputs: Opus (`REVISE_OFFICINA_WP3_CONTRACT`, W3-C1,
W3-M1..M6, W3-m1..m2) and Sol (`REVISE_OFFICINA_WP3_CONTRACT`,
findings 1–12, R1–R10). Nothing committed; no existing file changed.

## Verdict

**READY_FOR_OFFICINA_WP3_V2_XY_CONFIRMATION**

## 1. Disposition table (one-to-one)

| Finding | Disposition | v2 |
|---|---|---|
| **W3-C1 / Sol-1** (Critical) — printed Q reserve wrong, overlaps C frame | **Adopted**: v1 list withdrawn as a transcription error by name; rule-derived set `{28,29,32,33,38,39,42,43,48,49,52,53,58,59,62,63}` printed; full `(h,j,p,block,assignment)` table; machine-recomputed regression vectors; mandatory pre-emission `Q∩C=∅` / coverage / cardinality / balance / exclusion checks | §2a, §3 |
| **W3-M1 / Sol-4, Sol-10 / R1, R2** — CH-1a+CH-2a-only text | **Adopted**: generic `n0`, `p(h,j)`, `b_{h,j}` formulas; branch-complete design table (`N_h`, `N_C`, `q_h`, `W_h`, `π_h`, FPC, census, claim-capable `n_h`) for both CH-2 branches; CH-2b instantiated independently; high band determined by the same formula with `n0 = 126`; no sentence true only for the recommended branch | §2, §2b |
| **W3-M2** — frame schema unspecified | **Adopted**: exact canonical-JSON field list, types, orderings, derived-array regression rule, hash procedure, token/contract-hash bindings | §3 |
| **W3-M3 / R4-adjacent** — wire grammar; PAD/SEP conflation | **Adopted**: query/answer/typed-refusal wire formats pinned; PAD/SEP reclassified as learner/WP-9 encoding constants, never oracle-visible; oracle defined on `{R,L}` only | §4 |
| **W3-M4** — caller-supplies-`n` route | **Adopted**: capability-gated constructors; no public arbitrary-`n` oracle; contractual invariant stated; enforcement assigned to reviewed WP-4 code/tests; path-policy routes noted as already discharged | §4 |
| **W3-M5** — T-dev bands unjustified, not CH-1-coherent | **Adopted with an invariant rule (no author cell needed)**: fixed set `[10,25] ∪ [166,205]`, disjoint from both candidate bands and the predecessor registry; near band contiguously adjacent to the frame under **both** CH-1 branches; extrapolation property named (across modulus identity at adjacent scale; distal band = deliberate scale stress) | §5 |
| **W3-M6 / item 10** — shortcut solvers; over-claim foreclosure | **Adopted**: selection-conditional interpretability retained; forbidden language extended — absent a WP-6 admissibility rule, no "learned the modulus/construct," "represents the group," "validates small-learner/contact mechanism" narration; WP-6 rule not chosen | §6 |
| **W3-m1** — donor transcript/`B` ownership | **Adopted**: stated WP-9 in §1 | §1 |
| **W3-m2** — reserve bound branch-specific | **Adopted**: superseded by per-stratum depletion inequalities | §7 |
| **Sol-2 / R3** (Critical) — orientation estimand undefined | **Adopted**: base block unordered; author cell OR with two coherent alternatives — OR-1 orientation-averaged two-stage (target, unbiased estimator, two-component variance with the unidentifiable `σ²_{R,b}` term and WP-9 route obligation) and OR-2 realized-orientation conditional (full-frame vector, sealed `C_design_realization_id`, exact estimation, claim conditions named); recommended OR-2; not selected; "census removes orientation/seed randomness" explicitly forbidden under both | §8 |
| **Sol-3 / R4** (Critical) — `[0,B] ∪ {censored}` not a numeric object | **Adopted**: typed observation `(X, Δ)`; WP-3 fixes type only; Sol's ownership sentence carried in substance verbatim | §1 |
| **Sol-5 / R5** — `n_h = 1` presented as usable | **Adopted**: exact small-stratum rule; claim-capable rows per branch in the design table | §2b |
| **Sol-6 / R7** (Major) — exchangeability language unsound | **Adopted**: withdrawn; replaced by the author-accepted fixed-frame target-competence transport premise with dedicated token, licensed/not-identified lists, the single-world-cannot-validate-comparative-machinery statement, and the required pre-C non-outcome engineering validation | §7 |
| **Sol-7, Sol-8 / R6** — launch-product shortcut; adaptive depletion | **Adopted**: `Σ_ℓ m_{ℓ,h} ≤ q_h` per stratum + total bound; `P_{Q,ℓ}` conditional on history/registry/candidate/attempt; every charged launch consumes; full-coverage ceilings 4/6 stated; other schedules owned by WP-6 with proof; eight-launch example withdrawn; `E2 = 12` a registration ceiling only | §7 |
| **Sol-9 / R8** — stratum multiplicity overbroad | **Adopted**: family follows the claim (C1/C2–C4/C5/C6); descriptive summaries locked non-inferential with the exact prohibited devices | §9 |
| **Sol-11 / R10** — CH recommendations' rationale | **Adopted**: CH-1 provenance kept as word-length/resource planning; CH-2 rationale rebuilt on conditional branch-complete arithmetic; expected-qualification/effect readings forbidden | §10, §12 |
| **Sol-12 / R9** — partition/selection boundary | **Adopted**: conditioned-on design facts; weights correct only unequal C inclusion — the exact non-adjustment list carried in | §6 |

Nothing was dropped; no scientific ambiguity is resolved by prose alone
— every load-bearing repair is a formula, table, machine check, typed
object, or dedicated token.

## 2. Corrected arithmetic (all CH-1 × CH-2 branches)

With `b_{h,j} = {n0+2[p−1], n0+2[p−1]+1}`, `p = 5(h−1)+j`:

| Branch | C blocks (`p`) | Q worlds |
|---|---|---|
| LOW × C-rich (`n0=26`) | {1,3,5,6,8,10,11,13,15,16,18,20} | {28,29,32,33,38,39,42,43,48,49,52,53,58,59,62,63} |
| LOW × Q-rich | {3,5,8,10,13,15,18,20} | {26,27,28,29,32,33,36,37,38,39,42,43,46,47,48,49,52,53,56,57,58,59,62,63} |
| HIGH × C-rich (`n0=126`) | same `p` sets | {128,129,132,133,138,139,142,143,148,149,152,153,158,159,162,163} |
| HIGH × Q-rich | same `p` sets | {126,127,128,129,132,133,136,137,138,139,142,143,146,147,148,149,152,153,156,157,158,159,162,163} |

Machine-verified: `Q ∩ C = ∅` and `Q ∪ C = [n0, n0+39]` in every
branch; `q_h = 4/6`, `N_h = 3/2`, `W_h = 1/4` throughout; design
quantities per §2b. Full-coverage launch ceilings: 4 (C-rich), 6
(Q-rich) — conditional on the WP-6 coverage design, promising nothing.

## 3. Complete proposed author-token packet (none signable now)

```text
I_ACCEPT_OFFICINA_WP3_POPULATION_CONTRACT
I_SELECT_OFFICINA_FRAME_BAND_LOW | I_SELECT_OFFICINA_FRAME_BAND_HIGH
I_SELECT_OFFICINA_SPLIT_C_RICH  | I_SELECT_OFFICINA_SPLIT_Q_RICH
I_SELECT_OFFICINA_ORIENTATION_AVERAGED_BLOCK_ESTIMAND |
  I_SELECT_OFFICINA_ORIENTATION_CONDITIONAL_FIXED_VECTOR_ESTIMAND
I_ACCEPT_OFFICINA_Q_TO_C_TARGET_COMPETENCE_TRANSPORT_PREMISE
```

Exactly one token per choice row; the transport token is dedicated and
not subsumable; refusal destinations are named in v2 §10 (including
the transport refusal routing to a charter-level redesign decision).
T-dev geometry carries no token — §5's invariant rule removed that
cell. Recommendations: LOW, C_RICH, CONDITIONAL, accept — all on
pre-data scientific/resource grounds only.

## 4. Replacement index (v1 → v2)

| v1 section | v2 section |
|---|---|
| §1 unit/roles/outcomes | §1 (unordered block; `(X,Δ)`; WP-9 ownership of transcript/`B`) |
| §2 construct/support | §2 (generic formulas) + §4 (wire grammar; PAD/SEP removed from construct) |
| §3 enumeration/partition/T-dev | §2a (corrected enumeration + regression vectors), §3 (schema), §5 (T-dev invariant rule) |
| §4 C measure | §2b + §6 (branch-complete; claim boundary extended) |
| §5 `P_Q`/relation | §7 (depletion inequalities; transport premise; information boundary) |
| §6 estimand/multiplicity | §9 (family-of-the-claim rule) |
| §7 seeds | §9 |
| §8 interpretation/forbidden | §6 (extended forbidden list) |
| §9 checks | distributed: §3 machine checks, §4 capability invariant, §7 spendability, §12 provenance |
| §10 author cells | §10 (four cells incl. OR + transport) |
| §11 WP-4 | §11 |

## 5. Bounded final-confirmation questions

**Opus (three):**

1. Do §2/§2a/§3 make the frame byte-reproducible for **all four**
   CH-1 × CH-2 combinations from the contract alone — rule governs,
   regression vectors check, generator bound to contract hash +
   selected tokens, machine checks fail-closed — with no hand-copied
   list left authoritative?
2. Does §4 close the caller-supplies-`n` route at the contractual
   level (capability invariant + no public constructor + Q/C
   capabilities nonexistent until their roots), with exactly the
   enforcement remainder you assigned to reviewed WP-4 tests?
3. Does §5's invariant T-dev rule (fixed `[10,25] ∪ [166,205]`,
   contiguously adjacent near band under both CH-1 branches, named
   extrapolation property) resolve W3-M5 without a hidden
   CH-1-dependent side effect — or do you still require an author
   cell?

**Sol (three):**

1. Do §8's two orientation alternatives state the target, estimator,
   variance obligations, realization/freeze, serialization, and claim
   scope exactly as your R3 requires — with the OR-1 second-component
   identifiability gap and the census caveat carried verbatim in
   substance, and no mixing of the two meanings anywhere in v2?
2. Do §7's depletion inequalities, attempt-indexed `P_{Q,ℓ}`, charged
   invalid launches, withdrawn eight-launch example, and the
   dedicated transport token with its licensed/not-identified lists
   land R6/R7 completely — and is the pre-C engineering-validation
   requirement placed at the right ownership level?
3. Do §1's `(X,Δ)` typed observation, §2b's small-stratum rule, §6's
   claim-boundary additions, and §9's family-of-the-claim multiplicity
   rule land R4, R5, R9, and R8 respectively, with no residual
   sentence that averages an undefined object or absorbs a C2–C5
   stratum claim into C1?

## 6. WP-4 handoff

WP-4 drafting/implementation remains **unavailable** until (i) this v2
receives both bounded X/Y confirmations and (ii) Kirill signs the
complete packet of §3 (contract token + CH-1 + CH-2 + OR + transport).
Scope and mechanical impossibilities are fixed in v2 §11. T activation
additionally requires the signed envelope's activation ledger event.

## 7. Bootstrap integrity

`python scripts/verify_officina_wp12.py` →
`OK: Officina WP-1/WP-2 bootstrap is quarantined and inactive.` (run
read-only for this closure). The exact `successor/officina/` bootstrap
set (`LINEAGE.json`, `PATH_POLICY.json`, `README.md`, `T_ENVELOPE.json`,
`T_LEDGER.md`, `T_LEDGER.md.head.json`, `WP1_WP2_IMPLEMENTATION.md`)
is unchanged; this task added no file under `successor/officina/` and
edited nothing anywhere.

## 8. Negative space

No entropy, world, frame instance, sample, panel, candidate, manifest,
datum, ledger event, root, lock, escrow artifact, T activation, Q/C
process, learner run, outcome, Proof, or claim movement was created or
authorized. T remains `NOT_ACTIVATED` at the genesis head. The
predecessor line remains immutable, `OPEN`, and
`BLOCKED_LEVEL1_FEASIBILITY`; its records are non-citable and chose no
value here. Officina's T and Q can never earn, kill, or boundary-label
C1–C6; a future Q pass is a spendability gate fact only; S is
unavailable; only a valid, independently locked C execution may move an
Officina claim — within its selection-conditional, selected-frame,
orientation, device, and learner-seed scope. No qualification,
scientific direction, or programme success is predicted.
`PROOF_CORE`/`PROOF_STRONG` remain earned by nothing; the programme
claim stays `OPEN`.
