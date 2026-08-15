# Stage-R L3 projection-only executable annex V1

Status: `FROZEN_FOR_BOUNDED_IMPLEMENTATION`

Date: 2026-08-15

## 0. Authority

This annex executes only §4.1 items 1–2 of
`PHILOSOPHIA_MINIMUM_CAUSAL_CONTRACT_R_V2_1.md`, SHA-256
`1c3cec3aa6bd7094e2d37b062a8f349df5b226e91bbdc4a7b21e80fb785172f3`.
The author activation is
`STAGE_R_L3_PROJECTION_ONLY_ACTIVATION_V1.md`, SHA-256
`2539786a2b3954408a8fb98f0d8238636c0644900b56c74a2a6eec436da017b2`,
durably recorded in commit
`240808cbb5f313c4905c1d4dafe565af8a248cea`.

Other governing pins:

| object | SHA-256 |
|---|---|
| Stage-B charter v1.1.1 | `703bf39cfe8f875f9be3781659a7365c1bc99c42f7523e43fef2c0a2c47b8311` |
| accepted L2 annex | `3a78a53ecb8e5275f433bc03c50b7b93746c597e3d2d1fcf0bedd4249f102da8` |
| accepted L2 generator | `de9b05d6732dfe07c5303439a1fd533f9d6053a62a04480db0659075b16d2a34` |
| accepted L2 V5 test | `01adece50de5dc4cece3acfed80b21725ca7400e5d375204d5010eaae0dca4e8` |
| L2 code-gate JSON | `8961b5a97ee0972d83a071e1b1c82869a9841f5f01c45add12a88dbfee1010f0` |
| exclusion ledger V3 | `a1f907ad6665b7c96d91496c5a91d32f0f0cae63da48b6b26da6b292d48f528d` |
| accepted cumulative patch through L2 V5 | `3a570b2e35b15dc796d86cd8a997230c00bbf5aed3b5c06f3b14dca78b46b683` |
| MINIMO base | commit `6066f482c6752915ad21119f93dc162f4cb9db72` |

The recovered L3 V1 draft is non-authoritative provenance. This annex retains
its proved theorem-normalization, skeleton-erasure and projection rules where
they follow from the current authority, but removes the broader dev-root
pipeline, exact-plan identity and stage-6 seed machinery that the Stage-R
contract does not require.

## 1. Exact boundary

L3 provides exactly three frame-disjointness representations:

1. alpha-canonical theorem identity;
2. canonical public-item bytes;
3. canonical rule-skeleton identity.

It also independently re-derives the raw theorem from the checked plan's public
fields and materializes identities for the eleven already excluded valid-plan
fixtures. It does not choose, generate or seal a reservoir or held-out panel.

### 1.1 Authorized MINIMO files

Exactly two new files:

```text
learning/phase2_stageb_identity.py
learning/test_phase2_stageb_identity.py
```

No existing MINIMO file may change. Production may import only
`itertools`, `typing`, `phase2_stageb_canonical`, `phase2_stageb_render` and
`phase2_stageb_schema`. It must not import the checker, generator, tests, Peano,
MCTS, Torch, `json`, `hashlib`, `random`, `secrets`, filesystem or process APIs.
There is no mutable module state.

The test may import the accepted checker, the five L1 fixture builders and the
accepted L2 generator solely to reconstruct the eleven literal excluded valid
plans. It must not import or call `select_l2_code_gate_rows`, scan a key range,
mint or derive a key, or generate any row outside the six frozen rows already
listed in the L2 code-gate JSON.

### 1.2 Explicitly absent

There is no exact-plan identity, stage-6 collision seed, dev-root processing,
quota accounting, L4 compile/replay, frame selection, learner/selector call or
scientific execution. Exact-plan identity is not one of the three identities in
Stage-R §3.2, and Stage-R §4.1 says the minimum boundary is “and only these”.
Universal collision economy is deferred by §4.2. The archived AC-1 seed-scope
choice is therefore unreachable here rather than silently decided.

## 2. Production API and records

Production exposes these pure functions:

```python
def canonical_theorem(theorem: Mapping) -> dict
def theorem_identity(theorem: Mapping) -> str
def rule_skeleton(node: Mapping) -> dict
def skeleton_identity(plan: Mapping) -> str
def public_projection(canon_theorem: Mapping) -> dict
def rederive_theorem(plan: Mapping) -> dict
def identify(plan: Mapping, checker_theorem: Mapping) -> dict
```

