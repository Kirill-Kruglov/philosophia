# Officina P1 W-B inert scaffold handoff v2 (draft)

**Author:** Claude Code Opus 5, **handoff author only**. This document is a
**scope contract for a future implementer**. It is not an implementation
authorization.

**NOTHING IN THIS DOCUMENT AUTHORIZES CODE TO BE WRITTEN.** Writing code under it
requires (i) acceptance of
`I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8` and
(ii) a separate **inactive-scaffold authorization**. Neither exists. `T` is
`NOT_ACTIVATED`; the programme claim is `OPEN`.

---

## §H-0. THE HONEST TITLE OF THIS DOCUMENT — read this before §H1

**`Y-M5` REPAIR.** Version 1 of this handoff was called an "inactive
implementation handoff" and its `§H3` described the watchdog EOF route, the PCS
endpoint-loss trigger, the group-stop authority and the supervisor freeze routes
as *behaviour to implement*. The Y line determined, and this author line accepts
without reservation, that **no path on the allowed list can implement any of
that**. The two allowed code paths are an in-memory byte oracle and a pure data
module with no I/O, no syscall and no clock. A route that must observe pipe EOF,
call `_killpg`, hold descriptors and order durable records **cannot be written
with those**.

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
    including KG-1, KG-2, KV-1..KV-6 and SC-1..SC-8, which composite v1.11
    §P1-10.7 now DEFINES IN FULL. A DEFINITION IS NOT AN AUTHORIZATION.
  THE DESCRIPTOR TOPOLOGY.          NOT IMPLEMENTED, NOT IMPLEMENTABLE HERE.
  ANY PROCESS OPERATION.            NOT IMPLEMENTED, NOT IMPLEMENTABLE HERE.
  THE SUPERVISOR FREEZE ROUTES.     NOT IMPLEMENTED, NOT IMPLEMENTABLE HERE.
  THE M5 VERIFIER, THE M6 MODULES, G-10, G-11 OR CK-1..CK-15.
                                    NOT IMPLEMENTED. OR-5 AND OR-7 OWN THEM.

§H11 states, item by item, what separate authorization each of those requires.
THE ALLOWED SURFACE IS NOT EXPANDED BY THIS ROUND. Narrowing the claim is the
repair; widening the scope would be a separate authorization decision that no
one has taken.
```

Read together with
`successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V2_DRAFT.md`. Where the two
differ, **the binding governs**; where the binding and a governing clause of the
v1.8/v1.11 pair differ, **the governing clause governs and both drafts are the
defect.**

---

## §H1. Standing rules for the implementer

```text
R-1  IMPLEMENT FROM GOVERNING BYTES ONLY. The only documents opened for
     behaviour are
       successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8_DRAFT.md
         71ec025a6d5da2b975e8f958d4c5e218e37e0de76fc1c64e2824e20cb3e08a4c
       successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_11.md
         c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6
     Every earlier amendment (v1..v1.7), every earlier composite (v1..v1.10),
     every author choice packet including v2.11, and every review file are
     HISTORICAL EVIDENCE ONLY and are NOT opened to determine behaviour
     (DA-1, DA-2, DA-4, IR-12).

R-2  NO DESIGN DISCRETION. Where this document is not exact enough to implement
     a function, STOP AND ASK. Do not infer, do not reconstruct from a
     superseded document, and do not fill a gap with a reasonable default.

R-3  W-B ONLY. Never implement, stub, flag, comment or leave dead a W-A
     capability. No freeze-request socket, no slot-6 endpoint, no
     t-wd-freeze.v1 frame, no bounded service window, no accept or reject of a
     watchdog request. THE W-A TOKENS THEMSELVES REMAIN IN TS-1's CLOSED
     VALIDATION VOCABULARY and in the CK-14 fixture, and a fixture that deletes
     them is WRONG — see binding §2.5.

R-4  INERT MEANS INERT. Nothing written under this handoff may be reachable from
     a production entry point, an install path or an activation path, and
     nothing written under it may perform I/O, a syscall, a clock read, a
     descriptor operation or a process operation. §H8 states the verifier
     obligation that enforces the first half; §H7.1 states the isolation rule
     that enforces the second.

R-5  NO PROCESS-CONTROL SMOKE ANYWHERE. Not in the shared runtime tree, not in a
     temporary root, not in a container, not under a marker. There is no
     process-control smoke test under this handoff at all.

R-6  THIS IS NOT OR-4. No file at either MS-1 literal path is edited, ever,
     under this handoff. The oracle rewrites copies in memory and returns them.

