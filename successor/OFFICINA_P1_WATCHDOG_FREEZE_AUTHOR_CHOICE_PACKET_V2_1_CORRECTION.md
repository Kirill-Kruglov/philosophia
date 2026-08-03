# Officina P1 watchdog-freeze mechanism — author choice packet v2.1 (correction)

**Author:** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This correction selects nothing.**

**No token here is signable** until a bounded independent X-line and Y-line
final confirmation round confirms this correction on identical bytes. `T` is
`NOT_ACTIVATED`; the programme claim is `OPEN`. This document creates nothing
executable and authorizes no implementation, activation, resource spend, T/Q/C
datum, outcome, Proof or claim movement.

---

## §0. What this document is

### §0.1 Base and scope

```text
BASE, carried forward in full except where §0.3 replaces it:
  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
  72212a986d9551ef47718e871a81951b55a849a10d34eb12e6276499cb675505

v2.1 IS A PATCH, NOT A REPLACEMENT. v2 is read alongside it. Every section of
v2 not named at §0.3 stands byte-unchanged and is not restated here. Where this
document and v2 differ, THIS DOCUMENT GOVERNS.

v2, v1, both v1 reviews, both v2 confirmations and the v2 closure are preserved
BYTE-UNTOUCHED as the evidentiary record. This round modified no existing file.
```

### §0.2 The two binding verdicts

Both confirmations returned `REVISE` and both are treated here as **binding
defect reports**, not as advice:

```text
X-line, reviews/opus_officina_p1_watchdog_freeze_choice_v2_confirmation.md
        REVISE_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2
        R-A  undisclosed constant CLOCK_MONOTONIC
        R-B  the "twelve-site" freezer/witness audit is incomplete, and
             invariant 89 would reject the very freeze path both options need

Y-line, reviews/sol_officina_p1_watchdog_freeze_choice_v2_confirmation.md
        REVISE_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2
        YV2-M1  the count-key rename surface is incomplete: four further
                normative references in the governing correction
        YV2-M2  §7.3 R2 and R9 conflate the row-4 freeze-observation schema
                with the separate §N5 fallback schema
```

**Where X and Y overlap, v2.1 takes the reading that keeps the two schemas
separate.** X R-B asked for invariant 89 to admit the autonomous classifier and
for the row-4 prose to be reconciled. Y YV2-M2 additionally requires that the
§N5 `ABSENT` fallback never be assigned to the row-4 writer, class or
namespace. Both are satisfied together: the autonomous classifier is admitted
as a **freeze-execution** site that writes **no record of any peer class**, and
the fallback stays a distinct object written by the supervisor in a distinct
namespace. Nothing in this correction lets one become evidence for the other.

### §0.3 The exact replacement index — five rows, and nothing else

| # | Finding | v2 locus replaced | v2.1 locus |
|---|---|---|---|
| 1 | X `R-A` | §3.6 `C-4`'s clock expression; §5.2's binding-block disclosure; §9.1 "additional binding-block change"; §10's blast-radius row; §12.0/§12.2 handoff; §12.0 item 9 tests | **§1** |
| 2 | X `R-B` | §7 in whole — §7.2's twelve-site audit, §7.3's `R1`..`R12`, §7.4's headline | **§2**, with the replaced §7 given in full at §2.3–§2.5 |
| 3 | Y `YV2-M1` | §6.3's reopened-sentence table and its "exactly one … sentence" claim; §12.0 item 8 | **§3** |
| 4 | Y `YV2-M2` | §7.3 `R2` | **§2.4 `R2`**, disposed at §4 |
| 5 | Y `YV2-M2` | §7.3 `R9`; §7.3 `R10` retained unchanged | **§2.4 `R9`/`R10`**, disposed at §5 |

**No sixth mechanism is opened.** Two arithmetic consequences that follow
necessarily from row 1 and row 2 are disclosed at §6 as `O-5`..`O-7`, and one
pre-existing chain discrepancy the audit surfaced is disclosed at §6 as `O-8`.
None is a new author cell, and none changes a mechanism.

### §0.4 What v2.1 does not touch

```text
UNCHANGED, in full, from v2:
  §1  the blocker and its four mechanisms
  §2  the rejected route families
  §3  the common freeze classifier — TOTAL, KV-1..KV-6, pgid_or_null
      population P-1..P-3, the §3.5 scope and its total inclusion/exclusion
      table, the sixteen closed tokens, §3.7's continuations, §3.8's three
      terminals, §3.9's invalidity dominance, §3.10's named residual
      — EXCEPT §3.6 C-4's clock expression, replaced at §1.
  §4  W-A in full: the one-shot constant grammar, the G-1..G-4 gate, the
      §4.4 reply/ack/timeout/replay rules, the §4.5 T-1..T-7 ordering window,
      the §4.6 journal and its P-1..P-4 pricing, the §4.7 capability amendment
  §5  W-B in full: E-1..E-4 endpoint-loss semantics, §5.3's single
      continuation, §5.4's establishment table, §5.5's record-first R1..R6,
      §5.6's crash matrix, §5.7, §5.8
  §6  the A-ABS-1..A-ABS-6 amendment itself, §6.4's common token, §6.5's
      identity-cell separation, §6.6 — EXCEPT §6.3's reopened-sentence
      enumeration, replaced at §3.
  §8  L6..L9 and ND-1..ND-4
  §9  §9.2..§9.7 — EXCEPT the two §9.1 rows named at §0.3 row 1 and row 2.
  §10 the recommendation and its criteria
  §11 the token set, including both selection tokens and all six amendments
  §13 N-1..N-6
  §14 negative space

AND SPECIFICALLY PRESERVED:
  the total PCS classifier; W-A's one-shot gate; W-B's endpoint-loss
  semantics; pre-action journaling; the nullable ABSENT values; full charging;
  the publication boundary; the recommendation. process_id remains a
  CONSTRUCTIBLE OPAQUE CLAIM IDENTIFIER, not a PID, and A-ABS leaves it
  mandatory and non-null on every branch. No new author cell is opened. W-B
  MAY REMAIN RECOMMENDED AND DOES — AND NEITHER OPTION IS SELECTED. The
  identity cell is neither selected nor repaired. T = NOT_ACTIVATED; the
  programme claim is OPEN.
```

---

## §1. Repair 1 — bind `CLOCK_MONOTONIC` (closes X `R-A`)

### §1.1 The defect, restated from the bytes

v2 §3.6 `C-4` samples `freeze_ns := _clock(CLOCK_MONOTONIC)`. `_clock` is bound
as `time.clock_gettime_ns` (composite `:414`, `:636`), which **requires** a
clock-id integer argument. `CLOCK_MONOTONIC` is in **no** pinned integer-constant
set: §P1-3.4's list at composite `:419-423` pins `_MSG_CMSG_CLOEXEC`,
`_MSG_CTRUNC` and `_MSG_TRUNC` but no clock id, and the token `CLOCK_` occurs
nowhere in the composite. v2 disclosed exactly one binding-block addition,
`_MSG_EOR`, and asserted at the closure's bounded X-question that no further
constant is required. **That assertion was false, and the X line's answer to its
own bounded question was correctly `NO`.**

### §1.2 The replacement — `_CLOCK_MONOTONIC` pinned as the second addition

