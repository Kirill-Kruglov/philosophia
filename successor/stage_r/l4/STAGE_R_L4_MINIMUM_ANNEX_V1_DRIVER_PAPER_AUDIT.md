# Stage-R L4 minimum annex V1 driver paper audit

Status: `BOUNDED_PAPER_REPAIR_REQUIRED`

Date: 2026-08-15

Object audited:
`STAGE_R_L4_MINIMUM_COMPILE_REPLAY_EXECUTABLE_ANNEX_V1_DRAFT.md`,
SHA-256
`ee48524f1c1ad2b91e218006e8c1784d3a1f425d1cf787ca7a39133ba437ce4e`.

All authority hashes in draft section 0 were independently recomputed and
match. The scope reconciliation in draft sections 5.1–5.4 is accepted. The
draft does not reactivate roots, the eight-root route, ambient-arrow
universality, query measurement, a learner/selector or science.

The paper is not safe to freeze. The defects below are closed and repairable in
the single bounded paper-repair pass allowed by the activation. They require no
new author or scientific choice.

## Critical

### C1. The obligation algorithm is not the Peano semantics of the accepted ND rules

Evidence: draft sections 2.3, 3.4 and 3.4.2, lines 137, 201–218 and 242–274.

The generic rule

```text
open_goals = child conclusions excluding ASSUME children
```

is false for this theory:

1. `NOT_INTRO` produces the Peano subgoal `['P -> false]`, not the body child's
   conclusion `false`. Even an `ASSUME` body still requires the arrow subgoal
   before its one `intro.`.
2. `OR_ELIM` marks its major premise as inferred and produces two branch-arrow
   subgoals `['P -> R]` and `['Q -> R]`; it does not produce the major child's
   conclusion as an open goal. The major must already be inhabited.
3. A forward `AND_ELIM_LEFT/RIGHT` node must first ensure that its `source`
   neutral spine is inhabited. Draft pseudocode never visits the forward
   child's obligation at all. It can therefore handle only a one-step
   elimination from an already present conjunction and cannot compile the
   accepted L2 elimination chains.
4. `SelectGoals` returns multiple independent `PyProofState` objects. The draft
   alternates between a singular `state` and an unspecified obligation stack,
   and replay likewise does not define the exact active-frontier update. “The
   last action returned an empty list” is not a global empty-goal condition
   while sibling states remain.
5. Matching `SelectGoals` effects as a multiset and then pairing returned states
   to plan-ordered children is not total when goals repeat or have different
   proof obligations. The rule declaration supplies an ordered semantic
   frontier; a multiset loses that relation.

Consequence: the proposed code must return `COMPILER_NO_MATCH` on real
`NOT_INTRO`, nontrivial `OR_ELIM` or nested `AND_ELIM` paths, or can attach the
wrong obligation to a returned state. The claimed ten-kind semantic coverage
and fresh empty-goal replay therefore do not follow.

Smallest bounded repair:

- replace generic `open_goals` with an exact per-rule transition table derived
  from the pinned theory declaration and annotations;
- define two explicit modes: `PROVE_ACTIVE_GOAL` and
  `MATERIALIZE_NEUTRAL_IN_CONTEXT`;
- in materialize mode, recursively materialize an `AND_ELIM` source neutral
  spine before its forward construction; for `OR_ELIM`, materialize/verify its
  neutral major before applying `or_e`;
- prove from L1 normality that every materialized source/major has the allowed
  neutral grammar (`ASSUME` followed only by eliminations), otherwise refuse;
- wrap `NOT_INTRO` and both `OR_ELIM` branches in their exact arrow goals,
  independently of whether their bodies are `ASSUME`;
- carry an explicit ordered frontier of `(PyProofState, obligation)` pairs in
  compile and replay, with a fixed push/pop law and global success only when
  both the script and the whole frontier are empty;
- use the ordered Peano effect tuple. Repeated equal goals require an exact
  canonical obligation ordering or a typed ambiguity refusal; never a
  multiset-to-position guess;
