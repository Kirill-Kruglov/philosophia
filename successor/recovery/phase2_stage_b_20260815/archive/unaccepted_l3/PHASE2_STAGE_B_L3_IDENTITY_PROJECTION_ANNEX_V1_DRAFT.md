# Phase 2 Stage-B L3 identity/projection annex v1 (unaccepted draft)

Status: `READY_FOR_PHASE2_STAGE_B_L3_ANNEX_V1_XY_REVIEW`

Date: 2026-08-14

This draft authorizes nothing. It specifies L3 to the level of executable detail
required by charter sections 5.1-5.3, 6 and pipeline stage 5, and by the L2 V5
code closure. It does not authorize L3 code, a dev root key, a generated plan, a
scan, L4 work, Peano/MCTS/search execution, query measurement, training, an
audit or scientific item, a repository edit, a commit or a push. One bounded
author choice is collected in
`PHASE2_STAGE_B_L3_IDENTITY_PROJECTION_ANNEX_V1_AUTHOR_CHOICES.md`; it must be
recorded before X/Y acceptance, because it changes the pipeline stage-6
collision seed.

## 0. Authority and evidence

Every hash below was recomputed by this author against the named file and
matches.

- MINIMO base: `6066f482c6752915ad21119f93dc162f4cb9db72`
- Stage-B dev charter v1.1.1:
  `703bf39cfe8f875f9be3781659a7365c1bc99c42f7523e43fef2c0a2c47b8311`
- L0/L1 v3 closure:
  `d6b103a3334d6bb0d7fd6e9bb7ecfa49ed86eb7b4e273dba3b6a47166eccb3d6`
- accepted L2 annex:
  `3a78a53ecb8e5275f433bc03c50b7b93746c597e3d2d1fcf0bedd4249f102da8`
- L2 V5 code closure:
  `d09781ea2cb9335cba72ce004a576f7e722a66b3b4c1c9b9d9d0de31faf9ccd9`
- accepted V5 cumulative patch:
  `3a570b2e35b15dc796d86cd8a997230c00bbf5aed3b5c06f3b14dca78b46b683`
- frozen L2 code-gate artifact:
  `8961b5a97ee0972d83a071e1b1c82869a9841f5f01c45add12a88dbfee1010f0`
- raw-fixture exclusion ledger V3:
  `a1f907ad6665b7c96d91496c5a91d32f0f0cae63da48b6b26da6b292d48f528d`

The pinned patch files, not the disposable inspection tree
`/tmp/minimo_phase2_stageb_l2_final`, are the evidence of record. The L0/L1/L2
sources quoted below were read from that tree and are reproduced only where the
specification depends on their exact behaviour.

### 0.1 Facts read from the accepted code, on which this annex depends

These are not assumptions. Each is quoted or derived from the accepted surface.

1. `phase2_stageb_canonical` supplies exactly `canonical_dumps`,
   `canonical_bytes`, `canonical_hash`, over
   `json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True)`
   encoded ASCII, SHA-256 lowercase hex. There is no second serializer.
2. `phase2_stageb_render` supplies `render_formula`, `render_declaration`,
   `render_sequent(atoms, hypotheses, goal)`. It is pure surface and validates
   nothing.
3. `phase2_stageb_checker.rederived_theorem(plan, goal)` returns exactly
   `{'atoms': list(plan['atoms']), 'hypotheses': [h['formula'] for h in
   plan['hypotheses']], 'goal': goal}`, and `check_plan` returns that object
   under key `theorem` with `goal = derived`, the root node's stated conclusion,
   after asserting `formulas_equal(derived, plan['goal'])`.
4. `_schema_plan` rejects any plan whose `atoms` list is empty, has duplicates,
   or is not equal to `sorted(atoms)`. So `plan['atoms']` is duplicate-free and
   in ascending byte-lexicographic order.
5. `check_plan` enforces `MIN_DECLARED_ATOMS = 3 <= len(atoms) <= 6 =
   MAX_DECLARED_ATOMS`, `occurring <= declared`, and
   `declared <= public_atom_names(plan)`.
6. `check_plan` enforces that the canonical bytes of the global hypothesis
   formulas are pairwise distinct.
7. `_schema_hypothesis` and `_schema_proof` enforce `^h(0|[1-9][0-9]*)$` for
   global identifiers and `^l(0|[1-9][0-9]*)$` for local identifiers, plan-wide
   local uniqueness, and no `hN`/`lN` collision. The two namespaces are disjoint
   by grammar.
8. `PROOF_CHILD_FIELDS` is exactly
   `ASSUME:()`, `AND_INTRO:('left','right')`, `AND_ELIM_LEFT:('source',)`,
   `AND_ELIM_RIGHT:('source',)`, `OR_INTRO_LEFT:('source',)`,
   `OR_INTRO_RIGHT:('source',)`, `OR_ELIM:('major','left_branch',
   'right_branch')`, `NOT_INTRO:('body',)`, `NOT_ELIM:('negative','positive')`,
   `EXFALSO:('source',)`.
9. All five L1 valid-plan fixtures declare exactly `['a0','a1','a2']`, i.e.
   `k = 3`. All six L2 gate fixtures declare `k` in `3..6` by generator
   construction and L1 acceptance.
10. In the V3 ledger, `premise_witness_or_e` and `renderer_or_commute` carry
    byte-identical `raw_ascii_sequent_sha256`
    (`aa5844b1f498b09ff16c52d048b0f66e693430c226dab45ddd56455c53205267`) and
    byte-identical `canonical_json_string_sha256`
    (`8089c6d1eefd4c200f913b99842eb950e19a549993de444262a215b299ef5e22`). This
    author confirmed both equalities directly from the artifact.
11. The accepted L2 generator emits no surface syntax and no rendering.

**Derived Lemma D1 (declared = public = used).** For any `check_plan`-accepted
plan, `set(plan['atoms'])` equals the set of atom names occurring anywhere in
the plan, and equals `public_atom_names(plan)`. Proof: fact 5 gives
`occurring_everywhere <= declared` and `declared <= public`. `public` is by
definition the atoms of the hypothesis formulas and the goal, which are a subset
of `occurring_everywhere`. Chaining, `declared <= public <=
occurring_everywhere <= declared`, so all three coincide. Therefore charter
section 5.1's phrase "the 3..6 used atoms" denotes exactly `plan['atoms']`, and
no separate "used atom" computation is authorized or needed.

## 1. Exact L3 scope and fixed boundary

L3 owns exactly six duties and nothing else:

1. alpha-canonical theorem identity (charter 5.1), section 4 below;
2. exact plan identity (charter 5.2), section 5;
3. rule-skeleton identity (charter 5.3), section 6;
4. public projection and erasure (charter 6), section 7;
5. independent theorem re-derivation and `SEQUENT_REDERIVATION_MISMATCH` at
   pipeline stage 5, section 7.1;
6. materialization of final identities for excluded valid fixtures and a
   deterministic pipeline stage-6 exclusion seed, section 8.

L3 does not construct plans, does not import the generator in production, does
not compile Peano actions, does not replay, does not measure queries, does not
mint or consume a root, does not run search, and fits nothing. L3 adds no L1
predicate, weakens none, and does not reorder charter section 8.

### 1.1 Authorized files

```text
learning/phase2_stageb_identity.py          production, new
learning/test_phase2_stageb_identity.py     code gate, new
```

Exactly two files. No Stage-A file, no L0 file, no L1 file, no L2 file, no
theory byte and no other test may change. One `/tmp` artifact is generated by
the code gate, section 8.6.

No class hierarchy, configuration file, registry, plugin table, supervisor,
governance or harness framework is authorized. Enums are literal frozen tuples
in the production module. All state is passed explicitly; there is no module
level mutable global.

### 1.2 Production import boundary

The production module may import exactly:

```text
phase2_stageb_schema
phase2_stageb_canonical
phase2_stageb_render
itertools
typing
__future__
```

and must be disjoint from:

