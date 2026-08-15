# Phase 2 Stage-B development-core charter v1.1.1 boundary correction

Status: `READY_FOR_STAGE_B_DEV_CHARTER_V1_1_1_TARGETED_XY_CONFIRMATION`

Date: 2026-08-14

This self-contained charter replaces v1 and v1.1. It carries the author's
`I_ACCEPT_PHASE2_STAGE_B_DEV_CORE_CHOICES_A_TO_E` and
`I_ACCEPT_PHASE2_STAGE_B_DEV_CHARTER_CHOICES_F1_G1_H1`. It authorizes no code or
data until joint independent X/Y acceptance is recorded. After acceptance it
authorizes only uncommitted L0 and then L1 implementation below. Every later
layer requires its named pre-implementation annex and code gate.

## 1. Authority, inputs and narrow supersession

- Philosophia: `41adcaa96e3281746a6e59247d0fed5d1c42260c`
- MINIMO base: `6066f482c6752915ad21119f93dc162f4cb9db72`
- accepted Stage-A patch SHA-256:
  `e08a8d29d67d82297216722b3e13e6c1a3f4bd354962a2865b1cfc57a9980bbd`
- disposable standalone-theory bytes SHA-256:
  `2056deaf9c12a81dcb047e60154e8a473ffe235b5e48bb9433eb1d9f70afb507`

L0 must add those exact theory bytes at
`learning/theories/propositional-logic-intuitionistic-fragment.p` in a new
cumulative patch over the accepted Stage-A patch. The repository-path copy in
that patch becomes authoritative; `/tmp` does not. This does not authorize a
MINIMO commit.

Once this charter and the applicable layer are independently accepted,
domain-separated Stage-B development plans are not `carrier candidates` in the
prohibited audit/scientific sense of the Stage-A closure. They are disposable
fixtures. This supersedes only that phrase. Cost blocks, audit roots, selector
data, learner training, SELF/YOKED and scientific outcomes remain prohibited.

## 2. Development-only construct

### 2.1 Formula and sequent grammar

The only formula AST is:

```text
F ::= atom | false | not(F) | and(F,F) | or(F,F)
```

Implication is not a formula constructor. A public item is exactly an
atom-declaration prefix, zero or more formula hypotheses and one formula goal:

```text
[('a0 : prop) -> ... -> ('ak : prop) -> H0 -> ... -> Hm -> G]
```

Ambient arrows occur only in that outer sequent and in rule-internal premise
types required by Peano. There are 3..6 distinct declared atoms. Every declared
atom occurs in a proof hypothesis or goal. Every declared global proof
hypothesis is referenced at least once. Hypothesis reuse is allowed.

Atom names match `^a(0|[1-9][0-9]*)$`. Every formula occurring anywhere in a
plan has at most `MAX_FORMULA_NODES = 24` AST nodes, counting `ATOM` and `FALSE`
as one and each constructor as one. This includes every hypothesis, goal, proof
node conclusion, discharge formula, free `OR_INTRO_LEFT/RIGHT` disjunct and
`EXFALSO` conclusion. Violation is `PLAN_CONSTRAINT_INVALID`.

The `atoms` list is duplicate-free and in ascending byte-lexicographic order.
Every `ATOM.name` occurring anywhere in the plan appears in that list.

### 2.2 Rules, scope and size

The rule kinds are:

```text
ASSUME
AND_INTRO, AND_ELIM_LEFT, AND_ELIM_RIGHT
OR_INTRO_LEFT, OR_INTRO_RIGHT, OR_ELIM
NOT_INTRO, NOT_ELIM
EXFALSO
```

`NOT_INTRO` and each branch of `OR_ELIM` introduce one lexically scoped local
hypothesis. Local and global hypothesis IDs never shadow one another. Every
introduced local hypothesis is referenced in its body/branch. All local
hypothesis IDs in one plan are pairwise distinct, including across sibling
scopes. Global hypothesis formulas are pairwise byte-distinct. One global
hypothesis may still be reused by any number of `ASSUME` leaves; contraction
remains permitted.

