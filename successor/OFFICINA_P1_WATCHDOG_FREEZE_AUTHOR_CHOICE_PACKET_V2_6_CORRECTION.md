# Officina P1 watchdog-freeze mechanism — author choice packet v2.6 (correction)

**Author:** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This correction selects nothing.**

**No token here is signable** until a bounded independent X-line and Y-line
confirmation round confirms this correction, the v1.3 peer amendment and
composite v1.6 on identical bytes — **performed by reviewers that did not author
v2.3, v2.4, v2.5 or v2.6.** `T` is `NOT_ACTIVATED`; the programme claim is
`OPEN`. This document creates nothing executable and authorizes no
implementation, activation, process control, resource spend, T/Q/C datum,
outcome, Proof or claim movement. **It modified no existing file, generated no
key and created no artifact.**

---

## §0. Scope — narrow, and stated as a limit

**v2.6 is a schema-completeness and honesty repair. It reopens no watchdog
behaviour and no option design.** The independent X line confirmed v2.5 in full.
The Y line confirmed the member set and the signature chain and returned
`REVISE` on three things: incomplete generated schemas, false retrospective
order and replay claims, and false unique-attester wording. v2.6 repairs exactly
those three and nothing else.

```text
NO NEW OPTION. NO NEW TOKEN. NO NEW AUTHOR CELL. NO NEW SCIENTIFIC CELL.
NO NEW CONSTANT. NO NEW WATCHDOG MECHANISM. NO NEW TREATMENT. NO NEW EVIDENCE
CLASS. NO IMPLEMENTATION AUTHORITY. NO ACTIVATION AUTHORITY.
NO MECHANISM CHANGED. THE RECOMMENDATION DID NOT MOVE.

AND, EXPLICITLY, THE ROUTE NOT TAKEN:
NO HARDWARE SECURITY MODULE. NO EXTERNAL SERVICE. NO TIMESTAMP ORACLE. NO
NOTARY. NO TRANSPARENCY LOG. NO MONOTONIC-COUNTER DEVICE. NO NEW SCIENTIFIC
GATE. The Y line offered two routes for its second finding; v2.6 takes the
HONEST PROCEDURAL ROUTE and says exactly what the gate does and does not prove.
```

### §0.1 The two binding v2.5 verdicts

