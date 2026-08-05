# Officina P1 W-B v2.12 — final independent X-line review

**Reviewer:** Claude Code Opus 5, **independent X-line reviewer only**. Not the
governing-pair repair author, not the Y line. This review is read-only: no
governing, historical, code, test, signature or runtime artifact was modified,
nothing was staged or committed, and exactly one file — this one — was created.

**Repository:** `/home/master/llm_projects/philosophia`. The prompt names commit
`9be5148` (`Repair executable W-B contract in v2.12`); `HEAD` at review time is
`bd52991` (`Request final executable W-B v2.12 reviews`), which adds only the
review-request bytes. **All six pinned inputs were recomputed from disk and all
six MATCHED**, so the bytes reviewed are the bytes commissioned.

`T = NOT_ACTIVATED`. Programme claim `OPEN`. W-B is signed and was not reopened.
`OR-2` alone is complete; `OR-3`..`OR-11` remain unauthorized.

The author closure `reviews/opus5_officina_p1_wb_v2_12_governing_repair_closure.md`
was treated as **untrusted**. Every figure below was recomputed from the produced
bytes. Where a figure and the closure disagree, the bytes govern and the closure
is named as the defect.

---

## §1. Verdict

```text
REVISE_OFFICINA_P1_WB_V2_12
```

Two **executable Major** defects survive in the produced governing bytes.

```text
X-M1  MAJOR, EXECUTABLE.  KV-5 AND KV-4 MASK KV-6's FRESH-OBSERVATION CONJUNCT
      IN PHASE P1. SC-6's first-failing-predicate rule and KG-2 P-6's dominance
      sentence return DIFFERENT ANSWERS on the same handle table, and under the
      SC-6 reading a _killpg IS REACHED while a current-generation entry's
      freshly observed process group is a member of the protected set G.
      This is Sol's M-1 surviving at the one conjunct Phase P0 cannot cover.

X-M2  MAJOR, EXECUTABLE.  A STALE ACCOUNTING LITERAL SURVIVED THE FORCED SWEEP.
      Composite v1.12 line 7227, test row 89-adjacent row 108, still reads
      "a members array of any length other than 77 is a STRUCTURAL failure".
      The enforced cardinality is 81 at MS-8, TS-3, CK-6, TS-5 B7/B17 and
      IR-13 row 38. The closure's §5.2 lists this exact literal as moved. It
      did not move.
```

Everything else this round claimed is confirmed. The two-phase structure is
sound against the recorded-group attack surface, `KG-1` is executable and
fail-closed, the Cell-2 splice is byte-unique, the `D1`/`D2` arrays reproduce
exactly, and the `67 / 81 / 75` accounting recounts to the byte with one
exception. The defects above are narrow and both are repairable without
reopening `W-B` or touching any signed surface.

---

## §2. Method

All verification was performed in a session scratchpad, over copies of the
repository bytes, with no write to any repository path and no contract
execution. Specifically: no `/proc` was read against any process of this
contract, no freeze was executed, requested, journalled or witnessed, no
governing module was imported or compiled, and no `_killpg` was called — the
classifier model records intended signals and never issues one. One read of the
reviewing interpreter's own `/proc/self/stat` was taken purely as a **parser
fixture** for `KG-1`; it creates no artifact and touches no governing path.

---

## §3. `Q1` — two-phase totality and protected-group dominance

> *Is `SC-9` plus `SC-10` total and fail-closed, and does `KV_FORBIDDEN_TARGET`
> now dominate EVERY skip and error token in BOTH phases?*

**Partly. Phase P0 is total and fail-closed against the RECORDED group. Phase P1
is not total against the FRESHLY OBSERVED group, and that is `X-M1`.**

### §3.1 What holds

I built an executable model of `SC-9` `P0-1`..`P0-7` and `SC-10`
`P1-1`..`P1-6` directly from the bytes of §P1-10.7 and drove it adversarially.
The following all confirm:

```text
P0-1 precedence            nothing precedes Phase P0; no KV skip can mask it
P0-2(a) fail-closed        PCS self-observation not PRESENT_VALID => terminal,
                           zero signals
P0-2(b) both forms         watchdog pid AND non-NULL watchdog recorded group
                           both enter G, so an unrecorded watchdog group is
                           still unreachable
P0-2(c) fail-closed        SPAWNING_GROUP.json absent, unreadable or with a
                           non-conforming process_group_id => terminal, zero
                           signals; never unknown-and-proceed
P0-3 totality              every current-generation entry visited regardless of
                           role, ownership, state, fd_delivery and candidacy
P0-5 stale                 a stale entry is not examined by the group test and
                           grants no scope, because it grants no scope at all
P0-6 malformed             bool pgid_or_null (type(x) is int), role outside the
                           signed literals, malformed generation_id, non-mapping
                           table, wrong-shaped KG-1 return, any BaseException
                           => SC-8 STRUCTURAL_VIOLATION, classifier terminates,
                           zero signals
SC-8 parity                equally terminal, equally silent, in both phases
P1-2 / P1-3                all results collected before any signal; a protected
                           RECORDED group found after other candidates are
                           already KV_OK discards them rather than signalling
P1-6                       the four-part conjunction is stated so a build fails
_killpg reachability       reachable only from SC-10 P1-5
```

`_getpid` **is** bound at §P1-3.4, so `P0-2(a)`'s
`PGRP_OBSERVE(_getpid())` is executable rather than an unbound-name defect of
the shape `M-2` named. `_getpgid` is bound nowhere and is not added.