One non-`ASSUME` rule application is one plan node. Assumption references are
leaves and count zero. A plan is a tree: a derived node is never shared or
reused. Its inference-dependency graph has one vertex per non-`ASSUME` node and
one parent-to-child edge only when the child is also non-`ASSUME`; edges into
`ASSUME` leaves do not count. The longest directed path is at least two edges,
that is, at least three chained inference nodes. A retained plan uses at least
three of these seven families:

```text
AND_INTRO
AND_ELIM
OR_INTRO
OR_ELIM
NOT_INTRO
NOT_ELIM
EXFALSO
```

It also uses `AND_INTRO` or `OR_ELIM`. This branching requirement is a signed
authorial construct constraint.

Bands use plan-node count only:

```text
S1=8..11, S2=12..17, S3=18..25, S4=26..37
```

Compiled primitive Peano-action count is recorded separately and is never
assumed equal to plan-node count. Any later alternative-proof search minimizes
total proof-tree rule applications, not path depth or compiled trace length.

### 2.3 Normality

Only immediate beta-redexes are prohibited:

- `AND_ELIM_LEFT/RIGHT` directly consuming `AND_INTRO`;
- `OR_ELIM` directly consuming `OR_INTRO_LEFT/RIGHT`;
- `NOT_ELIM` whose negative child is directly `NOT_INTRO`.

Commuting conversions are permitted and are recorded by preservation in the
exact checked plan bytes and exact plan identity; there is no separate
occurrence detector or counter. No implementation may add a stronger
normalization rule without a new charter version and new dev roots.

## 3. Data-only schemas

Every mapping has exactly the named keys. Every string is nonempty printable
ASCII, bytes `0x20..0x7e`; canonical objects therefore contain no control-byte
escapes. No floats, free text or extension fields occur in a signed object.

### 3.1 Formula schema

```text
ATOM  = {"kind":"ATOM",  "name":"aN"}
FALSE = {"kind":"FALSE"}
NOT   = {"kind":"NOT",   "arg":F}
AND   = {"kind":"AND",   "left":F, "right":F}
OR    = {"kind":"OR",    "left":F, "right":F}
```

### 3.2 Hypothesis schema

```text
{"id":"hN", "formula":F}
```

Local IDs match `^l(0|[1-9][0-9]*)$`; global IDs match
`^h(0|[1-9][0-9]*)$`. IDs are duplicate-free plan-wide within their respective
namespace, and the two namespaces are disjoint by grammar.

### 3.3 Proof-node schema

Every proof node has `kind` and `conclusion`. Additional exact fields are:

```text
ASSUME:        hypothesis_id
AND_INTRO:     left, right
AND_ELIM_*:    source
OR_INTRO_*:    source
OR_ELIM:       major, left_assumption, left_branch,
               right_assumption, right_branch
NOT_INTRO:     assumption, body
NOT_ELIM:      negative, positive
EXFALSO:       source
```

`left_assumption`, `right_assumption` and `assumption` use the hypothesis schema.
All other named child fields are proof nodes.

### 3.4 Plan schema

```text
{
  "schema":"philosophia.stageb.nd-plan.v1",
  "atoms":["a0",...],
  "hypotheses":[Hypothesis,...],
  "goal":F,
  "proof":ProofNode
}
```

The plan file is canonical data, not executable Python and not a pickle.

### 3.5 Checker expectation schema

Each L1 fixture is paired with:

```text
{
  "schema":"philosophia.stageb.plan-expectation.v1",
  "node_count":N,
  "band":"S1|S2|S3|S4",
  "families":[Family,...],
  "max_dependency_depth":D
}
```

`families` is duplicate-free and canonically sorted by the seven-family order in
section 2.2. The plan carries no count, band, identity or expectation field. The
checker recomputes every expectation. At L2 this record is the draw's target, not
a field trusted from a generated plan. `node_count` and `max_dependency_depth`
are JSON integers, never booleans; `node_count` must lie in the named band and
`max_dependency_depth` is nonnegative. `families` contains only named families.

## 4. Independent checker contract (L1)

