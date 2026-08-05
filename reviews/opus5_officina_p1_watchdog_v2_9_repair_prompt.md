# Officina P1 watchdog v2.9 consolidation and exit repair

You are Claude Code Opus 5, specification repair author. Work in:

`/home/master/llm_projects/philosophia`

Review base commit: `3d19dc7` (`Review watchdog v2.8 import and ownership closure`).
Do not modify historical files, code, tests, untracked work, signatures, runtime
artifacts, or prior review artifacts. Do not commit.

This is the consolidation round for the pre-T watchdog specification. It may
repair only the concrete Critical/Major defects below. It must not create a new
author cell, broaden the scientific programme, or reopen already accepted
choices. After this round, stylistic or documentary refinements are to be
logged for implementation unless they expose an actual authority, accounting,
quarantine, identifiability, or fail-closed defect.

## Exact inputs

v2.8 governing bytes:

- `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_8_CORRECTION.md`
- `successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_5_DRAFT.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_8.md`

Independent reviews:

- X: `reviews/fable_officina_p1_watchdog_v2_8_independent_x_confirmation.md`
  SHA-256 `ddd6d63aac69a6e3003fe7880ac7e5cbfe9f74cdb64b6f1d0716750795d8e8e9`
- Y: `reviews/sol_officina_p1_watchdog_v2_8_final_y_confirmation.md`
  SHA-256 `88efa91dcb9142483cab6f832088ee3d19c51eb79ba20335deb84e005ea90a46`
- signed identity state:
  `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md`
  (Option A, observation-only; bounded weakening remains unaccepted)

X independently reproduced the exact 89-row stdlib closure:

- kinds: 29 BUILTIN / 13 FROZEN / 2 EXTENSION / 45 PURE_PYTHON;
- 76 transitive names; 39 empty arrays; all 267 effect booleans false;
- canonical length 20,534;
- SHA-256 `aa974e0c91e5c9afd0aceefa6b0e47ef42b5ad7b71dc4de690a4873232dc20ee`;
- exact fourteen-row bootstrap subset.

Do not perturb this value. Both lines returned `REVISE`, for the bounded defects
R1-R5 below.

## Deliverables

Create exactly:

1. `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_9_CORRECTION.md`
2. `successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_6_DRAFT.md`
3. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_9.md`
4. `reviews/opus5_officina_p1_watchdog_freeze_choice_v2_9_closure.md`

Carry v2.8 forward except where R1-R5 explicitly replace it.

## R1 - make validation ownership disjoint and executable

Sol found that the v2.8 topology still assigns some relations twice or to stale
owners. Repair the governing bytes, not merely the closure narrative.

### R1.1 stale IR-3 ownership

Every install-record identifier equality governed by the operative CK-12 must
name CK-12. Remove stale references assigning the same equality to CK-8 or
CK-9. Recompute all row and cross-reference labels.

### R1.2 missing M4 Stage-A keys

For `stage_a_pre_selection_record_sha256` and
`stage_a_pre_selection_record_path` (and every analogous M4 key):

- absence is a structural exact-key-set failure owned once by CK-8 and returns
  `MEMBER_SUBSTITUTED` (or one explicitly equivalent existing structural code);
- a later Stage-A semantic/binding check may run only after that key exists and
  has the correct type/grammar;
- delete any later `STAGE_A_*` code for the same missing-key condition.

Show the exact changed row 111 behavior.

### R1.3 total CK-13 partition

`MEMBER_EXTRA`, `MEMBER_STALE`, and `MEMBER_SUBSTITUTED` must be pairwise
disjoint predicates with a literal internal order and complete coverage of the
member-set states assigned to CK-13. Do not use prose synonyms for overlapping
conditions. Either:

- define a total partition over cardinality, class/path identity, and digest
  equality; or
- remove/merge a redundant code and update every count/reference.

At minimum give first-code fixtures for: unknown extra path, replacement of an
expected path by another path, correct paths with wrong digest, missing member,
extra plus stale, and replacement plus stale.

### R1.4 narrow CK-10

CK-10 owns only its enumerated semantic/cross-object M4 relations. It must not
claim M4 schema/version/created_utc, exact-key-set, type, grammar, or structural
shape already owned by CK-8. List CK-10's exact field relations exhaustively.

### R1.5 prove the total order

Publish the complete topological predicate sequence and a relation -> earliest
owner -> code table. Add combined multi-fault fixtures for the states above and
for malformed M4 plus a semantic Stage-A mismatch. Two conforming
implementations must emit the same first code.

## R2 - bind the real project import surface

The 89-row literal correctly describes the pinned stdlib closure, but executing
`import philosophia.officina.generic_harness` also executes four tracked project
modules before the role root:

```text
src/philosophia/__init__.py
src/philosophia/officina/__init__.py
src/philosophia/officina/canonical.py
src/philosophia/officina/interlock.py
```

They are currently neither production roots nor stdlib rows nor digest-bound
dependencies. Their present bytes are benign; that is not an integrity binding.

### Required repair

Add one prospective, exact, code-compatible project-import dependency surface
without misclassifying these modules as role entry roots or stdlib modules. The
preferred minimal form is a closed `project_import_dependencies` object in M4
that contains:

- canonical module name and repository-relative path for all four files;
- SHA-256 of the exact prospective reviewed bytes;
- their exact project-to-project import edges;
- their scoped direct stdlib-import seeds;
- explicit import-time effect assertions covering process/task creation, fork
  hooks, signal/handler installation, thread creation, environment mutation,
  filesystem writes, and any other control-relevant side effect already
  forbidden by the contract.

If the existing schema requires a different minimal representation, use it only
if it provides the same binding. M4 structural and semantic checks must
recompute these hashes from installed bytes before authority. The install record
binds M4, and M4 binds these bytes; state the acyclic chain explicitly.

Do not edit the four files or the untracked `generic_harness.py`. This is a
prospective source contract: future implementation bytes must match, and any
change requires a new reviewed generation. Do not fold these four rows into the
89-row stdlib literal, whose verified canonical value remains unchanged.

Show the full import sequence:

```text
philosophia/__init__.py
  -> philosophia/officina/__init__.py
  -> canonical.py / interlock.py as actually executed
  -> generic_harness.py
  -> verified stdlib closure
