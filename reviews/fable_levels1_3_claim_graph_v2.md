# Fable 5 — Levels 1–3 claim graph, revision 2 (post X/Y review)

Author: Fable 5. Supersedes `fable_levels1_3_claim_graph.md` (v1), which is
preserved as the reviewed artifact. This is the bounded correction pass
mandated after Opus (X-line, `REVISE_CLAIM_GRAPH`) and Sol (Y-line,
`REVISE_CAUSAL_DESIGN`). No code, no lock, no scout, no escrow, no numeric
threshold, no outcome prediction. Every review finding is either adopted with
its exact repair or answered with a named reason; none is silently dropped.

**Status: CLOSED_FOR_SIGNATURE.** With the corrections below, the claim graph
and the Level 1 core are closed as designs; nothing may execute until the
seven signature lines in §8 are answered, and Level 1 may not lock until the
gate ledger in §7 is green.

**Accepted direction preserved (unchanged):** R1 (a Level 1 null kills
chosen-contact advantage only), R2's direction (realized answer entropy is
not a matching target), R3 (Level 2 infrastructure parallel, execution gated
on the Level 1 decision), R4 (renamed-token = positive anchor, not C3), R5
(C6 constitutionally non-decisive), C5 required for the strong Proof but not
the retained-history core, C6 explains but never decides/rescues/vetoes.

**One named contradiction found and resolved.** The essay's §VII Proof
paragraph lists "compression and progress measures survive their nulls" as a
Proof condition. That sentence, read as a conjunct, makes C6 decisive —
contradicting accepted R5. Resolution (in favor of R5, by signature line S1):
C6-null survival is reported as a mandatory *annotation* on any strong-Proof
narration, never a conjunct that can grant or veto the verdict. This is the
single place this revision touches the essay's meaning, it is a strengthening
of discipline rather than of claim, and it is named here rather than done
silently.

---

## 1. Two proof layers (closes Opus C-2; mandate §1)

Machine-readable names, fixed before any outcome:

- **`PROOF_CORE`** = C2 ∧ C3 ∧ C4. The retained-history core: contact-derived
  history shortens forward work on unseen families, survives the
  semantics-preserving presentation change, and is traceable to truthful
  content against weights-only, ledger-only, and false-ledger controls.
- **`PROOF_STRONG`** = `PROOF_CORE` ∧ C1 ∧ C5. The essay's §VII Proof,
  preserved at full strength: additionally, chosen contact beats matched
  off-target active geometry (C1) and path-invariant credit grows more
  transferable structure than destination credit (C5).

**Reporting rules (locked; no narration drift):**

- Every verdict carries a **contact-mode scope annotation**:
  `[contact=ACTIVE | YOKED-GEOMETRY | RANDOM-STATIC]` (Opus M-6). A
  `PROOF_CORE[contact=RANDOM-STATIC]` is a weaker claim than
  `[contact=ACTIVE]` and is never narrated as actively earned.
- `PROOF_CORE` with C1− → reported as
  `PROOF_CORE + BOUNDARY_CONTACT_CHOICE`; the essay may say the retained-
  history core held and *choice* was not the active ingredient. It may not
  use the unqualified word "Proof," which the essay reserves for
  `PROOF_STRONG`.
- `PROOF_CORE` with C5− → `PROOF_CORE + BOUNDARY_P_AXIS_REDUNDANT`; the
  phrase "manufactured experience" in the bundle-of-paths (P-axis) sense is
  forbidden (Opus C-2); the destination-credit equivalence is published as
  the map already promises.
- `PROOF_CORE` with C5 not run → `PROOF_CORE (C5_UNRESOLVED)`; the strong
  Proof is *unavailable*, not failed; C5 is named as the first successor
  wall. Same for C1 not run.
- C6 status is always reported as an annotation (`C6: passed nulls | failed
  nulls | not run`) and never appears in a verdict condition.