```text
X-line, reviews/fable_officina_p1_watchdog_v2_5_independent_x_confirmation.md
        c2e9ddb2e6270f2b870986b01d1114ea68d5f3e1db466f165ee2f47a0f256427
        OFFICINA_P1_WATCHDOG_V2_5_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION
        Reviewer: Claude Code, model claude-opus-4-8, fresh session.

        CONFIRMED, all ten bounded items, each independently recomputed:
          1  cross-references resolve; no live §P1-19
          2  member set enumerable; cardinalities 2/39/7/1/1/2/1 = 53; all 21
             class pairs disjoint; all 46 M2+M3 digests matched; 47 provenance
             rows, 47 = 39 + 7 + 1
          3  M4/M5/M6/M7 exact schema, paths, encoding and bundle rule;
             CK-4 draws only on MS-1..MS-7
          4  Stage A token pairing, key and key id, pre-selection binding,
             exact threat bytes, and the temporal gate on Kirill's token
          5  Stage B canonical bytes, pure Ed25519, detached encoding, bindings
          6  OR-1..OR-11 has exactly one conforming order
          7  no self-attestation; Stage artifacts outside M1..M7; partial
             substitution rejected
          8  TR-2 states, and does not close, full-chain substitution; no
             stronger claim survives anywhere
          9  stated counts recomputed: 216 = 162 + 54; 132 amendment tags; 53
             members; 24 test rows; 47 provenance rows; 24 failure codes
         10  accepted behaviour, option symmetry and non-selection, and the
             negative space unchanged
        BLOCKING-CONDITION SWEEP: none found.

Y-line, reviews/sol_officina_p1_watchdog_v2_5_final_y_confirmation.md
        80d42229b2e9b32e51a5448c10af410640e2088f777334fa4431f29e4e840c81
        REVISE_OFFICINA_P1_WATCHDOG_V2_5
        Reviewer: GPT-5.6 Sol, independent governance Y line.

        PASSES: literal enumeration and disjointness (§1); the Stage-B
        cryptographic binding as non-circular on its stated procedural threat
        model (§3); scientific and authorization boundaries (§6). All 39 MS-2
        and 7 MS-3 rows, the empty intersection, the four region digests and
        the byte-identical joint block were reproduced.

        Y25-1  GENERATED-SCHEMA COMPLETENESS — the schemas are not yet
               constructible without a further choice. MS-4 does not define the
               JSON type, entry shape or ordering of reachable_closure, and
               composite §P1-3.3 is a prose table, not a canonical JSON value.
               MS-4, MS-7 and IR-3 give no value grammar for created_utc, and
               none states the mandatory value of the schema key as the older
               exact record definitions do. TS-1 describes the three
               governing_pre_selection paths in words; the literal v2.5 packet
               path does not occur in either governing file. TS-2(c)..(f) and
               TS-5 check only selected bindings and never expressly check
               schema, version, author, signature_algorithm, the embedded
               pre-selection paths, threat_model or created_utc. Consequence:
               two independent verifier implementations cannot derive the same
               artifact-validity predicate.

        Y25-2  FORBIDDEN HISTORICAL ORDER IS NOT MECHANICALLY DISTINGUISHABLE,
               and complete-generation rollback passes — BLOCKING, two parts.
               (a) CK-1..CK-12 authenticate only the final byte state. There is
                   no trusted monotonic event, append-only predecessor,
                   externally checked sequence number or other order evidence.
                   Given the exact valid final bytes, no check observes that
                   the record was written before Stage B existed, that M7 was
                   written before the matrix ran, that an id was computed from
                   planned M4 bytes, or that Stage A was created after variant
                   resolution. created_utc does not repair this and would not
                   be trusted order evidence in any case. Therefore composite
                   test 106(h), OR-11's early-record refusal, packet §3.2 and
                   closure §4.1's "any deviation" statement are not mechanical
                   consequences of G-11.
               (b) A repository writer can restore a previously valid bundle in
                   full — its Stage A, all members, Stage B, detached signature
                   and sole content-addressed record. Stage A matches the
                   restored M4; the old signature verifies under the restored
                   key; the old id matches the restored members and the sole
                   record name; CK-10 sees one record; every digest matches.
                   A whole-generation post-hoc replay therefore reaches a
                   runnable state, and TR-2's claim to close "every post-hoc
                   substitution" is false. The residual's temporal scope is too
                   narrow.

        Y25-3  FALSE UNIQUE-ATTESTER WORDING. IR-4 says every member is
               attested by exactly one other object and test row 115 says by
               the record "and by nothing else". That is literally false: M4
               carries M1 digests and M7 carries M5/M6 digests while the record
               also carries all member digests. This does not create
               self-attestation; the uniqueness wording should be removed.
```

**The two lines do not conflict.** X audited constructibility and
non-circularity of the dependency graph and found them sound; Y audited what the
governing bytes *claim* and found three claims exceeding what the bytes deliver.
v2.6 changes no structure X confirmed; it completes the schemas and narrows the
claims.

### §0.2 The v2.5 pair is wholly replaced

```text
REPLACED, NOT AMENDED:
  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_2_DRAFT.md
    058c119c5de770dc537fd16962723063d2c3d4dad5da17d1431d4402927ebd1b
  successor/…P1_OPERATIVE_COMPOSITE_V1_5.md
    8751317511a3f738de35402b3c67ab9786e7fe1c95ea12d1e175ddd6540ddb20

Both become PROVENANCE on acceptance of the v2.6 pair, at document
granularity. Their bytes are not edited. In MS-2's literal order they are
members 40 and 41, with the two v2.5 independent confirmations as members 42
and 43; the v2.4 pair and its two confirmations remain members 36 through 39.

THE NEW GOVERNING PAIR:
  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_3_DRAFT.md
    c3da2a7d24d0cea025f014f9231c0b856318b4a4c11ffc40c66972e7f905b3d1
  successor/…P1_OPERATIVE_COMPOSITE_V1_6.md
    6283d081df3eb3978bf963820859a5ebbf125689a4a3e249d3e85c1ca8d3d49d
```

---

## §1. Part A — every generated schema and validator completed (`Y25-1`)

### §1.1 What each generated object now fixes

