# Opus 4.8 X-line review — Philosophia Levels 1–3 claim graph

Reviewer: Opus 4.8 (X-line, adversarial constructive). Target: Fable 5's
`reviews/fable_levels1_3_claim_graph.md` (uncommitted, verdict `REVISE_PROGRAMME`).
Stage: pre-outcome. This review creates no code, no lock, no scout, no escrow,
no numeric threshold, and fills no outcome slot. It does not predict any
outcome. Every number below is marked UNRESOLVED and pushed to a signed lock.

---

## Verdict

**`REVISE_CLAIM_GRAPH`**

Fable's two self-corrections are correct and load-bearing, and the overall
direction is the right one. R1 (demoting `active ≤ static` from programme-kill
to a contact-choice boundary) is logically sound. R2 (replacing entropy-matching
with a yoked transplant) is the right *direction* and is salvageable. R4 and R5
are sound. But the document is **not yet closed enough to sign the truth table or
open a bounded Level 1 lock**, for four reasons that each change an estimand, a
verdict, or an interpretation *after* outcome — exactly the class the objective
says to reject:

1. **The `PROOF_BOUNDED = C2 ∧ C3 ∧ C4` label collides with the essay's own
   stated "Proof."** The author-approved essay (commit `90256ee`, §VII) defines
   Proof as the five-way conjunction *including* active contact and path credit.
   Fable's three-way conjunction is more defensible science, but it silently
   redefines the word "Proof" the essay already published. This cannot be
   adopted silently; it needs a signed essay amendment and a label that cannot
   equivocate. (X1)

2. **The `FALSIFIED_AT_C4` row wrongly withdraws C2.** `E ≈ C` (false ledger
   works as well as true) does *not* by itself falsify forward shortening. When
   weights alone also reach C (`B ≈ C > A`), forward shortening is real and
   weight-borne; only *traceability* fails. The table's evaluation order checks
   C4 before consulting B and will therefore mislabel a legitimate
   `BOUNDARY_WEIGHTS_ONLY` as a falsification. (X1)

3. **The yoked estimand has an unresolved stopping/sign/variance triple.** Sign
   convention contradicts itself (`ACTIVE > YOKED` vs a budget-to-truth
   difference that is *negative* when active wins); budget-to-truth with a
   variable stop is in direct tension with transplanting a fixed sequence; and
   `YOKED(i)` consuming `ACTIVE(σ(i))` couples the paired differences around
   derangement cycles, so ordinary within-instance paired inference is invalid.
   All three are fixable, but none is fixed. (X2)

4. **The cross-presentation (Cayley) contract is a direction, not a freeze
   candidate.** Vertex-ID volatility is unspecified; stable IDs make equality
   free and make budget-to-truth incomparable across interfaces; and no
   native-Cayley competence control exists, so a C3 null cannot separate
   structural failure from modality migration. The *Level-1 algebraic core* is
   nearly freezable; the C3 sub-contract is not. (X3)

None of these is a reject-identifiability wall (yoking is repairable) or a total
world block (Level 1 can proceed on the cyclic-algebra core). They are precisely
the ambiguities that would let an outcome be re-read after the fact. Fix them by
signed amendment and the programme is ready for a bounded Level 1 lock.

---

## Findings, ordered

### Critical (must close before any signature on the truth table)

- **C-1 — `FALSIFIED_AT_C4` conflates traceability failure with C2 falsification.**
  §4 row `any + + −(E≈C) · → FALSIFIED_AT_C4` withdraws C2's positive reading on
  `E ≈ C` alone, without consulting B. If `B ≈ C > A`, forward shortening is
  established through weights and C2 stands; the correct verdict is
  `BOUNDARY_WEIGHTS_ONLY` with an inert/untraceable ledger. `E ≈ C` is a genuine
  falsification of the *experience* reading only in the sub-case where no
  content-bearing channel reaches C without a ledger — i.e. `E ≈ C > A` **and**
  `B ≈ A` **and** `D ≈ A` (benefit rides on ledger *form*, truth irrelevant: the
  KILL_MATRIX "false ledger carries the effect"). The table must split the row on
  B before it can fire either verdict.