```text
REPLACES v2 §5.2's one-name disclosure and v2 §3.6 C-4's clock expression.

B-1  THE ADDITION. §P1-3.4's pinned integer-constant list (composite :419-423)
     is extended by EXACTLY TWO names, appended in this order, so that S-3's
     "exactly the list of §P1-3.4, in that order" remains decidable:

         … _MSG_CMSG_CLOEXEC _MSG_CTRUNC _MSG_TRUNC
           _POSIX_SPAWN_OPEN _POSIX_SPAWN_CLOSE _POSIX_SPAWN_DUP2
           _MSG_EOR _CLOCK_MONOTONIC

B-2  SOURCE. _CLOCK_MONOTONIC is the Attribute `time.CLOCK_MONOTONIC`. `time`
     is already one of the six modules S-1 admits in the PCS root and already
     supplies _clock, so this adds NO import, NO module and NO primitive.
     _MSG_EOR is the Attribute `_socket.MSG_EOR`, likewise already admitted.

B-3  VALUE, PINNED. Under the platform §P1-2.1 fixes — Linux, x86_64, CPython
     3.12.3, the exact reviewed interpreter build — `time.CLOCK_MONOTONIC` is
     the integer 1. §P1-3.5's integer-constant row is extended with the literal
     conjunct:
         _CLOCK_MONOTONIC == 1
     alongside the existing _SIGCHLD == 17, _SIG_DFL == 0, _F_GETFL == 3,
     _O_ACCMODE == 3, _O_RDONLY == 0 conjuncts. _MSG_EOR carries no inline
     literal here and falls under the existing clause "every other constant
     equals the value recorded in the implementation review"; naming its value
     inline is not required and is not claimed.

B-4  VALIDATION, AND STRUCTURAL REFUSAL. The extended §P1-3.5 check runs in the
     runtime preflight of §P1-14.7, before any fork, any lock acquisition and
     any record install. IF THE RUNTIME BINDING DOES NOT EQUAL THE PINNED
     CONSTANT — `type(_CLOCK_MONOTONIC) is not int`, or the value is not 1 —
     THE RESULT IS `PRIMITIVE_NOT_GENUINE`: a fail-closed refusal with no fork,
     no lock acquisition and no record installed (composite :445-446). There is
     no degraded mode, no substitute clock id, and no continuation on a
     mismatch.

B-5  NO IMPLICIT DEFAULT CLOCK. A zero-argument `_clock()` call is FORBIDDEN
     everywhere in both production roots. There is no path on which a clock
     sample is taken from an unnamed or implementation-default clock. This is
     enforced statically at B-7 and is not left to prose.

B-6  THE EXACT USE. v2 §3.6 C-4 is replaced in its clock expression only:

       WITHDRAWN, v2 §3.6 C-4, verbatim:
         "freeze_ns := _clock(CLOCK_MONOTONIC) sampled ON THAT PASS, never the
          signal-send time"

       REPLACEMENT:
         "freeze_ns := _clock(_CLOCK_MONOTONIC), sampled ON THE PASS THAT
          PROVED THE GROUP QUIESCENT, never the signal-send time and never a
          sample taken on any other pass"

     The bound name carries the leading underscore because §P1-3.4 binds every
     primitive and constant under an underscored local name and §P1-3.6 requires
     every later use to go through that local name. THIS IS A SPELLING
     CORRECTION TO THE NAME THE X LINE REPORTED, NOT A DIFFERENT CONSTANT, AND
     IT IS FLAGGED HERE RATHER THAN MADE SILENTLY. The bounded X question at the
     closure asks the X line to confirm or reject it.

B-7  VERIFIER RULE, NEW, IN §P1-14.6 (the next free number after S-24b):

       S-25  every _clock call has exactly one positional argument and no
             keyword argument, and that argument is the plain Name
             _CLOCK_MONOTONIC. A zero-argument _clock() call, a call whose
             argument is any other Name, any literal, any Attribute or any
             expression, and any binding of a second clock id each fail.
             ⇒ "S-25: unpinned or implicit clock"

     This rule is UNIFORM over both roots, so it also pins the composite's
     THREE PRE-EXISTING monotonic samples — reported_monotonic_ns (:636),
     §P1-10.5's termination-schedule t0 (:1673) and §P1-11.5's M1 (:1795) —
     which the composite describes as monotonic samples without ever naming the
     clock id. The X line recorded this as a PRE-EXISTING composite
     under-specification that the PCS-side freeze makes concrete; S-25 repairs
     it once, for every site, rather than only for freeze_ns.

B-8  WHOSE BLAST RADIUS. BOTH. §3's classifier is shared verbatim by W-A and
     W-B, so _CLOCK_MONOTONIC falls on both options identically and separates
     nothing. See §6 O-7 for the corrected accounting of _MSG_EOR, which v2
     charged to W-B alone and which in fact also falls on both.
```

### §1.3 Tests added by this repair

```text
Added to §P1-15, as behavioural rows after the highest existing row 91:

 92  a preflight fixture in which time.CLOCK_MONOTONIC does not equal 1
     refuses with PRIMITIVE_NOT_GENUINE before any fork, any lock acquisition
     and any record install; no freeze is attempted and no journal entry exists
 93  a build containing a zero-argument _clock() call, or a _clock call whose
     argument is not the plain Name _CLOCK_MONOTONIC, fails S-25 statically
 94  the classifier's freeze_ns for a GROUP_FROZEN_PROVED group equals a
     _clock(_CLOCK_MONOTONIC) sample taken on the proving pass; a fixture that
     samples on the signal-send pass, or on a later pass, fails
 95  a build binding a second clock id anywhere in either production root fails
     S-3 (the binding block is not exactly §P1-3.4's list, in order) and S-25
```

### §1.4 Replacement rows in v2's own tables

```text
REPLACES v2 §9.1 row "additional binding-block change":
  | additional binding-block change | `_MSG_EOR` and `_CLOCK_MONOTONIC` added
    to the pinned constants (§1, and §6 O-7) | identical — the same two names |

REPLACES v2 §10 blast-radius row:
  | blast radius | §3 + §6 + §7 + a topology change + a grammar + a gate +
    two pinned constants | §3 + §6 + §7 + two pinned constants |

REPLACES v2 §12.0 (common handoff), by inserting after item 1:
  1b. §P1-3.4: append `_MSG_EOR` and `_CLOCK_MONOTONIC`, in that order, to the
      pinned integer-constant list. §P1-3.5: add the conjunct
      `_CLOCK_MONOTONIC == 1` to the integer-constant row. §P1-14.6: add S-25.
      This item is COMMON to both selections.

REPLACES v2 §12.2 item 12 ("§P1-3.4: add `_MSG_EOR`…"), which is DELETED from
  the W-B-only list because item 1b above now carries both names for both
  selections.

REPLACES v2 §12.0 item 9, by extending it: add test rows 92..95 of §1.3, the
  §3 rows v2 already required, and the §3.3 rows of this document.
```

---

## §2. Repair 2 — the complete freezer / witness and execution-site audit (closes X `R-B`, and carries Y `YV2-M2`)

### §2.1 The withdrawn claim

```text
WITHDRAWN, v2 §7.2, §7.3, §7.4, §9.1, §10 and §12.0 item 6, verbatim:

  "Every sentence, invariant and table row in composite v1.2 that assigns the
   watchdog the freezer or the witness-of-record role."   [as a claim of
   completeness over the twelve sites listed]
  "BOTH make the SAME TWELVE NORMATIVE P1 PROSE CHANGES."
  "the identical twelve sites"
  "| **normative P1 prose changes** | **twelve** (§7) | **twelve** (§7) |"
  "W-B makes zero topology and opcode changes and twelve normative prose
   changes; W-A makes the same twelve plus …"
  "**§7's twelve sites**, replaced with the `R1`..`R12` texts"

WHY IT IS FALSE. The X line's independent exhaustive grep found at least two
normative sites in neither list, and a third partly stale. A re-audit of the
WHOLE composite performed for this correction finds TEN omitted sites, not
two or three. The count is therefore not twelve. THE WORD "TWELVE" IS
WITHDRAWN AND IS NOT RESTATED ANYWHERE IN v2.1 IN PARAPHRASE.

AND, MATERIALLY MORE THAN ENUMERATION. Invariant 89 (composite :2758) rejects
"a supervisor-executed freeze that did not go through SIGNAL_GROUP", and the
§P1-13.7 row at :2368 assigns "every group stop the freeze routes need" to the
SIGNAL_GROUP handler alone. The §3 classifier calls _killpg DIRECTLY, in the
PCS root, not through the SIGNAL_GROUP opcode. A v1.3 handoff following v2
literally would therefore leave a composite whose invariant rejects the exact
freeze path BOTH options depend on. v2's own new verifier rule already admitted
two _killpg call sites (v2 §12.0 item 5) without reconciling invariant 89 to
them. That is the defect, and §2.4 R19 and R21 close it.
```

### §2.2 The corrected count

```text
FINAL EXACT NORMATIVE-SITE COUNT IN THE GOVERNING COMPOSITE: TWENTY-TWO.

  carried from v2's audit, unchanged as sites          12
  found by this correction's re-audit, newly added     10
                                                     ----
  total normative composite sites both options amend   22

Of the ten new sites, THREE are the ones the X line named (R-B: the §P1-13.2
row-4 rationale paragraph at :2278-2287; the §P1-13.8 reader sentence at
:2389-2391; invariant 89 at :2758) and SEVEN were found by re-auditing the
whole composite for this correction and are in NO review:
  §P1-9.2 property 11's rationale clause          :1459-1463
  §P1-11.4 supervisor-continuation step 2         :1781-1782
  §P1-13.2 row 4's discriminator block            :2254-2257
  §P1-13.2 row 4's "P1 invariant" block           :2270-2275
  §P1-13.6 SW-2                                   :2337-2341
  §P1-13.7's group-stop row                       :2368
  invariant 91                                    :2760

THE COUNT STILL FALLS IDENTICALLY ON W-A AND W-B. All twenty-two are amended
under either selection, with wording differences only at sites 1, 3, 7, 8, 11
and 13. R-B therefore does not move the recommendation, exactly as both the X
line and F1 concluded for the sites they did find.
```