```text
OBJECT   WHAT v1.2 LEFT OPEN            WHAT v1.3 FIXES
M4       reachable_closure had no type, MS-4 gives all twenty top-level keys
         entry shape or order; §P1-3.3  with exact types, and ONE canonical
         is a prose table                JSON shape for reachable_closure:
                                         an ARRAY of OBJECTS with EXACTLY the
                                         six keys module, kind,
                                         transitive_imports, starts_task,
                                         registers_at_fork, installs_handler;
                                         kind ∈ four literals;
                                         transitive_imports sorted ascending by
                                         code point and pairwise distinct;
                                         the array sorted ascending by module,
                                         module values pairwise distinct; and a
                                         CLOSURE rule — every name appearing in
                                         any transitive_imports also appears as
                                         some element's module.
         no created_utc grammar          MS-10, one grammar for every object
         schema value not stated as the  the exact mandatory literal is stated
         mandatory value of the key      as the value of the schema key
         (3 new keys)                    pre_selection_{packet,amendment,
                                         composite}_path added, so Stage A's
                                         embedded paths are checkable
M7       no created_utc grammar; schema  MS-7 states the mandatory schema
         value not pinned; nested        literal, version 1, the exact
         shapes/order loose              two-element ordered
                                         test_bundle_modules shape, the exact
                                         24-integer ascending rows_attested,
                                         row_count 24 and all_rows_passed true
RECORD   same omissions                  IR-3 states the mandatory schema
                                         literal, version 1, the 57-entry
                                         members array with exactly the three
                                         keys per entry, and IR-1's sort order
                                         as PART OF THE VALUE
STAGE A  three pre-selection paths       TS-1 states all three as LITERAL
         described in words, and the     repository-relative strings, and they
         v2.5 packet path occurred in    are the v2.6 successors actually
         neither governing file          reviewed: the v2.6 packet, the v1.3
                                         amendment and the v1.6 composite
STAGE B  values/types not pinned per key TS-3 gives an exact type and value
                                         grammar for all thirteen keys,
                                         including install_record_path as a
                                         literal concatenation
```

### §1.2 The two verification algorithms are now exhaustive

```text
TS-2  STAGE A, clauses A1..A17. A1 path · A2 canonical bytes · A3 exact
      eleven-key set · A4 schema literal · A5 version integer 1 · A6 author
      literal · A7 algorithm literal · A8 option token · A9 paired
      option-specific token · A10 public key form · A11 key id derivation ·
      A12 pre-selection shape · A13 pre-selection literal paths · A14
      threat_model bytes and created_utc grammar · A15/A16 manifest
      pre-selection path and digest binding · A17 manifest Stage-A binding.

TS-5  STAGE B, clauses B1..B18. B1 both paths · B2 canonical bytes · B3 exact
      thirteen-key set · B4 schema literal · B5 version integer 1 · B6
      created_utc · B7 member_count 57 · B8 five hex fields · B9
      install_record_path concatenation · B10 algorithm literal · B11 signature
      encoding · B12 Ed25519 under Stage A's key and no other · B13 Stage-A
      path/hash/key id · B14 option equality · B15 recomputed id · B16 record
      file · B17 enumerated member count · B18 both M1 digests.

EVERY MANDATORY LITERAL AND EVERY DERIVED RELATION IS CHECKED. NO FIELD IS
SATISFIED BY MERE PRESENCE. Each clause names the failure code it raises, so
two implementations agree not only on validity but on the reason for refusal.
```

### §1.3 `created_utc`, once, and never as order evidence

```text
MS-10 fixes one grammar — exactly 20 ASCII characters,
YYYY-MM-DDThh:mm:ssZ, no fraction, no offset but the literal Z, no lowercase
t or z — and one semantic validator: 2000..2999, month 1..12, day bounded by
the proleptic Gregorian calendar with the ordinary leap rule, hour 0..23,
minute and second 0..59, NO LEAP SECOND.

AND THE CLAUSE THAT MATTERS MOST: created_utc IS PROVENANCE ONLY AND IS NOT
TRUSTED TEMPORAL-ORDER EVIDENCE. No check compares two created_utc values,
orders artifacts by them, derives a construction sequence from them, or
refuses on their relative values. A verifier that ordered artifacts by
created_utc would be trusting an unauthenticated author-supplied string.
```

### §1.4 New fixtures

Row 105 now exhausts the install-record schema; row 111 exhausts every `MS-4`
field including every `reachable_closure` malformation and six `created_utc`
malformations; row 113 exhausts every `MS-7` field; row 106(j) walks each of the
eleven `TS-1` keys and each of the thirteen `TS-3` keys in turn with a wrong
literal, a wrong type, a wrong length and a wrong derived relation, and requires
the exact clause code for each. A companion fixture presents each field with a
correct type but an incorrect value, so **no field can pass on presence alone**.