The checker is built before the generator. It may import only the L0 schema,
canonical-byte, closed-enum and renderer modules plus Python standard-library
modules. It must not import a generator, compiler, Peano, MCTS, Torch or MINIMO
policy code.

It independently parses the data schema, establishes lexical contexts and
re-derives every conclusion:

- `ASSUME` concludes exactly the referenced in-scope formula;
- `AND_INTRO` concludes `and(left.conclusion,right.conclusion)`;
- `AND_ELIM_LEFT/RIGHT` require an `and(P,Q)` source and conclude `P`/`Q`;
- `OR_INTRO_LEFT/RIGHT` require their source to equal the corresponding
  disjunct of the stated `or(P,Q)` conclusion;
- `OR_ELIM` requires major `or(P,Q)`, checks its branches under fresh local
  assumptions `P` and `Q`, and requires both branch conclusions and the node
  conclusion to be byte-identical;
- `NOT_INTRO` checks its body under a fresh local assumption `P`, requires body
  conclusion `false`, and concludes `not(P)`;
- `NOT_ELIM` requires `not(P)` and `P`, and concludes `false`;
- `EXFALSO` requires source `false` and may conclude any well-formed formula.

The root conclusion must equal `goal`. The checker then enforces atom use,
global/local hypothesis use, duplicate-global-formula prohibition, the 24-node
formula bound, node count/band, dependency depth, family count, branching and
beta-normality. L1 renders the checker-rederived theorem in its checked input
atom/hypothesis order solely to test the L0 surface renderer. L1 neither performs
alpha-canonicalization nor compares a generator-supplied public rendering. L3
performs both duties and owns `SEQUENT_REDERIVATION_MISMATCH`.

The cause partition is closed:

- `PLAN_SCHEMA_INVALID`: exact key sets, JSON types, enum membership, printable
  ASCII, atom/ID grammar, atom-list ordering/uniqueness and ID uniqueness or
  shadowing;
- `PLAN_TYPE_INVALID`: hypothesis resolution, lexical scope, discharge-formula
  agreement, root-goal equality and every re-derived conclusion;
- `PLAN_CONSTRAINT_INVALID`: declared-atom use, global/local hypothesis use,
  duplicate global formulas, formula bound, node count, band, dependency depth,
  family count and branching;
- `PLAN_NON_NORMAL`: only the three section-2.3 redexes.

L0 freezes the following mutation-to-cause tuple; L1 asserts it exactly:

```text
wrong kind/key/type/string/atom-name/ID/atom-list -> PLAN_SCHEMA_INVALID
duplicate or shadowed hypothesis ID              -> PLAN_SCHEMA_INVALID
missing or out-of-scope hypothesis reference     -> PLAN_TYPE_INVALID
wrong child/conclusion/root goal                 -> PLAN_TYPE_INVALID
wrong discharge formula                          -> PLAN_TYPE_INVALID
undeclared or unused declared atom               -> PLAN_CONSTRAINT_INVALID
unused global/local hypothesis                   -> PLAN_CONSTRAINT_INVALID
duplicate global hypothesis formula              -> PLAN_CONSTRAINT_INVALID
formula bound                                    -> PLAN_CONSTRAINT_INVALID
node-count/band/expectation mismatch              -> PLAN_CONSTRAINT_INVALID
shallow dependency/too few families/no branching -> PLAN_CONSTRAINT_INVALID
each section-2.3 beta-redex                       -> PLAN_NON_NORMAL
```

L1 fixtures cover every rule kind and band. Every L1-reachable cause has at least
one mutation and every mutation must fail at the mapped first cause. A mutation
escape is reason code `MUTATION_ESCAPE` under
`DEV_CORE_FEASIBILITY_STOP`. `SEQUENT_REDERIVATION_MISMATCH` is unreachable at L1
and is first exercised at L3.

## 5. Canonical bytes and identities

Canonical object bytes are ASCII JSON:

```python
json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode('ascii')
```

Hashes are lowercase SHA-256 hex over those bytes. This is the Stage-A canonical
JSON rule; no second serializer is permitted.

