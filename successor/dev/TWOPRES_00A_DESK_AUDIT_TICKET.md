# TWOPRES_00A — desk audit, cut scope

Status: `UNSIGNED__AWAITING_PROTOCOL_ACCEPTANCE`

Supersedes `TWOPRES_00_DESK_AUDIT_TICKET.md`. Disposition of the review that
caused the cut: `TWOPRES_00_REVIEW_DISPOSITION.md`.

NON-CITABLE. No learner, no training, no arm, no cell, no outcome.
Constants are folded into this file rather than kept separately: at 120 lines
of throwaway script, a separate constants document is apparatus, not
discipline.

## 1. What is audited

Two presentations `R1`, `R2` of one **finite** monoid `M`. Cheap methods see
words over `Sigma_1` and words over `Sigma_2`, drawn independently per stream.
Nothing pairs them.

> The audited question is whether **element correspondence** — which words
> over the two alphabets denote the same element of `M` — is recoverable by
> cheap methods that never solve a word problem, as a function of nominal
> presentation distance.

Not audited: alphabet correspondence. With `|Sigma| <= 6` there are at most
720 bijections; enumeration settles it at every `t`. It survives only as the
instrument's positive control.

**Finiteness is a scope restriction with a one-sided consequence.** It exists
so that both same-element and different-element labels are ground truth by
construction. It makes the task *easier* for cheap methods. Therefore survival
transfers upward and a kill does not — the kill terminal is named
accordingly.

## 2. Prior work, restated at the strength it supports

- Conneau et al., arXiv:1710.04087 (MUSE): a correspondence between two
  vocabularies is recoverable with no parallel data.
- Søgaard, Ruder, Vulić, ACL 2018 (arXiv:1805.03620): the isomorphism
  assumption usually fails; eigenvector similarity of nearest-neighbour graphs
  correlates strongly with induction success. **Correlation, not implication;
  isospectrality is not isomorphism.** This is why D1.0 orders work and never
  kills.
- Shehper, Kucharski, Wang, Gukov, arXiv:2408.15332; the Miller–Schupp
  trivialization work (2025); *The Two-Hump Problem*, arXiv:2606.21611 — all
  concern **group** presentations. Adjacent motivating prior for search
  difficulty over presentation moves. No claim about bimodality in this
  monoid family is made or inherited.
- Bridson, arXiv:1504.04187 — cited for the Tietze metric on presentation
  space only. `VERIFY_BEFORE_CITING`: the stronger reading in ticket 00 was
  not checked against the paper and is withdrawn.

**Novelty status: PLAUSIBLE GAP, NOT ESTABLISHED.** Not to be restated as
priority anywhere.

## 3. Materialization law — frozen, deterministic, complete

Nothing below may be chosen at runtime.

```text
MONOID_ORDER_BAND   = <author cell>   # |M|, finite
SIGMA_BAND          = 4..6
RELATION_BAND       = 6..10
RELATOR_LEN_MAX     = 4
WORD_LEN_BAND       = <author cell>
N_WORDS_PER_STREAM  = <author cell>
N_PAIRS_PER_TRIPLE  = <author cell>   # balanced same/different, chance = 0.5
TRIPLES_PER_T       = <author cell>
T_GRID              = [0, 2, 4, 8, 16, 32]
DRAW_BUDGET         = <author cell>
```

**Tietze moves** (`M1` add derivable relation, `M2` remove redundant relation,
`M3` add generator with defining relation `|w| <= 4`, `M4` remove generator by
substitution), weights `3:3:2:2`, all bounded by the bands above. A chain
ending outside the bands is rejected whole and consumes its draw index. A
terminal alphabet bijection is applied and sealed; it is cosmetic, not a
difficulty move.

**Word streams.** Per presentation, draw `N_WORDS_PER_STREAM` words by
counter-keyed uniform sampling over `WORD_LEN_BAND`, canonically dedupe, fix
the order, and materialize one immutable ordered corpus object recording
`n_items`, ordered identities, labels, split indices, canonical bytes and
SHA-256. Every method consumes that same object. Any mismatch returns
`CORPUS_MISMATCH` and no number is emitted. The corpus domain is keyed by
`(triple_id, seed)` only — never by method name, attempt, or run tag. That
last clause is the B2/09 defect written as a rule.

**Pair labels** come from evaluating both words in the sealed `M`. The sealed
chain and `M` are written to a file no method may open; only the scorer reads
it, and a call-graph test proves it.

**Every accept and every rejection consumes exactly one draw index**, with a
closed rejection-cause enum. Two fresh processes must produce byte-identical
corpora and ledgers.

## 4. Items

**D-1 — symmetry typing.** Before anything is scored, enumerate the at most
720 alphabet permutations and quotient the correspondence by the automorphisms
of the materialized relation set and corpora. Recovery is scored against the
**best representative of the equivalence class**. Presentations whose symmetry
class is degenerate are counted and reported in D0, not silently dropped.
Without this, a correct method can be failed by a symmetry it cannot see.

**D0 — generator feasibility.** Can triples be produced across the whole
`T_GRID` inside `DRAW_BUDGET`, with `M` finite and in band? Report fill per
`t`, rejection causes, and degenerate-symmetry counts. Infeasibility is
reported now, not discovered later.

