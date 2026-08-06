# Officina P1 W-B inert scaffold handoff v5 (draft)

**Author:** Claude Code Opus 5, **handoff author only**. This document is a
**scope contract for a future implementer**. It is not an implementation
authorization.

**NOTHING IN THIS DOCUMENT AUTHORIZES CODE TO BE WRITTEN.** Writing code under it
requires (i) acceptance of
`I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_11` and
(ii) a separate **inactive-scaffold authorization**. Neither exists. `T` is
`NOT_ACTIVATED`; the programme claim is `OPEN`.

**v5 REPLACES v4 WHOLLY** and is re-issued against the v1.11 / v1.14 governing
bytes. **THE ALLOWED SURFACE IS NOT WIDENED BY ONE LINE.** Exactly four things
changed, and every one of them is a value the implementer must not invent for
themselves:

```text
1. THE TRANSFORM'S INPUT MOVED, SO EVERY PINNED FIGURE MOVED. Binding v5 still
   pins ELEVEN spans, one deterministic splice order and a full resolved-output
   length and SHA-256 — but against composite v1.14. EVERY SOURCE DIGEST, EVERY
   LINE NUMBER, THE BYTE ARITHMETIC AND THE OUTPUT DIGEST DIFFER FROM v4's. An
   oracle carrying v4's constants FAILS CLOSED at binding §2.2.5 step 3 against
   the v1.14 bytes, which is the correct direction and is not a licence to
   "update" any figure by hand.
2. THE ACCOUNTING CONSTANTS MOVED. M2 is 75, MS-8 and TS-3 member_count are 89,
   the composite provenance region is 83 rows, and the recorded M2+M3 digest
   count is 82. D-6's sum and T-14's negative enumerations move with them.
3. THE PRIMITIVE-BINDING TABLE GAINED TWO NAMES. §P1-3.4 now binds _getsid and
   _getpgid from os. THE SCAFFOLD MAY HOLD THE BINDING LIST AS DATA AND MUST NOT
   CALL EITHER NAME: §H3's no-syscall rule, §H10's fences and §H11's ungranted
   runtime authorization are unchanged, and BINDING A NAME IN A SPECIFICATION IS
   NOT PERMISSION TO RUN IT.
4. THE CANONICAL PARSER DATA MAY STILL BE HELD AS CONSTANTS, and V18's published
   vector now carries an exact 145-byte buffer and the rule L0 rather than L1.
   THE PARSER ITSELF STILL MAY NOT BE WRITTEN, and §H3 D-8 and §H10 G-A say so
   in terms.
```

---

## §H-0. THE HONEST TITLE OF THIS DOCUMENT — read this before §H1

```text
WHAT THIS DOCUMENT ACTUALLY SCOPES:
  INERT ORACLE AND DECLARATIVE SCAFFOLDING ONLY.
    a pure in-memory transformation/validation oracle over byte copies, and
    a pure declarative contract surface — enums, frozen dataclasses, literal
    tables, error-code names, key sets — with NO I/O, NO SYSCALL, NO CLOCK, NO
    DESCRIPTOR, NO PROCESS AND NO NETWORK,
    plus DUMMY TESTS over those two.

WHAT THIS DOCUMENT DOES NOT SCOPE, AND DOES NOT CLAIM TO:
  THE RUNTIME W-B EOF ROUTE.        NOT IMPLEMENTED, NOT IMPLEMENTABLE HERE.
  THE PCS FREEZE CLASSIFIER,        NOT IMPLEMENTED, NOT IMPLEMENTABLE HERE.
    including KG-1, KG-2 with its P-1..P-12 population rules, KV-1..KV-6, and
    SC-1..SC-10 including all six global phases, which composite v1.14
    §P1-10.7 now defines IN FULL AND EXECUTABLY. A DEFINITION IS NOT AN
    AUTHORIZATION, AND AN EXECUTABLE DEFINITION IS STILL NOT AN AUTHORIZATION.
  THE CANONICAL PARSER ITSELF.      NOT IMPLEMENTED, NOT IMPLEMENTABLE HERE.
    §P1-10.3's STAT_READ, STAT_PARSE L0..L5 and KG_GROUP_ADMISSIBLE are a
    RUNTIME OBSERVER of a live /proc buffer. THEIR DATA MAY BE HELD AS
    CONSTANTS (§H3 D-8); THEIR CODE MAY NOT BE WRITTEN (§H10 G-A).
  THE DESCRIPTOR TOPOLOGY.          NOT IMPLEMENTED, NOT IMPLEMENTABLE HERE.
  ANY PROCESS OPERATION.            NOT IMPLEMENTED, NOT IMPLEMENTABLE HERE.
  ANY /proc READ AGAINST A LIVE PROCESS, OR AGAINST ANYTHING ELSE.
                                    NOT IMPLEMENTED, NOT IMPLEMENTABLE HERE.
  THE SUPERVISOR FREEZE ROUTES.     NOT IMPLEMENTED, NOT IMPLEMENTABLE HERE.
  THE M5 VERIFIER, THE M6 MODULES, G-10, G-11 OR CK-1..CK-15.
                                    NOT IMPLEMENTED. OR-5 AND OR-7 OWN THEM.

§H11 states, item by item, what separate authorization each of those requires.
```

Read together with
`successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V4_DRAFT.md`. Where the two
differ, **the binding governs**; where the binding and a governing clause of the
v1.11/v1.14 pair differ, **the governing clause governs and both drafts are the
defect.**

---

## §H1. Standing rules for the implementer