R-7  A GOVERNING DEFINITION IS NOT AN IMPLEMENTATION AUTHORIZATION. Composite
     v1.11 §P1-10.7 now defines the classifier's per-group verification in full.
     THAT DOES NOT MAKE IT WRITEABLE HERE. See §H10 and §H11.
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
      NAMES, literal key sets, literal count constants. NO I/O, NO SYSCALL, NO
      CLOCK, NO DESCRIPTOR, NO SOCKET, NO SUBPROCESS, NO THREAD.

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

REMOVED FROM v1's ALLOWED LIST, AND THE REMOVAL IS THE POINT:
  tests/test_officina_p1_wb_classifier_ordering.py       — it would have had no
      implementation under test. The classifier is not implementable here.
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
  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8_DRAFT.md
  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_11.md

THE FIVE P1 PRODUCTION ROOTS OF §P1-3.1 — frozen under this handoff
  scripts/officina_activate_t.py                       exists, DO NOT EDIT
  scripts/verify_officina_active.py                    exists, DO NOT EDIT
  src/philosophia/officina/generic_harness.py          exists UNTRACKED, DO NOT
                                                       EDIT, DO NOT ADOPT — §H11
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
  every signature. NOT EDITED, NOT STAGED, NOT REVERTED, NOT DELETED.

UNRELATED DIRTY AND UNTRACKED WORK — src/philosophia/officina/accounting.py, its
  test module, the reviews/ files, essay/OUTLINE.md, and the untracked
  generic_harness.py and its test module. NOT TOUCHED BY ANYTHING HERE.
```

---

## §H3. What the scaffold may model — declaratively, and only declaratively

**This section replaces v1's "Behaviour to implement".** Nothing below is a
runtime route. Each item is a **statement of the contract as data**, checkable by
a dummy test, with no execution of the thing it describes.

```text
D-1  THE W-B DESCRIPTOR TOPOLOGY AS A LITERAL TABLE.
     The watchdog role's expected /proc/self/fd set is the literal frozen set
     {0,1,2} | {3,4,5,7,8,9,10}, slot 6 absent. THIS IS A CONSTANT IN
     p1_wb_contract.py. NO DESCRIPTOR IS OPENED, DUPED, CLOSED OR INSPECTED.

D-2  THE W-B NEGATIVE SURFACE AS A LITERAL PREDICATE LIST.
     "writes nothing, freezes nothing, signals nothing, sends nothing, exits"
     as an enumerated frozen tuple of contract statements. NO EOF IS OBSERVED
     AND NO EXIT IS PERFORMED.

D-3  THE SC-5 RESULT-TOKEN SET AS A CLOSED ENUM.
     Exactly seven names: KV_OK, KV_STALE_HANDLE, KV_ROLE_OR_STATE_REFUSED,
     KV_OBSERVATION_UNAVAILABLE, KV_IDENTITY_CONTRADICTED, KV_GROUP_MISMATCH,
     KV_FORBIDDEN_TARGET. A dummy test asserts the enum has exactly seven
     members and no eighth. NO CLASSIFIER RUNS AND NO PREDICATE IS EVALUATED
     AGAINST A LIVE PROCESS.

D-4  THE SC-7 TOTALITY TABLE AS PURE DATA.
     The role x state x ownership x pgid product, 3 x 4 x 3 x 2 = 72, with the
     ordered rule list of SC-7 as a pure function over SYNTHETIC TUPLES. A dummy
     test asserts the function is total over all 72 synthetic tuples, that the
     partition sizes are 24 + 32 + 4 + 6 + 6 = 72, and that no tuple has two
     answers. THE INPUTS ARE INVENTED TUPLES. THERE IS NO HANDLE TABLE, NO
     /proc READ, NO PID AND NO SIGNAL.
     THIS IS A TABLE-TOTALITY TEST, NOT A CLASSIFIER. It proves that SC-7's
     partition is total as stated; it proves NOTHING about any running system.

D-5  THE FC-1 CLOSED FAILURE-CODE SET AS A LITERAL FROZEN SET of 25 names, and
     the CK-1..CK-15 ordering as a literal ordered tuple of 15 names. A dummy
     test asserts the cardinalities and the order. NO CHECK IS EXECUTED AND NO
     VERIFIER IS IMPLEMENTED — G-10, G-11 and CK-1..CK-15 belong to OR-5's M5
     verifier and MUST NOT be written here.