- account for every non-`ASSUME` plan node actually compiled. A silently
  inhabited non-`ASSUME` subtree must fail closed rather than count as semantic
  rule coverage.

If that exact neutral/branch construction cannot be specified from the pinned
API, the repair must return the structural-blocker token instead of attempting
implementation.

## Major

### M1. The alpha-automorphism tie proof is false

Evidence: sections 2.2 and 2.4, lines 124–153; gate item 6, line 455.

The lexicographically first theorem-minimising permutation is relative to the
source atom order. Under a raw alpha renaming, an automorphic theorem can choose
a different theorem-minimising map. The draft itself admits at line 130 that
two such maps can yield different obligation trees, then line 153 incorrectly
claims the first-permutation rule removes that difference. It does not follow
that the script hash is invariant over the full alpha orbit.

Smallest repair: first compute the L3 minimum theorem bytes; among **all**
permutations attaining those bytes, choose the minimum canonical obligation-tree
bytes, with the lexicographically first permutation only as a final tie-break.
Prove that the set of candidate obligation-tree bytes is invariant under source
alpha renaming. This changes no L3 theorem, name or public byte.

### M2. The descriptor selects by forbidden display text and records proof-relevant noise

Evidence: P11–P12 and sections 3.1–3.3 and 4.4, lines 51–54, 159–194 and
336–346.

Line 176 obtains the `Apply`/`Construct` arrow by `str(a)` equality even though
line 161 and the author task prohibit string equality as an action identity.
For proposition-valued `SelectConstruction`, Rust equality/dedup is explicitly
proof-irrelevant: only one representative per dtype survives, but the draft
stores `selection_value` in the semantic script. A different proof-term
representative can therefore move the supposedly semantic script hash without
moving the proof effect.

Smallest repair: candidate **selection and replay rematching** use typed kind
plus ordered executed effect (and proposition dtype where applicable), never
the arrow display. If two different actions have the required effect, refuse
ambiguity. The closed `a <premise>`/`c <premise>` display may be checked only
after unique semantic selection as a diagnostic rule-coverage assertion; it
must not disambiguate or enter the script identity. In this prop-only fragment,
omit the proof value from `SelectConstruction` identity/hash and prove why. Use
the accepted Stage-A action-object canonicalization path for containment and
duplicate-display refusal, while proving that its sort order never selects the
action.

### M3. The import allowlist cannot implement the specified algorithm or theory pin

Evidence: section 1.2 line 83; sections 2.2 and 8.1 lines 124 and 470–474.

The allowlist forbids/omits `itertools` although the algorithm requires
`itertools.permutations`; it forbids `hashlib` although the API requires a raw
UTF-8 SHA-256 comparison of caller-supplied `theory_text`; and it forbids
`phase2_actions` while the charter/author task requires the accepted Stage-A
contained enumeration path. `canonical_hash(theory_text)` is not the required
raw-byte theory hash.

Smallest repair: close one coherent allowlist. Permit `itertools`, permit
`hashlib` solely for `sha256(theory_text.encode('utf-8'))`, and specify the
exact accepted Stage-A helper used for contained action-object materialization.
Disclose any transitive imports; instantiate no codec, learner, MCTS or query
object. Alternatively embed and compare the complete pinned theory text, but
do not leave two possible implementations.

### M4. The public test seam contradicts the exact public API and input binding

Evidence: gate item 7 line 456 versus section 8.1 line 471.

The gate requires a candidate-list transformer keyword on the public entry
point, but the declared public signature has exactly three arguments and
section 1.4 says no caller can influence compilation. A production-visible
transformer is a route around that boundary.

Smallest repair: keep the public signature exact. Inject at one named
module-private candidate materialization boundary by temporary rebinding/mock,
always restore it in `finally`, and assert the result through the unmodified
public entry point. Add a signature test proving no test hook is public.

