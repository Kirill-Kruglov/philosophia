# Sol Y-line review - Levels 1-3 causal and statistical design

Reviewer: Sol, independent Y-line reviewer. Scope: Fable 5's proposed
Philosophia Levels 1-3 claim graph, with focus on causal identification,
statistical units, contrast algebra, endpoint semantics, and bounded claim
licensing. This is pre-outcome. I did not write code, create locks, run scouts,
choose outcome-friendly thresholds, invent effect sizes, or predict success.

## Verdict

REVISE_CAUSAL_DESIGN

Fable's programme graph is close enough to repair, and the demotion of Level 1
from programme-kill to a contact-choice boundary is scientifically correct.
However, the current ACTIVE/YOKED construction does not yet identify the
claimed instance-adaptive coupling effect; the variance scout cannot estimate
the variance of the paired contrast as described; the primary solve endpoint is
not fixed across world families; and the Level 2 contrast algebra needs a
stricter hierarchy before any Level 1 lock.

## Critical Findings

**C1 - The proposed single-derangement YOKED arm is not yet an identified
estimand for instance-adaptive coupling.** Fable's YOKED(i) receives the ACTIVE
query sequence from sigma(i), with answers from i. That does break target-answer
adaptivity, but with a single fixed derangement it also imports donor hidden
stratum, donor world geometry, donor policy trajectory, donor censoring, and
derangement-cycle dependence. The contrast estimates "target-adaptive ACTIVE
versus one off-target active transcript" conditional on the chosen derangement,
not a stable population effect of adaptive coupling. Mandatory edit: define the
Level 1 estimand as a potential-outcome contrast under a target-specific ACTIVE
policy versus a stratum-matched donor-active transcript distribution, and
implement either multiple locked derangements or multiple donor transcripts per
target within exact world-family/presentation strata. Analyze at the world-block
level with cycle-robust or randomization-based uncertainty, not as independent
paired observations.

**C2 - Donor early success cannot truncate YOKED.** If ACTIVE stops when its
donor solves, then YOKED inherits donor solve time as transcript length. That
turns a target comparison into a mixture of donor difficulty and target
difficulty. Mandatory edit: all ACTIVE donor transcripts used for yoking must
continue to the common maximum oracle budget under the frozen acquisition rule
even after the donor has solved, or must be deterministically padded by a
predeclared non-informative rule. The scientific endpoint may be censored at
the target budget, but transcript availability cannot depend on donor outcome.

**C3 - The primary solve endpoint is unresolved and currently vulnerable to
family artifacts.** Order-probe persistence is meaningful for cyclic order
worlds but does not carry unchanged to product groups, dihedral groups,
broken-axiom worlds, or anonymous Cayley presentations. Held-out EQ prediction
is more portable but is vulnerable to class imbalance, trivial inequality
prediction, calibration failure, and ABSTAIN gaming. Mandatory edit: choose one
primary endpoint before any scout that informs N3/N4. My recommendation is
budget-to-certified-solve: a right-censored time-to-event endpoint whose event
requires persistent performance on an escrowed, family-stratified, class-balanced
EQ panel, plus predeclared calibration/ABSTAIN/confident-lie constraints. Order
probes may remain secondary family diagnostics. Numerical thresholds and
margins remain unresolved until justified pre-outcome.

## Major Findings

**M1 - The Level 1 variance scout cannot estimate paired contrast variance if
it never compares arms.** A development-only scout that inspects only marginal
endpoint behavior can estimate runtime, censoring rate, marginal difficulty,
label balance, and approximate within-arm outcome variance. It cannot estimate
the covariance of ACTIVE and YOKED potential outcomes, derangement-cycle
variance, or the paired contrast variance. Mandatory edit: either label the
scout as feasibility-only and set N3/N4 by conservative precision rules, or run
a development-family contrast scout whose arm comparisons are explicitly
non-outcome, non-citable, and barred from threshold/policy tuning after the
analysis plan is frozen. Do not describe N3/N4 as powered by an effect-size
estimate unless an effect-size basis is predeclared independently.

**M2 - Label balance and answer entropy are mediators, not matching targets, but
the endpoint must stop an easy-label win.** Fable is right to reject equal
realized answer entropy as the matching rule. But if ACTIVE can select a query
region where "not equal" dominates or where one family gives easier labels, it
can win endpoint accuracy without learning structure. Mandatory edit: do not
match realized answers, but evaluate on fixed escrow panels with balanced
YES/NO, word-length, relation-type, family, and presentation strata. Report
answer entropy and label balance as mediators/diagnostics; never let them define
success.

