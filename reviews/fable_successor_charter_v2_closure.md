# Fable 5 — successor charter v2 closure memo

Author: Fable 5. Companion to `successor/CHARTER_V2_DRAFT.md` (complete
replacement of v1; v1 and every review preserved unedited). Inputs: the
Opus X-line review (X-A–X-J) and Sol Y-line review (findings 1–11 +
R1–R8), both `REVISE_SUCCESSOR_CHARTER_V1` at commit `c865297`; the
Route B decision; the canonical record. Nothing was committed; no
existing file was modified; the unrelated working-tree header change in
`reviews/sol_successor_charter_v1_review_prompt.md` was left untouched.

## Verdict

**READY_FOR_SUCCESSOR_CHARTER_V2_XY_CONFIRMATION**

## 1. Findings remaining after revision

### Critical

None known. Both Critical defects (X-A/Sol-2 predictable Q worlds;
Sol-1 missing Q family guarantee) are repaired at charter level.

### Major

- **V2-1 — the conservative no-scout sample-size rule may price C
  high.** Popoviciu-type bounds on a censored endpoint are loose; the
  default may demand a larger C than a nuisance-informed rule would.
  This is the deliberate cost of the smaller information surface; the
  strict-S alternative exists precisely for the case where the
  conservative N is unaffordable, and switching to it is a signed
  architecture amendment, not tuning. Residual, priced, named.
- **V2-2 — unified charging makes crashes expensive.** A process-invalid
  launch burns a cap slot and error allocation. This is the strict
  reconciliation both mandates require (no uncharged recovery pool); it
  buys crash-farming immunity at the price that platform instability
  can exhaust Q without a scientific look. Mitigation is engineering
  (WP-2/WP-4 hardening before any launch), not statistical. Residual,
  named.

### Minor

- **V2-3** — the beacon-vs-sealed-root cell leaves two custody designs
  alive until the Q contract; both satisfy §2's independence property,
  but X/Y will need to re-review whichever is instantiated.
- **V2-4** — layout/name remain open (author infrastructure cells);
  WP-1 cannot start until chosen.

## 2. Disposition table — Opus X-A–X-J, Sol 1–11