### §3.2 `X-M1` — the path to `_killpg` with a protected group present

`KV-6` has two conjuncts. The first tests `h.pgid_or_null`; Phase P0 already
covers it, and that is the `M-1` repair. The second — new in v1.12 — tests **the
`pgrp` of the `KV-3` observation of this same evaluation**, and Phase P0 cannot
cover it, because `P0-7` states that no P0 observation is carried into P1 and
`P0-4` tests only the recorded field.

`SC-6` then says, in terms:

```text
Within Phase P1, evaluation of a candidate stops at the FIRST failing
predicate, so every candidate yields EXACTLY ONE token:
  ...
  KV-5 fails    => KV_GROUP_MISMATCH          SKIP this group
  KV-6 fails    => KV_FORBIDDEN_TARGET        TERMINATE THE CLASSIFIER
```

`KV-5` fails **exactly when** the freshly observed `pgrp` differs from the
recorded `pgid_or_null`. That is precisely the condition under which the fresh
`pgrp` can be a protected value that the recorded field is not. So the one
predicate whose failure is guaranteed to precede a protected fresh observation
is ordered **before** the conjunct that would detect it.

**The counterexample, stated so a build can be failed on it.**

```text
HANDLE TABLE, current generation, two entries, PCS group 1000, recorded
supervisor group 2000:
  a   role CONTROLLER, state RUNNING, ownership OWNED, pgid_or_null 600,
      PRESENT_VALID, identity matching, observed pgrp 600
  b   role CONTROLLER, state RUNNING, ownership OWNED, pgid_or_null 601,
      PRESENT_VALID, identity matching, observed pgrp 2000
      — the live process has migrated into the RECORDED SUPERVISOR GROUP

PHASE P0   b.pgid_or_null is 601, which is NOT in G. a is 600, NOT in G.
           P0 completes clean. This is correct under P0-4 as written.
PHASE P1   a  -> KV_OK
           b  -> KV-5 fails (2000 != 601) -> KV_GROUP_MISMATCH, SKIP.
                 KV-6 IS NEVER EVALUATED FOR b.
P1-6       (i) P0 clean; (ii) every entry evaluated; (iii) no evaluated entry
           yielded KV_FORBIDDEN_TARGET; (iv) re-verified at the instant.
           ALL FOUR HOLD. THE SIGNAL IS AUTHORIZED.
RESULT     _killpg(600, 15) and _killpg(600, 9) ARE ISSUED from a table in which
           a current-generation handle's live process sits inside the
           supervisor's process group.
```

My model reproduces this: the run labelled *late discovery* returns
`(None, None, [('_killpg', 600, 15), ('_killpg', 600, 9)])`.

**`KV-4` masks it identically.** On a start-identity mismatch `KV-4` fails
first, `OWNERSHIP` is set `CONTRADICTED`, the group is skipped, and `KV-6` is
never reached — while the fresh observation whose `pgrp` may be protected has
already been taken. A reused pid landing in the supervisor group is the ordinary
way this arises, not an exotic one.

**The contract contradicts itself here rather than being merely silent.**
`KG-2` `P-6` states the opposite answer explicitly:

> *"AND THE PROTECTED-GROUP TEST DOMINATES BOTH: if the FRESHLY OBSERVED `pgrp`
> is a member of `SC-9`'s protected set, `SC-10` terminates the WHOLE classifier
> with `KV_FORBIDDEN_TARGET`, and no mismatch skip is recorded in its place."*

and `SC-6`'s own dominance paragraph agrees — *"`KV_GROUP_MISMATCH` … NEVER
SUPPRESS IT"*. But `SC-6`'s operative mechanism is the enumerated
first-failing-predicate table, which mechanically produces exactly that
suppression. `SC-3` and `P1-1` say `KV-1`..`KV-6` are evaluated *"IN FULL, IN
THAT ORDER"*, which on one reading forces all six and closes the hole; `SC-6`
says evaluation *stops at the first failing predicate* and that every candidate
yields *exactly one* token, which is the more specific rule and does not.

**Two conforming implementations therefore differ on this table, and one of them
signals where the contract's own dominance rule requires zero signals.** That is
executable, it is in the sole `W-B` endpoint-loss executor, and it is not
closed by any fixture: test row 89's permutation set varies only *which recorded
protected value* is named, and its clause (4) fails a build only when a later
entry *yields* `KV_FORBIDDEN_TARGET` — here the later entry yields
`KV_GROUP_MISMATCH`, so row 89 passes a nonconforming build.

**What a repair needs.** `KV-6`'s protected-group test must be evaluated for
every candidate that reached a `KV-3` `PRESENT_VALID` observation, before
`KV-4` and `KV-5` may consume the entry — or, equivalently, `SC-6`'s ordering
must be stated with `KV-6` promoted ahead of `KV-4`/`KV-5` for the fresh
conjunct, with `SC-5`'s single-token rule restated so the terminal wins. Row 89
then needs one further fixture: *recorded group unprotected, freshly observed
group protected, in the same table as a valid candidate* — expected result, the
same zero-signal terminal.

### §3.3 The other paths Q1 names, all clean

