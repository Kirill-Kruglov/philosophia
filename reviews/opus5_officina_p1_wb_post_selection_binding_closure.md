# Officina P1 W-B post-selection binding — author closure

**Author:** Claude Code Opus 5, post-selection binding author. **Not an
independent X-line or Y-line reviewer.** This closure is an **untrusted
self-assessment and is normative for nothing.** It selects nothing, accepts
nothing, authorizes nothing and executes nothing.

Base commit `6306e28`. `T = NOT_ACTIVATED`; programme claim `OPEN`.

---

## §1. Closure

```text
READY_FOR_OFFICINA_P1_WB_BINDING_XY_REVIEW
```

**Why this token and not one of the other three, stated so a reviewer can
overturn it deliberately.**

```text
NOT BLOCKED_PENDING_IDENTITY_WEAKENING_REVIEW.
  The governing bytes DO require a boundary stricter than the task's proposed
  fail-closed minimum — §4 below — but they require it by EXCLUSION, not by
  blockage. The identity-observation surface is not "code that must be kept
  disabled"; it is a surface the governing pair does not define at all
  (attested_pid and attested_pgid occur ZERO times in both files), and the W-B
  route provably does not need it, because §P1-10.7 computes scope from the
  PCS's own handle table. Excluding it costs the W-B implementation nothing and
  invents nothing. Blocking the whole binding on it would withhold reviewable
  work the selection signature expressly authorized preparing, and would
  conflate the watchdog cell with the identity cell that N-4, N-13 and XS-1
  keep separate. THE COMBINED BINDING OF XS-1 IS SEPARATELY RECORDED AS
  BLOCKED_PENDING_IDENTITY_WEAKENING_REVIEW in the ledger at §4 — as a state of
  a document that does not exist, not as this task's closure.

NOT REVISE_OFFICINA_P1_WB_BINDING.
  The two Major findings at §7 are defects in the GOVERNING PAIR, not in the
  binding. Revising the binding would not touch them.

NOT BLOCKED_OFFICINA_P1_WB_BINDING.
  The W-B/rejected-W-A resolution is fully determinate from the bytes — all 20
  loci, 13/13 markers, no residue of judgement. The binding is complete and
  reviewable. One implementation function is fenced (§7 F2); that is a gate on
  a function, not on the binding.

A REVIEWER WHO JUDGES THAT F2 ALONE SHOULD GATE THE WHOLE HANDOFF, OR THAT THE
IDENTITY CELL SHOULD BLOCK RATHER THAN EXCLUDE, SHOULD SAY SO — THOSE ARE THE
TWO PLACES THIS CLOSURE IS MOST LIKELY TO BE WRONG.
```

### §1.1 Deliverables

```text
successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V1_DRAFT.md
successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V1_DRAFT.md
reviews/opus5_officina_p1_wb_post_selection_binding_closure.md   (this file)

EXACTLY THREE FILES CREATED. NO EXISTING FILE MODIFIED. NOTHING COMMITTED.
```

### §1.2 Governing hashes, recomputed from disk

```text
ffcb4116a9171d873be773138cc2c97547f8ff919a1d71f4cbd46e328eb3a7dc  successor/OFFICINA_P1_WATCHDOG_FREEZE_SELECTION_V1_SIGNATURE.md
06aa44fbe3221c9d41484e14fa2a31df42ce58ae17c8b899278b0bf6c5608e9d  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_10_CORRECTION.md
4b7442bd1dafa1ff141212ac8cd59e94983f32633561b6396837ff0767aa48ff  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7_DRAFT.md
86755531f5a7a5f11085802c3e6b5770f4ef5aa90d98ae1a62599348e11f0e8f  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_10.md
0998fce3b881e0d0d1947c450b442821047f040a4bdd4a987a1a091ece3a56f7  reviews/fable_officina_p1_watchdog_v2_10_targeted_x_confirmation.md
90fb9f9155926df89e9993de1146c05e279639469d7bf2a60c63c6419bc37e52  reviews/sol_officina_p1_watchdog_v2_10_targeted_y_confirmation.md
7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md

ALL FIVE HASHES NAMED IN THE TASK MATCHED. The identity-selection digest
additionally matched the value XS-1 carries in the amendment bytes.

THE THREE NEW FILES CARRY NO DIGEST OF THEMSELVES and no digest of each other,
so no two copies of a value can disagree.
```