```text
phase2_stageb_checker
phase2_stageb_generator
test_phase2_stageb_checker
test_phase2_stageb_generator
test_phase2_stageb_l0
test_phase2_stageb_theory_enumerability
peano
torch
proofsearch
policy
phase2_policy
phase2_search
phase2_root
phase2_isolated
phase2_actions
phase2_spec
transformers
numpy
random
secrets
os
subprocess
json
hashlib
hmac
```

`json` and `hashlib` are forbidden in production because canonical bytes and
hashes come only from the L0 helper; a second serializer or hash call site is a
gate failure. `random` and `secrets` are forbidden because L3 makes no random
choice at all: every operation in this annex is a deterministic function of its
inputs. `itertools` is admitted solely for `permutations`; the gate asserts no
other `itertools` attribute is referenced.

The production module must not import the L1 checker even though it is the
upstream authority: independence of the stage-5 re-derivation is the entire
point of `SEQUENT_REDERIVATION_MISMATCH`, and an import would make the
comparison self-confirming.

## 2. Item A - input and output contracts

### 2.1 What L3 consumes

L3 consumes exactly two objects, both already produced by a **successful** L1
check:

```text
plan             the checked plan, charter section 3.4, exactly the object that
                 check_plan accepted
checker_theorem  the value of check_plan(...)['theorem'], charter 5.1 shape
```

L3 consumes no generator metadata. In particular it never receives and never
reads `root_id`, `draw_index`, `target_band`, `target_node_count`,
`words_consumed`, `expectation`, `scaffold`, `dir`, `key_hex`, the L2 result
record, a certificate, a trace or a rejection history. The entry point takes two
positional parameters and no others; there is no keyword escape hatch, no
`**kwargs` and no context object.

L3 assumes, and does not re-verify, the L1 predicates. It is a contract
violation to pass an unchecked plan. The gate never does so, and section 2.5
states the fail-closed behaviour if a caller does.

### 2.2 Exact production signatures

```python
def canonical_theorem(theorem: Mapping) -> dict
def theorem_identity(theorem: Mapping) -> str
def canonical_plan(plan: Mapping, theorem: Mapping) -> dict
def exact_plan_identity(plan: Mapping, theorem: Mapping) -> str
def rule_skeleton(node: Mapping) -> dict
def skeleton_identity(plan: Mapping) -> str
def public_projection(canon_theorem: Mapping) -> dict
def rederive_theorem(plan: Mapping) -> dict
def identify(plan: Mapping, checker_theorem: Mapping) -> dict
```

`identify` is the pipeline stage-5 entry point and the only function the future
pipeline calls. The other eight are the named sub-steps, exposed so the gate can
test them in isolation; none of them reads or writes shared state.

`minimizing_renamings(theorem) -> tuple` is an internal helper, section 4.4,
exposed to the gate for the tie tests.

### 2.3 Exact success record

`L3_SUCCESS_KEYS`, in this exact order:

```text
('schema','ok','cause','theorem_identity','theorem_name',
 'exact_plan_identity','skeleton_identity','canonical_theorem',
 'canonical_plan','public_item')
```

```text
schema              = "philosophia.stageb.identity-projection.v1"
ok                  = True
cause               = None
theorem_identity    = lowercase 64-hex SHA-256, section 4.6
theorem_name        = "t_" + theorem_identity, 66 ASCII characters
exact_plan_identity = lowercase 64-hex SHA-256, section 5.6
skeleton_identity   = lowercase 64-hex SHA-256, section 6.4
canonical_theorem   = the exact 3-key object of section 4.5
canonical_plan      = the exact 5-key object of section 5.5
public_item         = the exact 5-key object of section 7.3
```

All values are plain nested `dict`/`list`/`str`/`int`/`bool`/`None`. There are
no dataclasses, no floats, no free-text fields and no extension keys.

`canonical_plan` is **dev-internal**. It carries the full proof tree and must
never be fed to a public projection or a public carrier record. Section 7.2
makes that structurally impossible rather than merely forbidden.

### 2.4 Exact failure record

`L3_FAILURE_KEYS`, in this exact order:

```text
('schema','ok','cause','subcause')
```

```text
schema   = "philosophia.stageb.identity-projection.v1"
ok       = False
cause    = "SEQUENT_REDERIVATION_MISMATCH"
subcause = member of L3_MISMATCH_SUBCAUSES
```

`SEQUENT_REDERIVATION_MISMATCH` is the only charter draw cause L3 owns, and L3
returns no other. L3 does not invent, refine or reorder any charter section 8
cause; the charter grants no sub-enum permission at stage 5, so the subcause
below is a **diagnostic field of the record**, not a new draw cause, and every
member collapses to the single charter cause.

`L3_MISMATCH_SUBCAUSES` is a literal frozen tuple, evaluated in this precedence
order, first failure wins:

```text
THEOREM_KEYSET_MISMATCH
THEOREM_ATOMS_MISMATCH
THEOREM_HYPOTHESES_MISMATCH
THEOREM_GOAL_MISMATCH
```

### 2.5 Fail-closed invariants that are not draw outcomes

Certain conditions are implementation defects, not draw outcomes. They are
detected fail-closed and raise `L3InvariantError(code)`, where `code` is a
member of the literal frozen tuple `L3_INVARIANT_CODES`:

```text
INPUT_NOT_L1_SHAPED
DECLARED_ATOM_COUNT_OUT_OF_RANGE
BIJECTION_BOUND_EXCEEDED
FORMULA_RECURSION_BOUND_EXCEEDED
PROOF_RECURSION_BOUND_EXCEEDED
SIZE_NORMALIZATION_MISMATCH
CANONICAL_THEOREM_PRECONDITION_VIOLATED
LOCAL_ID_NOT_UNIQUE
GLOBAL_ID_UNRESOLVED
```

`L3InvariantError` carries exactly one attribute, `code`, drawn from that tuple.
It carries no free text, no formatted message and no payload object.

Section 9 proves that none of these can fire on an L1-accepted plan. They exist
because a guard that cannot fire is still the correct response to an
implementation defect. The code gate exercises each by direct injection at the
internal function boundary, never by hunting for a fixture.

**Upstream note, carried to the driver.** Charter section 10 freezes a closed
list of `DEV_CORE_FEASIBILITY_STOP` reason codes containing `CHECKER_UNSOUND`,
`COMPILER_UNSOUND`, `PUBLIC_PROJECTION_LEAK`, `COLLISION_ACCOUNTING_ERROR` and
`NONDETERMINISM`, but no code for an identity-normalization defect. An
`L3InvariantError` at future dev-execution time therefore has no charter reason
code. This does not block the annex, the implementation or the code gate, all of
which run on fixed excluded fixtures where the gate asserts no raise occurs. The
smallest upstream correction is to append exactly one reason code,
`IDENTITY_NORMALIZATION_UNSOUND`, to charter section 10's closed list before any
dev execution is authorized. This annex does not design around the gap and does
not assign the condition to an ill-fitting existing code.

### 2.6 Deep copy, aliasing and input immutability

- Every formula, hypothesis record, proof node, list and dict placed into any
  returned object is freshly allocated by L3. No input sub-object is ever placed
  in an output.
- No input object is mutated. The gate asserts, for every fixture, that
  `canonical_bytes(plan)` and `canonical_bytes(checker_theorem)` are unchanged
  after every L3 call.
- No two positions in any single returned object share a mutable object. The
  gate walks each returned object collecting `id()` of every `dict` and `list`
  and asserts pairwise distinctness.
- Renaming and relabeling are implemented as pure constructors that build new
  nodes bottom-up; there is no in-place substitution anywhere in the module.

### 2.7 Bounds and totality

Derived, enforced as fail-closed guards:

```text
MAX_DECLARED_ATOMS            = 6        (from L0 schema)
MAX_BIJECTIONS                = 720      = 6!
MAX_FORMULA_RECURSION_FRAMES  = 24       = MAX_FORMULA_NODES
MAX_PROOF_RECURSION_FRAMES    = 38       = 37 plan nodes + 1 ASSUME leaf
```