### §2.3 The replaced §7.2 — the complete audit, twenty-two sites

Every sentence, invariant and table row in composite v1.2 that assigns the
watchdog the **freezer** or the **witness-of-record** role, **or that asserts a
property of the freeze-execution model which the §3 classifier makes false**.
Sites 1–12 are v2's, unchanged in identification. Sites 13–22 are new; the
"src" column records who found each.

| # | Site | Line(s) | src | The sentence that becomes false |
|---|---|---|---|---|
| 1 | C1 intro statement | `202` | X v1 | "A dedicated watchdog process **witnesses and freezes**." |
| 2 | §P1-9.2 property 7 | `1447-1451` | X v1 | it "**physically emits freeze observations** under its own witness identifier, in the record class of §P1-13.2 row 4" |
| 3 | §P1-9.2 property 12 | `1464-1465` | X v1 | "on observing update-pipe EOF it **freezes the groups it knows, writes their observations**, and exits" |
| 4 | §P1-9.2 Termination ¶ | `1469-1470` | X v1 | "the watchdog observes EOF, **writes its final observations** and exits" |
| 5 | §P1-9.4 `S-4` | `1490` | X v1 | "the watchdog observes EOF, **writes its final observations**, `os._exit(0)`" |
| 6 | §P1-11.4 continuation step 3 | `1783-1784` | X v1 | "the watchdog **writes its observations for the groups it knows** and exits" |
| 7 | §P1-11.7 crash matrix row | `1888` | X v1 | "the watchdog sees update-pipe EOF **and freezes, observes and exits**" |
| 8 | §P1-13.1 process/layer table, watchdog row | `2006` | v2 | watchdog runs "**generic-harness peer witness code**"; "it **physically emits a peer-owned record**" |
| 9 | §P1-13.2 row 4, executing process | `2249-2253` | v2 | "**EITHER the watchdog role process, normally**, OR the supervisor role process, on the signed dead-watchdog route" |
| 10 | §P1-13.7 single-writer table, freeze row | `2367` | v2 | the freeze-witness function is "**called from the watchdog role entry** and from the supervisor's dead-watchdog route" |
| 11 | Invariant 61 | `2730` | X v1 | "supervisor death produces update-pipe EOF **and the freeze, observe and exit route**" |
| 12 | Invariant 63 | `2732` | v2 | "every one of the **thirteen** watchdog properties of §P1-9.2 holds in a live generation" — properties 7, 11 and 12 are three of the thirteen |
| 13 | §P1-9.2 property 11, rationale clause | `1459-1463` | **v2.1** | "treating it as supervisor death **would produce a false freeze**" — under W-B the watchdog can produce no freeze at all, so the stated reason for the prohibition is false even though the prohibition itself stands |
| 14 | §P1-11.4 supervisor-continuation step 2 | `1781-1782` | **v2.1** | "freeze is unavailable, because **the quiescence proof needs `SIGNAL_GROUP`**" — the conclusion survives, the reason does not: after §3 there are two freeze-execution sites, and it is their common dependence on a live PCS, not `SIGNAL_GROUP` alone, that makes freeze unavailable on PCS loss |
| 15 | §P1-13.2 row 4, discriminator block | `2254-2257` | **v2.1** | "This is the **`R-L5` case, and it is the only one in this document**" — row 4 ceases to have two executing processes |
| 16 | §P1-13.2 row 4, "P1 invariant" block | `2270-2275` | **v2.1** | "P1 provides **the watchdog role process, its two sealed descriptors**, and — **on the supervisor-executed branch** — the `SIGNAL_GROUP` mediation" — the watchdog contributes nothing to this record, and "the supervisor-executed branch" implies a second branch that no longer exists |
| 17 | §P1-13.2 row-4 rationale ¶ | `2278-2287` | **X R-B** | "it has **two possible executing processes**"; "C1 selected a **dedicated freezer watchdog as the normal witness**"; "the freeze it performs is **PCS-mediated exactly like every other group stop**" |
| 18 | §P1-13.6 `SW-2` | `2337-2341` | **v2.1** | "**Exactly one artifact** in this document is in that class: row 4, discriminated by `killer`" — no artifact remains in that class |
| 19 | §P1-13.7, group-stop row | `2368` | **v2.1** | "**every group stop the freeze routes need** \| … the `SIGNAL_GROUP` handler \| P1 \| **mediation only**" — the §3 classifier's group stops are group stops a freeze needs, are executed not mediated, and do not go through `SIGNAL_GROUP` |
| 20 | §P1-13.8 reader sentence | `2389-2391` | **X R-B** | "the freeze-observation record, which **a P1-created role physically emits** and which the supervisor branch **reaches only through `SIGNAL_GROUP`**" — literally survivable, but written to describe the watchdog, and silent on the classifier |
| 21 | **Invariant 89** | `2758` | **X R-B** | "a freeze observation written by a process that is **neither the watchdog role nor the supervisor role** is rejected" — still names the watchdog a permitted writer; **and** "a supervisor-executed freeze that **did not go through `SIGNAL_GROUP`** is rejected" — which would reject the §3 classifier both options depend on |
| 22 | Invariant 91 | `2760` | **v2.1** | "**exactly one artifact carries a multi-process discriminator**, and it is row 4's `killer`" — the `SW-2` companion; false for the same reason |

**Checked across the whole composite and confirmed NOT to need amendment.**
This list is stated so the audit is closed in both directions:

```text
Invariant 57  (:2726)  both signal opcodes refused for a watchdog handle; no
                       signal reaches a watchdog on any path — TRUE and
                       STRENGTHENED: KV-6 additionally forbids any killpg whose
                       target group is a watchdog leader group or the PCS's own.
Invariant 60  (:2729)  the watchdog never uses getppid(); a PCS-death fixture
                       with the supervisor alive produces no freeze — TRUE
                       under both, and strengthened.
Invariant 62  (:2731)  watchdog termination is EOF-driven; WATCHDOG_UNREAPED
                       routes to §P1-11.6 with no signal — TRUE, unchanged.
Invariant 65  (:2734)  PCS death: … freeze unavailable … — TRUE under both.
Invariant 84  (:2753)  the P1 layer opens the process-claim and
                       freeze-observation records on no path — TRUE; the §3
                       classifier opens neither and writes neither.
Invariant 85  (:2754)  nothing in §P1-13.8's out-of-scope list is read, written
                       or produced by any P1 path — TRUE.
Invariant 86  (:2755)  wrong logical writer — TRUE; no P1 root gains an install
                       site for any of the four artifacts (§4 A-4).
Invariant 88  (:2757)  duplicate claim write — TRUE; one install site each.
Invariant 90  (:2759)  process-name based ownership inference; "the fixture
                       presents a peer-owned write performed inside a
                       P1-created role — the row 3 and row 4 cases" — TRUE:
                       row 4's remaining write executes in the SUPERVISOR role
                       process, which is equally a P1-created role.
R-L2          (:2015-2018)  a peer-owned schema may be read or physically
                       emitted by a P1-created role process; every such case is
                       a §P1-13.2 row whose executing process differs from its
                       logical writer — TRUE: rows 3 and 4 both still differ.
R-L4          (:2022-2027)  one-way call direction — TRUE and untouched.
R-L5          (:2028-2032)  the general rule that a multi-executing-process
                       logical writer MUST carry a discriminator — the RULE is
                       UNCHANGED. What changes is that after the amendment NO
                       ROW INSTANTIATES IT; that is what sites 15, 18 and 22
                       record. The rule text itself is not amended.
§P1-10.5      (:1655-1656)  "killpg is used only against a kernel-verified
                       group" — TRUE and STRENGTHENED: KV-1..KV-6 is
                       re-evaluated immediately before EVERY _killpg and is
                       never cached across a signal.
§P1-13.3      (:2312)  SIGNAL_GROUP mediation serves "the peer layer's freeze
                       routes, including the supervisor-executed branch of
                       §P1-13.2 row 4" — TRUE: that branch is retained intact
                       and still reaches every group stop through SIGNAL_GROUP.
§P1-13.2 row 4 path, schema value, key set, logical writer, readers,
              durability/ordering, deletion authority (:2232-2248, :2258-2269)
                       — UNCHANGED. The peer schema t-freeze-observation.v1 is
                       NOT amended by either option, and `killer` is retained
                       as a mandatory schema key.
§P1-13.2 "What P1 replaced in that same signed route" ¶ (:2289-2293)
                       — TRUE: the dead-watchdog route's freeze-and-observe
                       half is retained exactly, including the SUPERVISOR
                       discriminator value.
§P1-13.2 adjacent-artifacts ¶ (:2295-2302)  "The peer layer also owns a freeze
                       fallback record and a replacement-freeze record, written
                       by the peer layer executing in the supervisor process,
                       in namespaces the watchdog has no path to and never
                       writes … so that no implementer collapses them."
                       — TRUE, UNCHANGED, AND LOAD-BEARING: this is the signed
                       authority for the R2/R9 separation Y YV2-M2 requires.
§P1-13.2 row 3 readers, and :2116-2119, :2176-2177, :2213 — the freeze-evidence
                       acceptance predicate comparing a witness's pgid and start
                       identity against the supervisor identity record — TRUE,
                       UNCHANGED: those readers consume row 4's witness keys,
                       which A-ABS does not touch. A-ABS amends only the
                       SEPARATE §N5 fallback object.
C1 cell text  (:201-206)  the SELECTION TOKEN
                       I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER is not
                       revoked, re-run or re-opened. Site 1 amends the
                       composite's operative sentence; the reassignment is
                       carried by the amendment token
                       P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1, exactly as v2
                       §11 already provides.
P1 cell text  (:221-227)  the supervisor "calls fork, Popen, waitpid, kill and
                       killpg on no path" — TRUE and STRENGTHENED: the §3
                       classifier executes in the PCS root only.
S-12          (:2601)  RETAINED UNCHANGED under both options.
```