---

## §2. Complete W-B / rejected-W-A resolution matrix

```text
SELECTED    W-B  I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
            with P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1
REJECTED    W-A  I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
            with P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1
```

### §2.1 The census, recomputed rather than read

```text
marker-bearing lines, composite v1.10        20
marker-bearing lines, amendment v1.7          0   ← OR-4 edits ONE file
"[W-A]" occurrences                          13
"[W-B]" occurrences                          13
lines carrying BOTH markers, WHOLE FILE       6   (83, 2277, 6363, 6391, 6402,
                                                   6501)
lines carrying BOTH markers, BODY ONLY        4   (2277, 6363, 6391, 6402)
  ← the four that must be EDITED IN PLACE at OR-4. Line 83 is preamble and is
    DELETED; line 6501 is guard data and is RETAINED. A reviewer recomputing
    this over the whole file gets 6, not 4, and the qualifier is why.
```

### §2.2 The three-region split — the finding a reviewer should check first

The twenty loci are **not one population**, and this is the load-bearing
structural result of the binding.

```text
REGION      SENTINEL RANGE   LINES  A   B   OR-4 ACTION
  PREAMBLE   1..247             3    2   2   DELETE (notation + discharged
                                              blocking notice; NOT branches)
  BODY       249..6460         16   10  10   RESOLVE to [W-B], delete [W-A]
  GUARDDATA  6464..6503         1    1   1   RETAIN BYTE-IDENTICAL
                                       ---
                                  20 13  13

TWO CONSEQUENCES THAT DO NOT FOLLOW FROM READING OR-4 LITERALLY:

  (i)  G-10 matches ONLY NORMALIZE(REGION(BODY)). Lines 79, 80 and 83 sit
       BEFORE OFFICINA-P1-BODY-BEGIN at line 248. A resolution that edits only
       the 16 body loci SATISFIES OR-4's stated success condition — "After this
       step G-10 finds zero markers" — WHILE LEAVING THE CELL-2 BLOCKING NOTICE
       AND THE NOTATION DEFINITION IN THE FILE, still telling the reader the
       cell is unsigned and the document not operative, all covered by H_FILE.
       The binding adds PO-2, a strictly stronger whole-file-minus-guarddata
       check, to close this.

  (ii) Line 6501 is the SOURCE of G-10's two patterns and is never a match
       target. An implementer told "delete every marker" destroys the guard
       permanently AND moves H_GUARDDATA, which G-6 then refuses. THE CORRECT
       ACTION AT 6501 IS TO CHANGE NOTHING.
```

### §2.3 The 20 loci

```text
#   LINE  REGION     OWNING SECTION                ACTION   WHAT W-B RETAINS
 1    79  PREAMBLE   Cell 2 blocking notice        DELETE   —
 2    80  PREAMBLE   Cell 2 blocking notice        DELETE   —
 3    83  PREAMBLE   Cell 2 blocking notice        DELETE   —
 4   302  BODY       §P1-1.3                       RESOLVE  (W-A request clause deleted)
 5   303  BODY       §P1-1.3                       RESOLVE  "The watchdog requests nothing"
 6  1653  BODY       §P1-9.2 property 11           RESOLVE  executes no freeze on any path
 7  1656  BODY       §P1-9.2 property 11           RESOLVE  (W-A G-1 rationale deleted)
 8  1663  BODY       §P1-9.2 property 12           RESOLVE  (W-A slot-6 send deleted)
 9  1667  BODY       §P1-9.2 property 12           RESOLVE  "It sends nothing"
10  1904  BODY       §P1-10.6                      RESOLVE  (W-A extra operation deleted)
11  1907  BODY       §P1-10.6                      RESOLVE  "No further operation of any kind"
12  1929  BODY       §P1-10.7 TRIGGER              RESOLVE  endpoint loss, record-first
13  1930  BODY       §P1-10.7 TRIGGER              RESOLVE  (W-A window trigger deleted)
14  2277  BODY       §P1-13.0 residence matrix     RESOLVE  "It holds no socket"   [both]
15  2560  BODY       §P1-13.2 P1 invariant         RESOLVE  TWO SEALED PIPES, slot 6 closed
16  2566  BODY       §P1-13.2 P1 invariant         RESOLVE  (W-A THREE ENDPOINTS deleted)
17  6363  BODY       §P1-15 row 61                 RESOLVE  W-B classifier terminal  [both]
18  6391  BODY       §P1-15 row 89                 RESOLVE  site (b) = endpoint loss [both]
19  6402  BODY       §P1-15 row 99                 RESOLVE  {0,1,2}+{3,4,5,7,8,9,10} [both]
20  6501  GUARDDATA  §P1-17 VARIANT_MARKER         RETAIN   both patterns, untouched
```