```text
R-1  IMPLEMENT FROM GOVERNING BYTES ONLY. The only documents opened for
     behaviour are
       successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_11_DRAFT.md
         5f2c74ff371f618039de705f21464454684da122f91e06c251e147bfc61d26be
       successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_13.md
         11c8963ac3cbd4c72a90b0a1f0fdc0fe3bfb35be84a974c3a2a953ec699bbdee
     Every earlier amendment (v1..v1.9), every earlier composite (v1..v1.12),
     every author choice packet including v2.14, and every review file are
     HISTORICAL EVIDENCE ONLY and are NOT opened to determine behaviour
     (DA-1, DA-2, DA-4, IR-12).

R-2  NO DESIGN DISCRETION. Where this document is not exact enough to implement
     a function, STOP AND ASK. Do not infer, do not reconstruct from a
     superseded document, and do not fill a gap with a reasonable default.
     THE WHOLE TRANSFORMATION NOW SATISFIES THIS RULE RATHER THAN MERELY
     INVOKING IT: binding §2.2.1 pins eleven spans by sentinel and by source
     digest, §2.2.2 through §2.2.4 pin every replacement byte, §2.2.5 pins the
     splice order, and §2.2.6 pins the full resolved-output length and digest.
     THE IMPLEMENTER CHOOSES NO BOUNDARY, NO SENTENCE, NO PHRASE AND NO SPACE.

R-3  W-B ONLY. Never implement, stub, flag, comment or leave dead a W-A
     capability. No freeze-request socket, no slot-6 endpoint, no
     t-wd-freeze.v1 frame, no bounded service window, no accept or reject of a
     watchdog request. THE W-A TOKENS THEMSELVES REMAIN IN TS-1's CLOSED
     VALIDATION VOCABULARY and in the CK-14 fixture, and a fixture that deletes
     them is WRONG — see binding §2.5.

R-4  INERT MEANS INERT. Nothing written under this handoff may be reachable from
     a production entry point, an install path or an activation path, and
     nothing written under it may perform I/O, a syscall, a clock read, a
     descriptor operation or a process operation.

R-5  NO PROCESS-CONTROL SMOKE ANYWHERE. Not in the shared runtime tree, not in a
     temporary root, not in a container, not under a marker. There is no
     process-control smoke test under this handoff at all.

R-6  THIS IS NOT OR-4. No file at either MS-1 literal path is edited, ever,
     under this handoff. The oracle rewrites copies in memory and returns them.
     THE PINNED REPLACEMENT BYTES ARE CONSTANTS IN THE ORACLE AND ARE NEVER
     WRITTEN TO A GOVERNING PATH. THE PINNED FULL RESOLVED OUTPUT IS AN
     ASSERTION TARGET AND IS NEVER WRITTEN TO ANY PATH, INCLUDING A TEMPORARY
     ONE.

R-7  A GOVERNING DEFINITION IS NOT AN IMPLEMENTATION AUTHORIZATION. Composite
     v1.14 §P1-10.3 defines the canonical parser and §P1-10.7 defines the six
     phases and the per-group verification IN FULL AND EXECUTABLY. THAT DOES NOT
     MAKE EITHER WRITEABLE HERE. See §H10 and §H11.
```

---

## §H2. Paths

### §H2.1 Allowed paths — the complete list, and it is small

Nothing outside this list may be created or edited.

```text
CODE  — two modules, both PURE
  src/philosophia/officina/p1_wb_oracle.py
      the §H4 in-memory transformation and validation oracle. TEST-ONLY. It is
      not M5, is not a production root, and is imported by nothing under
      scripts/ and by nothing outside tests/.
  src/philosophia/officina/p1_wb_contract.py
      the §H5 pure declarative surface — enums, frozen dataclasses, error-code
      NAMES, literal key sets, literal count constants, and the §H3 D-8
      canonical parser DATA. NO I/O, NO SYSCALL, NO CLOCK, NO DESCRIPTOR, NO
      SOCKET, NO SUBPROCESS, NO THREAD.

TESTS  — dummy tests over the two modules above and nothing else
  tests/test_officina_p1_wb_oracle.py
  tests/test_officina_p1_wb_contract.py

FIXTURES
  tests/fixtures/p1_wb/            deterministic, committed, test-only

SCRATCH
  a per-test temporary root created by tempfile.mkdtemp and removed by the test

NOTHING ELSE. In particular: no new file under scripts/, none under successor/,
none under successor/officina/, none under any INSTALL directory, and no test
module named for a runtime route.

STILL EXCLUDED, AND THE EXCLUSION IS THE POINT:
  tests/test_officina_p1_wb_classifier_ordering.py       — it would have no
      implementation under test. The classifier is not implementable here, and
      the six global phases do not change that: they are runtime rules over a
      live handle table and live /proc reads.
  tests/test_officina_p1_wb_stat_parser.py               — there is no parser
      to test. D-8 holds the parser's DATA; §H10 G-A forbids the parser.
  tests/test_officina_p1_wb_negative_surface.py          — a negative surface
      test over a surface that does not exist is not a test.
  tests/test_officina_p1_wb_disposable_integration.py    — there is no
      integration to run. R-5 forbids process-control smoke outright.

IMPORT INVARIANT, STATED POSITIVELY AND TESTED. Both modules live inside
src/philosophia/officina/, whose __init__.py is MS-13-digest-bound. Adding a
sibling module changes no bound byte, and MS-11's 89-row closure is unperturbed
BECAUSE NO PRODUCTION ROOT IMPORTS THEM. That is safe only while it stays true,
so the suite MUST carry a test asserting: these two modules are imported by
nothing outside tests/, and neither imports any production root.
```

### §H2.2 Frozen paths — must not be edited, created or deleted