### M5. Production domain and the eleven-row acceptance population are conflated

Evidence: sections 1.1, 5.1, 6 and the closing literal, lines 64–70, 364–368,
419–422 and 578–581.

Eleven excluded plans are the complete **paper/code-gate calibration
population**, but a compiler hard-limited to those eleven cannot later witness
reservoir membership for a fresh, non-excluded L2 plan. Conversely the public
entry point contains no fixture-hash check and therefore is not actually
limited to eleven.

Smallest repair: state one distinction. Production accepts the bounded
L1-accepted Stage-B plan interface and returns success or a closed compile/replay
refusal; no universal success/completeness claim is made. The current acceptance
artifact and mandatory gate cover exactly the eleven permanent exclusions and
no other plan. This restores prospective reservoir admission without generating
or selecting one now and without restoring the full catalogue.

### M6. Bounds and exception semantics are not closed

Evidence: sections 3.3 and 3.6, lines 188–195 and 282–298.

- `37 × 2 + 37 × 12 = 518`, not a value that can be “rounded up” to the stated
  `PRIMITIVE_STEP_BOUND = 512`.
- `MAX_GLOBAL_HYPOTHESES = 4` is justified as an observation over the eleven
  fixtures rather than derived from the supported L2 production grammar.
- a non-panic exception during candidate evaluation is silently excluded; the
  compiler can then succeed through another candidate, hiding a partial Peano
  failure. No closed cause records that event.
- `CANDIDATE_EVALUATION_BOUND = 8192` is not related to the product of the
  per-step and per-enumeration bounds; calling it fail-closed is permissible,
  but the exact counter increment and terminal precedence are unstated.

Smallest repair: rederive the step bound from the repaired per-rule traversal;
derive the hypothesis bound from accepted L2, not the sample; make every
candidate-evaluation exception immediately fail closed under an exact existing
compile cause/subcause; and specify when both budget counters increment and
which limit fires first. A finite refusal ceiling need not claim universal
reachability.

## Minor

### m1. The paper-author pass reports a prohibited disposable reconstruction

Evidence: section 0 line 37. The author task prohibited creating a worktree,
but the draft says its source facts came from a disposable reconstruction.

This produced no scientific data and no durable artifact in `/tmp`, and the
driver independently verified the cited Rust/authority facts by read-only
`git show`, patches and durable files. The repair must disclose the procedural
deviation rather than claim full compliance, and cite only durable source
locations as authority. It does not authorize another reconstruction.

### m2. Exception and success wording is internally contradictory

Section 8.1 says “No other exception escapes,” while section 8.3 requires
`L4InvariantError` to escape. Section 4.3 describes the last returned empty
list as empty-goal while also mentioning an obligation stack. Replace both with
one exact invariant/public-exception law and the global frontier condition from
C1.

## Disposition and bounded next step

No author choice is open. One targeted paper repair may replace this draft with
a standalone V1.1 annex addressing C1 and M1–M6 plus the two minor consistency
repairs. The repair may not execute Peano, reconstruct fixtures/worktrees,
write code, widen the two-file scope or consume another general review.

After V1.1, the driver performs a bounded mechanical confirmation only. If any
critical algorithmic point remains open, the route returns the structural
blocker rather than starting implementation.

Focused-time accounting:

- paper author: 0.50 h;
- this driver paper audit: 0.75 h (conservative);
- cumulative L4 focused time: 1.25 h;
- remaining L4 focused time: 22.75 h.

```text
L4_V1_PAPER_ACCEPTED=NO
BOUNDED_PAPER_REPAIR_PASSES_REMAINING=1
L4_IMPLEMENTATION_AUTHORIZED=NO
ROOT_OR_FRAME_GENERATION_AUTHORIZED=NO
SCIENTIFIC_EXECUTION_AUTHORIZED=NO
```

BOUNDED_REPAIR_REQUIRED_STAGE_R_L4_MINIMUM_ANNEX_V1_DRIVER
