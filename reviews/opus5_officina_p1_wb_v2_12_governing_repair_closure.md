# Officina P1 W-B v2.12 governing repair — author closure

**Author:** Claude Code Opus 5, **governing-pair repair author only**. Not an
independent X-line or Y-line reviewer. **This closure is an untrusted
self-assessment and is normative for nothing.** Every figure in it was
recomputed from the produced bytes; a reviewer who disagrees with a figure
should trust the bytes and name this closure as the defect.

**Base commit:** `d4d683a` (`Review W-B governing pair v2.11`). Nothing was
committed by this round.

`T = NOT_ACTIVATED`. Programme claim `OPEN`. W-B is signed and was not reopened.
`OR-2` alone is complete; `OR-3`..`OR-11` remain unauthorized.

---

## §1. Verdict

```text
READY_FOR_OFFICINA_P1_WB_V2_12_FINAL_XY_REVIEW
```

Sol's three Majors are repaired in the produced bytes, every X-line and Y-line
log item is dispositioned, the forced accounting is performed and recounted, and
the round created no code, no test, no key, no artifact, no `OR` step, no
process operation, no install and no activation.

---

## §2. Inputs, outputs and scope

### §2.1 The six pinned inputs, recomputed from disk — all six MATCHED

```text
71ec025a6d5da2b975e8f958d4c5e218e37e0de76fc1c64e2824e20cb3e08a4c  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8_DRAFT.md
c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_11.md
d7ccf170b759f89519f24b26bd817d273197dddd0b5208e0d95eecebf59ec91d  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V2_DRAFT.md
a70f6a7774386d7b36084b0e19c5f1e78b11a5e04f2d992d95d93148878c5c6b  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V2_DRAFT.md
3964469740fc73a6a4836b64247003c39d5261a6af9c6ddf37a0da76c13f0759  reviews/fable_officina_p1_wb_v2_11_final_x_review.md
ef4508be13d9ef395b2e8d5542d6256e2bd5719e99cbff209d13612dc5dd00c4  reviews/sol_officina_p1_wb_v2_11_final_y_review.md
```

### §2.2 Exactly six files were created, and there is no seventh

The v2.11 commit added a chat-response file that its closure did not declare;
the Y line graded that a scope-accounting error (`Q10`). **This round declares
its file list exactly and writes nothing outside it.**

```text
510d6a88c772b4a7a40b9cbf36711e441a9fbe9fb57ee0a3f92d5ff864711fa7  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_12_CORRECTION.md
a7ec78cca0c7a537c4251a5342d7bb27c63d16de307c2ee2e901d69187d98e17  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_9_DRAFT.md
e796d9e8838b160cc76a3c14814881ac38a0b2a6568ee3103c1286334e5f729b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_12.md
9a0fc412f67f98e78a0a4991f1bcb6923195366c9126718a42827ae6e2409cb1  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V3_DRAFT.md
f539720f57585bff080a826771e898e66abcc0ade2b0f7c4154d634d4c051bb2  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V3_DRAFT.md
                                                                  reviews/opus5_officina_p1_wb_v2_12_governing_repair_closure.md   (this file)
```

**No chat-response file, transcript, note or scratch artifact is authored by
this round.** The working tree's pre-existing dirty and untracked files —
`accounting.py` and its test module, the ten modified `reviews/` files,
`essay/OUTLINE.md`, the untracked `generic_harness.py` and its test module, and
one untracked prior chat response — are byte-unchanged and were not read for
behaviour, adopted, staged, reverted or cited.

### §2.3 Which line governs, and why

Fable returned `OFFICINA_P1_WB_V2_11_X_CONFIRMED_FOR_ACCEPTANCE_REVIEW`; Sol
returned `REVISE_OFFICINA_P1_WB_V2_11` with three executable Majors. **The
stricter executable counterexamples govern.** An X-line confirmation does not
neutralize a Y-line counterexample that runs against the same bytes: a
demonstrated fail-open in the sole `W-B` endpoint-loss executor is not made safe
by a second reader not having found it. This round is bounded to `R1`..`R5`.

---

## §3. Disposition of Sol `M-1`..`M-3`

### §3.1 `M-1` — `KV_FORBIDDEN_TARGET` did not dominate earlier skips. **REPAIRED.**

**The defect, restated so the repair is checkable.** `SC-2` admitted to the
scope sequence only candidates already satisfying `KV-1` and `KV-2`; `SC-6`
stopped at the first failing predicate. A current-generation entry whose recorded
group *was* a protected group could therefore fail `KV-2` first, be skipped, and
never reach `KV-6`, while a different valid handle in the same table still
reached `_killpg`. That contradicted `SC-6`'s own dominance sentence, row 89's
required whole-classifier termination, and Q3's required dominance over every
skip. Fable's `Q3` argued the masking case was safe because `SC-2` excludes such
a handle from scope; **that argument protects the forbidden group from being
signalled, and it does not deliver the whole-classifier termination row 89
requires.** Sol's reading is the operative one.

**The repair, in composite v1.12 `§P1-10.7`.** The classifier is now explicitly
two-phase and the range is `SC-1`..`SC-10` everywhere.