The four `[both]` lines must be **edited in place**; a line-deletion strategy
is wrong on its face.

### §2.4 The mechanical invariant

`PO-1` marker elimination in `BODY` (this is G-10) · `PO-2` the strictly
stronger whole-file-minus-guarddata check · `PO-3` `H_GUARDDATA` unchanged at
`faf2d709…0426` · `PO-4` rejected-branch capability absent by name, with
`slot 6` permitted **only** in its closed sense · `PO-5` the five W-B
invariants positively present · `PO-6` `TS-1`'s option **set** preserved — the
non-selected token is **not** deleted, or `IR-13` row 47 breaks · `PO-7`
`H_GUARDDATA` unchanged while `H_BODY`, `H_NORMATIVE` and `H_FILE` change, and
the §A0.4 anchor `86755531…f0e8f` is the **pre**-selection value and must never
be updated to the post-`OR-4` digest · `PO-8` the amendment carries no marker,
so `OR-4`'s marker work does not touch it.

**Common amendments bound without meaning change:**
`P1_FREEZE_ABSENT_FALLBACK_NULLABLE_IDENTITY_V1` (§A6, FB-1..FB-5 — `process_id`
non-null on **every** branch including `ABSENT`) ·
`P1_PCS_FREEZE_CLASSIFIER_V1` (§P1-10.7 — W-B fixes the **trigger only**) ·
`P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1` (common to both options, **not itself
a choice**) · `P1_FREEZE_PUBLICATION_L6_L9_V1` (§A8.2 PUB-1..PUB-4).

---

## §3. Dry-run versus `OR-4`

A **test-only, in-memory** oracle may be built and unit-tested before
acceptance. It consumes byte copies, selects W-B in memory, checks `PO-1`..`PO-6`,
and returns a value.

```text
IT MAY NOT       write any governing or runtime path; create a key, entropy,
                 Stage A, Stage B, manifest, attestation, signature or install
                 record; be production input; be OR-4 evidence; sample a clock;
                 or perform any process-control operation.
IT MUST          tag every reported digest with the literal
                 "test-only/non-installed/non-authoritative" — a bare 64-hex
                 value is a defect, because a bare value can be pasted into a
                 manifest.

WHAT AUTHORIZED OR-4 DOES THAT THE ORACLE DOES NOT
  writes resolved bytes ON DISK at MS-1's second literal path
  requires the accepted v1.7 token, a completed OR-3 with a generated key pair,
    an implementation authorization and a one-shot handoff authorization
  installs the amendment, and FIXES M1 AND ITS TWO DIGESTS
  is a precondition of OR-5..OR-11 and lands with them or not at all
  its digests are recorded in M4 at OR-6; the oracle's NEVER are
  is subject to G-10 in the shipped verifier
  IS NOT REVERSIBLE

ONE SENTENCE: the oracle rewrites a copy and returns it; OR-4 rewrites the
governing file and every later step depends on the result.

THE RESOLVED-BYTE FILES WERE NOT CREATED BY THIS TASK, at any path.
```

---

## §4. Total gate ledger and identity-token disposition