```text
THE GOVERNING PAIR — read-only, opened for behaviour, never written
  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_11_DRAFT.md
  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_13.md

THE FIVE P1 PRODUCTION ROOTS OF §P1-3.1 — frozen under this handoff
  scripts/officina_activate_t.py                       exists, DO NOT EDIT
  scripts/verify_officina_active.py                    exists, DO NOT EDIT
  src/philosophia/officina/generic_harness.py          exists UNTRACKED, DO NOT
                                                       EDIT, DO NOT ADOPT — §H9
  scripts/officina_process_control_bootstrap.py        ABSENT — DO NOT CREATE
  scripts/officina_role_bootstrap.py                   ABSENT — DO NOT CREATE

THE HANDOFF-STEP ARTEFACT PATHS — none may be created
  src/philosophia/officina/verification.py             MS-5. EXISTS as the
      non-enforced pre-install baseline. It is NOT M5 and DO NOT EDIT IT.
  tests/test_officina_p1_freeze_authority.py           MS-6 module 1, ABSENT
  tests/test_officina_p1_install_integrity.py          MS-6 module 2, ABSENT
  successor/officina/authorization/P1_WATCHDOG_FREEZE_SELECTION_V1.json
                                                       TS-1 Stage A, ABSENT
  successor/officina/authorization/P1_WATCHDOG_AUTHORITY_INSTALL_AUTHORIZATION_V1.json
  successor/officina/authorization/P1_WATCHDOG_AUTHORITY_INSTALL_AUTHORIZATION_V1.sig
                                                       TS-3 Stage B, ABSENT
  successor/officina/runtime_control/PRODUCTION_CALL_GRAPH.json   M4, ABSENT
  successor/officina/runtime_control/INSTALL/…         M7, install record, ABSENT

  THE THREE MS-5/MS-6 PATHS ARE THE MOST LIKELY MISTAKE. Rows 92..115 belong to
  modules that OR-5 installs and OR-7 runs. Creating either now would place a
  file at a MEMBER path before OR-3 exists, and CK-7's enumeration would then
  find a member whose digest no manifest records.

NO test_p1_row_NNN_ FUNCTION MAY BE CREATED, ANYWHERE, UNDER ANY NAME, IN ANY
MODULE. MS-6's membership rule reserves that exact name form for rows 92..115 in
exactly two modules that do not exist. Zero such functions exist in the
repository today and that must remain true until OR-5 and OR-7.

NEITHER MS-6 MODULE MAY BE CREATED BEFORE OR-5.

THE FOUR MS-13 PROJECT MODULES — digest-bound; a byte change breaks the manifest
  they are named literally at MS-13 and MUST NOT be edited under this handoff.

THE GOVERNING PROVENANCE AND HISTORY — every M2 and M3 path, every prior review,
  every signature. NOT EDITED, NOT STAGED, NOT REVERTED, NOT DELETED. THAT NOW
  INCLUDES THE FOUR PATHS THAT BECAME M2 ROWS THIS GENERATION: amendment v1.9,
  composite v1.12, and the two v2.12 final reviews.

UNRELATED DIRTY AND UNTRACKED WORK — src/philosophia/officina/accounting.py, its
  test module, the reviews/ files, essay/OUTLINE.md, and the untracked
  generic_harness.py and its test module. NOT TOUCHED BY ANYTHING HERE, AND NOT
  EVIDENCE FOR ANYTHING HERE.
```

---

## §H3. What the scaffold may model — declaratively, and only declaratively

Nothing below is a runtime route. Each item is a **statement of the contract as
data**, checkable by a dummy test, with no execution of the thing it describes.