```text
PHASE P0 — SC-9, THE GLOBAL PROTECTED-GROUP PRE-PASS
  P0-1  runs before ANY candidate filtering, ANY KV-1 or KV-2 evaluation, ANY
        scope construction, ANY sort and ANY _killpg. NOTHING RUNS BEFORE IT,
        so no earlier KV skip can mask it.
  P0-2  builds the protected set G from three sources:
          (a) the PCS's own group, one KG-1 PGRP_OBSERVE(_getpid()) at the start
              of P0; not PRESENT_VALID => FAIL CLOSED, classifier terminates
          (b) EVERY watchdog pid AND EVERY non-NULL watchdog recorded group of
              the current generation — both, so an unrecorded watchdog group is
              still unreachable
          (c) the recorded supervisor group of SPAWNING_GROUP.json (§P1-5.1,
              §P1-7.5 c10/c14, §P1-4.6)
  P0-3  scans EVERY current-generation entry regardless of role, ownership,
        state and fd_delivery, and regardless of whether it could ever be a
        candidate. It visits every entry before it concludes.
  P0-4  a non-NULL recorded group in G TERMINATES THE WHOLE CLASSIFIER:
          token KV_FORBIDDEN_TARGET / terminal
          PCS_FREEZE_CLASSIFIER_FORBIDDEN_TARGET / qualifier
          FREEZE_NOT_ATTEMPTED / signals ZERO, this pass and every later pass
  P0-5  stale-generation entries are NOT examined by the group test and retain
        exactly KV-1's governing treatment, KV_STALE_HANDLE, a skip
  P0-6  every malformed or NULL value takes its exact closed branch and NONE
        grants scope; an absent or malformed SPAWNING_GROUP.json process_group_id
        fails closed rather than being treated as unknown-and-proceed
  P0-7  Phase P1 begins only after a complete clean scan; nothing is signalled
        in P0 and no P0 observation is carried into P1

PHASE P1 — SC-10, THE COMPLETE PROSPECTIVE SCOPE
  P1-1  every otherwise eligible candidate through FRESH KG/KV checks
  P1-2  ALL results collected BEFORE ANY signal; no _killpg while any entry is
        unevaluated
  P1-3  a freshly observed protected group terminates the ENTIRE classifier
        WHEREVER FOUND, including AFTER other candidates are already KV_OK; the
        already-verified candidates are DISCARDED, not signalled
  P1-4  only then are the verified distinct groups deduplicated and sorted
  P1-5  re-verification IMMEDIATELY BEFORE EACH individual signal and for EVERY
        signal number; a protected result there ABANDONS every remaining action
  P1-6  the four-part conjunction any signal requires, stated so a build fails
```

**Supporting amendments that make the dominance total.** `SC-2` now projects
only candidates that passed `KV-1`..`KV-6` in full, and says in terms that
building from `KV-1`/`KV-2` survivors *was* the masking defect. `KV-6` gains a
second conjunct testing the *freshly observed* `pgrp` against `G`, so a recorded
group that was safe when written is not safe if the kernel now reports the handle
inside a protected group. `KV-2` is labelled a candidate filter and **not** a
safety boundary, with the sentence that a handle `KV-2` refuses has already been
examined. `SC-7` records that all 72 tuples — including all 24 watchdog tuples,
all 32 contradicted-or-reaped tuples and all 6 NULL-group tuples — were scanned
by Phase P0 before the partition is reached.

**Dominance pinned over every skip and error token, in `SC-6`.**

```text
a protected group anywhere in the current-generation table produces the
  terminal, whatever token any OTHER entry produces, and whatever token THAT
  entry would have produced under KV-1..KV-5;
KV_STALE_HANDLE, KV_ROLE_OR_STATE_REFUSED, KV_OBSERVATION_UNAVAILABLE,
  KV_IDENTITY_CONTRADICTED, KV_GROUP_MISMATCH and KV_OK NEVER SUPPRESS IT,
  never consume the entry before SC-9 has examined it, and never reorder it;
SC-8's STRUCTURAL_VIOLATION is EQUALLY TERMINAL and equally sends no signal, so
  it is not a mask either.
```

**The exact Y counterexample, in the governing bytes.**

```text
h1  current generation, role CONTROLLER, state RUNNING, ownership CONTRADICTED,
    pgid_or_null = the process_group_id of SPAWNING_GROUP.json
h2  current generation, role CONTROLLER, state RUNNING, ownership OWNED, a valid
    unprotected leader group, PRESENT_VALID, identity matching, pgrp equal

v1.11   h1 fails KV-2 -> KV_ROLE_OR_STATE_REFUSED, SKIP; KV-6 never runs for it;
        h2 passes KV-1..KV-6; _killpg(h2, 15) and _killpg(h2, 9) AUTHORIZED.
v1.12   P0-3 scans h1 REGARDLESS of ownership; P0-4 finds its group in G;
        the WHOLE classifier terminates, KV_FORBIDDEN_TARGET /
        PCS_FREEZE_CLASSIFIER_FORBIDDEN_TARGET / FREEZE_NOT_ATTEMPTED.
        EXACTLY ZERO SIGNALS ARE SENT, including none to h2's group.
A BUILD THAT SENDS ANY SIGNAL ON THAT TABLE IS NONCONFORMING.
```

**Permutation fixtures, required by test row 89.**

```text
the protected entry at position 1                      same zero-signal terminal
the protected entry at every interior position         same zero-signal terminal
the protected entry at position n                      same zero-signal terminal
the protected entry as the only entry                  same zero-signal terminal
the protected entry carrying each role of §P1-8.5      same zero-signal terminal
the protected entry carrying each state                same zero-signal terminal
the protected entry carrying each ownership            same zero-signal terminal
the protected value = the PCS's own group              same zero-signal terminal
the protected value = a watchdog leader group          same zero-signal terminal
the protected value = a watchdog pid                   same zero-signal terminal
the protected value = the recorded supervisor group    same zero-signal terminal
A BUILD WHOSE ANSWER DIFFERS BY POSITION, ROLE, STATE, OWNERSHIP OR PROTECTED
VALUE FAILS ROW 89.
```

