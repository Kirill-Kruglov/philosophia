# Phase 2 Stage-B L3 identity/projection annex v1 - driver handoff

Status: `READY_FOR_PHASE2_STAGE_B_L3_ANNEX_V1_XY_REVIEW`

Date: 2026-08-14

## Deliverables and hashes

| file | SHA-256 | lines |
|---|---|---|
| `PHASE2_STAGE_B_L3_IDENTITY_PROJECTION_ANNEX_V1_DRAFT.md` | `a3760d619f147ec083bcd7cab4b158d39f13bce963f12ff8db236c85a9c0601a` | 1395 |
| `PHASE2_STAGE_B_L3_IDENTITY_PROJECTION_ANNEX_V1_AUTHOR_CHOICES.md` | `f36e620e0a99a98f939f7ee2b1013fb59b45e022f56bbc15abe8f13c84f18ef4` | 187 |
| `PHASE2_STAGE_B_L3_IDENTITY_PROJECTION_ANNEX_V1_DRIVER_HANDOFF.md` | this file | - |

## Authority verified

All seven pinned hashes were recomputed by this author and match: charter
`703bf39c…`, L0/L1 closure `d6b103a3…`, accepted L2 annex `3a78a53e…`, L2 V5
closure `d09781ea…`, V5 cumulative patch `3a570b2e…`, L2 code-gate artifact
`8961b5a9…`, exclusion ledger V3 `a1f907ad…`. MINIMO base
`6066f482c6752915ad21119f93dc162f4cb9db72`.

The governing L0/L1/L2 sources were read from the disposable inspection tree,
not assumed from the prompt: `phase2_stageb_canonical.py`,
`phase2_stageb_render.py`, `phase2_stageb_causes.py`, `phase2_stageb_schema.py`,
`phase2_stageb_checker.py`, the five L1 valid-plan fixture builders in
`test_phase2_stageb_checker.py`, and the public surface of
`phase2_stageb_generator.py`. Annex section 0.1 lists the eleven facts the
specification depends on, each traceable to a named source line.

## Verdict

`READY_FOR_PHASE2_STAGE_B_L3_ANNEX_V1_XY_REVIEW`

Not `PHASE2_STAGE_B_L3_UPSTREAM_CONTRACT_BLOCKER`: the three upstream notes
below are a missing enum member, a loose closure phrase with exactly one
consistent reading, and a duty with no reachable input. None of them prevents
writing, reviewing or implementing L3 on the fixed excluded fixtures.

Not `PHASE2_STAGE_B_L3_ANNEX_DRAFT_BLOCKER`: every mandatory item A through H is
closed with exact schemas, algorithms, precedence, bounds and tests.

## What the annex closes

- **A.** Consumes exactly the checked plan plus `check_plan(...)['theorem']`,
  two positional parameters, no generator metadata, no keyword escape. Exact
  `L3_SUCCESS_KEYS` (10 keys) and `L3_FAILURE_KEYS` (4 keys), plain data only.
  Nine production signatures, an import allowlist that excludes the L1 checker
  and the L2 generator, deep-copy and input-immutability rules, and derived
  bounds `720` bijections, `24` formula frames, `38` proof frames.
- **B.** Bijection enumeration frozen as ascending
  `itertools.permutations(range(k))`; non-mutating recursive substitution;
  sorting of hypothesis **formula bytes only**; exact 3-key canonical theorem;
  byte-minimum with the full minimizing set retained for section C; lowercase
  64-hex identity and `t_<64hex>` name; five named invariance proofs with tests.
  Lemma B1 shows the hypothesis sort is a strict total order, so no factorial
  occurrence matching is introduced beyond the `k! <= 720` atom bijections.
- **C.** Per minimizing renaming: atom substitution, hypothesis sort by renamed
  formula bytes with `h0..` reassignment, local renaming by a stated preorder
  rule with the binding/use relationship for `OR_ELIM` and `NOT_INTRO`,
  `ASSUME` reference rewriting, 5-key canonical plan, byte-minimum, and the
  size-before-equals-after assertion with its disposition. Four invariance
  proofs plus four must-differ pairs.
