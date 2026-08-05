# Officina P1 W-B inactive implementation handoff v1 (draft)

**Author:** Claude Code Opus 5, **handoff author only**. This document is a
**scope contract for a future implementer (Cursor)**. It is not an
implementation authorization.

**NOTHING IN THIS DOCUMENT AUTHORIZES CODE TO BE WRITTEN.** Writing code under
it requires (i) acceptance of
`I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7`
and (ii) a separate implementation authorization. Neither exists. `T` is
`NOT_ACTIVATED`; the programme claim is `OPEN`.

Read together with
`successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V1_DRAFT.md`. Where the two
differ, the binding governs; where the binding and a governing clause of the
v1.7/v1.10 pair differ, **the governing clause governs and both drafts are the
defect.**

---

## §H0. Standing rules for the implementer

```text
R-1  IMPLEMENT FROM GOVERNING BYTES ONLY. The only documents opened for
     behaviour are
       successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7_DRAFT.md
       successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_10.md
     at the digests recorded in the binding §0.2. Every earlier amendment
     (v1..v1.6), every earlier composite (v1..v1.9), every author choice packet
     including v2.10, and every review file are HISTORICAL EVIDENCE ONLY and
     are NOT opened to determine behaviour (DA-1, DA-2, IR-12).

R-2  NO DESIGN DISCRETION. Where this document is not exact enough to implement
     a function, STOP AND ASK. Do not infer, do not reconstruct from a
     superseded document, and do not fill a gap with a reasonable default.
     §H12 lists the one place where this is known to bite.

R-3  W-B ONLY. Never implement, stub, flag, comment or leave dead a W-A
     capability. No freeze-request socket, no slot-6 endpoint, no
     `t-wd-freeze.v1` frame, no bounded service window, no accept/reject of a
     watchdog request.

R-4  INACTIVE MEANS INACTIVE. Nothing written under this handoff may be
     reachable from a production entry point, an install path or an activation
     path. §H10 states the verifier obligation that enforces this.

R-5  NO PROCESS-CONTROL SMOKE IN THE SHARED RUNTIME TREE. §H9 states the
     isolation rule and it is absolute.

R-6  THIS IS NOT OR-4. No file at either MS-1 literal path is edited, ever,
     under this handoff. The transformation oracle of §H4 rewrites copies in
     memory and returns them.
```

---

## §H1. Paths

### §H1.1 Allowed paths — the complete list

Nothing outside this list may be created or edited.

```text
CODE
  src/philosophia/officina/p1_wb_oracle.py
      the §H4 in-memory transformation oracle. TEST-ONLY. It is not M5, is not
      a production root, and is imported by nothing under scripts/.

  src/philosophia/officina/p1_wb_contract.py
      the §H5 pure declarative surface — enums, dataclasses, error codes,
      descriptor topology, schema key sets. NO I/O, NO SYSCALL, NO CLOCK.

TESTS
  tests/test_officina_p1_wb_oracle.py
  tests/test_officina_p1_wb_contract.py
  tests/test_officina_p1_wb_classifier_ordering.py
  tests/test_officina_p1_wb_negative_surface.py
  tests/test_officina_p1_wb_disposable_integration.py

FIXTURES
  tests/fixtures/p1_wb/            deterministic, committed, test-only

SCRATCH
  a per-test temporary root created by tempfile.mkdtemp and removed by the test

NOTHING ELSE. In particular: no new file under scripts/, none under
successor/, none under successor/officina/, and none under any INSTALL
directory.
```

### §H1.2 Frozen paths — must not be edited, created or deleted

```text
THE GOVERNING PAIR — read-only, opened for behaviour, never written
  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7_DRAFT.md
  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_10.md

THE FIVE P1 PRODUCTION ROOTS OF §P1-3.1 — frozen under this handoff
  scripts/officina_activate_t.py                       exists, DO NOT EDIT
  scripts/verify_officina_active.py                    exists, DO NOT EDIT
  src/philosophia/officina/generic_harness.py          exists UNTRACKED, DO NOT
                                                       EDIT — see §H11
  scripts/officina_process_control_bootstrap.py        ABSENT — DO NOT CREATE
  scripts/officina_role_bootstrap.py                   ABSENT — DO NOT CREATE

THE HANDOFF-STEP ARTEFACT PATHS — none may be created
  src/philosophia/officina/verification.py             MS-5. EXISTS as the
      non-enforced pre-install baseline. It is NOT M5 and DO NOT EDIT IT.
  tests/test_officina_p1_freeze_authority.py           MS-6 module 1, ABSENT
  tests/test_officina_p1_install_integrity.py          MS-6 module 2, ABSENT
  successor/officina/authorization/P1_WATCHDOG_FREEZE_SELECTION_V1.json
                                                       TS-1 Stage A, ABSENT
  successor/officina/runtime_control/INSTALL/…         M4, M7, install record,
                                                       Stage B, .sig — ABSENT

  THE THREE M6/M5 PATHS ABOVE ARE THE MOST LIKELY MISTAKE. Rows 92..115 belong
  to modules that OR-5 and OR-7 create. Creating them now would produce files
  at member paths before OR-3 exists.

THE FOUR MS-13 PROJECT MODULES — digest-bound; a byte change breaks the manifest
  src/philosophia/__init__.py
  src/philosophia/officina/__init__.py
  src/philosophia/officina/canonical.py
  src/philosophia/officina/interlock.py

ALL HISTORY — every successor/ document, every reviews/ file, every signature,
every runtime artifact, and every unrelated dirty file in the working tree.
```

