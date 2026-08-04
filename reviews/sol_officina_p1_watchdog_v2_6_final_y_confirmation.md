# Final Y-line confirmation — Officina P1 watchdog v2.6

**Reviewer:** GPT-5.6 Sol, independent governance/statistical Y line

**Date:** 2026-08-04

**Review target:** committed tree `92c7012b6608c4eaa7eff920a0834f34c978963f`
(`Repair watchdog trust claims in v2.6`)

**Authority used:** the four governing inputs named below and the prior v2.5 Y
finding. The Opus 5 v2.6 closure was read as context only and was not treated as
authority.

## Verdict

```text
REVISE_OFFICINA_P1_WATCHDOG_V2_6
```

The honest procedural narrowing is acceptable for informed author selection in
this local, same-UID, author-operated research programme. An external freshness
anchor is not a claim-identification necessity for choosing between W-A and W-B.
The present bytes nevertheless cannot be confirmed because `Y25-1` is not fully
closed, the claimed complete integrity graph omits real edges, and three
unqualified digest-guard sentences can still be quoted as rollback-detection
claims even though `TR-2(b)` proves the contrary.

This verdict authorizes nothing.

## Custody and exact-byte basis

The live branch had advanced beyond the requested commit and contained unrelated
working-tree changes. I did not check out, edit, or use those changes. Every
review read was pinned to the `92c7012` tree. The four requested objects at that
tree recompute to:

```text
1dbb99b7390c943a6f82be2be867652f43504f03a87f9017349a1acd522369a9  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_6_CORRECTION.md
c3da2a7d24d0cea025f014f9231c0b856318b4a4c11ffc40c66972e7f905b3d1  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_3_DRAFT.md
6283d081df3eb3978bf963820859a5ebbf125689a4a3e249d3e85c1ca8d3d49d  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_6.md
7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md
```

The delimited joint install/authorization block in the amendment and composite
is byte-identical; both copies hash to
`b839a668b28ce0707a2c280bcc542bfd6ff74718dff71dbb1ac102ca93bbba8f`.

## Blocking findings

### B1. `Y25-1` remains open: several M4 meanings are not validated

The repair successfully fixes the JSON types, exact key sets, ordering,
canonical encoding, nested shapes, and `created_utc` grammar. It does not make
every claimed M4 relation part of one validity predicate.

1. `MS-4` requires `peer_amendment_sha256` to be a 64-character lowercase-hex
   string, but v1.3 no longer says there that it equals the M1 amendment digest,
   and no check compares it with the M1 amendment. `B18` checks Stage B's
   `governing_amendment_sha256`, which is a different field. Therefore an
   arbitrary well-formed `peer_amendment_sha256` can pass.

2. `reachable_closure` now has one structural representation, but the gate
   checks only that it is a non-empty, sorted, internally closed array with the
   stated element shapes. It does not require the module set, each `kind`, each
   `transitive_imports` value, or the three booleans to equal either the audited
   closure at composite §P1-3.3 or a closure recomputed from the production
   roots. Two different self-consistent arrays can both pass. Row 111 exercises
   malformed shape and self-closure, not a factually wrong but structurally
   valid closure.

3. `A16` proves only that Stage A's three pre-selection digest strings equal
   the corresponding strings in M4. Neither `TS-2` nor `CK-5` compares them to
   the actual reviewed pre-selection packet/amendment/composite digests or to
   literal constants. A coordinated arbitrary triple in Stage A and M4 passes.
   Path equality at `A13`/`A15` does not anchor the digest values.

The root-source and composite-region digest fields do have recomputation rules
elsewhere (`CHANGE 5`, `G-6`, and `G-7`), and the Stage-A binding fields are
anchored by `A17`; those fields pass this part of the audit. M7's M5/M6
relations are checked at `CK-11`, and the record/member relations are checked at
`CK-6` through `CK-8`. The omissions above are therefore bounded, but they
directly refute the packet's statement that every derived relation is checked.

**Required repair:** state the semantic source for every M4 digest/value and
assign a check to it. In particular, compare `peer_amendment_sha256` to the M1
amendment, anchor the three pre-selection hashes to immutable literal reviewed
values, and either validate `reachable_closure` against a fully canonical
audited value or specify and run a deterministic recomputation algorithm.

### B2. Two conforming verifiers can disagree on the first failure code

`CK-5` runs before `CK-6` through `CK-11` and says that M4, M7, and the install
record must satisfy their **full schemas and value grammars**, with any violation
reported as `MEMBER_SUBSTITUTED`. The later test rows draw a different boundary:

- `IR-3` makes equality of `install_record_id` to the IR-1 digest and filename
  part of the record value grammar. Under literal `CK-5`, a well-formed but
  mismatching id fails first as `MEMBER_SUBSTITUTED`. Row 105 instead requires
  that case to reach `CK-7` and return `INSTALL_RECORD_NAME_MISMATCH`.