`identify` is the only future orchestration entry point. It takes the exact
plan accepted by L1 and `check_plan(...)['theorem']`; it accepts no generator or
run metadata.

The exact success keys are:

```text
('schema','ok','cause','theorem_identity','theorem_name',
 'skeleton_identity','canonical_theorem','public_item')
```

with:

```text
schema              = "philosophia.stager.l3-projection.v1"
ok                  = True
cause               = None
theorem_identity    = lowercase 64-hex SHA-256
theorem_name        = "t_" + theorem_identity
skeleton_identity   = lowercase 64-hex SHA-256
canonical_theorem   = the exact object in §3
public_item         = the exact object in §5
```

The exact failure keys are:

```text
('schema','ok','cause','subcause')
```

with `ok=False`, `cause="SEQUENT_REDERIVATION_MISMATCH"` and the first
applicable subcause in this strict order:

```text
THEOREM_KEYSET_MISMATCH
THEOREM_ATOMS_MISMATCH
THEOREM_HYPOTHESES_MISMATCH
THEOREM_GOAL_MISMATCH
```

Malformed or non-L1-shaped internal inputs are implementation defects, not draw
outcomes. They raise `L3InvariantError(code)` where `code` is exactly one of:

```text
INPUT_NOT_L1_SHAPED
DECLARED_ATOM_COUNT_OUT_OF_RANGE
BIJECTION_BOUND_EXCEEDED
FORMULA_RECURSION_BOUND_EXCEEDED
PROOF_RECURSION_BOUND_EXCEEDED
CANONICAL_THEOREM_PRECONDITION_VIOLATED
```

The exception carries only `.code`. None may arise for an L1-accepted fixture.
At this stage any such raise is a code-gate failure; it is not a newly invented
draw cause.

All outputs are fresh plain data. Inputs are unchanged; no returned mutable
object aliases any input object or another returned position.

## 3. Alpha-canonical theorem identity

Input has exactly keys `atoms`, `hypotheses`, `goal`. For `k=3..6`, enumerate
`itertools.permutations(range(k))` in its native lexicographic order. For source
atoms in the accepted ascending list, permutation `p` maps source atom `i` to
`a{p[i]}`. Under every bijection:

1. recursively substitute atoms in every hypothesis and the goal;
2. set atoms to `['a0',...,'a{k-1}']`;
3. sort renamed hypothesis formula objects by `canonical_bytes(formula)`;
4. form exactly
   `{'atoms': [...], 'hypotheses': [...], 'goal': formula}`;
5. choose the candidate with byte-lexicographically minimum
   `canonical_bytes(candidate)`.

Theorem identity is `canonical_hash(canonical_theorem(theorem))`; the public
name uses every one of its 64 lowercase hex characters. Global hypothesis IDs,
input hypothesis order, atom spelling, plan shape and metadata never enter.

Bounds are `k! <= 720` and formula recursion at most 24 frames. Substitution is
a fresh recursive constructor. Accepted L1 input guarantees all declared atoms
are public and used and distinct global hypothesis formulas remain a strict
sorting order under any bijection; no hypothesis matching search exists.

## 4. Reservoir-local rule skeleton

`rule_skeleton(node)` uses this exact recursive schema:

```text
ASSUME hN       -> {'kind':'ASSUME_GLOBAL'}
ASSUME lN       -> {'kind':'ASSUME_LOCAL'}
AND_INTRO       -> {'kind':'AND_INTRO',
                    'children':SORT2(sk(left),sk(right))}
AND_ELIM_LEFT   -> {'kind':'AND_ELIM','children':[sk(source)]}
AND_ELIM_RIGHT  -> {'kind':'AND_ELIM','children':[sk(source)]}
OR_INTRO_LEFT   -> {'kind':'OR_INTRO','children':[sk(source)]}
OR_INTRO_RIGHT  -> {'kind':'OR_INTRO','children':[sk(source)]}
OR_ELIM         -> {'kind':'OR_ELIM',
                    'children':[sk(major)]
                               + SORT2(sk(left_branch),sk(right_branch))}
NOT_INTRO       -> {'kind':'NOT_INTRO','children':[sk(body)]}
NOT_ELIM        -> {'kind':'NOT_ELIM',
                    'children':[sk(negative),sk(positive)]}
EXFALSO         -> {'kind':'EXFALSO','children':[sk(source)]}
```

