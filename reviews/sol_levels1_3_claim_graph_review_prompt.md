# GPT-5.6 Sol Y-line review: Philosophia Levels 1-3 causal and statistical design

You are the independent Y-line reviewer of Fable 5's proposed Philosophia
claim graph. Focus on causal identification, statistical units, contrast
algebra, and the minimum evidence needed for a bounded claim. This is
pre-outcome. Do not write code, invent effect sizes, choose outcome-friendly
thresholds, create locks, or predict success.

## Read first

1. `reviews/fable_next_levels_claim_graph_prompt.md`
2. `reviews/fable_levels1_3_claim_graph.md`
3. `ROADMAP.md`
4. `canonical/CLAIM_LEDGER.md`
5. `canonical/KILL_MATRIX.md`
6. `canonical/RESULTS_CANONICAL.md`
7. `experiments/level_1_contact/README.md`
8. `experiments/level_2_experience/README.md`
9. `experiments/level_2_5_path_credit/README.md`
10. `inheritance/line12_same_wall/LINE12_MAP.md`
11. `references/LITERATURE_MAP.md`

Level 0 is valid platform evidence only. No Level 1+ outcome exists. Fable
returns `REVISE_PROGRAMME` and proposes ACTIVE/YOKED/RANDOM-STATIC at Level 1,
then five arms A-E at Level 2.

## Y-line tasks

### Y1. Potential-outcome estimand for ACTIVE versus YOKED

Write the estimand precisely with lower budget-to-truth better. Define the
intervention, world-instance distribution, learner seed schedule, maximum
budget, censoring rule, and what is held fixed. Determine whether yoking
ACTIVE(sigma(i)) into YOKED(i) estimates instance-adaptive coupling or a blend
of coupling, policy/world mismatch, and hidden stratum differences.

Audit these specific risks:

- fixed derangement induces a dependency graph/cycles between observations;
- paired contrasts by instance may understate variance;
- early ACTIVE success can truncate the donor sequence;
- multiple ACTIVE donors or derangements may be needed for stable inference;
- query tokens can be valid but have different semantic difficulty across n,
  group families, or presentation strata;
- global query-multiset equality does not imply per-world geometry matching;
- label balance and answer entropy are declared mediators, but the endpoint
  must prevent an easy-label victory;
- ties, non-solves, ABSTAIN, repeated queries, and budget exhaustion need
  deterministic treatment.

Give either a corrected analysis plan or a reason the construction is not
identified. Separate design validity from sample-size adequacy.

### Y2. Variance scout and sample-size logic

Fable proposes a development-only variance scout that does not compare arms.
Assess whether that can estimate the variance of the paired causal contrast.
Specify what a scientifically non-outcome calibration may inspect, what must
remain hidden, and what can justify N3/N4 without pretending to provide power
from no effect-size basis. State the correct experimental unit and variance
unit under world blocks, seeds, repeated checkpoints, and derangement cycles.

### Y3. Endpoint and equivalence semantics

Compare the two proposed solve criteria:

- order-probe persistence;
- held-out EQ prediction persistence.

Test their validity across cyclic, product, dihedral, broken-axiom, and Cayley
worlds. Check class imbalance, trivial inequality prediction, calibration,
ABSTAIN, right censoring, and family-specific comparability. Recommend a
primary endpoint form, not unsupported numerical thresholds. Define the role
of superiority, non-inferiority/equivalence margins, quorum, UNKNOWN, and
multiple-family aggregation.

### Y4. Five-arm Level 2 contrast algebra

Represent A-E as interventions on transferred weights and ledger type. Decide
whether Fable's listed pairwise contrasts identify:

- total retained-history effect;
- weights channel;
- truthful-ledger incremental effect;
- ledger-alone portability;
- false-ledger/placebo effect;
- interaction between weights and ledger.

Check whether `C > E and E <= B` is sufficient for C4, whether `E ~= C`
should erase the empirical C2 effect or only its causal interpretation, and
whether D can support any first-hand-experience claim. Require matched query,
replay, compute, token, and memory budgets. State the minimal preregistered
contrast family and multiplicity/hierarchical decision order.

### Y5. C3 transfer and claim scope

Determine what comparison establishes cost reduction across algebra and Cayley
presentations without treating free destination agreement as transfer. Audit
whether the two interfaces expose equal information and cost, and whether a
modality adapter becomes an uncontrolled treatment. Specify the narrowest
claim licensed by positive C2/C3/C4 and the correct boundary claim when C3
fails.

### Y6. External anchors

Using primary sources where useful, identify only literature facts that alter
the design materially: active-learning evaluation under adaptive sampling,
yoked controls/dependent randomization, survival endpoints with censoring,
finite-group learning, or representation-transfer controls. Distinguish a
source-supported requirement from your own design recommendation. Do not turn
the review into a broad literature survey.

## Required output

Write to `reviews/sol_levels1_3_claim_graph_review.md`. Use exactly one:

- `CAUSAL_DESIGN_ACCEPTED`
- `REVISE_CAUSAL_DESIGN`
- `YOKED_ESTIMAND_NOT_IDENTIFIED`