---

## §2. Part B — the historical-order claim narrowed to the truth (`Y25-2a`)

### §2.1 The final-state / history boundary, stated as a truth table

```text
PROPERTY                                              PROVED BY G-11?
Stage A exists at its literal path and every field
  satisfies A1..A17                                          YES  FS-1(a)
Stage B and its signature exist; every field satisfies
  B1..B18; the signature verifies under Stage A's key        YES  FS-1(b)
all 57 members exist with the exact digests, and M4, M7
  and the record satisfy their full schemas                  YES  FS-1(c)
the recomputed id equals the record filename and Stage B's
  install_record_id                                          YES  FS-1(d)
M7 binds the M5 and M6 digests actually found                YES  FS-1(e)
exactly one content-addressed record exists                  YES  FS-1(f)
------------------------------------------------------------------------
the record was written AFTER Stage B existed                  NO  FS-2
M7 was written AFTER the matrix ran                           NO  FS-2
the id was computed AFTER M4 was written                      NO  FS-2
Stage A was created BEFORE variant resolution                 NO  FS-2
any ordering of creation events whatsoever                    NO  FS-2
that no earlier valid generation can be restored              NO  TR-2(b)
```

**In each `NO` row the final bytes are identical to the conforming case, so no
predicate over final bytes can separate them.** That is not a defect that better
wording fixes; it is what a filesystem-resident final-state verifier is.

### §2.2 What v2.6 withdraws, by name

```text
WITHDRAWN, each explicitly, in the governing bytes themselves:
  OR-11's sentence "a record installed before OR-10 completes is an ordering
    violation and is refused at CK-3 or CK-9"          → withdrawn at OR-11
  test 106(h)'s claim that the gate refuses each forbidden ordering
                                                       → rewritten, see §2.3
  packet v2.5 §3.2's ordering presentation as a gate property
                                                       → this §2 replaces it
  closure v2.5 §4.1's "ANY DEVIATION FROM S0→S7 IN THAT ORDER REFUSES"
                                                       → withdrawn; the v2.6
                                                         closure states the
                                                         truth table instead
  IR-4's "every member is attested by exactly one other object"  → §4
  row 115's "by the record and by nothing else"                  → §4
  TR-2's "every partial and every post-hoc substitution"         → §3
```

### §2.3 What replaces them — the honest procedural route

```text
FS-3  OR-1..OR-11 REMAINS THE SOLE CONFORMING CONSTRUCTION PROCEDURE AND IS A
      MANDATORY OPERATOR OBLIGATION. An operator who departs from it has
      produced a nonconforming installation whether or not any check can say
      so. FS-2 withdraws a false claim about DETECTION; it withdraws no
      obligation, weakens no step and permits no alternate route.

FS-4  A CONTEMPORANEOUSLY DISCOVERED VIOLATION FAILS CLOSED, with the new
      failure code PROCEDURE_VIOLATION_OBSERVED, routed to the ordinary
      process/control invalidity disposition, with NO PRODUCTION ENTRY. The
      observable cases are named: a hex-named record present while Stage B is
      absent; an M7 present with no recorded matrix run; a manifest written
      after the id was computed; a Stage A created after OR-4 in the driver's
      own recorded state; a driver step counter out of order.

FS-5  AN UNDISCOVERED VIOLATION IS INSIDE THE DECLARED RESIDUAL OF TR-2 AND IS
      NOT CLAIMED TO BE CAUGHT.

TEST 106(h) is rewritten accordingly: it drives the OR sequence and asserts
transitions and crash cuts WHILE THEY OCCUR, each refused with
PROCEDURE_VIOLATION_OBSERVED. It asserts nothing about the final state, and the
row FAILS a fixture that claims G-11 distinguishes byte-identical forbidden
history.
```

---

## §3. Part C — coherent rollback, stated exactly (`Y25-2b`)