```text
 1  W-B author selection (OR-2)                    COMPLETE
 2  this post-selection binding                    DRAFT, awaiting X/Y
 3  watchdog authority amendment v1.7 acceptance   NOT ACCEPTED
 4  process identity Option A selection            COMPLETE
 5  P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1   NOT ACCEPTED
 6  the LATER COMBINED BINDING of XS-1             DOES NOT EXIST —
                                                   BLOCKED_PENDING_IDENTITY_
                                                   WEAKENING_REVIEW, by XS-1(b)
 7  inactive code/test implementation              CANDIDATE ELIGIBILITY ONLY
 8  implementation authorization                   NOT GRANTED
 9  OR-3  key generation and Stage A               NOT AUTHORIZED
10  OR-4  variant resolution, amendment install    NOT AUTHORIZED
11  OR-5..OR-9  verifier, tests, M4, M7, members   NOT AUTHORIZED
12  OR-10 Stage B and detached signature           NOT AUTHORIZED
13  OR-11 install record, no-replace, last         NOT AUTHORIZED
14  one-shot atomic-handoff authorization          NOT GRANTED
15  T activation                                   NOT AUTHORIZED

Rows 9..13 are not five independent permissions: H-1 makes the pair one
indivisible acceptance unit and H-2/H-3 make OR-1..OR-11 land together or not
at all. They are listed apart only to show that none is open.
```

### §4.1 The identity disposition, resolved from the bytes

**Question:** may the inactive implementation contain observation-only identity
code while the weakening token is unaccepted?

**Answer — stricter than the proposed fail-closed minimum:**

```text
NO CODE AT ALL. Not disabled, not gated, not flagged, not stubbed, not
dummy-tested. THE SURFACE IS OUT OF SCOPE ENTIRELY.
```

```text
THE CLAUSES
  C-1  MECHANICAL: attested_pid and attested_pgid occur ZERO times in composite
       v1.10 and ZERO times in amendment v1.7. There is no schema, key, type,
       carrier, consumer or destination to conform to.
  C-2  composite §P1-13.2 row 2 / Cell 1: two coherent repairs exist, choosing
       between them CHANGES SIGNED MEANING, and — verbatim — "This document
       chooses neither and invents no value." WRITING THE CODE WOULD CHOOSE.
  C-3  composite Cell 1: the Option A signature "does not unblock this cell and
       does not make this version operative." The blocking notice STANDS.
  C-4  amendment XS-1(b): the later combined binding must record the separate
       review and acceptance of the weakening token, OR REFUSE TO PROCEED.
  C-5  amendment N-13 / N-4: this amendment neither selects nor repairs the
       process-claim identity fields and does not become operative because an
       identity option was selected.
  C-6  identity selection signature: the bounded weakening must be reviewed and
       accepted separately before Option A can become operative.

WHY IT DOES NOT BLOCK W-B: §P1-10.7 computes the classifier's scope from the
PCS's OWN HANDLE TABLE — row 89 confirms it — and the opaque handle_id remains
the only addressable process name. THE W-B SURFACE IS IDENTITY-FREE BY
CONSTRUCTION.

THREE SEPARABLE STATES, so neither is smuggled into the other:
  the W-B binding                    NOT blocked by identity
  the W-B implementation scope       identity code EXCLUDED
  the combined binding of XS-1       BLOCKED_PENDING_IDENTITY_WEAKENING_REVIEW

THE TOKEN IS NOT TREATED AS ACCEPTED ANYWHERE, UNDER ANY NAME.
Under the handoff the feature is disabled by ABSENCE, which is the strongest
form consistent with the selected Option A contract; §H10 V-5 keeps the active
verifier's refusal obligation standing for any future surface.
```

---

## §5. Cursor implementation surface and test matrix