- **D.** Exact recursive skeleton schema over a 9-member erased kind alphabet;
  `ASSUME_GLOBAL` versus `ASSUME_LOCAL` decided from the L0 identifier grammar
  with no scope tracking; direction merged; `AND_INTRO` children and the
  `OR_ELIM` branch pair sorted by canonical bytes with ties resolved on bytes
  alone; all other child order preserved. Ten erasure pairs and eight retention
  pairs.
- **E.** Raw re-derivation from public plan fields only, compared before
  canonicalization, with a four-member precedence. `public_projection` takes
  exactly one parameter and enforces a canonical-form precondition, so sealed
  metadata cannot enter by any call path. Exact 5-key public item, L0 renderer
  only, 31 enumerated sealed field names, three hold-theorem-fixed proofs and
  twelve leak mutations.
- **F.** V4 schema with exact key sets, preserving every V3 row and field.
  Eleven valid-plan fixtures get all three identities **after** their V3 raw
  hashes are reverified; the two renderer-only and seventeen enumerability
  fixtures get `identity_status = NOT_DEFINED` with a closed reason, because no
  ND plan object and fewer than three declared atoms make charter 5.1 undefined
  for them. One alias group for the byte-identical
  `premise_witness_or_e` / `renderer_or_commute` sequent, both provenance rows
  retained, no invented theorem identity. Test-only reconstruction imports the
  L1 fixture builders and calls the generator on exactly the six literal frozen
  rows, never the scan.
- **G.** Eleven mandatory gate sections, including exhaustive atom-permutation
  invariance, hypothesis and local-ID invariance, mismatch mutation, leak
  battery, full skeleton mutation battery, no-alias and input-unchanged checks,
  fresh-process determinism under varied `PYTHONHASHSEED`, V3 reverification
  before identities, V4 reproducibility and alias accounting, import-graph
  discipline, patch routes and regression gates.
- **H.** Two authorized files plus one gate-generated `/tmp` artifact, frozen
  patch names relative to accepted V5, X/Y before implementation and independent
  code review after, and a mandatory stop.

## Open author choice: one

**AC-1, stage-6 exclusion seed scope.** Whether the six L2 code-gate fixtures
seed pipeline stage 6 alongside the five L1 hand fixtures. Charter section 8
literally names only the L1 hand fixtures; charter section 5.3 plus the L2 V5
closure's "import the complete V3 exclusion set" point at all eleven. The two
readings change collision outcomes and fixture eligibility for every future dev
draw, so the annex does not resolve it.

Three fully specified options: `(a) ALL_ELEVEN_VALID_PLAN_FIXTURES`
(recommended), `(b) L1_HAND_FIXTURES_ONLY`,
`(c) THEOREM_ALL_ELEVEN_SKELETON_L1_ONLY`. The recommendation is (a) because it
is the only option under which no accepted dev item carries a theorem or
skeleton that is simultaneously permanently excluded from every later scope. Its
honest cost, tightening an already small skeleton budget, is stated in the
choices file and connected to risk R1 below.

Ten further points that a reader might expect to be choices are listed in the
choices file as **determined**, each with the accepted clause or lemma that
determines it, so review can confirm they were decided rather than overlooked.

## Upstream notes for driver disposition