Work bound. For `k` declared atoms there are exactly `k! <= 720` bijections.
Each bijection renames at most `37` proof nodes plus `1` goal plus at most `6`
hypothesis formulas, each formula at most `24` AST nodes, and serializes one
plan of at most a few kilobytes. Total work per plan is therefore bounded by
`720 * O(37 * 24)` node constructions and `720` canonical serializations, which
is small and constant-bounded. No search, no backtracking and no rejection loop
exists anywhere in L3; every function is a straight-line fold over a bounded
structure. L3 is total on L1-accepted input: it returns a success record, or a
`SEQUENT_REDERIVATION_MISMATCH` record, and cannot hang.

Recursion depth is at most `24` for formula recursion and at most `38` for proof
recursion, both far below the default interpreter limit. The 37-node plan bound
is guaranteed upstream by L1's band check (`8..37`), so no L3 path can exceed it
on accepted input.

## 3. Item A - stage-5 order of operations

`identify(plan, checker_theorem)` performs exactly these steps, in this order.
Any step that produces a mismatch returns immediately with the failure record of
section 2.4.

```text
S1  raw = rederive_theorem(plan)                       section 7.1
S2  compare raw with checker_theorem, before any
    canonicalization, by the precedence of 2.4         section 7.1
S3  ct = canonical_theorem(checker_theorem)            section 4
S4  tid = SHA-256 of canonical_bytes(ct)               section 4.6
S5  cp  = canonical_plan(plan, checker_theorem)        section 5
S6  pid = SHA-256 of canonical_bytes(cp)               section 5.6
S7  sk  = rule_skeleton(plan['proof'])                 section 6
S8  sid = SHA-256 of canonical_bytes(sk)               section 6.4
S9  item = public_projection(ct)                       section 7
S10 assemble the success record of 2.3
```

S2 occurs strictly before S3. The comparison is on **raw**, pre-canonical
objects, exactly as required: canonicalizing first would mask a hypothesis-set
or goal disagreement behind a common normal form.

## 4. Item B - alpha-canonical theorem identity

### 4.1 Input shape

`canonical_theorem` accepts a mapping whose key set is exactly
`('atoms', 'hypotheses', 'goal')`. Any other key set raises
`INPUT_NOT_L1_SHAPED`. `atoms` must be a list of `3..6` strings matching
`ATOM_NAME_RE`, duplicate-free and ascending; otherwise
`DECLARED_ATOM_COUNT_OUT_OF_RANGE` (for the cardinality) or
`INPUT_NOT_L1_SHAPED` (for anything else). `hypotheses` is a possibly empty list
of formulas; `goal` is a formula.

By Lemma D1 the atom set to be renamed is exactly `atoms`. No separate
occurrence scan is performed.

### 4.2 Exact bijection enumeration order

Let `src = tuple(theorem['atoms'])`, already ascending and duplicate-free, with
`k = len(src)`.

```text
BIJECTIONS(k) = tuple(itertools.permutations(range(k)))
```

`itertools.permutations(range(k))` yields the `k!` permutation tuples in
ascending lexicographic order of the tuple itself; that ordering is frozen here
as the enumeration order. The bijection at index `j` is

```text
sigma_j : src[i]  ->  'a' + str(BIJECTIONS(k)[j][i])     for i in 0..k-1
```

realised as a plain `dict` from source name to target name, built fresh per
bijection. `len(BIJECTIONS(k)) > MAX_BIJECTIONS` raises
`BIJECTION_BOUND_EXCEEDED`; it cannot occur for `k <= 6`.

The enumeration order is frozen for determinism of the **returned list** of
minimizing renamings. It cannot influence the minimum itself: the minimum of a
finite set of byte strings, and the set of arguments attaining it, are both
order-independent.

### 4.3 Recursive atom substitution

```text
subst(F, m):
  if F['kind'] == 'ATOM':  return {'kind': 'ATOM', 'name': m[F['name']]}
  if F['kind'] == 'FALSE': return {'kind': 'FALSE'}
  if F['kind'] == 'NOT':   return {'kind': 'NOT', 'arg': subst(F['arg'], m)}
  otherwise:               return {'kind': F['kind'],
                                   'left':  subst(F['left'], m),
                                   'right': subst(F['right'], m)}
```

`subst` allocates a new dict at every level and never mutates `F`. A missing key
in `m` is impossible by Lemma D1; if it occurs it raises `INPUT_NOT_L1_SHAPED`.
Recursion depth is bounded by `MAX_FORMULA_RECURSION_FRAMES`; exceeding it
raises `FORMULA_RECURSION_BOUND_EXCEEDED`.

### 4.4 Sorting, canonical object and minimum

For each bijection `sigma_j`:

```text
atoms_j = ['a0', ..., 'a{k-1}']
hyps_j  = the list of subst(H, sigma_j) for H in theorem['hypotheses'],
          sorted by canonical_bytes ascending
goal_j  = subst(theorem['goal'], sigma_j)
cand_j  = {'atoms': atoms_j, 'hypotheses': hyps_j, 'goal': goal_j}
bytes_j = canonical_bytes(cand_j)
```

Sorting is over **formula bytes only**. No hypothesis identifier, no plan field,
no generator field and no position index participates.

**Lemma B1 (the sort is a strict total order, no tie, no matching search).**
Fact 6 gives that the input global hypothesis formulas are pairwise
canonical-byte distinct. `subst` under a bijection is injective on formula
trees, because it is a relabeling by an injective map on atom names and is the
identity on structure. Therefore the renamed formulas are pairwise distinct, and
sorting their canonical bytes is a strict total order with no ties. Consequently
no factorial occurrence-assignment or bipartite matching over hypotheses is
introduced: the only combinatorial enumeration in L3 is the `k! <= 720` atom
bijections.

The theorem minimum is

```text
best   = min(bytes_j over all j)
MINSET = the tuple of j, in ascending j, with bytes_j == best
```

`canonical_theorem(theorem)` returns the `cand_j` for `j = MINSET[0]`. All `j`
in `MINSET` produce byte-identical `cand_j` by construction, so the choice of
representative cannot affect any output byte; `MINSET[0]` is named only so the
function is single-valued.

`minimizing_renamings(theorem)` returns `MINSET` together with the corresponding
substitution maps, for use by section 5.

### 4.5 Exact canonical theorem object

```text
{'atoms': ['a0', ..., 'a{k-1}'],
 'hypotheses': [F, ...],
 'goal': F}
```

Exactly three keys. `atoms` is the ascending canonical name list. `hypotheses`
holds formula objects only, in ascending canonical-byte order. This is exactly
charter section 5.1 step 3. Canonical bytes are `canonical_bytes` of that
object; the L0 serializer sorts keys, so the emission order of the three keys is
immaterial to bytes and is fixed above only for readability.

### 4.6 Identity and public name

```text
theorem_identity(theorem) = canonical_hash(canonical_theorem(theorem))
theorem_name              = 't_' + theorem_identity
```

lowercase 64-hex, so `theorem_name` is 66 ASCII characters. Charter section 5.1
requires all 64 hex characters; no truncation is authorized anywhere.

### 4.7 Required invariance proofs and their tests

**P-B1 input atom names cannot affect identity.** For any bijection `tau` of the
declared atoms, the theorem obtained by applying `tau` has candidate set
`{ subst(T, sigma o tau) }`, which ranges over exactly the same `k!` renamed
theorems. Hence the same minimum and the same identity. Test: for each of the
eleven excluded valid plans, apply every one of the `k!` atom permutations to
the whole plan, re-sort `atoms`, re-check with L1, and assert the theorem
identity is invariant.

**P-B2 input atom order cannot affect identity.** `plan['atoms']` is forced
ascending by fact 4, so the input order is not a free variable at all; P-B1
covers the only reachable variation.

**P-B3 hypothesis order and global identifiers cannot affect identity.** The
canonical theorem is built from `theorem['hypotheses']` after a total sort by
formula bytes, and reads no identifier. Test: permute `plan['hypotheses']` by
every permutation for the fixture's hypothesis count, relabel global identifiers
to a different admissible assignment, rewrite the `ASSUME` references, re-check
with L1, and assert the theorem identity is invariant.

**P-B4 no plan, generator or run metadata can enter.** Structural: the function
reads only `atoms`, `hypotheses`, `goal` of a 3-key mapping and raises on any
other key set. Test: for every name in `SEALED_FIELD_NAMES` (section 7.4),
attach the name to a copy of the theorem mapping and assert
`canonical_theorem` raises `INPUT_NOT_L1_SHAPED` rather than silently ignoring
it.