```text
ALLOWED PATHS — the complete list, nothing else may be created or edited
  src/philosophia/officina/p1_wb_oracle.py       the in-memory oracle
  src/philosophia/officina/p1_wb_contract.py     pure declarative surface
  tests/test_officina_p1_wb_oracle.py
  tests/test_officina_p1_wb_contract.py
  tests/test_officina_p1_wb_classifier_ordering.py
  tests/test_officina_p1_wb_negative_surface.py
  tests/test_officina_p1_wb_disposable_integration.py
  tests/fixtures/p1_wb/
  a per-test tempfile.mkdtemp root, removed by the test

FROZEN — the five §P1-3.1 production roots (two of which are ABSENT and must
NOT be created), the MS-5 baseline verification.py, both ABSENT MS-6 test
modules, all Stage A / Stage B / M4 / M7 / install paths, the four digest-bound
MS-13 modules, the governing pair, and all history.

  THE MOST LIKELY MISTAKE: creating tests/test_officina_p1_freeze_authority.py
  or tests/test_officina_p1_install_integrity.py. Those are M6 members that
  OR-5 creates. NO FUNCTION NAMED test_p1_row_NNN_ MAY EXIST; rows 92..115 are
  OR-7 work. (Verified: zero such functions exist today.)

SPECIFIED EXACTLY IN THE HANDOFF
  topology        watchdog fd set {0,1,2}∪{3,4,5,7,8,9,10}; slot 6 explicitly
                  closed; two sealed pipes; setsid False; parent is the PCS
  EOF behaviour   write nothing, freeze nothing, signal nothing, send nothing,
                  settle nothing, os._exit(0); no else-branch; getppid()
                  prohibited as a death inference
  trigger         PCS peer-endpoint loss, RECORD-FIRST, unmediated, no evidence
  authority       who may execute a group stop and who may write an observation
  routes          ROUTE-D / ROUTE-W as one procedure, six steps, mandatory
                  drain, strict progress with no zero-overrun branch
  APIs            WatchdogOption, OracleFinding, OracleReport, resolve_in_memory,
                  check_resolved; the enums, descriptor constants and schema key
                  sets of §H5
  error codes     the closed 25 of FC-1, MEMBER_EXTRA retired, refusal envelope
                  WATCHDOG_AUTHORITY_INSTALL_INCOMPLETE + exactly one code
  serialization   CANON, sorted keys, one trailing 0x0A, digests over WHOLE FILE
                  BYTES never an AST, array order a refusal not a normalization
  restart         CC-1..CC-8, including "never guess at an ambiguous singleton"
                  and the declared doubly-detached-descendant residual
  fixtures        deterministic, committed, obviously fake; NO key generation
                  primitive may be called anywhere in the suite

TEST MATRIX     16 unit · 18 adversarial · 5 multi-fault · 4 disposable
                integration.
  The order-deciding multi-fault fixture is carried verbatim: structurally
  perfect M4 + one wrong closure kind + a Stage-A digest disagreement refuses at
  CK-9 with STAGE_A_BINDING_MISMATCH, CK-10 is never reached, and a fixture
  expecting MANIFEST_VALUE_MISMATCH for that two-fault state FAILS.
  Adversarial A-2 exists specifically because G-10 cannot see a preamble marker.

ISOLATION       no real process-control smoke in the shared runtime tree;
                isolated temporary roots only; test-only capabilities; no
                production artifact names; no key generation.

VERIFIER WHILE INACTIVE
  fail closed before any production action. In the CURRENT state the first
  failing check is determinate: Stage A is absent at TS-1's literal path, so
  CK-2 refuses with STAGE_A_ABSENT and every later check is unreachable. A test
  asserting a different first code is wrong. G-11 and CK-1..CK-15 are NOT
  implemented under this handoff — see F1.

EXISTING CURSOR WORK — accounted for, not adopted, not overwritten
  generic_harness.py (untracked, 2380 lines) is P1 production root #3 and its
  current bytes do NOT satisfy P1: it imports subprocess (line 21) and calls
  subprocess.Popen(start_new_session=True) (411), os.kill (415) and os.killpg
  (424). §P1-3.2 gives that exact path a scoped 16-member allowlist EXCLUDING
  subprocess, and S-12 forbids all of those names on any path of that file.
  THIS IS NOT A BUG IN THAT FILE: it implements the generic harness chain
  v1..v2.3.1, which §P1-3.2 records as genuinely granting that launcher
  capability; P1 SUPERSEDED the launch route. It conforms to its lineage and
  not to P1.
  DISPOSITION: do not edit, do not revert, do not stage. A FRESH RECORDED AUDIT
  AGAINST THE SIGNED CONTRACTS IS MANDATORY BEFORE ANY REUSE; no line may be
  copied without re-derivation from the v1.7/v1.10 bytes, and its test module
  proves nothing about P1 conformance. The accounting.py and reviews/ changes
  are unrelated and must survive untouched.
```