D-6  THE MEMBER-CLASS ACCOUNTING AS LITERAL CONSTANTS.
     M1 2, M2 63, M3 7, M4 1, M5 1, M6 2, M7 1, total 77; TS-3 member_count 77;
     composite provenance region 71 rows; 7 member classes. A dummy test asserts
     the sum and the NEGATIVE cases of binding PR-4: an enumeration of 59, 69,
     73 or 81 FAILS. NO MEMBER IS ENUMERATED FROM DISK.

D-7  THE SCHEMA KEY SETS AS LITERAL FROZEN SETS — TS-1's eleven keys, TS-3's
     thirteen, IR-3's five, MS-4's twenty-one, MS-7's ten. A dummy test asserts
     each cardinality and each exact key set. NO ARTIFACT IS PARSED, WRITTEN OR
     VALIDATED, and no instance of any of them is constructed.
```

---

## §H4. The transformation oracle

The one thing that may actually be built, and it is inert.

```text
SIGNATURE SURFACE, NORMATIVE FOR THIS HANDOFF.

resolve_wb(amendment_bytes: bytes, composite_bytes: bytes) -> bytes
    pure; returns a candidate resolved composite byte string; writes nothing

check_po(resolved: bytes, guarddata_digest: str) -> tuple[PoResult, ...]
    pure; evaluates binding §2.4 PO-1..PO-9 and returns one result per check,
    each carrying the check name, a pass/fail boolean and the failing locus

census(resolved: bytes) -> OccurrenceCensus
    pure; evaluates binding §2.5's class R and class F rows and returns the
    observed count for each against its expected count

detect_open_cell(resolved_minus_guarddata: bytes) -> tuple[Finding, ...]
    pure; binding §2.6 detectors D1 and D2, over a closed list of normalized
    phrase patterns held IN THE ORACLE, never in the composite

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

FORBIDDEN, ABSOLUTELY: writing any governing or runtime path; any key or
entropy; any Stage A, Stage B, signature, manifest, attestation, member list or
install record; any process, socket, pipe, fork, exec, signal, wait, prctl or
/proc operation; and any export that a writer of a governing path could accept.
```

---

## §H5. The declarative contract surface

`p1_wb_contract.py` carries **only** the `§H3` `D-1`..`D-7` data. It is pure:
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
composite v1.11 and ZERO times in amendment v1.8. There is no schema, key, type,
carrier, consumer or destination to conform to. Code written now could only be
invented, and composite Cell 1 says in its own words that the document "chooses
neither and invents no value."

THIS HANDOFF IS NOT THE LATER COMBINED BINDING OF XS-1. It does not resolve
§P1-13.2 row 2, does not accept P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1,
does not decide membership for the identity signature, and does not re-derive
any identity field. The combined binding remains BLOCKED_PENDING_IDENTITY_
WEAKENING_REVIEW.

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
I-2  NO /proc READ AGAINST ANY LIVE PROCESS. D-4's inputs are synthetic tuples.
I-3  NO PRODUCTION ARTIFACT NAME. No fixture file may be named for, or placed
     at, any MS-1..MS-7, TS-1 or TS-3 path, or any name a reader could mistake
     for an installed object.
I-4  NO KEY-GENERATION PRIMITIVE ANYWHERE IN THE SUITE. Not Ed25519, not any
     other algorithm, not a seed, not a CSPRNG draw for a key-shaped value. This
     is absolute and has no marker-gated exception.
I-5  NO WRITE OUTSIDE A PER-TEST TEMPORARY ROOT. Created by tempfile.mkdtemp,
     removed by the test.
I-6  NO CLOCK IS SAMPLED FOR ANY CONTRACT PURPOSE.
I-7  NO SHARED RUNTIME TREE IS TOUCHED, created, read or written.
```

### §H7.2 What the dummy tests assert

```text
T-1  the oracle is deterministic: two runs over the same inputs return identical
     bytes
T-2  PO-1..PO-9 each return a result, and the oracle's own negative fixtures —
     a candidate with a surviving body marker, one with a surviving preamble
     marker, one with a mutated guard-data region, one with a deleted TS-1
     literal, one with a surviving open-cell sentence, one with a surviving W-A
     grant — each FAIL the expected check and no other
T-3  binding §2.5's class R rows are each present at their expected count in a
     correct candidate, and DELETING ANY OF THEM FAILS D3
T-4  binding §2.5's class F rows are each absent at count zero in a correct
     candidate
T-5  D1's pattern list covers every REPLACE row of binding §2.2; a pattern list
     that does not is reported INCOMPLETE
T-6  D-3's enum has exactly seven members
T-7  D-4's rule function is total over all 72 synthetic tuples with the stated
     partition sizes and no double answer
T-8  D-5's sets have 25 and 15 members in the stated order
T-9  D-6's sum is 77 and enumerations of 59, 69, 73 and 81 FAIL
T-10 D-7's five key sets have exactly 11, 13, 5, 21 and 10 members
T-11 THE IMPORT INVARIANT: neither allowed module is imported by anything
     outside tests/, and neither imports any production root
T-12 EVERY REPORTED DIGEST CARRIES THE test-only/non-installed/non-authoritative
     TAG
```