Row 89 additionally fails a build on: any pre-Phase-P0 filter, sort or signal; a
signal issued for a `KV_OK` group while a later entry yields
`KV_FORBIDDEN_TARGET`; continuation after a pre-signal protected result; and any
promotion of a stale entry or any non-`SC-8` treatment of a malformed value.

**`FREEZE_NOT_ATTEMPTED` is not an eighth token.** It qualifies the classifier
terminal. `SC-5` remains exactly seven, and **both** `SC-5` and test row 101 now
say so in terms, and row 101 fails a build that implements it as an `SC-5` token,
as a per-group result, or as an `FC-1` code. The twenty-five-code closed failure
set is untouched.

### §3.2 `M-2` — `KG-1` unexecutable and `KG-2` not derived. **REPAIRED.**

**`KG-1`'s grammar, now executable and closed.**

```text
G0  TOKENISATION. Locate the LAST 0x29 ")" in the already-read buffer; none =>
    UNPARSABLE. Take the bytes strictly after it, minus one trailing 0x0A.
    A SEPARATOR is one of 0x20 0x09 0x0A 0x0B 0x0C 0x0D; a TOKEN is a maximal
    non-separator run; fewer than twenty tokens => UNPARSABLE. NO TOKEN CAN
    CONTAIN A SEPARATOR BY CONSTRUCTION, so no whitespace is admitted inside any
    field and no missing or extra separator is absorbed silently.

G1  TOKEN(1) IS THE STATE FIELD. It is EXACTLY ONE BYTE and that byte is a
    member of the CLOSED PERMITTED SET, and IT IS NEVER PARSED AS AN INTEGER:
      "R" 0x52 running        "S" 0x53 sleeping       "D" 0x44 disk sleep
      "T" 0x54 stopped        "t" 0x74 tracing stop   "X" 0x58 dead
      "Z" 0x5A zombie         "P" 0x50 parked         "I" 0x49 idle
    Any other length, or any one-byte token outside the set => UNPARSABLE.
    PROVENANCE: exactly the characters the CURRENT Linux kernel emits for field
    3 of /proc/<pid>/stat, from task_state_array in fs/proc/array.c of the 5.x
    and 6.x series.
    NOT A CATCH-ALL: the pre-3.13 characters proc(5) also records — "W" paging
    or waking, "x" dead, "K" wakekill — are NOT admitted. A narrower set can
    only refuse and never permit, so the direction is fail-closed.
    THE CURRENT GOVERNING OBSERVER DEFINES NO BROADER EXACT STATE GRAMMAR.
    §P1-10.3 names the state field and fixes no character set for it, so this
    set is supplied as new supporting content and Part 2 records it as new.

G2  THE BASE-10 INTEGER GRAMMAR. A non-empty run of ONLY 0x30..0x39, length 1
    through 19. NO sign byte, NO underscore, NO radix prefix, NO decimal point,
    NO exponent, NO separator anywhere, NO other byte. Value above
    9223372036854775807 => UNPARSABLE. Leading zeros permitted and read as
    base ten.
G3  ppid  = TOKEN(2), a G2 integer >= 0.
G4  pgrp  = TOKEN(3), a G2 integer >= 1. ZERO IS REFUSED, because
    killpg(0, sig) signals the CALLER's own process group; it is refused at the
    parse, before any predicate sees it.
G5  start_identity = TOKEN(20), a G2 integer >= 0 — the same token §P1-10.3
    already parses from the same position in the same buffer.

PRESENT_VALID is returned ONLY AFTER G0 succeeded and G1, G3, G4 and G5 ALL
parsed. Every other outcome takes exactly one closed token of the five-value
result set { ABSENT, PRESENT_VALID, UNREADABLE, UNPARSABLE, ERROR }; a read
failure takes ABSENT / UNREADABLE / ERROR by §P1-10.3's unchanged errno map.
```

**`KG-2` is now honest.** `§P1-10.7` carries **two** source traces. Part 1 lists
only what is genuinely derived from current governing bytes — and it now
separates out, as their own rows, the two facts the v1.11 table conflated with
`KG-2`: that a `pgid_or_null` field exists and that `_killpg` requires a
kernel-verified group, and that the *supervisor* group is kernel-verified and
recorded. **Part 2 states, row by row, every new normative rule this version
supplies, against the existing clause it attaches to.**

```text
EXISTING CURRENT CLAUSE                   NEW NORMATIVE SUPPORTING RULE IN v2.12
§P1-8.5 declares the field                P-1 NULL at handle creation, EVERY
                                              role, no exception
§P1-7.5 c10 verifies the SUPERVISOR       P-2 the ONE population point for a
  group; it says nothing about child          CHILD handle — PRESENT_VALID,
  handles                                     identity equal, pgrp == pid, one
                                              assignment at that instant
no clause states a write site             P-3 exactly one writer, exactly one
                                              site, at most one write; a second
                                              write is a structural violation
no clause states either behaviour         P-4 role-independent population, so a
                                              watchdog's recorded group is
                                              decidable for SC-9/KV-6(b); and a
                                              non-leader child stays NULL
                                              forever and is never signalable
no clause states immutability             P-5 never rewritten, re-derived,
                                              widened, narrowed, repaired or
                                              cleared on release or reap
KV-5 refuses; nothing says what happens   P-6 the field is NOT repaired; the
  to the FIELD                                refusal is KV_GROUP_MISMATCH; the
                                              protected-group test dominates it
no clause enumerates the paths            P-7 the complete creation and failure
                                              table: creation failure, no
                                              verification yet, each unusable
                                              observation class, identity
                                              mismatch, non-leader, the one
                                              write, release and reap
§P1-10.3 names a "state field" and        KG-1 G1's closed nine-character set
  fixes no character set
§P1-10.3 says only "a non-integer         KG-1 G2's exact integer grammar and
  field ⇒ UNPARSABLE"                         overflow bound
no clause constrains pgrp's value         KG-1 G4's refusal of pgrp 0
KV-6 and row 89 require a terminal;       SC-9  Phase P0
  nothing made it dominant
SC-3 required re-verification             SC-10 Phase P1, collect-all-then-act
SC-6 names one terminal                   the qualifier FREEZE_NOT_ATTEMPTED
```