---

## §6. Provenance-row disposition

The confirmed v2.10 ruling is carried unchanged: **the four deferred `MS-2`
rows are bounded accounting, not a fail-open.** `MS-2` stays 55, `MS-3` 7,
`MS-8` 69, the `TS-3` `member_count` literal 69, the composite provenance region
63 rows. `MS-2` states only that its literal list **is** `M2`, never that it
contains every superseded document; `DA-1` governs what is not opened for
behaviour, not membership. The omission is declared at `N-14` with the digests
the rows will carry, so it is auditable rather than silent.

```text
PR-1  THEY DO NOT ENTER AT OR-4, OR-6, OR-9 OR OR-11 OF THIS GENERATION.
      Adding a row during the handoff breaks CK-4's enumeration, CK-13's D1/D2
      partition, B7's member_count-is-69 check and B17 at CK-14.
PR-2  THEY ENTER AT THE FIRST ACTUAL POST-SELECTION GENERATIONAL ROUND — the
      next round that REPLACES the pair. OR-4 IS NOT SUCH A ROUND: it produces
      post-selection bytes of the SAME generation at MS-1's SAME two paths and
      replaces no document.
PR-3  THEY ENTER TOGETHER WITH THAT ROUND'S OWN FOUR ROWS, not alone; the
      arithmetic (55 -> 59 -> 63) is done once, in that round's bytes, and is
      not performed here.
PR-4  THE HANDOFF MUST NOT PRETEND THEY ARE MEMBERS. Adversarial test A-13
      fails any enumeration of 59 or 73; A-14 fails any MS-2 cardinality but 55.
PR-5  NO HISTORICAL BYTE IS EDITED. MS-2's literal list is byte-unchanged.
```

---

## §7. Findings against the governing pair — raised, not repaired

Found while building the bridge. **This author line repairs none of them and
proposes no regeneration**; v2.10's exit discipline reserves that to an
independent reviewer's counterexample.

```text
F1  MAJOR, FAIL-OPEN DIRECTION. THE TWO COPIES OF THE HANDOFF DISAGREE ON THE
    RANGE OF THE PRE-PRODUCTION CHECK.
      amendment §A9 H-3, line 1149   "it is `CK-1`..`CK-12`"
      amendment §A10                 defines CK-1 through CK-15
      amendment line 1202            "(`CK-1`..`CK-15`)"
      composite §P1-14.8 H-3         "Its fifteen checks"
      packet v2.10 §6.1              "PRE-PRODUCTION CHECKS  15  UNCHANGED"
    §A9 and §P1-14.8 EACH claim the handoff is stated "IN FULL and IDENTICALLY"
    in the other, and H-2 says "no two statements of it can disagree." The two
    blocks are NOT byte-identical (a diff shows four divergent passages) and
    they disagree here on a count.
    WHY IT IS OPERATIVE: a verifier built to §A9's range omits CK-13, CK-14 and
    CK-15 — the D1/D2 member partition with MEMBER_EXTRA retired, and CK-14,
    WHICH CARRIES B14, THE CLAUSE THAT BINDS THE SELECTED OPTION TOKEN ACROSS
    THE TWO STAGES. B14 is exactly what makes a signed W-B token bind, so this
    sits on the W-B critical path, and the omission direction is fail-open.

F2  MAJOR, BLOCKS EXACT IMPLEMENTATION OF THE W-B CLASSIFIER SCOPE.
    KV-1..KV-6 IS REFERENCED OPERATIVELY AND DEFINED NOWHERE IN THE PAIR.
      composite §P1-10.7 SCOPE and §P1-15 row 89 site (b) both require it
      "re-evaluated before every _killpg"
      "KV" occurs EXACTLY TWICE in composite v1.10 — both are these references
      — and ZERO times in amendment v1.7 and ZERO times in packet v2.10
      the only full definition survives at §3.4 of the SUPERSEDED
      OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md, a member of
      nothing, not opened for behaviour
    WHY IT MATTERS HERE SPECIFICALLY: W-B makes the PCS classifier the sole
    group-stop executor for the endpoint-loss route, and KV-6 is what stops it
    from signalling the PCS's own group, a watchdog leader group or the
    supervisor group. Guessing it is the one guess that could produce a
    self-directed group stop. The handoff FENCES the predicate at §H12.

F3  MINOR, LOG. A FIFTH GENERATION-SCOPED STRING IN AN OPERATIVE CLAUSE.
    amendment OR-4, line 3456: "the other branch is DELETED; THE V1.3 AMENDMENT
    IS INSTALLED." MS-1 names v1.7. §A9's audit enumerates "the four places a
    generation number appears in an OPERATIVE clause" and this is a fifth —
    the same class as the v2.9 X-line finding B-1, and exactly what packet §8
    item 2 predicted. MINOR because OR-4 is an operator obligation the
    final-state gate does not verify (OR-1, FS-2), and MS-1's literal paths,
    not OR-4's prose, are what CK-7 and CK-13 check. No byte state is made
    unsatisfiable. Logged because the audit's completeness claim is falsified.

F4  MINOR, LOG. composite line 90 says "(`G-10`, §P1-14.3)". G-10 is defined at
    line 2982, inside §P1-14.4 (which begins at 2941), and composite line 2923
    itself calls it "the unresolved-variant-block guard of §P1-14.4". §A9's
    audit only checks that a §P1- reference names an EXISTING heading, which
    §P1-14.3 does, so the audit passes over it. No operative ambiguity — G-10
    is reserved uniquely and unambiguous by name. Line 90 is outside
    REGION(BODY), so it is covered by H_FILE alone.
```