**U1, missing reason code, non-blocking.** Charter section 10's closed
`DEV_CORE_FEASIBILITY_STOP` list contains `CHECKER_UNSOUND`, `COMPILER_UNSOUND`,
`PUBLIC_PROJECTION_LEAK`, `COLLISION_ACCOUNTING_ERROR` and `NONDETERMINISM`, but
no code for an identity-normalization defect. The charter also grants no stage-5
sub-enum permission, so L3 must not invent a draw cause. The annex therefore
routes internal invariant violations to a typed `L3InvariantError` carrying one
code from a closed nine-member tuple, proves none can fire on L1-accepted input,
and requires the gate to assert no fixture raises one. Smallest upstream
correction: append exactly one reason code, `IDENTITY_NORMALIZATION_UNSOUND`, to
charter section 10's closed list before any dev execution is authorized. Dev
execution is unauthorized and requires L4, so nothing is blocked today.

**U2, closure wording, non-blocking.** The L0/L1 v3 closure says L3 "must
deduplicate their theorem identity" for the
`premise_witness_or_e` / `renderer_or_commute` pair. Charter section 5.1 defines
theorem identity only over `3..6` used atoms, and the shared object is a
two-atom renderer surface sequent with no ND plan, so no such identity exists.
The only consistent reading is deduplication of the shared **raw excluded
sequent**, which this author confirmed is byte-identical under both provenance
names in V3 (`raw_ascii` `aa5844b1…`, `canonical_json_string` `8089c6d1…`). The
annex implements that reading and retains both provenance rows. Smallest
correction: reword the closure sentence to say "raw excluded sequent".

**U3, vacuous duty, no correction required.** Charter section 4 assigns L3 the
duty of comparing the independently rendered public sequent against "any later
generator-supplied rendering". The accepted L2 emits no surface syntax, so this
branch has no reachable input. The annex records it rather than dropping it
silently, and adds no speculative parameter.

## Prospective risk recorded, not measured

**R1, skeleton collision density.** Under the frozen A/B/C catalogue, a plan's
rule skeleton is determined by the scaffold, the unordered pair of the first two
chain lengths and the third chain length, because the frame's `AND_INTRO`
children are sorted and elimination direction is erased. The reachable skeleton
space per band is therefore far smaller than the per-root draw budget, so
`SKELETON_ID_COLLISION` is expected to reject a substantial fraction of later
dev draws and charter section 10's `ROOT_QUOTA_UNFILLED` is a live prospective
risk.

This is a structural consequence of two frozen accepted rules, not a
measurement: no draw was generated, no scan was run and no yield was computed.
It is recorded so the later quota owner is not surprised, and it interacts with
AC-1, since option (a) tightens the skeleton budget further. It must not be used
to alter the catalogue, the skeleton rule or the quota within this charter
version; charter section 10 forbids within-version configuration change.

## Suggested review focus for X and Y

1. Lemma D1 and Lemma B1, since the whole no-matching-search argument rests on
   them.
2. The local-ID preorder reading in annex section 5.4, including the explicitly
   rejected alternative and the claim that both readings induce identical
   equivalence classes.
3. The `OR_ELIM` branch-pair treatment in annex section 6.2, specifically the
   claim that the assumption record erases to nothing so the pair unit is the
   branch skeleton, and that adding a phantom token would itself be a leak.
4. Whether `public_projection`'s single-parameter signature plus canonical-form
   precondition really makes sealed metadata structurally unable to enter, or
   whether a further constructor-level restriction is wanted.
5. AC-1, and whether the R1 skeleton-budget cost changes the recommendation.
6. U1 and U2, and whether the driver wants the two upstream corrections issued
   now or carried into the L4 cycle.

## Boundary

No code was written, no prototype built, no plan generated, no scan run, no key
or root minted or derived, no Peano compilation or replay, no training, no audit
or scientific item, no repository edit, no commit and no push. The MINIMO and
Philosophia repositories are untouched. Only the three `/tmp` files named above
were written.

## Authorization

This handoff authorizes nothing. It requests the AC-1 decision and joint
independent X/Y review of the annex. Acceptance would authorize exactly
`learning/phase2_stageb_identity.py` and
`learning/test_phase2_stageb_identity.py`, and nothing else. L4, dev roots,
Peano/MCTS/search, query measurement, training, audit and scientific execution
remain unauthorized.