### §2.4 The replaced §7.3 — exact replacements `R1`..`R22`

**Identical for W-A and W-B except where a variant is marked.** Every one
**replaces** the named sentence, row or block; none is added beside it.

```text
R1  line 202:
    "A dedicated watchdog process witnesses the supervisor control channel and
     signals its loss. The PCS executes every freeze."
    W-A VARIANT: "... signals its loss, and requests the freeze the PCS
     executes."

R2  §P1-9.2 property 7 — REPLACED IN v2.1 PER Y YV2-M2. The v2 text is
    WITHDRAWN verbatim:
      "it emits NO freeze observation and writes no record of any class. The
       freeze-witness record class of §P1-13.2 row 4 is written only by the
       supervisor, on the signed dead-watchdog route AND ON THE ABSENT FALLBACK
       ROUTE OF §N5 as amended."
    THE REPLACEMENT:
      "7. it emits NO freeze observation and writes no record of any class. The
          freeze-witness record class of §P1-13.2 row 4 —
          `philosophia.officina.t-freeze-observation.v1`, installed under
          `WATCHDOG/FREEZE/` — is written ONLY by the supervisor role process,
          on the signed dead-watchdog route, and by no other process on any
          path. SEPARATELY, AND IN A DIFFERENT CLASS: the §N5 `ABSENT` route
          writes `philosophia.officina.t-freeze-fallback-observation.v1` under
          `WATCHDOG/FREEZE_FALLBACK/`, written by the supervisor under
          `T_RUNTIME.lock` per §N5.2 as amended by `A-ABS`. That object is NOT a
          record of row 4's class, is NOT written by row 4's writer, and is NOT
          installed in row 4's namespace; it is one of the two adjacent peer
          artifacts the composite already names at :2295-2302 and is outside
          §P1-13.2 entirely;"

R3  §P1-9.2 property 12:
    W-B: "12. on observing update-pipe EOF it writes nothing, freezes nothing,
          and exits, settling nothing;"
    W-A: "12. on observing update-pipe EOF it sends exactly one constant
          t-wd-freeze.v1 record on slot 6, waits at most
          T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS for one reply record, writes
          nothing, and exits, settling nothing;"

R4  §P1-9.2 Termination ¶:
    "The supervisor closes the update pipe write end; the watchdog observes
     EOF, writes nothing, and exits; the PCS reaps it on REAP_ROLE."
    (The WATCHDOG_UNREAPED sentence that follows is unchanged.)

R5  §P1-9.4 S-4:
    "S-4. the watchdog observes EOF, writes nothing, os._exit(0)"

R6  §P1-11.4 continuation step 3:
    "3. close the watchdog update pipe write end; the watchdog writes nothing
        and exits; its adopter reaps it;"

R7  §P1-11.7 crash matrix row 1888 — REPLACE THE ROW, do not add beside it:
    W-B: "| supervisor control endpoint lost while the PCS lives | the PCS runs
     the §3 classifier record-first, appends its terminal, holds every live
     handle in the non-returning reaper state and frees the singleton for no
     one; the watchdog sees update-pipe EOF, writes nothing and exits;
     §P1-11.1 governs the records at the next attempt |"
    W-A: as above, but "the PCS opens the bounded W-A service window of §4.5
     and runs the classifier only on an ACCEPTED request; on window end without
     one, no freeze occurs".
    THEN add the rows of §5.6 (W-B) or §4.5 (W-A).

R8  §P1-13.1 watchdog row:
    "**P1 role-entry layer only.** It emits no peer-owned record and owns no
     peer decision."
    W-A VARIANT adds: "It holds one single-opcode, target-free freeze-request
     socket and emits no record."

R9  §P1-13.2 row 4 executing process — REPLACED IN v2.1 PER Y YV2-M2. The v2
    text is WITHDRAWN verbatim:
      "the supervisor role process, on the signed dead-watchdog route AND ON THE
       §N5 ABSENT-FALLBACK ROUTE. The watchdog executes no write of this class."
    THE REPLACEMENT:
      "executing process    the supervisor role process ONLY, on the signed
                            dead-watchdog route, when the watchdog has been
                            declared dead by ack absence past
                            T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS. The watchdog role
                            process executes no write of this class on any path.
                            The §N5 ABSENT fallback is a DIFFERENT artifact, of
                            a different schema, in a different namespace, and is
                            NOT an executing-process branch of this row."

R10 §P1-13.7 freeze row — SEMANTICALLY UNCHANGED from v2, retained verbatim as
    the Y line requires:
    "| write a freeze observation | `src/philosophia/officina/generic_harness.py`,
     **one** freeze-witness function, called from the supervisor's dead-watchdog
     route only, setting `killer` from its caller | peer | install, no-replace |"

R11 Invariant 61 — REPLACE:
    W-B: "| 61 | loss of the peer control endpoint produces the PCS's
     record-first §3 classifier and its terminal; supervisor death additionally
     produces update-pipe EOF and the watchdog's write-nothing exit route |"
    W-A: "| 61 | loss of the peer control endpoint produces the PCS's bounded
     service window; an ACCEPTED t-wd-freeze.v1 record produces the
     record-first §3 classifier and its terminal; window end without one
     produces no freeze |"

R12 Invariant 63 — the thirteen properties remain thirteen; properties 7, 11 and
    12 are the amended texts R2, R13 and R3. The invariant's WORDING is
    unchanged; its CONTENT changes because three of the thirteen changed.
    (v2 said "two of the thirteen"; site 13 makes it three. This is the only
    consequential change to R12 and it is stated rather than left implicit.)

R13 §P1-9.2 property 11 — REPLACE the rationale clause only; the PROHIBITION is
    unchanged and is not weakened:
    W-B: "11. it must not use `getppid()` to infer supervisor death and must not
          treat a change in `getppid()` as any signal about the supervisor: its
          parent is the PCS, so a change means the PCS died, a distinct
          condition in which the supervisor may still be alive. The watchdog
          executes no freeze on any path, so no misuse of `getppid()` can
          produce a freeze at all; the prohibition stands because the inference
          is false, not because of what it would trigger;"
    W-A: "11. … in which the supervisor may still be alive. A watchdog that made
          that inference would send its one authorized t-wd-freeze.v1 record
          against a generation whose peer control endpoint may still be live,
          which the G-1 gate REFUSES with PEER_ENDPOINT_LIVE and no syscall, so
          no false freeze is reachable; the prohibition stands because the
          inference is false, not because of what it would trigger;"

R14 §P1-11.4 supervisor-continuation step 2 — REPLACE:
    "2. freeze is unavailable, because every freeze-execution site in this
        contract requires a live PCS — the peer layer's supervisor
        dead-watchdog route reaches every group stop through `SIGNAL_GROUP`,
        which is a PCS operation, and the PCS's own §3 freeze classifier
        executes in the PCS root — so no live stream has a valid continuation;"
    IDENTICAL FOR BOTH OPTIONS.

R15 §P1-13.2 row 4 discriminator block — REPLACE:
    "discriminator        the mandatory in-record key `killer`, RETAINED from
                          the peer schema, whose value on every path reachable
                          under this contract is SUPERVISOR, because this row
                          now has EXACTLY ONE executing process. This row is no
                          longer an `R-L5` two-executing-process case. `R-L5`
                          itself is unchanged and is instantiated by no row of
                          this document."

R16 §P1-13.2 row 4 "P1 invariant" block — REPLACE the first sentence; the second
    is unchanged:
    "P1 invariant         P1 provides the watchdog role process and its two
                          sealed descriptors for the supervisor-channel-liveness
                          function ONLY, and provides NO input to this record.
                          On the one executing branch P1 provides the
                          `SIGNAL_GROUP` mediation without which the supervisor
                          could not stop a group at all. P1 decides nothing
                          about the content, the acceptance, or the consumption
                          of this record, and writes no field of it."

R17 §P1-13.2 row-4 rationale ¶ (2278-2287) — REPLACE THE WHOLE PARAGRAPH:
    "**Why one executing process does not break single-writer or C1.** There is
     exactly **one** logical writer, the peer layer's freeze-witness function,
     and under the amended C1 exactly **one** executing process: the supervisor
     role process, on the signed dead-watchdog route. The mandatory `killer` key
     is retained from the peer schema and carries `SUPERVISOR` on every
     reachable path. C1 is **amended, not preserved**: the watchdog is no longer
     the freezer and no longer the witness of record, and that reassignment is
     carried by `P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1`. The supervisor's
     branch requires `SIGNAL_GROUP`, because the supervisor holds no process
     authority of its own, so the freeze it performs is PCS-mediated exactly
     like every other group stop. **The PCS's own §3 freeze classifier is a
     separate, signed freeze-EXECUTION site**: it runs in the PCS root, is not
     `SIGNAL_GROUP`-mediated, targets only the §3.5 scope computed from the
     PCS's own handle table under `KV`, writes **no record of this or any peer
     class**, and its journal terminal is a P1-owned fact that is never freeze
     evidence (§P1-12.2 `L8`, `ND-1`..`ND-3`)."
    W-A VARIANT: "… is a separate, signed freeze-execution site, entered only on
     an ACCEPTED t-wd-freeze.v1 record inside the §4.5 service window: it runs
     in the PCS root, is not SIGNAL_GROUP-mediated, …" (remainder identical).

R18 §P1-13.6 SW-2 — REPLACE:
    "SW-2. Where one logical writer has more than one possible executing
           process, the record carries a mandatory discriminator key naming
           which process executed it, and §P1-13.2's row for that artifact names
           the key. **No artifact in this document is in that class.** Row 4
           retains its peer-schema `killer` key, but it has exactly one
           executing process — the supervisor role process — so that key is a
           carried schema field and not a live discriminator."

R19 §P1-13.7 group-stop row (2368) — REPLACE THE ROW WITH TWO ROWS:
    "| every group stop the PEER freeze routes need |
       `scripts/officina_process_control_bootstrap.py`, the `SIGNAL_GROUP`
       handler | P1 | mediation only |
     | every group stop the PCS's own freeze classifier performs |
       `scripts/officina_process_control_bootstrap.py`, the freeze classifier of
       new §P1-10.7 | P1 | EXECUTION; installs no record of any class |"
    This row pair is the §P1-13.7 companion to invariant 89's `SIGNAL_GROUP`
    clause and MUST be replaced in the same step as R21.

R20 §P1-13.8 reader sentence (2389-2391) — REPLACE the final clause:
    "… or the freeze-observation record, which the **supervisor role process** —
     a P1-created role — physically emits on the signed dead-watchdog route, and
     which that branch reaches only through `SIGNAL_GROUP`. The PCS's own freeze
     classifier emits no record of this or of any peer class, and the §N5
     freeze-fallback record remains outside this table entirely, as §P1-13.2's
     adjacent-artifacts paragraph already states."

R21 Invariant 89 (2758) — REPLACE THE ROW. This is the load-bearing replacement:
    "| 89 | **wrong freeze writer, and the two signed freeze-execution sites**:
     a freeze observation whose `killer` value does not name the process that
     executed the write is rejected; a freeze observation written by a process
     that is **not the supervisor role process** is rejected — the watchdog role
     writes no record of this class on any path, and no other process may write
     one; and a group stop performed for a freeze is rejected unless it is one
     of **exactly two** signed execution sites:
       (a) the **supervisor's dead-watchdog route**, which reaches every group
           stop through the `SIGNAL_GROUP` opcode and may not bypass it; and
       (b) the **PCS's own freeze classifier** of §P1-10.7, executing in the PCS
           root, under `KV-1`..`KV-6` re-evaluated before every `_killpg`,
           against the scope computed from the PCS's own handle table, and
           reachable only from its own trigger site
           [W-B: the `E-1a` endpoint-loss site; W-A: an `ACCEPTED`
            t-wd-freeze.v1 record inside the §4.5 service window].
     Site (b) is **request-driven by no peer opcode** and is **not
     `SIGNAL_GROUP`-mediated**; site (a) is mediated and is not autonomous. Both
     sites' `_killpg` executes in the PCS root and nowhere else, so the PCS
     remains the **sole caller** of `killpg` and `S-12` is retained unchanged.
     Any other freeze-observation writer, and any other executor of a freeze
     group stop, is rejected. **Site (b) installs no record of any peer class:**
     its journal terminal, its per-group tokens and its `freeze_ns` are
     P1-owned process-control journal facts, are never a
     `t-freeze-observation.v1`, are never a field of a
     `t-freeze-fallback-observation.v1`, and are never an input to any peer
     validity predicate (`L8`, `ND-1`..`ND-3`). A build in which any of them
     reaches a peer artifact, an acceptance predicate, a qualification, a
     comparison, a Q or C fact or any published record fails this test. |"

R22 Invariant 91 (2760) — REPLACE:
    "| 91 | `SW-1` through `SW-5` hold over the four rows: exactly one schema
     owner and exactly one logical writer each; **no artifact carries a live
     multi-process discriminator, because row 4 now has exactly one executing
     process**, and its retained `killer` key is a carried peer-schema field;
     and no artifact has two install sites |"
```