---

## §8. Negative authorization confirmation

Nothing in this task authorized, and nothing in it performed:

```text
no code edit, no test, no test execution, no commit, no staging
no key, entropy, seed, Stage A, Stage B, detached signature, manifest,
  attestation, member list, install record or install_record_id
no resolved amendment or composite bytes at any path — OR-4 DID NOT RUN
no amendment acceptance, no identity-token acceptance, no bounded weakening
no OR-3..OR-11 step, no install, no activation
no process, socket, pipe, fork, exec, signal, wait or prctl operation
no supervisor, PCS, controller, worker or watchdog
no freeze executed, requested, journalled or witnessed
no /proc read against a live process; no clock sampled for a contract purpose
no Philosophia production or project module imported, executed or compiled
no candidate, learner, world, trajectory, capacity artifact, custody
  disposition, result manifest, spend, E1/E2/E3, Q/C object, datum, outcome,
  Proof or programme-claim movement

NO EXISTING FILE WAS MODIFIED — no historical or governing document, no code,
no test, no signature, no runtime artifact, no prior review, and no untracked
or dirty working-tree file. Exactly three files were created. Nothing was
committed.

The untracked generic_harness.py was read ONLY to establish the §H11 audit
facts. It was not adopted as evidence, not extended and not edited.

T = NOT_ACTIVATED       PROGRAMME CLAIM = OPEN
```

---

## §9. Bounded X/Y questions

**Scope: binding correctness and implementation eligibility. This is not an
architecture review, and no question below reopens the W-A/W-B choice, the other
five signed choices, the 89-row closure, the accounting, or the recommendation.**