**The v1.11 sentence "the one supporting rule the live pair did not already
carry is `KG-1`'s process-group field" is withdrawn as false**, and `§A0.3` `R2`
says so.

**No import expansion.** `_getpgid` is still unbound in both files; no scoped or
global allowlist of `§P1-3.2` gains a name; `MS-11`'s 89 rows, CANON length
20534 and digest `aa974e0c…c20ee` are byte-unchanged; `MS-13` is unchanged;
`S-12` is retained. **No superseded v2 packet was opened for behaviour**, and
`§P1-10.3` and every existing `STAT_OBSERVE` consumer are unchanged.

**One disclosure the reviewers should weigh, and it is not repaired here.**
`§P1-10.3`'s own summary phrase — "a short token list, **a non-integer field**,
or any parse failure ⇒ `UNPARSABLE`" — is ambiguous as to whether the state
field it names is among the "fields" required to be integers. Read strictly, it
carries the same shape of defect `M-2` names in `KG-1`. **v2.12 does not edit
`§P1-10.3`**, because Sol's Major is against `KG-1`, editing the identity
observer would move a clause outside `R1`..`R5` and would perturb consumers this
round has no license to touch. `KG-1` instead states its own grammar in full and
says in terms that it governs this classifier's parse and nothing else, and that
`§P1-10.3` is unchanged. **§9 `Q6` asks the two lines whether that boundary is
right or whether `§P1-10.3` must be repaired in the next round.**

### §3.3 `M-3` — the transformation and `PO-9` were not identifiable. **REPAIRED.**

**The overlap is gone.** Binding v2's semantic line-action table — in which lines
58, 60, 85 and 88 each appeared in two rows with different actions — is deleted
in full. **Binding v3 replaces ONE span as ONE unit.**

```text
SOURCE SPAN, identified by SENTINELS and not by line numbers
  first line   ### Cell 2 — `AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM`, new in v1.3
  last line    decisions — whichever way they go — land in a document that is otherwise ready.
  cardinality  each occurs EXACTLY ONCE in composite v1.12 under whole-line
               equality; zero, or two or more, FAILS CLOSED
  the sentinels are PART OF the span and are replaced with it
  informative  lines 55..95 in composite v1.12; the LINE NUMBERS ARE INFORMATIVE
               AND THE SENTINELS ARE NORMATIVE
  length       41 lines, 2184 UTF-8 bytes
  SHA-256      1623dc45bb5c17c507ca590c3d6ca2a171ed7e40e5c4f287a8a736ee860db2b8

REPLACEMENT BYTES, pinned in a fenced literal whose extraction rule EXCLUDES the
fence markup: the bytes are the lines strictly between the opening
REPLACEMENT-BYTES fence line and the closing fence line, each including its
0x0A; no line of the replacement is itself a fence line
  length       37 lines, 2120 UTF-8 bytes
  SHA-256      f2782a63db003dfb370d0c0c5afb9c928a8fc61c8af29285c8a1172657a84fee
  encoding     UTF-8, no BOM, LF, final byte 0x0A, U+2014 at two loci and no
               other non-ASCII character
  VERIFIED     the block was extracted from the produced binding by its own
               stated rule and re-hashed; it matches

SPLICE, deterministic and total
  1..4  locate the two unique sentinel lines; any cardinality other than one, or
        any order other than begin < end, FAILS CLOSED
  5     VERIFY the source span digest; a mismatch FAILS CLOSED and OR-4 does not
        proceed against unexpected bytes
  6     RETURN prefix || REPLACEMENT || suffix
  EXACTLY ONE REPLACED RANGE. NO TWO RANGES OVERLAP BECAUSE THERE IS ONLY ONE.
  NO IMPLEMENTER CHOOSES ANY BOUNDARY, SENTENCE OR WORD, so two implementations
  given the same source bytes emit BYTE-IDENTICAL in-memory output.
```

**The post-selection text is exact.** It states the cell signed, names the W-B
token and the signature path and digest; names W-A as rejected with **no**
capability; carries **no** "open", "unsigned", "selects neither", "predicts
neither" or "carries both variants" assertion; carries no marker string and no
notation example; leaves Cell 1 untouched because the span begins after every
byte of Cell 1; and adds no normative rule. It retains every common fact needed
outside the replacement: the reassignment common to both options, the `H-1`..`H-4`
canonical-block pointer, "no author closure states that step", the corrected
`G-10` / `§P1-14.4` reference, and — with the stale wording gone from the source
span itself — "a finished replacement for version 1.11".

**`PO-9` now has literal arrays, an exact normalization and exact boundary
matching.**

