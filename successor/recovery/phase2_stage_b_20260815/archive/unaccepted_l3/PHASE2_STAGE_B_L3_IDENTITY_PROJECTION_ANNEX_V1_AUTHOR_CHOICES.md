# Phase 2 Stage-B L3 identity/projection annex v1 - author choices

Status: `AWAITING_AUTHOR_DECISION`

Date: 2026-08-14

Companion to `PHASE2_STAGE_B_L3_IDENTITY_PROJECTION_ANNEX_V1_DRAFT.md`. It
contains **one** cell. Everything else in L3 is derived from the accepted
charter, the accepted L0/L1 surface or the accepted L2 annex, and is resolved
normatively in the annex.

The single cell is presented because it changes **pipeline stage-6 collision
precedence outcomes and future fixture eligibility**, which the ambiguity
discipline forbids resolving silently.

---

## AC-1. Pipeline stage-6 exclusion seed scope

### The undetermined point

Charter section 8 says of stage 6:

> Stage 6 uses the cumulative set of all previously accepted dev theorem and
> skeleton identities in that order, seeded by registered L0/L1 hand-fixture
> identities.

That sentence names **five** fixtures: the L1 hand-written valid plans. It was
written before L2 existed and therefore before six additional permanently
excluded valid plans existed.

Charter section 5.3 says:

> Every dev theorem and skeleton is permanently ineligible for cost, audit,
> selector, pilot and scientific scopes.

and the accepted L2 V5 code closure requires L3 to "import the complete V3
exclusion set", which contains **eleven** valid-plan rows: the five L1 hand
fixtures and the six L2 code-gate fixtures.

The charter does not say whether the six L2 gate fixtures seed stage 6. The two
readings give different acceptance outcomes for future dev draws, so this is a
genuine author decision, not a drafting detail.

### Why it is material

Stage-6 collision is a hard rejection. If the six L2 fixtures are in the seed,
any future dev draw whose canonical theorem or rule skeleton coincides with one
of them is rejected with `THEOREM_ID_COLLISION` or `SKELETON_ID_COLLISION`. If
they are not, such a draw is accepted into a dev quota even though its theorem
and skeleton are already permanently excluded from every later cost, audit,
selector, pilot and scientific scope by charter section 5.3.

The six L2 fixtures were produced by the same frozen A/B/C catalogue that every
future dev draw uses, from the five public test-vector keys. They are not exotic
outliers; they are ordinary members of the reachable population. So this choice
has real consequences for both acceptance accounting and later scope hygiene.

### The options

All three are fully specified. Whichever is recorded is written verbatim into
the V4 artifact field `stage6_seed.seed_scope` and into the annex, and the code
gate asserts the seed matches it exactly.

---

**(a) `ALL_ELEVEN_VALID_PLAN_FIXTURES` - recommended**

```text
stage6_seed.seed_scope        = "ALL_ELEVEN_VALID_PLAN_FIXTURES"
stage6_seed.source_fixture_names = the eleven valid_plan_fixtures names,
                                   ascending
theorem_identities  = deduplicated ascending identities of all eleven
skeleton_identities = deduplicated ascending identities of all eleven
```

Rationale:

1. It is the only option under which no accepted dev item can carry a theorem or
   skeleton that is simultaneously permanently excluded from every later scope.
   Under (b) that state is reachable, and it is an accounting hazard precisely of
   the kind charter section 10's `COLLISION_ACCOUNTING_ERROR` exists to catch.
2. It matches the accepted L2 V5 closure's instruction that L3 "import the
   complete V3 exclusion set" and "define registration of final identities
   before any root key can be minted". Importing the complete set and then
   seeding from part of it would make the import partly decorative.
3. It is the conservative direction: it can only reject more, never accept
   something a stricter rule would have rejected.

Cost, stated honestly: it removes six theorem identities and up to six skeleton
identities from the reachable dev population before the first draw. Given
prospective risk R1 in annex section 12.5 - the skeleton space per band is small
because the frame sorts its `AND_INTRO` children and erases elimination
direction - this measurably tightens an already tight skeleton budget and makes
`ROOT_QUOTA_UNFILLED` somewhat more likely. That cost is real and is the reason
this cell exists rather than being resolved silently.

---

**(b) `L1_HAND_FIXTURES_ONLY`**

```text
stage6_seed.seed_scope        = "L1_HAND_FIXTURES_ONLY"
stage6_seed.source_fixture_names = the five L1 hand fixture names, ascending
theorem_identities  = deduplicated ascending identities of the five
skeleton_identities = deduplicated ascending identities of the five
```

This is charter section 8's literal text. V4 still records the identities of all
eleven fixtures in `valid_plan_fixtures`; only the seed lists are narrowed, and
the six L2 identities are still recorded and still permanently excluded from
later scopes by charter section 5.3.

