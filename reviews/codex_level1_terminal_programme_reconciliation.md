# Codex reconciliation — Level 1 terminal programme review

Date: 2026-07-18

This note preserves Fable 5's review unchanged while reconciling its visual
inventory with the reviewed atlas commit.

## Accepted findings

The terminal synthesis, route comparison, negative space, and recommendation
are internally consistent with the canonical record. The three optional wording
notes MN-1 through MN-3 were adopted without changing any scientific status or
numeric result.

## Visual-inventory correction

The review says that the holdout matrix, resource profile, and proof-layer DAG
are missing from atlas commit `3ca5f3e`. They were already present in that exact
commit:

- `docs/index.html`: Figure 2 is the five-row H1-H5 escrowed holdout matrix,
  with H4 marked as the adverse clean-room flag.
- `docs/index.html`: the Level 1 section reports the 35.820 h trajectory
  aggregate, 49.782 GiB peak RSS, and 24.575 MiB checkpoint estimate, explicitly
  as engineering-only evidence with no synthetic series.
- `docs/index.html`: the claim section contains the `PROOF_CORE` /
  `PROOF_STRONG` DAG, with C6 annotation-only and every scientific node marked
  unavailable, blocked, or untested rather than negative.

The atlas therefore already covers all seven figure candidates in the review.
No new evidence figure is required for the minimum release. The hero wording
was changed from a feasibility "wall" to the Workshop stopping at its own
"gate", preserving the essay's narrower use of wall.

## Route status

Fable recommends Route B. This note records the recommendation but authorizes no
continuation. Route selection, C1's standing, successor device policy, and any
new-line charter remain Kirill's author decisions.