### 5.1 Theorem identity

Alpha-canonical theorem identity is computed from public formulas only:

1. enumerate every bijection of the 3..6 used atoms to `a0..a{k-1}`;
2. under each bijection, sort the multiset of global hypothesis formula bytes;
3. serialize `{"atoms":["a0",...],"hypotheses":[F,...],"goal":F}` canonically,
   where `hypotheses` contains the sorted hypothesis formulas only;
4. choose the byte-lexicographically smallest serialization.

Global hypothesis formulas are pairwise distinct by section 2.2. No hypothesis
ID enters theorem identity, theorem name or public projection. The public theorem
name is `t_` plus all 64 hex characters of this identity hash. Block, band,
root, draw index, plan, trace and rejection history never enter the name.

### 5.2 Exact plan identity

For every atom renaming that attains the minimum theorem bytes, global
hypothesis IDs are assigned by sorted formula bytes. Local IDs are assigned by
preorder first introduction.
Serialize the resulting exact plan; choose the byte-minimum. Size counting
occurs before this identity normalization on the checked tree, and must equal the
count after normalization.

### 5.3 Rule-skeleton identity

Formulas, atom names and hypothesis IDs are erased. Leaves retain
`ASSUME_GLOBAL` or `ASSUME_LOCAL`. Direction is erased for `AND_ELIM_*` and
`OR_INTRO_*`. `AND_INTRO` child skeletons are sorted. In `OR_ELIM`, the major
child remains first and the two branch skeletons are sorted as a pair; no branch
is exchanged independently of its local assumption. Other child order is
preserved. Canonical JSON and SHA-256 produce the skeleton identity.

Every dev theorem and skeleton is permanently ineligible for cost, audit,
selector, pilot and scientific scopes. The later audit contract must extend this
to mutual theorem-and-skeleton disjointness of every scope.

At L1 acceptance, canonical raw plan bytes and checker-rederived raw theorem
bytes for every valid-plan fixture are registered and permanently excluded. The
two renderer-only fixtures retain their raw-sequent exclusions. L3 computes and
registers theorem and skeleton identities for all of these fixtures before any
root key can be minted or consumed. The raw exclusions are never removed.
Fixture theorems and skeletons are therefore barred from the later audit frame
without requiring L1 to implement L3 identity logic.

## 6. Public projection and erasure

The only public carrier record is:

```text
{
  "schema":"philosophia.stageb.public-item.v1",
  "theory_sha256":"2056deaf9c12a81dcb047e60154e8a473ffe235b5e48bb9433eb1d9f70afb507",
  "premises":["and_i","and_el","and_er","or_il","or_ir","or_e",
              "not_i","not_e","exfalso"],
  "theorem_name":"t_<64hex>",
  "goal":"<canonical Peano sequent ASCII>"
}
```

`public_projection(plan)` is a pure function of the checker-rederived canonical
theorem plus the frozen common theory/premise constants. The projection contains
no root, draw, band, plan size, plan, trace, skeleton, generator stratum,
certificate or rejection field. L3 must enumerate every sealed field and prove
none affects projection bytes when the theorem is held fixed.

L0 freezes the Peano renderer as a pure surface function. It renders the theorem
object it is given and performs no atom-cardinality or alpha-canonicalization
validation. L0 anchors use already canonical input. L3 alone supplies the
alpha-canonical theorem for public projection, with atoms/hypotheses in canonical
order and atoms named `a0..a{k-1}`. Rendering is ASCII with no optional
whitespace:

```text
ATOM(aN)  := 'aN
FALSE     := false
NOT(F)    := (not F)
AND(P,Q)  := (and P Q)
OR(P,Q)   := (or P Q)
DECL(aN)  := ('aN : prop)
SEQUENT   := [DECL(a0) -> ... -> DECL(a{k-1}) -> H0 -> ... -> Hm -> G]
```