```text
TR-2 NOW HAS TWO CLAUSES.

(a) FULL-CHAIN SUBSTITUTION AT OR BEFORE STAGE-A CREATION — carried forward
    from v1.2 unchanged in substance.

(b) COMPLETE COHERENT ROLLBACK OF A PREVIOUSLY VALID GENERATION, AT ANY LATER
    TIME — new, and stated because the Y line proved it. After a newer
    generation exists, an actor able to replace the whole repository control
    set can restore an earlier generation IN FULL: its Stage A, all of its
    members, its Stage B, its detached signature and its sole content-addressed
    record. On those restored bytes every check of FS-1 passes. NO NEW
    SIGNATURE AND NO PRIVATE KEY ARE NEEDED. THIS REACHES A RUNNABLE STATE AND
    IS NOT REFUSED.

WHAT IS ACTUALLY CLOSED — the exact proper-subset list, and this is the whole
of the claim:
    Stage A replaced while the manifest is not          A17
    the manifest replaced while Stage A is not          A17, CK-5, CK-8
    the signature replaced, removed or malformed        B11, B12
    Stage B replaced while the signature is not         B12
    the record replaced while the members are not       CK-6, CK-7, B15
    the members replaced while the record is not        CK-5, CK-8
    M7 replaced while M5 or M6 is not                   CK-11
    an old record presented against current members     CK-7, B15
    an old record retained beside the current one       CK-10
    a mixed-generation pair of governing files          CK-5, CK-8, B15
    an option mismatch between the two stages           A9, B14
    an unsigned install of any shape                    B1, B12 — no route
                                                        admits one

FORBIDDEN SENTENCES, in every governing file, packet and closure: that every
post-hoc substitution is closed; that complete coherent rollback is resisted,
detected or refused; that custody is immutable or external to this repository;
that any cryptographic freshness, monotonicity, recency or liveness property
holds.

THE ED25519 CHAIN AUTHENTICATES STAGE B RELATIVE TO THE STAGE-A KEY AND CLOSES
PARTIAL SUBSTITUTION UNDER THE PROCEDURAL ROOT. IT CREATES NO FRESHNESS. A
signature proves who signed a message, never when, and never that no earlier
signed message is still available.

THE THREAT-MODEL STRING STAGE A CARRIES IS EXTENDED to name both clauses, so
the author reads the rollback residual at the moment of signing.

THE FIXTURE. Test 106(i), labelled OUTSIDE_GUARANTEE_COHERENT_ROLLBACK, builds
generation N, then N+1, then restores N in full and ASSERTS THAT G-11 PASSES.
THAT IS THE EXPECTED RESULT; the row fails if the fixture asserts a refusal.
The case is classified outside the guarantee, not falsely refused.
```

---

## §4. Part D — the real integrity graph (`Y25-3`)

```text
IR-4 NOW STATES THE ACTUAL DIRECTED GRAPH, edge by edge:

  install record  --digest-->  each of the 57 members
  M4 manifest     --digest-->  the two M1 members
                  --digest-->  the five production roots
                  --digest-->  the three composite region digests and H_FILE
                  --path+digest-->  the three pre-selection inputs
                  --path+digest+key id-->  Stage A
  M7 attestation  --digest-->  M5
                  --digest-->  each of the two M6 modules
                  --digest-->  the M6 canonical bundle digest
                  --assertion-->  that the matrix ran and every row passed
  Stage B         --path+digest+key id-->  Stage A
                  --id+path+count-->  the record and the member set
                  --digest-->  the two M1 members
  detached sig    --Ed25519-->  the exact canonical Stage-B bytes
  Stage A         --key pin-->  the one key under which Stage B verifies

THESE ADDITIONAL EDGES ARE INTENTIONAL AND ARE NOT SELF-ATTESTATION. Redundant
inbound edges make a partial substitution fail in more than one place; they
never let an object vouch for itself.

WHAT REMAINS TRUE, AND IS THE ACTUAL PROPERTY: NO OBJECT ATTESTS ITSELF. The
record is not its own member and its id is not in its own preimage; no member
carries its own digest; Stage A carries no digest of itself; Stage B carries no
signature of itself; the manifest carries no digest of itself; the attestation
does not attest itself; the composite carries none of its own digests.

NO UNIQUENESS OF ATTESTER IS CLAIMED, AND NO RULE DEPENDS ON ONE. NO UNIQUENESS
OF EXTERNAL ATTESTER IS CLAIMED EITHER.

ROW 115 is rewritten to assert the redundant edges POSITIVELY: a build in which
M4 does not carry the M1 digests and the Stage-A binding, or in which M7 does
not carry the M5/M6 digests and the bundle digest, FAILS the row — and so does
a fixture asserting a unique attester or a unique external attester.
```

---

## §5. Part E — member accounting and the identity selection (`R5`)

### §5.1 The member set, mechanically updated only

