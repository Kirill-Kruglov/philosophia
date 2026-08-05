# Final Y-line confirmation — Officina P1 watchdog v2.7

**Reviewer:** GPT-5.6 Sol, independent governance/statistical Y line

**Date:** 2026-08-05

**Review target:** exact commit
`9acc3eaa64cfb8085faf32348bf05dab2a9ba97d`
(`Repair watchdog semantic checks in v2.7`)

**Authority used:** the four byte-pinned primary inputs, the governing v2.6 Y
review, and direct reconstruction from the governing bytes. The v2.6 X review
and the Opus 5 v2.7 closure were read as context only. The Opus 5 closure was
not treated as authority.

## Verdict

```text
REVISE_OFFICINA_P1_WATCHDOG_V2_7
```

The v2.7 repair genuinely closes the narrow `peer_amendment_sha256` hole, the
literal-value side of `reachable_closure`, the three pre-selection digest
anchors, and the three rollback-overclaim sentences. The `§A0.4` anchor is an
honest, non-circular cross-file commitment rather than a disguised freshness
claim.

Confirmation nevertheless cannot issue. The written first-failure order still
has states for which no unique first owner is defined; the graph called
complete omits at least one real cross-object authorization edge; and MS-11's
denotation excludes `generic_harness.py` on a premise contradicted by the
operative launch: that module has its own 17-name scoped allowlist and is
imported inside every role at `A-10`, not merely run under the 19-name default
in caller context. Root hashes and root-AST rules do not audit the transitive
effects of the modules imported during that role import.

This verdict authorizes nothing.

## Custody and exact-byte basis

The live branch had advanced to `9b86f274...` and the working tree already
contained unrelated modified and untracked files. I did not check out, edit,
stage, or use those changes as governing evidence. The four named inputs in the
worktree are byte-identical to `9acc3ea` and recompute to:

```text
a03afc3acab5e37d9b27c4f1538887aa5216f6a910546ac2389bede8ede3efb0  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_7_CORRECTION.md
f845b98dcef0edc415420fec1103f7adad4f905c21380a0dddcba0d3b370b794  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_4_DRAFT.md
5301f7e987b768cc3acd9641f6f00400a74b453773299cbd379473c7db569beb  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_7.md
7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md
```

Commit `9acc3ea` adds five documentation/review files and modifies no historical
file. The delimited joint install/authorization block is byte-identical in the
amendment and composite. The amendment contains exactly one line matching the
`A16(d)` anchor grammar, and its value is the composite digest
`5301f7e9...569beb` above.

## Findings by severity

### Blocking for v2.7 Y-line confirmation

#### 1. `Y26-B2` is not closed: the actual precedence is not total

`VP-3`'s field table is substantially better than v1.3's mixed
structural/value grammar, but the executable order in `VP-4` and `CK-1..CK-13`
still leaves at least two multi-fault boundaries undefined.

First, `CK-2` runs all of `A1..A17`, including M4-dependent `A15`, `A16(a)`
and `A17`, before `CK-6` establishes that M4 exists, parses as JSON, is an
object, and has the required fields and types. Neither `TS-2` nor `CK-2`
defines how those clauses read an absent, invalid-JSON, non-object, or
missing-key M4. For example, with a valid Stage A and an absent M4, one verifier
can map the failed read at `A15` to `STAGE_A_PRESELECTION_MISMATCH`; another can
defer the absent-member fact to `CK-6` and return `MEMBER_OMITTED`; a literal
implementation can also have no specified reason-code mapping for the failed
field access. `VP-4` orders predicates but does not create the prerequisite
object value they need.

Second, `CK-6` applies `VP-1` to M4, M7 **and the install record**, while
`VP-4(4)` orders only the 61 members in `IR-1` order. The install record is not
one of those members. Its structural-validation position relative to the 61
member existence/digest checks is therefore unstated. A state with a malformed
sole record and an absent or stale member can return either
`MEMBER_SUBSTITUTED` for the record or `MEMBER_OMITTED`/`MEMBER_STALE` for the
member, depending on where a conforming implementation inserts the record
check.

There are also textual symptoms of the same incomplete partition: `CK-7` says
to evaluate every `MS-12` relation, while `VP-3` says the six pre-selection and
three Stage-A rows are owned earlier by `CK-2` and are not re-raised at `CK-7`;
and `CK-13` reasserts M2/M3 byte identity already made fatal at `CK-6` despite
`VP-2` saying structural and semantic predicates are not re-evaluated. These
later contradictions do not create an accepted bad value, but they refute the
claimed exactly-one-owner description.

The structural/semantic split therefore closes the three v2.6 examples in
their single-fault fixtures, but it does not give exactly one first owner and
code for every multi-fault byte state.

#### 2. MS-11's denotation creates an unguarded role-import route

MS-11 defines `reachable_closure` as only the at-import closure of the two
bootstrap allowlists. That division is acceptable for the activation and
standalone verification scripts: they execute in caller tooling, their source
bytes are pinned, and they do not become role code merely by being roots.

It is not acceptable for `src/philosophia/officina/generic_harness.py`.
MS-11 says all three excluded roots run under the 19-member global default in
caller context. The same composite says the opposite in two operative places:

- `§P1-3.2` gives `generic_harness.py` its own exact 17-member scoped allowlist,
  never the union with the global default.
- `§P1-7.4 A-10` imports `philosophia.officina.generic_harness` inside the
  `SUPERVISOR`, `WATCHDOG`, `CONTROLLER`, and `WORKER` role bootstraps, after
  `sys.path` replacement and before the pinned entry function is called.

Consequently this root is part of the role import path whose task, at-fork,
handler/hook, signal-state, and import-origin effects matter directly to the
watchdog/control claim. `root_source_sha256` proves only which root bytes were
installed. `S-1..S-24b` constrain root ASTs and selected call/topology
properties; they do not enumerate or pin the transitive standard-library
modules executed by `generic_harness.py`, and the role path does not repeat
`P-c`, `P-d`, and `P-g` after `A-10` to make all such import effects irrelevant.
Calling the excluded root merely caller-context code therefore leaves a real
semantic gap.

The repair must either include the actual role import closure of
`generic_harness.py` in a reviewed canonical value, or add an equivalently
complete and fail-closed argument that constrains its direct imports,
transitive imports, and post-import effects. It must also state the scoped
17-member context correctly.

At the exact commit tree only `scripts/officina_activate_t.py` and
`scripts/verify_officina_active.py` of the five named roots are tracked;
`generic_harness.py` exists only as an unrelated untracked working-tree file,
and both bootstrap roots are absent. Thus the target commit itself contains
two tracked roots and three future roots, not three tracked roots and two
future roots. No untracked implementation byte can supply evidence for this
review.

#### 3. `Y26-B4` is not fully closed: the graph still omits an edge

The three Stage-A pre-selection edges are now present, and the new

```text
M1 amendment --anchor-line digest--> pre-selection composite bytes
```

edge is real. Independent derivation also confirms the record-to-members,
M4-to-M1/roots/regions/pre-selection/Stage-A, M7-to-M5/M6/bundle/test-assertion,
Stage-B-to-Stage-A/record/M1, and detached-signature-to-Stage-B families.

But the graph omits the cross-object relation enforced at `B14`:

```text
Stage B --selected_option_token equality--> Stage A
```

That relation is not cosmetic. It is the link making the option token inside
the signed Stage-B bytes agree with the option selected in Stage A, and
`TR-2` itself lists an option mismatch between the two stages as a closed
proper-subset case. The graph includes other non-digest relations—key pin,
member count, and M7 assertions—so it cannot exclude `B14` while honestly
calling itself the complete directed integrity/authorization graph. At minimum
the edge must be added to `IR-4`, the summaries, and row 115, or the graph's
scope and the word “complete” must be narrowed explicitly.

### Passed repairs

#### `Y26-B1(1)` is closed

For an otherwise valid state, an arbitrary well-formed
`peer_amendment_sha256` survives `CK-6`'s lexical check and reaches `CK-7`.
`CK-7` recomputes the SHA-256 of the M1 amendment at its literal path and
returns `MANIFEST_VALUE_MISMATCH` on inequality. `B18` independently requires
Stage B's governing amendment digest to equal both the M1 bytes and the
manifest field. No arbitrary well-formed value can pass under the written
single-fault order.

This conclusion does not cure the separate prerequisite-order defect above:
it assumes the otherwise valid M4 needed to reach `CK-7`.

#### `Y26-B1(2)` is closed as an internal value check

`MS-11.1` supplies one fourteen-row JSON value; `MS-11.3` requires JSON-value
equality and pins the canonical encoding. I independently reconstructed that
encoding:

```text
length  2118
sha256  e28c33e3985317a25c333a02674784cb23516b9c50232f8064deed17a8abf287
```

The rows are sorted, distinct, and self-closed. A structurally valid value that
differs in module membership, kind, imports, or booleans is semantically wrong
relative to the literal and reaches `CK-7`/
`MANIFEST_VALUE_MISMATCH`; row 111 now contains the appropriate class of
fixtures. As elsewhere in this design, the hash form assumes SHA-256 collision
resistance; a direct comparison with the literal JSON value is the clearest
implementation of the stated equality.

That is internal consistency, not proof that the literal describes reality.
The origin values spot-check correctly on the pinned CPython 3.12.3 build, but
the complete module-edge and forty-two-boolean claim remains a factual software
claim for the independent X line to reproduce. More importantly for Y, even a
factually perfect fourteen-row value does not validate the scientifically
inadequate two-bootstrap-only denotation identified above.

#### `Y26-B1(3)` is closed; the `A0.4` anchor is accepted

`A16(b)` hashes the named packet bytes; `A16(c)` hashes the named amendment
bytes; and `A16(d)` accepts exactly one grammar-matching anchor line from the
amendment. The line's value equals the pre-selection composite digest reviewed
here. The composite contains no digest of itself; the amendment carries the
composite digest; the amendment is separately hashed as M1 and bound through
M4, the record, and signed Stage B. This is an ordinary, acyclic cross-file
commitment, not merely a relocated unchecked assertion, because the independent
pre-selection reviewers can and must compare the line to the surviving
pre-selection composite bytes before author selection.

