# Level 1 scientific specification draft

Status: `DRAFT_PRE_S_GATE`

This document consolidates the signed Levels 1–3 claim graph into the smallest
Level 1 specification that can be reviewed and implemented without silently
choosing outcome-sensitive numbers. It creates no scout, escrow, lock, or
outcome authorization.

Governing authority, in order:

1. `reviews/LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`;
2. `reviews/fable_levels1_3_claim_graph_v2.md` plus the bounded corrections in
   `reviews/fable_levels1_3_claim_graph_v2_1.md`;
3. `canonical/CLAIM_LEDGER.md` and `canonical/KILL_MATRIX.md`;
4. the eventual Level 1 preregistration and lock, once separately reviewed and
   signed.

If this draft conflicts with a governing signature, the signature wins and the
draft must be revised before use.

## 1. Scientific question and scope

**C1 chosen contact:** within the locked cyclic-world family, learner class,
oracle budget, acquisition rule, and evaluation contract, does coupling query
choice to the target learner's own state and answers reduce
budget-to-certified-solve relative to active query geometry donated by an
independent matched world?

The primary contrast is ACTIVE versus YOKED-GEOMETRY. RANDOM-STATIC locates
whether useful query geometry transfers without target adaptivity.

Level 1 can earn or reject only C1. A negative result yields
`BOUNDARY_CONTACT_CHOICE`; it cannot prove or falsify `PROOF_CORE`, forward
shortening, ledger causality, representation transfer, path credit, or C6.

Scope never exceeds the locked finite cyclic family, learner, grammar, budget,
and acquisition rule. It is not a claim about active learning in general.

## 2. Hidden cyclic world

For each world parameter `n` from a locked sampler range N1:

- hidden states are `0, ..., n - 1`;
- the hidden origin is `0`;
- `R(x) = x + 1 mod n`;
- `L(x) = x - 1 mod n`;
- a word over `{R, L}` is evaluated by a left fold from the origin;
- `EQ(u, v)` returns one bit, true exactly when the two words end at the same
  hidden state;
- every oracle call costs one unit, including a repeated query;
- repeated queries return the same bit and are never silently deduplicated.

The learner never receives `n`, state identifiers, endpoint identifiers,
relations, modular displacements, evaluator labels, sampler metadata, donor
answers, or any channel other than its own sequential `(query, answer)` contact.

For this minimal world, `n` is the world identity: two copies with the same `n`
and the same R/L contract have the same oracle truth table. Re-running learners
on the same `n` creates repeated measurements, not a new world block. N3 cannot
be manufactured from duplicate instance IDs.

### Identifiability constraint on N1/N2

N2 is the maximum word length. N1 and N2 are not independent resource knobs.
The locked grammar must contain wrap-around witnesses for every sampled `n`;
at minimum it must admit word pairs whose displacement difference is `n`.
Otherwise EQ positives reveal only syntactic displacement equality and the
hidden order is not identifiable. The S-gate must prove grammar coverage by
enumeration for every N1 stratum before any comparative scout.

## 3. Grammar and candidate pool

The candidate-pool freeze must specify:

- canonical word enumeration: length first, then lexicographic token order;
- canonical EQ-pair orientation so `(u, v)` and `(v, u)` are not accidentally
  separate design cells;
- treatment of syntactic identities such as `(u, u)`;
- allowed length and relation-type strata;
- pool size and a proof that the locked budget cannot exhaust it;
- whether repeats are selectable and how a learner may remember them;
- one stable query index used by ACTIVE, donor ACTIVE, and RANDOM-STATIC.

The same admissible pool governs all arms. Any sampling shortlist used to make
ACTIVE scoring tractable must be generated independently of target truth and
made identically available to RANDOM-STATIC. Selection compute is reported
separately from oracle cost; training-update compute is matched across arms.

These details are S-gate choices. Implementation may expose them as named config
fields but may not assign outcome values before review.

## 4. Development, target, donor, and escrow separation

- **Development worlds:** used only by unit tests and the separately authorized
  non-citable comparative calibration scout. They are disjoint from all escrow
  strata.
