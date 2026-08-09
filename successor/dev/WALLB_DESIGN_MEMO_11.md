# WALLB_DESIGN_MEMO_11

NON-CITABLE design-selection memo. Dev world only. No code, no runs, no datum.
Written BEFORE any implementation, per `ascesis/IDEA_GATE.md`.

(Slot 10, `WALL_LOCALIZE`, was proposed after `GROKKING_PROBE_09` and declined:
it required a full retrain to answer a question that changed no decision. Not
built. This memo takes slot 11.)

Supersedes nothing. The walk-world branch is closed; see `GROKKING_PROBE_09.md`
and the essay status ledger.

---

## 1. Scope sentence (Wall B), fixed before design

> In this experiment, manufactured experience does not mean acquiring logically
> unavailable facts. It means constructing persistent, transferable structure
> that makes derivable facts reachable within a bounded budget.

Consequences, binding on every later claim:

- The estimand is a **cost** estimand, never an information estimand.
- Wall B holds only for **goals pre-selected to have a finite witness**. Goals
  are generated with their witness (see §4), so undecidability and independence
  never enter. Nothing here bears on incompleteness.
- No result from this cell may be worded as "the mind earned facts the world
  withheld". The admissible wording is "the mind built structure that made
  already-derivable facts affordable".

The walk world failed a different gate: there the manufacturable invariant was a
linear function of the move counts. Here the manufacturable object is a library
of derivations, closed under composition and not expressible as a count. §7
turns that from a hope into a pre-registered check.

## 2. Literature position

| work | what it establishes | what it leaves |
|---|---|---|
| Poesia et al., *Learning Formal Mathematics From Intrinsic Motivation* (arXiv:2407.00695) | a conjecturer/prover pair self-improves from axioms with no human data and transfers to held-out extrinsic theorems | no persistent library and no replay of one learner's conjecture curriculum into another learner state |
| *DreamProver* (arXiv:2604.26311) | wake-sleep abstraction of a persistent, transferable lemma library improves later proving | component and no-library ablations do not separate library content from coupling to the learner state that produced it |
| *Self-Supervised Theorem Discovery in a Formal Axiomatic System* (arXiv:2606.28747) | a persistent theorem library is grown from primitive rules and reused by the discoverer and by external LLMs | the with/without-prompt-lemmas comparison tests usefulness, not counterfactual ownership or curriculum coupling |
| Xu et al., *Model-Based Meta Automatic Curriculum Learning* (MM-ACL, CoLLAs 2023) | records one adaptive curriculum and replays it on five other random-seed student states; online adaptation outperforms the fixed replay with lower variance | this is the closest known state-coupling control, so the broad novelty claim is withdrawn; it is an RL diagnostic ablation, not a preregistered compute-matched formal experiment with an inspectable acquired object |
| Portelas et al., *Meta Automatic Curriculum Learning* / AGAIN (arXiv:2011.08463) | curricula distilled from earlier students can be useful priors for later students and then adapt to them | donor history can help rather than hurt; it is not a frozen donated-curriculum counterfactual |
| *LLM Library Learning Fails* (arXiv:2504.03048) and the compute-matched TroVE re-evaluation (arXiv:2507.22069) | apparent library/tool-reuse gains can vanish or shrink to a marginal non-significant gain once compute is equalized | two independent warnings that learner-only budget parity is insufficient |
| Chen & Li, *A Theoretical Framework for Self-Play Theorem Proving Algorithms* (arXiv:2606.01861) | on a well-connected theorem graph, a reversible-random-walk conjecturer can already drive exponential growth | ACTIVE must beat a strong random-walk curriculum, not merely a weak pre-fixed random list |
| Chiviacowsky & Wulf, self-controlled feedback with yoked controls (PMC4237043) | the yoked design isolates the effect of *choosing* from the content and frequency of what is received | never transplanted into formal-mathematics agents, as far as this scan reached |
| Knuth–Bendix completion (classical) | a standard algorithm that converts a presentation into a decision procedure where it succeeds | it is a **trivializer** for this cell and must be run as a baseline (§7) |