`SORT2` compares only `canonical_bytes` and returns a new two-element list.
Formula fields, atom names, conclusions, hypothesis IDs and assumption records
are erased. Elimination/introduction direction is erased only where shown.
`NOT_ELIM` order and the `OR_ELIM` major position remain. Exchanging both
`OR_ELIM` `(assumption,branch)` units together changes only the two sorted branch
skeletons and therefore preserves identity; changing one branch shape does not.

The skeleton identity is
`canonical_hash(rule_skeleton(plan['proof']))`. Proof recursion is bounded by
38 frames (37 checked inference nodes plus guard headroom).

## 5. Independent raw check and public projection

`rederive_theorem(plan)` freshly constructs:

```text
{'atoms': plan['atoms'],
 'hypotheses': [h['formula'] for h in plan['hypotheses']],
 'goal': plan['goal']}
```

It reads only these public plan fields and does not import the checker or walk
the proof. `identify` compares this raw object with `checker_theorem` before any
canonicalization, by §2 precedence, using canonical bytes of each subobject.

`public_projection` has exactly one argument: a canonical theorem. It rejects
extra keys, non-canonical atom names/order, non-strictly-sorted hypotheses,
malformed formulas, undeclared occurrences or a cardinality outside 3..6. It
returns exactly:

```text
PUBLIC_ITEM_KEYS =
('schema','theory_sha256','premises','theorem_name','goal')

{
  'schema': 'philosophia.stageb.public-item.v1',
  'theory_sha256': THEORY_SHA256,
  'premises': list(THEORY_PREMISES),
  'theorem_name': 't_' + canonical_hash(canon_theorem),
  'goal': render_sequent(canon_theorem['atoms'],
                         canon_theorem['hypotheses'],
                         canon_theorem['goal'])
}
```

The accepted L0 renderer is the only renderer. The `goal` value is the complete
ASCII sequent. Projection bytes are `canonical_bytes(public_item)`. No root,
draw, band, node count, plan, trace, skeleton, scaffold, direction, source,
branch, held-out marker, certificate, rejection or fixture name can enter the
signature or record.

`identify` order is fixed: raw re-derivation and comparison; canonical theorem;
theorem identity/name; skeleton identity; public projection; success assembly.
It has no retry, search, random call or filesystem access.

## 6. L3 gate exclusion artifact

The gate uses only the five L1 valid-plan fixtures and the six literal selected
L2 rows. Every raw plan and checker theorem hash is compared with V3 before an
L3 identity is accepted. No renderer-only or enumerability fixture receives a
fabricated theorem or skeleton identity.

The durable artifact is named
`STAGE_R_L3_CODE_GATE_EXCLUSIONS_V1.json`. Canonical JSON plus one newline has
these exact top-level keys:

```text
('schema','contract_sha256','activation_sha256','charter_sha256',
 'source_v3_sha256','l2_code_gate_sha256','identity_domain','source_v3',
 'valid_plan_identities','raw_sequent_alias_groups')
```

Values:

```text
schema = "philosophia.stager.l3-code-gate-exclusions.v1"
identity_domain = "L1_CHECKED_ND_PLAN_WITH_3_TO_6_DECLARED_ATOMS"
source_v3 = the complete parsed V3 object, byte-for-value unchanged
```

`valid_plan_identities` is ascending by `fixture_name`; every one of its eleven
rows has exactly:

```text
('fixture_name','source','raw_plan_sha256','raw_theorem_sha256',
 'theorem_identity_sha256','theorem_name','public_projection_sha256',
 'public_item','skeleton_identity_sha256')
```

`source` is `L1_HAND_FIXTURE` for the five named `valid_*` rows and
`L2_CODE_GATE_FIXTURE` for `l2_gate_00..05`. Hash and public fields come only
after V3 raw-hash reverification.

`raw_sequent_alias_groups` contains every duplicate pair of
`(raw_ascii_sequent_sha256, canonical_json_string_sha256)` across V3's
renderer/enumerability rows, sorted by the hash pair. Each row has exact keys
`raw_ascii_sequent_sha256`, `canonical_json_string_sha256`, `members`, with
ascending member names. For V3 there is exactly one row with members
`['premise_witness_or_e','renderer_or_commute']`. It records one raw excluded
sequent with two provenance roles and defines no L3 theorem identity.

