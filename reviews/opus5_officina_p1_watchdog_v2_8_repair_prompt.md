# Officina P1 watchdog v2.8 bounded role-import and precedence repair

You are Claude Code Opus 5, specification repair author. Work in:

`/home/master/llm_projects/philosophia`

Review base commit: `15357b7` (`Review watchdog v2.7 role import boundary`).
Do not modify historical files, code, tests, untracked work, signatures, or
runtime artifacts. Do not commit.

## Exact inputs

v2.7 governing bytes:

- `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_7_CORRECTION.md`
  `a03afc3acab5e37d9b27c4f1538887aa5216f6a910546ac2389bede8ede3efb0`
- `successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_4_DRAFT.md`
  `f845b98dcef0edc415420fec1103f7adad4f905c21380a0dddcba0d3b370b794`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_7.md`
  `5301f7e987b768cc3acd9641f6f00400a74b453773299cbd379473c7db569beb`

Independent reviews:

- X confirmation:
  `reviews/fable_officina_p1_watchdog_v2_7_independent_x_confirmation.md`
  `4855020e522228eeb0625fba1efb78941bc547c124da2d1dbb754b548d3057cc`
- Y revision:
  `reviews/sol_officina_p1_watchdog_v2_7_final_y_confirmation.md`
  `0b33108e885fec97ab11e2de5c6ac3ba6ceeb8e98283bb29a09c70ce1c574780`
- signed identity state:
  `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md`
  `7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f`

X independently reproduced the existing fourteen-row bootstrap closure exactly.
Preserve those verified rows. Y accepted A0.4, M4's literal-value repair, all
rollback qualifiers, the procedural residual, and prospective freezing before
implementation. Y returned `REVISE_OFFICINA_P1_WATCHDOG_V2_7` on exactly three
blocking defects plus one repository-state wording correction.

## Deliverables

Create exactly:

1. `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_8_CORRECTION.md`
2. `successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_5_DRAFT.md`
3. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_8.md`
4. `reviews/opus5_officina_p1_watchdog_freeze_choice_v2_8_closure.md`

Carry v2.7 forward except for R1-R4. No new author cell is permitted.

## R1 — make the validation order genuinely total

Repair the exact multi-fault gaps identified by Y. A table alone is not enough;
every predicate's prerequisites must exist before it runs.

### R1.1 M4 prerequisite

Split Stage-A validation into:

- a self-contained stage that reads only Stage A and already validated direct
  prerequisites (`A1..A14` or an exactly equivalent partition);
- a later M4-dependent stage for `A15..A17`, executed only after M4 existence,
  JSON parse, object type, exact schema/key/type/shape and structural grammar
  have succeeded.

No clause may read an absent, invalid-JSON, non-object, missing-key or wrongly
typed M4. Give each such state one earlier owner and one code.

### R1.2 install record versus members

State the exact structural-validation position of the non-member install record
relative to all member checks. Use one literal order, for example:

1. locate exactly one record;
2. structurally validate that record;
3. enumerate and validate the member set in one fixed order;
4. run semantic/cross-object relations.

The chosen order must cover a malformed record plus absent/stale member with one
unambiguous first code. Do not leave “inside CK-6” as the ordering rule.

### R1.3 remove duplicate ownership

- `CK-7` must not claim relations assigned to the later M4/Stage-A binding
  stage.
- `CK-13` must own a relation distinct from every relation already fatal
  earlier, or be removed/merged with counts and references updated.
- Every field and every cross-object relation has exactly one earliest owner.

Provide a literal topological predicate order, a complete relation-to-owner-
to-code table, and multi-fault fixtures including at minimum:

- valid Stage A + absent M4;
- valid Stage A + invalid-JSON M4;
- malformed sole install record + absent member;
- malformed sole install record + stale member;
- M4 semantic mismatch + Stage-A binding mismatch;
- changed M2/M3 bytes + coordinated record/member mismatch.

Two independent implementations must return the same first code in each case.

## R2 — cover the actual role import surface

Y established that `generic_harness.py` is imported inside every role at A-10
and has its own exact 17-name scoped direct-import allowlist:

```text
__future__ ast dataclasses datetime enum fcntl hashlib hmac json os pathlib
re subprocess time typing weakref _socket
```

It is not caller-only. Root hashes and S-1..S-24b do not by themselves cover
the import-time transitive effects relevant to watchdog/control.

### Required denotation