```text
D-1  THE W-B DESCRIPTOR TOPOLOGY AS A LITERAL TABLE.
     The watchdog role's expected /proc/self/fd set is the literal frozen set
     {0,1,2} | {3,4,5,7,8,9,10}, slot 6 absent. THIS IS A CONSTANT IN
     p1_wb_contract.py. NO DESCRIPTOR IS OPENED, DUPED, CLOSED OR INSPECTED.

D-2  THE W-B NEGATIVE SURFACE AS A LITERAL PREDICATE LIST.
     "writes nothing, freezes nothing, signals nothing, sends nothing, exits"
     as an enumerated frozen tuple of contract statements. NO EOF IS OBSERVED
     AND NO EXIT IS PERFORMED.

D-3  THE SC-5 RESULT-TOKEN SET AS A CLOSED ENUM, AND THE TERMINALS AND
     QUALIFIERS AS SEPARATE CLOSED SETS.
     Exactly seven token names: KV_OK, KV_STALE_HANDLE, KV_ROLE_OR_STATE_REFUSED,
     KV_OBSERVATION_UNAVAILABLE, KV_IDENTITY_CONTRADICTED, KV_GROUP_MISMATCH,
     KV_FORBIDDEN_TARGET. Exactly three terminal names:
     PCS_FREEZE_CLASSIFIER_STRUCTURAL_VIOLATION,
     PCS_FREEZE_CLASSIFIER_STALE_GENERATION,
     PCS_FREEZE_CLASSIFIER_FORBIDDEN_TARGET. Exactly two qualifier names:
     FREEZE_NOT_ATTEMPTED, FREEZE_ABANDONED. A dummy test asserts the three
     cardinalities and asserts that NO terminal and NO qualifier is a member of
     the seven-token enum and that none is a member of FC-1's twenty-five.
     NO CLASSIFIER RUNS AND NO PREDICATE IS EVALUATED AGAINST A LIVE PROCESS.

D-4  THE SC-7 TOTALITY TABLE AS PURE DATA.
     The role x state x ownership x pgid product, 3 x 4 x 3 x 2 = 72, with the
     ordered rule list of SC-7 as a pure function over SYNTHETIC TUPLES. A dummy
     test asserts the function is total over all 72 synthetic tuples, that the
     partition sizes are 24 + 32 + 4 + 6 + 6 = 72, and that no tuple has two
     answers. THE INPUTS ARE INVENTED TUPLES. THERE IS NO HANDLE TABLE, NO
     /proc READ, NO PID AND NO SIGNAL.
     THIS IS A TABLE-TOTALITY TEST, NOT A CLASSIFIER. It proves that SC-7's
     partition is total as stated; it proves NOTHING about any running system,
     AND IN PARTICULAR IT PROVES NOTHING ABOUT ANY OF THE SIX PHASES, WHOSE
     CONTENT IS A LIVE HANDLE TABLE AND LIVE /proc OBSERVATIONS.

D-5  THE FC-1 CLOSED FAILURE-CODE SET AS A LITERAL FROZEN SET of 25 names, and
     the CK-1..CK-15 ordering as a literal ordered tuple of 15 names. A dummy
     test asserts the cardinalities and the order. NO CHECK IS EXECUTED AND NO
     VERIFIER IS IMPLEMENTED — G-10, G-11 and CK-1..CK-15 belong to OR-5's M5
     verifier and MUST NOT be written here.

D-6  THE MEMBER-CLASS ACCOUNTING AS LITERAL CONSTANTS.
     M1 2, M2 75, M3 7, M4 1, M5 1, M6 2, M7 1, total 89; TS-3 member_count 89;
     composite provenance region 83 rows; recorded M2+M3 digests 82; 7 member
     classes. A dummy test asserts
     the sum and the NEGATIVE cases of binding PR-4: an enumeration of 63, 69,
     73, 77, 81 or 89 FAILS. NO MEMBER IS ENUMERATED FROM DISK.

D-7  THE SCHEMA KEY SETS AS LITERAL FROZEN SETS — TS-1's eleven keys, TS-3's
     thirteen, IR-3's five, MS-4's twenty-one, MS-7's ten. A dummy test asserts
     each cardinality and each exact key set. NO ARTIFACT IS PARSED, WRITTEN OR
     VALIDATED, and no instance of any of them is constructed.

D-8  THE CANONICAL PARSER DATA — DATA ONLY, AND THE BOUNDARY IS EXPLICIT.
     The following are CONSTANTS in p1_wb_contract.py:
       the layout identifier string LINUX_PROC_PID_STAT_52_FIELD_V1, the
         whole-record field count 52 and the suffix field count 50, as a
         CLOSED one-member accepted-layout set;
       the four accepted suffix field positions 1, 2, 3 and 20 with the names
         state, ppid, pgrp and start_identity;
       the closed nine-byte state set 0x52 0x53 0x44 0x54 0x74 0x58 0x5A 0x50
         0x49 — "R" "S" "D" "T" "t" "X" "Z" "P" "I";
       the two integer-grammar bounds as data: UDEC31 length 1..10 with value
         bound 2147483647, UDEC64 length 1..20 with value bound
         18446744073709551615, both with leading zeros REFUSED;
       the group-admissibility threshold pgrp >= 1;
       the SIX reader outcome names ABSENT, PRESENT_VALID, UNREADABLE,
         UNPARSABLE, ERROR, PRIMITIVE_FAULT;
       THE PUBLISHED VECTOR TABLE V0..V39 as (identifier, description,
         expected STAT_PARSE result, expected STAT_OBSERVE result, expected
         PGRP_OBSERVE result) tuples, with the SHA-256 of each positive vector.
     A dummy test asserts the cardinalities, asserts that "W", "x" and "K" are
     NOT members of the state set, asserts that the accepted-layout set has
     exactly one member, and asserts that the vector table names exactly one
     expected result per consumer per vector and no vector twice.
     THIS IS A CONSTANT TABLE ONLY. NO /proc PATH IS OPENED, NO stat BUFFER IS
     READ OR CONSTRUCTED, NO PID IS NAMED, AND STAT_PARSE IS NOT IMPLEMENTED.
     A SCAFFOLD THAT IMPLEMENTS L0..L5, STAT_READ, KG_GROUP_ADMISSIBLE OR ANY
     TOKENISER OVER ANY REAL OR SYNTHETIC STAT BUFFER HAS LEFT THIS HANDOFF's
     SCOPE — that parser is part of the classifier, which §H10 G-A forbids.
     THE VECTOR BYTES THEMSELVES ARE NOT RECONSTRUCTED HERE EITHER: the table
     carries the vectors' IDENTIFIERS, DESCRIPTIONS, EXPECTED RESULTS AND
     DIGESTS, not their byte strings, because a byte string exists only to be
     parsed and there is nothing here permitted to parse it.
```

---

## §H4. The transformation oracle

The one thing that may actually be built, and it is inert.