---

## §H2. Process and descriptor topology under W-B

```text
WATCHDOG ROLE PROCESS
  created by       PCS opcode SPAWN_WATCHDOG, and by nothing else
  setsid           False — not a session leader, never a killpg target
  address space    execve'd, fresh, therefore holds no capability by
                   construction
  parent           the PCS. NOT the supervisor. A getppid() change means the
                   PCS died, which is a DISTINCT condition from supervisor
                   death.

  DESCRIPTOR SET, EXACTLY, AND THIS IS TEST ROW 99
    0, 1, 2        standard
    3              UPDATE PIPE READ END        sealed
    4              ACK PIPE WRITE END          sealed
    5              present
    6              ABSENT — EXPLICITLY CLOSED BY A FILE ACTION
    7, 8, 9, 10    present
    /proc/self/fd == {0,1,2} ∪ {3,4,5,7,8,9,10}

  UNDER W-B SLOT 6 IS NOT A SOCKET, NOT AN AF_UNIX SOCKETPAIR, NOT
  SOCK_SEQPACKET, NOT O_RDWR AND NOT PRESENT. There are TWO SEALED PIPES, not
  three sealed endpoints.

  NEGATIVE, ON EVERY PATH
    no SPAWN.lock descriptor        no lock of any kind
    no capability object            no write under runtime/
    no ledger append                no settlement, quarantine, promotion or
                                    capacity effect
    no signal sent OR received      no killpg, no kill
    no durable object of any class  no evidence, no witness
    it communicates ONLY over slots 3 and 4

  THE ONE PERMITTED PEER-LAYER OPERATION, WHICH IS ALSO REQUIRED
    read-only verification of the supervisor identity record of §P1-13.2 row 3
    (§P1-9.2 property 8, invariant 87). Never by any parent relationship.
    A read installs nothing and is not an authority.

SUPERVISOR ROLE PROCESS
  holds SPAWN.lock at slot 3 until its identity record is live-verified, then
  closes it. Direct parent of nothing, reaper of nothing; a wildcard wait
  returns ECHILD. Holds opaque handles and CANNOT EXPRESS A PID.

PCS
  the SOLE CALLER of fork, posix_spawn, kill, killpg and every wait-family
  primitive (S-12). Never retains the watchdog update-pipe WRITE end (N-2) —
  which is what keeps update-pipe EOF reachable on supervisor death.
```

---

## §H3. Behaviour to implement

### §H3.1 Watchdog EOF and exit — the whole of it

```text
DETECTION       exactly one mechanism: EOF on the slot-3 update READ end.
                No other mechanism. getppid() is PROHIBITED as a
                supervisor-death inference and the prohibition is not weakened.

ON EOF, W-B     write nothing
                freeze nothing
                signal nothing
                send nothing
                settle nothing
                os._exit(0)

THERE IS NO ELSE-BRANCH. No cleanup write, no final ack, no log line to a
durable path, no flush of a pending record — there is no pending record.

TERMINATION SEQUENCE (§P1-9.4 S-3..S-5)
  S-3  the supervisor closes the update pipe WRITE end
  S-4  the watchdog observes EOF, writes nothing, os._exit(0)
  S-5  the PCS reaps it on REAP_ROLE, bounded by
       T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS
         REAPED_POSITIVE      death proved; RELEASE_HANDLE
         CONTRADICTED_ECHILD  death NOT proved -> §P1-11.6
         STRUCTURAL_VIOLATION death NOT proved -> §P1-11.6
         NOT_YET at the bound WATCHDOG_UNREAPED -> §P1-11.6

  Watchdog death is observed and reaped before the supervisor exits, or the
  generation is explicitly invalid. THERE IS NO THIRD BRANCH.

ACK DUTY, unchanged by W-B: the watchdog acknowledges each published table on
the slot-4 ack pipe. The supervisor treats an absent acknowledgement past
T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS as watchdog death.
```

### §H3.2 PCS endpoint-loss trigger and record-first ordering

```text
ACTOR       the PCS, executing in the PCS root
TRIGGER     loss of the peer control endpoint — and no other trigger exists on
            this branch
ORDER       RECORD-FIRST. The classifier's journal record for the trigger is
            durable BEFORE any group action is taken for it. "Record-first"
            is the ordering constraint and it is not a performance hint.
MEDIATION   NONE. It is not SIGNAL_GROUP-mediated, BECAUSE IT IS THE PCS.
SCOPE       computed from the PCS's OWN HANDLE TABLE, under KV-1..KV-6
            re-evaluated before EVERY _killpg  ——  SEE §H12, THIS IS FENCED
EVIDENCE    NONE. It writes no t-freeze-observation.v1, no
            t-freeze-fallback-observation.v1, and no record of any peer class.
JOURNAL     terminal, per-group tokens and freeze_ns are P1-OWNED
            process-control journal facts

THE PUBLICATION BOUNDARY IS ABSOLUTE AND IS A TEST OBLIGATION (row 101).
None of the journal state may reach a peer artifact, an acceptance predicate,
a qualification, a comparison, a Q fact, a C fact, or any published record.
A build in which any of it does FAILS (L8, ND-1..ND-3, invariant 89).

TWO EXECUTION SITES, ONE CALLER. Site (a) is the supervisor's ROUTE-D and
ROUTE-W, which reach every group stop through SIGNAL_GROUP and may not bypass
it. Site (b) is this classifier. BOTH sites' _killpg executes in the PCS root
and nowhere else. TWO SITES ARE NOT TWO CALLERS; S-12 is retained unchanged.
```