```text
via a stale entry                  NO — P0-5, and a stale entry grants no scope
via a malformed value              NO — SC-8, terminal in both phases
via an SC-8 structural violation   NO — equally terminal, equally silent
via a KG-1 result != PRESENT_VALID NO — KV-3 skips; the group enters no sequence
via a second write of pgid_or_null NO — KG-2 P-3, SC-8 structural violation
via a NULL recorded group          NO SIGNAL REACHES A PROTECTED GROUP. Noted at
                                   §9 L-X7: P0-4 tests only the recorded field,
                                   so an entry whose recorded group is NULL but
                                   whose live process sits in a protected group
                                   is invisible to P0. It contributes no scope
                                   and KV-2 refuses it, so the outcome is safe;
                                   only SC-6's phrase "a protected group ANYWHERE
                                   in the table" is broader than the test.
```

---

## §4. `Q2` — the Y counterexample and the permutation fixtures

> *Does the Y counterexample now yield EXACTLY ZERO signals, and do the
> permutation fixtures leave a position-dependent or value-dependent hole?*

**Yes to both, for the recorded-group form the fixtures cover. Reproduced
mechanically.**

The exact `Y-CE-1` table of §P1-10.7 — `h1` current generation, `CONTROLLER`,
`RUNNING`, `CONTRADICTED`, `pgid_or_null` = the `SPAWNING_GROUP.json`
`process_group_id`; `h2` a valid unprotected `CONTROLLER` — returns:

```text
terminal   PCS_FREEZE_CLASSIFIER_FORBIDDEN_TARGET
qualifier  FREEZE_NOT_ATTEMPTED
signals    []   — EXACTLY ZERO, including none to h2's group
```

Under v1.11's rule the same table authorized `_killpg(h2, 15)` and
`_killpg(h2, 9)`. The repair is real.

**The permutation sweep, run exhaustively rather than asserted.** I ran the
full cross-product the bytes require:

```text
protected value   4  { PCS own group, watchdog leader group, watchdog pid,
                       recorded supervisor group }
role              3  { CONTROLLER, WORKER, WATCHDOG }
state             4  { SPAWNED, STOPPED, RUNNING, REAPED }
ownership         3  { OWNED, CONTRADICTED, REAPED }
table size        5  n = 1..5
position          every position 1..n, including first, every interior, last,
                     and as the only entry
                  ------------------------------------------------------------
                  2160 fixtures

OUTCOMES OTHER THAN THE ZERO-SIGNAL PHASE-P0 TERMINAL:  0 of 2160
```

Every fixture returned
`PCS_FREEZE_CLASSIFIER_FORBIDDEN_TARGET` / `FREEZE_NOT_ATTEMPTED` / zero
signals. There is **no** position-dependent, role-dependent, state-dependent,
ownership-dependent or value-dependent hole in the recorded-group form.

A control table — two valid unprotected candidates plus a watchdog — correctly
produces `_killpg` at 15 and 9 for each distinct group, so the classifier is not
trivially terminal.

**`FREEZE_NOT_ATTEMPTED` is not an eighth token.** `SC-5` enumerates exactly
seven and says so; `SC-9` `P0-4` says so; test row 101 says so and fails a build
that implements it as an `SC-5` token, as a per-group result, or as an `FC-1`
code. The twenty-five-code `FC-1` set is untouched. Confirmed in both files.

**The gap this question does not reach** is `X-M1`: the fixtures vary which
*recorded* value is protected and never vary the *freshly observed* one.

---

## §5. `Q3` — `KG-1` executability on ordinary and adversarial stat lines

> *Does `G0`..`G5` return `PRESENT_VALID` on an ordinary Linux
> `/proc/<pid>/stat` line, and does it refuse every malformed form named?*

**Yes. `M-2`'s `Y-CE-2` is repaired.** I implemented `G0`..`G5` verbatim from
the bytes and ran it against a real line and against every adversarial class.

**Ordinary lines.** A real `/proc/self/stat` line read on this host returns:

```text
1457751 (python3) R 1457731 1457751 1457731 0 -1 4194304 1001 0 0 0 0 0 ...
  ->  PRESENT_VALID  (start_identity 44784666, ppid 1457731, state 'R',
                      pgrp 1457751)
```

Under v1.11 this line was `UNPARSABLE` and no signal was ever authorizable.
Note that the real line carries `-1` at the tty-pgrp field; because `G3`/`G4`/`G5`
parse only `TOKEN(2)`, `TOKEN(3)` and `TOKEN(20)`, a negative value elsewhere
does not break the parse. Synthetic ordinary lines carrying **each** of the nine
permitted state characters all return `PRESENT_VALID`.

**Adversarial forms — every one refused, and refused as the bytes say.**

```text
no final ")"                                  UNPARSABLE
fewer than twenty tokens (18, 19)             UNPARSABLE   (20 -> PRESENT_VALID)
state "W", "x", "K" (pre-3.13 characters)     UNPARSABLE
state token of length 2                       UNPARSABLE
state token "0" — the v1.11 integer reading   UNPARSABLE
pgrp 0, and pgrp "00"                         UNPARSABLE   (G4, both forms)
pgrp "-1", "+7"                               UNPARSABLE   (sign byte)
ppid 20 digits, and 19 digits > INT64_MAX     UNPARSABLE   (overflow bound)
ppid exactly 9223372036854775807              PRESENT_VALID  — bound is inclusive
start_identity "887.7", "-1", "+1", "1_0",
  "0x10", 20 digits, INT64_MAX+1              UNPARSABLE
pgrp 9223372036854775808                      UNPARSABLE
tab separators, multiple spaces, no trailing
  newline, CRLF                               all resolve through G0's separator
                                              set and token count with no silent
                                              absorption
empty buffer, ")" alone                       UNPARSABLE
comm containing ")" and a separator           PRESENT_VALID, correctly aligned —
                                              G0's LAST-")" rule is the right
                                              adversarial choice, since nothing
                                              after comm contains ")"
leading zeros "007", "0007"                   PRESENT_VALID, read as base ten
```