- First-hand criterion (Opus M-6, positive and checkable, part of clause 1):
  in every arm counted as first-hand contact, the learner itself issues
  every oracle query against its own world instance and receives raw oracle
  bits; no pre-solved examples, no externally authored solution traces, and
  no other run's answers enter its input stream. RANDOM-STATIC contact
  satisfies this (its query *positions* are externally fixed; its contact is
  its own); arm D does **not** (it consumes another run's record — §3).

## 2. Repaired C2/C4 truth table (closes Opus C-1, m-2, m-3; Sol M4, M6; mandate §2)

**Deterministic, exclusive evaluation order.** Each step consults only locked
comparisons; any comparison that is unresolved at its locked margin/rule
(N6) stops the cascade at `INSUFFICIENT` — never a boundary, never success.
Positive claims are superiority claims; every `≈` / "no worse" is a
margin-locked equivalence/non-inferiority claim under **N6 (unresolved):
equivalence margins and interval/test rule (TOST-style), set at the Level 2
lock**.

0. Any locked invalidity (leakage, escrow breach, budget mismatch,
   non-finite, arm contamination, unmatched neutralization) →
   `PLATFORM_OR_DESIGN_INVALID`. No scientific verdict.
1. **C2 gate:** C > A on same-presentation escrow (superiority). Fail →
   `FALSIFIED_AT_C2`. Unresolved → `INSUFFICIENT`.
2. **C3 gate:** C > A on the destination presentation (superiority), with
   both presentation anchors green (renamed-token and native-Cayley
   competence — §4; anchor failure is step 0, not a finding). Fail →
   `BOUNDARY_REPRESENTATION`. Unresolved → `INSUFFICIENT`.
3. **C4 layer — condition on B and D before any verdict (the v1 error,
   Opus C-1):**
   - a. `E ≈ C > A` **and** `B ≈ A` **and** `D ≈ A` → `FALSIFIED_AT_C4`:
     ledger *form* reproduces the effect with no content-bearing channel;
     the empirical C > A shortening stands as a recorded fact, but its
     experience reading is reclassified placebo/format-sensitive (Sol Y4
     wording adopted).
   - b. `B ≈ C > A` (weights alone reach C; C ≯ B) → `BOUNDARY_WEIGHTS_ONLY`:
     weight-borne forward shortening is real and C2 stands; truthful-ledger
     traceability is not established.
   - c. `D ≈ C > A` (fresh + inherited ledger reaches C) →
     `BOUNDARY_INHERITED_LEDGER` (renamed from v1's
     `BOUNDARY_LEDGER_SUFFICIENT`): the record is independently sufficient —
     a boundary **on clause 1 first-handedness** (Opus M-5), because D is
     the inherited-example control, not positive first-hand evidence.
   - d. Both (b) and (c) hold → `BOUNDARY_REDUNDANT_MEMORY` (joint cell,
     Opus m-3).
   - e. C4 earned iff: `C > B` (truthful-ledger increment over weights,
     superiority) **and** `C > E` (content over form, superiority — the
     decisive traceability estimand, Opus m-4/Sol Y4) **and** `E ≯ B`
     (margin-locked non-inferiority: form adds nothing beyond weights),
     with D reported as the inherited-example coordinate. Then proceed to
     the proof layers of §1.
   - f. Any other configuration or unresolved cell → `INSUFFICIENT`.

**Frozen Level 2 contrast hierarchy (conceptual; margins N6):**

| Contrast | Meaning | Role |
|---|---|---|
| C − A | full retained-history package | C2 primary |
| B − A | weights channel | channel |
| C − B | truthful-ledger increment over weights | C4 necessary |
| C − E | truthful content vs false content, weights fixed | C4 decisive |
| E − B | ledger-form/placebo diagnostic | C4 control |
| D − A | inherited-ledger portability control | clause-1 coordinate |
| (C−B) − (D−A) | complementarity | descriptive unless separately powered and preregistered |

Multiplicity is controlled inside this family; hierarchy C2 → C3 → C4 →
channels; no later family rescues a failed earlier necessary claim (Sol M6).

**Budget statement (corrects v1's false sentence, Opus M-11):** the five arms
do **not** have identical contact. They have identical new-destination
access and deliberately different retained-history provenance. Query,
oracle, replay, optimization, token, and memory budgets are matched or
explicitly neutralized (A replays its own fresh data or replay compute is
neutralized; locked at L2). The false ledger E is valid as a placebo only
after a preregistered indistinguishability validation (a form-discriminator
cannot separate true from false ledgers on matched token/length/surprise
statistics; corruption mechanism specified at L2 lock) (Opus M-12).

## 3. Level 1 core: endpoint and donor construction (closes Opus C-3, M-1..M-4, m-1, m-5; Sol C1, C2, C3, M2, M3, m3; mandate §3)

**Common budget, no early stop, blind evaluator.** One common maximum oracle
budget **B** for every arm. No arm stops early. The learner and the
acquisition policy never see the escrow evaluator's solve decision; the
evaluator computes the **first persistent certified solve** post hoc at a
locked cadence from frozen artifacts. ACTIVE therefore produces a complete
B-query donor transcript under the frozen acquisition rule even if
evaluation later shows it crossed the criterion early — donor transcript
availability can never depend on donor outcome (Sol C2; kills the
stopping/censoring triple of Opus C-3 at the root).

**Primary endpoint (closed):** right-censored **budget-to-certified-solve
within B**. The solve event = persistent performance on an arm-independent,
escrowed, family-stratified, class-balanced EQ panel, plus locked
calibration, ABSTAIN, and confident-lie constraints. Order probes are
secondary, family-specific diagnostics only (Sol C3). Non-solve at B is
censored/UNKNOWN — never success, never a late tie. Estimand (sign fixed,
Opus M-1):

> Δ_choice = E over target blocks and seeds of
> [RMST_YOKED(B) − RMST_ACTIVE(B)], restricted mean solve time to horizon B;
> **positive Δ_choice = ACTIVE reaches certified truth with lower budget.**

If a bounded-cost variant is used (non-solves scored at B), it is named a
*bounded cost score*, never an uncensored time-to-solve. Deterministic
rules: ties at equal budget = zero contrast; ABSTAIN is never a solve;
repeated queries cost one unit each, return the same bit, and are never
silently deduplicated (Sol m3); exhaustion without solve = censored. All
numeric thresholds (persistence cadence, calibration bounds, panel sizes)
remain **unresolved N-series**, justified pre-outcome at lock.

**Independent-donor yoking (replaces v1's single cyclic derangement).**
Adopted as the smallest clean version; I do not claim a smaller design is
equally valid — the single derangement fails honest variance (Opus M-2, Sol
C1/M3: cycle coupling), and repairing it by randomization-over-σ alone still
leaves donor and target roles entangled in one pool. Construction:

- Evaluated **target worlds** and **donor worlds** are disjoint sets sampled
  from the same locked stratum distribution.
- Every YOKED target receives a full-B query sequence from exactly one
  ACTIVE **donor world**, under a locked one-to-one assignment **within
  exact declared strata**: family, order/size band, generator count,
  presentation, grammar regime (Opus M-3; Sol C1).
- Donor answers never transfer; YOKED receives honest answers from its own
  target oracle.
- Donor transcripts are **hash-committed before any YOKED derivation**
  (Opus m-1). Donor generation is part of the locked experiment — donor
  runs are not a result arm, and the v1 phrase "generated before outcome"
  is withdrawn: YOKED inputs are a pre-specified deterministic function of
  committed donor transcripts and the locked assignment.
- **Units:** the target world block is the scientific and variance unit;
  seeds are repeated measures; checkpoints are time observations; query
  rows are never units. Donor-assignment uncertainty is represented in the
  locked analysis: randomization inference over the locked assignment
  ensemble as primary, with block-clustered summaries reported alongside;
  if only one assignment is ever realized, the claim is explicitly
  assignment-conditioned (Sol M3).
- ACTIVE and YOKED remain paired by target instance; RANDOM-STATIC is
  **retained** (it separates transplantable active geometry from any
  geometry) and draws from the same candidate pool.

**Easy-label defense (Sol M2):** realized answer entropy and label balance
are mediators, reported as diagnostics, never matched and never success
criteria; the endpoint is scored only on the fixed escrowed panel balanced
over YES/NO, word length, relation type, family, and presentation strata
(also Opus m-5: the evaluation set is locked and arm-independent).

**Total L1 → L2 contact-mode map (no post-outcome discretion, Opus M-13).**
Committed before the L1 outcome; margins from N6; each cell names exactly
one mode:

| L1 result (locked comparisons) | L2 contact mode |
|---|---|
| ACTIVE superior to YOKED | `ACTIVE` |
| ACTIVE ≈ YOKED, and YOKED superior to RANDOM-STATIC | `YOKED-GEOMETRY` (transplanted active geometry; donor machinery reused) |
| ACTIVE ≈ YOKED ≈ RANDOM-STATIC | `RANDOM-STATIC` |
| ACTIVE inferior to YOKED | `YOKED-GEOMETRY` if YOKED superior to RANDOM-STATIC, else `RANDOM-STATIC` (deterministic sub-rule; the anomaly is reported) |
| any comparison unresolved / L1 `INSUFFICIENT` or invalid | **Level 2 blocked** — no default mode exists |

**Acquisition rule — closed before any comparative scout (Opus M-4; mandate):**

- Candidate pool: the declared enumeration of admissible `(u, v)` pairs from
  the locked grammar — the *same* pool RANDOM-STATIC samples.
- Uncertainty scalar: one locked definition; freeze candidate =
  `|P̂(equal) − ½|` from the learner's calibrated EQ head, minimized
  (maximum uncertainty). Final form is a pre-scout freeze item (S-gate),
  not tunable after any comparison.
- Deterministic tie-break: lowest index in the locked pool enumeration under
  a seeded, committed order.
- Duplicate/repeat rule: repeats permitted, cost 1 each, same oracle bit, no
  silent deduplication; the learner may deduplicate only as an explicit
  behavior available identically to all arms.
- Exhaustion: pool size is required ≫ B by construction (declared at
  freeze); exhaustion is therefore unreachable and, if reached, is a
  design-invalid event, not a learner choice.
- Fixed B for every arm.
- **Fail-closed gate:** the acquisition scorer receives learner state only —
  a mechanical import/dataflow proof that no oracle truth, no evaluator
  state, and no escrow content is reachable from the scorer (Level 0
  fail-closed discipline reused).

## 4. World status (closes Opus M-7..M-10, m-7; Sol M5; mandate §4)

**The full world contract is not frozen.** v1's "freeze candidate" language
is withdrawn. Status by layer:

**(a) Level 1 freeze candidate — cyclic algebra only.** Hidden `Z/n`:
states {0,…,n−1}, anonymous (never exposed); origin 0; `R: x ↦ x+1 (mod n)`,
`L: x ↦ x−1 (mod n)`, so `L = R⁻¹` on this rung; word evaluation = left
fold from origin; `EQ(u, v)` true iff net displacement of u ≡ net
displacement of v (mod n). Grammar: words over `{R, L}` to a declared cap
(N2). Forbidden truth: n, state labels, the relation set, any channel but
EQ bits. First-hand criterion as in §1. Evaluator: the balanced, escrowed,
arm-independent panel of §3. Leakage gates (all three retained from v1):
shuffled-answer null, parameter-shift control, probe-from-encoding.

**(b) Level 2 shared ontology — reframed (Opus M-7).** The invariant object
across all rungs is a **finite deterministic generator-labelled transition
system (automaton) on an anonymous state set**; groups are special strata.
This covers, without mid-stream ontology change: cyclic `Z/n`; **non-coprime
products** (`Z/n × Z/m`, gcd(n,m) > 1 — the genuinely new abelian family,
e.g. non-cyclic `Z/2 × Z/2`); dihedral `D_n` (generators r, s; relations
rⁿ = e, s² = e, srs = r⁻¹; inverses declared); broken-relation worlds
(sticky L: `L ≠ R⁻¹` on a declared defect set — still a deterministic
automaton, no longer a group). Per retained rung, the contract specifies
generators, relations/inverses, and the word→state evaluation table.
**Coprime `Z/n × Z/m` is reclassified** (Opus M-8): by CRT it is ≅ `Z/nm`,
so it is a presentation/control case on the C3 axis, never a C2 "unseen
family."

**(c) Cayley C3 contract — `DIRECTION_NOT_FROZEN`.** It remains a direction,
not a freeze, until it specifies: **volatile per-episode anonymized vertex
IDs** (equality must not be free off stable IDs); **matched interface
information rate** — proof by enumeration that word/EQ and vertex/edge
interfaces carry matched bits-per-query about the hidden object (Opus M-9);
a **frozen modality adapter** supplied identically to scratch and transfer
arms and trained without escrow answers (Sol M5 — otherwise the adapter is
the real treatment); enumeration verification of the semantic bijection;
and both presentation anchors — renamed-token (R4) and **native-Cayley
competence** (a from-scratch Cayley learner must succeed, else a C3 null is
modality migration, not structure — Opus M-10). **What may be implemented
now without pretending C3 is closed:** the automaton substrate, world
sampler, EQ oracle core, transcript/ledger machinery, and the enumeration
checker — all common to both presentations and to every C3 resolution.

## 5. Scout, escrow, and branching discipline (closes Sol M1, Y2; Opus X5, m-6; mandate §5)

**Scout route — chosen and named:** a **development-family comparative
calibration scout**, explicitly non-outcome and non-citable, under these
conditions: the acquisition rule, endpoint, censoring rule, and analysis
plan are frozen *first* (S-gate of §3); the development family is disjoint
from every escrow stratum; arm comparisons on development data inform
**only** N3/N4 precision logic; no threshold, policy, endpoint, or rule may
change after any comparative number is seen (any such change voids the
scout and reopens the S-gate). Chosen over feasibility-only because a
marginal scout cannot estimate paired-contrast variance at all (Sol M1) and
a conservative precision rule alone risks an unlockable N3; the dev-contrast
scout yields an honest paired-variance basis while staying uncitable.
Alternative preserved as a signature option (S5).

**Units and N-rules (no effect sizes invented):** experimental and variance
unit = target world block (L1) / unseen family-sequence-presentation bundle
(L2); seeds = repeated measures; checkpoints = time observations; query rows
= never units; donor assignments = dependency structure represented in the
analysis. N3 (L1 blocks) and N4 (L2 blocks) are set at lock by a precision
rule on the scout-estimated contrast variability (minimum block counts,
maximum acceptable censoring, minimum assignment-ensemble size for stable
randomization inference, resource ceilings) — never described as powered by
an effect size unless one is predeclared independently. **N6** (equivalence
margins + interval/test rule) joins the unresolved list.

**Escrow (exact discipline, Opus m-6):** the generator spec and seed
commitment are bound inside the relevant level's prereg lock; generation
happens **once**, after that lock, in the named clean room; plaintext is
encrypted before any researcher access; ciphertext and a plaintext hash are
committed to the DAG before any outcome; a malformed single generation ends
the holdout (no regeneration); custody = Kirill plus one named clean room.
**The custodian is not chosen here.** The exact required decision: Kirill
names the clean room (Gemini / Grok / local llama.cpp) and the second key
holder in signature line S6.

**Branching order (unchanged from v1 except as amended):** signed
amendments (this document's §8) → S-gate freeze (acquisition rule +
endpoint) → dev-contrast scout → L1 lock (N3, N6-L1) → escrow → L1 run →
decision → contact mode fixed by the total map → L2 lock (N4, N6, Cayley
contract resolved or C3 descoped by signature) → escrow → L2 run → decision
→ 2.5 / 3 as in v1. Level 2 *implementation* proceeds in parallel now (R3);
Level 2 *execution* remains blocked on the L1 decision, and `INSUFFICIENT`
at L1 blocks it entirely.

**Roadmap/kill-matrix hygiene (Sol m1):** the Level 1 README, KILL_MATRIX
row, and ROADMAP still carry "equal answer entropy." A loud signed
amendment replaces them with the yoked estimand at S-gate time — before any
lock, so no file disagrees with the locked design.

## 6. Review findings — disposition table

Every X/Y finding, with its disposition in this revision:

| Finding | Disposition |
|---|---|
| Opus C-1 / Sol M4 (C4 conflation) | Adopted — §2 B/D-conditioned cascade |
| Opus C-2 (Proof label collision) | Adopted — §1 two layers + signature S1 |
| Opus C-3 / Sol C2 (stopping/censoring) | Adopted — §3 common B, no early stop, blind evaluator, full-B donors |
| Opus M-1 (sign) | Adopted — §3 RMST estimand, positive = ACTIVE better |
| Opus M-2 / Sol C1, M3 (derangement coupling) | Adopted — independent-donor design; randomization inference; assignment-conditioned fallback |
| Opus M-3 (stratum matching) | Adopted — exact strata in §3 |
| Opus M-4 (acquisition rule) | Adopted — §3 closure list + fail-closed scorer gate |
| Opus M-5 / Sol m4 (D-arm meaning) | Adopted — D = inherited-example control; `BOUNDARY_INHERITED_LEDGER` on clause 1 |
| Opus M-6 (first-hand criterion) | Adopted — §1 positive definition + contact-mode scope |
| Opus M-7 (ontology) | Adopted — §4(b) automaton reframe |
| Opus M-8 (coprime CRT) | Adopted — reclassified to C3 axis; non-coprime products for new family |
| Opus M-9, M-10 / Sol M5 (Cayley) | Adopted — §4(c) `DIRECTION_NOT_FROZEN` with the five closure conditions |
| Opus M-11 (budget matching) | Adopted — §2 budget statement; v1's "identical contact" withdrawn |
| Opus M-12 (false-ledger validity) | Adopted — indistinguishability validation pre-L2 lock |
| Opus M-13 (total contact map) | Adopted — §3 table, `INSUFFICIENT` blocks L2 |
| Opus m-1..m-7 | Adopted (m-1 rewording; m-2 → N6; m-3 → `BOUNDARY_REDUNDANT_MEMORY`; m-4 → C−E decisive; m-5 → arm-independent panel; m-6 → §5 escrow; m-7 → per-rung tables) |
| Sol C3 (endpoint) | Adopted — right-censored budget-to-certified-solve; order probes secondary |
| Sol M1 (scout) | Adopted — named dev-contrast route, alternative preserved for signature |
| Sol M2 (easy-label) | Adopted — balanced escrow panel; mediators reported, never matched |
| Sol M6 (equivalence semantics) | Adopted — superiority for positives; margin-locked equivalence only for boundaries; UNKNOWN neither |
| Sol m2 (semantic difficulty) | Adopted — reported mediator + stratification variable, not assumed matched |
| Sol m3 (repeats) | Adopted — §3 deterministic cost/information rule |
| Sol Y6 literature | Retained as design constraints pointing at primary papers already in `LITERATURE_MAP.md` (Settles 2009; Cohn–Atlas–Ladner 1994; Kaplan–Meier 1958; Cox 1972; Schuirmann TOST); Sol's chat-level secondary/Wikipedia shortcuts are **not** promoted into the evidence map — each such item stays a design recommendation until a primary source is cited |

Nothing in either review was rejected. One item was resolved against a
governing text rather than a review: the essay-§VII/C6 contradiction, named
in the preamble and routed to signature S1.

## 7. Gate ledger (what closes where — supersedes v1 §9/§10 sequencing)

| Gate | Must be closed |
|---|---|
| Now, parallel | L1 cyclic-algebra core implementation; five-arm harness skeleton; automaton substrate + enumeration checker; escrow machinery |
| **S-gate** (before any comparative scout) | acquisition rule (pool, scalar, tie-break, repeats, exhaustion, fixed B, no-oracle-in-scorer proof); endpoint + sign + censoring; analysis plan; roadmap/README/kill-matrix amendment (Sol m1) |
| Before **L1 lock** | N3 + N6-L1 from scout precision logic; donor-assignment scheme + inference plan; arm-independent balanced panel; invalidity gates; first-hand criterion; total contact-mode map |
| Before **L1 outcome** | escrow generated post-lock per §5; leakage nulls green on development |
| Before **L2 lock** | contact mode from L1; N4 + N6; Cayley contract closed per §4(c) **or C3 descoped by signature**; false-ledger indistinguishability; compute/replay neutralization; per-rung grammar tables |
| Before **essay conclusion** | signed decision per §2 cascade; scope annotations (contact mode, C5/C1 status, C6 annotation) |

## 8. Kirill decision packet — seven atomic signature lines

1. **S1 — Two-layer proof and essay binding.**
   `I_ACCEPT_TWO_LAYER_PROOF` — `PROOF_CORE` = C2∧C3∧C4;
   `PROOF_STRONG` = core ∧ C1 ∧ C5 (the essay's Proof, preserved); the
   essay's unqualified "Proof" = `PROOF_STRONG`; C6 is an annotation, never
   a conjunct (resolves the named §VII contradiction).
   *Alternative:* `I_AMEND_ESSAY_PROOF_TO_CORE` (weakens the essay; not
   recommended).
2. **S2 — Repaired verdict cascade.**
   `I_ACCEPT_REPAIRED_C4_CASCADE` — §2's exclusive order, B/D-conditioned
   C4 layer, N6 margins at lock, `INSUFFICIENT` on any unresolved cell.
   *Alternative:* a named alternative cascade, in writing, before any lock.
3. **S3 — Level 1 endpoint.**
   `I_ACCEPT_L1_ENDPOINT_CENSORED_BTCS` — right-censored
   budget-to-certified-solve within common budget B, RMST estimand,
   balanced escrowed panel, order probes secondary.
   *Alternative:* `I_SELECT_ACCURACY_AT_B` (fixed-budget accuracy; simpler,
   loses the essay's budget-to-truth language).
4. **S4 — Donor construction.**
   `I_ACCEPT_INDEPENDENT_DONOR_YOKE` — disjoint donor worlds, stratum-exact
   one-to-one assignment, full-B hash-committed donor transcripts,
   randomization/cluster inference, RANDOM-STATIC retained.
   *Alternative:* `I_SELECT_DERANGEMENT_CONDITIONED` (one derangement,
   claim explicitly conditioned on it; weaker inference, fewer runs).
5. **S5 — Scout route.**
   `I_ACCEPT_DEV_CONTRAST_SCOUT` — frozen-first, non-citable, development-
   family comparative calibration; N3/N4 by precision logic only.
   *Alternative:* `I_SELECT_FEASIBILITY_ONLY_SCOUT` (marginal scout +
   conservative precision rule; risks an unlockable N3).
6. **S6 — Escrow custody.**
   `I_NAME_ESCROW_CUSTODIAN_<CLEAN_ROOM>` — name the generating clean room
   (Gemini / Grok / local llama.cpp) and the second key holder; custody =
   Kirill + that room; single malformed generation ends the holdout.
   (Required naming; not chosen for you.)
7. **S7 — Total contact-mode map.**
   `I_ACCEPT_TOTAL_CONTACT_MODE_MAP` — §3's deterministic L1→L2 table,
   including the anomaly sub-rule and `INSUFFICIENT` blocking Level 2.
   *Alternative:* a named replacement table, committed before the L1
   outcome.

---

**Unresolved numerics (updated):** N1 sampler range; N2 word-length cap;
N3 L1 block count (post-scout precision rule); N4 L2 block count; N5
resampled-path divergence threshold (pre-2.5); **N6 equivalence margins and
interval/test rule (new)**; plus the S-gate freeze items (persistence
cadence, calibration bounds, panel sizes). **Blocker types:** no source
blockers; S1–S7 are scientific signatures; the Cayley closure conditions
are scientific design; harness reuse and substrate implementation are
implementation choices; scout sizing and the cut order (v1 §10, unchanged
except RANDOM-STATIC moves above curriculum depth per Opus Q7 — it is
never cut while C1 is live) are resource choices.

*v1 named two places where my own map would have broken under an outcome.
The reviews found four more — the C4 conflation, the Proof-label collision,
the stopping/variance triple, and the unmatched Cayley interface — and this
revision closes them the same way: before any number exists that could
exploit them. The graph is now closed for signature; the rock has not
moved.*