**P-B5 non-minimizing atom names cannot appear.** The returned canonical theorem
always has `atoms == ['a0', ..., 'a{k-1}']`. Test asserts it for every fixture.

## 5. Item C - exact plan identity

### 5.1 Scope of the renaming set

Charter section 5.2 operates over **every** atom renaming that attains the
minimum theorem bytes, that is `MINSET` of section 4.4. For each such renaming
the plan is normalized as below, its canonical bytes computed, and the
byte-minimum over `MINSET` is the exact plan identity's preimage.

### 5.2 Step 1: atom renaming of the whole plan

Apply `subst(-, sigma_j)` to: `plan['goal']`, every `hypotheses[i]['formula']`,
every proof node's `conclusion`, every `OR_ELIM` `left_assumption['formula']`
and `right_assumption['formula']`, and every `NOT_INTRO`
`assumption['formula']`. Set `atoms` to `['a0', ..., 'a{k-1}']`. Structure,
kinds and identifiers are untouched at this step.

### 5.3 Step 2: global hypothesis ordering and identifier reassignment

Sort the renamed hypothesis records by `canonical_bytes` of their `formula`,
ascending. By Lemma B1 this is a strict total order with no tie. Assign new
identifiers `h0, h1, ...` in that order, and record
`gmap : old_global_id -> new_global_id`.

The emitted `hypotheses` list is `[{'id': new_id, 'formula': renamed_formula}]`
in the sorted order, each record freshly allocated.

### 5.4 Step 3: local identifier renaming by preorder first introduction

```text
LOCAL-PREORDER(node, counter):
  if node['kind'] == 'OR_ELIM':
      mint(node['left_assumption']['id'])
      mint(node['right_assumption']['id'])
  elif node['kind'] == 'NOT_INTRO':
      mint(node['assumption']['id'])
  for field in PROOF_CHILD_FIELDS[node['kind']]:
      LOCAL-PREORDER(node[field], counter)
```

`mint(old)` assigns `lmap[old] = 'l' + str(counter)` and increments `counter`,
starting at `0`. Traversal starts at `plan['proof']`.

**Reading of the charter, stated rather than assumed.** Charter section 5.2 says
"Local IDs are assigned by preorder first introduction". A local identifier is
introduced by its binder record, and the binder record is a field of the binding
node, not of a child. A preorder traversal visits the binding node before any of
its children. Therefore all binders of a node are introduced at that node, in
the fixed field order `left_assumption` then `right_assumption` for `OR_ELIM`,
and `assumption` for `NOT_INTRO`. The rejected alternative reading, interleaving
binder minting with `PROOF_NODE_KEYS` field order so that binders inside
`major` are minted before `left_assumption`, is not adopted; it is recorded here
so review can see it was considered rather than overlooked. Both readings induce
**identical equivalence classes**, because each is a deterministic function of
the proof-tree shape alone; they differ only in which representative bytes are
recorded. The adopted reading is the one that matches "introduction".

**Binding and use.** `OR_ELIM` binds `left_assumption['id']` over
`left_branch` only, and `right_assumption['id']` over `right_branch` only;
`major` is outside both scopes. `NOT_INTRO` binds `assumption['id']` over `body`
only. L1 has already enforced that each binder is referenced inside its own
branch or body, and that all local identifiers are plan-wide distinct, so
`mint` is called exactly once per local identifier. A second `mint` of an
already-mapped identifier raises `LOCAL_ID_NOT_UNIQUE`.

The emitted assumption records are `{'id': lmap[old], 'formula': renamed}`,
freshly allocated.

### 5.5 Step 4: reference rewriting and the canonical plan object

Every `ASSUME` node's `hypothesis_id` is rewritten by `gmap` if it is a global
identifier and by `lmap` if it is a local identifier; which map applies is
decided by the L0 grammar predicates `is_global_id` / `is_local_id`, which are
mutually exclusive and exhaustive on an L1-accepted plan (fact 7). An identifier
in neither map raises `GLOBAL_ID_UNRESOLVED`.

The canonical plan object has exactly the five charter section 3.4 keys:

```text
{'schema': PLAN_SCHEMA_NAME,
 'atoms': ['a0', ..., 'a{k-1}'],
 'hypotheses': [{'id': 'h0', 'formula': F}, ...],
 'goal': F,
 'proof': ProofNode}
```

Every proof node retains its exact `PROOF_NODE_KEYS` key set and its exact child
field order; only `conclusion`, assumption `formula`, assumption `id` and
`hypothesis_id` values change. No child is reordered, sorted or dropped. In
particular the exact plan identity, unlike the skeleton, does **not** sort
`AND_INTRO` children or `OR_ELIM` branches.

### 5.6 Step 5: byte-minimum, identity, and the size assertion

```text
for j in MINSET:  cp_j = the canonical plan for sigma_j
canonical_plan(plan, theorem) = the cp_j with the byte-minimum
                                canonical_bytes; ties are byte-identical
exact_plan_identity           = canonical_hash of those bytes
```

Because all `j` in `MINSET` yield byte-equal canonical theorems but may yield
different canonical plans, the minimum here is a real selection. Ties among
`cp_j` are byte-identical by definition of minimum, so the choice of
representative index cannot affect output bytes.

**Size before equals size after.** Charter section 5.2 requires that the plan
node count computed on the checked tree equals the count after identity
normalization. L3 computes the inference node count independently, by the
charter section 2.2 definition, on the input `plan['proof']` and on the emitted
`canonical_plan['proof']`, and raises `SIZE_NORMALIZATION_MISMATCH` if they
differ. This cannot fire: renaming and relabeling change only leaf strings and
assumption records, never a node kind and never a child edge, so the count is
preserved node for node. The guard is a defect detector; its disposition is
section 2.5, not a draw cause.

### 5.7 Required invariance proofs and their tests

**P-C1 alpha invariance.** Applying any atom bijection to the whole plan leaves
the exact plan identity unchanged, because the candidate set over `MINSET` is
the same set of renamed plans. Test: exhaustive over all `k!` permutations for
each of the eleven excluded valid plans.

**P-C2 hypothesis permutation and global relabeling invariance.** The canonical
plan sorts hypotheses by renamed formula bytes and reassigns identifiers, so any
input order and any admissible identifier assignment collapse to the same
output. Test as in P-B3, additionally asserting the exact plan identity.

**P-C3 local relabeling invariance.** `LOCAL-PREORDER` reads only node kinds and
the child structure, never the incoming identifier strings, so any admissible
relabeling of local identifiers yields the same output. Test: for each fixture,
apply a shifting relabeling `lN -> l{N+100}` and a reversing relabeling, re-check
with L1, and assert the identity is unchanged.

**P-C4 a real proof-tree change remains distinguishable.** Test pairs that must
produce **different** exact plan identities: swapping the two `AND_INTRO`
children where their subtrees differ; replacing an `AND_ELIM_LEFT` by an
`AND_ELIM_RIGHT` where both are well-typed; lengthening an elimination chain by
one node; exchanging an `OR_ELIM` `major` subproof with a branch subproof. Each
pair is L1-checked before comparison, so a difference is a genuine plan
difference and not a schema artifact.

## 6. Item D - rule-skeleton identity

### 6.1 Exact recursive schema

`rule_skeleton(node)` is a pure function of a schema-valid proof node. It needs
no scope tracking: whether an `ASSUME` is global or local is decided by the L0
grammar predicates on `hypothesis_id` alone (fact 7), and the two namespaces are
disjoint by grammar.