- **C-2 — `PROOF_BOUNDED` label ≠ the essay's "Proof."** The essay's §VII "Proof"
  is the five-conjunct claim; Fable's `PROOF_BOUNDED` is `C2 ∧ C3 ∧ C4`. The
  demotion of C1 and C5 to coordinates is scientifically better, but the shared
  word is a post-outcome equivocation hazard: a `C2∧C3∧C4` pass could be narrated
  in the essay's louder "Proof" voice. Either rename (e.g. `PROOF_CORE`) or bind
  by signed amendment that the essay's Proof section is rewritten to the
  three-conjunct meaning, and forbid the word "manufactured experience" in the
  path-bundle (P-axis) sense unless C5 is positive.

- **C-3 — Yoked stopping/censoring is unresolved and interacts with Q6.**
  Budget-to-truth with early stopping cannot coexist with transplanting a
  fixed-length query sequence: either ACTIVE continues past truth (post-solve
  acquisition degenerates as its uncertainty collapses, and YOKED inherits that
  degenerate geometry), or ACTIVE stops and YOKED receives a transcript whose
  *length and content are a function of its donor's solve time* — outcome-
  dependent truncation, the thing the Fable prompt forbids. This makes Q6 not a
  free endpoint choice: fixed-budget held-out accuracy (Q6-b) removes the
  censoring entirely; budget-to-truth (Q6-a) is only salvageable as a first-
  hitting-time inside a fixed common budget K with a pre-specified, non-degenerate
  continuation policy.

### Major (must close before the Level 1 lock / Level 2 lock as marked)

- **M-1 — Sign convention is internally contradictory (pre-L1 lock).** `Δ_choice =
  BTT(ACTIVE) − BTT(YOKED)` is *negative* when active wins (lower budget is
  better), yet §6 reads "ACTIVE > YOKED: C1 earned." Define a single
  `BENEFIT_i = BTT(YOKED_i) − BTT(ACTIVE_i)` (positive = active better) for
  endpoint (a), or the accuracy analogue for (b), and pin the one-sided
  direction. This is unlockable until Q6 fixes endpoint polarity.