**M3 - Derangement cycles break naive paired variance.** A fixed derangement
creates a dependency graph: i's YOKED transcript is sigma(i)'s ACTIVE transcript,
and cycles share donor policies. Instance-paired contrasts are therefore not
independent even when target worlds differ. Mandatory edit: record the
derangement graph, use cycle/block as a clustering level, and prefer
randomization inference over the locked derangement ensemble. If only one
derangement is used, restrict the claim to that derangement-conditioned
experiment and do not report independent-pair variance.

**M4 - Level 2 C4 contrast algebra is underspecified.** Fable's "C > E and
E <= B" is necessary but not sufficient for the truthful-ledger claim. C4 says
the truthful ledger adds value not carried by weights alone, ledger alone, or a
false ledger. That requires at least: C > B for truthful-ledger incremental
value over transferred weights; C > E and E <= B for false-ledger/placebo
control; D versus A to quantify ledger-alone portability; and a predeclared
interpretation for D approximately C. Mandatory edit: freeze the minimal
contrast family and hierarchy:

- primary full-package effect: C versus A;
- weights channel: B versus A;
- truthful-ledger increment with weights: C versus B;
- truth versus false ledger, conditional on weights: C versus E;
- false-ledger placebo: E versus B;
- ledger-alone portability: D versus A;
- complementarity/interaction: (C - B) versus (D - A), descriptive unless
  powered and preregistered.

**M5 - C3 transfer must be a cost-reduction contrast within the destination
interface.** Algebra-to-Cayley destination agreement is free from the
semantics-preserving map and licenses no transfer claim. The needed comparison
is budget-to-certified-solve in the Cayley presentation for retained-history
arms versus scratch Cayley baselines under equal information and cost. Mandatory
edit: specify whether a modality adapter exists. If yes, it is a treatment
component unless it is frozen before outcomes and given equally to every arm,
including scratch controls. If Cayley exposes vertex IDs, graph neighborhoods,
or state adjacency not available in the algebra interface, equal-cost transfer
is not identified.

**M6 - Equivalence, non-inferiority, quorum, and UNKNOWN semantics cannot be
left informal.** "Approximately equal" and "no worse" are claims, not
descriptions. Equivalence/non-inferiority require a predeclared margin and a
test/interval rule; failure to show superiority is not equivalence. Mandatory
edit: use superiority for primary positive claims, reserve equivalence or
non-inferiority for explicitly margin-locked boundary claims, and define
UNKNOWN as neither success nor boundary. Aggregate across families only through
a hierarchical rule: first same-presentation C2, then destination-interface C3,
then ledger causality C4, with family-specific failures reported as boundaries
rather than averaged away.

## Minor Findings

**m1 - The canonical roadmap still says "equal answer entropy."** The Level 1
README and kill matrix still carry the older equal-entropy framing. If Fable's
yoked redesign is adopted, those files need a loud signed amendment before
Level 1 lock.

**m2 - Query-token equality does not imply semantic difficulty equality.** A
word of the same length can have different diagnostic value across n, product
families, dihedral presentations, broken axioms, and Cayley graphs. This should
be a reported mediator and stratification variable, not assumed matched by the
query grammar.

**m3 - Repeated queries need deterministic cost and information rules.**
Repeated queries should cost one oracle unit each, produce the same oracle bit,
and not be silently deduplicated for endpoint credit unless deduplication is an
explicit learner behavior available to all arms.

**m4 - D can support ledger portability, not first-hand experience by itself.**
A fresh learner plus truthful ledger may prove the ledger text is useful. It
does not show that the destination learner earned the experience through its own
contact path.

## Y1. Corrected ACTIVE versus YOKED Estimand

Let W be a world instance drawn from the locked world-instance distribution P,
including family, parameter stratum, presentation, and query grammar. Let r be
a learner seed from the locked seed schedule. Let B be the maximum oracle
budget. Define T_a(W,r) as the budget-to-certified-solve under intervention a,
with observed outcome X_a = min(T_a, B) and event indicator delta_a = 1 if the
solve event occurs by B and 0 otherwise. Lower T is better; delta = 0 is
right-censored, not a solve at B.

The ACTIVE intervention is the frozen acquisition rule coupled to learner state
and answers from W. The corrected YOKED intervention draws one or more donor
ACTIVE query sequences from independently assigned donor worlds in the same
locked stratum, using full-B transcripts independent of donor solve time, and
applies those query tokens to W with W's own oracle answers. Held fixed:
learner architecture, initialization distribution, seed schedule, oracle
budget, evaluation panel, world sampler, presentation, grammar, replay rules,
and censoring rule.

The primary estimand should be a restricted mean budget-to-truth contrast or a
survival/event contrast up to B:

Delta_choice = E_P,r[RMST_YOKED(B) - RMST_ACTIVE(B)]