```text
CLASS  v2.5  v2.6  WHAT CHANGED
M1        2     2  paths only: amendment v1.3, composite v1.6
M2       39    43  four rows added, exactly as v2.5 added four: the v1.2
                   amendment, composite v1.5, and the two v2.5 independent
                   confirmations. No row removed.
M3        7     7  unchanged, digests unchanged, still equal to §A0.1
M4        1     1  same literal path; schema completed, key set 17 → 20
M5        1     1  unchanged
M6        2     2  unchanged, rows 92..115 unchanged, 24 functions
M7        1     1  same literal path; schema completed
TOTAL    53    57

DISJOINTNESS REPROVED. Twenty-one unordered pairs, three groups, same argument
as v2.5 with 52 literal strings instead of 48. Union 57 = 2+43+7+1+1+2+1, so no
path is counted twice and none is unassigned. M2 ∩ M3 = ∅ by direct comparison
of a 43-string list with a 7-string list.

PROVENANCE REGION 51 rows = 43 M2 + 7 M3 + 1 non-enforced verifier baseline.
A verifier that derived M2 from the region would enumerate 50 instead of 43;
test 108 requires that fixture to FAIL with MEMBER_EXTRA.
```

### §5.2 The signed identity selection — recorded, not bound

```text
successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md
  7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f
  Kirill, 2026-08-04, token
  I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY.

IT IS RECORDED AT XS-1 AS CURRENT AUTHOR STATE AND AS NOTHING ELSE.

IT IS NOT A MEMBER OF M1..M7, AND THIS IS SAID EXPLICITLY IN THE GOVERNING
BYTES. Why: binding it into M1..M7 would make the watchdog install depend on a
selection whose own enabling token is unaccepted, and would import an unreviewed
prerequisite into a gate whose entire point is that its inputs are literal,
closed and reviewed.

IT DOES NOT ACCEPT P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1. That token's
own signature file records it as NOT ACCEPTED and requires separate review and
acceptance before Option A can become operative. Nothing in v2.6 accepts it,
makes it signable, or predicts it.

IT DOES NOT ENTER SCIENTIFIC EVIDENCE. It is a control-plane author-state fact:
no covariate, no endpoint, no qualification or comparison input, no Q/C fact, no
input to any acceptance predicate.

IT DOES NOT MAKE THIS PAIR OPERATIVE. Composite v1.6's blocking notice stands
unchanged on BOTH cells, and its status line is unchanged.

WHERE THE LATER COMBINED BINDING MUST ACCOUNT FOR IT — XS-1 states four
obligations on that binding, which is the reviewed specification that binds the
signed identity selection together with the signed watchdog option and resolves
the cell of composite §P1-13.2 row 2:
  a. record this signature's literal path and exact digest;
  b. record the separate review and acceptance of the bounded-weakening token,
     or refuse to proceed;
  c. state whether this signature becomes a member of that binding's own closed
     set and, if so, in which class and with what cardinality;
  d. re-derive the identity fields of the process-claim record, which this
     amendment neither selects nor repairs.
```

---

## §6. Part F — the recomputed accounting

### §6.1 The counting rule — unchanged, including the identical-restatement clause

The v2.4 counting rule and the v2.5 identical-restatement clause are carried
forward verbatim. A **governing locus** is one normative unit bearing its own
identifier inside one of the two governing specification files; document
metadata is not a locus; and a unit carried byte-identically in both files is
one locus counted once, in file 1.

### §6.2 The v2.6 count, derived