**Is the closed nine-character set the right fail-closed choice?** Yes. It is
exactly `task_state_array` of `fs/proc/array.c` for the 5.x and 6.x series:
`R S D T t X Z P I`. The processes this classifier observes are the PCS itself
and the PCS's own children, which on those kernels take `R S D T t X Z I`; `P`
is kernel-thread-only and is admitted anyway. No state character this contract
can encounter falls outside the set. The direction is fail-closed regardless: an
`UNPARSABLE` result authorizes no signal of any number to any group.

One descriptive note, logged at §9 `L-X4`: the provenance sentence names *"the
5.x and 6.x series, which is the kernel series this contract runs on"*, while
this host reports `Linux 7.0.0-28-generic`. The set is nonetheless correct in
fact — the real 7.x line above parsed `PRESENT_VALID` — so this is a stale
range in a provenance sentence, not a parse defect.

---

## §6. `Q4` — `KG-2` Part 1 / Part 2 honesty and path coverage

> *Is the Part 1 / Part 2 split honest? Do `P-1`..`P-7` cover every creation and
> failure path with no residue?*

**Yes on all three counts.** I checked each row against the clause it names.

**Part 1 rows are genuinely derived, and nothing in Part 1 is new.** Spot-checked
against the live bytes:

```text
KG-1 structure  §P1-10.3 does carry the single full read, the five-way result
                set, the errno map and the "20th token after the final )" rule
KV-2            §P1-8.5 line 1457 does refuse BOTH signal opcodes for a
                WATCHDOG handle; §P1-10.1's OWNED-iff rule and §P1-10.6 are as
                cited
KV-5            §P1-8.5 does declare pgid_or_null; §P1-7.5 c10 does require the
                reported process_group_id to equal the kernel's answer
the pgid_or_null field exists, and _killpg requires a kernel-verified group
                §P1-8.5 "SIGNAL_GROUP additionally requires a kernel-verified
                group" and §P1-10.5 "killpg is used only against a
                kernel-verified group" — correctly SEPARATED OUT as their own
                rows rather than conflated with KG-2, which was the v1.11 defect
```

**Part 2 rows are genuinely new, and none is derivable from its paired clause.**
The two load-bearing pairings check out exactly:

```text
P-2 population point   §P1-7.5 c10 verifies the MIDDLE CHILD's group — "getsid
                       and getpgid of that pid both equal middle_child_pid" —
                       and says nothing whatever about child handles. Applying
                       that shape to a CHILD handle is new content and Part 2
                       says so.
KG-1 G1 / G2 / G4      §P1-10.3 names a "state field" and fixes no character
                       set; says only "a non-integer field => UNPARSABLE" and
                       defines no token grammar; constrains pgrp's value
                       nowhere. All three confirmed against the unchanged bytes.
```

**The v1.11 falsehood is withdrawn.** The sentence *"the one supporting rule the
live pair did not already carry is `KG-1`'s process-group field"* is stated as
withdrawn and false, at `§A0.3` `R2` and in the Part 2 header.

**`P-1`..`P-7` are total over the decision tree, with no residue.** The tree is
{creation succeeded?} × {verification attempted?} × {observation `PRESENT_VALID`?}
× {identity equal?} × {`pgrp == pid`?}, plus release and reap:

```text
creation fails                                  no field exists
handle exists, no verification attempted        NULL (P-1)
observation ABSENT / UNREADABLE / UNPARSABLE
  / ERROR                                       NULL, retryable, first success
                                                is still the only write
PRESENT_VALID, identity MISMATCHES              no write ever; CONTRADICTED
                                                irreversibly
PRESENT_VALID, identity matches, pgrp != pid    NULL forever (P-4)
PRESENT_VALID, identity matches, pgrp == pid    the one write (P-2)
released or reaped                              frozen, not cleared, not reused
```

Every leaf is assigned exactly one value and no leaf is discretionary. The
"identity not yet recorded" case falls under *no verification attempted* and is
covered. `P-3`'s second-write prohibition routes to `SC-8`, and `P-4`'s
role-independent population is correctly load-bearing for `SC-9` `P0-2(b)` and
`KV-6(b)` while remaining harmless, because `KV-2` refuses role `WATCHDOG` at
every state and ownership.

**No import surface moves.** `_getpgid` occurs three times across the pair and
every occurrence is a **negation** ("`_getpgid` IS NOT BOUND"). `§P1-3.2`'s
allowlists gain no name; `MS-11`'s 89 rows, canonical length 20534 and digest
`aa974e0c…c20ee` are byte-unchanged; `MS-13` is unchanged; `S-12` is retained.

One pre-existing observation, logged at §9 `L-X6` and **not** a defect of this
round: `§P1-7.5` `c10` requires a `getpgid` answer while `§P1-3.4` binds no
`_getpgid`. That predates `R1`..`R5` and is orthogonal to the no-expansion claim,
which is about what v2.12 added.

---