### §H3.3 Group-stop authority — who may do what

```text
                      MAY EXECUTE A     MAY WRITE A FREEZE   MEDIATED BY
                      FREEZE GROUP STOP OBSERVATION          SIGNAL_GROUP
  watchdog            NO, on any path   NO, on any path      n/a
  supervisor          yes, site (a)     YES — the sole       YES, always
                                        writer of
                                        t-freeze-observation.v1
  PCS classifier      yes, site (b)     NO — no peer class   no, it IS the PCS
  anything else       NO                NO                   n/a

killer == SUPERVISOR on every reachable path. The enum {WATCHDOG, SUPERVISOR}
is RETAINED; WATCHDOG is unreachable BY CONSTRUCTION, not by deletion, so a
stale or forged object is REJECTED at conjunct 8 rather than being unparseable.
A FIXTURE THAT NARROWS THE ENUM FAILS (KW-2).
```

### §H3.4 The supervisor freeze routes — implemented as one procedure

```text
ROUTE-D  ordinary lease-deadline entry, watchdog alive and healthy
         precondition: the MANDATORY ACK DRAIN — drain the ack pipe
         nonblocking, re-read the durable lease table, and if a strictly
         greater table_seq is durable AND acked, re-evaluate against the newest
         acked row and DO NOT freeze against the superseded deadline
ROUTE-W  dead-watchdog recovery entry; drain is vacuous
         after: refuse admissions, obtain a replacement watchdog by
         SPAWN_WATCHDOG uniform with the first, await its acknowledgement, then
         settle every overdue lease. The overdue / non-overdue split is TOTAL;
         a group frozen SOLELY for watchdog replacement whose deadline has NOT
         been reached takes the swap-only carve-out and NO witness is written.

THE SIX STEPS, IDENTICAL ON BOTH ROUTES, under T_RUNTIME.lock:
  1  verify /proc/<leader>/stat start identity against the claim's
     controller_start_identity; on mismatch SKIP the group — pid reuse
  2  SIGSTOP the process group THROUGH THE SIGNAL_GROUP OPCODE. The supervisor
     executes no killpg and no kill in its own address space, on any step
  3  PROVE QUIESCENCE: enumerate recorded members and every /proc process whose
     session id or parent chain reaches a recorded member; require each absent
     or in state T or Z. Repeat at T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS up to
     T_WATCHDOG_QUIESCE_MAX_PASSES passes, issuing SIGKILL through SIGNAL_GROUP
     after the FIRST failed pass
  4  on the proving pass apply STRICT PROGRESS
  5  on exhaustion: freeze_ns = null, overrun_ns = null, quiescence = UNKNOWN
  6  the SUPERVISOR writes WATCHDOG/FREEZE/<witness_id>.json atomic no-replace,
     file fsync, parent-directory fsync, then emits the event on the pipe

STRICT PROGRESS, EXACTLY
  s = clock_gettime_ns(CLOCK_MONOTONIC)      the only clock, pinned by
                                             _CLOCK_MONOTONIC
  s >  deadline_ns  -> PROVED, overrun_ns = s - deadline_ns, strictly positive
  s == deadline_ns  -> re-sample up to QC-1 times at QC-2, RE-PROVING
                       quiescence each pass; first s > deadline_ns with
                       quiescence still proved -> PROVED
  exhausted         -> freeze_ns null, overrun_ns null, quiescence UNKNOWN
  THERE IS NO ZERO-OVERRUN BRANCH, NO TOLERANCE CONSTANT, AND NO VALID TERMINAL
  REACHABLE FROM ANY FREEZE.
  freeze_ns is the conservative instant the whole declared tree is proved
  stopped or dead. IT IS NEVER THE SIGNAL-SEND TIME.
```

---

## §H4. The transformation oracle — the one thing that may actually be built

Implements binding §2A. `src/philosophia/officina/p1_wb_oracle.py`.

```python
# Signature surface, normative for this handoff.

class WatchdogOption(enum.Enum):
    W_A = "I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES"
    W_B = "I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS"

class OracleFinding(enum.Enum):
    PO_1_BODY_MARKERS_PRESENT        = "PO-1"
    PO_2_NONGUARD_MARKERS_PRESENT    = "PO-2"
    PO_3_GUARDDATA_PERTURBED         = "PO-3"
    PO_4_REJECTED_CAPABILITY_PRESENT = "PO-4"
    PO_5_WB_INVARIANT_ABSENT         = "PO-5"
    PO_6_OPTION_SET_DAMAGED          = "PO-6"

@dataclasses.dataclass(frozen=True)
class OracleReport:
    option: WatchdogOption
    findings: tuple[tuple[OracleFinding, str], ...]   # (code, locus)
    body_marker_counts: tuple[int, int]               # (W-A, W-B)
    nonguard_marker_counts: tuple[int, int]
    guarddata_marker_counts: tuple[int, int]
    tagged_digests: Mapping[str, str]                 # every value carries the
                                                      # test-only tag, §H4 R-4
    @property
    def conforming(self) -> bool: ...

def resolve_in_memory(composite_bytes: bytes,
                      option: WatchdogOption) -> bytes: ...

def check_resolved(resolved: bytes,
                   original_guarddata: bytes,
                   option: WatchdogOption) -> OracleReport: ...
```