- **M-2 — Derangement coupling invalidates naive paired inference (pre-L1 lock).**
  `ACTIVE(σ(i))` enters both `D_i` (as YOKED's queries) and `D_{σ(i)}` (as
  ACTIVE's own value), so `{D_i}` are correlated along σ's cycles; a paired
  t-test assuming i.i.d. differences will misestimate variance. Smallest repair:
  either **donor separation** (ACTIVE-evaluated instances disjoint from
  YOKED-donor instances, restoring independent `D_i`) or **randomization
  inference over σ** as the primary test (exact regardless of coupling, and it
  matches the "re-derive YOKED from committed ACTIVE + σ" audit story). A single
  fixed σ is adequate for a point estimate but not for honest variance. Y-line
  should co-sign.

- **M-3 — Derangement must be stratum-respecting, and the matching level fixes
  the licensed claim (pre-L1 lock).** If σ can map across strata (a `Z/n` donor
  onto a `D_m` recipient), YOKED gets a priori invalid geometry and ACTIVE wins
  by mismatch, not by coupling. Global-multiset matching licenses only "this
  sequence beats a random other sequence"; **per-stratum within-derangement**
  licenses the intended C1 ("adapted-to-this-instance beats adapted-to-a-sibling").
  Lock σ as a within-stratum derangement with strata defined finely enough
  (matched group order, generator-set size, word-length regime) that any donor's
  geometry is valid on its recipient.

- **M-4 — Acquisition rule is underspecified; several sub-items are pre-*scout*
  blockers.** "Maximum predicted disagreement over the declared grammar" does not
  fix: the candidate pool (which `(u,v)` per step, and it must equal the pool
  RANDOM-STATIC draws from); the uncertainty scalar (`|P(equal) − ½|`? ensemble
  disagreement? — one locked definition); deterministic seeded tie-breaking;
  duplicate handling; budget-exhaustion (fixed K); and the hard invalidity gate
  that **the scorer sees only learner state, never oracle truth**. These must be
  frozen before the variance scout, because the scout must use the locked rule.

- **M-5 — `BOUNDARY_LEDGER_SUFFICIENT` is a boundary *on clause 1*, not a free
  coordinate (pre-L2 lock / interpretation).** `D` is a *fresh* learner reading a
  ledger it did not produce — i.e. an inherited *report* of another run's contact,
  which is precisely the second-hand experience the essay's opening defines the
  programme against ("It inherits our report of contact"). `D ≈ C > A` therefore
  shows the manufactured experience is *transmissible as a document*, collapsing
  the first-hand/inherited distinction. It remains publishable, but it is a
  boundary on the primacy of the experience, and `D` must be reframed as the
  **inherited-example control**: `D > A` alone is not programme evidence, and
  `D ≈ C` is closer to a first-handedness falsification than a neutral coordinate.

- **M-6 — First-hand contact needs a positive operational definition (pre-L1
  lock).** R1 relocates clause 1 onto "first-hand static contact," but if C1 is
  negative and Level 2 runs on RANDOM-STATIC contact, clause 1 is then carried by
  a fixed query design — the very "static corpus" the essay contrasts against.
  The contract must state, as a clause-1 criterion, what makes RANDOM-STATIC
  contact first-hand (learner issues its own oracle queries against its own
  world; no pre-solved examples or externally authored solution traces enter),
  and the verdict must be **scope-annotated by contact mode**
  (`PROOF_BOUNDED[contact=RANDOM]` is a weaker claim than `[contact=ACTIVE]`).

- **M-7 — Ontology changes midstream; reframe at the automaton/monoid level
  (pre-L2 lock).** The contract says "hidden object = finite abelian groups" then
  includes dihedral `D_n` (non-abelian) and broken-axiom systems (`L ≠ R⁻¹`,
  possibly not a group). The invariant object across all rungs is *a finite
  transformation monoid / automaton on an anonymous state set with named
  generators*; groups are the special case. Reframe there so the EQ semantics and
  the semantics-preservation theorem hold uniformly, honoring the Fable prompt's
  own "no ontology change midstream."

- **M-8 — Coprime `Z/n × Z/m` is abstractly cyclic; it is a presentation change,
  not a new family (pre-L2 lock).** By CRT, `gcd(n,m)=1 ⇒ Z/n × Z/m ≅ Z/nm`. Used
  as a C2 "unseen family," it conflates C2 (new structure) with C3 (re-presentation
  of known structure). If a genuinely new abelian family is wanted, use
  **non-coprime** products (`Z/2 × Z/2`, etc.); if the coprime product is kept, it
  belongs on the C3 axis and must be labelled so.

- **M-9 — Cayley interface information rate is unmatched and unproven (pre-L2 lock
  / C3 identifiability).** Semantic bijection is necessary but not sufficient
  (Fable says this; the prompt insists on it). Stable vertex IDs make "same-vertex?"
  free (read equality off IDs) and let a learner brute-force the graph at a
  *different cost* than the EQ-on-words interface — so cross-presentation
  budget-to-truth is confounded by intrinsic interface information rate, not
  transferred structure. Specify **ID volatility** (freshly anonymized per
  episode/query) and prove, by enumeration, that the two interfaces carry matched
  bits-per-query about the hidden object. Until then C3 is not identifiable.

- **M-10 — C3 conflates structural transfer with modality migration (pre-L2
  lock).** Moving one learner from a token/word interface to a graph interface may
  demand an adapter/new embedding; a C3 null could then be an architecture-
  migration artifact, not a structural wall. Add a **native-Cayley competence
  control** (a learner trained from scratch on the Cayley interface must succeed),
  as the graph-side analogue of the renamed-token positive anchor. A C3 null is
  uninterpretable without it.

- **M-11 — Five-arm budget matching is incomplete (pre-L2 lock).** Arms are
  matched on new-family oracle access, but not visibly on **total optimization
  budget**: if C/D replay a stored ledger and A cannot, C/D receive extra
  gradient steps — a compute confound masquerading as experience (the standard
  replay/EWC artifact). Match total optimization budget across arms (A replays its
  own fresh data, or replay is compute-neutralized). Also: "all arms use identical
  contact" is false in the relevant sense — D and E consume inherited/corrupted
  *records*; reword to "identical new-family access; deliberately varied
  retained-history provenance."

- **M-12 — False-ledger placebo (E) is only valid if formally indistinguishable
  (pre-L2 lock).** If the corruption is coarse, the learner gates the ledger out
  and `E ≈ B` vacuously — testing "learner ignores obvious noise," not
  traceability. Before E can serve as a placebo, validate that a discriminator
  cannot separate true from false ledgers by *form* (matched token/length/
  surprise-rate statistics), and specify the corruption mechanism (within-world
  answer shuffle vs cross-world substitution changes what E controls).

- **M-13 — L1→L2 contact-mode map is not a total function (pre-L1 outcome).** §6's
  middle reading ("YOKED geometry *or* RANDOM-STATIC") leaves post-outcome
  discretion — a meaning-drift vector. Lock the map so every L1 result
  deterministically fixes exactly one L2 contact mode, committed before the L1
  outcome.

### Minor (clarify before lock; not blocking the direction)

- **m-1 — "Generated before outcome" is imprecise for YOKED.** YOKED is generated
  before the *YOKED* outcome but is a deterministic function of *ACTIVE* outcomes.
  Reword to "pre-specified deterministic function of committed (hashed) ACTIVE
  transcripts and a locked σ," and require σ + derivation rule locked *before*
  ACTIVE runs, ACTIVE transcripts hash-committed before YOKED is derived.

- **m-2 — Equivalence margins are undefined and unlisted.** Every `≈` in §4
  (`E ≈ C`, `B ≈ C`, `D ≈ C`, `ACTIVE ≈ YOKED`) is an equivalence claim requiring
  a pre-registered margin (TOST-style). None appears in the UNRESOLVED-N list. Add
  `N6 — equivalence margins`; without them the proof/boundary line is chosen
  post-outcome by picking a margin.

- **m-3 — Non-exclusive boundary rows.** If both `B ≈ C > A` and `D ≈ C > A`
  hold, rows for `BOUNDARY_WEIGHTS_ONLY` and `BOUNDARY_LEDGER_SUFFICIENT` both
  fire. Add a joint cell / tie-break (both channels independently sufficient →
  `BOUNDARY_REDUNDANT_MEMORY`).

- **m-4 — Traceability estimand can be stated cleanly.** Prefer the content
  contrast `C − E` (both weighted, differ only in ledger truth) as the C4 estimand,
  with `E − B` reported separately as the *ledger-form/scaffolding* diagnostic,
  rather than folding both into "`E ≤ B`."

- **m-5 — Arm-independent evaluation set (pre-L1 lock).** Answer balance is a
  legitimate mediator (Fable is right) *only* if the endpoint is scored on a
  locked, arm-independent held-out set; if eval composition depends on the arm's
  own queries it becomes the easy-label route. State the eval-set independence
  explicitly.

- **m-6 — Escrow gating and hash binding.** Make explicit that escrow generation
  is gated on the *relevant level's* prereg lock (not merely the contract freeze),
  the generator seed/spec is part of that lock, plaintext hash is committed to the
  DAG pre-outcome, custody is Kirill + one clean room, and a malformed single
  generation ends the holdout (essay precedent). Inherited from Line 12 but not
  restated in the document.

- **m-7 — `{R,L}`/`{S,T}` grammar lacks relations/inverses for the non-cyclic
  rungs.** Words over the tokens are not a presentation without declared
  generators, relations, inverses (is `L = R⁻¹` on every rung? no, on broken-axiom
  rungs), and a word→state evaluation. Specify per rung.

---

## Answers to the required attacks

### X1 — Claim graph and verdict semantics

- **Is R1 correct?** Yes. Clause 1 as written ("earned through declared contact
  rather than inherited examples") is about *first-hand vs inherited*, not about
  *choice*. `ACTIVE ≤ YOKED` kills only "choice of contact matters"; first-hand
  static contact can still satisfy clause 1, and C2–C5 route through Level 2's
  first-hand arms. The old roadmap did overstate Level 1's logical role. **Caveat
  (M-6):** the "first-hand" property carrying clause 1 has no positive definition
  yet; if C1 fails and Level 2 runs on RANDOM-STATIC, clause 1 rests on a fixed
  query design that is uncomfortably close to the "static corpus" the essay
  defines the programme against. R1 is correct *conditional on* adding a checkable
  first-hand criterion and scope-annotating the verdict by contact mode.

- **Does `PROOF_BOUNDED = C2 ∧ C3 ∧ C4` match the five-clause programme?** It
  matches the *necessary core* (clause 3 → C2, clause 4 → C3, clauses 2 and the
  false-ledger part of clause 5 → C4). It **demotes** clause 1 (first-hand,
  enforced only by the leakage gate, not a node) and the destination-credit /
  correlated-copies part of clause 5 (→ C5, "mechanism strength only"). Relative
  to the *programme question* this is a defensible narrowing; relative to the
  *essay's own §VII "Proof"* (five conjuncts, explicitly naming active contact and
  path credit) it is a **redefinition of a published word** and must not be
  silent (C-2). Net: the conjunction is sound science; the *label* silently weakens
  the essay's strong claim and needs a signed rename or essay amendment.

- **Are the falsification/boundary verdicts mutually exclusive and exhaustive?**
  Not yet. (i) `FALSIFIED_AT_C4` and `BOUNDARY_WEIGHTS_ONLY` are separated only by
  the "E clean" qualifier, and the C4-before-B evaluation order mislabels the
  `E ≈ C ∧ B ≈ C` case as falsification when forward shortening is genuinely
  weight-borne (C-1). (ii) `BOUNDARY_WEIGHTS_ONLY` and `BOUNDARY_LEDGER_SUFFICIENT`
  can co-fire (m-3). (iii) Every `≈` needs a pre-registered equivalence margin or
  the partition is not decidable (m-2). (iv) A decided `C2 ∧ C3` with UNKNOWN C4
  routes to `INSUFFICIENT` — correct, but state it. Fix these and the partition
  becomes exclusive/exhaustive.

- **Does an E-arm result comparable to C invalidate C2 itself?** No — not by
  itself. `E ≈ C` invalidates the *truthful-ledger interpretation* (C4/
  traceability). It invalidates C2-as-manufactured-experience **only** in the
  configuration where the effect exists solely through the ledger *form*
  (`E ≈ C > A`, `B ≈ A`, `D ≈ A`): a false ledger reproducing the benefit means
  the "experience" is a format placebo. When `B ≈ C > A`, `E ≈ C` leaves C2
  standing as weight-borne forward shortening and the verdict is
  `BOUNDARY_WEIGHTS_ONLY`. The table currently gets this wrong (C-1).

- **Are `BOUNDARY_WEIGHTS_ONLY` and `BOUNDARY_LEDGER_SUFFICIENT` compatible with
  the first-hand clause?** `BOUNDARY_WEIGHTS_ONLY`: **yes** — the weights were
  formed by first-hand contact in the source families. `BOUNDARY_LEDGER_SUFFICIENT`:
  **no, in tension** — `D` is a fresh learner consuming a record it did not
  produce, i.e. inherited-report contact; that boundary is *on* clause 1, not
  beside it (M-5). It is publishable but must be labelled as the collapse of the
  first-hand/inherited distinction, not as a neutral bonus coordinate.

### X2 — Yoked-transplant identifiability

**Estimand (restated so the sign is unambiguous).** For endpoint (a),
`BENEFIT_i = BTT(YOKED_i) − BTT(ACTIVE_i)`, positive when adaptive coupling
lowers budget-to-truth on instance *i*; target `E[BENEFIT] > 0`. Both arms are
evaluated against instance *i*'s own oracle and *i*'s locked, arm-independent
truth criterion; they differ only in whether the query sequence was adapted to
*i* (ACTIVE) or to `σ(i)` (YOKED). The construction *does* isolate instance-
adaptive coupling — but only after the following are repaired.

- **Sign (M-1):** contradictory as written; fix as above; blocked on Q6 polarity.
- **Stopping/censoring (C-3):** the dominant threat. Variable stopping cannot
  produce a fixed transplantable sequence without either post-solve acquisition
  degeneracy (ACTIVE's uncertainty collapses; YOKED inherits noise geometry) or
  donor-solve-time-dependent truncation (outcome-dependent matching, forbidden).
  Smallest repair: fix a common budget K for all arms, no early stop; prefer
  endpoint (b) accuracy-at-K (removes censoring); if (a) is kept, define BTT as
  first-hitting-time within K under a pre-specified, non-degenerate continuation
  policy.
- **Dependency / variance unit (M-2):** the true unit is *not* the instance under
  naive pairing, because `D_i` are coupled along σ's cycles. Use donor separation
  or randomization inference over σ; a single fixed σ gives a point estimate only.
- **Matching level (M-3):** must be per-stratum within-derangement; global-multiset
  matching licenses only the weakest claim; cross-stratum σ manufactures a trivial
  ACTIVE win.
- **Answer balance (m-5):** a *legitimate mediator* (Fable is right that it is
  downstream of the treatment and must not be matched) **provided** the endpoint
  is scored on a locked, arm-independent held-out set; otherwise it becomes the
  easy-label route.
- **"Generated before outcome" (m-1):** true only for the YOKED outcome; YOKED is
  a function of ACTIVE outcomes. Reword to "pre-specified deterministic function
  of committed ACTIVE transcripts and locked σ"; lock σ pre-ACTIVE; hash-commit
  ACTIVE transcripts before deriving YOKED.
- **Fixed derangement enough? (M-2):** for inference, no — resample σ
  (randomization) or donor-separate.
- **Acquisition-rule requirements (M-4):** pool, uncertainty scalar, tie-break,
  duplicates, budget exhaustion, and a hard no-oracle-in-scorer gate must all be
  frozen before the variance scout.

**Salvageable?** Yes. With C-3, M-1, M-2, M-3, M-4, m-1, m-5 closed, the yoked
transplant identifies the adaptive-coupling effect. This is why the verdict is
`REVISE_CLAIM_GRAPH`, not `REJECT_IDENTIFIABILITY`. No replacement experiment is
required; the smallest identifiable version is the repaired yoke plus the
RANDOM-STATIC third arm (which Fable already includes and which correctly
separates "good geometry" from "any geometry").

### X3 — World and cross-presentation contract

- Ontology creep is real (M-7): reframe on transformation-monoid/automaton-on-
  anonymous-states so groups, dihedral, and broken-axiom rungs share one EQ
  semantics.
- Coprime `Z/n × Z/m ≅ Z/nm` is a presentation change, not a new family (M-8):
  reclassify to the C3 axis, or switch to non-coprime products for a genuinely
  new abelian family.
- The `{R,L}`/`{S,T}` grammar is not yet a presentation for the non-cyclic rungs
  (m-7): declare generators, relations, inverses, and word→state evaluation per
  rung.
- The Cayley interface is the load-bearing gap (M-9): specify volatile
  (per-episode) anonymized vertex IDs and *prove by enumeration* that
  word/EQ and vertex/edge interfaces carry matched bits-per-query; otherwise C3's
  budget-to-truth comparison measures interface information rate, not transferred
  structure. Semantic bijection is necessary, not sufficient (agreed).
- Modality migration confound (M-10): add a native-Cayley competence control, the
  graph-side analogue of the renamed-token anchor; without it a C3 null cannot be
  read.

**Freeze status:** the **Level-1 cyclic-algebra core** (`Z/n`, word/EQ interface,
oracle cost 1, forbidden-truth list, fail-closed views, leakage nulls) is a
**freeze candidate** once M-6 (first-hand criterion) and m-7 (grammar) are added.
The **dihedral / broken-axiom rungs and the entire Cayley cross-presentation
contract are a direction, not a freeze** until M-7, M-8, M-9, M-10 are closed.
Because Level 2 execution is gated behind Level 1 anyway, this does not block
signing R1/R2's direction — but the document should stop calling the C3 contract
a freeze candidate.

### X4 — Level 2 five-arm interpretation

The 2×2 (weights × ledger) + false-ledger placebo skeleton is sound and no
smaller design has the same identifiability (dropping D loses ledger-sufficiency,
dropping E loses traceability, dropping B loses the channel split — Fable is
right). Indispensable contrasts: `C−A` (C2), `B−A` (weights), `D−A` (ledger-alone
/ inherited-example control), `C−B` (ledger beyond weights), `C−E` (ledger
*content*), `E−B` (ledger *form*). The decisive C4 estimand is the content
contrast `C−E` with `E−B` reported as the scaffolding diagnostic (m-4).

Confounds that must be closed (M-11, M-12, M-5): total optimization/replay budget
matching; a validated formally-indistinguishable false ledger; and the reframing
of D. Specifically **D (fresh + truthful ledger) is not a positive experience arm
— it is the inherited-example control.** A fresh learner reading a transcript of
solved queries is trained on inherited examples; `D > A` is the mundane
"inherited examples transfer" effect, the null the programme defines itself
against. Treat `D > A` accordingly and read `D ≈ C` as a first-handedness
boundary (M-5), not a bonus. "All arms use identical contact" is false as stated;
correct to "identical new-family access; deliberately varied retained-history
provenance."

### X5 — Lock order and negative space

- **Scout validity:** the non-outcome variance scout is good discipline
  (Line-12 scouts-never-cited), but it cannot run until the acquisition rule and
  endpoint (Q6) are frozen (M-4, C-3), and it must not be used to *choose* the
  rule or endpoint (Goodhart on the scout). Sequence: freeze rule+endpoint →
  scout → set N3 → lock.
- **Escrow order / hash binding (m-6):** make explicit — gated on the level's own
  prereg lock, generator seed in the lock, plaintext hash committed pre-outcome,
  custody Kirill + one clean room, single malformed generation ends the holdout.
- **Contact-mode branching (M-13):** the L1→L2 map must be a total function
  committed before the L1 outcome; and because a RANDOM-STATIC branch changes the
  scope of any eventual proof, the verdict must carry a contact-mode annotation
  (M-6).
- **"Level 2 largely specifiable pre-branch":** accepted — the five-arm structure,
  curriculum, escrow machinery, endpoints, and contrast algebra are orthogonal to
  how source contact was acquired and can be specified now; only the contact-mode
  parameter and the post-L1 N4 are downstream. This is the correct reading of R3.

**Gate ledger (what closes where):**

| Gate | Must be closed |
|---|---|
| Implementation (now, parallel) | L1 algebra core (Z/n, word/EQ, fail-closed views); five-arm harness skeleton; inherited escrow/encryption machinery |
| Before **scout** | acquisition rule fully specified (pool, uncertainty scalar, tie-break, no-dup, no-oracle-in-scorer); endpoint + sign (Q6); fixed K + continuation policy; development family disjoint from escrow |
| Before **L1 lock** | N3 from scout; σ scheme (stratum-respecting; donor-separation or randomization-inference plan); primary contrast + one-sided direction + equivalence margins (N6); arm-independent eval set; invalidity gates; first-hand criterion (M-6); total L1→L2 contact-mode map |
| Before **L1 outcome** | escrow generated post-lock, encrypted, hash-committed, custody set; leakage nulls green on development |
| Before **L2 lock** (post-L1) | contact mode from L1; N4 from post-L1 scout; Cayley contract (M-9, M-10) or C3 descoped; false-ledger indistinguishability (M-12); compute/replay budget matching (M-11); ontology reframe (M-7); coprime-product reclassification (M-8); per-rung grammar (m-7) |
| Before **essay conclusion** | signed decision per repaired truth table; scope annotations (contact mode; C5 status; C2-as-weights-vs-experience) |

---

## Smallest repairs (adopt by signed amendment)

1. **Truth table C4 layer:** replace the single `FALSIFIED_AT_C4` row with a
   B-conditioned split — `E ≈ C ∧ B ≈ C > A → BOUNDARY_WEIGHTS_ONLY` (untraceable
   ledger, C2 stands); `E ≈ C ∧ B ≈ A ∧ D ≈ A → FALSIFIED_AT_C4` (false-ledger
   placebo, C2's experience reading void). Add the joint `BOUNDARY_REDUNDANT_MEMORY`
   cell (m-3) and equivalence margins N6 (m-2).
2. **Rename** `PROOF_BOUNDED` → `PROOF_CORE` (or bind an essay §VII rewrite by
   signature), and forbid the P-axis "bundle of paths" wording unless C5+.
3. **Yoke:** fix common budget K, no early stop; resolve Q6 toward accuracy-at-K
   (or first-hitting-time-within-K with a pre-specified continuation policy);
   define `BENEFIT` with an explicit sign; make σ a locked within-stratum
   derangement; adopt donor-separation *or* randomization inference over σ; freeze
   the full acquisition rule with a no-oracle-in-scorer gate; reword "generated
   before outcome."
4. **World:** reframe ontology to automaton/monoid; reclassify coprime products;
   specify per-rung grammar; **downgrade the Cayley contract from freeze to
   direction** pending volatile IDs + information-rate proof + native-Cayley
   control.
5. **Level 2:** reframe D as the inherited-example control; match total
   optimization budget; validate false-ledger indistinguishability; state C4 as
   the `C−E` content contrast; scope-annotate the verdict by contact mode.

---

## Questions requiring Kirill's decision (load-bearing)

1. **Essay–label collision (C-2):** rename Fable's verdict to `PROOF_CORE` and
   keep the essay's five-conjunct "Proof" as the strong horizon, *or* amend the
   essay §VII to the three-conjunct meaning by signature? (One of these must
   happen before the truth table is committed.)
2. **Endpoint polarity (Q6, now coupled to X2):** accuracy-at-fixed-budget-K
   (removes the yoked censoring problem) or budget-to-truth as first-hitting-time
   within K (keeps the essay's "budget-to-truth" language but needs a
   continuation policy)? This fixes both levels' primary endpoint *and* the yoke's
   identifiability.
3. **Yoke inference (M-2):** donor-pool separation (extra ACTIVE runs, clean
   independence) or randomization inference over σ (no extra runs, exact test)?
4. **C3 scope:** require the full Cayley contract (volatile IDs +
   information-rate proof + native-Cayley control) before Level 2 lock, or descope
   C3 to `BOUNDARY_REPRESENTATION`-only for this line and defer true
   algebra→geometry transfer to a successor? (Affects whether C3 stays a Proof
   conjunct.)
5. **D-arm interpretation (M-5):** accept that `D > A` is the inherited-example
   control and `BOUNDARY_LEDGER_SUFFICIENT` is a boundary on clause 1
   (first-handedness), not a neutral coordinate?
6. **First-hand criterion (M-6):** approve a positive, checkable definition of
   first-hand contact and a contact-mode scope annotation on every verdict?
7. **Cut-order interaction:** §10 cuts RANDOM-STATIC before ACTIVE-vs-YOKED; but
   RANDOM-STATIC is what separates "good geometry" from "any geometry." Confirm
   the cut still preserves an interpretable C1, or move RANDOM-STATIC above
   curriculum depth in the cut order.

---

## Additions to the negative space (§11)

- A `PROOF_CORE` obtained on RANDOM-STATIC contact must never be narrated as
  actively/first-hand-earned; scope-annotate by contact mode.
- `D > A` (inherited ledger) is not programme evidence; D is the inherited-example
  control. `D ≈ C` is a first-handedness boundary, not a bonus.
- `E ≤ B` is not, by itself, traceability; only `C − E > 0` with a *validated
  indistinguishable* false ledger, and only after confirming a content-bearing
  channel (`B` or the interaction) does not already carry C2.
- Cross-presentation cost reduction is uninterpretable unless interface
  information rates are matched and a native-Cayley control passes; a C3 number on
  unmatched interfaces licenses nothing.
- `PROOF_CORE` (`C2 ∧ C3 ∧ C4`) is not the essay's five-conjunct Proof and must
  not be worded as proof of the path-bundle experience unless C5 is positive.

---

## What can be signed now vs. what is blocked

- **Sign now (amended):** R1 (with M-6's first-hand criterion and contact-mode
  scope), R4, R5. The *direction* of R2 (yoke replaces entropy-matching) and R3
  (parallel L2 implementation, gated execution).
- **Do not commit yet:** the §4 truth table (C-1, C-2, m-2, m-3), the yoked L1
  *design as lockable* (C-3, M-1..M-4), and the *freeze* status of the C3/Cayley
  contract (M-7..M-10).
- **Blocked until their gate:** L1 lock (pre-lock ledger above); L2 lock (Cayley,
  false-ledger, budget-matching, ontology); any essay conclusion (signed
  decision + scope).

The rock has not moved and Fable set the two right pitches as load-bearing. This
review adds four more that would otherwise break silently under an outcome — the
C2/C4 conflation, the Proof-label collision, the yoke's stopping/variance triple,
and the unmatched Cayley interface — and leaves them repairable by signed
amendment before any number exists to exploit them.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