### §2.5 The replaced §7.4 — what this does and does not shift

Both options demote the identical executor/witness role and therefore amend the
identical **twenty-two** sites, with wording differences only at sites 1, 3, 7,
8, 11 and 13. **X `F1` and X `R-B` fall equally on both.** The honest headline
is now: *W-B makes zero topology and opcode changes and twenty-two normative
prose changes; W-A makes the same twenty-two plus a topology change, a grammar,
a dispatch path and a gate.* The site count grew by ten and separated nothing.

**What did change qualitatively, and it is not enumeration.** `R19` and `R21`
admit a **second signed freeze-execution site** into the composite. Before this
correction the composite enforced a single model in which every freeze group
stop is `SIGNAL_GROUP`-mediated. That model cannot survive a PCS-side
classifier, and v2 introduced the classifier without reconciling the invariant
that forbade it. A reviewer weighing the options should weigh this: **both
options require the composite to acknowledge two freeze-execution sites**, and
neither option avoids it, because §3 is common. It does not separate W-A from
W-B, and it does not create a new author cell — it is the exact consequence of
`P1_PCS_FREEZE_CLASSIFIER_V1`, which v2 §11 already puts on both options.

### §2.6 Tests added by this repair

```text
Added to §P1-15, after the rows of §1.3:

 96  the amended invariant 89: a fixture in which the watchdog role writes a
     t-freeze-observation.v1 is REJECTED; a fixture in which the supervisor's
     dead-watchdog route stops a group without SIGNAL_GROUP is REJECTED; a
     fixture in which the §P1-10.7 classifier stops a group in the PCS root
     under KV is ACCEPTED as site (b) and installs no record
 97  a fixture in which any process other than the PCS root calls _killpg fails;
     S-12 is asserted unchanged in the same run
 98  a fixture in which a classifier journal terminal, a per-group token or a
     freeze_ns value reaches a peer artifact, an acceptance predicate, a
     qualification, a comparison, a Q or C fact, or any published record fails
 99  the amended SW-2 and invariant 91: a fixture asserting that some artifact
     carries a live multi-process discriminator fails; row 4 has exactly one
     executing process and its `killer` key is present and equal to SUPERVISOR
100  a fixture in which the §N5 fallback object is installed under
     WATCHDOG/FREEZE/, or validated by row 4's acceptance predicate, or written
     by row 4's writer function, fails — the two classes never converge
```