| Finding | Substance | Disposition | v2 |
|---|---|---|---|
| **X-A** (Crit) | Q worlds precomputable from public dev-root | **Adopted (R-A)**: Q removed from dev-root; per-attempt randomness exists only after durable manifest+claim freeze; 6-step ordering; independence property stated; mechanism deferred as signed cell | §2 |
| **X-B** | lock/escrow order self-contradictory | **Adopted (R-B)**: single canonical order, lock strictly before escrow, stated once and cross-referenced | §9 |
| **X-C** | device freeze contradictory; qualify-on-X/confirm-on-Y | **Adopted (R-C)**: stack in manifest, frozen before Q randomness; promotion carries manifest unchanged; standalone stack-freeze step removed; changed stack = new candidate | §5 |
| **X-D** | scout restriction rhetoric, not mechanism | **Adopted, strictest form**: Sol R4 contract governs the S option; **draft default is no scout at all** | §6 |
| **X-E** | predicate numerics tunable around a favored learner | **Adopted (R-E)**: candidate-blind numerics signed before any candidate registration; no-candidate-tuning; invariant meaning | §4 |
| **X-F** | first-to-qualify search-order exploitable; binary-only rule unstated | **Adopted (R-F) and strengthened**: serial durable queue with durable submission order; automatic promotion; no-Q-fact-beyond-binary+validity+predeclared-eligibility | §5 |
| **X-G** | recovery crash-farmable | **Adopted in the stricter Sol form**: unified charging replaces the two-ceiling design (see strictness table) | §4, §8 |
| **X-H** | "separate repo scientifically stronger" overstated | **Adopted (R-H)**: claim withdrawn; semantic quarantine + path-allowlist carry the guarantee; layout an author cell on engineering grounds | §1a |
| **X-I** | conditionality must ride in the estimand | **Adopted (R-I + Sol R1)**: full formal scope object, `selection_scope_id`, design-conditional proof semantics | §1c |
| **X-J** | scout-statistics cell must be typed | **Superseded by the no-scout default**; under S the released surface is schema-typed per R4 | §6 |
| **Sol 1** (Crit) | no Q family false-pass control | **Adopted (R2)**: `δ_Q`, attempt-wise spending/always-valid rule, finite caps, formal guarantee | §4 |
| **Sol 2** (Crit) | public dev-root defeats freshness | **Adopted (R2)**: same repair as X-A | §2 |
| **Sol 3** (Crit) | scout bridge unsafe | **Adopted (R4)**: strict nuisance-only contract for S; margins/horizon never scout-informed; conservative fallback mandatory; default drops S entirely | §6 |
| **Sol 4** (Crit) | confirmatory multiplicity unowned | **Adopted (R8)**: five families assigned pre-data; conjunction/gatekeeping for proof | §7 |
| **Sol 5** | estimand named, not defined | **Adopted (R1)**: `H_TQ`/`H_preC`/`d*`/`s*`/`L*`/`P_C`, permitted claim wording, forbidden claims | §1c |
| **Sol 6** | "same construct" is not a population contract | **Adopted (R5)**: eight-object pre-T contract; disjointness ≠ exchangeability; `P_Q`↔`P_C` relation; one C interpretation | §3 |
| **Sol 7** | Q predicate shape too weak | **Adopted (R6)**: invariant population-assurance meaning; blind numerics; engineering gates separated from competence floor | §4 |
| **Sol 8** | terminal taxonomy not exclusive/total | **Adopted (R7)**: full state machine; missing/non-finite ownership pre-data; distinct process endings | §8 |
| **Sol 9** | post-Q discretion in promotion | **Adopted (D)**: serial first-valid-qualifier is the charter rule (mandated draft default), not an option | §5 |
| **Sol 10** | C randomness timing needs one sentence | **Adopted**: contract-before-T / entropy-after-lock stated in §3 and §9 | §3, §9 |
| **Sol 11** | process endings need stable names | **Adopted**: `T_ENVELOPE_EXHAUSTED`, `T_AUTHOR_STOP`, `Q_CAP_EXHAUSTED_NO_QUALIFIER` etc. | §8 |

Nothing was averaged away; every repair is the stricter of the two
where they differed.

## 3. Strictness table (reviewer differences)

| Topic | Opus proposed | Sol proposed | Resolution |
|---|---|---|---|
| Q attempt accounting | cap counts valid completed attempts + separate bounded signed ceiling for process-invalid recoveries | every launch consumes id, error allocation, cap slot, including invalid launches | **Sol (stricter, per mandate): unified charging, no uncharged pool.** Not incoherent: a crash costs a slot — fail-closed pricing. Opus's crash-farming concern is met a fortiori (V2-2 names the residual platform-instability cost) |
| Promotion | both variants permissible with added constraints (binary-only, pre-committed order) | serial queue, automatic first valid qualifier, no author choice after Q | **Sol (stricter, per mandate): automatic serial rule is the charter rule.** Opus's constraints (durable order, binary-only) are embedded in it |
| Scout | fix a direction-blind schema now or drop; drop is the honest fallback if scale leaks | strict invariance-proved nuisance channel; optional only with predeclared fallback; never margins/horizon | **Sol's contract governs the S option; the draft default drops S entirely** — the strictest information surface (zero extra released bits), chosen on governance cost, not evidence |
| Predicate-numerics sign point | before any candidate is **registered** | before the first candidate **enters Q** / first attempt | **Opus (earlier = stricter): before any candidate registration**, immutable after first launch |
| Q entropy mechanism | post-freeze OS-CSPRNG draw by reviewed driver | beacon or sealed root, both valid under stated conditions | **Deferred as a signed Q-contract cell** (mandate permits), bound by §2's conditional-independence property that both reviewers stated equivalently |

## 4. Corrected temporal/freeze table