```text
ORACLE RULES, MECHANICALLY ENFORCED BY ITS OWN TESTS
  R-1  resolve_in_memory returns bytes. IT HAS NO PATH PARAMETER AND NO WRITE
       PATH. The module imports no writer from canonical.py — not
       atomic_create, not atomic_replace, not fsync_directory.
  R-2  the module performs no os.fork, posix_spawn, kill, killpg, signal,
       socket, pipe, prctl or wait call, and reads no /proc entry for a live
       process. A static AST assertion in the test bundle proves it.
  R-3  it samples no clock and draws no entropy. No time, no random, no
       secrets, no os.urandom.
  R-4  EVERY digest it reports is a string of the form
         "<64 hex> test-only/non-installed/non-authoritative"
       Emitting a bare 64-hex digest is a defect, because a bare value could be
       pasted into a manifest.
  R-5  it is deterministic and total: same input bytes, same output bytes.
  R-6  it exports no symbol that any module under scripts/ imports, and no
       production root imports it. A test asserts the import graph.
```

**Region extraction.** The oracle extracts `BODY`, `GUARDDATA` and
`PROVENANCE` by the §P1-14.0 sentinel algorithm — it does **not** hard-code the
line numbers in binding §2.1, which are authoring aids and would silently
mis-slice a resolved file.

---

## §H5. The declarative contract surface

`src/philosophia/officina/p1_wb_contract.py`. **Pure data. No I/O, no syscall,
no clock, no import beyond `enum`, `dataclasses`, `typing`, `__future__`.**

```text
ENUMS AND CONSTANTS TO DECLARE, WITH THEIR EXACT MEMBERS

  Killer                     WATCHDOG, SUPERVISOR        both retained (KW-2)
  Quiescence                 PROVED, UNKNOWN
  UnknownReason              EVIDENCE_ABSENT, EVIDENCE_UNVERIFIABLE,
                             FREEZE_INSTANT_UNKNOWN
  FreezeRoute                ROUTE_D, ROUTE_W            exhaustive, no third
  FreezeExecutionSite        SUPERVISOR_MEDIATED, PCS_CLASSIFIER  exactly two
  ReapOutcome                REAPED_POSITIVE, CONTRADICTED_ECHILD,
                             STRUCTURAL_VIOLATION, NOT_YET

  WATCHDOG_DESCRIPTOR_SET    frozenset({0,1,2,3,4,5,7,8,9,10})
  WATCHDOG_CLOSED_SLOTS      frozenset({6})
  WATCHDOG_SEALED_PIPES      2

  REJECTION_CONJUNCT_RANGE   0..10 inclusive; 0 is the ABSENT sentinel

INSTALL FAILURE CODES — the closed set of 25 (FC-1). No build may add, rename
or merge one. MEMBER_EXTRA IS RETIRED and must not appear.
  STAGE_A_ABSENT                 STAGE_A_MALFORMED
  STAGE_A_OPTION_INVALID         STAGE_A_KEY_MALFORMED
  STAGE_A_PRESELECTION_MISMATCH  STAGE_A_BINDING_MISMATCH
  STAGE_B_ABSENT                 STAGE_B_MALFORMED
  STAGE_B_SIGNATURE_ABSENT       STAGE_B_SIGNATURE_INVALID
  STAGE_B_ALGORITHM_INVALID      STAGE_B_STAGE_A_MISMATCH
  STAGE_B_OPTION_MISMATCH        STAGE_B_INSTALL_ID_MISMATCH
  STAGE_B_GOVERNING_MISMATCH
  INSTALL_RECORD_ABSENT          INSTALL_RECORD_NAME_MISMATCH
  INSTALL_RECORD_REPLAYED
  MEMBER_OMITTED                 MEMBER_STALE
  MEMBER_SUBSTITUTED
  MANIFEST_VALUE_MISMATCH        ATTESTATION_MISMATCH
  HISTORICAL_BYTE_MOVED          PROCEDURE_VIOLATION_OBSERVED
The refusal envelope is the constant "WATCHDOG_AUTHORITY_INSTALL_INCOMPLETE"
plus EXACTLY ONE reason code naming the first failing check and the offending
path.

SCHEMA KEY SETS TO DECLARE AS FROZEN SETS — declared, never written
  t-freeze-observation.v1              §A4
  t-freeze-fallback-observation.v1     §A6, seventeen keys, listed there
  t-p1-test-bundle-digest.v1           MS-6
  t-watchdog-authority-test-attestation.v1   MS-7, exactly ten keys

FORBIDDEN — DO NOT DECLARE ANY OF THESE
  t-wd-freeze.v1 and every field of it
  any slot-6 socket type, socketpair or SOCK_SEQPACKET constant
  attested_pid, attested_pgid, or any identity-observation field — SEE §H8
  MEMBER_EXTRA
  any member count other than 69, and any MS-2 cardinality other than 55
```

---

## §H6. Canonical serialization and hashing