Redefine the canonical role `reachable_closure` to cover the import-time
closure of:

1. both bootstrap-root scoped allowlists; and
2. the `generic_harness.py` scoped role-import allowlist used at A-10.

Activation and standalone verification scripts may remain caller-only if the
argument is stated accurately.

### Fail-closed audit before choosing the literal

On the exact pinned interpreter/build/flags, independently and without
importing or executing Philosophia production modules:

1. derive every direct and transitive module in the combined role closure;
2. pin every module's kind and import-time edges;
3. audit `starts_task`, `registers_at_fork`, and `installs_handler` for every
   row;
4. identify all platform-conditional branches;
5. detect any transitively reached module that the operative contract elsewhere
   calls forbidden, especially effects reached through `subprocess`, `typing`,
   `dataclasses`, `pathlib`, or `weakref`;
6. distinguish `from __future__` compiler directives from runtime imports.

Do **not** merely expand the literal array if the resulting closure violates the
watchdog/control invariants. If a direct import unnecessarily admits a forbidden
or side-effectful transitive surface, choose the smallest prospective scoped-
allowlist reduction consistent with the signed generic-harness contract and the
future implementation obligations, state every removed name and why, and make
the future code conform. If no such reduction is contract-compatible without a
new author decision, emit `BLOCKED_OFFICINA_P1_WATCHDOG_V2_8` rather than hiding
the conflict.

The new governing bytes must contain one full canonical literal value, its
CANON length/hash, exact audit method, factually-wrong fixtures, and a rule that
future root bytes/import graph changes require a new reviewed generation.
Preserve the independently confirmed fourteen-row bootstrap subset exactly.

The untracked worktree `src/philosophia/officina/generic_harness.py` is not
governing evidence and must not be edited or silently adopted. The contract's
literal allowlist is the prospective source unless a reviewed reduction above
is necessary.

## R3 — complete the authorization graph

Add the omitted cross-object edge everywhere completeness is asserted:

```text
Stage B --selected_option_token equality (B14)--> Stage A
```

Update `IR-4`, every packet/composite graph summary and row 115. Re-derive the
graph from all path-, digest-, id-, signature-, option-, key-, member-count- and
assertion-bearing relations and add any other omission found. Preserve the
explicit rejection of unique-attester claims.

## R4 — correct repository-state and preserve closed work

The exact reviewed commit contains only two tracked production roots:

- `scripts/officina_activate_t.py`
- `scripts/verify_officina_active.py`

Both bootstraps are absent. `generic_harness.py` is unrelated untracked work in
the live worktree and is not evidence at the reviewed commit. State this
accurately wherever implementation existence is discussed.

Preserve without reopening:

- A0.4 as an honest acyclic cross-file commitment, not freshness;
- the verified fourteen-row bootstrap subset;
- M4 peer/pre-selection anchors and rollback-qualified digest language;
- `FS-1..FS-5`, `TR-2(a)/(b)`, row 106(i) expected PASS;
- W-A/W-B behavior, symmetry and recommendation; neither selected;
- identity Option A as external author state, bounded weakening unaccepted;
- `T=NOT_ACTIVATED`, programme claim `OPEN`, all negative authorization space.

Recompute every digest, region/joint-block hash, path, member class/count,
provenance count, rule/check/code/test count and cross-reference. Do not copy
v2.7 numerics after the closure expansion or check-order repair.

## Closure requirements

Emit exactly one:

- `READY_FOR_OFFICINA_P1_WATCHDOG_V2_8_FINAL_XY_CONFIRMATION`
- `REVISE_OFFICINA_P1_WATCHDOG_V2_8`
- `BLOCKED_OFFICINA_P1_WATCHDOG_V2_8`

The closure must:

1. disposition all three Y blockers and the repository-state correction;
2. show the exact new validation topology and all mandated multi-fault results;
3. show the complete role-import closure or explain a fail-closed BLOCKED route;
4. list any scoped-allowlist reduction and prove it does not change a signed
   scientific cell;
5. show the complete graph including B14;
6. state all residuals and prove no authority/scientific state moved;
7. ask bounded independent X and Y questions on the new bytes.

This is documentation-only. No key, entropy, Stage A/B, code edit, test run,
manifest, attestation, install, process, activation, candidate, trajectory,
datum, Proof or claim movement is authorized.

In chat report the verdict, output paths/hashes, combined closure cardinality,
any allowlist reduction, exact check topology, graph delta, residuals and next
boundary.