- `MS-7` makes the literal verifier path, M5/M6 digests, module paths/order,
  bundle digest, row values, count, and passing assertion part of its value
  grammar. Under literal `CK-5`, a well-typed wrong value fails first as
  `MEMBER_SUBSTITUTED`. Row 113 says mismatches may reach `CK-11` and return
  `ATTESTATION_MISMATCH`, reserving `MEMBER_SUBSTITUTED` for when “the schema
  itself” is violated. “Schema itself” is not defined and contradicts `CK-5`'s
  express inclusion of value grammars.

Thus one implementation can treat `CK-5` as structural-only and another can
apply the written full value grammar. They reject the same bytes with different
first codes; for some M7 fields, a structural-only `CK-5` also depends on
whether `CK-11` happens to restate the relation. `FC-1`'s single first-failure
claim is therefore not constructible from the governing bytes.

The Stage-A `A1..A17` and Stage-B `B1..B18` algorithms themselves now cover all
top-level fields, exact types/literals, canonical bytes, key/id derivations,
signature encoding and verification, option pairing, Stage-A binding, install
id, member count, and M1 digests in a fixed order. Their remaining semantic
defect is the missing external anchor for the pre-selection digests described
in B1. The principal failure-code disagreement lies at the `CK-5` boundary for
M7 and the record.

**Required repair:** define a disjoint structural-validation phase and a
cross-object/value-validation phase, field by field, with exactly one earliest
clause and reason code for every malformed or mismatched value. Alternatively,
make `CK-5` own every full-value failure and rewrite rows 105 and 113 and the
later checks consistently.

### B3. Absolute digest-guard wording still permits a rollback-resistant overclaim

The composite contains three unqualified sentences that are true only while the
current generation's manifest/control set remains fixed:

- preamble, line 231: “no byte of it can change undetected”;
- `G-6`, lines 2856–2860: an edit “cannot pass unnoticed”;
- `G-7`, lines 2862–2864: “no byte of the file can change without detection.”

Under the exact `TR-2(b)` fixture, the composite changes from generation N+1
back to N together with M4, Stage A, Stage B, the signature, members, and sole
record, and `G-11` passes. These sentences therefore exceed the guarantee when
read without an unchanged-control-set qualifier. `TR-2`'s later prohibition on
overclaiming does not make a contradictory absolute sentence safe for future
publication.

**Required repair:** qualify all three statements as proper-subset/current-
generation checks, explicitly conditional on the matching manifest and
authorization chain not also being replaced, and cross-reference
`TR-2(b)`. No sentence should say an arbitrary byte change is detected.

### B4. The graph labelled “complete” omits Stage A's pre-selection edges

`TS-1.governing_pre_selection` carries three path/digest pairs for the packet,
amendment, and composite. Those are three directed integrity edges from Stage A
to the pre-selection inputs. `IR-4` calls its graph complete but lists only M4's
three edges to those inputs; it omits the parallel Stage-A edges. The packet's
graph repeats the omission. Composite §P1-14.5 link 4 also describes only the
composite and peer-amendment digests and omits the packet.

This does not revive the false unique-attester claim—on the contrary, it is one
more source of redundancy—but the “complete graph” and row 115 are not exact.

**Required repair:** add
`Stage A --path+digest--> the three pre-selection inputs` to `IR-4` and all
summaries/tests that claim graph completeness.

## Findings that pass

### `Y25-2`: the procedural narrowing is substantively accepted

The core `FS`/`TR` repair is honest and adequate for the stated procedural
threat model:

- `FS-1` identifies G-11 as a one-instant final-byte predicate and enumerates
  the present-state facts it proves.
- `FS-2` states that G-11 observes no event, reconstructs no history, trusts no
  timestamp, and has no monotonic counter, append-only predecessor, external
  witness, or notarized time. Its four byte-identical history pairs are correct.
- `FS-3` keeps `OR-1..OR-11` mandatory as contemporaneous operator procedure
  without calling that order retrospectively detectable.
- `FS-4` routes an actually observed contemporaneous departure fail-closed as
  `PROCEDURE_VIOLATION_OBSERVED`, through process/control invalidity and with no
  production entry. It is expressly non-scientific.
- `FS-5` places an unobserved departure in the residual and introduces no
  external anchor.

`PROCEDURE_VIOLATION_OBSERVED` is therefore correctly a report about an
observation made while the procedure or an exposing intermediate state exists;
it is not represented as evidence reconstructed from final bytes.