- **Target worlds:** each distinct target `n` supplies the same hidden world to paired ACTIVE,
  YOKED-GEOMETRY, and RANDOM-STATIC target learners.
- **Donor worlds:** disjoint from target and development worlds, sampled from
  the same locked declared size stratum, and used only to produce full-budget
  ACTIVE query sequences for YOKED targets. A donor must have `n_donor !=
  n_target`; matching the hidden `n` would make donor and target oracle-identical
  and would fail to break instance adaptivity. Every stratum must therefore
  contain enough distinct admissible `n` values for one-to-one pairing.
- **Escrow evaluation panels:** generated once after lock under the signed
  procedural escrow. They are arm-independent and inaccessible to learners,
  acquisition policies, training code, and researchers before outcome.

An inferential block contains one target world, its three target arms, and its
unique donor world/transcript. No target or donor appears in two blocks. Seeds
are crossed repeated measurements inside a block, not independent units.
Queries and checkpoints are never units of variance.

Development controls must include: a shuffled-answer learner that cannot earn
certified solve; a parameter-stratum shift report; and a pre-contact
encoding-only probe that cannot recover `n`. Query choices made *after* contact
may encode what ACTIVE has learned and are treated as mediators, not leakage.

## 5. Learner and online update contract

Every target arm and donor run uses the same learner class, initialization
distribution, optimizer, prediction head, and sequential update schedule.
All begin from scratch under paired, domain-separated seeds.

At oracle step `t`:

1. the arm selects or receives query `q_t` without evaluator access;
2. its own oracle returns bit `a_t`;
3. the learner records a pre-update probability for `EQ(q_t)`;
4. the learner receives exactly the locked number of optimization updates on
   the same allowed history/replay view;
5. a frozen checkpoint/metric snapshot may be emitted for the blind evaluator.

No arm is batch-trained after collecting its corpus. That would confound query
choice with online-versus-batch optimization. No arm stops early. Training
continues to common budget B even if post-hoc evaluation later locates an early
solve event.

The architecture, update count, replay view, optimizer, calibration method, and
seed schedule are unresolved S-gate scientific choices where they affect the
trajectory. They must be shared across arms.

## 6. Arms and donor ordering

### ACTIVE

Chooses the admissible query minimizing the locked uncertainty scalar. Freeze
candidate: `abs(p_equal - 0.5)` from the learner's calibrated EQ head, with a
seeded committed pool order as deterministic tie-break.

The scorer receives learner state and admissible query encodings only. A
fail-closed dataflow test must prove it cannot reach oracle truth, evaluator
state, hidden `n`, or escrow content.

### Donor ACTIVE

Runs ACTIVE for the full B steps on its disjoint donor world. Donor solve status
is never fed back. The complete query sequence is serialized and hash-committed
before YOKED derivation. Donor answers and learner state never transfer.

### YOKED-GEOMETRY

Receives the donor's committed query indices in order and asks those queries of
its own target oracle. It trains online on its own answers under the common
update schedule.

### RANDOM-STATIC

Receives a full B-step query-index sequence from the locked random design over
the same admissible pool and trains online on its own answers. The random design
distribution and repeat rule freeze at the S-gate.

### Execution order

Within each block the donor transcript must be completed and committed before
the YOKED arm is derived. Target-arm execution order is fixed or counterbalanced
independently of outcomes. A partial donor or donor reuse invalidates the block.

## 7. Certified-solve endpoint

The primary endpoint is right-censored budget-to-certified-solve within common
horizon B. Larger benefit means faster/lower-cost certified solve.

The evaluator is a separate read-only process. It consumes frozen target-model
states at locked cadence and an arm-independent escrow panel. It cannot send
solve status, labels, gradients, thresholds, or panel structure to training or
acquisition code.

A solve event requires all locked conditions to persist for a locked window:

- performance on a class-balanced YES/NO EQ panel;
- required performance within each locked word-length and relation-type stratum;
- calibration within the locked bound;
- ABSTAIN below/within its locked rule;
- confident-lie rate below its locked rule.