```text
SIGNATURE SURFACE, NORMATIVE FOR THIS HANDOFF.

resolve_wb(amendment_bytes: bytes, composite_bytes: bytes) -> bytes
    pure; returns a candidate resolved composite byte string; writes nothing.
    Its work is EXACTLY binding §2.2.5's RESOLVE over the ELEVEN spans of
    §2.2.1, whose sentinels, source digests, replacement bytes and replacement
    digests are all literals, and it asserts the full-output digest of §2.2.6
    before returning.

check_po(resolved: bytes, guarddata_digest: str) -> tuple[PoResult, ...]
    pure; evaluates binding §2.4 PO-0..PO-10 and returns one result per check,
    each carrying the check name, a pass/fail boolean and the failing locus.
    PO-0 IS THE PRIMARY CHECK AND ITS FAILURE IS FATAL TO THE CANDIDATE
    WHATEVER ELSE PASSES.

census(resolved: bytes) -> OccurrenceCensus
    pure; evaluates binding §2.5's class R and class F rows and returns the
    observed count for each against its expected count

detect_open_cell(resolved_minus_guarddata: bytes) -> tuple[Finding, ...]
    pure; binding §2.6 detectors D1 and D2 over the LITERAL ARRAYS of §2.6.2 and
    §2.6.3, held IN THE ORACLE, never in the composite, under binding §2.6.1's
    PN normalization. The arrays are constants; the implementer derives nothing.
    THE ORACLE MUST NOT REPORT A ZERO RESULT FROM THESE DETECTORS AS PROOF THAT
    NO W-A CAPABILITY SURVIVES. Binding §2.6.0 withdraws that claim, and the
    oracle's own report must carry the narrowed wording.

CONSTANTS THE ORACLE MUST CARRY VERBATIM, AND MUST ASSERT THE DIGEST OF
  the eleven span source digests   binding §2.2.1, one per span
  the eleven replacement blocks    binding §2.2.2, §2.2.3 and §2.2.4, with the
                                   eleven replacement digests
  THE FULL RESOLVED OUTPUT         624840 bytes, digest
                                   9904ff3bf73f90329df7ac06fac5dbf4b211713964f610541761018c9bacb5c5
  the resolved H_BODY              f57002460cc94d5f1c220193459ec662f713e0f5e3a1564f76f1732d4e1830df
  the resolved H_NORMATIVE         3bbd378dec0d189d1b4374970a01272b73634c539eb2182773e46ea4cec6811f
  H_GUARDDATA, unchanged           faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
  the D1 array                     11 literals, canonical serialization 926
                                   bytes, digest
                                   d5b375c518c935d3a6935a1932bf6bfa237cb9c99c7b81913f4e1433142b6c1e
  the D2 array                     13 literals, canonical serialization 1044
                                   bytes, digest
                                   4e2120857dd67124095e5f5479d69cbf7ba703605abb3448a2fe414b3ff8a15c

INPUT DISCIPLINE. Byte copies read from the two literal governing paths in
read-only mode and held in memory. The oracle opens neither for behaviour: it
hashes and rewrites bytes and interprets no rule.

OUTPUT DISCIPLINE. Every reported digest is emitted with the literal tag
  test-only/non-installed/non-authoritative
adjacent to the value, in the same string, so that no transcript, log line or
test output can be quoted as an install digest.

DETERMINISM. Same inputs, same output bytes, on every run, on any host. No
clock, no entropy, no environment variable, no locale dependence, no filesystem
state beyond the two read-only reads.

FORBIDDEN, ABSOLUTELY: writing the resolved bytes to ANY path, including a
temporary one; writing any governing or runtime path; any key or entropy; any
Stage A, Stage B, signature, manifest, attestation, member list or install
record; any process, socket, pipe, fork, exec, signal, wait, prctl or /proc
operation; and any export that a writer of a governing path could accept.
```

---

## §H5. The declarative contract surface

`p1_wb_contract.py` carries **only** the `§H3` `D-1`..`D-8` data. It is pure:
no import of `os`, `subprocess`, `socket`, `signal`, `threading`, `time`,
`fcntl` or any I/O module; no module-scope side effect other than constant
construction; no clock; no randomness.

**It defines no behaviour.** It is a place to put the literals so that a dummy
test can assert them, and so that a later authorized runtime implementation has
a reviewed source for them. **It is not that implementation and does not become
one.**

---

## §H6. Identity — the exclusion, restated where the implementer will look

```text
THE IDENTITY-OBSERVATION SURFACE IS OUT OF SCOPE ENTIRELY.
NO CODE, NO DISABLED CODE, NO GATED CODE, NO DUMMY TEST, NO ENUM VALUE, NO
SCHEMA KEY, NO CONSTANT, NO COMMENT DESCRIBING A FUTURE ONE.

THE MECHANICAL REASON: attested_pid and attested_pgid occur ZERO times in
composite v1.14 and ZERO times in amendment v1.11. There is no schema, key,
type, carrier, consumer or destination to conform to. Code written now could
only be invented, and composite Cell 1 says in its own words that the document
"chooses neither and invents no value."

THE NEW R1 CONTENT DOES NOT OPEN A CRACK IN THIS. STAT_PARSE's start_identity,
ppid, state and pgrp, and KG-2's recorded group, are PROCESS-CONTROL
observations inside the PCS's own in-memory handle table. They are NOT the
attested_pid / attested_pgid peer-record fields of §P1-13.2 row 2, they have no
schema key, and they reach no durable object. A scaffold that introduces an
attested_pid or attested_pgid constant, key, field or comment ON THE STRENGTH OF
STAT_PARSE, KG-1 OR KG-2 HAS LEFT SCOPE.

XS-1 REMAINS BLOCKED ON AN UNACCEPTED WEAKENING. THIS HANDOFF IS NOT THE LATER
COMBINED BINDING OF XS-1. It does not resolve §P1-13.2 row 2, does not accept
P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1, does not decide membership for the
identity signature, and does not re-derive any identity field. The combined
binding remains BLOCKED_PENDING_IDENTITY_WEAKENING_REVIEW.

IF SUCH A SURFACE IS EVER ADDED WITHOUT A SEPARATE ACCEPTED TOKEN, the active
verifier must REFUSE before any production action. That obligation belongs to
the M5 verifier of OR-5 and is NOT implemented here.
```

---

## §H7. Dummy tests

### §H7.1 Isolation rules — absolute