```text
CANON        the existing src/philosophia/officina/canonical.py functions.
             DO NOT REIMPLEMENT THEM AND DO NOT EDIT THAT FILE — it is one of
             the four digest-bound MS-13 modules.
OBJECT KEYS  sorted. No space outside a string literal. Exactly one trailing
             0x0A. Bytes are byte-identical to CANON of the parsed value (MS-0,
             VP-1 S6).
DIGESTS      SHA-256 over WHOLE FILE BYTES AS FOUND ON DISK. No normalization,
             no line-ending translation, no whitespace or comment stripping, no
             compilation, no region exclusion. THE DIGEST IS OF BYTES, NEVER OF
             AN AST.
ARRAYS       stated cardinality, element shape, order or sortedness, and
             pairwise distinctness are all CK-8 predicates. Swapping two
             elements produces a different digest and is A REFUSAL, NOT A
             NORMALIZATION.
INTEGERS     strict int. version is the INTEGER 1 — not "1", not 1.0.
REGIONS      H_BODY, H_GUARDDATA and H_NORMATIVE are extracted by the §P1-14.0
             sentinel algorithm and by no other means.
```

---

## §H7. Restart and crash-cut behaviour

```text
CC-1  FAIL CLOSED, NEVER GUESS. On a malformed singleton record — schema value,
      key set, value type, enum value, hex grammar or timestamp grammar wrong;
      or not a regular file; or link count != 1; or resolving through a symlink
      — REFUSE with retryable false; unlink nothing; kill nothing; release no
      live process. THE CONTRACT NEVER GUESSES AT AN AMBIGUOUS SINGLETON
      RECORD.

CC-2  PID REUSE IS NOT LIVENESS. A recorded process that is live with a
      DIFFERENT start identity is treated as NOT LIVE and IS NEVER KILLED.

CC-3  ADOPT-OR-REFUSE. A present, well-formed record whose process is live with
      the same spawning_id and byte-identical to what this attempt would
      install is ADOPTED, not rewritten. Otherwise REFUSE with retryable true;
      unlink nothing; kill nothing.

CC-4  A LOST OBSERVATION IS NEVER RECONSTRUCTED. There is exactly one writer —
      the supervisor — so the object is absent only when the supervisor did not
      write it. On absence take the §A6 ABSENT fallback with
      rejection_conjunct = 0, rejected_witness_path_or_null = null,
      rejected_object_sha256_or_null = null, and process_id NON-NULL.

CC-5  A REJECTED OBJECT IS NEVER OVERWRITTEN, TRUNCATED, RENAMED OR DELETED to
      make room (KW-3).

CC-6  RECORD REMOVAL ORDER is exactly §P1-11.3: each unlink followed by an
      fsync of the parent directory, ENOENT tolerated.

CC-7  NOTHING DEGRADES TO A PRIOR BEHAVIOUR ON REFUSAL. No process is created,
      no handle allocated, no freeze route reachable, no evidence accepted, no
      settlement run. Recovery is to complete OR-1..OR-11 and re-run the check;
      THERE IS NO OTHER RECOVERY.

CC-8  DOUBLY DETACHED DESCENDANTS ARE THE DECLARED A3 RESIDUAL. No cgroup, PID
      namespace or PR_SET_CHILD_SUBREAPER is available. The fail-closed
      quiescence scan detects the escape and routes to unknown recovery RATHER
      THAN PRETENDING THE GROUP STOP COVERED IT. Do not "fix" this.
```

---

## §H8. Identity — the exclusion, restated where the implementer will look

```text
DO NOT WRITE IDENTITY-OBSERVATION CODE. NOT ENABLED, NOT DISABLED, NOT GATED,
NOT FEATURE-FLAGGED, NOT STUBBED, NOT DUMMY-TESTED, NOT COMMENTED IN.

  no attested_pid, no attested_pgid, no field, key, enum member, dataclass
  attribute, parameter, constant or test fixture representing either

WHY, IN ONE LINE THE IMPLEMENTER CAN CHECK: the strings attested_pid and
attested_pgid occur ZERO times in composite v1.10 and ZERO times in amendment
v1.7. There is no schema to conform to.

Composite §P1-13.2 row 2 states the conflict, states that two coherent repairs
exist, that choosing between them CHANGES SIGNED MEANING, and — verbatim —
"This document chooses neither and invents no value."
WRITING THE CODE WOULD CHOOSE. Amendment XS-1(b) requires the later combined
binding to record acceptance of P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1
OR REFUSE TO PROCEED. That token is NOT ACCEPTED.

THE W-B ROUTE DOES NOT NEED IT. §P1-10.7 computes the classifier's scope from
the PCS's OWN HANDLE TABLE. The opaque handle_id remains the only addressable
process name. Excluding identity code costs the W-B implementation nothing.

IF A FUTURE CHANGE ADDS SUCH A SURFACE, the verifier obligation of §H10 applies
and it REFUSES BEFORE ANY PRODUCTION ACTION.
```

---

## §H9. Test matrix

### §H9.1 Isolation rules — absolute

```text
I-1  NO REAL PROCESS-CONTROL SMOKE IN THE SHARED RUNTIME TREE. No test may
     fork, exec, posix_spawn, signal, killpg, wait on, or /proc-inspect a live
     process inside successor/officina/runtime/ or any shared runtime path.
I-2  DISPOSABLE INTEGRATION TESTS USE AN ISOLATED TEMPORARY ROOT ONLY, created
     by tempfile.mkdtemp and removed in a finally block. Never a fixed path,
     never a path derived from the repository root.
I-3  TEST-ONLY CAPABILITIES ONLY, and NO PRODUCTION ARTIFACT NAMES. A fixture
     may not be named P1_WATCHDOG_FREEZE_SELECTION_V1.json, may not be written
     under an INSTALL directory, and may not carry a real schema literal in a
     position where a scanner could mistake it for an installed object.
I-4  TEST-ONLY KEYS AND SEEDS ARE MECHANICALLY UNABLE TO PRODUCE A PRODUCTION
     ARTIFACT. Every fixture key is a fixed, committed, obviously-fake constant
     documented as such. NO KEY GENERATION OF ANY KIND RUNS IN THE TEST SUITE —
     no Ed25519 keygen, no os.urandom, no secrets. A static assertion proves
     the suite calls no key-generation primitive.
I-5  NO NETWORK, NO CLOCK DEPENDENCE, NO ORDERING DEPENDENCE BETWEEN TESTS.
```