Order probes are secondary cyclic-family diagnostics and never define the
primary solve event. A non-solve at B is right-censored/UNKNOWN, never success.

Panel construction, balance cells, cadence, persistence window, performance
thresholds, calibration statistic, ABSTAIN semantics, and confident-lie
threshold are unresolved S-gate choices. They freeze before comparative data.

## 8. Estimand and inferential unit

For each independent target+donor block, define paired ACTIVE and YOKED solve
times/censoring indicators. The primary population estimand is

`Delta_choice = RMST_YOKED(B) - RMST_ACTIVE(B)`,

where positive Delta means ACTIVE reaches certified truth with less oracle
budget. The exact paired/block estimator, interval, seed aggregation, censoring
handling, and multiplicity rule freeze at the S-gate.

One donor assignment is randomized within declared size strata for design balance and
then conditioned on. Primary inference is block-level under the locked
world-sampling model. Because distinct `n` values may be sampled without
replacement from a finite registered set, the S-gate must choose and justify a
finite-population or other valid block model; it may not call duplicate `n`
values independent. No randomization test may pretend to observe YOKED training
trajectories that were not run. Assignment permutations may be used only for
pre-treatment balance diagnostics.

Realized answer entropy, label balance, query lengths, relation types, repeats,
selection compute, calibration curves, and abstention/lie profiles are
mediators or diagnostics. None can replace the primary endpoint.

## 9. Comparisons and Level 2 mode selection

Before any comparative scout, the S-gate defines on one benefit scale:

- superiority `SUP(X, Y)`;
- equivalence `EQ(X, Y)` with N6-L1 margin;
- non-inferiority/non-superiority predicates needed by the total selection
  rule, with explicit directions and simultaneous interval handling.

C1 is read only from paired ACTIVE versus YOKED. The downstream contact-mode
selector considers all three arms:

1. invalid or unresolved required comparison blocks Level 2;
2. a uniquely superior arm is selected;
3. among a mutually equivalent best set, select the least adaptive member in
   priority RANDOM-STATIC, YOKED-GEOMETRY, ACTIVE;
4. non-transitive, cyclic, or unclassified intervals yield `INSUFFICIENT` and
   block Level 2.

RANDOM-STATIC beating ACTIVE is a registered anomaly, not a reason to alter the
rule. Contact-mode selection never rewrites the C1 verdict.

## 10. Comparative development scout

No scout is authorized by this draft. A later reviewed driver may run only after
the S-gate freezes the world, policy, endpoint, margins, and analysis plan.

Allowed uses on development worlds:

- endpoint computability and censoring rate;
- block-level contrast variance and covariance;
- runtime, memory, and artifact size;
- feasibility and N3 precision logic.

Forbidden uses:

- changing N1/N2, policy, endpoint, panel, thresholds, margins, estimator, or
  arm meaning after seeing a comparison;
- selecting favorable strata or excluding unfavorable valid blocks;
- treating a development contrast as evidence or citing it in the essay;
- accessing or generating escrow.

Any forbidden use voids the scout and reopens the S-gate. N3 may follow scout
precision evidence; N6 may not.

## 11. Procedural escrow candidate

The signed generator/witness is LOCAL_LLAMA under a procedural, not
cryptographically independent, threat model. Before implementation, a bounded
protocol review must define a fail-closed wrapper that:

1. binds the locked generator code/spec, secret seed commitment, model identity,
   prompt, public-key fingerprint, and one-generation rule;
2. uses audited deterministic code, not free-form model output, to construct and
   independently enumerate-validates worlds and panels;
3. prevents plaintext from stdout, logs, shell history, research chat, and
   committed files;
4. encrypts before researcher access and emits only ciphertext, plaintext hash,
   validation proof, and attestation;
5. treats any malformed generation, plaintext exposure, or second generation as
   terminal holdout invalidity.