```text
PN(bytes) := NORMALIZE( STRIP_LEAD(bytes) )
  STRIP_LEAD  from the START of every line, delete every leading byte in
              { 0x20, 0x09, 0x3E } repeatedly. It removes markdown blockquote
              markers and indentation, which §P1-14.2 NORMALIZE does not, and
              which would otherwise let a rewrapped or unquoted restatement of a
              forbidden assertion evade a literal. IT LIVES IN THE ORACLE, adds
              no governing surface, adds no guard-pattern class, and changes
              neither §P1-14.2 nor §P1-17 nor G-10.
  NORMALIZE   composite §P1-14.2, verbatim.
BOUNDARY MATCHING  a literal matches iff its bytes occur as a CONTIGUOUS
              SUBSTRING of PN(scope). No word boundary, no stemming, no
              wildcard, no regular expression, no fuzzy match; counts are
              non-overlapping, left to right.

D1  ELEVEN literals, order part of the value
    canonical serialization 926 bytes
    SHA-256 d5b375c518c935d3a6935a1932bf6bfa237cb9c99c7b81913f4e1433142b6c1e
    every literal is PN of a passage of the PRE-RESOLUTION Cell-2 span, checked
    mechanically, so coverage is verified rather than asserted

D2  THIRTEEN literals, order part of the value
    canonical serialization 1044 bytes
    SHA-256 4e2120857dd67124095e5f5479d69cbf7ba703605abb3448a2fe414b3ff8a15c
    D2[1] is the whole Cell-2 W-A exposition with blockquote markers stripped;
    D2[2]..D2[5] are its four capability clauses separately, so a partial
    reintroduction is still caught; D2[6]..D2[13] are the [W-A] branch texts of
    the eight other operative loci with their markers removed, because a
    marker-free reintroduction is exactly what PO-2 cannot see
    NO LITERAL IS A BARE WORD. "slot 6", "socket", "window" and "accepted" are
    not literals, because each occurs legitimately in class R.
```

**False positives — measured, not argued.**

```text
the §2.2 replacement bytes                       D1 0   D2 0
Cell 1, byte-unchanged, which legitimately still
  asserts an OPEN cell about a DIFFERENT cell    D1 0   D2 0
the joint install and authorization block, where
  TS-1's grammar, TS-1's pairing rule and CK-14's
  fixture MUST name the W-A token                D1 0   D2 0
REGION(GUARDDATA)                                D1 0   D2 0
each of R-5's seven supervisor-side clauses      contains no literal, and no
                                                 literal contains it
each of R-6's two closed/absent watchdog slot-6  contains no literal, and no
  clauses                                        literal contains it

THE SHARPEST CASE IS CELL 1. Its notice says "...until the author cell
AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS is signed"; D1[2] requires
"...until the watchdog-freeze mechanism cell is signed". EVERY D1 LITERAL
CARRIES A WATCHDOG-FREEZE-SPECIFIC DISCRIMINATOR FOR EXACTLY THIS REASON. A
detector firing on Cell 1 would demand deletion of a blocking notice this
signature does not discharge, which CT-5 forbids.
```

**False negatives — measured.** Each of the eleven `D1` and thirteen `D2`
literals, embedded in a marker-free carrier with arbitrary surrounding bytes,
arbitrary wrapping and arbitrary blockquote indentation, is detected: 11 of 11
and 13 of 13. The whole W-A exposition restored as plain paragraphs is caught by
`D2[1]`..`D2[5]`; any single capability clause restored alone is caught by its
own literal; the pre-resolution heading is caught by `D1[1]`.

**Retained exactly, and `D3` enforces it.** Both option tokens and both paired
amendment tokens in `TS-1`; the `CK-14` mismatch-fixture vocabulary; the guard
data at `H_GUARDDATA` `faf2d709…0426`; the seven legitimate supervisor/PCS socket
and slot-6 loci; and watchdog slot-6 only in its closed/absent sense at two loci.
**Removed only:** operative W-A grant and request behaviour, and the discharged
Cell-2 open state.

One arithmetic consequence is disclosed rather than hidden: the replacement names
the rejected option's paired amendment token once, as a historical fact with no
capability, so `P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1` occurs **twice** in the
resolved file — the `TS-1` pairing rule and that historical mention. Both are
class R; binding §2.5's totals say so explicitly.

---

## §4. Disposition of every X-line and Y-line log item

```text
ITEM                                          DISPOSITION IN v2.12
Sol M-1  forbidden-target dominance           REPAIRED — §3.1, SC-9/SC-10, row 89
Sol M-2  KG-1 grammar and KG-2 derivation     REPAIRED — §3.2, G0..G5, Part 2 table
Sol M-3  transformation and PO-9 identity     REPAIRED — §3.3, binding v3
Sol Q1 / Fable L-X3  "content bytes" were     REPAIRED — every region length is
  character counts (4052/222364)              now an actual UTF-8 byte count:
                                              4166 and 223250. No operative
                                              clause consumes a region length.
Sol Q5 / Fable L-X2  N-16 says MS-8 is 69     REPAIRED — N-16 now says 81
Sol Q7 / Fable L-X4  H-4 attributes           REPAIRED — H-4 now names CK-7 and
  HISTORICAL_BYTE_MOVED to CK-12              adds a sentence recording that
                                              CK-7 owns it alone and CK-12 owns
                                              INSTALL_RECORD_NAME_MISMATCH.
                                              INSIDE the canonical block, so it
                                              lands in BOTH files.
Sol log 4 / closure L-2  stale "finished      REPAIRED — the Cell-2 sentence now
  replacement for v1.2"                       reads "version 1.11", and the
                                              replacement bytes carry the same
Sol Q10  the commit's seventh chat-response   REPAIRED — §2.2 declares exactly
  file versus the six-deliverable claim       six files and no seventh exists
Fable L-X1  row 106 declares eleven fixture   REPAIRED — the header now declares
  groups and defines ten                      TEN, (a)..(j), every one defined,
                                              with an explicit statement that
                                              there is no group (k) and that the
                                              CK-14 obligation is held in full
                                              inside the joint block by H-3.
                                              Ten was preferred over inventing
                                              an eleventh fixture, as required.
Fable L-X5  the v2.11 closure miscounted      CORRECTED AND RECOUNTED — see §5.4
  the twelve-check mentions
Fable L-X6  binding §2.2's spans overlap      REPAIRED — one span, one unit, no
                                              action table at all
Fable L-X7  the KV-6 masking argument is      SUPERSEDED — the argument is no
  unstated                                    longer needed, because the case it
                                              defended is now a terminal. SC-9
                                              and SC-6 state the reasoning.
AUTHOR-FOUND, NEITHER LINE LOGGED IT          REPAIRED AND DISCLOSED — CK-13's
  "a record with a 70th entry" was a          extra-entry fixtures now read "an
  literal correct only in the 69-member       82nd entry", with rows 107 and 108
  generation                                  moved with it. §5.3 lists it.
AUTHOR-FOUND, NEITHER LINE LOGGED IT          REPAIRED — the §A9 cross-reference
  the §A9 audit cited a composite LINE        audit now cites the locus by
  NUMBER for the Cell-2 G-10 locator          section, not by a line number that
                                              every generation moves.
```