### §H9.2 Unit tests

```text
U-1   the 20-locus resolution table of binding §2.2 is reproduced mechanically
      from the composite bytes: 20 marker lines, 13/13 markers, and the
      3 / 16 / 1 preamble / body / guarddata split
U-2   PO-1: zero VARIANT_MARKER matches in NORMALIZE(REGION(BODY)) of the
      resolved bytes
U-3   PO-2: zero matches over the whole resolved file MINUS GUARDDATA — the
      strictly stronger check that closes binding §2.3 E-1
U-4   PO-3: H_GUARDDATA equals
      faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
      and both patterns are still present there exactly once each
U-5   PO-4: the W-A option token, P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1 and
      t-wd-freeze.v1 occur zero times; slot 6 occurs ONLY in its CLOSED sense
U-6   PO-5(a): the descriptor set resolves to {0,1,2}∪{3,4,5,7,8,9,10}
U-7   PO-5(b)(c): property 12 and §P1-10.6 read the W-B text with no marker
U-8   PO-5(d)(e): the §P1-10.7 TRIGGER and row 89 site (b) name the
      endpoint-loss site and nothing else
U-9   PO-6: TS-1 still carries BOTH literal option tokens as the option set
U-10  PO-7: H_GUARDDATA unchanged while H_BODY, H_NORMATIVE and H_FILE differ
      from the pre-resolution values
U-11  the four both-marker lines (2277, 6363, 6391, 6402) are EDITED IN PLACE,
      not deleted — a deletion strategy is caught here
U-12  the 25-code failure set is exactly 25, contains no MEMBER_EXTRA, and each
      code maps to exactly one owning check
U-13  the killer enum retains BOTH values; a fixture narrowing it FAILS (KW-2)
U-14  rejection_conjunct range 0..10 with 0 as the ABSENT sentinel; process_id
      non-null on EVERY fallback branch including ABSENT (FB-4)
U-15  current_unresolved_member_count and unresolved_member_count are distinct
      keys, never equated, renamed into one another, or substituted (FB-3)
U-16  the oracle emits no bare digest: every reported digest carries the
      test-only tag (§H4 R-4)
```

### §H9.3 Adversarial tests — each must FAIL the build if it passes silently

```text
A-1   a resolved file with ONE surviving [W-A] marker in BODY            -> PO-1
A-2   a resolved file with a surviving marker in the PREAMBLE only —
      G-10 does NOT catch it; PO-2 MUST                                 -> PO-2
A-3   a "resolution" that DELETED the guarddata patterns                -> PO-3
A-4   a resolved file retaining the W-A branch at any of the 16 body loci-> PO-4
A-5   a resolved file granting the watchdog a slot-6 socket             -> PO-4
A-6   an observation with killer == WATCHDOG, on any path               -> A5
      conjunct 8, permanently non-evidence, rejection_conjunct = 8
A-7   an attempt to re-enter WATCHDOG by default, migration, shim, recovery,
      archival re-import, takeover re-derivation or fixture               -> KW-1
A-8   a freeze observation written by any process other than the supervisor
A-9   a group stop for a freeze from any site other than the two signed ones
A-10  classifier journal state reaching a peer artifact, acceptance predicate,
      qualification, comparison, Q fact, C fact or published record       -> row
      101, L8, ND-1..ND-3
A-11  a watchdog code path that writes, signals, freezes or sends on EOF
A-12  a watchdog code path using getppid() to infer supervisor death
A-13  a member enumeration of 59 or 73 instead of 69 — the deferred MS-2 rows
      treated as members. MUST FAIL. See binding §5.1 PR-4
A-14  an MS-2 cardinality other than 55
A-15  a test that creates a file at any frozen path of §H1.2
A-16  a test that calls a key-generation primitive                       -> I-4
A-17  freeze_ns <= deadline_ns, or a zero-overrun branch                 -> KW-3
A-18  a synthesized freeze instant, or an overrun_ns on a fallback       -> FD-1
```

### §H9.4 Multi-fault tests

```text
M-1   THE ORDER-DECIDING FIXTURE, carried verbatim from packet §3.2. M4 is
      structurally perfect, its reachable_closure is factually wrong in exactly
      one row's kind (FROZEN -> PURE_PYTHON), AND Stage A's file digest
      disagrees with M4.stage_a_sha256.
        CK-7   no M4 field is read
        CK-8   accepts — the structure is perfect
        CK-9   REFUSES.  FIRST CODE: STAGE_A_BINDING_MISMATCH
        CK-10  NEVER REACHED
      REMOVE THE STAGE-A FAULT and the same manifest refuses at CK-10 with
      MANIFEST_VALUE_MISMATCH.
      A FIXTURE EXPECTING MANIFEST_VALUE_MISMATCH FOR THE TWO-FAULT STATE
      FAILS. A FIXTURE EXPECTING ANY CODE AT CK-7 FOR EITHER STATE FAILS.
M-2   marker present AND guard data perturbed: both PO-1 and PO-3 report; the
      report is not truncated at the first finding
M-3   watchdog unreaped AND a live overdue group: WATCHDOG_UNREAPED routes to
      §P1-11.6 and the overdue group is not silently dropped
M-4   ack absent AND a strictly greater durable acked table_seq: the ROUTE-D
      drain wins and no freeze is issued against the superseded deadline
M-5   pid reuse AND a malformed singleton: CC-1 refuses first, and nothing is
      unlinked or killed
```