## §7. `Q5` — byte identifiability of the Cell-2 splice, and the `D1`/`D2` arrays

> *Do the sentinels, the pinned block and the splice determine the
> post-selection Cell-2 bytes UNIQUELY? Do `D1`/`D2` produce zero false
> positives and zero false negatives?*

**Yes to the Cell-2 splice, exactly. Yes to `D1`/`D2`, reproduced to the byte.**

### §7.1 The splice — reproduced exactly

Every figure recomputed from composite v1.12's bytes:

```text
begin sentinel  "### Cell 2 — `AUTHOR_CELL_..._MECHANISM`, new in v1.3"
                cardinality 1, at line 55                                MATCH
end sentinel    "decisions — whichever way they go — land in a document
                 that is otherwise ready."
                cardinality 1, at line 95                                MATCH
span            41 lines, 2184 UTF-8 bytes                               MATCH
span SHA-256    1623dc45bb5c17c507ca590c3d6ca2a171ed7e40e5c4f287a8a736ee860db2b8
                                                                         MATCH
```

The replacement block, extracted by the binding's **own** stated rule — the
lines strictly between the `REPLACEMENT-BYTES` fence and the first subsequent
line equal to three backticks, each including its `0x0A`:

```text
opening fence cardinality 1, at binding line 337; closing fence line 375
no line of the replacement is itself a fence line                        MATCH
replacement     37 lines, 2120 UTF-8 bytes                               MATCH
replacement SHA f2782a63db003dfb370d0c0c5afb9c928a8fc61c8af29285c8a1172657a84fee
                                                                         MATCH
no BOM, LF only, no CR anywhere, final byte 0x0A                         MATCH
```

**Uniqueness holds.** There is exactly one replaced range `[b, e]`; both
sentinels are unique under whole-line equality; the span digest is verified
before the splice proceeds; the replacement is a literal verified by digest; and
step 6 is a total concatenation. No implementer chooses any boundary, sentence
or word. **Two conforming implementations given composite v1.12 emit
byte-identical Cell-2 output.** `L-X6` — v2's overlapping semantic line-action
table, in which lines 58, 60, 85 and 88 each appeared twice with different
actions — is gone: there is no action table at all.

`CT-5` also holds structurally: line 55 is after every byte of Cell 1, so `OR-4`
edits no byte of Cell 1 and the process-claim blocking notice this signature does
not discharge stands unchanged.

**One false property statement, logged at §9 `L-X1`.** §2.2.2 asserts:

> *"NON-ASCII CHARACTERS — the block contains the U+2014 EM DASH at two loci and
> no other non-ASCII character"*

The pinned bytes contain `U+2014` twice **and `U+00A7` SECTION SIGN five times**
(replacement lines 13, 24, 29, 30, 31). The claim is false against the bytes it
describes, and the closure §3.3 repeats it. It is **not** an executable defect:
§2.2.3 step 6 names the SHA-256 as the sole verification of the replacement, the
digest reproduces, and the output bytes are unaffected. It is a false audit
sentence that should be corrected to say "`U+2014` at two loci and `U+00A7` at
five, and no other non-ASCII character".

### §7.2 `D1` and `D2` — reproduced exactly

Transcribing the arrays from §2.6.2 and §2.6.3 and serializing under `MS-0`
`CANON` — JSON array, order preserved and never sorted, no whitespace outside
string literals, every character outside printable ASCII escaped `\uXXXX`, one
trailing `0x0A`:

```text
D1  11 literals   926 bytes   d5b375c518c935d3a6935a1932bf6bfa237cb9c99c7b81913f4e1433142b6c1e
                                                            LENGTH MATCH, SHA MATCH
D2  13 literals  1044 bytes   4e2120857dd67124095e5f5479d69cbf7ba703605abb3448a2fe414b3ff8a15c
                                                            LENGTH MATCH, SHA MATCH
```

`PN` was implemented as `NORMALIZE(STRIP_LEAD(bytes))` with `NORMALIZE` taken
verbatim from composite §P1-14.2 (UTF-8 decode, NFC, ASCII lowercase, delete
`*` `_` backtick and the HTML-comment opener and closer, collapse whitespace
runs to one space, strip) and `STRIP_LEAD` deleting leading `0x20 0x09 0x3E`
repeatedly per line.

**Coverage, checked rather than asserted.**

```text
each of the 11 D1 literals occurs in PN(pre-resolution Cell-2 span)    11 of 11
each of the 13 D2 literals occurs in PN(composite v1.12)               13 of 13
```

So the coverage claim is verified, and the `INCOMPLETE` condition the oracle
would report does not arise.

**False positives — zero, against every retained class I could test directly.**

```text
the §2.2.2 pinned replacement bytes           D1 0   D2 0
Cell 1, byte-unchanged (the sharpest case)    D1 0   D2 0
```

Cell 1 is the sharp case exactly as the binding argues: its notice reads
*"…until the author cell `AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS` is
signed"*, while `D1[2]` requires the continuation *"…until the watchdog-freeze
mechanism cell is signed"*. Every `D1` literal carries a watchdog-freeze-specific
discriminator, and a detector firing on Cell 1 would demand deletion of a notice
`CT-5` forbids removing. Confirmed by measurement, not by the argument alone.

`D3` is correctly the soundness half — a resolution that satisfies `D1`/`D2` by
deleting a class-R occurrence fails `D3` — and `D4` pins `H_GUARDDATA`. No
literal is a bare word: `"slot 6"`, `"socket"`, `"window"` and `"accepted"` are
absent from both arrays, which is what keeps class R clean.

