# TWOPRES_00 — desk audit ticket (pre-cell, pre-code-of-record)

Status: `DESK_AUDIT_ONLY__NO_CELL_AUTHORIZED`
Slot: *(author assigns; not yet an IDEA_GATE slot)*

NON-CITABLE. Dev world only. No learner, no training, no arm, no outcome.
This ticket exists to answer IDEA_GATE item 1 — identifiability — **before**
any harness exists. Written after B2/09, whose lesson was that the whole
arm was answerable from one init probe.

---

## 1. The idea being audited, stated so it can be killed

Two finite presentations `R1`, `R2` of the same monoid are two *roads* to one
object. A learner sees words and derivations from both streams. **The
correspondence between the two alphabets is never given.** If the learner
recovers structure that is invariant across the two presentations, that
invariance was earned, not donated.

Scope sentence, binding on every later claim:

> This is not a test of whether a translation between `R1` and `R2` exists.
> Translation exists by construction. It is a test of whether the
> correspondence is *findable from the observable streams alone* without
> solving the word problem, and of whether joint exposure reduces forward
> work relative to a matched single-presentation budget.

Consequences:

- The estimand is a **cost** estimand, as in `WALLB_DESIGN_MEMO_11` §1.
- Paired presentation of the same element across streams is **prohibited**.
  Supplying pairs donates the invariance and reduces the cell to supervised
  multi-view learning.
- The Tietze chain relating `R1` to `R2` is **sealed** and is never learner
  input, never a feature, and never a label.

## 1b. Literature position (scan of 2026-08-16)

| work | what it establishes | what it leaves |
|---|---|---|
| Conneau, Lample, Ranzato, Denoyer, Jégou, *Word Translation Without Parallel Data* (arXiv:1710.04087; MUSE) | a correspondence between two vocabularies can be recovered with no parallel data, by adversarial alignment plus iterative Procrustes | never applied to two presentations of one formal object; no cost estimand |
| Søgaard, Ruder, Vulić, *On the Limitations of Unsupervised Bilingual Dictionary Induction* (ACL 2018; arXiv:1805.03620) | the isomorphism assumption usually fails; success depends on the pair, on corpus comparability and on embedding parameters; **eigenvector similarity of nearest-neighbour graphs correlates near-perfectly with induction success** | gives D1 a predictor that requires running no alignment at all |
| Shehper, Kucharski, Wang, Gukov, *What makes math problems hard for reinforcement learning* (arXiv:2408.15332) | difficulty structure of search over presentation-transformation moves, studied directly | single presentation; searches for a path, not for an invariant across two |
| *AI-Driven Mathematical Discovery for the Andrews–Curtis Conjecture* (2026) | Lean + LLM + RL trivialises 753 Miller–Schupp presentations; long horizon, sparse reward named as the two hard properties | same |
| *The Two-Hump Problem: Bridging the Difficulty Gap in Mathematical Reinforcement Learning* (arXiv:2606.21611) | difficulty in this world is bimodal — trivial and impossible with little between | this is the named prior form of the D3 band risk |
| Bridson, *The complexity of balanced presentations and the Andrews–Curtis conjecture* (arXiv:1504.04187) | the space of balanced presentations carries a metric = minimal number of Tietze transformations, and exponentially many presentations are pairwise far apart | that minimum is not what a generator produces (see §2) |

**Claimed contribution, stated narrowly.** The mechanism is not ours:
unsupervised correspondence recovery, RL over presentation moves, and the
Tietze metric are all established. What the scan did not find is a design in
which two presentations of one object are given to one learner **with the
correspondence withheld**, scored by forward-work reduction at a matched
budget, along a graded presentation distance.

**Status: PLAUSIBLE GAP, NOT ESTABLISHED.** Do not restate this as priority.

**Predicted failure mode, to be mapped rather than assumed.** Combining
Søgaard with the `t` ladder predicts that small `t` leaves the two
co-occurrence structures near-isomorphic, so the correspondence is cheaply
recoverable and the cell is trivial; while large `t` breaks the isomorphism,
so there may be nothing left to earn either. The usable band is where the
correspondence is not cheap but is reachable. It may be narrow or empty.
D1 exists to draw that curve.

## 2. World construction

Reuse the `WALLB_DESIGN_MEMO_11` §4 family unchanged where possible:

- alphabet `Sigma`, `|Sigma| = 4..6`; presentation `R1` = 6..10 unordered
  pairs `u_i <-> v_i` with `|u_i|, |v_i| <= 4`; strings capped `L_max = 24`.