Rationale: it changes no accepted charter sentence and leaves the maximum
skeleton budget available to the dev run.

Cost, stated honestly: a dev draw may be accepted whose theorem or skeleton is
byte-identical to a permanently excluded L2 gate fixture. That dev item would
then be simultaneously admitted to a dev quota and barred from every later
scope. Nothing in the charter detects or reports that state, so it would be
silent.

---

**(c) `THEOREM_ALL_ELEVEN_SKELETON_L1_ONLY`**

```text
stage6_seed.seed_scope        = "THEOREM_ALL_ELEVEN_SKELETON_L1_ONLY"
stage6_seed.source_fixture_names = the eleven valid_plan_fixtures names,
                                   ascending
theorem_identities  = deduplicated ascending identities of all eleven
skeleton_identities = deduplicated ascending identities of the five L1 fixtures
```

A split scope: seed theorem identities from all eleven, because an exact
duplicate public theorem is the acute hazard, but seed skeleton identities only
from the five L1 fixtures, to preserve the scarce skeleton budget identified in
annex section 12.5.

Rationale: it removes the acute duplicate-theorem hazard of (b) while avoiding
the skeleton-budget cost of (a).

Cost, stated honestly: the split is not derivable from any accepted charter
sentence, so it is a new rule rather than a reading of an existing one. It also
makes the two identity kinds behave asymmetrically at the same pipeline stage,
which a later reviewer must be told about explicitly every time stage 6 is
discussed. Recommendation is (a); (c) is offered because the skeleton-budget
concern is real and the author may weigh it differently.

---

## What is not an author choice, and why

Recorded so review can see these were decided rather than overlooked.

| point | resolution | why it is determined |
|---|---|---|
| Which atom set the bijection ranges over | `plan['atoms']` | Annex Lemma D1: the L1 checker forces declared = public = occurring, so charter 5.1's "used atoms" has exactly one referent. |
| Bijection enumeration order | `itertools.permutations(range(k))`, ascending lexicographic | Order cannot affect the minimum or the set attaining it; it is frozen only so the returned list is deterministic. |
| Hypothesis sorting key | canonical bytes of the formula only | Charter 5.1 step 2 as written; annex Lemma B1 shows it is a strict total order, so no occurrence matching arises. |
| Local-ID preorder reading | mint all binders at node entry, `left_assumption` before `right_assumption` | A binder record is a field of its binding node, and preorder visits a node before its children. Both candidate readings induce identical equivalence classes, so this affects recorded bytes only, not identity semantics. The rejected reading is named in annex section 5.4. |
| Skeleton computed on checked or canonical plan | either, they are byte-identical | The skeleton reads only node kinds and child edges, neither of which renaming or relabeling changes. The gate asserts the equality. |
| `OR_ELIM` branch-pair unit | the branch skeleton alone | The assumption record erases to nothing, so the pair unit *is* the branch skeleton. Adding a phantom token would leak a distinction the charter erases. Annex section 6.2. |
| Theorem/skeleton identity for renderer-only and enumerability fixtures | not defined, not recorded | Two-atom surface sequents and Peano witnesses have no ND plan object and fewer than `MIN_DECLARED_ATOMS` atoms, so charter 5.1 is undefined for them. Deriving an identity from a raw hash would fabricate one. Annex section 8.2. |
| `premise_witness_or_e` / `renderer_or_commute` | one alias group over the shared raw sequent hashes, two provenance rows retained, no invented theorem identity | Their raw hashes are byte-identical, confirmed directly from V3. Annex section 8.2 and upstream note U2. |
| Stage-6 order theorem then skeleton | frozen | Charter section 8 lists `THEOREM_ID_COLLISION` before `SKELETON_ID_COLLISION` and attributes to the first failure. |
| L3 internal invariant disposition | raise `L3InvariantError`, never a new draw cause | The charter grants no sub-enum permission at stage 5. Annex section 2.5 and upstream note U1. |

---

## Decision record required

Record `(a)`, `(b)` or `(c)`. Then, and only then:

1. the annex is revised to v1.1 with the selected `seed_scope` inlined and this
   cell's cross-references removed;
2. joint independent X/Y acceptance of that annex is recorded;
3. acceptance authorizes exactly `learning/phase2_stageb_identity.py` and
   `learning/test_phase2_stageb_identity.py`, and nothing else;
4. Builder implements those two files;
5. the code gate runs and emits
   `/tmp/PHASE2_STAGE_B_L3_IDENTITY_EXCLUSIONS_V4.json`;
6. driver review and an independent code review accept or reject L3.

No dev root is minted or consumed at any step above. No L4 annex, no Peano,
MCTS or search execution, no query measurement, no training, no audit and no
scientific outcome is authorized by recording this decision.