```

Derive the actual order rather than accepting the illustrative arrows if Python
semantics differ. Include fixtures where one project dependency changes bytes,
path, import edge, or effect assertion.

## R3 - make the integrity relation surface honest and complete

v2.8 added B14 but still calls a reduced graph complete while omitting governing
relations inherited from TS-2/TS-5. Repair by one of these code-equivalent
routes:

1. produce a genuinely exhaustive relation graph/table derived from every
   path-, filename-, digest-, id-, signature-, option-, key-, member-count-,
   assertion-, Stage-A-, Stage-B-, M4-, and project-dependency relation; or
2. rename the diagram an explicitly non-exhaustive `integrity binding summary`
   and make a separate exhaustive relation-to-owner table normative.

The normative surface must include, where present:

- Stage B `governing_amendment_sha256` equality to the M4 peer-amendment field;
- Stage A / M4 direct equalities, not merely their common downstream target;
- Stage-A path/hash/key equalities to the corresponding M4 fields;
- install-record id equality to its canonical filename/path;
- B14 selected-option equality;
- the R2 project-dependency hash/path/import-edge bindings.

If equivalence classes or a quotient graph are used, define their canonical
construction and do not call the visualization complete. Preserve the rejection
of any unique-attester interpretation.

## R4 - correct the unexecuted branch inventory

The 89-row value/hash is correct, but v2.8 says there are six unexecuted
module-scope branches. There are seven. In exactly the owning loci (including
composite MS-11.3 and packet section 2.5), change six to seven and add:

```text
datetime -> _pydatetime
```

The branch is not taken because `_datetime` is available on the pinned build.
Do not change the 89-row literal, length, or hash.

## R5 - reconcile history and replace stale rationale

State the sequence accurately:

1. the accepted generic-harness contract originally permitted a subprocess
   launcher;
2. the later signed/accepted P1 architecture superseded that launcher with the
   S-11/S-12 `_posix_spawn` process-control route;
3. removing `subprocess` from the prospective role allowlist is therefore a
   consistency consequence of the later authority design, not a new author
   choice and not a retroactive claim that it was never permitted.

Replace the obsolete `signal` rationale at its owning section (including
§P1-3.2) rather than leaving an old statement contradicted by a later note.

## Preserve closed work

Do not reopen or change:

- A0.4 acyclic cross-file commitment semantics;
- exact 89-row stdlib closure and fourteen-row bootstrap subset;
- all 267 false effect booleans and the prospective freeze rule;
- project code remains unexecuted during derivation;
- rollback-qualified digest language and M4 peer/pre-selection anchors;
- `FS-1..FS-5`, `TR-2(a)/(b)`, row 106(i), B14;
- W-A/W-B behavior, symmetry and recommendation; neither is selected;
- identity Option A as signed external author state; weakening unaccepted;
- `T=NOT_ACTIVATED`, programme claim `OPEN`;
- no implementation, key, entropy, Stage A/B, manifest, install record,
  process, activation, candidate, trajectory, datum, verdict or Proof.

Recompute all affected schema key counts, member/provenance counts, region and
joint hashes, rules/checks/codes/tests, graphs and cross-references. Do not carry
stale v2.8 numerics.

## Exit discipline and closure

Emit exactly one:

- `READY_FOR_OFFICINA_P1_WATCHDOG_V2_9_FINAL_XY_CONFIRMATION`
- `REVISE_OFFICINA_P1_WATCHDOG_V2_9`
- `BLOCKED_OFFICINA_P1_WATCHDOG_V2_9`

The closure must:

1. disposition every X and Y finding one-to-one;
2. show the total validation ownership table and decisive multi-fault results;
3. show how the four project modules are byte- and effect-bound without changing
   the 89-row stdlib value;
4. provide the exhaustive normative integrity-relation table and label any
   reduced diagram non-exhaustive;
5. show the seven-branch correction and historical rationale replacement;
6. enumerate all changed constants/hashes/counts and all preserved authority
   boundaries;
7. ask X and Y only bounded confirmation questions tied to Critical/Major
   implementation eligibility.

This is the final documentation repair round unless an independent reviewer
demonstrates a concrete Critical/Major authority, accounting, quarantine,
identifiability, or fail-closed defect. Minor wording, formatting, redundant
visualization, or non-operative commentary must be logged for implementation
and must not trigger another specification generation.

In chat report the verdict, output paths/hashes, validation-topology delta,
project-import binding, integrity-relation result, branch correction, residuals,
and the exact next boundary.