After `OR-4`, those exact composite bytes no longer survive and the final-state
gate cannot recompute their digest. That limitation is disclosed rather than
hidden. Under complete coherent rollback the earlier amendment, anchor,
packet, M4, Stage A/B, signature, members, and record return together and every
check passes. The anchor therefore closes only the coordinated arbitrary-
triple proper-subset case and supplies no freshness or rollback resistance.

#### `Y26-B3` is closed

All three live v1.7 sentences are now expressly current-generation,
proper-subset statements:

- the preamble conditions `H_FILE` refusal on the matching manifest and
  `TS-1..TS-6` chain remaining fixed and names `TR-2(b)`;
- `G-6` applies the same condition to the normative regions and withdraws
  “cannot pass unnoticed”;
- `G-7` applies the same condition to the whole file and withdraws “no byte of
  the file can change without detection.”

An independent commit-wide lexical sweep found the old absolute strings still
present in historical composites v1.1 through v1.6 and in reviews/quoted
withdrawals. They are not silently erased. `DA-1..DA-4` make those historical
composites document-level provenance with no behavioural authority. In the new
packet, amendment, and operative composite, positive watchdog-install uses are
either the three fixed-current-chain claims or explicit denials/residuals. No
live v1.7 sentence claims arbitrary-byte, full-generation, or coherent-
rollback detection, refusal, resistance, freshness, recency, or external
custody.

### Preserved boundaries and residuals

`FS-1..FS-5` survive without rhetorical narrowing. In particular:

- `FS-1` remains a one-instant final-byte predicate; its new clause (g) adds
  the new anchors but no historical claim.
- `FS-2` still says no event or history is reconstructed and no timestamp,
  monotonic counter, predecessor chain, notary, or external witness is trusted.
- `FS-3` keeps `OR-1..OR-11` mandatory as procedure.
- `FS-4` keeps `PROCEDURE_VIOLATION_OBSERVED` contemporaneous, fail-closed,
  control-plane-only, and scientifically inert.
- `FS-5` keeps an unobserved violation in the accepted procedural residual and
  expressly introduces no external freshness anchor.

Both `TR-2` residuals remain: full-chain substitution at or before Stage-A
creation, and complete coherent rollback at any later time. The four newly
closed items are added only to the proper-subset list. Row 106(i) still requires
`G-11` to **PASS** on a fully restored generation and fails a fixture that
expects refusal. The `A0.4` anchor does not narrow either residual.

Freezing a literal closure before the bootstrap roots exist is not, by itself,
a reversal of evidence and implementation. At this stage the value can be a
reviewed contract that future root bytes must satisfy; `S-1`, MS-11.4, the root
hashes, M4, the matrix, M7, the install record, and Stage B are later gates.
That is legitimate only if it is described as a prospective conformance
constraint and not evidence that an implementation already exists. It does not
cure the excluded role-import route, and no implementation or install may
proceed on v2.7 until that denotation is repaired and independently reviewed.

## State and symmetry

The extracted `[W-A]`/`[W-B]` lines in composite v1.7 are byte-identical to
v1.6 (SHA-256 `d8ceaed7ff000ca871ce9ff5e14ab8646389c824bb9dfc3e59c5a3800e2bf1e5`
for each extraction). Markers remain balanced 13/13 whole-file and 10/10 in
the body. W-A and W-B remain symmetric and unselected; W-B remains only the
same recommendation.

The identity signature remains external author state only. Option A is
recorded but not bound into M1..M7, not scientific evidence, and not operative.
`P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` remains unaccepted, with no
bounded weakening accepted under another name. Nothing in commit `9acc3ea`
creates a key, Stage A/B artifact, signature, M4, M7, record, implementation,
test, install, activation, candidate, trajectory, datum, Proof, or claim
movement.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 WATCHDOG-FREEZE CELL = NOT SELECTED
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, external author state only
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
```

## Smallest bounded repair

1. Reorder or split the checks so M4 existence/parse/shape is established
   before `A15..A17`, and state the exact position of install-record structural
   validation relative to all 61 member checks. Remove or reconcile the
   `CK-7`/`VP-3` and `CK-13` ownership duplications, then add multi-fault
   fixtures.
2. Correct MS-11's execution-context statement and close the actual role import
   surface of `generic_harness.py`, either in the canonical closure or by an
   equally complete post-import/static predicate.
3. Add the `B14` Stage-B-to-Stage-A selected-option edge everywhere graph
   completeness is asserted, or narrow the graph's declared scope and name.
4. Correct the implementation-existence statement for the exact review tree
   and repeat bounded independent X/Y review on identical repaired bytes.

## Authorization boundary

The next permissible action is a documentation-only v2.8 (or equivalent)
repair and a fresh bounded independent X/Y confirmation round. Kirill's
watchdog option selection is **not authorized** by this review.

No key, entropy, Stage A/B artifact, detached signature, M4, M7, install
record, implementation, test execution, manifest, install, production entry,
activation, candidate, trajectory, scientific datum, Proof, or programme-claim
movement is authorized.