```text
I-1  NO PROCESS OPERATION OF ANY KIND. No fork, exec, posix_spawn, subprocess,
     signal, kill, killpg, wait, prctl, setsid, socket, socketpair, pipe or
     descriptor manipulation, in any test, under any marker, in any container.
I-2  NO /proc READ AGAINST ANY LIVE PROCESS, AND NO /proc PATH OPENED AT ALL.
     D-4's inputs are synthetic tuples and D-8 is a constant table.
I-3  NO PRODUCTION ARTIFACT NAME. No fixture file may be named for, or placed
     at, any MS-1..MS-7, TS-1 or TS-3 path, or any name a reader could mistake
     for an installed object.
I-4  NO KEY-GENERATION PRIMITIVE ANYWHERE IN THE SUITE. Not Ed25519, not any
     other algorithm, not a seed, not a CSPRNG draw for a key-shaped value. This
     is absolute and has no marker-gated exception.
I-5  NO WRITE OUTSIDE A PER-TEST TEMPORARY ROOT. Created by tempfile.mkdtemp,
     removed by the test. THE RESOLVED BYTES ARE NEVER WRITTEN, EVEN THERE.
I-6  NO CLOCK IS SAMPLED FOR ANY CONTRACT PURPOSE.
I-7  NO SHARED RUNTIME TREE IS TOUCHED, created, read or written.
```

### §H7.2 What the dummy tests assert

```text
T-1  the oracle is deterministic: two runs over the same inputs return identical
     bytes
T-2  PO-0..PO-10 each return a result, and the oracle's own negative fixtures —
     a candidate with a surviving body marker, one with a surviving preamble
     marker, one with a mutated guard-data region, one with a deleted TS-1
     literal, one with a surviving open-cell sentence, one with a surviving W-A
     grant — each FAIL the expected check and no other
T-3  binding §2.5's class R rows are each present at their expected count in a
     correct candidate, and DELETING ANY OF THEM FAILS D3
T-4  binding §2.5's class F rows are each absent at count zero in a correct
     candidate, and the W-A option token occurs THREE times and the W-A
     amendment token TWICE — the corrected §2.5 arithmetic, not v3's
T-5  THE COMPLETE SPLICE IS BYTE-EXACT: each of the eleven extracted source
     spans hashes to its pinned source digest, each replacement constant hashes
     to its pinned replacement digest, the spans are verified pairwise
     non-overlapping, the output is byte-identical across two runs and across
     two independent implementations of §2.2.5, THE FULL OUTPUT IS 624840 BYTES
     HASHING TO 9904ff3b…b5c5, and a source file whose span digest differs
     FAILS CLOSED rather than being spliced
T-6  THE D1 ARRAY IS COMPLETE AND EXACT: exactly 11 literals in the stated
     order, canonical serialization 926 bytes hashing to d5b375c5…6c1e, every
     literal occurs in PN of the pre-resolution Cell-2 span, and zero literals
     occur in PN of the S1 replacement bytes
T-7  THE D2 ARRAY IS COMPLETE AND EXACT: exactly 13 literals in the stated
     order, canonical serialization 1044 bytes hashing to 4e212085…a15c, every
     literal occurs in PN of composite v1.14, and zero occur in PN of the S1
     replacement bytes
T-8  NO FALSE POSITIVE ON ANY RETAINED CLASS: zero D1 and zero D2 matches in PN
     of Cell 1, of the joint install and authorization block, of REGION(GUARDDATA),
     and of each of R-5's seven and R-6's two clauses taken alone
T-9  NO FALSE NEGATIVE ON ANY LISTED LITERAL: each of the 11 D1 and 13 D2
     literals, embedded in a marker-free carrier with arbitrary wrapping and
     arbitrary blockquote indentation, is DETECTED. THE TEST NAME AND THE
     ASSERTION MESSAGE MUST SAY "LISTED LITERAL", NOT "FORBIDDEN GRANT"
T-10 THE MP-1 FIXTURE OF BINDING §2.6.5: the marker-free paraphrase candidate
     PASSES PO-1, PO-2, PO-3 and D3, yields ZERO D1 and ZERO D2 matches, and
     FAILS PO-0 with full-output digest afbdb075…5ccf. A build that reports MP-1
     as conforming FAILS
T-11 D-3's token enum has exactly seven members, the terminal set exactly three,
     the qualifier set exactly two, and no member of either of the latter two is
     a member of the first or of FC-1's twenty-five
T-12 D-4's rule function is total over all 72 synthetic tuples with the stated
     partition sizes and no double answer
T-13 D-5's sets have 25 and 15 members in the stated order
T-14 D-6's sum is 89 and enumerations of 63, 69, 73, 77, 81, 85 and 93 FAIL
T-15 D-7's five key sets have exactly 11, 13, 5, 21 and 10 members
T-16 D-8's state set has exactly nine members and excludes W, x and K; the
     accepted-layout set has exactly one member; the suffix field count constant
     is exactly 50; the four field positions are 1, 2, 3 and 20; and the vector
     table names exactly one expected result per consumer per vector
T-17 THE IMPORT INVARIANT: neither allowed module is imported by anything
     outside tests/, and neither imports any production root
T-18 EVERY REPORTED DIGEST CARRIES THE test-only/non-installed/non-authoritative
     TAG
```

### §H7.3 Rows 92..115 are NOT implemented here

`MS-6`'s membership rule reserves `test_p1_row_NNN_` for rows 92..115 in two
modules that **do not exist**. `OR-5` installs them and `OR-7` runs them.
**Nothing under this handoff may create such a function or such a module.** In
particular **row 89's counterexample fixtures, its permutation fixtures, its
dominance-pair fixtures and its parser-vector fixtures are NOT implemented
here**: they exercise a live classifier and a live parser, and neither exists nor
may be written.

---

## §H8. Verifier behaviour while inert

Nothing under this handoff is reachable from a production entry point, an
install path or an activation path. **No verifier is written here.** The M5
verifier of `OR-5` will, when it exists, refuse before any production action if
an identity-observation surface, a W-A capability or an unresolved variant block
is present. **That is a future obligation recorded here, not an implemented
one.**