The single order (charter §9): pre-T population/construct contract →
T development → Q contract signed (before any candidate registration)
→ serial charged Q attempts → first valid pass = automatic promotion →
[optional signed S] → scientific spec → X/Y review → author signatures
→ **durable preregistration lock** → **post-lock** secret C root +
realization → ciphertext/salted-hash commitment → separate execution
authorization → one-shot C execution → authorized unsealing. The v1
escrow-before-lock inversion (X-B) is corrected; the standalone
promotion-time stack freeze (X-C) is deleted; the C
contract-before-T / entropy-after-lock split (Sol 10) is explicit.

## 5. Q false-pass and candidate-equivalence contract (formal)

Let `canonical(m)` canonicalize the executable scientific manifest
(learner code commit, optimizer, policy, interface, config, stack);
candidates are equivalent iff their canonical forms are equal;
behavior-inert edits preserve `canonical(m)`, behavior-relevant edits
change it (new candidate, same total cap). For launch `j` with
candidate `c_j` frozen before its Q randomness and `H_{<j}` the full
adaptive prior history:

```text
Pr(Q_PASS_j | H_{<j}, c_j Q-incompetent) ≤ α_j          (attempt-wise)
Σ_{j=1}^{J_total} α_j ≤ δ_Q                             (family budget)
#{j : canonical(c_j) = k} ≤ m_class  for every class k  (per-class cap)
J_total finite; every launch — valid or invalid — consumes one j,
its α_j, and one total-cap slot; no reuse, no redraw
⇒ Pr(∃ j : Q_PASS_j ∧ c_j Q-incompetent) ≤ δ_Q
```

by union bound, or by a predeclared always-valid sequential rule.
`Q-incompetent` is the common invariant population predicate of §4
(competence on fresh units from `P_Q` below the signed floor). Values
of `α_j`, `δ_Q`, `J_total`, `m_class` are Q-contract cells; the
inequality structure is charter law.

## 6. Selected-design estimand and permitted public claim

Charter §1c: every C estimand/verdict is conditional on `H_preC`,
`d* = R(H_TQ)`, `s*`, `L*`, averaging only over worlds and any seed law
named by `P_C` and `L*`; every verdict carries `selection_scope_id` =
hash of those objects. In the ACTIVE-vs-YOKED orientation:

```text
Δ_C1^sel = E_{w~P_C}[ Y_YOKED(w; d*,s*,L*) − Y_ACTIVE(w; d*,s*,L*)
                      | H_preC, d* = R(H_TQ), s*, L* ]
```

(finite frame: the locked design-weighted frame mean; census:
descriptive of the frame). Permitted claim: the §1c blockquote —
selected locked design on the locked C population only. Forbidden:
search-procedure, learner-class, Route-B-general, and out-of-population
claims. `PROOF_CORE`/`PROOF_STRONG`, if earned, are design-conditional
in the estimand.

## 7. Scout surface-count decision and rationale

**Decision: no scout (three data surfaces); strict S available only by
separate author signature that also amends the architecture token.**
Rationale: the only cells S may lawfully inform are blinded sample size
and label-free engineering caps. Engineering caps are already available
label-free from Q telemetry (Q has no arms); sample size has an honest
conservative fallback (bounded-outcome variance + resource envelope).
S would buy a possibly smaller C at the cost of a sealed evaluator, an
invariance proof, custody, and its own review cycle — a governance-cost
trade, not an evidence question, and stated as such in the charter. If
the conservative N proves unaffordable at spec time, signing S then is
a loud amendment, not tuning.

## 8. Cells still requiring Kirill's later choice

Layout/final name (before WP-1); C interpretation type (WP-3, pre-T);
T envelope (pre-T); Q unpredictability mechanism (Q contract); optional
off-CPU breathing check (T time); strict-S adoption (before promotion);
all numeric cells at their owning gates (§11 table). None was chosen in
v2.

## 9. Signature-token readiness