**The broad novelty claim is withdrawn.** State-coupled curriculum selection
versus replay of a curriculum generated for another student state has already
been run as an ACL diagnostic in MM-ACL, with a positive sign. The sign, the
general contrast and the claim that adaptation to student state can matter are
therefore not contributions of this cell.

**Claimed contribution: a narrower formal-mechanism contrast.** Self-conjecturing,
lemma libraries, learned proof guidance and state-coupled curricula are known
and are used here as substrate. What this scan did not find is a formal or
symbolic experiment that simultaneously:

1. freezes a conjecture curriculum generated by one learner and transplants it
   into a different learner state;
2. equalizes both learner work and the full curriculum-generation machinery;
3. exposes the acquired object (library and policy) to direct TRUE/FALSE/NONE
   intervention; and
4. measures whether that object shortens fixed future proof work, with the
   transplanted-curriculum contrast as the preregistered primary estimand.

### Manual ablation audit of the three closest formal works

The audit was performed on 2026-08-09 and read experiment and ablation sections
for the actual control, not for the word "yoked".

| work | locations read | ablations / controls actually run | curriculum replayed into another learner state? | acquired object and future-work test | result for this cell |
|---|---|---|---|---|---|
| Poesia et al. / MINIMO | §§4.1–4.2; Figs. 2–4; Appendix C | with vs without hindsight relabeling over five iterations and three seeds; fresh conjectures each iteration; held-out textbook/Natural Number Game evaluation | **No.** Seeds supply error bands; a conjecture sequence from one seed is not frozen and replayed to another | no growing theorem library; proof policy is evaluated on held-out human theorems | no donated-curriculum control |
| DreamProver | §§4.1–4.4; Table 3; Appendices A–C | full wake-sleep system; no iterative library optimization; no semantic clustering; no library; LEGO-style single-pass retrieval | **No.** The domain training theorem set is fixed, but no adaptive theorem/decomposition sequence is transplanted across learner states | explicit persistent lemma library; unseen-theorem reuse, proof length and output tokens are measured | useful mechanism ablations, but no state-coupling counterfactual and no matched whole-system yoke |
| Ota et al. | §§5.1–5.4; Figs. 4–6; Appendix A | library growth over six generations; benchmark coverage; external GPT proof search with vs without extracted prompt lemmas; no component-ablation section | **No.** Goals discovered by one policy are not replayed as the fixed curriculum of another policy/seed | theorem actions retain primitive proofs; external LLM use is tested, but discovery cost is not matched to a donated-library arm | usefulness and transfer are tested; ownership/coupling is not |

**Status of the novelty claim: NARROW GAP SURVIVES TARGETED SCAN, NOT AN
EXHAUSTIVE PRIORITY CLAIM.** The closest cross-state control is MM-ACL outside
formal mathematics. None of the three closest formal ablation sections contains
the four-part control above. This is sufficient to proceed to the desk audit of
the concrete equational world; it is not sufficient to claim that no formal
paper anywhere contains such a control in an appendix.

## 3. The unit of yoking, and the confound that decides the design

**The donated unit is a conjecture curriculum, never a proof trajectory.**
Donated proof steps depend on the donor's terms, its already-found lemmas and
its search state; on another world they may be inexecutable. The recipient
receives goals and runs its own search against its own verifier.

```text
ACTIVE  chooses conjectures C1, C2, C3, ... from its own state
YOKED   receives sigma(C1), sigma(C2), sigma(C3), ... in the same order
        and performs its own proof search, scored by its own verifier
```

**The confound (and it decides interpretability):** a
donated curriculum can be worse for the recipient for two entirely different
reasons.

- **(a) Feasibility mismatch** — the donated conjectures are simply harder or
  unprovable for me, so I prove fewer of them and end with a smaller library.
