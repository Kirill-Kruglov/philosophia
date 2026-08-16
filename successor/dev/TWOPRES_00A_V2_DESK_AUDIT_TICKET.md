# TWOPRES_00A_V2 — desk audit, cut scope

Status: `UNSIGNED__AWAITING_PROTOCOL_ACCEPTANCE`

Supersedes `TWOPRES_00A_DESK_AUDIT_TICKET.md`.
Disposition: `TWOPRES_00A_REVIEW_DISPOSITION_2.md`.

NON-CITABLE. No learner, no training, no arm, no cell, no outcome.

## 1. What is audited

Two presentations `R1`, `R2` of one finite monoid `M`. Methods see words over
`Sigma_1` and words over `Sigma_2`, drawn independently per stream. Nothing
pairs them.

> Is **element correspondence** — which words over the two alphabets denote the
> same element of `M` — recoverable by cheap label-free methods, as a function
> of nominal presentation distance, up to `Aut(M)`?

**Every terminal in this ticket is scoped to the exact materialized finite
family. No claim transfers to infinite monoids, to other families, or upward
in any direction.** The previous version asserted that survival transfers
upward. That assertion had no argument behind it and is withdrawn.

**Identifiability boundary, by construction.** For `alpha` in `Aut(M)`,
composing the second evaluation map with `alpha` leaves both unpaired streams
byte-identical while changing every cross-stream label. Exact element
correspondence is therefore unidentifiable up to `Aut(M)` for any method
whatsoever. Scoring quotients by the orbit (§4, `D-1`). The realized
`|Aut(M)|` distribution is reported in D0 whatever the outcome: it is the size
of the boundary.

**Alphabet correspondence is not audited.** At `t = 0` only a cosmetic
renaming separates the presentations and enumeration of the `<= 720`
bijections settles it. At `t > 0` moves `M3`/`M4` may leave no bijection at
all, so the enumerated map is a heuristic partial map and not a
correspondence. This boundary is stated because the previous version claimed
enumeration settles the question at every `t`, which contradicts its own move
set.

## 2. Prior work, at the strength it supports

- Conneau et al., arXiv:1710.04087 — correspondence recoverable without
  parallel data.
- Søgaard, Ruder, Vulić, arXiv:1805.03620 — the isomorphism assumption usually
  fails; graph-spectrum similarity correlates with induction success.
  **Correlation, not implication.** D1.0 orders work and never kills.
- Shehper, Kucharski, Wang, Gukov, arXiv:2408.15332; Miller–Schupp
  trivialization work (2025); *Two-Hump*, arXiv:2606.21611 — **group**
  presentations. Adjacent motivating prior only; no bimodality claim about
  this monoid family is made or inherited.
- Bridson, arXiv:1504.04187 — cited for the Tietze metric only.
  `VERIFY_BEFORE_CITING`.

**Novelty: PLAUSIBLE GAP, NOT ESTABLISHED.**

## 3. Materialization law — frozen, deterministic, complete

### 3.1 The monoid is defined by the presentation, not sampled beside it

Sample `R1` in band. Run bounded Knuth–Bendix completion. **Accept only if
completion terminates with a finite complete system whose element count is in
`MONOID_ORDER_BAND`.** `M` is then defined as what `R1` presents; no
isomorphism claim exists to certify, `|M|` is exact, and normal forms give
equality *and* inequality as ground truth.

M1/M2 derivability and redundancy witnesses reduce to normal-form comparison.
M3/M4 update the evaluation map mechanically.

**Consistency note.** `WALLB_DESIGN_MEMO_11` §7.2 forbids convergent
presentations because convergence trivializes finding derivations. That
applies to a learner searching. Here convergence is used only by the sealed
scorer and no party under test ever sees it. **00b inherits a blocker:** once
a learner searches, ground truth cannot come from a convergent system, and
00b must specify another mechanism before it may be designed.

### 3.2 Two disjoint objects

```text
UNPAIRED_STREAM_CORPORA   # all a method may read: words per stream, no labels
SEALED_PAIR_EVAL          # balanced same/different pairs; scorer only
```

The sealed set, the Tietze chain, the completion, the Cayley table and
`Aut(M)` live in a file no method may open. A call-graph test proves it. Every
baseline is label-free until final scoring; no method fits on labels.