The disclosed arithmetic consequence is honest: the replacement names
`P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1` once as a historical fact with no
capability, so it occurs twice in the resolved file — the `TS-1` pairing rule and
that mention — and binding §2.5's totals say so rather than hiding it.

### §7.3 The census and the digests, all recomputed

```text
marker-bearing lines, composite      20   at 79 80 83 305 306 1656 1659 1666
                                          1670 1907 1910 1932 1933 2959 3242
                                          3248 7179 7207 7218 7317        MATCH
[W-A] / [W-B] occurrences          13 / 13                                MATCH
both-marker lines, whole file          6   83 2959 7179 7207 7218 7317    MATCH
both-marker lines, body only           4   2959 7179 7207 7218            MATCH
amendment marker-bearing lines         0                                  MATCH
region sentinels, each cardinality 1   BODY 251/7277, GUARDDATA 7279/7320,
                                       PROVENANCE 7322/7527               MATCH
H_BODY       d5125d54e312fd87fff7c622cedf8538ef2ea99c9666ec619becfd2e4651a1e6  MATCH
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426  MATCH
H_NORMATIVE  0d3b411e6f92c37f759025d71af6fa59d7b648a0106869829c30c1917b490d66  MATCH
H_FILE       e796d9e8838b160cc76a3c14814881ac38a0b2a6568ee3103c1286334e5f729b  MATCH
attested_pid / attested_pgid       0 / 0 in both files                    MATCH
```

Every one of the twenty loci in §2.3's table lands on the line and marker the
table names.

**One scope note, logged at §9 `L-X3`, and it is not a defect of the `M-3`
repair.** §2.2 pins Cell 2 byte-exactly; §2.3's sixteen **body** loci are
specified in prose, including four `EDIT IN PLACE` both-marker lines where the
`[W-A]` text must be excised and the remainder rewrapped — for example lines
305/306, where the W-A sentence spans a line break. No post-`OR-4` digest is
pinned anywhere (`PO-7` says only that `H_BODY`, `H_NORMATIVE` and `H_FILE`
change), so two implementations could differ by a byte in line wrapping and no
stated check would see it. `Q5` is scoped to the Cell-2 bytes and the answer
there is a clean yes; `M-3` and `L-X6` were both raised against the Cell-2
transformation and both are discharged. The body-locus surface is a distinct,
pre-existing gap that neither line has previously raised, `OR-4` is not
authorized, and it should be pinned before it is.

---

## §8. `Q6` — the `§P1-10.3` boundary

> *Is that boundary right, or must `§P1-10.3` be repaired — and if so, is that
> this round's defect or the next round's work?*

**The boundary is right. `§P1-10.3` is properly isolated and does not conflict
operatively with `KG-1`. It is the next round's work, not this round's defect.**

`§P1-10.3` is byte-identical to v1.11 at the same offsets; v2.12 edited nothing
there. Its summary phrase reads:

> *"parse the 20th whitespace-separated token after the final `)`, which is the
> kernel start time, together with the state field and the ppid field: no final
> `)`, a short token list, a non-integer field, or any parse failure ⇒
> `UNPARSABLE`"*

Three findings.

**It is genuinely ambiguous, but it is weaker than the defect `M-2` named.**
v1.11's `KG-1` said in terms that a **non-integer state** is `UNPARSABLE` — an
explicit misclassification of a field that is never an integer. `§P1-10.3` names
the state field separately and never asserts it is an integer; the strict reading
that "field" sweeps in the state field is available but is not the only one. So
the two clauses carry the same *shape* of ambiguity at very different strengths.

**There is no operative conflict with `KG-1`.** `KG-1` defines `PGRP_OBSERVE` as
its own function over its own buffer and says in terms that its grammar governs
this classifier's parse and nothing else, that `§P1-10.3` is unchanged, and that
every existing `STAT_OBSERVE` consumer is unchanged. The freeze classifier never
calls `STAT_OBSERVE`, and `§P1-10.3`'s consumers — `§P1-10.4`'s
`IDENTITY_OBSERVE` decision table — never call `PGRP_OBSERVE`. The two grammars
do not meet, so the isolation is real rather than declared.

**The strict reading of `§P1-10.3` is fail-closed, not fail-open.** Under it
every ordinary observation is `UNPARSABLE`, which at `§P1-10.4` row `I-7` means
identity capture is unavailable while ownership still authorizes the §P1-10.5
signal schedule. That degrades durable-record constructibility; it opens no kill
path. So it does not meet the executable-Critical/Major bar that returns
`REVISE`, and it is correctly outside `R1`..`R5`: editing the identity observer
would move a clause this round had no licence for and would perturb consumers
this round had no licence to touch.

**Recommendation.** `§P1-10.3` should be repaired in the next round — not by
importing `KG-1`'s grammar, but by the one-clause disambiguation that its
"fields" means the start-time and `ppid` tokens and that the state field is a
state character. Deferring it costs nothing operative today.

---

## §9. `Q7` — the `67 / 81 / 75` accounting and the maintenance sweep

> *Do `67 / 81 / 75` recount from the produced bytes, did every dependent literal
> move with them, and did the sweep leave anything behind?*

**The three headline figures recount exactly. One dependent literal did not
move, and that is `X-M2`.**