---

## §3. Repair 3 — complete the count-key rename surface (closes Y `YV2-M1`)

### §3.1 The withdrawn claim

```text
WITHDRAWN, v2 §6.3, verbatim:
  "**Exactly one contract file's schema is reopened, in exactly three keys, on
   exactly one branch.** No routing, no id preimage, no consumption order and
   no §Z4.6 conjunct changes."
   [insofar as it asserted that ONE SENTENCE is reopened]
and the v2 §6.3 row:
  | §N5.4's "unknown_reason = FREEZE_INSTANT_UNKNOWN with
    current_unresolved_member_count = 0 and supervisor_quiescence = PROVED is
    legal and expected" | :905-909 | **unchanged** … |

WHY IT IS FALSE. A-ABS-2 renames the schema key globally. Four FURTHER
normative references in the governing
OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md still
name the superseded key. Applying v2's handoff literally would leave a signed
schema and four signed readers, definitions and examples naming DIFFERENT keys.
The §N5.4 row above is semantically valid on its non-ABSENT branch — Y confirms
this — but it CANNOT remain byte-unchanged once the key is renamed.
```

### §3.2 The complete rename surface, enumerated and replaced

**All five normative references, in the one governing file
`OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md`
(`2cd8b7b5…`).** Each is a **replacement**, not an addition.

| # | Locus | Kind | Present text | Replacement |
|---|---|---|---|---|
| K1 | §N5.2 key list, `:866` | schema | `current_unresolved_member_count (int ≥ 0),` | `current_unresolved_member_count_or_null (int ≥ 0, or null; null IF AND ONLY IF rejection_conjunct == 0),` |
| K2 | §N5.4 field-definition block, `:900` | generic definition | `current_unresolved_member_count — what the supervisor observes NOW` | `current_unresolved_member_count_or_null — what the supervisor observes NOW; null IF AND ONLY IF rejection_conjunct == 0, because with pgid_or_null null the group cannot be named and no integer is computable` |
| K3 | §N5.4 legal example, `:905-909` | example | `unknown_reason = FREEZE_INSTANT_UNKNOWN` with `current_unresolved_member_count = 0` and `supervisor_quiescence = PROVED` is **legal and expected** | `unknown_reason = FREEZE_INSTANT_UNKNOWN` with `current_unresolved_member_count_or_null = 0` and `supervisor_quiescence = PROVED` is **legal and expected**. **The integer `0` is retained**: this example is on a `rejection_conjunct != 0` branch, where the field is a mandatory non-null integer, and `0` there means "zero members are unresolved now", which is exactly the fact §N5.4 separates from the historical instant |
| K4 | §N10.2 fact-location table, `:1370` | fact location | `FREEZE_FALLBACK/*` (`current_unresolved_member_count`, `supervisor_quiescence`) | `FREEZE_FALLBACK/*` (`current_unresolved_member_count_or_null`, `supervisor_quiescence`); on the `rejection_conjunct == 0` branch the pair is exactly (`null`, `UNKNOWN`), and no current-member fact is recorded there |
| K5 | §N11 crash-cut example, `:1416` | example | fallback with `unknown_reason = FREEZE_INSTANT_UNKNOWN`, `current_unresolved_member_count = 0`, `supervisor_quiescence = PROVED` ⇒ `UNKNOWN` route | fallback with `unknown_reason = FREEZE_INSTANT_UNKNOWN`, `current_unresolved_member_count_or_null = 0`, `supervisor_quiescence = PROVED` ⇒ `UNKNOWN` route; no timestamp synthesized. **The integer `0` is retained**, for K3's reason |

**The generic definitions state the biconditional; the two non-`ABSENT` examples
retain the integer `0`.** That is exactly Y's instruction and it is exactly what
K2/K4 versus K3/K5 do.

### §3.3 What the rename does NOT touch — stated so the surface is closed in both directions

```text
NOT RENAMED, AND EXPLICITLY DISTINGUISHED:
  `unresolved_member_count` — the key of the WATCHDOG-WRITTEN
  t-freeze-observation.v1 (composite :2243), bound by §Z4.6 conjunct 9 as
  narrowed at §N5.4:890-894. It is a DIFFERENT key on a DIFFERENT schema, it
  carries no _or_null suffix, and A-ABS does not amend it. A rename that
  touched it would be a defect.

NO ADDITIONAL SURFACE FOR THE OTHER TWO RENAMED KEYS. `pgid` and
  `start_identity` occur in the fallback schema at exactly ONE locus, §N5.2
  :860. Verified by direct grep over the governing file: every other `pgid` /
  `start_identity` occurrence belongs to a DIFFERENT schema — §N3's spawning
  records (:564-567, :588, :634-642, :655-657, :667) and §N5.6's
  t-replacement-freeze.v1 (:957, :976) — none of which A-ABS amends. So for
  those two keys v2 §6.3's one-sentence claim was CORRECT and stands.

NO READER OR PREDICATE CONSUMES THE FALLBACK COUNT. Verified: the four extra
  references are one field definition, two examples and one fact-location row.
  No signed acceptance predicate, no validity conjunct and no settlement rule
  reads `current_unresolved_member_count`. §Z4.6 conjunct 9 binds only the
  watchdog-written record, per §N5.4's own narrowing. So the repair is a
  rename surface and NOT a predicate change, exactly as Y determined.

UNCHANGED, RE-AFFIRMED: §N5.1's id preimage (:833-840) contains none of the
  three amended keys, so fallback_witness_id values are stable; §N5.3's routing
  (:876-886) is verbatim untouched; §N5.5's production / duplicate / conflict /
  consumption order (:912-937) is untouched; §Z4.6 conjunct 10 is untouched.
```

### §3.4 The corrected reopened-sentence count

```text
REPLACES v2 §6.3's closing claim:

  "Exactly ONE contract file's schema is reopened, in exactly THREE keys, on
   exactly ONE branch, across exactly FIVE normative sentences:
       §N5.2  :859-866    the schema key list          (K1)
       §N5.4  :899-902    the field-definition block   (K2)
       §N5.4  :905-909    the legal example            (K3)
       §N10.2 :1370       the fact-location row        (K4)
       §N11   :1416       the crash-cut example        (K5)
   No routing, no id preimage, no consumption order and no §Z4.6 conjunct
   changes."

v2 said one sentence. The correct number is FIVE. The file count, the key count
and the branch count are UNCHANGED at one, three and one.
```

### §3.5 Handoff and tests

```text
REPLACES v2 §12.0 item 8:
  8. §N5 of …V2_1_2_CORRECTION.md: apply A-ABS-1..A-ABS-6, AND apply the five
     replacements K1..K5 of §3.2 — §N5.2 :866, §N5.4 :900, §N5.4 :906,
     §N10.2 :1370, §N11 :1416. After the edit, no occurrence of the bare token
     `current_unresolved_member_count` remains in that file, and every
     occurrence of `current_unresolved_member_count_or_null` is either the
     schema key, the generic definition with its biconditional, the
     fact-location row, or one of the two `= 0` non-ABSENT examples.

Added to §P1-15, after the rows of §2.6:
101  a fallback record with rejection_conjunct == 0 and a NON-NULL
     current_unresolved_member_count_or_null is INVALID; a record with
     rejection_conjunct != 0 and a NULL one is INVALID. Both directions of the
     biconditional are asserted, as for pgid_or_null and
     start_identity_or_null
102  a static check that no signed document names the superseded key
     `current_unresolved_member_count`, and that the distinct watchdog-record
     key `unresolved_member_count` is unchanged and still bound by §Z4.6
     conjunct 9 as narrowed at §N5.4
```

---

## §4. Repair 4 — separate the two observation schemas in `R2` (closes Y `YV2-M2`, first half)