**D1.0 — spectral predictor, descriptive only.** Per-stream nearest-neighbour
graph, spectrum similarity between streams, reported against two anchors:
`t = 0` as the roof and an independently drawn presentation of a **different**
monoid as the floor. High similarity emits `PREDICTED_CHEAP` and orders the
work. **It never kills and never stands in for a measurement.**

**D1a — exact cheap baselines on element correspondence.** Scored on the
frozen balanced pair set, chance `0.5`:

1. surface-statistic classifier — word length and symbol counts only;
2. best partial alphabet map by exhaustive search over the `<= 720`
   candidates, scored by short-derivation agreement, then used to classify
   pairs. This is the strongest cheap method available in this world and is
   the one that decides whether knowing the alphabet map also gives element
   correspondence;
3. nearest neighbour in independently built per-stream co-occurrence
   embeddings, under the best map from (2).

Output is the recovery-vs-`t` curve per method, with numerator and denominator
printed for every cell.

Deferred to 00b, by disposition: MUSE-style adversarial alignment, D2 init
decodability, D3 search calibration, and the reverse-search certificate.
D4 is reclassified `PAPER_OBLIGATION_NOT_SCRIPT` and must close before any
cell is authorized; it consumes no budget here.

## 5. Analysis population

Every quantity is a deterministic qualification function of the complete
finite attempted audit, not a sample-based estimate. Triples are repeated
deterministic records within a nominal-`t` band, not independent inferential
units. **No confidence interval, hypothesis test or bootstrap.** Triples get
equal weight within a band; bands get equal weight in any pooled figure.

`t` is **nominal**: applying `t` moves bounds Tietze distance from above only.
Every axis is labelled `nominal t`. No re-labelling rule exists in 00a, so
none can misfire.

## 6. Terminal cascade — first match wins, evaluated in order

1. `AUDIT_NOT_RUN_GENERATOR_INFEASIBLE` — D0 cannot fill the grid inside
   `DRAW_BUDGET`.
2. `INSTRUMENT_INVALID_POSITIVE_CONTROL` — at `t = 0`, after D-1
   class-quotienting, method 2 fails to recover the correspondence in full.
   The scorer or the generator is broken; no other number is read.
3. `INSTRUMENT_INVALID_NONDETERMINISTIC` — two fresh executions disagree.
4. `CORPUS_MISMATCH` — any frozen-corpus assertion fails.
5. `CELL_VOID_CHEAP_RECOVERY_FINITE` — recovery exceeds `RECOVERY_MAX` at
   every feasible `t`. Closes the finite case only.
6. `REACHABILITY_UNRESOLVED` — recovery is within `CHANCE_TOL` of `0.5` at
   every feasible `t`. Not a kill: cheap methods failing does not show the
   correspondence is unreachable for a learner.
7. `CURVE_NON_MONOTONE_UNRESOLVED` — the curve is neither uniformly above
   `RECOVERY_MAX` nor uniformly at chance, and no contiguous band satisfies
   the band condition.
8. `BAND_CANDIDATE_FOUND` — otherwise. Authorizes the design of 00b and
   nothing else. It is not evidence for the cell.

```text
RECOVERY_MAX = <author cell>   # separation above chance, per method
CHANCE_TOL   = <author cell>
BAND_MIN_T   = <author cell>   # contiguous t values required for a band
```

For each of terminals 5–8, the script must carry a comment naming the concrete
data pattern that produces a different terminal. A rule whose opposite cannot
be named is a defect; stop and escalate rather than implement it. This is the
16B/16D lesson placed inside the executable file.

## 7. Scope cap

One throwaway file, **<= 120 lines**, plus a results JSON. CPU only, one
process, one thread, deterministic. Hard ceiling **90 minutes**. No package,
no config system, no runner abstraction.

Stop early on: D0 infeasible, `t = 0` positive-control failure, corpus
mismatch, or nondeterminism.

If the file outgrows the cap, stop. Do not modularize to stay under the count,
do not request a raise. Ticket 00 put a generator, a reverse search, spectral
analysis, four alignment methods including adversarial MUSE, an encoder probe,
a bidirectional search, two ledgers and a double execution inside 200 lines
and called it the cheapest measurement in the document. That was the error
this cut exists to correct.

## 8. Provenance

Record **both** the raw-byte and the LF-normalized SHA-256 of the script and
of every input; the normalized digest does not replace byte provenance. Emit
the script's own hashes into the results JSON and quote the same values in any
report. In B2/09 the JSON recorded a `script_hash` that matched no document,
because the executed file was CRLF and the archived copy was LF.

## 9. Author cells

Materialization: `MONOID_ORDER_BAND`, `WORD_LEN_BAND`, `N_WORDS_PER_STREAM`,
`N_PAIRS_PER_TRIPLE`, `TRIPLES_PER_T`, `DRAW_BUDGET`.
Terminals: `RECOVERY_MAX`, `CHANCE_TOL`, `BAND_MIN_T`.

Nine cells. Every one is signed before any triple exists, and no audit output
may revise any of them; revision requires a new version of this ticket and
fresh generator roots.

## 10. Negative authorization

Authorizes one throwaway measurement script after protocol acceptance and
author signature, and nothing else. No cell, no arm, no learner, no training,
no curriculum, no scientific outcome, no commit to a citable path. Nothing in
this document is a result.