- **(b) Usefulness decoupling** — the donated conjectures are equally provable
  for me, but they are not the ones my current state needed next.

`YOKED-SEED` does **not** remove (a). Sharing a world matches logical truth, not
in-budget feasibility for a learner whose state has already diverged. The
primary contrast therefore estimates the **total effect of state coupling**:
feasibility matching, timing and usefulness together. Realized proved-fraction,
library growth and reuse are reported as mediators, but conditioning the primary
effect on them is forbidden. This cell cannot claim to isolate usefulness (b)
alone; that would require a later design that intervenes on feasibility without
conditioning on a post-treatment outcome.

**Two yoking arms bracket the scope of that total effect.**

- **YOKED-SEED** — donor is an ACTIVE learner with a different seed on the
  **same world**. `sigma` = identity. Logical validity and presentation are
  identical, while in-budget feasibility may differ because the learner states
  differ. This is the primary total-effect test. Donor and recipient states are
  correlated, so the contrast is conservative relative to a different-world
  transplant and a null is correspondingly local.
- **YOKED-WORLD** — donor is an ACTIVE learner on a **different presentation of
  the same family**, `sigma` a fixed bijection on the alphabet. Fully decoupled,
  but adds presentation transfer to the feasibility component.

Pre-registered reading: the primary claim rests on **YOKED-SEED**.
`YOKED-WORLD` is reported as the liberal bound, always alongside its realized
solved-fraction. No inferential contrast is adjusted for realized proved-count
or realized library size; both are post-treatment mediators.

**ACTIVE selection rule.** At curriculum position `r`, the witnessed-goal
generator emits a hash-ordered candidate batch of size `K` from a predeclared
witness-length stratum. The primitive witness and its length within the stratum
are hidden from every selector. Candidates directly closable by one current
macro are ineligible. ACTIVE chooses the lexicographic maximum of:

1. `connected(c,L)`: whether at least one current library macro applies to an
   endpoint of `c`;
2. `H_pi(c)`: mean normalized entropy of the current policy over legal
   **primitive** rewrites at both endpoints;
3. `novelty(c)`: minimum normalized edit distance from `c`'s ordered endpoint
   pair to an earlier curriculum pair; and
4. the negative canonical candidate hash (deterministic tie-break).

The selector may read only the raw endpoint strings and the learner's current
`L` and `pi`; it performs no proof search, verifier call or hidden-witness read.
At initialization the first two coordinates tie, so selection reduces to
novelty and the hash. `K`, the witness-length strata and their fixed schedule are
frozen by the desk audit using runtime and shortcut diagnostics only, never an
ACTIVE-vs-control outcome. A selector that cannot be implemented side-effect
free and hash-deterministically invalidates the cell.

`YOKED-SHUFFLED` is **deferred**: an arbitrary permutation breaks dependencies
(a lemma may need one not yet discovered). If it returns later, it must permute
only independent blocks, or use a different topological order of the same
dependency DAG.

## 4. The world family (concrete enough to implement)

**String rewriting (semi-Thue) over a small alphabet.**

- alphabet `Sigma`, `|Sigma| = 4..6`; presentation `R` = 6..10 unordered pairs
  `u_i <-> v_i` with `|u_i|, |v_i| <= 4`; strings capped at `L_max = 24`.
- a move rewrites one occurrence of `u_i` into `v_i` or the reverse. Every move
  is mechanically checkable, so **every derivation is a proof and the verifier
  is free**. This is the manufactured-contact channel.
- **goals are generated with their witness**: sample `s`, apply a random
  derivation of length `l`, obtain `t`; the goal is `(s, t)` and `l` is a known
  upper bound on the witness. This implements the Wall B scope of §1 and gives
  a difficulty ladder in `l`.
- the task is **not** to decide equality (every posed goal is true, so a
  "yes" oracle scores 100%). The task is to **find a derivation**. The metric is
  therefore search cost, which is exactly the short-path quantity the essay's
  VI.3 asks for.