This artifact is an exclusion registration, not a fixture selection. It has no
stage-6 seed, collision precedence, quota or root field. All eleven mapped
theorem/public/skeleton representations and the embedded V3 raw exclusions are
permanently barred from later Stage-R scopes.

## 7. Mandatory code gate

The new test file must cover all of the following:

1. Verify every governing file hash before fixture reconstruction.
2. Reconstruct five L1 fixtures from their existing builders and regenerate
   only the six frozen L2 `(key_hex,draw_index)` rows from the pinned JSON.
   Assert their complete canonical result hashes where recorded. The selector
   helper name must neither be imported nor called.
3. Re-run L1 checking and reverify all eleven V3 raw plan/theorem hashes before
   computing identities.
4. Exhaustively permute all `k!` atom bijections for every valid fixture,
   re-check each transformed plan, and prove theorem identity, public bytes and
   skeleton identity invariant.
5. Permute global hypotheses with consistent global-ID rewrites; relabel local
   IDs consistently; prove the same invariances. Prove at least two
   theorem-changing mutations change theorem/public identity.
6. Exercise all four raw mismatch subcauses and their precedence; assert exact
   success/failure keys and absence of identity fields on failure.
7. Test all skeleton erasures: atom/formula/conclusion changes, global/local ID
   relabeling, both direction erasures, `AND_INTRO` exchange and paired
   `OR_ELIM` exchange. Test retention of global-vs-local leaf, `NOT_ELIM` order,
   `OR_ELIM` major position, branch shape, chain length and rule kind.
8. Assert `public_projection`'s one-argument signature, exact key set, exact
   renderer value, all-64-hex name and refusal of every sealed-field mutation.
   Hold canonical theorem fixed while varying plan/identifier order and assert
   byte-identical projection.
9. Assert input canonical bytes unchanged and walk every output to prove no
   mutable alias with inputs or within the output.
10. Inject every `L3InvariantError` at its real internal boundary. No accepted
    fixture may raise one.
11. Run representative outputs in two fresh processes under different
    `PYTHONHASHSEED` values and compare canonical bytes.
12. Materialize the §6 artifact twice in separate temporary paths and prove
    byte identity, exact schemas, all eleven mappings, embedded V3 equality,
    the one raw alias group and absence of identities for non-plan fixtures.
    Expose a test-only helper that can write the identical durable artifact to
    an explicit caller-supplied path.
13. Parse the production source with `ast`; enforce the import allowlist and
    absence of forbidden calls, hidden retries, filesystem/process access and
    mutable globals.
14. Run ordinary Stage-B discovery and report the measured count. Existing 67
    tests must remain green. Do not run the frozen selector scan. Verify both
    patch routes and that the original MINIMO and Philosophia worktrees are not
    presented as implementation evidence.

The gate may use explicit constructed inputs. It performs no Peano compile,
MCTS/search/query work, learner call, fixture/frame selection or science.

## 8. Deliverables and stop

The Builder persists, under `successor/stage_r/l3/candidate/`:

```text
learning/phase2_stageb_identity.py
learning/test_phase2_stageb_identity.py
STAGE_R_L3_CODE_GATE_EXCLUSIONS_V1.json
minimo_phase2_stageb_l3_projection_v1_delta.patch
minimo_phase2_stagea_stageb_l01_l2_l3_projection_v1_cumulative.patch
STAGE_R_L3_BUILDER_REPORT_V1.md
```

The delta is relative to the accepted L2 V5 tree and adds exactly the two
authorized files. The cumulative patch is relative to MINIMO base and changes
only the already accepted Stage-A/L0–L2 paths plus those two files. The report
pins every output hash, test command/count, temporary tree base, patch scope and
focused time used.

The Builder does not commit or push. After producing these objects it stops.
There is one driver code audit and at most one independent bounded code review;
a concrete defect gets one scoped repair, not a new annex or general review.

```text
L3_SCOPE=THEOREM_IDENTITY_PUBLIC_PROJECTION_RESERVOIR_LOCAL_SKELETON
EXACT_PLAN_IDENTITY_IMPLEMENTED=NO
STAGE6_SEED_IMPLEMENTED=NO
L4_AUTHORIZED=NO
ROOT_OR_FRAME_GENERATION_AUTHORIZED=NO
SCIENTIFIC_EXECUTION_AUTHORIZED=NO
```