**Methods may run bounded rewriting in their own presentation.** That is their
cost, not cheating, and it is what makes a label-free decision possible at
all. Budget `METHOD_WORD_BUDGET`, reported per method and per pair, with
`BUDGET_EXHAUSTED` counted separately from a decision.

### 3.3 Constants

```text
MONOID_ORDER_BAND   = <author cell>
AUT_MAX             = <author cell>   # triple rejected if |Aut(M)| exceeds it
SIGMA_BAND          = 4..6
RELATION_BAND       = 6..10
RELATOR_LEN_MAX     = 4
KB_BUDGET           = <author cell>   # completion; non-termination is a rejection cause
WORD_LEN_BAND       = <author cell>
WORD_LAW            = uniform over Sigma at each position, uniform over WORD_LEN_BAND
N_WORDS_PER_STREAM  = <author cell>   # after canonical dedupe; top up by continuing
                                      #   the same counter stream, never by re-seeding
N_PAIRS_PER_TRIPLE  = <author cell>   # balanced; chance = 0.5
PAIR_LENGTH_MATCH   = same-element and different-element pairs are drawn to the
                      same joint length marginal; asserted before scoring
TRIPLES_PER_T       = <author cell>
T_GRID              = [0, 2, 4, 8, 16, 32]
DRAW_BUDGET         = <author cell>
ROOT_SET            = counter-keyed, domain (triple_id, seed); no other field
METHOD_WORD_BUDGET  = <author cell>
```

Tietze moves `M1`–`M4`, weights `3:3:2:2`, bounded by the bands above. A chain
ending out of band is rejected whole and consumes its draw index. Terminal
alphabet bijection applied and sealed; cosmetic, not a difficulty move.

**Rejection-cause enum, closed:** `KB_NONTERMINATION`, `ORDER_OUT_OF_BAND`,
`AUT_TOO_LARGE`, `SIGMA_OUT_OF_BAND`, `RELATION_OUT_OF_BAND`,
`WORD_LEN_EXCEEDED`, `INSUFFICIENT_POSITIVE_PAIRS`, `DRAW_BUDGET_EXHAUSTED`.
Every accept and every rejection consumes exactly one draw index. Two fresh
processes produce byte-identical corpora and ledgers.

**Corpus identity.** One immutable ordered corpus object per `(triple_id,
seed)`, recording `n_items`, ordered identities, split indices, canonical
bytes and SHA-256. Every method consumes that object; equality is asserted
immediately before each measurement. Mismatch returns `CORPUS_MISMATCH` and no
number is emitted. Method name, attempt and run tag may never enter the corpus
domain — that is the B2/09 defect as a rule.

## 4. Items

**D-1 — symmetry typing.** Quotient by two distinct groups, both required:
alphabet permutations (`<= 720`, enumerated) and `Aut(M)` computed from the
sealed Cayley table. Recovery is scored against the best representative of the
joint orbit. Triples with `|Aut(M)| > AUT_MAX` are rejected and counted.

**D0 — generator feasibility.** Fill per `t` inside `DRAW_BUDGET`; rejection
counts per cause; realized `|M|` and `|Aut(M)|` distributions. Infeasibility is
reported now.

**D1.0 — spectral predictor, descriptive only.** Per-stream nearest-neighbour
graph; spectrum similarity between streams, against `t = 0` as roof and an
independently drawn presentation of a different monoid as floor. High
similarity emits `PREDICTED_CHEAP` and orders work. **It never kills and never
substitutes for a measurement.**

**D1a — cheap label-free baselines**, scored on `SEALED_PAIR_EVAL`, chance
`0.5`:

1. **surface statistics** — word length and symbol counts only; an unsupervised
   decision rule fixed in advance, fitted on no labels;
2. **best partial alphabet map** — exhaustive search over the `<= 720`
   candidates, scored by short-derivation agreement between the two rule sets
   (label-free), then used to classify a pair by bounded rewriting in `R2`
   within `METHOD_WORD_BUDGET`.

Method 3 of the previous version (co-occurrence-embedding nearest neighbour)
is deferred to 00b with its hyperparameters.

Deferred to 00b: MUSE-style alignment, D2 init decodability, D3 search
calibration, reverse-search certificate. D4 is
`PAPER_OBLIGATION_NOT_SCRIPT`: it must close before any cell is authorized and
consumes no budget here.