---

## §5. The accounting, recounted from the produced bytes

### §5.1 The four new `M2` rows and the atomic update

```text
71ec025a6d5da2b975e8f958d4c5e218e37e0de76fc1c64e2824e20cb3e08a4c  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8_DRAFT.md
c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_11.md
3964469740fc73a6a4836b64247003c39d5261a6af9c6ddf37a0da76c13f0759  reviews/fable_officina_p1_wb_v2_11_final_x_review.md
ef4508be13d9ef395b2e8d5542d6256e2bd5719e99cbff209d13612dc5dd00c4  reviews/sol_officina_p1_wb_v2_11_final_y_review.md
```

```text
                                       v2.11   v2.12   RECOUNTED FROM BYTES
MS-2 literal rows                         63  ->  67   67, all distinct
MS-3 literal rows                          7       7   7
MS-8 / TS-3 member_count                  77  ->  81   M1 2 + M2 67 + M3 7 +
                                                       M4 1 + M5 1 + M6 2 +
                                                       M7 1 = 81
composite provenance region rows          71  ->  75   75, all distinct
member classes                             7       7   seven, no eighth
```

### §5.2 Every dependent literal, schema, fixture and count that moved

```text
MS-9   P(M2) 63 -> 67 ; "72 literal strings" -> 76 ; the M2/M3 intersection
       sentence ; 2+63+7+1+1+2+1 = 77 -> 2+67+7+1+1+2+1 = 81 ; "still
       enumerates 77" -> 81 ; and the Group-3 M1/M2 disjointness argument, whose
       amendment enumeration gains _V1_8_DRAFT.md and whose composite
       enumeration gains _V1_11, with the "eight rows" phrasing replaced by
       "four more rows"
IR-4   the 77-member enumeration -> 81 ; the 77 members --IR-1--> -> 81
IR-3   ARRAY of exactly the 77 entries -> 81 ; the record's 77-member digest
       edge and its (M1 2, M2 63, ...) breakdown -> (M1 2, M2 67, ...)
MS-4   members ARRAY of exactly 77 OBJECTS -> 81
IR-13  row 38 StageB.member_count = 77 -> 81
TS-3   member_count INTEGER, exactly 81
TS-5   B7 at all three loci, and B17 -> 81
OR-9   the canonical 81-member list
CK-4   enumerate the 81 members
CK-6   81 entries / 81-entry sorted array / any length other than 81 /
       cardinality fixed at 81
CK-7   visit the 81
CK-13  "a record with an 82nd entry"
FS-1   all 81 members exist ; every one of the 81 present
rows   103 (70 -> 74 recorded digests), 104 (77 -> 81), 105 (77 -> 81),
       106 (77 -> 81 plus the group-count repair), 107 (77->81, 76->80, 63->67,
       "70th entry" -> "82nd entry" at both loci), 108 (78->82, 77->81, 70->74,
       63->67), 115 (77 -> 81)
prov   "literal 63-path list" -> 67 ; "71 rows: the 63 M2 members" -> "75 rows:
       the 67 M2 members" ; every "not counted in the 71" -> 75 ; the accounting
       note rewritten for four rows
N-14   rewritten for the four rows ; N-16's stale 69 -> 81
```

### §5.3 Generation strings, anchors and consumers

```text
MS-1's two literal member paths        _V1_9_DRAFT.md, _COMPOSITE_V1_12.md
TS-1's three pre-selection paths       the packet _V2_12_CORRECTION.md, the
                                       amendment _V1_9_DRAFT.md, the composite
                                       _COMPOSITE_V1_12.md
the §A0.4 anchor token                 P1_WATCHDOG_V2_12_PRE_SELECTION_COMPOSITE_SHA256
the A16(d) consuming token             the same, inside the joint block
OR-4's operative sentence              "the v1.9 amendment is installed"
the acceptance token                   ..._AMENDMENT_V1_9
the anchor VALUE                       e796d9e8838b160cc76a3c14814881ac38a0b2a6568ee3103c1286334e5f729b
                                       equal to composite v1.12's H_FILE, on
                                       exactly one line, in the amendment only
RETIRED, ZERO OCCURRENCES IN EITHER FILE
  ..._AMENDMENT_V1_8 and ..._AMENDMENT_V1_7 as acceptance tokens
  P1_WATCHDOG_V2_8 / V2_9 / V2_10 / V2_11_PRE_SELECTION_COMPOSITE_SHA256
```