```text
Q1  F1 — THE HIGHEST-PRIORITY QUESTION. Is §A9 H-3's "CK-1..CK-12" an operative
    contradiction of §P1-14.8's "fifteen checks", of §A10's CK-1..CK-15, of
    line 1202 and of §6.1's count? If yes, is it a Major counterexample against
    the v2.10 governing bytes sufficient to license a v2.11 generation under
    the §0 exit discipline — noting that the omitted range contains CK-14 and
    therefore B14, the binding of the selected option token? If no, state which
    reading makes the two copies consistent.

Q2  F2 — Can KV-1..KV-6 be implemented from the governing pair alone? If not,
    is the correct repair (a) to carry the definition into the governing bytes
    in a later round, or (b) to accept that the §P1-10.7 scope predicate has no
    implementation authorization until it is? Confirm that reconstructing it
    from the superseded V2_DRAFT packet is NOT permitted under DA-1/DA-2/IR-12.

Q3  THE THREE-REGION SPLIT. Independently recompute the 20 loci, the 13/13
    markers and the 3 / 16 / 1 preamble / body / guarddata split against the
    sentinels at 248, 6461, 6463, 6504. Confirm or refute: (a) a body-only
    resolution satisfies OR-4's stated success condition while leaving the
    Cell-2 blocking notice in the file, so PO-2 is genuinely needed; (b) line
    6501 must be RETAINED byte-identical, and deleting it destroys G-10 and
    moves H_GUARDDATA.

Q4  THE IDENTITY DISPOSITION — THE SECOND PLACE THIS CLOSURE MAY BE WRONG. Is
    EXCLUSION (no identity code at all, justified by the zero occurrences of
    attested_pid/attested_pgid and by §P1-13.2 row 2's "chooses neither and
    invents no value") the correct fail-closed reading? Or does XS-1(b) reach
    this binding too and force BLOCKED_PENDING_IDENTITY_WEAKENING_REVIEW as the
    task closure? Confirm specifically that this document is NOT the "later
    combined binding" XS-1 names, and that treating it as such would be an
    error in the opposite direction.

Q5  PO-4's SLOT-6 CARVE-OUT. PO-4 bans rejected-branch capability strings by
    name, but "slot 6" must SURVIVE in its CLOSED sense (§P1-13.2's "explicitly
    closed by a file action" and row 99's descriptor set). Is the granting-clause
    versus closing-clause distinction stated precisely enough to be mechanical,
    or does it need an exact permitted-occurrence list in the governing bytes?

Q6  PO-6 AND IR-13 ROW 47. Confirm that OR-4 must NOT delete the non-selected
    option token from TS-1, because row 47 requires selected_option_token to be
    one of TS-1's TWO literal option tokens and B14 binds against that set.
    A resolution that "removes all W-A traces" from TS-1 would break it.

Q7  PROVENANCE ENTRY POINT. Is PR-2 correct that OR-4 is NOT a generational
    round — that it produces post-selection bytes of the SAME generation at the
    SAME MS-1 paths and replaces no document — so the four deferred MS-2 rows
    do not enter during the handoff? Is PR-3's "together with that round's own
    four rows" the right accounting, or should the two sets enter separately?

Q8  IMPLEMENTATION ELIGIBILITY. Is the §H1.1 allowed-path list correct and
    complete for an inactive implementation, and is the §H1.2 frozen list
    complete? In particular: is it right that no test_p1_row_NNN_ function and
    neither MS-6 module may exist before OR-5/OR-7?

Q9  THE EXISTING generic_harness.py. Confirm the §H11 reading — that its
    subprocess/Popen/kill/killpg usage is conforming to the generic-harness
    lineage and non-conforming to P1 §P1-3.2 and S-12, that it is production
    root #3, that it must not be edited or adopted here, and that a recorded
    fresh audit is mandatory before reuse.

Q10 CLOSURE TOKEN. Given F1 and F2, is READY_FOR_OFFICINA_P1_WB_BINDING_XY_REVIEW
    the right verdict — the binding being complete and reviewable with the two
    Major findings surfaced as review items and the affected function fenced —
    or should a governing-pair Major finding gate the binding itself?
```

---

```text
READY_FOR_OFFICINA_P1_WB_BINDING_XY_REVIEW

T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, OBSERVATION-ONLY
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
P1 IDENTITY-OBSERVATION IMPLEMENTATION SURFACE = OUT OF SCOPE, NO CODE
P1 WATCHDOG-FREEZE CELL = SELECTED: OPTION W-B, SENSOR-ONLY
WATCHDOG AUTHORITY AMENDMENT V1.7 = NOT ACCEPTED
IMPLEMENTATION AUTHORIZATION = NOT GRANTED
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
```

The exact selected token and the formal selection signature govern. This
closure is an untrusted self-assessment and is normative for nothing.