The repository-wide lexical sweep found install-protocol uses of order,
replay, rollback, freshness, monotonicity, custody, and attestation either in
explicit withdrawals/residuals or in the three conflicting digest sentences
identified at B3. Uses of replay, monotonic time, and liveness in the operative
runtime protocol describe watchdog/channel behaviour and are not claims of
cryptographic freshness for the install chain.

Conceptually, `Y25-2` is closed by narrowing; textually, corpus-wide closure
must wait for B3's qualifiers.

### `TR-2` and row 106(i) pass

`TR-2(a)` names full-chain substitution at or before Stage-A creation.
`TR-2(b)` separately names complete coherent rollback of a previously valid
generation **at any later time**, including Stage A, all 57 members, Stage B,
the detached signature, and the sole content-addressed record. It correctly
states that no new key or signature is needed, every `FS-1` check passes, the
state is runnable, and the gate does not refuse it.

Row 106(i) correctly constructs N, then N+1, restores N in full, expects G-11 to
**pass**, labels the case `OUTSIDE_GUARANTEE_COHERENT_ROLLBACK`, and fails a test
that expects refusal. This is the right expected result.

For author selection, the residual is complete enough. If future scientific or
governance claims require chronological authority, freshness, or rollback
resistance, an external monotonic/freshness anchor would be necessary and would
require a new design and review round. That is a governance/property choice,
not a prerequisite to identify and select the watchdog mechanism under the
present narrowed claim.

### `Y25-3` unique-attester wording is closed

No surviving positive claim says that each member has a unique attester or a
unique external attester. The old statements occur only as quoted, expressly
withdrawn text. `IR-4`, row 115, and the packet positively reject uniqueness.
The actual graph is redundant: the record digests all 57 members, M4 also binds
M1/roots/regions/pre-selection/Stage A, M7 also binds M5/M6/bundle assertions,
and Stage B plus its detached signature bind the authorization chain. B4 must
repair graph completeness, but uniqueness itself is no longer claimed.

### Identity-selection handling passes

The identity signature records only Kirill's selected identity architecture,
Option A,
`I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY`. `XS-1` and both
blocking notices correctly state that it:

- is not an `M1..M7` member and enters no install record;
- is not scientific evidence or an acceptance input;
- does not accept or authorize
  `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`;
- does not make the amendment/composite operative or resolve their blocking
  notice;
- does not select, influence, or activate the watchdog cell.

The later combined binding remains responsible for recording the identity
signature, separately accepting the bounded-weakening token or refusing, and
deriving the identity fields. The present watchdog pair does none of those
things.

### W-A/W-B symmetry, non-selection, and scientific inertness pass

All lines containing `[W-A]` or `[W-B]` in composite v1.6 are byte-identical to
the corresponding lines in v1.5 (extracted-line hash
`d8ceaed7ff000ca871ce9ff5e14ab8646389c824bb9dfc3e59c5a3800e2bf1e5`).
The only §A1–§A8 change is the necessary cross-reference from composite v1.5 to
v1.6; watchdog behaviour is unchanged. The whole-file markers remain balanced
13/13, and the body claim is balanced 10/10.

Neither option is selected or signable. W-B remains only a recommendation on
the same five criteria. The selection schemas, verification clauses, order,
failure codes, and new fixtures are option-independent. Both options remain
control-plane alternatives and scientifically inert at this stage.

### Terminal state passes

At tree `92c7012`:

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 WATCHDOG-FREEZE CELL = NOT SELECTED
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, author state only
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
```

The commit adds five documentation/review files only. The tree contains the
pre-install baseline `src/philosophia/officina/verification.py`, but contains
none of the two future M6 test modules, Stage A, Stage B, detached signature,
M4 manifest, M7 attestation, or content-addressed install record. Nothing in
the governing bytes authorizes a key, entropy draw, implementation, test run,
production entry, process operation, candidate, trajectory, datum, Proof, or
scientific/programme-claim movement.

## Smallest bounded repair

1. Complete M4's semantic validators for `peer_amendment_sha256`, all three
   pre-selection digests, and `reachable_closure`.
2. Make `CK-5`, rows 105/113, and `FC-1` define one unambiguous first-failure
   boundary and code for every M7/record field.
3. Qualify the three absolute digest-detection sentences by the unchanged
   current-generation control set and `TR-2(b)`.
4. Add Stage A's three pre-selection edges to the complete integrity graph and
   row 115.
5. Repeat bounded independent X/Y review on the repaired identical bytes.

## Authorization boundary

The next permissible action is a documentation-only v2.7 (or equivalent)
repair and a fresh bounded independent confirmation round. Kirill's watchdog
option selection is **not yet authorized by this review**.

No key, entropy, Stage A/B artifact, detached signature, M4, M7, install record,
implementation, test execution, production entry, candidate, trajectory,
scientific datum, Proof, activation, or claim movement is authorized.