### §9.1 The figures, recounted from the bytes

```text
MS-2 literal rows                67   COUNTED 67, all 67 paths distinct   MATCH
MS-3 literal rows                 7   COUNTED  7, all distinct            MATCH
MS-1 literal member paths         2   _AMENDMENT_V1_9_DRAFT.md and
                                      _COMPOSITE_V1_12.md                 MATCH
MS-8 / TS-3 member_count         81   2 + 67 + 7 + 1 + 1 + 2 + 1 = 81     MATCH
composite provenance rows        75   COUNTED 75, all 75 paths distinct   MATCH
                                      = 67 M2 + 7 M3 + 1 baseline
member classes                    7   seven, no eighth                    MATCH
```

Three further integrity checks the closure did not claim, all of which pass:

```text
M2 and M3 path sets are DISJOINT — intersection empty, so the v2.4 overlap
  defect has not returned
M2 and M3 are both SUBSETS of the provenance region; the single provenance row
  outside them is exactly src/philosophia/officina/verification.py, the
  non-enforced baseline
ALL 75 PROVENANCE DIGESTS AND ALL 67 MS-2 DIGESTS WERE RECOMPUTED FROM THE
  FILES ON DISK: 0 mismatches, 0 absences. The provenance digests and the
  MS-2 / MS-3 literals agree with each other everywhere.
```

The four new rows — amendment v1.8, composite v1.11, the Fable v2.11 X review
and the Sol v2.11 Y review — are present in `MS-2` and in the provenance region,
and their recorded digests match the bytes on disk.

### §9.2 Generation strings and retired literals — swept clean

```text
..._AMENDMENT_V1_8 / _V1_7 as acceptance tokens     0 occurrences, both files
P1_WATCHDOG_V2_8 / V2_9 / V2_10 / V2_11_PRE_
  SELECTION_COMPOSITE_SHA256                        0 occurrences, both files
P1_WATCHDOG_V2_12_PRE_SELECTION_COMPOSITE_SHA256    6 amendment, 1 composite
the anchor VALUE e796d9e8…f729b                     exactly 1 line, amendment
                                                    only; equals composite
                                                    v1.12's H_FILE
"a 70th entry" as a live fixture literal            0 — the only occurrence is
                                                    the §A0.3 record of the
                                                    repair itself
"an 82nd entry"                                     1 amendment, 2 composite
```

`N-16`'s stale `69` is repaired to `81`. `H-4` now names `CK-7` as sole owner of
`HISTORICAL_BYTE_MOVED` with `CK-12` owning `INSTALL_RECORD_NAME_MISMATCH`, and
it sits inside the canonical block so it lands in both files. Row 106 declares
**ten** groups `(a)`..`(j)`, defines all ten, and states there is no group `(k)`
— `L-X1` of the v2.11 round is discharged, and ten was preferred over inventing
an eleventh fixture, as required. Rows 103, 104, 105, 107 and 115 all carry the
new figures: row 103's `74` recorded digests is correct (67 + 7), row 107's
`81 to 80`, `82nd entry` and `67 literal provenance paths` are all correct.

### §9.3 `X-M2` — the one literal that did not move

Composite v1.12, **line 7227, test row 108**, inside `REGION(BODY)` and
therefore normative:

> *"…taking the record to 82 entries while `CK-4` still enumerates 81 from the
> constants; each is refused at `CK-6` with `MEMBER_SUBSTITUTED`, **because a
> members array of any length other than 77 is a STRUCTURAL failure** and
> `MEMBER_EXTRA` no longer exists."*

The other three figures in that same row **did** move (`78` → `82`, `70` → `74`,
`63` → `67`). This one did not. It is the only surviving occurrence of the phrase
in either file.

