# Essay post-reconciliation formal/evidential review — GPT-5.6 Sol V1

## Findings

### Critical

None.

### Major

None. The current publication surface contains no concrete Critical or Major
formal, statistical, citation, chronology, or evidential defect within the
bounded review scope.

### Minor

None requiring publication repair.

## Integrity gate

The governing handoff recomputes to
`a9ddde576e47608010ba1f4dd672de00db966d9ca8fbc7dab92a810bb2ed18cc`.
I recomputed every publication-surface and evidence pin in handoff §§1 and 5;
all match. The checked-out commit is exactly
`ba3718cb9364696dc93b0565c42efcf5c6757d80`. The review object was therefore
stable and the integrity gate is open.

## Formal and evidential determinations

### 1. Hamilton-Zero

The statements at `essay/climbing-the-wall-of-experience.md:47-64` are
supported, with the ordinary distinction between an authors' empirical report
and independent reproduction preserved.

- The authors report approximately 0.5 billion variational parameters,
  pretraining over hundreds of thousands of Hamiltonians, variation in
  topology, size, interaction type and strength, held-out evaluation, and
  larger-system fine-tuning/evaluation. Those statements appear in the
  [paper and full text](https://arxiv.org/abs/2608.11911); they are reported
  results, not facts independently reproduced by this review.
- Independently checkable release facts do hold: the public
  [source repository](https://github.com/simulacra-research/HamiltonZero)
  contains the model workflows and training/evaluation source, and the
  [checkpoint repository](https://huggingface.co/simulacra-research/HamiltonZero/tree/main/weights)
  contains `hamiltonzero_v1.eqx`.
- Neither the paper nor the released workflow reports the complete reciprocal
  comparison in which exact learner twins receive own-selected versus matched
  donated contact. Hamilton-Zero amortizes learning over generated systems and
  evaluates held-out systems; it does not isolate the Philosophia selection
  estimand. The denial at lines 63-64 is therefore correct.

The comparative phrase at lines 61-62 is an explicitly argumentative judgement
about scale, not a claim of independent replication. Nothing in this passage
turns Hamilton-Zero into evidence for Philosophia.

### 2. Minimo and the meaning of fixed-panel transfer

The description at `essay/climbing-the-wall-of-experience.md:991-1001` is
jointly faithful to the primary paper and the local terminal.

The [Minimo paper](https://papers.neurips.cc/paper_files/paper/2024/file/4b8001fc75f0532827472ea5a16af9ca-Paper-Conference.pdf)
describes one model jointly learning conjecturing and proof search, starting
from axioms, with experiments in propositional logic, arithmetic and group
theory. It also evaluates agents trained on self-proposed conjectures against
human-written Kleene and Natural Number Game theorems that were not targeted in
training. Locally, `successor/dev/PHASE1_TERMINAL_18.md:42-47` records one
unseeded repository-default CPU-debug realization in which checkpoint 1 reduced
capped entered proof-search work on a fixed 30-item Kleene panel relative to
checkpoint 0, while expressly denying theorem-population, seed-stability,
ACTIVE/YOKED, and general-Philosophia inference.

Accordingly, “its fixed-panel transfer measured” is admissible only in its
immediate narrow sense: a saved post-training checkpoint changed work on that
fixed external panel. Lines 997-1001 immediately enforce that scope. The phrase
does not become the programme's registered cross-world, cross-family, or
presentation transfer and does not imply an inferential estimate beyond those
30 items.

### 3. TWOPRES automorphism claim

The sentence at `essay/climbing-the-wall-of-experience.md:968-974` follows from
the closure argument.

Let the two presentation evaluators be
`e1: Sigma1* -> M` and `e2: Sigma2* -> M`. For any `a` in `Aut(M)`, replacing
`e2` by `a o e2` leaves every byte in each unpaired stream unchanged. It also
leaves all within-second-presentation equality information unchanged because
`e2(u)=e2(v)` iff `a(e2(u))=a(e2(v))`. But the cross-presentation label
`e1(u)=e2(v)` is changed to `e1(u)=a(e2(v))`. Thus unpaired observations cannot
distinguish correspondence maps in the same `Aut(M)` orbit. If `Aut(M)` is
trivial, the quotient reduces to exact identification; “at best up to
`Aut(M)`” already includes that case.

The essay keeps every necessary quantifier and boundary: two presentations of
one finite monoid, the unpaired-stream interface, and a mapped development
result rather than an experiment. It neither universalizes to representations
in general nor weakens the proved obstruction.

### 4. Successor chronology

The essay, `README.md`, `essay/README.md`, and `essay/REVIEW_HANDOFF.md` agree on
the complete chronology:

1. Wall-B library prevalence closed `CLOSED / SPARSE` at 2/40; the distinct
   policy-channel screen reached `SCREEN-VIABLE` at 12/40 and was left unrun.
2. One exploratory Phase-1 Minimo learner ran and was evaluated; it is
   non-citable development.
3. Phase-2 Stage A and Stage-B L0-L3 reached accepted engineering surfaces only.
4. The Stage-R route stopped at the minimum-L4 paper boundary; E2 stopped at
   IDEA_GATE before build.
5. No L4 implementation, Stage-R root, scientific learner/selector execution,
   ACTIVE/YOKED comparison, scientific lock, or scientific outcome followed.

The programme claim remains `OPEN` on all four surfaces.

### 5. Screen counts and Wilson intervals

Using the ordinary two-sided 95% Wilson score interval with `z=1.959964`:

- `x=2, n=40` gives `[0.0138, 0.1650]`, correctly printed as
  `[0.014, 0.165]`;
- `x=12, n=40` gives `[0.1807, 0.4543]`, correctly printed as
  `[0.181, 0.454]`.

The 2/40 wording compares the observed count with the frozen floor of five. The
12/40 wording describes a screen-valid policy carrier; its Wilson lower bound
also exceeds `5/40`. The essay repeatedly labels both as non-citable engineering
screens. Neither count is converted into a scientific efficacy estimate or an
ACTIVE/YOKED outcome.

### 6. Search for evidential leakage

No prohibited route exists in the current essay.

- Engineering acceptance is expressly called “not programme evidence” at
  `essay/climbing-the-wall-of-experience.md:872-904`.
- Failed learner competence is expressly said to add no evidence at lines
  955-966.
- TWOPRES `NOT_CHEAPLY_AUDITABLE` is confined to a non-experimental interface
  boundary at lines 968-974.
- The fixed-panel work reduction is immediately marked non-citable and denied
  cross-world/presentation or ACTIVE/YOKED meaning at lines 991-1001.
- Hamilton-Zero is called a neighbour and expressly denied the matched-donation
  isolation at lines 55-64.

The status table's accepted surfaces and counts are therefore descriptions of
apparatus history, not bridges to the programme claim.

### 7. Global consistency

The reconciliation creates no contradiction with the three conditional endings
at lines 636-695, the conclusion's future conditionals at lines 745-771, “What
this does not show” at lines 935-1010, or the permanent statement at lines
903-904: `REPRODUCED, PLATFORM ONLY -- NO PROGRAMME INFERENCE.` Proof,
falsification, and mapped boundary all remain unchosen. The later evidence
ledger adds status detail without filling a signed scientific slot.

### 8. Delta-dependent citations and names

The Minimo title, system description, domains, and external-panel reading agree
with its primary NeurIPS paper. Hamilton-Zero's name, paper, source, checkpoint,
model scale, and corpus description resolve to current primary objects. The
delta does not depend on a missing or misnamed citation.

## Non-binding plan audit

### Existential asymmetry

The asymmetry in `successor/dev/PROGRAMME_GOAL_AND_REENTRY_PLAN_V1.md:20-38` is
valid. A valid witness can establish existence within its prospectively bounded
world, learner, interface, and compute class. Any finite list of null or failed
feasibility cases leaves an unrestricted existential open because a witness may
lie outside the tested list. A global negative requires a bounded universal
claim tested over its complete domain or a valid impossibility/non-identifiability
argument for the stated class. TWOPRES has the latter form only for its named
interface.

### `PROOF_CORE` priority

The priority is coherent with the signed graph. The signatures and canonical
ledger define `PROOF_CORE = C2 AND C3 AND C4`; C1 and C5 are additions required
for `PROOF_STRONG`, while C6 is only an annotation. Prioritizing the core is
therefore a legitimate cheaper route to the bounded weak witness, provided a
future report continues to reserve unqualified “Proof” and the own-selection
and path-credit claims for `PROOF_STRONG`.

### Re-entry loophole

The plan does not fully prevent another apparatus loop. Section 5 requires eight
properties, including an already-existing host-independent work counter and
executable zero/injected controls (`PROGRAMME_GOAL_AND_REENTRY_PLAN_V1.md:85-89`).
But the operative five-question desk screen at lines 120-131 omits both. A
candidate can therefore return all five literal `YES` answers while still
requiring Philosophia-specific construction of the work ledger and control
instrument after re-entry.

The smallest plan-only correction is to add
`HOST_INDEPENDENT_WORK_COUNTER_ALREADY_EXISTS=YES|NO` and
`ZERO_AND_INJECTED_CONTROLS_ALREADY_EXECUTABLE=YES|NO` to the §7 screen, with
either `NO` ending the screen under the existing no-repair rule. This advisory
finding does not alter the essay verdict and authorizes no work.

EXISTENTIAL_ASYMMETRY_VALID=YES
PROOF_CORE_PRIORITY_COHERENT=YES
REENTRY_GATE_PREVENTS_APPARATUS_LOOP=NO

ACCEPT_ESSAY_POST_RECONCILIATION_FORMAL_V1