With zero hypotheses the last declaration points directly to `G`. L0 includes
alpha-renamed forms of the already Peano-accepted renderer fixtures
`[('a0 : prop) -> ('a1 : prop) -> (and 'a0 'a1) -> (and 'a1 'a0)]` and
`[('a0 : prop) -> ('a1 : prop) -> (or 'a0 'a1) -> (or 'a1 'a0)]` with exact
expected bytes. These are two-atom renderer-only syntax fixtures, not admitted
dev plans. Their raw sequent SHA-256 values are permanently excluded; every
3..6-atom valid-plan fixture separately receives theorem and skeleton identities
under section 5.3. L1 tests the pure renderer without importing Peano; L4
compares its result to a fresh Peano parse/replay. The public record stores the
rendered ASCII string; canonical Peano sequent bytes are its ASCII encoding.

## 7. Development generator interface (not yet implementation-authorized)

The L2 generator requires a separately reviewed executable annex defining its
complete recursive construction algorithm and byte-consumption schedule. This
charter already binds the following interface and distributional choices; the
annex may not change them:

- one raw draw is one complete construction attempt;
- root keys are exactly 32 bytes; `root_id` is the lowercase 64-character
  `SHA256(root_key)` hex digest;
- each draw has an independent HMAC-SHA256 counter stream with `key = root_key`,
  the 32 raw bytes, never `root_id`; its message is ASCII
  `philosophia.stageb-dev.v1`, then NUL, unsigned big-endian `draw_index`
  (8 bytes), then unsigned big-endian `block_index` (8 bytes), starting at zero;
- the stream concatenates HMAC blocks in ascending `block_index`;
  `randbelow(n)` consumes successive non-overlapping unsigned big-endian 64-bit
  words and rejects words at or above `floor(2**64/n)*n`; a rejected word is
  consumed and no word is reused; there is no modulo bias;
- band target is `draw_index mod 4`, mapped `0:S1,1:S2,2:S3,3:S4`;
- target plan-node count is uniform over the target band's integers;
- a filled-band draw is consumed and ledgered; no adaptive replenishment;
- every attempt emits either one checked plan or one closed rejection cause;
- generator code is not imported by the checker.

The annex must specify the recursive proof-construction grammar, exact decision
order, byte used by every choice, and termination bound. It must be accepted
before root keys are minted or L2 code is written. Before root minting, the
accepted fixed-fixture code gates must include at least one S4 plan satisfying
the 24-node formula bound and no-sharing rule, and L4 must compile and replay it.

## 8. Total future acceptance pipeline and closed causes

L2-L4 must implement this order for every consumed draw:

1. derive draw stream and target band/node count;
2. construct one plan candidate;
3. validate exact schema;
4. run independent typed checker and constraints;
5. re-derive/canonicalize theorem and identities;
6. reject dev theorem/skeleton collision;
7. run classical truth-table necessary check;
8. compile checked nodes by unique semantic match to enumerated Peano actions;
9. replay from a fresh state to empty goal;
10. render and record every exact Stage-A-format query length without loading an
    LM, truncating or applying a context admission threshold;
11. admit to the target quota or record filled-band consumption.

The eight roots are processed in registered order `0..7`, one root at a time;
draws within a root are processed in ascending `draw_index`. Stage 6 uses the
cumulative set of all previously accepted dev theorem and skeleton identities in
that order, seeded by registered L0/L1 hand-fixture identities. Collision
acceptance is therefore deterministic and nonreplacement.

Closed draw causes are:

```text
PLAN_CONSTRUCTION_FAILED
PLAN_SCHEMA_INVALID
PLAN_TYPE_INVALID
PLAN_CONSTRAINT_INVALID
PLAN_NON_NORMAL
SEQUENT_REDERIVATION_MISMATCH
CLASSICAL_COUNTEREXAMPLE
THEOREM_ID_COLLISION
SKELETON_ID_COLLISION
COMPILER_NO_MATCH
COMPILER_AMBIGUOUS_MATCH
PEANO_REPLAY_REFUSAL
PEANO_REPLAY_NONTERMINAL
QUERY_MEASUREMENT_OVERFLOW
TARGET_BAND_ALREADY_FULL
```