### §5.4 Recomputed digests, regions and censuses

```text
H_BODY       d5125d54e312fd87fff7c622cedf8538ef2ea99c9666ec619becfd2e4651a1e6
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426   UNCHANGED
H_NORMATIVE  0d3b411e6f92c37f759025d71af6fa59d7b648a0106869829c30c1917b490d66
H_FILE       e796d9e8838b160cc76a3c14814881ac38a0b2a6568ee3103c1286334e5f729b

H_HANDOFF    a03cb516958052109a860f461e7777916b4185ff1cd1deedeb0d3d955c343a66
             4166 UTF-8 bytes, BYTE-IDENTICAL across both files
H_JOINT      6b0e64e0bd4f56c6c2b6a748808944221125ced2d482d8684c7566461584a2f7
             223250 UTF-8 bytes, BYTE-IDENTICAL across both files
             each of the four delimiter lines occurs EXACTLY ONCE per file under
             whole-line equality; the six composite region sentinels likewise

MARKER CENSUS, composite v1.12
  marker-bearing lines            20   preamble 3, body 16, guarddata 1
  [W-A] / [W-B]                13/13
  both-marker lines, whole file     6  83, 2959, 7179, 7207, 7218, 7317
  both-marker lines, body only      4  2959, 7179, 7207, 7218
  amendment marker-bearing lines    0

CK-1..CK-12 MENTIONS, RECOUNTED
  amendment v1.9   3   composite v1.12   3
  every one is a negation or a description of the removed defect; NO OPERATIVE
  CLAUSE IN EITHER FILE STATES A TWELVE-CHECK RANGE. The v2.11 closure said
  "three in each file"; that was right for the composite and wrong for the
  amendment, which then carried five (Fable L-X5). The recount above is over
  THESE bytes.

attested_pid / attested_pgid      0 in the amendment, 0 in the composite
```

---

## §6. Preserved, and verified preserved

```text
the signed W-B selection and its sensor-only semantics       NOT REOPENED
the 89-row reachable_closure, its 14-row bootstrap subset,
  its 7 unexecuted branches, CANON length 20534 and digest
  aa974e0c91e5c9afd0aceefa6b0e47ef42b5ad7b71dc4de690a4873232dc20ee  BYTE-UNCHANGED
the project-import surface, MS-13's four modules and their
  32 effect booleans                                         UNCHANGED
CK-13's D1/D2 partition, the 25 closed failure codes,
  B14's semantics, IR-13's 50 rows and its K1..K5 / K6..K8
  boundary                                                   UNCHANGED
the rollback residuals TR-2(a) and TR-2(b), FS-1..FS-5,
  A0.4's honest rollback limitation                          UNCHANGED
identity Option A as signed external author state, with
  P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1 UNACCEPTED    UNCHANGED
every scientific contract, treatment, evidence class,
  covariate, endpoint, qualification and comparison          UNTOUCHED
the T envelope and the programme claim                       UNMOVED
row 106 group (i)'s expected PASS                            UNCHANGED
the seven member classes                                     UNCHANGED
H_GUARDDATA and the VARIANT_MARKER class                     BYTE-UNCHANGED
```

---

## §7. Negative space, verified on disk rather than asserted

```text
src/philosophia/officina/p1_wb_oracle.py         ABSENT
src/philosophia/officina/p1_wb_contract.py       ABSENT
tests/test_officina_p1_wb_oracle.py              ABSENT
tests/test_officina_p1_wb_contract.py            ABSENT
tests/fixtures/p1_wb/                            ABSENT
tests/test_officina_p1_freeze_authority.py       ABSENT   (MS-6 module 1)
tests/test_officina_p1_install_integrity.py      ABSENT   (MS-6 module 2)
successor/officina/authorization/                ABSENT
successor/officina/runtime_control/              ABSENT
scripts/officina_process_control_bootstrap.py    ABSENT
scripts/officina_role_bootstrap.py               ABSENT
test_p1_row_NNN_ functions, whole repository     ZERO
```

**No code, test, key, entropy, artifact, `OR` step, process operation, install
or activation was created.** No `/proc` was read against any live process; no
freeze was executed, requested, journalled or witnessed; no clock was sampled
for any contract purpose; no Philosophia production or project module was
imported, executed or compiled. **The §2.2.2 replacement bytes exist only inside
the binding document and are at no governing path.**

**No existing file was modified.** The ten modified `reviews/` files,
`accounting.py`, its test module, `essay/OUTLINE.md`, the untracked
`generic_harness.py`, its test module and one untracked prior chat response are
byte-unchanged; `generic_harness.py` was not opened, adopted, cited or reverted,
and the handoff records no line number and no content claim about it. **Nothing
was committed.**

### §7.1 Scaffold, identity and acceptance boundaries

```text
SCAFFOLD   handoff v3 remains INERT ORACLE AND DECLARATIVE SCAFFOLDING ONLY.
           No runtime EOF, classifier or process-control implementation; no
           PGRP_OBSERVE; no G0..G5 parser over any buffer, real or synthetic;
           no production root, MS-5, MS-6, test-row or shared-runtime edit; no
           identity-observation code; not the XS-1 combined binding. The three
           removed v1 test paths stay removed. D-8 adds the KG-1 state-character
           SET as a constant and explicitly is not the parser.
IDENTITY   attested_pid and attested_pgid occur zero times in both governing
           files. KG-1's start_identity and pgrp and KG-2's recorded group are
           process-control observations in the PCS's own in-memory handle table,
           are NOT the §P1-13.2 row 2 peer-record fields, have no schema key and
           reach no durable object. A scaffold that introduces an identity
           constant on the strength of KG-1 or KG-2 has left scope.
ACCEPTANCE the future token is version-bumped to
             I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_9
           EVEN A FUTURE ACCEPTANCE AUTHORIZES NO CODE, NO TEST, NO KEY, NO
           OR-3, NO OR-4, NO INSTALL AND NO ACTIVATION. Separate
           inactive-scaffold, runtime-implementation and one-shot atomic-handoff
           authorizations all remain required and none exists.
```

