# Opus 4.8 X-line review: Philosophia Levels 1-3 claim graph

You are the adversarial X-line reviewer of Fable 5's proposed correction to
the Philosophia programme. This is a pre-outcome scientific design review.
Do not write code, choose unsupported numerical thresholds, create a lock, or
predict a positive outcome.

## Read first

1. `reviews/fable_next_levels_claim_graph_prompt.md`
2. `reviews/fable_levels1_3_claim_graph.md`
3. `ROADMAP.md`
4. `inheritance/line13_philosophia_map.md`
5. `canonical/CLAIM_LEDGER.md`
6. `canonical/KILL_MATRIX.md`
7. `canonical/RESULTS_CANONICAL.md`
8. `essay/climbing-the-wall-of-experience.md`
9. `experiments/level_1_contact/README.md`
10. `experiments/level_2_experience/README.md`
11. `experiments/level_2_5_path_credit/README.md`
12. `inheritance/line12_same_wall/LINE12_MAP.md`
13. `references/LITERATURE_MAP.md`

Repository state: Level 0 is earned and valid, but is platform evidence only.
No Level 1+ outcome exists. Fable's document is uncommitted and explicitly
returns `REVISE_PROGRAMME`.

## Review objective

Decide whether Fable's revised DAG, yoked-transplant Level 1, world contract,
and five-arm Level 2 are scientifically closed enough for Kirill to sign the
programme amendments and begin a bounded Level 1 design.

Attack the strongest version of the design. Do not reject it merely because
implementation details remain open, but do reject any ambiguity that could
change the causal estimand, truth table, or interpretation after outcome.

## Required attacks

### X1. Claim graph and verdict semantics

- Is R1 correct that `ACTIVE <= YOKED` kills chosen contact only, while
  first-hand static contact can still satisfy the programme?
- Does `PROOF_BOUNDED = C2 AND C3 AND C4` match the five-clause programme, or
  does demoting C1 or C5 silently weaken the essay's strong claim?
- Are `FALSIFIED_AT_C2`, `FALSIFIED_AT_C4`, and the boundary verdicts mutually
  exclusive and exhaustive under equivalence/UNKNOWN cases?
- Does an E-arm result comparable to C invalidate C2 itself, or only the
  interpretation of C2 as truthful-ledger experience?
- Are `BOUNDARY_WEIGHTS_ONLY` and `BOUNDARY_LEDGER_SUFFICIENT` logically
  compatible with the first-hand-contact clause?

### X2. Yoked-transplant identifiability

Formalize the proposed estimand and test whether the construction identifies
the effect of instance-adaptive coupling.

In particular audit:

- sign convention: lower budget-to-truth is better, while the document also
  writes `ACTIVE > YOKED`;
- stopping/censoring: if ACTIVE reaches truth early, how is a full fixed-length
  query sequence produced for its YOKED partner without outcome-dependent
  truncation or post-solve policy drift?
- dependency: YOKED(i) consumes ACTIVE(sigma(i)), so instance contrasts are
  linked around derangement cycles; determine the actual variance unit and
  whether ordinary within-instance paired inference is invalid;
- whether query geometry is matched per instance, per stratum, or only as a
  global multiset, and what claim each matching level licenses;
- whether answer balance is a legitimate mediator or an easy-label route that
  defeats the requested estimand;
- whether the claim that YOKED transcripts are "generated before outcome" is
  true, or should be replaced by pre-specified sequential generation;
- whether a fixed derangement is enough, and how it must respect world strata;
- exact acquisition-rule requirements: candidate pool, uncertainty definition,
  tie-breaking, duplicates, budget exhaustion, and forbidden oracle access.

State the smallest repair if yoking is salvageable. If it is not, propose the
smallest identifiable replacement.

### X3. World and cross-presentation contract

Audit the mathematical ontology and information surface:

- the text starts with finite abelian groups, then introduces dihedral groups
  and broken-axiom systems;
- `Z/n x Z/m` is restricted to coprime pairs, which are abstractly cyclic;
- the stated `{R,L}` / `{S,T}` grammar does not yet define a dihedral
  presentation or its inverses;
- an algebraic word/EQ interface and a Cayley interface with anonymous vertex
  IDs or exposed edges may reveal different amounts of truth at different
  costs;
- stable vertex IDs could make equality directly observable;
- semantic bijection of two presentations is necessary but not sufficient to
  show learned transfer;
- transferring one learner between token and graph modalities may conflate
  structural transfer with adapter/architecture migration.

Require one precise candidate contract small enough to enumerate. Say whether
the current contract is a freeze candidate or only a direction.

### X4. Level 2 five-arm interpretation

Check whether A-E isolate forward shortening, weights, truthful ledger, and
false-ledger placebo without inherited-example or contact-budget confounds.
Specify the indispensable contrasts or interactions. Audit the meaning of D
(`fresh + truthful ledger`), the construction of E, arm-specific first-hand
contact, replay budgets, and the claim that all arms use identical contact.

### X5. Lock order and negative space

Check scout validity, escrow generation/custody order, ciphertext/hash binding,
contact-mode branching after Level 1, and the claim that Level 2 can be largely
specified before that branch. Identify every item that must be closed before
implementation, before scout, before lock, and before outcome.

## Required output

Write to `reviews/opus_levels1_3_claim_graph_review.md`. Use exactly one:

- `CLAIM_GRAPH_ACCEPTED`
- `REVISE_CLAIM_GRAPH`
- `REJECT_IDENTIFIABILITY`
- `BLOCKED_WORLD_CONTRACT`

Then provide: findings ordered Critical/Major/Minor; answers X1-X5; exact