---

## §H9. The existing working-tree implementation — audit obligation

```text
src/philosophia/officina/generic_harness.py IS PRODUCTION ROOT 3 OF §P1-3.1 AND
IT EXISTS UNTRACKED IN THE WORKING TREE.

IT IS NOT EVIDENCE OF ANYTHING FOR P1, IT MAY NOT BE ADOPTED, AND IT MAY NOT BE
EDITED, REVERTED, STAGED OR CITED UNDER THIS HANDOFF.

WHY IT CANNOT SIMPLY BE REUSED, stated from the governing bytes and not from a
reading of the file: §P1-3.2 gives that path a MODULE_SCOPED import entry of
EXACTLY 16 names, "a file with an entry gets EXACTLY that entry and never the
union with the default", and S-12 forbids subprocess, Popen, fork, waitpid,
kill, killpg and system on any path of that file.

WHY CALLING IT A BUG WOULD BE WRONG: §P1-3.2 itself records that the accepted
generic-harness chain genuinely grants that launcher capability. The file
conforms to its own lineage and does not conform to P1, because P1 superseded
the launch route.

THE REQUIRED CONTROL. THIS VERSION RECORDS NO LINE NUMBERS AND NO CONTENT CLAIMS
ABOUT THAT FILE AT ALL, and it was not opened while this handoff was written.
  A-1  A FRESH AUDIT IS MANDATORY before any P1 reuse of that path.
  A-2  IT MUST BE ITS OWN REVIEWED ARTIFACT, produced against the v1.11/v1.14
       bytes at the digests of §H1 R-1, at a commit it names. An informal
       reading does not discharge A-1.
  A-3  NO LINE MAY BE COPIED WITHOUT RE-DERIVATION from those bytes.
  A-4  ITS COMPANION TEST MODULE PROVES NOTHING ABOUT P1 CONFORMANCE AND MAY
       NOT BE CITED.
  A-5  BRINGING THAT PATH INTO P1 CONFORMANCE IS OR-5-ERA WORK UNDER A SEPARATE
       AUTHORIZATION and is outside this handoff entirely.
```

---

## §H10. The fenced gaps

`R-2` says: where this document is not exact enough, stop and ask. These are the
places where it is known to bite.

```text
G-0  THE TWO BOUND BOOTSTRAP QUERY PRIMITIVES, NEW IN v5 AND FENCED FROM THE
     MOMENT THEY EXIST. Composite v1.14 §P1-3.4 binds `_getsid` and `_getpgid`
     from `os`, pins their argument, result and error semantics, and gives them
     exactly three call sites — §P1-7.5 `c10`, `c14` and `m3`. **THE SCAFFOLD MAY
     HOLD THE BINDING LIST, THE TWO NAMES, THEIR EXPECTED `__qualname__` VALUES
     AND THEIR RESULT BOUNDS AS DECLARATIVE DATA. IT MAY NOT CALL EITHER NAME,
     MAY NOT IMPORT `os` FOR THEM, MAY NOT WRITE `c10`, `c14` OR `m3`, AND MAY
     NOT WRITE ANY BOOTSTRAP STEP.** A binding is a specification fact; running
     it is a process-control operation, and §H1's no-syscall rule and §H11's
     ungranted runtime authorization both forbid it. A dummy test may assert that
     the declarative list CONTAINS the two names; no test may invoke them.

G-A  THE CANONICAL PARSER AND THE PCS FREEZE CLASSIFIER. Composite v1.14
     §P1-10.3 defines STAT_READ, STAT_PARSE L0..L5 and KG_GROUP_ADMISSIBLE, and
     §P1-10.7 defines KG-1, KG-2's P-1..P-12 population rules, KV-1..KV-6, and
     SC-1..SC-10 including all six phases and the dominance table, IN FULL AND
     EXECUTABLY. NONE OF IT IS IMPLEMENTABLE HERE, because implementing it
     requires /proc reads against live processes, a real handle table, a real
     SPAWNING_GROUP.json read, _killpg, an AWAIT_STOP evaluation and a P1-owned
     journal — none of which any allowed path may touch.
     D-4 models SC-7's TABLE over synthetic tuples and D-8 holds the parser's
     DATA as constants; NEITHER IS THE PARSER AND NEITHER IS THE CLASSIFIER.
     DO NOT WRITE STAT_READ, DO NOT WRITE STAT_PARSE, DO NOT WRITE
     KG_GROUP_ADMISSIBLE, DO NOT WRITE PGRP_OBSERVE, DO NOT WRITE THE KG-2
     POPULATION SITE, AND DO NOT WRITE ANY OF THE SIX PHASES.

G-B  THE WATCHDOG EOF ROUTE, THE SUPERVISOR FREEZE ROUTES, THE DESCRIPTOR
     TOPOLOGY AND EVERY PROCESS OPERATION. Same reason. DO NOT WRITE THEM.

G-C  THE M5 VERIFIER AND THE M6 MODULES, INCLUDING G-10, G-11 AND CK-1..CK-15.
     OR-5 installs them and OR-7 runs them. DO NOT WRITE THEM.

G-D  ANYTHING NOT LISTED IN §H3 D-1..D-8 OR §H4. If a task seems to require it,
     STOP AND ASK. Do not infer it, do not reconstruct it from a superseded
     document, and do not fill it with a reasonable default.
```

---

## §H11. Later-stage authorization table

**What each excluded surface needs before it may be written, after governing
acceptance.** Each row is a **separate** author act. None of them is granted by
the acceptance token, and none is granted by an inactive-scaffold authorization.