- **inequality, finite quotients and the balcony are out of scope for cell 1.**
  Not every finitely presented structure admits a separating finite model and
  the general word problem is undecidable. The "only positives are
  manufacturable" motif motivates this cell but is not tested by it.

**Acquired state (both parts observable, neither an LLM):**

1. **Library `L`** — proved equations promoted to macro-rules (`s_i <-> t_i` in
   one search edge), with usage counts and the canonical primitive derivation
   stored as its witness. Readable by eye, freezable, transplantable.
2. **Policy `pi`** — ranks `(rule, position)` candidates during search. Linear
   model or small gradient-boosted ranker on hand features; CPU; trained only
   on the learner's own successful derivations (on-path steps positive,
   expanded-off-path negative).

**Feature rule (anti-tautology, from the collapse of the transparent-learner
option):** `pi`'s features MUST include surface features — the identity of
symbols at and around the rewrite position — and not only canonical or
structural ones. A renaming of `Sigma` must be *able* to break `pi`. Transfer
under renaming is then an earned measurement, not a property of the
representation. **Check before running: at initialization, transfer under
renaming must not already be perfect.** If it is, the features are wrong.

## 5. Arms and what is equalized

Acquisition arms: **ACTIVE**, **YOKED-SEED**, **YOKED-WORLD**, **STATIC-RW**
(a state-independent reversible-random-walk curriculum; §7.4). Evaluation is
then run on frozen state in three ledger conditions: **TRUE**, **FALSE**
(library and policy from a different presentation), **NONE**.

**Primary learner-ledger equalization across arms:** indexed search-work units
(`ISWU`, below); policy training steps; number and witness-length strata of
conjectures presented; library *capacity* (max entries); evaluation cap.

`ISWU` measures the work of using the frozen acquired state. Rule left-hand
sides are matched by one deterministic trie index. Traversing one trie edge and
emitting one concrete rule-position match each cost one unit. A
verified macro witness is paid once when the macro enters the library; later
applications cost the same emitted-match unit as primitive rules. This is the
primary reading because persistent reusable structure is the treatment, not an
accounting abbreviation to be expanded on every reuse.

Two protections keep that reading honest. First, index construction, witness
verification and library maintenance remain in the acquisition and
whole-system ledgers. Second, every successful proof separately reports its
fully expanded primitive derivation length. A sensitivity ledger also adds the
stored witness length at every successful macro match (`EXPANDED_MATCH`); it is
an intentionally anti-reuse upper bound, never the primary future-work metric.

**Secondary whole-system ledger:** learner work plus curriculum selection,
donor-curriculum generation, library maintenance, policy updates and measured
CPU time. It is reported as an additional cost frontier, not used to truncate a
YOKED learner's primary budget. A donor used for multiple recipients is shown
both with full cost per recipient and with the actual amortized cost; only the
former is the conservative single-recipient deployment reading.

**NOT equalized — measured as mediators:** realized library size, realized
proved-fraction of the curriculum, lemma reuse rate, library compression.
Forcing realized library size equal would subtract part of the treatment.

## 6. Metrics and estimand

For held-out goal `g` in arm `a`, let `T_ag` be ISWU to the first verifier-valid
derivation, `B` the common evaluation cap, `X_ag = min(T_ag, B)`, and
`delta_ag = 1[T_ag <= B]`. Unsolved goals remain in the primary endpoint at
`X_ag = B`; no analysis conditions on `delta = 1`.

Primary estimand at equal **learner-ledger** acquisition budget:

> `Delta_choice(B) = E[X_YOKED-SEED] - E[X_ACTIVE]` on paired held-out goal
> blocks. Positive values mean ACTIVE makes future derivations cheaper.

This is the restricted mean search cost through `B`, not mean cost among solved
goals. The mandatory companion statistic is `Pr(delta=1)` for each arm. The
primary block analysis uses paired block means with a 95% interval; no log
transform is used in the primary bounded endpoint. Paired `log(1+X)` and the
solve-rate contrast are sensitivity/diagnostic analyses only.