- `R2` is derived from `R1` by a sealed chain of `t` Tietze transformations
  (add/remove a generator with its defining relation; add/remove a relation
  derivable from the others). Same-monoid-ness therefore holds **by
  construction**, exactly as Wall B's goals are generated with their witness,
  and no undecidable word problem is ever posed.
- `t` is the difficulty ladder. Report every result per `t`.

**`t` is nominal, not a distance.** Applying `t` moves bounds the Tietze
distance from above; moves cancel, so the true distance may be far smaller.
Computing the true distance is hard — that is the content of Bridson's result
and part of why Andrews–Curtis is open. Two obligations follow, and neither
may be skipped:

1. every table and figure labels the axis `nominal t`, never "distance";
2. a bounded reverse search reports, per triple, whether a chain shorter than
   `t` was found, with `SPACE_CLOSED` and `BUDGET_EXHAUSTED` recorded as
   distinct outcomes (Wall B §7 discipline). A triple whose reverse search
   finds a much shorter chain is struck from its band and re-labelled.

Author choice required before the script is written: the exact Tietze move
set, their sampling weights, and the `t` grid.

## 3. Kills — each is a pre-registered kill of the whole cell

Every item is checked on sampled `(R1, R2, t)` triples. All are measurement,
not experiment.

**D0 — generator feasibility.** Can `(R1, R2)` triples be produced at the
sizes above across the whole `t` grid, within a declared draw budget, without
`R2` exceeding the size caps? If some band of `t` cannot be filled, report it
now rather than at cell time. Record accepts and rejections with a closed
cause enum; every draw is ledgered.

**D1 — cheap recovery of the correspondence.** For each triple, run these on
samples drawn from each stream *separately*, with no cross-stream pairing
supplied, and score them against the sealed generator correspondence.

**D1.0 — the spectral predictor, run first because it is the cheapest thing
in this document.** Build a nearest-neighbour (or co-occurrence) graph per
stream, independently, and compute the eigenvector/Laplacian-spectrum
similarity between them. Søgaard et al. report a near-perfect correlation
between this quantity and unsupervised correspondence recovery. If it stays
high across the whole feasible `t` grid, the cell is void **without running a
single alignment**. This is one page of code and it goes first.

Then, only if D1.0 leaves a candidate band:

1. rule-set matching modulo alphabet renaming (detects small `t` outright);
2. unigram/bigram symbol-frequency matching between streams;
3. word-length-distribution matching;
4. MUSE-style alignment of independently built per-stream co-occurrence
   embeddings: adversarial initialisation plus iterative Procrustes
   refinement.

**Output is a curve, not a verdict.** Report recovery-vs-`t` and
spectral-similarity-vs-`t` for every method. Do not reduce D1 to a
threshold test: a threshold on a quantity whose shape is unknown is the
degenerate reading rule that has now cost two runs (16B, 16D). The band
decision is made from the shape of the curve against `RECOVERY_MAX`, and
`RECOVERY_MAX` is signed before the script runs.

Kill: if recovery exceeds `RECOVERY_MAX` at every feasible `t`, **the cell is
void and this ticket is the kill record.** If recovery is at chance for every
`t`, that is equally informative and equally fatal — there is no band in which
the correspondence is reachable at all.

**D2 — init decodability.** On a randomly initialised encoder of the intended
family, fit a linear probe to classify `(w1, w2)` as same-element versus
different-element. If accuracy at initialisation exceeds `INIT_MAX`, the
correspondence is architectural and the cell measures the encoder.

Binding requirement, from the B2/09 defect, in the executable form supplied by
the protocol review:

> Before the first D2 measurement for seed `s`, materialize one ordered corpus
> byte string and record `n_items`, ordered item identities, ordered
> labels/strata, split indices, canonical bytes, and SHA-256. Every init,
> trained, method, and repeat measurement for `s` must consume that same
> immutable object. Immediately before each measurement assert equality of the
> object identity, byte length, SHA-256, ordered identities, labels/strata,
> and split indices to the frozen record. No measurement function may
> resample, filter, rebalance, reorder, or select a stratum. Any mismatch or
> changed denominator returns `D2_INVALID_CORPUS_MISMATCH`; no D2 curve,
> delta, or verdict is emitted. Different seeds use separate seed-only
> domains; measurement state or method name may not enter the corpus domain.