```text
SURFACE                                REQUIRES, SEPARATELY AND IN ADDITION
---------------------------------------------------------------------------
the inert oracle and the declarative   (1) acceptance of
  contract module of §H2.1                 I_ACCEPT_..._AMENDMENT_V1_11
                                       (2) an INACTIVE-SCAFFOLD AUTHORIZATION
                                       neither exists

the W-B watchdog EOF route             (1) and (2) above, PLUS
the canonical parser of §P1-10.3       (3) a RUNTIME IMPLEMENTATION
  (STAT_READ, STAT_PARSE L0..L5,           AUTHORIZATION naming the routes it
   KG_GROUP_ADMISSIBLE)                    permits, the paths they may occupy
the PCS freeze classifier                  and the isolation regime under which
  (KG-1, KG-2, KV-1..KV-6,                 they may be exercised
   SC-1..SC-10, all six phases)        (4) a reviewed disposition of the
the descriptor topology and file           §H9 generic_harness.py audit, if any
  actions                                  of it lands at production root 3
the supervisor freeze routes           none of (3) or (4) exists
every process, signal, wait and
  descriptor operation
every /proc read

the M5 verifier at MS-5's literal      (1), (2), (3), PLUS
  path                                 (5) the ONE-SHOT ATOMIC-HANDOFF
the two M6 modules and rows 92..115,       AUTHORIZATION, because these paths
  including row 89's counterexample,       are MEMBER paths and creating them is
  permutation, dominance-pair and          OR-5, which lands only with
  parser-vector fixtures                   OR-3..OR-11 or not at all
                                       (5) does not exist

Stage A, the Ed25519 key pair          (1), (5), and OR-3 in order. NO KEY MAY
                                       BE GENERATED BEFORE THEN, AND THE KEY IS
                                       NOT A SEPARATE PERMISSION FROM OR-3

OR-4 resolved composite bytes,         (1), (5), and OR-3 complete and verified.
  including WRITING any of the         THE PINNED BYTES AND THE PINNED FULL
  eleven replacement blocks or the     OUTPUT ARE SPECIFICATION CONSTANTS UNTIL
  full resolved output to disk         THEN AND NOTHING MORE

M4, M7, the member list, Stage B,      (1), (5), and OR-5..OR-10 in order
  the detached signature, the install
  record

T activation                           everything above, PLUS a separate T
                                       activation act. T = NOT_ACTIVATED.
---------------------------------------------------------------------------
THE WRITE SCOPE IS NOT EXPANDED BY THIS ROUND. This table names what would be
required; it grants none of it and predicts none of it.
```

---

## §H12. Evidence that `T` remains `NOT_ACTIVATED`

```text
E-1   No file exists at either TS-3 Stage-B path, at the TS-1 Stage-A path, at
      MS-4's path, at MS-7's path, or under the INSTALL directory.
E-2   Neither MS-6 module exists.
E-3   src/philosophia/officina/verification.py exists ONLY as the non-enforced
      pre-install baseline named in the composite provenance region. It is not
      M5 and it is not edited.
E-4   Zero test_p1_row_NNN_ functions exist in the repository.
E-5   Neither allowed module of §H2.1 exists yet, because no authorization to
      write them exists.
E-6   No Ed25519 key, no key_id and no public_key_hex value exists as key
      MATERIAL anywhere. THE IDENTIFIERS key_id AND public_key_hex OCCUR
      THROUGHOUT GOVERNING PROSE AS FIELD NAMES; a bare absence check on those
      strings produces a false failure and must not be used. The correct check
      is for key MATERIAL and for an ARTIFACT at a TS-1 or TS-3 path.
E-7   THE ACCEPTANCE TOKEN OCCURS IN GOVERNING AND SIGNATURE PROSE — including
      under a heading recording that it remains unsigned. A bare absence check
      on that string produces a false failure. The correct check is that no
      SIGNED acceptance artifact exists.
E-8   No OR step has run. OR-4 did not run, and no resolved amendment or
      composite bytes exist at any path. THE ELEVEN REPLACEMENT BLOCKS EXIST
      ONLY INSIDE THE BINDING DOCUMENT, AND THE FULL RESOLVED OUTPUT EXISTS ONLY
      AS A LENGTH AND A DIGEST.
E-9   The two governing files are at the digests of §H1 R-1 and have not been
      modified since they were written.
```

---

## §H13. Negative space

This handoff creates nothing executable and authorizes no implementation,
commit, host change, verifier edit, manifest, process, socket, pipe, FIFO, fork,
exec, signal, wait or `prctl` operation, key, entropy, seed, Stage A, Stage B,
detached signature, attestation, member list, install record, capability, world,
learner, candidate, trajectory, capacity artifact, custody disposition, result
manifest, spend, datum, outcome, Proof or claim movement.

No freeze was executed, requested, journalled or witnessed. No `/proc` was read
against any live process. No clock was sampled for any contract purpose. No
Philosophia production or project module was imported, executed or compiled. No
existing file was modified.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 WATCHDOG-FREEZE CELL = SELECTED: OPTION W-B, SENSOR-ONLY
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, OBSERVATION-ONLY
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
P1 IDENTITY-OBSERVATION IMPLEMENTATION SURFACE = OUT OF SCOPE, NO CODE
WATCHDOG AUTHORITY AMENDMENT V1.11 = NOT ACCEPTED
INACTIVE-SCAFFOLD AUTHORIZATION = NOT GRANTED
RUNTIME IMPLEMENTATION AUTHORIZATION = NOT GRANTED
ONE-SHOT ATOMIC-HANDOFF AUTHORIZATION = NOT GRANTED
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
```

This handoff, the companion binding and every author closure are untrusted
self-assessments and are normative for nothing. The exact selected token and the
formal selection signature govern.