### §H9.5 Disposable integration tests

```text
D-1   in a temporary root, the oracle round-trips real governing bytes: read
      copies, resolve W-B in memory, check PO-1..PO-6, assert the temporary
      root is EMPTY at the end and that no path under successor/ was opened for
      writing
D-2   an import-graph assertion: no production root imports p1_wb_oracle or
      p1_wb_contract; neither module imports a writer from canonical.py
D-3   a static AST assertion over both new modules: no fork, posix_spawn, kill,
      killpg, signal, socket, pipe, prctl, wait-family call, no subprocess, no
      clock sample, no entropy draw
D-4   a filesystem-negative assertion: running the whole new suite leaves the
      repository working tree byte-identical except for the temporary root,
      which no longer exists
```

### §H9.6 Rows 92..115 are NOT implemented here

```text
The 24 test rows of §P1-15 belong to the two MS-6 modules, which OR-5 creates
and OR-7 runs. THIS HANDOFF CREATES NEITHER MODULE AND NO test_p1_row_NNN_
FUNCTION. Creating one would place a file at a member path before OR-3 exists
and would make the membership rule of MS-6 evaluable against a file that is not
M6. Rows 92..115 are recorded here as the future obligation they are, and the
inactive suite must contain NO function whose name begins with "test_p1_row_".
```

---

## §H10. Verifier behaviour while inactive

```text
V-1  FAIL CLOSED BEFORE ANY PRODUCTION ACTION. Any production entry point
     reached while the install is incomplete REFUSES with
     "WATCHDOG_AUTHORITY_INSTALL_INCOMPLETE" and exactly one reason code naming
     the first failing check and the offending path.

V-2  IN THE CURRENT STATE THE FIRST FAILING CHECK IS DETERMINATE AND SHOULD BE
     ASSERTED AS SUCH. Stage A does not exist at TS-1's literal path, so CK-2
     refuses with STAGE_A_ABSENT. Every later check is unreachable. A test
     asserting a different first code in the current state is wrong.

V-3  ON REFUSAL: no process is created, no handle is allocated, no freeze route
     is reachable, no evidence is accepted, no settlement runs, and NOTHING
     DEGRADES TO A PRIOR BEHAVIOUR.

V-4  THE INACTIVE MODULES ARE NOT A VERIFIER. p1_wb_oracle and p1_wb_contract
     are not M5, are not installed at MS-5's path, and must never be invoked by
     a production entry point. The real verifier is written at OR-5 under a
     separate authorization.

V-5  IF AN IDENTITY-OBSERVATION SURFACE IS EVER ADDED, the active verifier
     REFUSES until the separately reviewed
     P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1 is accepted and bound.
     Under this handoff the surface does not exist, so the refusal is
     unreachable and the feature is disabled by ABSENCE, which is the strongest
     form consistent with the selected Option A contract.

V-6  DO NOT IMPLEMENT G-11 OR CK-1..CK-15 UNDER THIS HANDOFF. They are OR-5
     work. §H12 F1 records an unresolved contradiction about their range that
     must be settled before anyone implements them.
```

---

## §H11. The existing working-tree implementation — audit obligation

The working tree already contains Cursor implementation work. **None of it is
governing evidence for this contract, and none of it may be adopted, extended
or overwritten under this handoff.**

```text
UNTRACKED
  src/philosophia/officina/generic_harness.py     2380 lines
  tests/test_officina_generic_harness.py          2007 lines
MODIFIED, UNRELATED TO P1
  src/philosophia/officina/accounting.py          +115 lines
  tests/test_officina_accounting.py               +264 lines
  ten review/prompt files under reviews/
UNTRACKED, UNRELATED
  essay/OUTLINE.md
  reviews/opus5_officina_supervisor_p1_operative_composite_v1_repair_chat_response.md

DISPOSITION
  DO NOT EDIT ANY OF THEM. DO NOT REVERT ANY OF THEM. DO NOT STAGE OR COMMIT
  ANY OF THEM. The accounting.py and reviews/ changes are unrelated work and
  must survive this handoff untouched.

THE ONE FACT THAT MATTERS AND IS NOT AN OPINION.
  src/philosophia/officina/generic_harness.py IS P1 PRODUCTION ROOT #3, and its
  current untracked bytes do NOT satisfy the P1 contract:
      line  21  import subprocess
      line 408  def start(...) -> "subprocess.Popen[bytes]"
      line 411  subprocess.Popen(list(argv), start_new_session=True)
      line 415  os.kill(pid, 0)
      line 424  os.killpg(process_group_id, 15)
  §P1-3.2 gives that exact path a SCOPED 16-member allowlist that EXCLUDES
  subprocess, and S-12 requires that subprocess, Popen, fork, waitpid, kill,
  killpg and system appear on NO PATH of that file.

  THIS IS NOT A BUG IN THAT FILE. Its docstring says it implements the generic
  metered harness chain v1..v2.3.1 plus the batch settlement amendment, and
  §P1-3.2 records that the accepted generic-harness chain GENUINELY DOES grant
  a subprocess launcher capability with start_new_session=True and os.killpg.
  P1 SUPERSEDED THAT LAUNCH ROUTE; the file predates the supersession. It
  conforms to its own lineage and does not conform to P1.

CONSEQUENCE — A FRESH AUDIT IS MANDATORY BEFORE ANY REUSE
  A-1  no line of that file may be copied into a P1 module without being
       re-derived from the v1.7/v1.10 bytes
  A-2  its test module proves nothing about P1 conformance and may not be cited
  A-3  bringing that path into P1 conformance is OR-5-era work under a separate
       authorization, and it is NOT in this handoff's scope
  A-4  the audit must be recorded as its own reviewed artifact before any P1
       code reuses it; an informal reading does not discharge A-1
```