```text
ASSUME with is_global_id(hypothesis_id) -> {'kind': 'ASSUME_GLOBAL'}
ASSUME with is_local_id(hypothesis_id)  -> {'kind': 'ASSUME_LOCAL'}

AND_INTRO      -> {'kind': 'AND_INTRO',
                   'children': SORT2(sk(left), sk(right))}
AND_ELIM_LEFT  -> {'kind': 'AND_ELIM',  'children': [sk(source)]}
AND_ELIM_RIGHT -> {'kind': 'AND_ELIM',  'children': [sk(source)]}
OR_INTRO_LEFT  -> {'kind': 'OR_INTRO',  'children': [sk(source)]}
OR_INTRO_RIGHT -> {'kind': 'OR_INTRO',  'children': [sk(source)]}
OR_ELIM        -> {'kind': 'OR_ELIM',
                   'children': [sk(major)]
                               + SORT2(sk(left_branch), sk(right_branch))}
NOT_INTRO      -> {'kind': 'NOT_INTRO', 'children': [sk(body)]}
NOT_ELIM       -> {'kind': 'NOT_ELIM',  'children': [sk(negative), sk(positive)]}
EXFALSO        -> {'kind': 'EXFALSO',   'children': [sk(source)]}
```

Leaf skeletons have exactly one key; internal skeletons have exactly two. The
erased kind alphabet is the literal frozen tuple

```text
SKELETON_KINDS = ('ASSUME_GLOBAL','ASSUME_LOCAL','AND_INTRO','AND_ELIM',
                  'OR_INTRO','OR_ELIM','NOT_INTRO','NOT_ELIM','EXFALSO')
```

`SORT2(a, b)` returns `[a, b]` if `canonical_bytes(a) <= canonical_bytes(b)`
else `[b, a]`. It compares serialized bytes only. It never consults object
identity, memory address, input position or construction order, so equal
children produce a byte-identical result either way and the tie is resolved
without any hidden dependence.

Formulas, atom names, hypothesis identifiers, assumption records and node
`conclusion` fields are never read. Direction is erased for `AND_ELIM_*` and for
`OR_INTRO_*`. All child order other than the two mandated sorts is preserved:
`NOT_ELIM` keeps `negative` before `positive`, and `OR_ELIM` keeps `major`
first.

### 6.2 The `OR_ELIM` branch-pair rule, stated exactly

Charter section 5.3 requires that the two branch skeletons be sorted as a pair
and that no branch be exchanged independently of its local assumption. Under the
erasure above, an assumption record contributes **nothing** to the skeleton: its
`id` and `formula` are both erased and it has no other field. The branch unit is
therefore exactly the branch proof skeleton, and sorting the two branch
skeletons is literally sorting the two units. This annex implements the clause
as written and does not add a phantom assumption token to the skeleton, which
would leak a retained distinction the charter erases.

The clause is not vacuous as a review obligation. The gate must assert both
directions: that exchanging `(left_assumption, left_branch)` with
`(right_assumption, right_branch)` as a pair leaves the skeleton identity
unchanged, and that changing the shape of one branch changes it.

### 6.3 Skeleton is computed on the checked plan

`skeleton_identity(plan) = canonical_hash(rule_skeleton(plan['proof']))`.

Because every field the skeleton reads is a node kind or a child edge, and
neither atom renaming nor identifier relabeling changes any of those, the
skeleton of the checked plan and the skeleton of the canonical plan of section 5
are byte-identical. The gate asserts this equality for every fixture, so the
choice of input is not a hidden decision.

### 6.4 Identity

```text
skeleton_identity = canonical_hash(rule_skeleton(plan['proof']))
```

lowercase 64-hex.

### 6.5 Mandatory mutation pairs

Mutations operate directly on proof-node subtrees passed to `rule_skeleton`,
which is total on any schema-valid node. Whole-plan invariance is covered
separately by section 10. Each pair names the expected relation.

Erasure pairs, which must produce **equal** skeleton bytes:

```text
X1  atom name changed throughout a subtree
X2  a hypothesis formula replaced by any other schema-valid formula
X3  a global hypothesis identifier relabeled h0 -> h7
X4  a local identifier relabeled l0 -> l9 in binder and use together
X5  AND_ELIM_LEFT replaced by AND_ELIM_RIGHT at the same position
X6  OR_INTRO_LEFT replaced by OR_INTRO_RIGHT at the same position
X7  a node conclusion replaced by any other schema-valid formula
X8  an OR_ELIM assumption formula replaced by any other formula
X9  AND_INTRO children exchanged
X10 OR_ELIM (assumption, branch) units exchanged as pairs
```

Retention pairs, which must produce **different** skeleton bytes:

```text
Y1  ASSUME_GLOBAL replaced by ASSUME_LOCAL at the same position
Y2  NOT_ELIM negative and positive exchanged, with structurally different
    children, since that order is preserved
Y3  a subproof moved from OR_ELIM major into a branch
Y4  one AND_INTRO child's shape changed
Y5  one OR_ELIM branch's shape changed
Y6  an AND_ELIM chain lengthened by one node
Y7  EXFALSO replaced by NOT_ELIM
Y8  NOT_INTRO replaced by OR_INTRO
```

X9 and X10 are the sorted-position pairs; Y4 and Y5 prove the sorts do not
collapse genuinely different multisets. Y2 is the explicit proof that
`NOT_ELIM` order is retained, and must use children with different shapes,
because a `NOT_ELIM` whose two children have equal skeletons is legitimately
symmetric.

## 7. Item E - re-derivation, projection and the mismatch boundary

### 7.1 Independent raw re-derivation and `SEQUENT_REDERIVATION_MISMATCH`

```text
rederive_theorem(plan) =
  {'atoms':      [fresh copy of each name in plan['atoms']],
   'hypotheses': [deep copy of h['formula'] for h in plan['hypotheses']],
   'goal':       deep copy of plan['goal']}
```

This reads only the plan's **public** fields: the declared atom list, the global
hypothesis formulas in plan order, and the goal. It does not walk the proof, does
not re-derive any conclusion and does not import the checker. It is therefore a
genuinely independent path: the checker builds its theorem's goal from the root
node's re-derived conclusion, whereas L3 builds it from `plan['goal']`. A
disagreement between the two is exactly a sequent re-derivation mismatch.

Comparison, in the precedence order of section 2.4, on raw objects before any
canonicalization:

```text
if key set of checker_theorem != ('atoms','hypotheses','goal'):
      THEOREM_KEYSET_MISMATCH
elif canonical_bytes(raw['atoms'])      != canonical_bytes(ct['atoms']):
      THEOREM_ATOMS_MISMATCH
elif canonical_bytes(raw['hypotheses']) != canonical_bytes(ct['hypotheses']):
      THEOREM_HYPOTHESES_MISMATCH
elif canonical_bytes(raw['goal'])       != canonical_bytes(ct['goal']):
      THEOREM_GOAL_MISMATCH
```

Each comparison is on canonical bytes of the sub-object, so list order is
significant for `atoms` and `hypotheses`, which is correct: at this stage no
sorting has occurred and a reordered hypothesis list from a defective caller is
a real disagreement worth catching.

**Vacuous charter clause, recorded not silently dropped.** Charter section 4
assigns L3 the duty of comparing the independently rendered public sequent with
"any later generator-supplied rendering". The accepted L2 generator emits no
surface syntax and supplies no rendering (fact 11), so there is no second
rendering to compare against and this branch of the duty has no reachable input
under the accepted L2. L3 still renders the canonical sequent for the public
item, section 7.3. If a future layer ever supplies a rendering, the comparison
belongs here and yields `SEQUENT_REDERIVATION_MISMATCH`; this annex authorizes
no such input and adds no speculative parameter for it.

### 7.2 Structural impossibility of metadata entering the projection

```python
def public_projection(canon_theorem: Mapping) -> dict
```

Exactly one parameter. There is no second parameter, no keyword argument, no
`**kwargs`, no default carrying a mutable object and no module-level mutable
state. The theory and premise constants are read from the accepted L0 schema
module as frozen literals (`THEORY_SHA256`, `THEORY_PREMISES`), not passed in.

Sealed metadata therefore cannot enter by any call path: it is not in the
signature. The function additionally enforces a precondition, so that only the
output of section 4.5 can be projected:

```text
key set is exactly ('atoms','hypotheses','goal')
atoms == ['a0', ..., 'a{k-1}'] for some k in 3..6
hypotheses is a list of formulas whose canonical bytes are strictly ascending
goal is a schema-valid formula
every atom occurring in hypotheses or goal is in atoms
```