### §4.1 The defect and the replacement

v2 `R2` said the row-4 freeze-witness class is written by the supervisor "on the
signed dead-watchdog route **and on the `ABSENT` fallback route of §N5 as
amended**". That is false against the governing bytes and against v2's own §6:

```text
A-1  §N5.2 (:856-857) defines the ABSENT object as a DIFFERENT SCHEMA:
     philosophia.officina.t-freeze-fallback-observation.v1
A-2  §N5.1 (:842) installs it in a DIFFERENT NAMESPACE:
     runtime_control/T_SUPERVISOR/WATCHDOG/FREEZE_FALLBACK/<fallback_witness_id>.json
     whereas row 4's path is WATCHDOG/FREEZE/<witness_id>.json (composite :2236)
A-3  The composite ITSELF already forbids collapsing them, at :2295-2302:
     the fallback is one of "two adjacent peer artifacts … named so their
     absence from this table is not read as an omission … so that no implementer
     collapses them."
A-4  §N5.3 (:882-886) and §P1-13.8 keep the fallback OUTSIDE §P1-13.2 entirely.
     No P1 root gains an install site for it, and A-ABS-6 preserves that.
```

**The replacement is `R2` as given at §2.4**, which states the row-4 class and
its single writer, and then states the fallback **separately**, by its own
schema name and its own namespace, explicitly as **not** a record of row 4's
class and **not** written by row 4's writer.

### §4.2 The rule this correction adopts, stated once and applied everywhere

```text
SEP-1  THE §N5 FALLBACK OBJECT IS NEVER ASSIGNED TO ROW 4's WRITER, ROW 4's
       CLASS OR ROW 4's NAMESPACE, in any sentence of this packet, in any
       replacement text, in any handoff item, or in any test row.
SEP-2  The two objects are related only by ROUTING: an absent row-4 witness is
       what causes the supervisor to write the fallback. Routing is not
       authorship. v2 §6 already said this; `R2` contradicted it, and `R2` is
       replaced rather than reconciled.
SEP-3  Neither option makes a fabricated freeze expressible in either object.
       Row 4's class is written only by the supervisor's dead-watchdog route.
       The fallback synthesizes nothing (`A-ABS-4`). The PCS journal is neither
       (`L8`). Y's determination that "this does not permit fabricated evidence"
       is preserved, and the repair makes the TEXT single-valued as well.
```

---

## §5. Repair 5 — remove the fallback route from `R9`; `R10` unchanged (closes Y `YV2-M2`, second half)

```text
D-1  v2 R9's clause "and on the §N5 ABSENT-fallback route" is REMOVED from the
     row-4 EXECUTING-PROCESS clause. The replacement at §2.4 R9 names exactly
     one executing process — the supervisor role process on the signed
     dead-watchdog route — and states that the fallback is not an
     executing-process branch of this row.

D-2  R10 IS SEMANTICALLY UNCHANGED and is retained verbatim, as the Y line
     requires: the row-4 freeze-witness function is "called from the
     supervisor's dead-watchdog route only, setting `killer` from its caller".
     v2's R10 was already correct; it is R2 and R9 that were inconsistent with
     it, and they are now consistent with it rather than the reverse.

D-3  CONSEQUENCE FOR SITES 15, 17, 18 AND 22. Because row 4 now has exactly ONE
     executing process, the composite's R-L5 / discriminator / SW-2 /
     invariant-91 cluster becomes false. Those four sites are added at §2.3 and
     replaced at §2.4 R15, R17, R18 and R22. THE PEER SCHEMA IS NOT AMENDED:
     `killer` remains a mandatory key of t-freeze-observation.v1, retained, with
     value SUPERVISOR on every reachable path. Neither option reopens the row-4
     schema.

D-4  DISPOSITIONS UPDATED. X F1, X F3 and Y-C3 are re-dispositioned at the
     closure §4 accordingly: F1 was reported CLOSED in the v2 closure and is
     NOT closed by v2; it is closed by v2.1 §2 and §5. F3 and Y-C3 were reported
     CLOSED and are closed on their VALUES but not on their RENAME SURFACE by
     v2; they are closed by v2.1 §3.
```

---

## §6. Findings this correction opened on itself

**None creates a new author cell. None changes a mechanism.**

```text
O-5  THE BINDING CARRIES MIRROR SENTENCES THAT MUST BE AMENDED IN STEP.
     The §7 audit is scoped, by both reviews and by this correction, to the
     GOVERNING COMPOSITE v1.2, which is the operative document. Re-auditing for
     this correction surfaced SEVEN mirror statements in
     …V2_1_10_4_P1_BINDING.md that carry the same properties:
         :564-567   "Every other C1 property — witness/freezer role … 
                     WATCHDOG/FREEZE/<witness_id>.json observations — is carried
                     byte-for-byte"
         :579       "Treating it as supervisor death would produce a false
                     freeze"                      (mirrors site 13)
         :629-630   "The watchdog observes update-pipe EOF, freezes all known
                     groups per §W3.3, writes their observations, and exits"
                                                  (mirrors sites 3 and 7)
         :660-663   "FREEZE IS UNAVAILABLE — the carried §W3.3 quiescence proof
                     needs SIGNAL_GROUP"          (mirrors site 14)
         :860-863   "C1 — dedicated freezer watchdog … witness/freezer role …
                     WATCHDOG/FREEZE/<witness_id>.json observations"
         :932       invariant 451                 (mirrors invariant 60)
         :933       invariant 452 "the carried freeze/observe/exit route"
                                                  (mirrors invariant 61/site 11)
     THESE ARE NOT COUNTED IN THE TWENTY-TWO. They are the binding's carried
     statements of the same composite properties. A v1.3 handoff that amends the
     composite MUST carry the identical amendment into the binding's carried-
     property list, or the two governing documents disagree. Added as a handoff
     item at §7 item 6b. This is disclosed rather than left for a later
     reviewer to find, and it falls identically on both options.

O-6  I DID NOT AUDIT THE WHOLE PEER CHAIN. v2's closure weak point 6 stands
     unchanged and is NOT closed by this correction: the composite is audited
     exhaustively, §N5, §N10, §N11 and §Z4.6 were read directly, and the rest of
     the harness and settlement chain was searched by key name only. The X line
     recorded this as "a real, disclosed, still-open item that the R-B repair
     should be paired with before any implementation." IT REMAINS OPEN. §W3.3
     itself — the peer freeze procedure — is unamended and remains the
     supervisor's dead-watchdog procedure; no option amends it.

O-7  v2 CHARGED `_MSG_EOR` TO W-B ALONE, AND THAT IS WRONG. v2 §9.1 recorded
     "additional binding-block change | none | _MSG_EOR", and v2 §10's blast
     radius gave W-A no pinned constant. But v2 §4.3 G-1 gates W-A on the PCS
     having "ALREADY recorded PEER_CONTROL_ENDPOINT_LOST … (§5.2 defines that
     event, and it is shared by both options)", and v2's own closure §5 records
     that W-A "inherits §5.2 via the G-1 gate". W-A therefore needs the E-1a /
     E-1b discrimination and therefore needs `_MSG_EOR`. NEITHER REVIEW CAUGHT
     THIS. Corrected at §1.4: BOTH options add BOTH constants.
     EFFECT ON THE COMPARISON: it REMOVES a row that appeared to favour W-A, so
     it cannot help W-B's case dishonestly — it strengthens "the rows that
     decide did not move" by deleting one row that never should have moved.
     This is arithmetic, not a mechanism, and it is forced by repair 1's own
     requirement to state the exact blast-radius delta.

O-8  A PRE-EXISTING DISCREPANCY IN THE GOVERNING CHAIN, DISCLOSED, NOT REPAIRED.
     The composite's row 4 path is `WATCHDOG/FREEZE/<witness_id>.json`
     (:2236-2237). §W3.3 step 6 writes `WATCHDOG/FREEZE/<process_id>.json`
     (…V2_1_CORRECTION.md:763). Two signed documents name different filename
     preimages for the same artifact. v2 §0.3 W-7 corrected v1's transcription
     against §W3.3 and did not notice that the composite disagrees. THIS
     CORRECTION DOES NOT REPAIR IT: it is pre-existing, it predates this cell,
     it is immaterial to the freeze-executor choice, and repairing it is not one
     of the five bounded repairs. It is named so that no later reader believes
     the audit missed it, and so that whoever writes v1.3 resolves it
     deliberately. IT OPENS NO CELL AND CHANGES NO OPTION.
```