---

## §H12. The fenced gap — the one place where §H0 R-2 bites

```text
F2, FROM BINDING §5.2. THE CLASSIFIER SCOPE PREDICATE IS NOT IMPLEMENTABLE.

  §P1-10.7 SCOPE and §P1-15 row 89 site (b) both require KV-1..KV-6 to be
  re-evaluated before EVERY _killpg. The token "KV" occurs exactly twice in
  composite v1.10 — those two references — and ZERO times in amendment v1.7 and
  ZERO times in packet v2.10. THE SIX RULES ARE DEFINED NOWHERE IN THE
  GOVERNING PAIR.

  A full definition survives at §3.4 of
    successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
  which is a SUPERSEDED packet draft, a member of nothing, not the governing
  packet, and NOT OPENED FOR BEHAVIOUR.

  DO NOT IMPLEMENT THE SCOPE PREDICATE. DO NOT COPY IT FROM THE SUPERSEDED
  PACKET. DO NOT RECONSTRUCT IT FROM AN EARLIER COMPOSITE. DO NOT INFER IT.

  WHAT MAY STILL BE BUILT AROUND THE GAP: §H3.2's actor, trigger, record-first
  ordering, mediation, evidence and publication constraints are all fully
  stated in the governing bytes and are implementable now. Only the per-group
  kernel verification is fenced.

  WHY IT MATTERS RATHER THAN BEING PEDANTRY: KV-6 is what stops the classifier
  from signalling the PCS's own group, a watchdog leader group or the
  supervisor group. Guessing it is the one guess that could produce a
  self-directed group stop.

  RESOLUTION PATH: it is the second bounded X/Y question of the companion
  closure. Until an X/Y round rules on it, the scope predicate has no
  implementation authorization even if every other gate opens.
```

---

## §H13. Evidence that `T` remains `NOT_ACTIVATED`

The implementer asserts each of these mechanically, and the assertions are part
of the inactive suite.

```text
E-1  successor/officina/authorization/ DOES NOT EXIST. No Stage A.
E-2  successor/officina/runtime_control/ DOES NOT EXIST. No INSTALL directory,
     no M4, no M7, no Stage B, no detached signature, no install record.
E-3  src/philosophia/officina/verification.py is the PRE-INSTALL BASELINE, not
     M5. Its baseline digest appears in MS-2 nowhere and is compared by nothing.
E-4  tests/test_officina_p1_freeze_authority.py and
     tests/test_officina_p1_install_integrity.py DO NOT EXIST, so M6 does not
     exist and no row 92..115 has run.
E-5  no function named test_p1_row_NNN_ exists anywhere in the repository.
E-6  scripts/officina_process_control_bootstrap.py and
     scripts/officina_role_bootstrap.py DO NOT EXIST — three of the five
     production roots are absent.
E-7  no Ed25519 key, key_id or public_key_hex exists anywhere in the tree.
E-8  the string
     I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7
     occurs in EXACTLY ONE signature file —
     successor/OFFICINA_P1_WATCHDOG_FREEZE_SELECTION_V1_SIGNATURE.md — and
     there it occurs under the heading "The following acceptance token remains
     UNSIGNED". THE ASSERTION IS NOT "the string is absent"; it is that its
     ONLY occurrence in a signature is as an explicitly unsigned token, and
     that no signature file contains it as a signed or emitted token. An
     implementer writing this assertion as a bare absence check WILL GET A
     FALSE FAILURE.
E-9  the composite at MS-1's second literal path still contains 20
     marker-bearing lines and 13/13 markers — OR-4 HAS NOT RUN.
E-10 the amendment and composite digests still equal the §0.2 values of the
     binding — no governing byte moved.
E-11 no process, socket, pipe, fork, exec, signal, wait or prctl operation was
     performed by anything in this suite.

     T = NOT_ACTIVATED       PROGRAMME CLAIM = OPEN
```

---

## §H14. Negative space

This handoff creates nothing executable. It authorizes no code, no test, no
test execution, no commit, no key, no entropy, no artifact, no signature, no
manifest, no attestation, no install record, no resolved amendment or composite
at any path, no OR step, no install, no activation, no process-control
operation, no candidate, learner, world, trajectory, spend, datum, outcome,
Proof or claim movement.

**No existing file was modified in producing it.** The untracked
`generic_harness.py` was read only to establish the §H11 audit facts; it was
not adopted as evidence, not extended and not edited.

Every author closure, including the companion to this handoff, is an untrusted
self-assessment and is normative for nothing.