Kirill holds the decryption key. This is process discipline, not cryptographic
independence from Kirill, and no stronger claim is permitted. The wrapper may be
implemented and tested only on dummy non-escrow fixtures before lock; it may not
generate the real holdout until separately authorized.

## 12. Fail-closed invalidity conditions

At minimum, any of the following invalidates the affected block or entire design
as preregistered:

- learner/acquisition access to hidden truth or evaluator state;
- target/donor/development/escrow overlap;
- donor reuse, partial donor, answer transfer, or transcript hash mismatch;
- unequal oracle or training-update budgets;
- early stop or outcome-dependent sequence truncation;
- arm-dependent evaluation panel or threshold;
- candidate-pool mismatch across arms;
- non-finite state or nondeterministic replay divergence;
- post-scout policy, endpoint, margin, or analysis change;
- escrow plaintext exposure, regeneration, malformed output, or hash failure.

Block-level versus programme-level invalidity and quorum consequences must be
fixed in the preregistration; no invalid block may be silently dropped.

## 13. Required implementation tests

Implementation is not yet started. The reviewed substrate must eventually test:

- exact `Z/n` transition and EQ truth against enumeration;
- N1/N2 wrap-around witness coverage;
- canonical candidate-pool identity and arm equality;
- domain-separated, disjoint target/donor/development schedules;
- rejection of target/donor equal-`n` pairs and duplicate-`n` pseudoreplication;
- one-to-one donor assignment and no reuse;
- full-B donor serialization/hash and YOKED re-derivation;
- learner/evaluator/acquisition dataflow separation;
- identical online update counts across arms;
- deterministic ACTIVE tie-break and RANDOM sequence replay;
- repeated-query cost and same-bit behavior;
- balanced evaluator construction without learner access;
- censored solve/persistence as pure functions of frozen observations;
- all branches of the total contact-mode rule, including RANDOM-superior and
  non-transitive `INSUFFICIENT` cases;
- checkpoint/state integrity and deterministic resume;
- interlocks proving no committed driver can run a comparative scout, escrow,
  or outcome before its capability exists.

## 14. Gate ledger

| Gate | Current status | Required closure |
|---|---|---|
| Claim-graph signatures | **CLOSED** | committed signature record |
| Canonical/essay amendment | **CLOSED** once its commit exists | synchronized governing text |
| Level 1 spec review | **OPEN** | resolve the choice register below; adversarial review |
| Substrate implementation | **ELIGIBLE AFTER SPEC REVIEW** | world/oracle/dataflow modules and tests only |
| S-gate | **OPEN** | all trajectory, endpoint, N6, and analysis choices frozen before comparative data |
| Comparative scout | **FORBIDDEN** | reviewed capped driver + S-gate signature |
| Level 1 lock | **FORBIDDEN** | N3 from scout; complete preregistration and verifier |
| Real escrow | **FORBIDDEN** | committed lock + reviewed wrapper |
| Level 1 outcome | **FORBIDDEN** | escrow committed; all invalidity gates green; explicit execution authorization |

## 15. Pre-S-gate choice register

Every item below is unresolved; none may be filled from comparative outcomes:

- N1: sampled `n` range and exact strata;
- N2: word-length cap and proof of wrap-around coverage;
- B: common oracle budget and candidate-pool headroom;
- learner architecture, initialization, optimizer, online update/replay schedule;
- ACTIVE uncertainty/calibration rule and tractable candidate scoring;
- RANDOM-STATIC distribution and repeat policy;
- target/donor block and seed schedules;
- finite-population/distinct-`n` sampling and variance model;
- evaluator panel cells, cadence, persistence, thresholds, calibration,
  ABSTAIN, and confident-lie rules;
- N6-L1 margins, simultaneous interval rules, and contact-mode predicates;
- paired censored estimator, seed aggregation, multiplicity, and invalidity
  handling;
- development/escrow split generator and N3 precision rule;
- artifact cadence, storage projection, and outcome-independent resource wall.

The next scientific step is review and closure of this register. The next
engineering step, only after that review, is the pure cyclic-world/oracle and
fail-closed dataflow substrate. No number in this draft is an outcome.