The registered `ACTIVE ~ YOKED-SEED` kill requires the full 95% interval for
`Delta_choice(B)` to lie inside `[-0.05B, +0.05B]` **and** at least 20% of goals
to solve in each arm. Superiority requires the interval lower bound to exceed
zero. Every other pattern, including heavy censoring that cannot establish
either condition, is `INDETERMINATE`, never equivalence and never success.

Secondary: the same restricted cost on a *second* held-out batch (forward-work
reduction); the `EXPANDED_MATCH` sensitivity; the whole-system cost frontier
from §5; lemma reuse rate; library size and compression; solve rate after
alphabet renaming; median fully expanded primitive derivation length.
Everything is reported per seed with paired blocks over world instances; no
metric is selected after seeing results.

## 7. Desk audit: identifiability and cheap shortcuts

The lesson of the walk world is that a cell must be proven non-trivial **before**
it is built. Each item below is marked as a **VOID**, **BASELINE** or **VALIDITY**
obligation and is checked on sampled presentations before any scientific arm
runs. The desk audit may reject a presentation family or fix a comparator; it
may not report an ACTIVE effect.

1. **VOID / BASELINE — Completion first.** Run ordered or unfailing
   Knuth–Bendix completion under the same whole-system CPU cap, put its partial
   rules into the exact same indexed library/search harness, and evaluate with
   the same ISWU endpoint. If completion saturates the held-out set (>=80% solved or
   restricted mean <=0.20B), the cell has no usable headroom and is void. If it
   does not saturate, KB remains a mandatory scientific baseline.
2. **VOID — Abelianization, length and Parikh shortcuts on the actual goal
   distribution.** Run length-only, letter-count/Parikh and their combined
   heuristic on the generated acquisition and held-out candidate pools, not
   merely on the presentation. If they close the held-out set at budget or
   explain the selected difficulty ladder without composition, the cell is a
   count/length task again. The report includes performance by witness-length
   stratum; "harder" may not mean only "longer".
3. **VOID — Convergence trap.** If the sampled presentation is terminating and
   confluent, normalization decides equality and finding derivations is trivial.
   Presentations must be verified **non-convergent** at the sampled sizes.
4. **BASELINE — Reversible random-walk curriculum.** Chen & Li show that graph
   connectivity plus a simple reversible-random-walk conjecturer can suffice for
   rapid theorem-set growth. `STATIC-RW` therefore samples provable conjectures
   by a state-independent reversible walk over the same reachable graph, with
   the same curriculum length, verifier work and generator-work ledger as
   ACTIVE. A pre-fixed iid list is too weak and is removed. If the graph cannot
   support a reversible walk without leaking held-out goals, the presentation is
   invalid for this design. `ACTIVE ~ STATIC-RW` in the later experiment is a
   scientific negative, not a desk-audit void.
5. **BASELINE — Plain bidirectional BFS / IDA\* at matched budget.** This is the NONE
   baseline. Calibrate `l` and the node cap so its solved-at-budget lands in a
   **20–60%** band: above that there is no room for experience to show, below it
   the signal is noise.
6. **VALIDITY — Two compute ledgers.** Verify §5 mechanically. The primary
   learner cap is identical and is never reduced to pay for a donor. The
   whole-system ledger reports, but does not disguise as the primary estimand,
   the cost of selection, donor generation and state updates. MM-ACL's replay
   removes online teacher selection work, and the two compute-matched
   library-learning re-evaluations show why both readings are required. Any arm
   whose ISWU cannot be equalized, or whose full machinery cannot be measured
   or conservatively charged, is invalid before outcome.
7. **VALIDITY — Lookup / memorization.** Held-out goals must not be closable by a single
   library entry (see §8).
8. **VALIDITY — Built-in canonicalization.** No component may canonicalize terms in a way
   that makes renaming-transfer automatic (§4).