```text
FILE 1 — peer amendment v1.3, c3da2a7d…
  A  tagged normative rules                                           141
       DA 5 · WA 6 · TIMING 4 · QC 5 · FD 4 · F 8 · KW 3 · FB 5 · TO 5
       RF 3 · NS 4 · AK 7 · PUB 4 · H 4 · N 13
       IR 12 · MS 11 · TS 6 · OR 11 · CK 12 · FC 1 · TR 2 · FS 5 · XS 1
  B  acceptance-predicate conjuncts (§A5)                              10
  C  freeze-sequence steps (§A3.3)                                      6
  D  named entry routes (§A3.1)                                         2
  E  swap-only state-machine units (§A7.3: I1..I7, S1, S2, 3 states)   12
  --------------------------------------------------------------------
  FILE-1 GOVERNING LOCI                                               171

FILE 2 — P1 operative composite v1.6, 6283d081…
  F  normative behavioural repairs carried forward
       (R1..R22 plus invariant 60)                                     23
  G  new normative sections
       §P1-10.6, §P1-10.7, §P1-13.9, §P1-14.8                           4
  H  guard rules defined or renamed by this repair
       G-10 (redefined and reserved), G-11 (new), AD-1 (renamed)        3
  I  test rows 92..115                                                 24
  --------------------------------------------------------------------
  FILE-2 GOVERNING LOCI                                                54

  ====================================================================
  TOTAL GOVERNING LOCI                                                225
  GOVERNING SPECIFICATION FILES                                         2
  HISTORICAL LOCI WITH GOVERNING FORCE                                  0
  HISTORICAL BYTES EDITED                                               0
  INSTALL-RECORD MEMBERS                                               57
  MEMBER CLASSES                                                        7
  CLOSED FAILURE CODES                                                 25
  COMPOSITE PROVENANCE ROWS                                            51
  ====================================================================

DELTA FROM v2.5's 216: +9, all in file 1. MS 10 → 11 (created_utc), TR 2 → 2
(unchanged count, TR-2 extended in place), N 11 → 13, plus the new families
FS 5 and XS 1: +1 +2 +5 +1 = +9. File 2 is unchanged at 54: no test row was
added or removed and no guard identifier moved.
```

### §6.3 The four accountings kept separate

```text
1. GOVERNING-LOCUS COUNT — 225, in exactly two specification files. The only
   count with authority meaning.
2. PROVENANCE OCCURRENCE COUNT — unchanged in kind and governing nothing. THE
   V2.5 PAIR AND ITS TWO INDEPENDENT CONFIRMATIONS JOIN THE INVENTORY on
   acceptance of the v2.6 pair.
3. THE MEMBER COUNT — 57 — counts FILES pinned by the install record, not
   normative units.
4. EXTERNAL AUTHOR STATE — the signed identity selection — is none of the
   three. It is recorded at XS-1 with its digest, is in no class, is in no
   install record, and is counted nowhere.
```

---

## §7. Part G — everything the X line confirmed, preserved

| X-confirmed item | Where it lives in the v2.6 pair | Changed? |
|---|---|---|
| Cross-references resolve; no live `§P1-19` | §A9 audit note; composite contains `P1-19` **0** times | re-audited, still clean |
| Member set enumerable from `MS-1`..`MS-7` alone | `MS-1`..`MS-7`, `CK-4` | paths and counts only |
| 21/21 class pairs disjoint, union = cardinality sum | `MS-9` | reproved at 57 |
| All `M2`+`M3` digests recompute; provenance arithmetic holds | `MS-2`, `MS-3`, §P1-18 | 50 digests, 51 rows |
| `M4`/`M5`/`M6`/`M7` exact paths, encoding, bundle rule | `MS-4`..`MS-7` | **completed**, never loosened |
| Stage A token pairing, key/key id, pre-selection binding, exact threat bytes | `TS-1`, `TS-2` | pre-selection paths made literal; threat string extended |
| Stage B canonical bytes, pure Ed25519, detached encoding, single key | `TS-3`, `TS-4`, `TS-5` `B12` | **format byte-unchanged** |
| No self-attestation; Stage artifacts outside `M1`..`M7` | `IR-4`, `TS-6` | uniqueness wording removed only |
| `TR-2` states, does not close, the residual; no stronger claim survives | `TR-2` | **residual widened, never narrowed** |
| Accepted behaviour §A1–§A8 byte-identical in substance | amendment §A1–§A8 | unchanged |
| Option symmetry, `W-B` recommended, neither selected | §8 below; `N-1`, `N-2` | unchanged |
| `killer == WATCHDOG` unreachable; one freeze writer; PCS journal invisible | §A5 conjunct 8, `KW-1`..`KW-3`, `WA-2`, composite §P1-10.7 | unchanged |
| Zero historical bytes moved; `T = NOT_ACTIVATED`; claim `OPEN` | `N-9`, §A12, §P1-16 | unchanged |

**The two-stage Ed25519 format is byte-unchanged.** `TS-4` — the signed message,
the pure-Ed25519 rule, the 128-hex detached encoding — is carried forward
verbatim. What changed around it is that `TS-5` now checks every field rather
than a selected few, and that `TR-2` no longer claims more than the signature
delivers.

---

## §8. Recommendation, tokens and invariants — unchanged

> **W-B remains recommended**, on the same five criteria and no others:
> signed-authority fidelity, constructibility, mechanical testability,
> liveness, and blast radius.

