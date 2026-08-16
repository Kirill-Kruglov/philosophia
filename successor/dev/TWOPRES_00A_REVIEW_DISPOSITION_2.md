# TWOPRES_00A — disposition of the second protocol review

Status: `TICKET_00A_SUPERSEDED_BY_00A_V2`

Input: `TWOPRES_00A_PROTOCOL_REVIEW_SOL.md`, verdict
`TWOPRES_00A_PROTOCOL=REVISE`, dispatch valid at `92f8f8d`.

## Disposition table

| finding | disposition |
|---|---|
| C1 — `R1` not proven to present the sealed `M` | **ACCEPT THE DEFECT, REPLACE THE REPAIR.** The isomorphism gap is removed rather than certified: see below. |
| C2 — `D-1` quotients alphabet symmetry but not `Aut(M)` | **ACCEPT, AND PROMOTE.** This is an identifiability result about the programme, not only a ticket repair: see below. |
| C3 — unclear whether baselines see pair labels | **ACCEPT.** `UNPAIRED_STREAM_CORPORA` / `SEALED_PAIR_EVAL` split adopted verbatim. The consequence the review implies but does not state is also adopted: methods are permitted a **bounded rewriting search in their own presentation**, budgeted and reported. Without it no label-free method can decide a pair at all, and the ticket's "never solve a word problem" was self-contradictory. |
| M1 — upward-transfer claim unjustified | **ACCEPT IN FULL.** The asymmetry paragraph is deleted, not weakened. It asserted a monotone simplification with no argument — the same unearned-claim pattern this programme's reviews exist to catch, made by the ticket's own author. Every terminal is now scoped to the exact materialized family, `BAND_CANDIDATE_FOUND` included. |
| M2 — materialization still incomplete | **ACCEPT.** All nine named gaps become frozen clauses or author cells. |
| M3 — cascade not a total function | **ACCEPT.** `r_m(t)`, `r*(t)` and the band condition defined; `CURVE_NON_MONOTONE_UNRESOLVED` renamed `NO_CONTIGUOUS_BAND_UNRESOLVED`, since non-monotonicity is not itself a defect. |
| M4 — scope failures have no terminal | **ACCEPT.** Two terminals added above D0; the 90-minute ceiling is defined as total across both fresh executions. |
| M5 — "settles at every `t`" contradicts M3/M4 | **ACCEPT.** Enumeration settles only the `t = 0` cosmetic renaming; for `t > 0` the partial map is a heuristic, not the correspondence. Written as an explicit boundary. |

**Cut to pay for the additions:** D1a method 3 (co-occurrence-embedding
nearest neighbour) moves to 00b. It was the weakest of the three and carried
every embedding hyperparameter the review flagged as undefined. Removing it
retires a whole class of author cells and keeps the 120-line cap credible.

## C1: remove the gap instead of certifying it

The review is right that relations merely *true* in `M` may present a larger
monoid, in which case the scorer's labels encode information absent from the
streams and D1a measures a hidden channel.

Both proposed repairs certify an isomorphism after the fact. The cheaper move
is to make the gap impossible:

> **Do not sample `M` and hope `R1` presents it. Sample `R1` in band, run
> bounded Knuth–Bendix completion, and accept the triple only if completion
> terminates with a finite complete system whose element count is in band.
> `M` is then *defined* as what `R1` presents.**

There is no isomorphism claim left to prove. Normal forms give equality and
inequality as ground truth on both polarities, `|M|` is exact, and M1/M2
derivability and redundancy witnesses reduce to normal-form comparison — which
also closes the review's remark that those moves lacked witnesses.

**Recorded tension.** `WALLB_DESIGN_MEMO_11` §7.2 forbids convergent
presentations, because convergence trivializes finding derivations. That
constraint is about a *learner searching*. Here convergence is used only by
the sealed scorer, and no party under test ever sees it. 00a is therefore
consistent with the Wall B rule. **00b is not, by default:** the moment a
learner searches for derivations, ground truth can no longer come from a
convergent system, and 00b must specify a different mechanism. This is a
blocker on 00b, registered now so it is not discovered late.

## C2: this is a finding, not only a repair

If `α ∈ Aut(M)`, composing the second evaluation map with `α` leaves both
unpaired streams byte-identical and changes the cross-stream labels. So exact
element correspondence is **unidentifiable up to `Aut(M)`** — by construction,
for any method, however good.

That is a concrete, computable instance of the boundary this programme has
been circling in prose: a learner earns the world only up to the equivalence
class its interface admits. Here the class has a name and a size.

Repair adopted, between the review's two options: compute `Aut(M)` from the
sealed Cayley table, admit a triple only if `|Aut(M)| <= AUT_MAX`, and score
over the whole orbit. Restricting to trivial `Aut(M)` would be simpler but
would silently select for rigid monoids; scoring over an unbounded orbit would
be uncapped. The realized `|Aut(M)|` distribution is reported in D0 regardless
of outcome, because it is the size of the boundary and is worth knowing even
if the cell dies.

## Stop rule on the review loop itself

Two `REVISE` verdicts have now been returned, both on real defects, and the
object has changed twice (alphabet → element correspondence; sampled `M` →
completion-defined `M`). That is convergence, not circling. But the loop needs
a declared floor, and nothing in the programme has one:

> **If the third protocol review returns `REVISE` on newly discovered Critical
> items rather than on the repairs of this disposition, the line is closed as
> `NOT_CHEAPLY_AUDITABLE` and no further paper repair is authorized.**

An object that cannot be typed in three bounded passes is not a candidate for
a 120-line audit, whatever its scientific appeal. Closing it then is the
result.

## What this disposition does not authorize

No implementation, no triple, no completion run, no author cell chosen. 00a-v2
requires its own protocol acceptance before any cell may be signed.