Violation raises `CANONICAL_THEOREM_PRECONDITION_VIOLATED`. In particular a raw,
non-canonical theorem cannot be projected, and a theorem mapping carrying an
extra key is refused rather than silently ignored.

### 7.3 Exact public item

Charter section 6 key order, exactly five keys:

```text
PUBLIC_ITEM_KEYS = ('schema','theory_sha256','premises','theorem_name','goal')
```

```text
schema        = "philosophia.stageb.public-item.v1"
theory_sha256 = phase2_stageb_schema.THEORY_SHA256
premises      = list(phase2_stageb_schema.THEORY_PREMISES)
                = ["and_i","and_el","and_er","or_il","or_ir","or_e",
                   "not_i","not_e","exfalso"]
theorem_name  = "t_" + canonical_hash(canon_theorem)
goal          = render_sequent(canon_theorem['atoms'],
                               canon_theorem['hypotheses'],
                               canon_theorem['goal'])
```

The only renderer invoked is the accepted L0 `render_sequent`, on the canonical
atoms, canonical-order hypotheses and canonical goal. No second renderer, no
string formatting of formulas and no manual sequent assembly exists in L3.

The key named `goal` holds the **entire rendered sequent**, not the goal formula
alone. That is charter section 6 as written ("The public record stores the
rendered ASCII string"). The naming is inherited from the charter and is not
changed here; the gate asserts the value begins with `[` and ends with `]` and
equals `render_sequent` of the canonical theorem.

### 7.4 Sealed fields and hold-theorem-fixed proofs

`SEALED_FIELD_NAMES` is a literal frozen tuple enumerating every field the
charter section 6 seals, plus every field the accepted L2 record actually
carries:

```text
root_key, root_id, draw_index, target_band, band, target_node_count,
node_count, max_dependency_depth, families, plan_size, plan, canonical_plan,
proof, trace, skeleton, skeleton_identity, exact_plan_identity, scaffold,
dir, generator_stratum, words_consumed, key_hex, canonical_result_sha256,
raw_plan_sha256, raw_theorem_sha256, expectation, certificate, rejection,
subcause, cause, fixture_name
```

Three independent proofs, each with a test:

**P-E1 signature proof.** `public_projection` has exactly one parameter. Test
asserts the parameter count and names via `inspect.signature`, and asserts the
production source contains no `**` parameter.

**P-E2 refusal proof.** For every name in `SEALED_FIELD_NAMES`, attaching that
key to a copy of a canonical theorem and calling `public_projection` raises
`CANONICAL_THEOREM_PRECONDITION_VIOLATED`. Pollution is refused, never ignored.

**P-E3 hold-theorem-fixed proof.** For each excluded valid fixture, construct a
family of plans that all share one canonical theorem but differ maximally as
plans: every atom permutation, every hypothesis permutation with global
relabeling, and two local relabelings. Each family member is L1-checked, then
projected. Assert that `canonical_bytes(public_item)` is identical across the
whole family. This holds the theorem fixed while varying everything a sealed
field could describe, and is the test the charter section 6 obligation names.

### 7.5 Leak mutations

Each mutation is applied to a copy of `public_projection` inside the test, never
to the production module, and must fail an explicit gate assertion:

```text
L1  add a 'root_id' key to the emitted item
L2m add a 'draw_index' key
L3m add a 'target_band' key
L4  add a 'node_count' or 'plan_size' key
L5  add a 'plan' key carrying the canonical plan
L6  add a 'trace' key
L7  add a 'skeleton_identity' key
L8  add a 'scaffold' or 'dir' key, the generator-stratum leak
L9  add a 'certificate' key
L10 add a 'rejection' or 'subcause' key
L11 replace theorem_name by a truncated 16-hex form
L12 replace the rendered sequent by a rendering of a non-canonical atom order
```

The gate asserts, for every fixture, that the emitted key tuple equals
`PUBLIC_ITEM_KEYS` exactly and that the canonical bytes match a value recomputed
from the canonical theorem alone. L11 and L12 are included because they are
leaks of a different shape: L11 weakens the identity, L12 leaks input ordering
into public bytes.

A leak is `PUBLIC_PROJECTION_LEAK`, which charter section 10 lists under
`DEV_CORE_FEASIBILITY_STOP`. At this stage it is a **code-gate failure**, not a
generated scientific outcome and not a dev terminal, because no dev item exists
and no root is minted.

## 8. Item F - exclusion materialization, identity ledger V4

### 8.1 What V4 is

V4 is a canonical-JSON artifact that preserves every V3 row and every V3
provenance field unchanged, and adds final L3 identities exactly where they are
defined. V4 never removes, renames or rewrites a V3 field. The gate reverifies
the V3 file hash `a1f907ad6665b7c96d91496c5a91d32f0f0cae63da48b6b26da6b292d48f528d`
before reading it.

### 8.2 The three fixture classes and what is defined for each

**Class 1: eleven `valid_plan_fixtures`, five L1 hand fixtures plus six L2 gate
fixtures.** Each has a real ND plan object with `3..6` declared atoms and an L1
acceptance. For each, the gate reconstructs the plan, verifies
`canonical_hash(plan) == raw_plan_sha256` and
`canonical_hash(check_plan(...)['theorem']) == raw_theorem_sha256`, and only
then records theorem identity, theorem name, exact plan identity and skeleton
identity.

**Class 2: two `renderer_only_fixtures`.** Charter section 6 states these are
"two-atom renderer-only syntax fixtures, not admitted dev plans". They have no
ND plan object, and two declared atoms is below `MIN_DECLARED_ATOMS = 3`, so
charter section 5.1's bijection over "the 3..6 used atoms" is undefined for
them. **No theorem identity, no exact plan identity and no skeleton identity is
defined or recorded.** Their exclusion mechanism remains exactly what V3
records: the raw ASCII sequent hash and the canonical-JSON-string sequent hash,
both retained verbatim.

**Class 3: seventeen `enumerability_fixtures`.** These are hand-written Peano
premise witnesses and ambient-arrow chains at depths 1..8. They are not ND plans
and not ND theorem objects at all. **No L3 identity is defined or recorded.**
Both raw hashes are retained verbatim.

This annex does not derive a theorem or skeleton identity from a raw hash. A
hash of a rendered sequent is not a charter section 5.1 canonical theorem, and
claiming otherwise would fabricate an identity for an object that does not
exist.

**Reading of the L0/L1 closure, stated rather than assumed.** The L0/L1 v3
closure says "L3 must deduplicate their theorem identity while retaining both
provenance aliases" of `premise_witness_or_e` and `renderer_or_commute`. Charter
section 5.1 cannot define a theorem identity for a two-atom surface sequent, so
the only consistent reading is that the deduplication is of the **shared raw
excluded sequent**, which fact 10 confirms is byte-identical under both
provenance names. V4 implements exactly that: one alias group over the shared
raw hashes, two retained provenance rows, and no invented theorem identity. This
reading is carried to the driver as a wording clarification, section 12.

### 8.3 Exact V4 schema

Top-level key set, exactly:

```text
('schema','charter_sha256','source_v3_sha256','l2_annex_sha256',
 'l2_code_gate_sha256','sequent_hash_kinds',
 'permanently_excluded_fixture_key_hex','identity_undefined_reasons',
 'valid_plan_fixtures','renderer_only_fixtures','enumerability_fixtures',
 'alias_groups','stage6_seed')
```

```text
schema = "philosophia.stageb.identity-exclusions.v4"
```

`charter_sha256`, `sequent_hash_kinds` and
`permanently_excluded_fixture_key_hex` are copied verbatim from V3.
`source_v3_sha256`, `l2_annex_sha256` and `l2_code_gate_sha256` are the pinned
hashes of section 0.

`identity_undefined_reasons` is the literal frozen tuple, emitted as a list:

```text
('NO_ND_PLAN_OBJECT_TWO_ATOM_RENDERER_SURFACE',
 'NO_ND_PLAN_OBJECT_PEANO_ENUMERABILITY_WITNESS')
```

Each `valid_plan_fixtures` row has exactly these keys:

```text
('fixture_name','source','raw_plan_sha256','raw_theorem_sha256',
 'declared_atom_count','identity_status','theorem_identity_sha256',
 'theorem_name','exact_plan_identity_sha256','skeleton_identity_sha256')
```

`source` is `'L1_HAND_FIXTURE'` or `'L2_CODE_GATE_FIXTURE'`.
`identity_status` is `'DEFINED'`. `raw_plan_sha256` and `raw_theorem_sha256` are
copied from V3 and independently reverified, never recomputed into the row from
a fresh object without comparison.

Each `renderer_only_fixtures` and `enumerability_fixtures` row has exactly:

```text
('fixture_name','raw_ascii_sequent_sha256','canonical_json_string_sha256',
 'identity_status','identity_undefined_reason')
```

`identity_status` is `'NOT_DEFINED'`; `identity_undefined_reason` is the
matching member of `identity_undefined_reasons`.

Each `alias_groups` row has exactly:

```text
('raw_ascii_sequent_sha256','canonical_json_string_sha256','members',
 'identity_status','identity_undefined_reason')
```

`members` is the ascending-sorted list of fixture names sharing those raw
hashes. For the accepted V3 content this yields exactly one alias group,
`['premise_witness_or_e','renderer_or_commute']`, with
`identity_status = 'NOT_DEFINED'`.

`stage6_seed` has exactly:

```text
('seed_scope','source_fixture_names','theorem_identities',
 'skeleton_identities','theorem_identity_members','skeleton_identity_members',
 'precedence')
```

```text
seed_scope   = the author-choice value of AC-1, section 11
precedence   = ['THEOREM_ID_COLLISION','SKELETON_ID_COLLISION']
```

`theorem_identities` and `skeleton_identities` are ascending-sorted,
duplicate-free lists of the 64-hex identities in scope.
`theorem_identity_members` and `skeleton_identity_members` are objects mapping
each identity to the ascending-sorted list of fixture names carrying it; an
identity carried by more than one fixture appears once in the identity list and
with all members here. This is the deterministic deduplication and alias
accounting: the seed is a **set**, the membership map preserves provenance, and
neither depends on input order or object identity.

All lists whose order is not otherwise fixed are ascending-sorted by their
ASCII bytes, so V4 canonical bytes are a pure function of its content.

### 8.4 Stage-6 collision precedence, defined but not executed

For a future consumed dev draw at charter section 8 stage 6, with cumulative
sets seeded by `stage6_seed`:

```text
if theorem_identity is in the cumulative theorem set:  THEOREM_ID_COLLISION
elif skeleton_identity is in the cumulative skeleton set: SKELETON_ID_COLLISION
else: accept and add both identities to the cumulative sets
```

Theorem first, then skeleton, matching charter section 8's cause order and its
"first failing stage only" attribution. L3 defines this precedence and produces
the seed. **L3 evaluates no draw now.** No dev draw exists, no root is minted,
and the code gate performs no stage-6 evaluation beyond asserting the seed's
internal consistency.

### 8.5 How the gate obtains real fixture objects without production importing tests

Production imports no test module and no generator (section 1.2). The **test**
module may, and must:

- import `test_phase2_stageb_checker.VALID_PLAN_BUILDERS` for the five L1 hand
  fixtures and their `expectation_for` helper;
- import `phase2_stageb_generator.generate_draw` and call it on exactly the six
  literal `(key_hex, draw_index)` rows read from the frozen code-gate artifact
  `PHASE2_STAGE_B_L2_CODE_GATE_V1.json`, whose hash it reverifies first;
- import `phase2_stageb_checker.check_plan` to re-establish L1 acceptance.

The test module must **never** run the frozen selector scan, must never call
`generate_draw` on any key or index outside those six literal rows, and must
never mint or derive a key. The six rows are read as data; no scan loop appears
in the test.

Order of operations, mandatory:

```text
1 verify the V3 file hash and the code-gate file hash
2 reconstruct all eleven plans
3 for each, assert canonical_hash(plan) == the V3 raw_plan_sha256
4 for each, run check_plan and assert ok, then assert
  canonical_hash(theorem) == the V3 raw_theorem_sha256
5 only then compute L3 identities and emit V4
```

If any hash in steps 1, 3 or 4 disagrees, the gate fails and no V4 is emitted.
Identities are never added to a row whose raw hashes were not first reverified.

### 8.6 Artifact path

```text
/tmp/PHASE2_STAGE_B_L3_IDENTITY_EXCLUSIONS_V4.json
```

Emitted by the code gate only, with `canonical_dumps` plus a single trailing
newline. It is a code-gate artifact produced after implementation is authorized,
never a prerequisite to authorizing it. Its SHA-256 is recorded in the L3
closure.

## 9. Feasibility and totality on paper

**T1 no unbounded work.** Every L3 loop is over a finite structure fixed before
the loop: `k! <= 720` bijections, at most `6` hypotheses, at most `37` proof
nodes, at most `24` formula nodes. There is no rejection loop, no retry, no
backtracking and no fixed-point iteration.

**T2 no invariant guard can fire on L1-accepted input.**
`INPUT_NOT_L1_SHAPED` is excluded by the checker's schema pass;
`DECLARED_ATOM_COUNT_OUT_OF_RANGE` by `MIN/MAX_DECLARED_ATOMS`;
`BIJECTION_BOUND_EXCEEDED` by `k <= 6`;
`FORMULA_RECURSION_BOUND_EXCEEDED` by `MAX_FORMULA_NODES = 24`;
`PROOF_RECURSION_BOUND_EXCEEDED` by the band bound `node_count <= 37`;
`SIZE_NORMALIZATION_MISMATCH` by section 5.6's structure-preservation argument;
`CANONICAL_THEOREM_PRECONDITION_VIOLATED` because the only production caller of
`public_projection` is `identify`, which passes the output of section 4.5;
`LOCAL_ID_NOT_UNIQUE` by L1's plan-wide local uniqueness;
`GLOBAL_ID_UNRESOLVED` by L1's identifier grammar and hypothesis-resolution
checks.

**T3 the only reachable failure is the stage-5 mismatch.** Consequently
`identify` is total on L1-accepted input, returning a success record or a
`SEQUENT_REDERIVATION_MISMATCH` record.

**T4 what this does not establish.** It does not establish that any dev quota
can be filled, that any theorem is interesting, minimal or hard, that L4 can
compile any of these plans, or that the identity population is diverse. Those
are later measurements owned by later layers, and the L3 gate must not report
them.

## 10. Item G - the code gate

Fixed excluded fixtures only. No new key, no scan, no root, no outcome. Every
assertion below is mandatory.

### 10.1 Alpha-permutation invariance, exhaustive

For each of the eleven excluded valid plans, for **every** one of the `k!`
permutations of its declared atoms: rename the whole plan, re-sort `atoms`,
assert `check_plan` still accepts, and assert that the theorem identity, the
exact plan identity, the skeleton identity and the canonical public item bytes
are all unchanged. For the five L1 fixtures `k = 3`, so this is `6` permutations
each; for the L2 fixtures `k` is `3..6`, so at most `720` each. The total is
bounded and small.

### 10.2 Hypothesis permutation and global-identifier invariance

For each fixture, for every permutation of its hypothesis list, and for a
second admissible global-identifier assignment, rewrite the `ASSUME` references,
assert `check_plan` accepts, and assert theorem identity, exact plan identity,
skeleton identity and public bytes are unchanged.

### 10.3 Local-identifier alpha invariance

For each fixture, apply a shifting relabeling and a reversing relabeling of all
local identifiers, in binder and use together, assert `check_plan` accepts, and
assert all three identities and the public bytes are unchanged.

### 10.4 Theorem mismatch mutation

For each fixture, construct a `checker_theorem` copy that differs in exactly one
of: key set, `atoms` list, `hypotheses` list, `goal`. Assert `identify` returns
the failure record with `L3_FAILURE_KEYS` exactly,
`cause == 'SEQUENT_REDERIVATION_MISMATCH'`, and the expected subcause by the
precedence of section 2.4. Assert no identity fields are present in the failure
record.

### 10.5 Public leak mutations

Every mutation of section 7.5, plus P-E1, P-E2 and P-E3 of section 7.4.

### 10.6 Skeleton erasure and retention mutations

Every pair X1..X10 and Y1..Y8 of section 6.5, including the `OR_ELIM`
branch-pair equality X10 and the branch-shape difference Y5. Additionally assert
`rule_skeleton(plan['proof'])` equals `rule_skeleton(canonical_plan['proof'])`
byte-for-byte for every fixture, and that every emitted skeleton node's `kind`
is a member of `SKELETON_KINDS` and its key set is exactly `('kind',)` or
`('kind','children')`.

### 10.7 No-alias and input-unchanged checks

For every fixture and every entry point: assert the input plan and theorem
canonical bytes are unchanged after the call; assert no returned object shares a
`dict` or `list` identity with any input sub-object; assert every returned
object's internal `dict`/`list` identities are pairwise distinct.

### 10.8 Fresh-process determinism

For every fixture, two fresh interpreters launched with different
`PYTHONHASHSEED` values must produce byte-identical canonical bytes for the
canonical theorem, canonical plan, skeleton, public item and V4 artifact. The
gate compares SHA-256 of those bytes. This is the standing guard against any
set- or dict-iteration order leaking into an identity.

### 10.9 V3 reverification and V4 accounting

All eleven V3 raw plan hashes and all eleven V3 raw theorem hashes reverified
before any identity is computed, per section 8.5. Then: V4 canonical bytes
reproducible across two independent constructions in one process and across
fresh processes; every V3 row present in V4 with its fields unchanged; every
class-2 and class-3 row carrying `identity_status == 'NOT_DEFINED'` and a valid
reason; exactly one alias group with members
`['premise_witness_or_e','renderer_or_commute']`; `stage6_seed` identity lists
ascending, duplicate-free, and equal to the deduplicated union of the in-scope
rows; every identity in `theorem_identity_members` and
`skeleton_identity_members` present in the corresponding identity list and vice
versa; and the number of distinct skeleton identities plus the number of alias
members accounted exactly against the row count.

### 10.10 Import graph and source discipline

Parse `learning/phase2_stageb_identity.py` with `ast` and assert the imported
top-level module set is a subset of the allowlist and disjoint from the
forbidden list of section 1.2. Assert the production source contains none of the
substrings `generate_draw`, `check_plan`, `randbelow`, `root_key`, `draw_index`,
`json.dumps`, `hashlib`, `secrets`, `os.urandom`. Assert `itertools` is used
only for `permutations`. Assert the test module imports the L1 checker, the L1
fixture builders and the generator, and that it contains no scan loop over draw
indices beyond the six literal rows.

### 10.11 Patch routes and regression gates

- new delta over the accepted V5 cumulative:
  `minimo_phase2_stageb_l3_v1_delta.patch`;
- new cumulative over the pinned MINIMO base:
  `minimo_phase2_stagea_stageb_l01_l2_l3_v1_cumulative.patch`.

Both must `git apply --check` clean on
`6066f482c6752915ad21119f93dc162f4cb9db72` in the documented order, both must be
`git diff --check` clean, and both routes must yield byte-identical trees. The
delta must name exactly the two authorized paths of section 1.1, both as new
files. Stage-A must remain unchanged and pass unchanged; the accepted Stage-B
`67/67` baseline must still pass unchanged, with the L3 module adding its own
tests on top. The new total is whatever is measured after implementation; any
count stated before the run is an invention and must not appear.

## 11. Author choice

Exactly one bounded choice remains open. It is stated in full in
`PHASE2_STAGE_B_L3_IDENTITY_PROJECTION_ANNEX_V1_AUTHOR_CHOICES.md` and
summarized here.

**AC-1, pipeline stage-6 exclusion seed scope.** Charter section 8 says stage 6
is "seeded by registered L0/L1 hand-fixture identities", which names five
fixtures. Charter section 5.3 says every dev theorem and skeleton is permanently
ineligible for later scopes, and the L2 V5 closure requires L3 to "import the
complete V3 exclusion set", which contains eleven valid-plan rows. The two
readings differ in whether the six L2 gate fixtures seed stage 6, which changes
collision precedence outcomes and fixture eligibility for every future dev draw.
This annex does not resolve it silently. `stage6_seed.seed_scope` records the
recorded decision.

## 12. Handoff obligations and recorded upstream notes

1. **To L4.** L4 consumes a checker-accepted plan. If L4 wishes a canonical
   input, `canonical_plan` of section 5.5 is the defined object; L3 asserts only
   that its node count equals the checked tree's. L3 supplies no compiled
   action, no replay and no query measurement.
2. **Upstream note U1, missing reason code.** Charter section 10's closed
   `DEV_CORE_FEASIBILITY_STOP` list has no code for an identity-normalization
   defect. Smallest correction: append `IDENTITY_NORMALIZATION_UNSOUND`. Not
   blocking for the annex, the implementation or the fixture gate.
3. **Upstream note U2, closure wording.** The L0/L1 v3 closure's phrase
   "deduplicate their theorem identity" for the
   `premise_witness_or_e` / `renderer_or_commute` pair cannot mean a charter
   section 5.1 theorem identity, because the shared object is a two-atom surface
   sequent and section 5.1 is defined only for `3..6` used atoms. Section 8.2
   adopts the only consistent reading, deduplication of the shared raw excluded
   sequent with both provenance rows retained. Smallest correction: reword the
   closure sentence to say "raw excluded sequent" rather than "theorem
   identity". Not blocking.
4. **Upstream note U3, vacuous rendering comparison.** Charter section 4's L3
   duty to compare a generator-supplied rendering has no reachable input under
   the accepted L2, which emits no surface syntax. Recorded in section 7.1; no
   correction is required, and no speculative parameter is added.
5. **Prospective risk R1, skeleton collision density.** Under the frozen A/B/C
   catalogue, a plan's skeleton is determined by the scaffold, the unordered
   pair of the first two chain lengths and the third chain length, because the
   frame's `AND_INTRO` children are sorted and elimination direction is erased.
   The reachable skeleton space per band is therefore far smaller than the draw
   budget, so `SKELETON_ID_COLLISION` is expected to reject a substantial
   fraction of later dev draws, and charter section 10's `ROOT_QUOTA_UNFILLED`
   is a live prospective risk. This is a structural observation from the frozen
   catalogue and the frozen skeleton rule; it is **not** a measurement, no draw
   was generated, and nothing here may be reported as yield or band
   reachability. It is recorded so the later quota owner is not surprised, and
   it must not be used to alter the catalogue, the skeleton rule or the quota
   within this charter version.
6. **No claims from fixtures.** Nothing in the L3 gate may be reported as
   generator yield, band reachability, quota fill, interface survival,
   scientific suitability or ACTIVE/YOKED evidence. The gate demonstrates
   identity well-definedness, projection tightness and exclusion accounting on
   specific permanently excluded fixtures, and nothing else.

## 13. Staging, review and mandatory stop

1. This annex plus the recorded AC-1 decision receive joint independent X/Y
   review. Acceptance authorizes exactly the two files of section 1.1 and
   nothing else.
2. Builder implements those two files.
3. The code gate of section 10 runs and emits
   `/tmp/PHASE2_STAGE_B_L3_IDENTITY_EXCLUSIONS_V4.json`.
4. Work stops for driver review and an independent code review, on excluded
   fixtures only.
5. Only after accepted L3 may an L4 compiler/replay annex be written.

## 14. Negative authorization

This unaccepted draft authorizes nothing. It does not authorize L3 code, a
prototype, a dev root key, a generated plan, a fixture scan, an L4 annex or
code, Peano/MCTS execution, proof search, compilation, replay, query
measurement, calibration, G4ip, inverse, statement or selector fitting, learner
training, a SELF/YOKED branch, an audit item, a scientific outcome, a repository
edit, a commit or a push. It requires the AC-1 decision to be recorded and joint
independent X/Y acceptance to be obtained before any L3 implementation may
begin. The V4 artifact is a code-gate artifact produced after that
authorization, never a prerequisite to it. The eight dev root keys remain
unminted and require accepted L2, L3 and L4.