If items 1–3 or the feasibility parts of 4–6 cannot be satisfied by any sampled
presentation within the sizes above, the cell is void and this memo is the kill
record. Passing this audit opens only implementation of the experiment; it does
not support the essay's scientific claim.

## 8. Leakage, defined correctly

Every provable goal lies in the logical closure of the axioms; reachability from
the closure is therefore **not** leakage. Leakage is:

- the held-out goal, or an alpha-/renaming-variant of it, appeared as a posed
  conjecture during acquisition;
- the goal pair `(s, t)` appears as an edge or endpoint pair in any acquisition
  proof DAG;
- a library entry is alpha-equivalent to the goal, or closes it in one macro
  step;
- train and test goals were generated from the same hidden derivation template
  (goal generation must draw disjoint template sets per split);
- the FALSE ledger accidentally shares entries with the TRUE ledger.

All five are asserted per goal, per run, and the assertion counts are printed in
the report. A run with any non-zero count is void, not "noted".

## 9. Pre-registered kills

- `ACTIVE ~ YOKED-SEED` at equal budget → coupling of contact to one's own state
  earns nothing here; the essay's registered `chosen contact` row takes a
  measured negative. Publishable as a limits result, and consistent with the
  compute-equalized null already reported for library learning.
- `TRUE ~ FALSE` or `TRUE ~ NONE` → the measured library is not the carrier of
  the acquired experience; the run is invalid as a ledger test, not a finding.
- transfer under renaming perfect at initialization → invariance was given, not
  earned; features are wrong, redesign before running.
- any §7 trivializer closes the held-out set → cell void.
- any §8 leakage count non-zero → run void.

## 10. Compute ledger and scope cap

CPU only; no GPU; no framework.

- acquisition: ~2000 conjectures x <=20k node cap ~ 4e7 expansions per arm-seed;
- evaluation: ~200 held-out goals x 50k node cap ~ 1e7 expansions;
- 4 acquisition arms x 3 ledger conditions x 5 seeds x 2 world instances;
- estimate ~10 CPU-minutes per arm-seed, order 5-10 CPU-hours total,
  embarrassingly parallel. Re-estimate after the first calibration run of §7.5.

**Complexity guard (exact LOC caps are withdrawn).** Neither `400` nor a larger
replacement has scientific meaning; both reward compressed, less reviewable
code and can trade directly against fair controls. The desk audit and later cell
must each remain one self-contained standard-library file, with no package,
config system, runner abstraction or generic harness. Line count is printed and
its growth must be attributed to named controls. A need for a second code module
or a generic abstraction is the design-circling alarm: work stops for scope
review. Fair comparators and validity checks may never be removed to satisfy
LOC.

## 11. What must happen before code

1. **DONE:** the targeted novelty scan found MM-ACL's cross-state replay outside
   formal mathematics, withdrew the broad novelty claim, and found no matching
   control in the three closest formal ablation sections.
2. **WITHDRAWN:** `WALLB_DESK_AUDIT_12.md` sampled eight presentations, but its
   surface arm was one-directional against bidirectional BFS and its completion
   arm normalized without searching under a non-confluent partial system. Its
   `PROCEED_TO_WORLD_CONTRACT` verdict is premature and carries no gate credit.
3. **SUPERSEDED CONFIGURATION FAILURE:** correction
   `WALLB_DESK_AUDIT_12B.md` used matched
   level-synchronous bidirectional search for both plain and surface-ordered
   arms, and tested `K in {0,8,32,64}` completion-derived macros inside that
   search. Every presentation supplied 64 macros with full, rechecked primitive
   witnesses. No nonzero K lowered its restricted mean. That establishes only
   `VOID_UNDER_PER_MATCH_WITNESS_TARIFF_WITH_LINEAR_SCAN_AND_COMPLETION_ORDER`:
   witness paths were repaid at every match, the matcher charged every
   rule-position pair, and selection ignored goal relevance. It is not a kill
   of the equational cell.