with positive Delta meaning ACTIVE reaches truth with lower budget. If the team
instead uses mean observed budget with non-solves set to B, call it a bounded
cost score, not an uncensored time-to-solve. Either way, define ties,
non-solves, ABSTAIN, repeated queries, and budget exhaustion deterministically:
ties at the same budget are zero contrast; non-solves are censored or assigned
the locked bounded-cost score; ABSTAIN is never a correct solve event; repeated
queries count cost; exhaustion without solve is censored/UNKNOWN, not success.

As currently written, ACTIVE(sigma(i)) into YOKED(i) estimates a blend of
adaptive coupling, policy/world mismatch, hidden stratum mismatch, donor
censoring, and derangement-cycle dependence. With the corrections above, it can
estimate the narrow effect of target-specific coupling against the marginal
active transcript distribution for the same stratum. That is a valid causal
question, but narrower than "active learning is better than static data."

## Y2. Variance Scout and Sample-Size Logic

Scientifically non-outcome calibration may inspect development-only runtime,
artifact size, endpoint computability, censoring frequency, family difficulty
spread, answer entropy, label balance, ABSTAIN/confident-lie rates, and marginal
outcome variance under declared arms if the dev family is excluded from
outcome. It must not inspect escrow outcomes, tune thresholds on arm differences,
choose favorable families, change the acquisition rule after seeing comparative
results, or report dev contrasts as evidence.

If the scout does not compare arms, it cannot estimate paired causal-contrast
variance. It can justify N3/N4 only by feasibility and precision logic:
minimum number of independent world blocks, maximum acceptable censoring,
minimum cycles/derangements for stable randomization inference, and resource
ceilings. It cannot honestly claim conventional power absent a pre-outcome
effect size.

The experimental unit and variance unit are world block or world instance
depending on the locked sampler. Seeds crossed within a world are repeated
measurements, not independent replications. Checkpoints are time observations,
not units. Query rows are not units. Derangement cycles are dependency clusters.
For Level 2, the block is the unseen world-family sequence/presentation bundle;
the five arms inside it are paired interventions.

## Y3. Endpoint and Equivalence Semantics

Order-probe persistence is attractive for cyclic groups because order is a
direct hidden parameter. It weakens across product groups, dihedral groups,
broken-axiom worlds, and Cayley presentations because no single "order" probe
has the same semantic load in all families. It should be secondary unless the
world contract explicitly defines a family-specific solve certificate and a
hierarchical family rule.

Held-out EQ prediction persistence is more general, but only if the escrow
panel prevents class imbalance and trivial inequality prediction. The panel
must be balanced and stratified by family, relation type, word length, and
presentation; require calibration; log confident lies separately from honest
ABSTAIN; and treat right-censoring as a time-to-event issue. The endpoint should
not be a raw pooled accuracy over an imbalanced panel.

Recommended primary endpoint: budget-to-certified-solve with persistence on
the balanced escrow EQ panel plus locked calibration/ABSTAIN constraints.
Superiority claims compare this endpoint between arms. Equivalence or
non-inferiority requires predeclared margins and interval rules. Quorum should
be over independent world blocks/families, not seeds or checkpoints. UNKNOWN
means insufficient evidence and cannot be converted to success or boundary.
Multiple-family aggregation should be hierarchical and closed: no later family
can rescue a failed earlier necessary claim unless the truth table names that
failure as a boundary.

## Y4. Five-Arm Level 2 Contrast Algebra

Represent the five arms as interventions:

| Arm | Weights | Ledger | Scientific role |
|---|---|---|---|
| A | scratch | none | destination scratch baseline |
| B | transferred | none | weights channel |
| C | transferred | truthful sparse ledger | full retained-history candidate |
| D | scratch | truthful sparse ledger | ledger-alone portability |
| E | transferred | false/statistics-matched ledger | placebo and traceability control |

The listed pairwise contrasts identify the following only if query, replay,
compute, token, memory, and oracle budgets are matched:

- total retained-history effect: C - A;
- weights channel: B - A;
- truthful-ledger incremental effect with weights: C - B;
- ledger-alone portability: D - A;
- false-ledger/placebo effect: E - B;
- truth-specific ledger effect with weights: C - E;
- interaction/complementarity: (C - B) - (D - A), descriptive unless
  preregistered as primary.

`C > E and E <= B` is not sufficient for C4 because it does not establish that
C exceeds B or how D behaves. `E ~= C` should not erase the empirical C2 fact
that C beat A, if that occurs; it erases the causal interpretation as truthful
experience and reclassifies the result as placebo/format-sensitive unless a
separate contrast rescues it. D cannot support a first-hand-experience claim:
it can show a truthful ledger is portable as text, not that the destination
learner's own path created the retained structure.