```text
SELECTION, exactly one, NEITHER SELECTED:
  I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
  I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
PER-OPTION AMENDMENT:
  P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1        with W-A only
  P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1          with W-B only
COMMON AMENDMENTS, required under EITHER selection:
  P1_FREEZE_ABSENT_FALLBACK_NULLABLE_IDENTITY_V1
  P1_PCS_FREEZE_CLASSIFIER_V1
  P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1
  P1_FREEZE_PUBLICATION_L6_L9_V1
ACCEPTANCE, not an author choice, VERSION-BUMPED ONLY:
  I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_3

NOTHING IN v2.6 IS ASYMMETRIC BETWEEN THE OPTIONS. Every schema field, every
verification clause, every order step, every failure code and every fixture is
option-independent. The variant markers remain balanced 10/10 in the body
region and 13/13 whole-file.

NO SELECTION TOKEN IS ADDED, REMOVED OR RENAMED. NO NEW AUTHOR CELL IS OPENED.
THE AUTHOR SELECTS NOTHING, MINTS NO TOKEN, GENERATES NO KEY AND PREDICTS NO
OUTCOME.
```

```text
N-1  THE BLOCKER REMAINS PROVED, on the same four mechanisms.
N-2  THE PCS NEVER RETAINS THE WATCHDOG UPDATE-PIPE WRITE END, either option.
N-3  THE PCS REMAINS THE SOLE CALLER of fork, posix_spawn, kill, killpg and
     every wait-family primitive. S-12 retained.
N-4  W-B MAY REMAIN RECOMMENDED and does — but NO OPTION IS SELECTED.
N-5  THE WATCHDOG PAIR NEITHER SELECTS NOR REPAIRS THE IDENTITY FIELDS. The
     identity cell was selected by Kirill separately; XS-1 records that and
     binds nothing.
N-6  PCS JOURNAL STATE REMAINS SCIENTIFICALLY INVISIBLE.
N-7  NO NEW AUTHOR CELL.
N-8  THE SIGNED SELECTION TOKENS ARE NOT REVOKED, RE-RUN OR REOPENED, and
     P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1 IS NOT ACCEPTED HERE.
N-9  THE HISTORICAL CHAIN IS NOT EDITED. Zero historical bytes moved.
N-10 THE PEER SCHEMAS ARE NOT REOPENED. The manifest, attestation and two
     authorization schemas are CONTROL-PLANE artifact schemas only.
N-11 NO KEY, ENTROPY, ARTIFACT, SIGNATURE, MANIFEST, ATTESTATION OR INSTALL
     RECORD IS GENERATED HERE.
N-12 NO TEMPORAL, FRESHNESS OR ROLLBACK-RESISTANCE PROPERTY IS CLAIMED.
N-13 T = NOT_ACTIVATED; the programme claim is OPEN.
```

---

## §9. Independence

```text
The v2.5 X review was performed by Opus 4.8 in a fresh session and is genuinely
independent; the v2.5 Y review by Sol likewise. BOTH FINDING SETS THAT v2.6
ACTS ON WERE INDEPENDENTLY PRODUCED.

v2.6 WAS AUTHORED BY THE SAME OPUS 5 SPECIFICATION-AUTHOR INSTANCE THAT
AUTHORED v2.3, v2.4 AND v2.5. It cannot be treated as having survived a review
pass of its own. The next X review must be performed by Fable 5 or Opus 4.8, by
an agent that did not author v2.3 through v2.6; the next Y review by Sol,
bounded. Every author closure, including this round's, is an untrusted
self-assessment that is normative for nothing.
```

---

## §10. Negative space

This correction creates nothing executable and authorizes no selection, X/Y
verdict, amendment acceptance, identity-token acceptance, identity bounded
weakening, implementation, commit, verifier or manifest edit, key generation,
entropy draw, selection artifact, authorization artifact, detached signature,
attestation, install record, process, socket, pipe, fork, exec, signal, wait or
`prctl` operation, supervisor, PCS, controller, worker or watchdog, capability,
world, learner, candidate, trajectory, capacity artifact, custody disposition,
result manifest, spend, datum, outcome, Proof or claim movement. No freeze was
executed, requested, journalled or witnessed. No `/proc` was read against any
live process. No clock was sampled for any contract purpose. It predicts no
qualification and no comparison outcome. It selects neither option and accepts
no token. **It modified no existing file.** `T` remains `NOT_ACTIVATED`; the
programme claim remains `OPEN`.