4. **DONE / UNDERPOWERED:** correction `WALLB_DESK_AUDIT_12C.md` used a
   deterministic trie matcher, printed both `ISWU` and `EXPANDED_MATCH`, and
   selected a goal-relevant order only from a disjoint seeded panel. Seven of
   eight presentations had no helpful K. Presentation `21b64bd46791` passed:
   at B=200, goal-relevant K=8 changed restricted-mean ISWU from 182.25 to
   157.25 and solve rate from 0.25 to 0.42; expanded-match sensitivity retained
   the gain (160.92). This is 6/24 versus 10/24 paired solves. Even under the
   favorable assumption of four gains and no losses, one-sided exact McNemar is
   0.0625 before eight-screen multiplicity. The singleton therefore has no gate
   credit; restricted mean is driven by the same censoring events.
5. **12D PREREGISTRATION / POWER BEFORE WIDTH:** rerun the same eight fixed
   presentations with three separately seeded, pairwise-disjoint panels per
   presentation: relevance, K=0 calibration and evaluation. Each panel has 64
   goals in each witness stratum (192 total). K=8 is the sole primary library
   size, frozen from 12c; K=32/64 and completion order are sensitivity only.
6. **CALIBRATION:** choose B solely on the calibration panel as the observed K=0
   work threshold whose solve rate is closest to 0.40 (tie: smaller B), and
   require the realized calibration rate to lie in [0.35,0.45]. Evaluation never
   changes B. Its K=0 position is reported, not tuned.
7. **PER-PRESENTATION GATE:** on the 192 paired evaluation goals require all of:
   K=8 solve-rate improvement; one-sided exact McNemar significance after Holm
   correction across the valid world-units; restricted-mean ISWU gain at least
   0.05B; and a positive one-sided paired-bootstrap lower bound using the
   conservative alpha=0.05/8 and 20,000 fixed-seed resamples. A panel collision
   invalidates only its presentation-local world-unit; no redraw or repair is
   allowed. Holm over all eight sampled units remains a sensitivity calculation.
   Any missing condition is not a pass. The report must expose gain/loss
   discordances and per-goal outcomes.
8. Only 12d may determine whether a usable development frame exists. No world
   contract or ACTIVE/YOKED arm is authorized before it.
9. **12D OBSERVED / POWERED SINGLETON:** powered evaluation preserved the former
   singleton on a fresh 192-goal panel: K=0 solved 70/192 and K=8 solved 94/192;
   discordance was 30 gains / 6 losses; exact one-sided McNemar p=3.48e-5 and
   Holm p=2.09e-4 over the six valid units; restricted-mean gain was 12.13 at
   B=179 (threshold 8.95), with conservative alpha=0.05/8 bootstrap lower bound
   7.26. Holm over all eight sampled units was 2.78e-4 and gives the same
   decision. Independently generated panels collided on one goal in
   `39cb46a5584e` and three goals in `95afdd10ecd2`; a collision invalidates only
   its world-unit because panels, seeds and inference are presentation-local.
   Neither invalid unit was a signal under either Holm route. No redraw or panel
   repair is authorized.
10. **HETEROGENEITY / NEXT GATE:** the powered signal occurred in one of eight
    sampled presentations. Several other presentations showed null or harmful
    library effects, so this is not evidence of a family-wide mechanism.
    Running ACTIVE/YOKED in `21b64bd46791` would estimate a
    selection-conditional effect in a world chosen for library usefulness. The
    only permitted next step is a preregistered independent frame audit, sized
    before generation (planning range 30--50 fresh presentations, 192 goals
    each), with mechanical inclusion, a frozen usable-world predicate and a
    frozen prevalence/acceptance rule. Its exact size is an author choice, not
    selected from 12d. No world contract or learner arm is authorized by 12d.

Nothing in this memo is a result. It is a design that can be killed cheaply, in
the order that kills it cheapest.