Minimal preregistered contrast hierarchy:

1. C2 full package: C superior to A on same-presentation escrow.
2. C3 transfer: C superior to A on destination presentation.
3. C4 traceability: C superior to B and E, E not superior to B by the locked
   margin/rule, and D interpreted as a boundary coordinate.
4. Channel reporting: B-A, D-A, E-B, and interaction estimates with multiplicity
   controlled inside this family.

## Y5. C3 Transfer and Claim Scope

Cost reduction across algebra and Cayley presentations is established only by
destination-interface budget-to-certified-solve contrasts: retained-history arms
versus scratch controls inside Cayley, under the same hidden object family and
equal oracle cost. Agreement between algebra and Cayley answers is not transfer;
it is the semantics-preserving theorem doing free work.

The two interfaces must expose equal information. If algebra provides only word
tokens and EQ while Cayley exposes vertex IDs, adjacency, degree, or reachable
state neighborhoods, then interface is an uncontrolled treatment. If a modality
adapter is used, it must be frozen before outcomes, trained without escrow
answers, and supplied equally to A-E; otherwise it becomes the real transfer
mechanism.

If C2/C3/C4 are positive, the narrowest licensed claim is: in the locked finite
algebraic/geometric world family, retained contact-derived weights plus a
truthful sparse ledger reduced oracle budget to certified truth on unseen
instances and on a semantics-preserving presentation change, beyond scratch,
weights-only, ledger-only, and false-ledger controls. If C3 fails after C2 is
positive, the correct boundary is within-presentation retained experience, not
representation-transfer experience.

## Y6. External Anchors That Matter

These sources alter design requirements; they do not prove Philosophia.

- Active learning literature, including Cohn, Atlas, and Ladner 1994 and the
  Settles 2009 survey mapped in `references/LITERATURE_MAP.md`, supports the
  premise that query choice can reduce label complexity under assumptions. It
  does not support equal realized answer entropy as an information match.
  Requirement: evaluate on a fixed target/escrow distribution and treat query
  distribution as part of the intervention.
- Potential-outcome/randomization principles from Neyman/Rubin imply that the
  treatment must be a manipulable regime and that interference must be modeled.
  Requirement: the derangement graph/cycles are part of the design, not a
  nuisance that paired t-tests can ignore.
- Kaplan and Meier 1958 and Cox 1972 make budget-to-truth a standard
  right-censored duration problem when runs can exhaust budget unsolved.
  Requirement: non-solves are censored or handled by a predeclared restricted
  mean/bounded-cost estimand, not silently tied with late solves.
- Equivalence testing practice, including Schuirmann's two-one-sided-tests
  framework, makes "no meaningful difference" a margin-locked claim.
  Requirement: `~=` and `<=` in the proof table need numerical margins and
  interval/test rules before outcome.
- The Level -1 transfer anchors show arithmetic transfer exists in selected
  settings but OOD transfer can fail. Requirement: C3 needs a destination
  scratch baseline and equal-interface controls; source/destination agreement
  is not evidence.

## Mandatory Edits Before Level 1 Lock

1. Replace equal-answer-entropy language in the README, kill matrix, and Level 1
   draft with the corrected yoking estimand.
2. Define full-budget donor transcript generation and deterministic padding.
3. Use multiple locked derangements/donors or explicitly restrict inference to
   a derangement-conditioned result.
4. Freeze the primary solve endpoint, censoring rule, ABSTAIN rule, repeated
   query rule, and balanced escrow evaluation panel.
5. State that the variance scout cannot estimate paired contrast variance
   unless it compares development arms; choose conservative precision or a
   development contrast scout.
6. Freeze Level 2's contrast hierarchy, margins/equivalence semantics, and
   multiplicity order before any Level 1 outcome.
7. Specify C3 equal-interface controls and modality-adapter handling.

## Authorized Scope After Revision

After these revisions, implementation may proceed as a reviewed pre-outcome
candidate. Kirill may not sign a Level 1 lock until the amended causal design,
endpoint, variance plan, and canonical route-map files agree. Level 2 code may
be drafted from the closed behavioral spec, but Level 2 execution must remain
blocked until the Level 1 decision fixes the contact mode. No long-run Level
1+ command should be issued under the current design.

## Residual Forbidden Inferences

Level 1 cannot prove manufactured experience; it can only locate whether
target-adaptive query choice matters beyond off-target active geometry. Level 2
cannot claim transfer from destination agreement, ledger causality from C > A
alone, or first-hand experience from D alone. C5 path credit is mechanism
strength, not required for the basic bounded proof. C6 diagnostics cannot
decide, rescue, or veto the programme. No result generalizes beyond the locked
world families, learner, budgets, endpoints, contact rule, and presentations.