## 5. Analysis population

Deterministic qualification of the complete finite attempted audit, not a
sample-based estimate. Triples are repeated deterministic records within a
nominal-`t` band, not independent inferential units. **No confidence interval,
hypothesis test or bootstrap.** Equal weight to triples within a band, equal
weight to bands in any pooled figure. Print every numerator and denominator.

`t` is **nominal**: `t` moves bound Tietze distance from above only. Every
axis is labelled `nominal t`. No re-labelling rule exists.

## 6. Terminal cascade — total function, first match wins

Define, per method `m` and nominal `t`:

```text
r_m(t)  = recovery of method m at t, pooled over triples with equal weight,
          scored against the best joint-orbit representative
r*(t)   = max over methods of r_m(t)
CAND(t) = r*(t) - 0.5 > RECOVERY_MAX                # candidate cell
BAND    = a contiguous run of >= BAND_MIN_T grid cells, all CAND-false and all
          with r*(t) - 0.5 > CHANCE_TOL             # not cheap, not chance
```

`BAND_MIN_T` counts **grid cells**, not numeric `t` width.

1. `AUDIT_NOT_RUN_SCOPE_CAP_EXCEEDED` — the file exceeds 120 lines.
2. `AUDIT_NOT_RUN_WALL_CAP_EXCEEDED` — 90 minutes total across both fresh
   executions is exceeded.
3. `AUDIT_NOT_RUN_GENERATOR_INFEASIBLE` — D0 cannot fill the grid.
4. `INSTRUMENT_INVALID_POSITIVE_CONTROL` — at `t = 0`, after D-1
   quotienting, method 2 does not recover the correspondence in full.
5. `INSTRUMENT_INVALID_NONDETERMINISTIC` — two fresh executions disagree.
6. `CORPUS_MISMATCH` — any frozen-corpus assertion fails.
7. `CELL_VOID_CHEAP_RECOVERY` — `CAND(t)` true at every feasible `t`.
8. `REACHABILITY_UNRESOLVED` — `r*(t) - 0.5 <= CHANCE_TOL` at every feasible
   `t`. Not a kill: cheap methods failing does not show unreachability for a
   learner.
9. `NO_CONTIGUOUS_BAND_UNRESOLVED` — neither 7 nor 8, and no `BAND` exists.
   Non-monotonicity alone is not a defect and does not appear here.
10. `BAND_CANDIDATE_FOUND` — otherwise. Authorizes the design of 00b within
    this exact family and nothing else. It is not evidence for the cell.

```text
RECOVERY_MAX = <author cell>
CHANCE_TOL   = <author cell>
BAND_MIN_T   = <author cell>
```

For terminals 7–10 the script carries a comment naming the concrete data
pattern producing a different terminal. A rule whose opposite cannot be named
is a defect; stop and escalate.

## 7. Scope cap

One throwaway file, **<= 120 lines**, plus a results JSON. CPU only, one
process, one thread, deterministic. **90 minutes total across both fresh
executions.** No package, no config system, no runner abstraction.

Stop early on terminals 1–6. If the file outgrows the cap, stop; do not
modularize to stay under the count and do not request a raise.

## 8. Provenance

Record **both** raw-byte and LF-normalized SHA-256 of the script and every
input; the normalized digest does not replace byte provenance. Emit both into
the results JSON and quote the same values in any report. In B2/09 the JSON
recorded a `script_hash` matching no document, because the executed file was
CRLF and the archived copy LF.

## 9. Author cells

`MONOID_ORDER_BAND`, `AUT_MAX`, `KB_BUDGET`, `WORD_LEN_BAND`,
`N_WORDS_PER_STREAM`, `N_PAIRS_PER_TRIPLE`, `TRIPLES_PER_T`, `DRAW_BUDGET`,
`METHOD_WORD_BUDGET`, `RECOVERY_MAX`, `CHANCE_TOL`, `BAND_MIN_T`.

Twelve cells, all signed before any triple exists. No audit output may revise
any of them; revision requires a new ticket version and fresh roots.

## 10. Negative authorization

Authorizes one throwaway measurement script after protocol acceptance and
author signature, and nothing else. No cell, no arm, no learner, no training,
no scientific outcome, no commit to a citable path. Nothing here is a result.