The last sentence is the one B2/09 violated: `run_tag` and the arm name
entered the stream domain, so init and trained probes drew different corpora
and every delta compared accuracies over different word sets.

**D3 — difficulty calibration.** Naked bidirectional search on each
presentation alone must close held-out derivations in the **20–60%** band at
the chosen node cap, per `WALLB_DESIGN_MEMO_11` §7.4. Above the band there is
no room for anything to reduce work; below it there is no signal. Report the
full distribution of search cost, not only the solved fraction: two settings
with the same 40% can be a smooth spectrum or a trivial/impossible mixture,
and only the first is usable. The mixture case is not hypothetical here —
arXiv:2606.21611 reports exactly this bimodality for search in this family,
so the shape check is mandatory and its absence voids D3.

**D4 — ledger arithmetic, declared before any number exists.** State, as
frozen text, how "joint exposure to two presentations at budget B" is made
comparable to "one presentation at budget B". Minimum content, per the
protocol review:

- **learner-only:** an immutable event schema; presentation identifier and
  order; learner state before and after; every charged transition with its
  exact unit cost; cumulative budget; the stop event; failed and aborted work;
  and a rule charging the joint and single conditions by the same primitive
  operation, with **no batching discount**.
- **whole-system:** all of the above plus construction and selection of each
  presentation, reverse-search or witness work, verification, serialization,
  indexing, storage and retrieval, scheduling, failed candidates and
  preprocessing, with a deterministic shared-cost allocation. Report total and
  per-item cost. A shared cost is either charged in full to the joint
  condition or allocated by one prospectively fixed additive rule that is also
  applied to the single condition.

If these fields and the common budget clock cannot be closed now, **D4 blocks
the cell, not the audit** — and values observed by this audit may never define
the ledger retroactively.

**D4 is the first admissible cut if the scope cap is exceeded** (§5). An
undefined dual ledger cannot kill a cell cheaply and risks costing more than
the harness it exists to prevent. Cutting D4 defers the cell; raising the cap
does not.

## 4. Reading rules, fixed before execution

For every threshold in D1–D3, **both outcomes must be reachable.** Before
dispatch, state for each rule what data would produce the opposite verdict.
A rule that can only return one answer is a defect, not a result — this is
the 16D lesson and the second time it has cost a run.

**Analysis population.** Every quantity here is a deterministic qualification
function of the complete finite attempted audit, not a sample-based estimate.
Triples are repeated deterministic records within a nominal-`t` band, not
independent inferential units. **No confidence interval, hypothesis test or
bootstrap is permitted** unless the ticket separately defines a stochastic
target population and an independent sampling law over it — it does not.
Give triples equal weight within a band and bands equal weight in any pooled
figure. Print every numerator and denominator.

**`t = 0` is the instrument's positive control and is free.** At `t = 0` the
two presentations differ only by the terminal alphabet renaming, so D1 method
1 must recover the correspondence in full. If it does not, the scorer or the
generator is broken. A `t = 0` failure is an **instrument kill**, not a cell
kill, and it stops the run before any other number is read.

Report per triple and per `t`. No threshold is chosen after seeing numbers.

## 5. Scope cap

- one throwaway file, **≤ 200 lines**, plus a results JSON;
- CPU only, one process, one thread; deterministic;
- no learner training, no arms, no curriculum, no policy, no cell;
- hard ceiling: 3 wall hours;
- stop early on: D0 infeasible across the grid, any D1 method saturating at
  every `t`, or nondeterminism between two fresh executions.

If the script outgrows the cap, that is the design-circling alarm and work
stops rather than continues.

## 6. Provenance

Hash the script and every input. **Normalise line endings before hashing and
record that normalisation**, or a Windows-to-Linux transfer will change every
digest without changing a byte of meaning — as it did in B2/09, where the
JSON's self-recorded `script_hash` matched no hash quoted in any document.

Emit the sealed Tietze chain to a separate file that the audit script never
reads and that no later cell may open.

## 7. Author choices required before dispatch

1. Tietze move set, sampling weights, and the `t` grid.
2. `RECOVERY_MAX` (D1) and `INIT_MAX` (D2).
3. Node cap for D3 and the held-out draw count.
4. The two ledger definitions in D4.
5. Encoder family for D2 — it must be the family the cell would actually use,
   or D2 measures the wrong architecture.

## 8. Negative authorization

This ticket authorizes a throwaway measurement script and nothing else. No
cell, no arm, no learner, no training, no curriculum, no scientific outcome,
no commit to a citable path. Nothing in this document is a result.