**Why it is executable rather than cosmetic.** `§P1-15`'s preamble states *"Every
row is a future obligation."* Row 108 does not merely describe a fixture; it
states `CK-6`'s structural rule. Against it stand `MS-8` ("exactly 81 entries"),
`TS-3` (`member_count` INTEGER, exactly 81), `CK-6` ("81 entries / 81-entry
sorted array / cardinality fixed at 81"), `TS-5` `B7` and `B17`, and `IR-13`
row 38. The authority hierarchy places §P1-14.4 and §P1-15 at the same level 2
with **no stated precedence between a definition and a test row**, so the
operative specification now asserts two incompatible cardinalities for the
install record's members array, and an implementer who builds `CK-6`'s structural
check from row 108 refuses the conforming 81-entry record — the install gate
refusing its own correct installation.

The fixture's own expected result happens not to flip, because 82 is refused
under either number. That limits the blast radius; it does not remove the
contradiction, and it is exactly the class of stale literal `Q7` asks about.

**The closure asserts the opposite.** §5.2 lists row 108 as `(78->82, 77->81,
70->74, 63->67)`. Three of the four moved. Per this round's own instruction, the
bytes govern and the closure is named as the defect.

### §9.4 Log items — descriptive, for the implementation log, none returning REVISE

```text
L-X1  §2.2.2's ENCODING block says the pinned replacement carries "U+2014 at two
      loci and no other non-ASCII character". It carries U+2014 twice AND
      U+00A7 five times. False audit sentence; the digest is the normative gate
      and it reproduces, so no output byte is affected. Closure §3.3 repeats it.

L-X2  SCOPE ACCOUNTING, A REPEAT OF SOL's Q10. Closure §2.2 declares exactly six
      files, states "there is no seventh", and states "No chat-response file,
      transcript, note or scratch artifact is authored by this round." Commit
      9be5148 adds SEVEN files, the seventh being
      reviews/opus5_officina_p1_wb_v2_12_governing_repair_chat_response.md.
      The closure is untrusted and normative for nothing, so this is not
      executable — but it is the same accounting error the Y line graded last
      round, made again in the round that claimed to have repaired it.

L-X3  §2.3's sixteen body loci, including four EDIT-IN-PLACE both-marker lines
      that require rewrapping, are prose-specified rather than byte-pinned, and
      no post-OR-4 digest is pinned to detect a divergence. Out of Q5's Cell-2
      scope and out of M-3/L-X6's scope; OR-4 is not authorized. Pin it before
      OR-4 is.

L-X4  KG-1 G1's provenance sentence names "the 5.x and 6.x series, which is the
      kernel series this contract runs on"; this host reports Linux 7.0.0-28.
      The nine-character set is nonetheless correct in fact — a real 7.x stat
      line parses PRESENT_VALID — so the range in the sentence is stale, not the
      set.

L-X5  SC-3 says "NO RESULT OF PHASE P0 ... IS CARRIED TO IT" and P0-7 says "NO
      OBSERVATION TAKEN IN PHASE P0 IS CARRIED INTO PHASE P1", while KV-6 says
      in terms that G is "the PROTECTED SET built by SC-9 P0-2 at the start of
      this classifier's Phase P0" — which is a P0 result built from a P0
      observation. Both readings are fail-closed (rebuilding G in P1 yields the
      same set or terminates), so this is not executable; the sentences should
      nonetheless be reconciled, most simply by excepting G by name.

L-X6  §P1-7.5 c10 requires "getsid and getpgid of that pid", while §P1-3.4 binds
      neither _getsid nor _getpgid. Pre-existing, predates R1..R5, and orthogonal
      to v2.12's no-import-expansion claim, which concerns what this version
      added. Noted so it is not mistaken for a v2.12 regression.

L-X7  SC-6 says "a protected group anywhere in the current-generation table
      produces the terminal", but P0-4 tests only h.pgid_or_null. An entry whose
      recorded group is NULL and whose live process sits in a protected group is
      invisible to P0. The outcome is safe — it contributes no scope and KV-2
      refuses it — so only the phrasing is broader than the test.
```

---

## §10. Preserved, and verified preserved

```text
the signed W-B selection and its sensor-only semantics       NOT REOPENED
MS-11's 89-row reachable_closure, CANON length 20534, digest
  aa974e0c91e5c9afd0aceefa6b0e47ef42b5ad7b71dc4de690a4873232dc20ee  UNCHANGED
MS-13, the project-import surface                            UNCHANGED
H_GUARDDATA and the VARIANT_MARKER class                     BYTE-UNCHANGED
SC-5's seven tokens; FC-1's twenty-five closed codes         UNCHANGED
§P1-10.3 and every existing STAT_OBSERVE consumer            BYTE-UNCHANGED
identity Option A as signed external author state, with
  P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1 UNACCEPTED    UNCHANGED
every scientific contract, treatment, evidence class,
  covariate, endpoint, qualification and comparison          UNTOUCHED
the T envelope and the programme claim                       UNMOVED
```

**Negative space, verified on disk by this reviewer, not taken from the
closure:** the oracle, the contract module, their test modules, the `p1_wb`
fixture directory, both `MS-6` test modules, the two `successor/officina/`
authorization and runtime-control directories, and the two bootstrap scripts are
all **ABSENT**; `test_p1_row_NNN_` functions number **zero** repository-wide.

---

## §11. What this review does not claim

It is not an acceptance. It does not certify that the pair is correct, only that
the questions asked were answered against the bytes and that two executable
Major defects were found. It claims no freshness, monotonicity or
rollback-resistance property, is evidence for nothing, and satisfies no `OR`
step. The pre-existing dirty and untracked working-tree files — `accounting.py`
and its test module, the modified `reviews/` files, `essay/OUTLINE.md`, the
untracked `generic_harness.py` and its test module, and the untracked prior chat
responses — were neither read for behaviour, adopted, staged, reverted nor cited.

---

## §12. Exact next boundary

```text
THIS REVIEW AUTHORIZES: a bounded repair round against X-M1 and X-M2 in the
governing pair, plus the Y line's own independent verdict on the same bytes.
Nothing else.

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
    outside the two named repairs
  no commit by this review

REPAIR SCOPE, BOUNDED
  R-X1  order KV-6's protected-group test ahead of KV-4 and KV-5 for the
        fresh-observation conjunct, or require KV-6 for every candidate reaching
        a PRESENT_VALID KV-3 observation; restate SC-6's single-token rule so the
        terminal wins; add the row-89 fixture "recorded group unprotected,
        freshly observed group protected".
  R-X2  composite line 7227, row 108: "any length other than 77" -> 81.
  Optionally, and only if the author judges them in licence: L-X1's encoding
  sentence and L-X5's G-carriage wording. L-X3 and the §P1-10.3 disambiguation
  of Q6 are next-round work and are NOT in this repair scope.

T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, OBSERVATION-ONLY
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
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
REVISE_OFFICINA_P1_WB_V2_12
```

The exact selected token and the formal selection signature govern. This review
confirms no acceptance and authorizes no scaffold, code, key, `OR` step, install
or activation.