The three tokens (`I_ACCEPT_PHILOSOPHIA2_CHARTER_V2`,
`I_ACCEPT_THREE_SURFACE_PHASE_ARCHITECTURE`,
`I_ACCEPT_SELECTION_CONDITIONAL_CONFIRMATORY_CLAIM`) are ready **only
for bounded X/Y confirmation of this v2 text — not yet for author
signature.** Both confirmations must accept before any token is
signable; the third token normatively accepts §1c's estimand and
limited generalization, per Sol's disposition; the second carries the
recorded amendment duty if S is later signed.

## 10. Questions for Kirill (four)

1. **C interpretation type:** fixed-frame census, probability sample
   from a fixed finite frame, or named superpopulation? (Chooses the
   kind of generalization; needed at WP-3, before T.)
2. **Q randomness mechanism preference:** post-freeze public beacon or
   one-shot sealed root under procedural custody? (Both satisfy the
   independence property; custody and audit differ.)
3. **Planning default:** do you accept the no-scout default with its
   conservative (possibly larger) confirmatory sample size, keeping
   strict S as a signed later option?
4. **Infrastructure:** repository layout and final name (engineering
   grounds only, per §1a) — and if T converges off-CPU, do you want the
   optional non-citable breathing check?

## 11. Bounded confirmation questions

**Opus (X):** (1) Do §2's six-step ordering and independence property
close X-A completely — is there any residual path by which a frozen
candidate can predict or influence its Q sample under either
unpredictability mechanism? (2) Does §9's single order, with §5's
manifest rule, close X-B and X-C everywhere the v1 text contradicted
itself — no escrow-before-lock, no post-Q stack choice, for every
manifested field? (3) Does the unified-charging rule (Sol's form)
preserve your X-G intent — no crash-farming, no automatic rerun — with
the V2-2 residual acceptably named? (4) Is the no-scout default plus
strict-S-by-amendment an acceptable resolution of X-D/X-J, with no
rhetoric-only restriction remaining?

**Sol (Y):** (1) Do §4 and closure §5 implement your R2/R6 guarantee —
finite caps, `δ_Q` spending over every launchable attempt including
invalid launches, canonical equivalence, candidate-blind invariant
numerics signed before registration? (2) Does §1c + closure §6 land R1
so that every verdict is scoped by `selection_scope_id` with the exact
permitted/forbidden claim split? (3) Does §3 pin all eight population
objects with contract-before-T / entropy-after-lock timing (R5, finding
10), leaving T genuinely open on the learner side only? (4) Do §7 and
§8 land R8 and R7 — five multiplicity families owned pre-data, and an
exclusive total terminal machine where no process state can become
censoring, a boundary, or `INSUFFICIENT`?

## 12. Negative space and change-proof

The stopped line remains immutable and `OPEN`; Level 1 remains
`BLOCKED_LEVEL1_FEASIBILITY`; C1 unrun and untested there; v1/v2
non-comparable, non-citable, and they chose nothing here — no learner,
world, budget, margin, threshold, cap, alpha, promotion winner, or
device. T and Q can never earn, kill, or boundary-label C1–C6; only a
valid, independently locked C confirmation may move successor claims,
within its selected-design/population scope. "No qualifier," censored,
`UNKNOWN`, and every invalid state are never success, equivalence, a
boundary, or learner impossibility. `PROOF_CORE`/`PROOF_STRONG` remain
earned by nothing; the programme claim stays `OPEN`.

**Change-proof:** this task created exactly two new files
(`successor/CHARTER_V2_DRAFT.md`, this memo) and committed nothing. No
existing file was modified — v1, all reviews, canonical records, essay,
ROADMAP, README, atlas, and user-owned `essay/OUTLINE.md` (and the
pre-existing working-tree change to the Sol prompt header) are
untouched. No code, entropy, world, model, learner, run, Q attempt,
scout, promotion, specification, authorization, escrow, lock, or
outcome was created; no numeric cell was chosen; no series inspected;
no arms compared; no v1/v2 contrast formed.