---

## §8. What this closure does not claim

It is not a review. It does not claim the pair is correct, only that the three
Majors were addressed in the produced bytes and that the figures above recompute.
It claims no freshness, monotonicity or rollback-resistance property. It is
evidence for nothing and satisfies no `OR` step. Where it and the bytes differ,
the bytes govern.

---

## §9. Bounded final X/Y questions

These are the only questions this round asks. They are confined to executable
totality and byte identifiability.

```text
Q1  TWO-PHASE TOTALITY. Is SC-9 plus SC-10 total and fail-closed, and does
    KV_FORBIDDEN_TARGET now dominate EVERY skip and error token in BOTH phases?
    Specifically: can any handle-table state reach a _killpg while a
    current-generation entry names a protected group — including via a stale
    entry, a malformed value, an SC-8 structural violation, a KG-1 result other
    than PRESENT_VALID, a second write of pgid_or_null, or an ordering an
    implementer could read as permitted?

Q2  ZERO-SIGNAL PROOF AND PERMUTATIONS. Does the Y counterexample now yield
    EXACTLY ZERO signals, and do the permutation fixtures cover position, role,
    state, ownership and all four protected values without leaving a
    position-dependent or value-dependent hole?

Q3  KG-1 EXECUTABILITY. Does G0..G5 return PRESENT_VALID on an ordinary Linux
    /proc/<pid>/stat line, and does it refuse every malformed form named — a
    missing final ")", a short token list, a wrong-length or out-of-set state
    character, a signed or whitespace-bearing or overflowing integer, and a pgrp
    of 0? Is the closed nine-character set the right fail-closed choice, or does
    a state character this contract can actually encounter fall outside it?

Q4  KG-2 HONESTY. Is the Part 1 / Part 2 split honest — is anything in Part 1
    actually new, and is anything in Part 2 actually derivable from the clause
    it is paired with? Do P-1..P-7 cover every creation and failure path with no
    residue, and does the repair still bind no _getpgid and expand no import
    surface?

Q5  BYTE IDENTIFIABILITY. Given composite v1.12's bytes, do binding §2.2.1's
    sentinels, §2.2.2's pinned block and §2.2.3's splice determine the
    post-selection Cell-2 bytes UNIQUELY — is there any residual prose choice,
    any overlapping range, or any way two conforming implementations could
    differ by one byte? Do the D1 and D2 arrays, under PN and contiguous-substring
    matching, produce zero false positives against every retained class and zero
    false negatives against every forbidden vector?

Q6  THE §P1-10.3 BOUNDARY, AND IT IS THE ONE PLACE THIS ROUND DELIBERATELY
    STOPPED. §P1-10.3's summary phrase "a non-integer field ⇒ UNPARSABLE" is
    ambiguous as to the state field it names, and read strictly it carries the
    same shape of defect M-2 named in KG-1. v2.12 left it untouched as outside
    R1..R5 and gave KG-1 a self-contained grammar that governs this classifier
    alone. IS THAT BOUNDARY RIGHT, or must §P1-10.3 be repaired — and if so, is
    that this round's defect or the next round's work?

Q7  ACCOUNTING AND SWEEP. Do 67 / 81 / 75 recount from the produced bytes, did
    every dependent literal move with them, and did the maintenance sweep leave
    any logged item — or any newly created stale literal — behind?
```

---

## §10. Exact next boundary

```text
THIS CLOSURE AUTHORIZES: two independent bounded reviews, X and Y, of the same
new bytes. Nothing else.

EXPLICITLY NOT AUTHORIZED
  no acceptance of I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_
    AMENDMENT_V1_9; the V1_8 and V1_7 tokens are retired and must not be signed
  no inactive-scaffold authorization; no code at any allowed path, including the
    oracle and the contract module
  no runtime implementation authorization
  no key, entropy, seed, Stage A or Stage B
  no OR-3, no OR-4, no OR-5..OR-11, no one-shot atomic-handoff authorization
  no identity-token acceptance and no bounded weakening under any name
  no T activation and no programme-claim movement
  no edit to any governing, historical, code, test, signature or runtime path
  no commit

T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, OBSERVATION-ONLY
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
P1 IDENTITY-OBSERVATION IMPLEMENTATION SURFACE = OUT OF SCOPE, NO CODE
P1 WATCHDOG-FREEZE CELL = SELECTED: OPTION W-B, SENSOR-ONLY
WATCHDOG AUTHORITY AMENDMENT V1.9 = NOT ACCEPTED
INACTIVE-SCAFFOLD AUTHORIZATION = NOT GRANTED
RUNTIME IMPLEMENTATION AUTHORIZATION = NOT GRANTED
ONE-SHOT ATOMIC-HANDOFF AUTHORIZATION = NOT GRANTED
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
XS-1 COMBINED IDENTITY BINDING = BLOCKED ON SEPARATELY REVIEWED AND ACCEPTED
  BOUNDED WEAKENING
```

```text
READY_FOR_OFFICINA_P1_WB_V2_12_FINAL_XY_REVIEW
```

The exact selected token and the formal selection signature govern. This closure
is an untrusted author self-assessment and is normative for nothing.