Each rejection is attributed to the first failing stage only. Every draw index
is represented exactly once by an acceptance or cause. The L2 annex may refine
`PLAN_CONSTRUCTION_FAILED` into a closed sub-enum but may not reorder later
stages.

The final `n_positions` and codec admission threshold are intentionally not a
dev retention rule. L0 freezes
`DEV_QUERY_MEASUREMENT_N_POSITIONS = 4096`, used solely to instantiate the
accepted Stage-A `QueryCodec` for measurement; no LM is loaded. Stage 10 records
exactly `{query_kind, artifact_id, byte_count, token_count}` for every query. No
dev item may take the codec overflow-refusal path. An overflow is reason code
`QUERY_MEASUREMENT_OVERFLOW` under `DEV_CORE_FEASIBILITY_STOP`, never a retention
event or carrier evidence. It is recorded as that draw's first-failing cause and
immediately stops dev execution under the same top-level reason.

The sentinel is neither the audit `n_positions` nor a `dev-fit` input. The later
audit contract freezes its own value and reruns the strict interface gate on
permanently fresh material. Observed dev query lengths may inform that later
engineering choice only when it is disclosed as `dev-fit`; the later contract
must state that interface survival is an engineering check, not evidence.

## 9. Compiler and replay contract (not yet implementation-authorized)

The L4 compiler consumes only a checker-accepted canonical plan. It may not
import or call a generator, MCTS, learned/uniform policy, G4ip or alternative
proof search. At each node it enumerates actions through the accepted Stage-A
contained path, selects by semantic identity rather than list position/string
prefix and typed-refuses zero or multiple matches. A fresh `PyProofState` replay
must end with an empty goal. Plan-node and primitive-action counts are both
retained.

`learning/test_phase2_stageb_theory_enumerability.py` is a separate L0 regression
module. Unlike the checker, it may import Peano and the repository-path theory. It uses
only hand-written statements, generates no plan, mints no root and runs no search.
It emits a frozen table for all nine premises with exact fields:

```text
{premise, annotation_text_or_ABSENT, enumerable,
 enumerable_directions, required_direction, witness_state}
```

Directions are a subset of `BACKWARD_ON_GOAL` and
`FORWARD_FROM_HYPOTHESIS`. Required directions are: backward for `and_i`,
`or_il`, `or_ir`, `or_e`, `not_i`, `not_e` and `exfalso`; forward for `and_el`
and `and_er`. `not_e` has annotation `ABSENT`; its available direction is
measured, not inferred from an annotation. Missing a required direction returns
`DEV_CORE_FEASIBILITY_STOP` at L0.

The same module checks enumerability, not compilation, for hand-declared
ambient-arrow chains at depths 1..8: at every relevant state the required action
must occur by exact serialization in the enumerated action set. Existing trace
lengths 6..34 remain prior observations, never thresholds. Full compilation and
fresh replay of this family are L4 duties. The independent checker never imports
this regression module or Peano.

## 10. Development scope, permitted use and terminals

After all accepted L2-L4 implementations pass their code gates, exactly eight
domain-separated dev roots are minted and registered. Each targets four accepted
plans per band and stops at 2,000 draws.
Execution is CPU-only, one process, one thread, primary workstation, with an
8-wall-hour total ceiling. Lenovo Legion is excluded because its 8 GiB VRAM did
not provide the expected performance gain.

Dev evidence may inform only generator yield, band reachability, resource
projection, context engineering and later quota feasibility; affected later
constants are labelled `dev-fit`. It may not tune future `B*` windows, 12/32 usable-block threshold,
75% interface survival, inverse threshold or positive-control Spearman threshold.

The only top-level terminals are:

```text
DEV_CORE_FEASIBILITY_STOP
DEV_CORE_FEASIBLE_FOR_AUDIT_CONTRACT
```

Closed reason codes under `DEV_CORE_FEASIBILITY_STOP` are:

```text
PREMISE_ENUMERABILITY_FAILED
DAG_ENUMERABILITY_FAILED
DAG_REPLAY_FAILED
CHECKER_UNSOUND
COMPILER_UNSOUND
MUTATION_ESCAPE
PUBLIC_PROJECTION_LEAK
COLLISION_ACCOUNTING_ERROR
NONDETERMINISM
COMPILER_FAMILY_UNREACHABLE
QUERY_MEASUREMENT_OVERFLOW
ROOT_QUOTA_UNFILLED
RESOURCE_CEILING_EXHAUSTED
```

The stop is non-inferential and does not kill the carrier. It permits no
within-version change to bands, draws, formula size, sentinel, quotas or any
other frozen configuration. A changed configuration requires a new charter
version and new permanently excluded fixtures/roots. Non-adaptive
`draw_index mod 4` allocation may fail to fill S4; that is an accepted prospective
risk and returns `ROOT_QUOTA_UNFILLED`, not permission to replenish adaptively.

If an unsoundness, mutation escape, leak, collision-accounting error or
nondeterminism is discovered after any root is minted, all eight keys and all
outputs from that run are voided. Already accepted fixture/dev bytes remain
permanently excluded. A repaired implementation must pass its code gate and mint
eight fresh keys before a new run; a code repair alone does not alter the frozen
scientific configuration or authorize reuse of a consumed key.

## 11. Staged authorization

1. **Charter X/Y acceptance.** Authorizes uncommitted implementation of L0 and
   then L1, in that order, with one review stop after L1. No intervening
   specification is produced.
2. **L0 file set:** exactly
   `learning/phase2_stageb_schema.py`,
   `learning/phase2_stageb_canonical.py`,
   `learning/phase2_stageb_causes.py`,
   `learning/phase2_stageb_render.py`, the theory path in section 1,
   `learning/test_phase2_stageb_l0.py`, and
   `learning/test_phase2_stageb_theory_enumerability.py`.
   `phase2_stageb_schema.py` is the sole home of `MAX_FORMULA_NODES`,
   `DEV_QUERY_MEASUREMENT_N_POSITIONS`, band edges and seven-family order.
3. **L1 file set:** exactly `learning/phase2_stageb_checker.py` and
   `learning/test_phase2_stageb_checker.py`. It uses hand-written fixtures only.
   Stop for driver and independent code review. The cumulative patch must name
   this complete file set.
4. **L2 generator annex:** written and independently accepted before L2 code.
   After implementation, stop for independent code review using only registered
   hand-written or fixed-stream fixtures, all permanently excluded.
5. **L3 identity/projection annex:** written and independently accepted before
   L3 code. After implementation, stop for independent code review on excluded
   fixtures only.
6. **L4 compiler/replay annex:** written and independently accepted before L4
   code. After implementation, stop for independent code review on excluded
   fixtures only.
7. **Dev execution:** the eight root keys are minted and consumed only after the
   accepted L2 generator, L3 identity/projection and L4 compiler/replay
   implementations execute the complete ordered pipeline. No earlier layer may
   mint or consume them.
8. Only after `DEV_CORE_FEASIBLE_FOR_AUDIT_CONTRACT` may a new Stage-B audit
   contract freeze uniform calibration, G4ip, inverse, statement models,
   alternative-proof search, positive control, resource projection and audit
   terminals.

No class hierarchy, plugin indirection, configuration file, registry abstraction,
cross-cutting supervisor, governance or harness framework is authorized at L0 or
L1. Enums are literal frozen tuples; canonical bytes use one serializer and one
hash function. Later learner-visible ordering derives from canonical theorem
identity, never draw index or acceptance order. Each layer is a small module plus
focused tests and a cumulative patch artifact.

## 12. Negative authorization

This unaccepted v1.1.1 draft and either X or Y review alone authorize nothing.
Joint recorded X/Y acceptance authorizes only the uncommitted L0 then L1 file set
in section 11 and their review artifacts. It authorizes no L2-L4 code, dev root,
generated plan, cost block, audit root, calibration, G4ip, inverse,
statement-model fitting, selector fitting, learner training, SELF/YOKED,
scientific outcome, commit or push. Every later layer requires its separately
accepted annex and code gate.