### §H7.3 Rows 92..115 are NOT implemented here

`MS-6`'s membership rule reserves `test_p1_row_NNN_` for rows 92..115 in two
modules that **do not exist**. `OR-5` installs them and `OR-7` runs them.
**Nothing under this handoff may create such a function or such a module.**

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

THE REQUIRED CONTROL, AND IT IS FRESH — v1 of this handoff recorded line-number
observations of that file and the Y line correctly said they are accurate for one
worktree and are NOT DURABLE EVIDENCE. THIS VERSION RECORDS NO LINE NUMBERS AND
NO CONTENT CLAIMS ABOUT IT AT ALL.
  A-1  A FRESH AUDIT IS MANDATORY before any P1 reuse of that path.
  A-2  IT MUST BE ITS OWN REVIEWED ARTIFACT, produced against the v1.8/v1.11
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
G-A  THE PCS FREEZE CLASSIFIER. Composite v1.11 §P1-10.7 now defines KG-1, KG-2,
     KV-1..KV-6 and SC-1..SC-8 IN FULL, so the F2 gap of the v1.7/v1.10 pair is
     closed AS A SPECIFICATION MATTER. IT IS STILL NOT IMPLEMENTABLE HERE,
     because implementing it requires /proc reads against live processes, a real
     handle table, _killpg and a P1-owned journal — none of which any allowed
     path may touch. D-4 models SC-7's TABLE over synthetic tuples and nothing
     more. DO NOT WRITE THE CLASSIFIER.

G-B  THE WATCHDOG EOF ROUTE, THE SUPERVISOR FREEZE ROUTES, THE DESCRIPTOR
     TOPOLOGY AND EVERY PROCESS OPERATION. Same reason. DO NOT WRITE THEM.

G-C  THE M5 VERIFIER AND THE M6 MODULES, INCLUDING G-10, G-11 AND CK-1..CK-15.
     OR-5 installs them and OR-7 runs them. DO NOT WRITE THEM.

G-D  ANYTHING NOT LISTED IN §H3 D-1..D-7 OR §H4. If a task seems to require it,
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
  contract module of §H2.1                 I_ACCEPT_..._AMENDMENT_V1_8
                                       (2) an INACTIVE-SCAFFOLD AUTHORIZATION
                                       neither exists

the W-B watchdog EOF route             (1) and (2) above, PLUS
the PCS freeze classifier              (3) a RUNTIME IMPLEMENTATION
  (KG-1, KG-2, KV-1..KV-6, SC-1..SC-8)     AUTHORIZATION naming the routes it
the descriptor topology and file           permits, the paths they may occupy
  actions                                  and the isolation regime under which
the supervisor freeze routes               they may be exercised
every process, signal, wait and        (4) a reviewed disposition of the
  descriptor operation                     §H9 generic_harness.py audit, if any
                                           of it lands at production root 3
                                       none of (3) or (4) exists

the M5 verifier at MS-5's literal      (1), (2), (3), PLUS
  path                                 (5) the ONE-SHOT ATOMIC-HANDOFF
the two M6 modules and rows 92..115        AUTHORIZATION, because these paths
                                           are MEMBER paths and creating them is
                                           OR-5, which lands only with
                                           OR-3..OR-11 or not at all
                                       (5) does not exist

Stage A, the Ed25519 key pair          (1), (5), and OR-3 in order. NO KEY MAY
                                       BE GENERATED BEFORE THEN, AND THE KEY IS
                                       NOT A SEPARATE PERMISSION FROM OR-3

OR-4 resolved composite bytes          (1), (5), and OR-3 complete and verified

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
      composite bytes exist at any path.
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
WATCHDOG AUTHORITY AMENDMENT V1.8 = NOT ACCEPTED
INACTIVE-SCAFFOLD AUTHORIZATION = NOT GRANTED
RUNTIME IMPLEMENTATION AUTHORIZATION = NOT GRANTED
ONE-SHOT ATOMIC-HANDOFF AUTHORIZATION = NOT GRANTED
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
```

This handoff, the companion binding and every author closure are untrusted
self-assessments and are normative for nothing. The exact selected token and the
formal selection signature govern.