---

## §7. The corrected v1.3 handoff delta

**Replaces the named items of v2 §12; every other item of v2 §12 stands.**

```text
§12.0 COMMON TO BOTH SELECTIONS:

  1b. NEW. §P1-3.4: append `_MSG_EOR` and `_CLOCK_MONOTONIC`, in that order, to
      the pinned integer-constant list. §P1-3.5: add `_CLOCK_MONOTONIC == 1` to
      the integer-constant row. §P1-14.6: add S-25 (§1.2 B-7). COMMON, not
      W-B-only.

  5.  REPLACES v2 item 5. §P1-14.6: add the rules that the sixteen-token set is
      closed; that `_killpg` appears only inside the §P1-10.7 classifier and the
      `SIGNAL_GROUP` handler, both in the PCS root and nowhere else; that `KV`
      precedes every `_killpg`; and S-25. **Retain `S-12` unchanged.**

  6.  REPLACES v2 item 6. **§2.3's TWENTY-TWO sites**, replaced with the
      `R1`..`R22` texts of §2.4, in the option's variant. REPLACE contradictory
      rows, sentences and blocks; do not add beside them. `R19` and `R21` must
      be applied in the same step, and `R15`/`R18`/`R22` in the same step as
      `R9`.

  6b. NEW. Carry the identical amendment into …V2_1_10_4_P1_BINDING.md's seven
      mirror statements enumerated at §6 `O-5`, so the composite and the binding
      do not disagree. This is a mechanical carry, not a new decision.

  8.  REPLACES v2 item 8. §N5 of …V2_1_2_CORRECTION.md: apply
      `A-ABS-1`..`A-ABS-6` AND the five replacements `K1`..`K5` of §3.2.

  9.  REPLACES v2 item 9. §P1-15: add v2's classifier rows, plus rows 92..95
      (§1.3), 96..100 (§2.6) and 101..102 (§3.5).

  10. UNCHANGED. Recompute `H_FILE`, `H_BODY`, `H_GUARDDATA`, `H_NORMATIVE`,
      sentinel counts, the placeholder audit and guard fires; required
      placeholder and guard-fire counts remain **zero**.

§12.2 IF W-B IS SIGNED:
  12. DELETED. `_MSG_EOR` moved to common item 1b.
  Items 11, 13, 14, 15 stand unchanged, with item 15's site reference now
  reading "the row of §2.3 site 7 per `R7` W-B".

§12.1 IF W-A IS SIGNED:
  Items 11..18 stand unchanged, with item 18's site reference now reading
  "the row of §2.3 site 7 per `R7` W-A".

§12.3 IF NEITHER IS SIGNED: unchanged.
```

---

## §8. The exact blast-radius delta this correction produces

| Row | v2 said | v2.1 says | Which option it moves |
|---|---|---|---|
| normative composite prose sites | twelve / twelve | **twenty-two / twenty-two** | **neither** — identical on both |
| additional binding-block change | none / `_MSG_EOR` | **`_MSG_EOR` + `_CLOCK_MONOTONIC` / the same two** | **neither** — removes a row that wrongly favoured W-A (`O-7`) |
| peer contract sentences reopened | one / one | **five / five** (one file, three keys, one branch) | **neither** |
| new verifier rules | classifier rules | classifier rules **+ `S-25`** | **neither** |
| new §P1-15 test rows | classifier rows | classifier rows **+ 92..102** | **neither** |
| signed freeze-execution sites in the composite | one, implicit | **two, explicit** (`R19`, `R21`) | **neither** — §3 is common |
| topology / opcode changes | several / **zero** | **unchanged** — several / **zero** | **W-B**, exactly as before |
| new liveness dependency | yes / **none new** | **unchanged** | **W-B**, exactly as before |

**Every row this correction touched falls identically on W-A and W-B. The two
rows that decide — topology/opcode changes and the new liveness dependency —
were not touched at all.**

---

## §9. Recommendation after repair — unchanged

> **W-B remains recommended**, on the same five criteria and no others:
> signed-authority fidelity, constructibility, mechanical testability, liveness,
> and blast radius.

```text
WHY THE CORRECTION DOES NOT MOVE IT:
  the site count grew by ten, identically on both;
  the reopened-sentence count grew by four, identically on both;
  one pinned constant was added, identically on both;
  one pinned constant was RE-ASSIGNED from W-B alone to both, which removes a
    W-A advantage v2 recorded in error;
  the R2/R9 separation is textual precision in replacements that are identical
    for both options;
  W-B's zero topology and opcode changes stand;
  W-A's new liveness dependency on a process whose loss is one of the
    conditions C1 exists to handle stands.

BOTH INDEPENDENT LINES REACHED THE SAME RECOMMENDATION AFTER THEIR OWN REPAIRS
AND BOTH RE-AFFIRMED IT IN THEIR REVISE CONFIRMATIONS.

**THE AUTHOR SELECTS NOTHING, ACCEPTS NO TOKEN, MINTS NO TOKEN, AND PREDICTS NO
OUTCOME.** Neither W-A nor W-B is selected. The identity cell is not selected.
```

---

## §10. Tokens — unchanged from v2 §11

```text
SELECTION, exactly one, NEITHER SELECTED:
  I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
  I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS

PER-OPTION AMENDMENT, conditional on the selection:
  P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1        with W-A only (v2 §4.7)
  P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1          with W-B only (v2 §5.8)

COMMON AMENDMENTS, required under EITHER selection:
  P1_FREEZE_ABSENT_FALLBACK_NULLABLE_IDENTITY_V1 v2 §6 + §3 of this correction
  P1_PCS_FREEZE_CLASSIFIER_V1                    v2 §3 + §1 of this correction
  P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1       §2 of this correction, now
                                                 twenty-two sites
  P1_FREEZE_PUBLICATION_L6_L9_V1                 v2 §8, unchanged

NO TOKEN IS ADDED, REMOVED OR RENAMED BY THIS CORRECTION. The three common
amendment tokens whose CONTENT this correction enlarges keep their v2 names and
their v2 meanings; what changed is the exact surface each one covers, which is
now stated correctly rather than under-stated. NONE IS SIGNABLE until a bounded
independent X/Y final confirmation round confirms this correction on identical
bytes.
```

---

## §11. Invariants this correction leaves exactly as they were

```text
N-1  THE BLOCKER REMAINS PROVED, on the same four mechanisms, both lines
     concurring and both re-affirming in their v2 confirmations.
N-2  THE PCS NEVER RETAINS THE WATCHDOG UPDATE-PIPE WRITE END, under either
     option. §P1-8.7's unconditional close (composite :1398) is untouched.
N-3  THE PCS REMAINS THE SOLE CALLER of fork, posix_spawn, kill, killpg and
     every wait-family primitive. `S-12` is retained unchanged under both
     options. `R21` admits a second freeze-EXECUTION SITE, not a second CALLER:
     both sites' `_killpg` executes in the PCS root and nowhere else.
N-4  W-B MAY REMAIN RECOMMENDED and does (§9) — but NO OPTION IS SELECTED.
N-5  THE IDENTITY CELL IS NEITHER SELECTED NOR REPAIRED HERE. `process_id`
     remains a CONSTRUCTIBLE OPAQUE CLAIM IDENTIFIER, not a PID, mandatory and
     non-null on every fallback branch, exactly as v2 §6 and the Y line's
     determination 2 record.
N-6  PCS JOURNAL STATE REMAINS SCIENTIFICALLY INVISIBLE and distinct from peer
     freeze evidence: `L8`, `ND-1`..`ND-3`, and now `R21`'s explicit test row 98.
N-7  NO NEW AUTHOR CELL IS OPENED.
N-8  T = NOT_ACTIVATED; the programme claim is OPEN.
```

---

## §12. Negative space

This correction creates nothing executable and authorizes no selection, X/Y
verdict, amendment acceptance, implementation, commit, verifier or manifest
edit, process, socket, pipe, fork, exec, signal, wait or `prctl` operation,
supervisor, PCS, controller, worker or watchdog, capability, world, learner,
entropy, capacity artifact, custody disposition, result manifest, spend, datum,
outcome, Proof or claim movement. No freeze was executed, requested, journalled
or witnessed. No `/proc` read was performed against any live process. It
predicts no qualification and no comparison outcome. It selects neither option
and accepts no token. It modified no existing file. `T` remains `NOT_ACTIVATED`;
the programme claim remains `OPEN`.
