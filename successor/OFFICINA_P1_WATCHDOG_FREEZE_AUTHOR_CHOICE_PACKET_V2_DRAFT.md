# Officina P1 watchdog-freeze mechanism — author choice packet v2 (draft)

**Author:** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This packet selects nothing.**

**No token here is signable** until a bounded independent X-line and Y-line
confirmation round confirms this packet on identical bytes. `T` is
`NOT_ACTIVATED`; the programme claim is `OPEN`. This document creates nothing
executable and authorizes no implementation, activation, resource spend, T/Q/C
datum, outcome, Proof or claim movement.

**Status.** v2 is a **self-contained replacement** for
`successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`. It is
not a patch and is not read alongside v1. v1 and both review files are preserved
byte-untouched as the evidentiary record.

**Bounded repair mandate.** v2 closes, one-to-one, the findings of two
independent reviews, both treated here as **binding defect reports**:

```text
X-line, reviews/opus_officina_p1_watchdog_freeze_choice_review.md
        F1, F2, F3
Y-line, reviews/sol_officina_p1_watchdog_freeze_choice_review.md
        Y-C1, Y-C2, Y-C3, Y-M1, Y-M2, Y-M3, Y-m1
```

**Where the two lines differ, v2 adopts the stricter constructible rule.** Three
places where they differ are named at §0.2 with the rule taken and why.

---

## §0. What v2 changes, and where

### §0.1 Finding-to-locus map

| Finding | Class | v2 locus | Nature of the repair |
|---|---|---|---|
| Y-C1 | Critical | §3 (whole section, new) | every peer-lease/`table_seq` claim **removed**; the scope is defined solely from P1-owned handle state; total inclusion/exclusion over every signed handle state; kernel verification pinned; dedup pinned; a closed result token and a single durable continuation for every identity, signal, `/proc`, enumeration, quiescence, timeout, denial, structural and partial-freeze result |
| Y-C2 | Critical | §4.2, §4.3, §4.6 | `request_seq` and `table_seq` **removed**; one constant no-target request identity per `(generation_id, watchdog_handle)`; exactly one accepted action; a mechanically verifiable PCS-side endpoint-loss gate; explicit pricing of the forced invalidity and full charge |
| Y-C3 | Critical | §6 (new) | the bounded `ABSENT`-branch peer-schema/predicate amendment, its exact reopened sentences, and its own common token |
| Y-M1 | Major | §5.2, §5.3, §5.4, §8 | `SUPERVISOR_LOST` **withdrawn**; `PEER_CONTROL_ENDPOINT_LOST`; `MSG_EOR` discrimination; the four indistinguishable causes; the "same kernel event" claim withdrawn |
| Y-M2 | Major | §5.5 | record-before-act: validate, `ACCEPTED`+fsync, classify, `COMPLETED`+fsync only on the exact valid terminal; all cuts, replay and partial side effects |
| Y-M3 | Major | §4.5 | W-A's dispatch ordered against endpoint loss and the non-returning reaper transition; deterministic routes for watchdog death, socket EOF, timeout, stale generation, PCS restart, simultaneous loss |
| X F1 | must fix | §7 (new) | the **complete** freezer/witness sentence audit, twelve sites, with exact replacements for **both** options; "W-B amends zero P1 sentences" **withdrawn** |
| X F2 | must fix | §5.2 | same repair as Y-M1, taken at Y's stricter framing |
| X F3 | should fix | §6 | repaired **constructively** at Y's stricter rule, not merely reframed as pre-existing |
| Y-m1 | Minor | §8 | `L6` split into `L6`–`L9` with the three mandated sentences and the no-distinguishability rule |

### §0.2 Where X and Y differ — the rule taken

```text
D-1  THE ABSENT FALLBACK.
     X F3 asks for a FRAMING repair ("say it adds no new dependency; the
     operability question is pre-existing and the identity cell governs it").
     Y-C3 asks for a CONSTRUCTIVE repair (a bounded peer-schema amendment
     making pgid/start_identity null exactly on the ABSENT branch).
     TAKEN: Y. §6 amends the schema, names every reopened sentence, and adds a
     dedicated common token. X's framing point is also stated (§6.6), but it is
     not the repair.

D-2  W-A's STATUS.
     X finds W-A's capability "genuinely non-general" and lists two W-A gaps as
     "non-blocking, close only if W-A is ever selected".
     Y finds W-A "cannot be offered for informed selection in its current form"
     and requires a constant one-shot key, a gate or explicit pricing, and an
     ordering contract, "otherwise mark W-A non-selectable".
     TAKEN: Y. §4 rebuilds W-A to Y's specification, and BOTH of X's
     "non-blocking" gaps (§4.4 slot-6 type; §4.4 descriptor accounting) are
     closed here rather than deferred. W-A is therefore repaired to selectable
     rather than marked non-selectable — but §9.4 states plainly what the gate
     costs W-A's rationale.

D-3  THE EOF TRIGGER.
     X F2 asks for "loss of the supervisor write stream, fail-safe to
     freeze-and-invalidate", keeping the name PEER_EOF.
     Y-M1 requires replacing SUPERVISOR_LOST with PEER_CONTROL_ENDPOINT_LOST
     and forbids calling it death or "the same kernel event" as watchdog EOF.
     TAKEN: Y. §5.2 uses PEER_CONTROL_ENDPOINT_LOST throughout and withdraws
     the same-event claim. X's MSG_EOR mechanic is adopted as the exact
     discriminator.
```

### §0.3 Sentences withdrawn from v1

```text
W-1  "table_seq ... must be a table_seq the PCS has recorded as published"
     (v1 §3.2 field 5, §3.3 BINDING).            WITHDRAWN at §4.2 — the PCS has
     no table-publication input; no specified event can create that record.
W-2  "SCOPE := every handle h ... h.state in {SPAWNED, RUNNING}" (v1 §3.4).
                                                 WITHDRAWN at §3.1 — omits
     STOPPED, ignores pgid_or_null nullability, and never verifies the group.
W-3  "one freeze ... per generation" priced as denial-of-progress only
     (v1 §5.7).                                  WITHDRAWN at §4.6 — the
     grammar permitted repeated fresh operations, and the effect is forced
     invalidity with full charge, not denial only.
W-4  "The supervisor's end was closed by the kernel at its exit, so this is a
     kernel fact, not a report" and "The two EOFs are the same kernel event"
     (v1 §4.2 E-1, §4.2 closing).                WITHDRAWN at §5.2 — a
     zero-length receive proves endpoint unavailability, not death, and the two
     descriptors are two independent events.
W-5  "W-B ... amends zero P1 sentences" (v1 §5.1, §6, closure §6).
                                                 WITHDRAWN at §7 — twelve
     composite sentences assign the freezer or witness role and both options
     must amend all twelve.
W-6  "routes exactly where the signed chain already routes one" presented as
     unconditional (v1 §4.5).                    WITHDRAWN at §6 — the signed
     fallback schema cannot be populated on the ABSENT branch without the §6
     amendment.
W-7  v1 §1.1 step 6's witness path "WATCHDOG/FREEZE/<witness_id>.json".
                                                 CORRECTED at §1.1 — §W3.3
     (`…V2_1_CORRECTION.md:763`) says `<process_id>.json`. Immaterial to the
     proof; corrected because X caught it.
```

No withdrawn sentence is restated anywhere in v2 in paraphrase.

---

## §1. The blocker, independently proved

The reporting author (myself, in the identity packet §6) is treated as
untrusted. The blocker was re-established from the contracts, and **both review
lines independently confirmed it as PROVED**. It is stronger than reported:
four independent mechanisms, any one sufficient.

### §1.1 What a freeze mechanically requires

§W3.3, `…SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md:744-770`, is the one
mechanical evidence path, and the P1 binding routes to it verbatim
(`…V2_1_10_4_P1_BINDING.md:627-629`: "freezes all known groups per §W3.3"):

```text
1. verify /proc/<leader>/stat start identity matches      needs a numeric pid
2. killpg(pgid, SIGSTOP)                                  needs a signal syscall
                                                          and a numeric pgid
3. prove quiescence by enumerating /proc                  needs numeric pids
4. killpg(pgid, SIGKILL) after the first failed pass      needs a signal syscall
5. sample freeze_ns, set quiescence
6. write WATCHDOG/FREEZE/<process_id>.json itself         needs the runtime root
```

Step 6's path is `<process_id>.json` (`…V2_1_CORRECTION.md:763`). v1 transcribed
it as `<witness_id>.json`; corrected here.

So a freeze requires, irreducibly: **a numeric process-group id**, **the
`killpg` syscall**, and **filesystem reach into the runtime root**.

### §1.2 Mechanism 1 — the composite's own verifier forbids it

v1.2 §P1-14.6 rule `S-12`, at composite line 2601:

> `S-12  subprocess, Popen, fork, waitpid, kill, killpg and system appear on no
> path of generic_harness.py`

The watchdog's role entry **is** in `generic_harness.py`: `A-13` calls "exactly
one pinned entry function, selected by `argv[7]` from a closed four-entry
mapping", and `A-10` imports `philosophia.officina.generic_harness` as the only
import. Therefore `killpg` **cannot appear on the watchdog's path**.

**This alone is dispositive.** The X line additionally answered the author's
open question in the negative: the role-bootstrap root (`A-1`..`A-13`) is a
fixed verification-then-dispatch sequence with an allowlist of `{os, sys,
fcntl}` and no room for target behaviour, so **no conforming build can relocate
the watchdog freeze out of `generic_harness.py`**.

### §1.3 Mechanism 2 — the signed authority sentence

`…V2_1_10_4_P1_BINDING.md:150-153`: the PCS "is the sole caller of `fork`,
`posix_spawn`, `kill`, `killpg` and every `wait`-family primitive." A watchdog
`killpg` contradicts the signed selection directly, independently of `S-12`.

### §1.4 Mechanism 3 — no endpoint, and none can be added without cost

v1.2 §P1-6.2: the watchdog's slot set is `{3,4,5,7,8,9,10}` — update read, ack
write, harness source, role-bootstrap source, `src` dir, interpreter, package
root. **Slot 6 is "not used; explicitly closed by a file action"**, and §P1-6.4
makes `{6}` the `WATCHDOG` explicit-close group. The watchdog holds **no PCS
socket**, and §P1-9.2 property 6 (composite `:1446`) states it "communicates
only over its two sealed pipes at slots 3 and 4".

It also holds **no runtime-root directory descriptor** — role slot 5 is the
harness source object, so it cannot `openat` `WATCHDOG/FREEZE/` to write the
witness.

### §1.5 Mechanism 4 — no relay exists at the only moment it is needed

The trigger is update-pipe EOF, which occurs because the supervisor's update
write end is gone. There is therefore no supervisor to relay a request to. The
PCS holds **no write end on the watchdog update pipe** — §P1-8.7 (composite
`:1398`) has it "close[] its copies of the supervisor's ends unconditionally"
after the send — so the PCS cannot speak to the watchdog either.

**A load-bearing corollary, which constrains every option below.** The PCS
*must not* retain a write end on the watchdog update pipe. If it did, the pipe
would never reach EOF on supervisor death, and update-pipe EOF is the **single
remaining supervisor-death detector** under P1 (§P1-9.2 property 10 "by no other
mechanism", `:1457-1458`; the `getppid()` detector deliberately deleted,
property 11 and composite `:203-205`). **Any design that gives the PCS a channel
to the watchdog by retaining that write end destroys C1's only detector and is
inadmissible.** The X line verified this corollary independently.

### §1.6 Verdict

**The blocker remains PROVED**, on the same four mechanisms, confirmed by both
independent lines. Under the selected P1 architecture, update-pipe EOF is
observable and no specified route can execute the freeze.

---

## §2. Rejected route families

| Family | Rejected because |
|---|---|
| give the watchdog numeric PID/PGID knowledge | reopens the identity cell inside this one, and puts numeric identity in a second contaminated-adjacent process for no gain over §4/§5 |
| give the watchdog direct signal syscalls | contradicts `S-12` and the sole-caller sentence; deletes the P1 authority model at its centre |
| give the watchdog a general PCS client | a general client is a general capability: it would let a compromised watchdog reach `SPAWN_ROLE`, `SIGNAL_ROLE` and `REAP_ROLE`. Only a single-opcode, target-free capability is admissible (§4) |
| relay through the supervisor after the peer control endpoint is lost | impossible by construction: endpoint loss *is* the trigger (§1.5) |
| have the PCS retain a write end on the update pipe | **inadmissible** — destroys the single supervisor-death detector (§1.5 corollary) |
| abandon the freeze and terminate leased roles instead | deletes signed C1 rather than implementing it, and destroys the `freeze_ns` evidence §W3.4 settlement consumes. A C1 replacement requiring a fresh selection, not a mechanism repair |
| **a supervisor-to-PCS lease-table publication opcode** | **NEW in v2.** Y-C1 notes that an exact *lease* scope would require this. It is rejected: it adds a tenth opcode, makes P1 hold peer scheduling state, and contradicts `R-L4`'s one-way boundary and §P1-13.0's "the PCS executes no peer-layer code and holds no peer-layer state" (composite `:2003`). §3 therefore defines the scope from P1-owned state alone |

---

## §3. The common freeze classifier — total, constructible, P1-owned (closes Y-C1)

**This section is shared verbatim by W-A and W-B.** Both options execute exactly
this classifier; they differ only in what triggers it (§4, §5).

### §3.1 The withdrawn v1 scope

```text
WITHDRAWN, v1 §3.4, verbatim:
  "SCOPE := every handle h in the current generation with
             h.role in {CONTROLLER, WORKER} and
             h.state in {SPAWNED, RUNNING} and
             h.ownership == OWNED"

WHY IT IS DEFECTIVE, on Y-C1's four counts, each verified:
  (i)   it omits state STOPPED, which is a signed member of the handle state
        set (composite :1261) and names a live, unreaped, leased process;
  (ii)  it never requires h.pgid_or_null to be non-null, although the signed
        handle shape names the field NULLABLE (composite :1260);
  (iii) it never establishes the kernel-verified group that SIGNAL_GROUP's own
        signed precondition requires (composite :1223, :1271, :1427);
  (iv)  it does not deduplicate groups before signalling.

ALSO WITHDRAWN, v1 §3.2 field 5 and §3.3 BINDING: every reference to table_seq
and to a "lease" scope. Watchdog lease tables are peer-owned (composite
:1993-2007), the PCS holds no peer-layer state, and no specified event can
create the PCS table-publication record v1 required. See §4.2.
```

### §3.2 A gap in v1.2 that this repair must fill, disclosed

`pgid_or_null` appears in the composite **exactly once** — at `:1260`, in the
handle-table shape. **No signed rule populates it, and no signed rule defines
what "a kernel-verified group is recorded for the handle" means for a
`CONTROLLER` or `WORKER` handle.** The middle's group verification at `c10`/`c11`
(composite `:1079`) is about `pid_mid`, not about role handles.

This is a pre-existing v1.2 gap that Y-C1 exposed. v2 fills it at §3.4, using
**only primitives already in the PCS binding block** (§P1-3.4, composite
`:409-417`), with one bounded parse extension disclosed at §3.3. It is counted
in both options' blast radius at §9 because both options need it.

### §3.3 One bounded parse extension: `STAT_OBSERVE_G`

```text
STAT_OBSERVE (§P1-10.3, composite :1600-1626) already opens /proc/<pid>/stat
with the bound _open/_read/_close primitives and parses, after the final ")",
the state field, the ppid field, and the 20th token (the kernel start time).

STAT_OBSERVE_G(pid) is the SAME read with the SAME five-way result
  (ABSENT | PRESENT_VALID | UNREADABLE | UNPARSABLE | ERROR)
and the SAME failure classification, returning on PRESENT_VALID the tuple
  (start_identity, ppid, state, pgrp, session)
where, counting whitespace-separated tokens AFTER the final ")":
  token 1 = state, token 2 = ppid, token 3 = pgrp, token 4 = session,
  token 20 = start_identity.
A short token list, a non-integer pgrp or session, or any parse failure is
UNPARSABLE, exactly as today.

WHAT THIS COSTS: no new primitive, no new import, no new module. _open, _read,
_close and _listdir are already bound (composite :409-411). This is an
extension of one parse function's return tuple and is checked by the existing
S-family AST rules unchanged. It is disclosed as an amendment to §P1-10.3 and
appears in both options' blast radius.

WHY /proc AND NOT getpgid: os.getpgid is NOT in the PCS's pinned primitive
binding block (composite :409-417). Using it would require adding a name to a
block that S-3 fixes exactly, in exactly the order given. Reading pgrp from the
stat line the PCS already reads is strictly smaller.
```

### §3.4 `KV` — kernel group verification, performed before **each** group action

```text
KV(h) is evaluated IMMEDIATELY BEFORE every _killpg issued against h's group,
separately for the SIGSTOP and for any later SIGKILL. It is never cached across
a signal.

KV-1  OWNERSHIP(h.pid) is OWNED, and h.state is not REAPED.
      Otherwise: NOT_VERIFIED, token EXCLUDED_OWNERSHIP_NOT_OWNED.
KV-2  r := STAT_OBSERVE_G(h.pid).
KV-3  r is PRESENT_VALID.
      ABSENT       ⇒ NOT_VERIFIED, token GROUP_LEADER_ABSENT
      UNREADABLE   ⇒ NOT_VERIFIED, token GROUP_LEADER_UNREADABLE
      UNPARSABLE   ⇒ NOT_VERIFIED, token GROUP_LEADER_UNPARSABLE
      ERROR        ⇒ NOT_VERIFIED, token GROUP_LEADER_STAT_ERROR
KV-4  r.start_identity == h.start_identity.
      Otherwise: OWNERSHIP := CONTRADICTED irreversibly (§P1-10.4 row I-2),
      NOT_VERIFIED, token GROUP_IDENTITY_MISMATCH, and no signal ever again for
      this handle.
KV-5  h.pgid_or_null is not null AND r.pgrp == h.pgid_or_null.
      pgid_or_null is null           ⇒ NOT_VERIFIED, token GROUP_PGID_NULL
      r.pgrp != h.pgid_or_null       ⇒ NOT_VERIFIED, token GROUP_CHANGED
KV-6  r.pgrp is not the PCS's own group (_getpid()'s group, read by
      STAT_OBSERVE_G(_getpid())), is not any WATCHDOG handle's leader group,
      and is not the recorded supervisor group.
      Otherwise: NOT_VERIFIED, token GROUP_FORBIDDEN_TARGET, and the classifier
      terminates immediately with FREEZE_NOT_ATTEMPTED (§3.8) — this is a
      structural violation of the handle table, not a per-group skip.
ALL SIX ⇒ VERIFIED.

POPULATION OF pgid_or_null, pinned here because v1.2 does not pin it:
  P-1  at a successful _posix_spawn of a CONTROLLER or WORKER, which the
       composite performs with setsid=True (composite :480-481), the kernel has
       made the child a session and group leader, so the PCS sets
       pgid_or_null := the returned pid.
  P-2  for a WATCHDOG handle, spawned with setsid=False (composite :1432-1433),
       pgid_or_null stays NULL. A watchdog handle is never in scope and is
       never a killpg target, exactly as invariant 57 (composite :2726) and
       §P1-8.3 already require.
  P-3  pgid_or_null is written exactly once per handle and is never rewritten.
       A KV-5 disagreement is GROUP_CHANGED, never a silent update.

KV-6 IS LOAD-BEARING. The watchdog is spawned with setsid=False and therefore
shares the PCS's process group (composite :1432-1433: "it is not a session
leader and is never a killpg target"). Without KV-6 a corrupted handle table
could aim killpg at the PCS's own group and stop the PCS and the watchdog. KV-6
is checked before every signal, not once.
```

### §3.5 The scope, total over every signed handle state

```text
SC-1  Consider every handle h in the PCS's own in-memory handle table.
SC-2  h is IN SCOPE iff ALL of:
        h.generation_id == the PCS's current generation_id
        h.role in {CONTROLLER, WORKER}
        h.ownership == OWNED
        h.state != REAPED
        KV(h) is VERIFIED
SC-3  SCOPE := the set of DISTINCT h.pgid_or_null values of the in-scope
      handles, in ASCENDING NUMERIC order. Duplicates are collapsed BEFORE any
      signal is sent; a group is signalled at most once per pass.
SC-4  SCOPE is computed once, from the PCS's own handle table and from
      /proc reads performed by the PCS, and from NOTHING ELSE. No peer state,
      no lease table, no table_seq, no supervisor input, and no watchdog input
      contributes to it. It is never widened, and it is never recomputed to
      include a handle created after the classifier began — no handle can be
      created after the trigger in either option (§4.5, §5.2).
```

**Total inclusion/exclusion, every signed handle state and ownership value.**
The signed sets are `state in {SPAWNED, STOPPED, RUNNING, REAPED}` and
`ownership in {OWNED, CONTRADICTED, REAPED}` (composite `:1261-1263`).

| Handle condition | In scope? | Token recorded | Class |
|---|---|---|---|
| role `CONTROLLER`/`WORKER`, `OWNED`, state `SPAWNED`, KV verified | **yes** | — | — |
| role `CONTROLLER`/`WORKER`, `OWNED`, state `STOPPED`, KV verified | **yes** — v1 wrongly omitted this | — | — |
| role `CONTROLLER`/`WORKER`, `OWNED`, state `RUNNING`, KV verified | **yes** | — | — |
| state `REAPED` | no | `EXCLUDED_STATE_REAPED` | **benign** — death was proved by `REAPED_POSITIVE`, the only death proof in the contract (composite `:1595-1597`) |
| ownership `REAPED` | no | `EXCLUDED_OWNERSHIP_REAPED` | **benign** — same proof |
| ownership `CONTRADICTED` | no | `EXCLUDED_OWNERSHIP_CONTRADICTED` | **NON-BENIGN** — ownership is lost, no signal may ever be sent (§P1-10.4 I-10), and the process is **not proved dead** |
| role `WATCHDOG` | no | `EXCLUDED_ROLE_WATCHDOG` | **benign** — invariant 57; it holds no lease and is never a `killpg` target |
| `pgid_or_null` is null on an `OWNED` unreaped role handle | no | `GROUP_PGID_NULL` | **NON-BENIGN** — a live leased process the PCS cannot address by group |
| KV fails for any reason other than `GROUP_FORBIDDEN_TARGET` | no | the KV token of §3.4 | **NON-BENIGN** |
| `h.generation_id != current` | no | `SCOPE_STALE_GENERATION_HANDLE` | **STRUCTURAL** — no PCS may adopt a live generation (composite `:1774-1777`), so such a handle cannot legally exist; the classifier terminates with `FREEZE_NOT_ATTEMPTED` |
| duplicate `pgid` among in-scope handles | collapsed | `DEDUPLICATED`, with the count | **benign** — recorded, not an error |

**On duplicates.** Because `setsid=True` makes `pgid == pid` at creation (`P-1`)
and an `OWNED` unreaped child holds its pid until the PCS's own targeted reap
(the reuse proof, composite `:1541-1550`), two in-scope handles cannot share a
pgid in a conforming run. `SC-3` is therefore expected to be a no-op, and the
classifier **asserts** the collapse count is zero rather than assuming it. A
non-zero count is recorded and is benign; it is not evidence of anything.

### §3.6 The per-group classifier — closed result tokens

For each `g` in `SCOPE`, in ascending order:

```text
C-1  KV of the handle whose pgid is g (re-evaluated: §3.4 forbids caching).
     NOT_VERIFIED ⇒ the KV token; no signal; next group.
C-2  s := _killpg(g, 19)                                        SIGSTOP
     Classified by the SIGNAL_ATTEMPT six-way rule of §P1-10.5 (composite
     :1649-1666), which the composite already applies to _killpg verbatim
     (:1607-1610):
       SENT          ⇒ continue to C-3
       GONE  (ESRCH) ⇒ under OWNED this is a contradiction, not a race:
                       OWNERSHIP := CONTRADICTED; no further signal;
                       token GROUP_SIGNAL_GONE
       INTERRUPTED   ⇒ retry the SAME signal at T_SUPERVISOR_POLL_INTERVAL_NS
                       within this group's deadline; on expiry ⇒ ERROR
       DENIED (EPERM)⇒ no further signal in this schedule; ownership NOT
                       contradicted; token GROUP_SIGNAL_DENIED
       ERROR         ⇒ token GROUP_SIGNAL_ERROR
       STRUCTURAL_VIOLATION (the return is not None, or a BaseException outside
                       the §P1-10.5 errno set) ⇒ OWNERSHIP := CONTRADICTED
                       irreversibly; no signal ever again; token
                       GROUP_SIGNAL_STRUCTURAL
C-3  Quiescence passes, per §W3.3 step 3, executed BY THE PCS:
       members := { p : STAT_OBSERVE_G(p).pgrp == g }
                  ∪ { p : p's session id or parent chain reaches a member }
       enumerated by _listdir("/proc") — already a bound primitive — and one
       STAT_OBSERVE_G per numeric entry.
       Require every member to be ABSENT, or state "T", or state "Z".
       PASS INTERVAL: T_SUPERVISOR_POLL_INTERVAL_NS (50_000_000)
       MAX PASSES   : T_PCS_QUIESCE_MAX_PASSES = 16
       After the FIRST failed pass: _killpg(g, 9), classified exactly as C-2.
C-4  Terminal for this group:
       proved on some pass  ⇒ freeze_ns := _clock(CLOCK_MONOTONIC) sampled ON
                              THAT PASS, never the signal-send time;
                              token GROUP_FROZEN_PROVED
       passes exhausted, or a reachable process is neither stopped, dead nor
       absent                ⇒ freeze_ns := null;
                              token GROUP_QUIESCENCE_UNKNOWN
       _listdir raises or an entry is unreadable ⇒ token GROUP_ENUM_UNREADABLE
       an enumeration result fails its structural test ⇒ token
                              GROUP_ENUM_STRUCTURAL
       any BaseException escaping C-1..C-3 for this group ⇒ token
                              GROUP_EXCEPTION; no retry; next group
```

**The complete closed per-group token set, sixteen values.** No seventeenth
value is expressible, and there is no "and similar" category:

```text
GROUP_FROZEN_PROVED              the ONLY token compatible with a valid terminal
GROUP_QUIESCENCE_UNKNOWN
GROUP_LEADER_ABSENT
GROUP_LEADER_UNREADABLE
GROUP_LEADER_UNPARSABLE
GROUP_LEADER_STAT_ERROR
GROUP_IDENTITY_MISMATCH
GROUP_PGID_NULL
GROUP_CHANGED
GROUP_SIGNAL_GONE
GROUP_SIGNAL_DENIED
GROUP_SIGNAL_ERROR
GROUP_SIGNAL_STRUCTURAL
GROUP_ENUM_UNREADABLE
GROUP_ENUM_STRUCTURAL
GROUP_EXCEPTION
```

**Deadline.** Each group's classifier runs within
`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` (10 s) from its own start; expiry yields
`GROUP_QUIESCENCE_UNKNOWN`. The whole classifier is bounded by that per-group
bound times `|SCOPE|`, which is finite because the handle table is finite. **No
unbounded wait exists anywhere in the classifier.**

**Why the pass interval is not §W3.3's constant.** §W3.3 uses
`T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS = 100_000_000`
(`…V2_1_CORRECTION.md:60-61`). The composite states at `:267-268`: "A value of
100_000_000 appears in no rule of this contract." Importing §W3.3's constant
would contradict that signed sentence. v2 therefore reuses the already-pinned
`T_SUPERVISOR_POLL_INTERVAL_NS = 50_000_000` with sixteen passes, which gives
**the same 800 ms total budget** as §W3.3's eight passes of 100 ms and
introduces **no new nanosecond numeral**. `T_PCS_QUIESCE_MAX_PASSES = 16` is one
new count constant in §P1-2.2. This deviation from §W3.3's literal constants is
deliberate, is taken to avoid contradicting a signed sentence, and is disclosed
in both options' blast radius.

### §3.7 Result token to durable continuation — one row each, exhaustive

| Token | Signal sent? | Ownership after | Journal record | Contributes a valid terminal? |
|---|---|---|---|---|
| `GROUP_FROZEN_PROVED` | yes | `OWNED` | group id, token, `freeze_ns`, member count | **yes** |
| `GROUP_QUIESCENCE_UNKNOWN` | yes | `OWNED` | group id, token, `freeze_ns = null`, unresolved count | no |
| `GROUP_LEADER_ABSENT` | **no** | `OWNED` | group id, token | no |
| `GROUP_LEADER_UNREADABLE` / `_UNPARSABLE` / `_STAT_ERROR` | **no** | `OWNED` | group id, token | no |
| `GROUP_IDENTITY_MISMATCH` | **no** | `CONTRADICTED` | group id, token | no |
| `GROUP_PGID_NULL` | **no** | `OWNED` | handle id, token | no |
| `GROUP_CHANGED` | **no** | `OWNED` | handle id, token, both pgid values | no |
| `GROUP_SIGNAL_GONE` | attempted | `CONTRADICTED` | group id, token | no |
| `GROUP_SIGNAL_DENIED` | attempted | `OWNED` | group id, token | no |
| `GROUP_SIGNAL_ERROR` | attempted | `OWNED` | group id, token | no |
| `GROUP_SIGNAL_STRUCTURAL` | attempted | `CONTRADICTED` | group id, token | no |
| `GROUP_ENUM_UNREADABLE` / `_STRUCTURAL` | yes (stop was sent) | `OWNED` | group id, token | no |
| `GROUP_EXCEPTION` | unknown | unchanged | group id, token | no |
| `EXCLUDED_STATE_REAPED` / `EXCLUDED_OWNERSHIP_REAPED` / `EXCLUDED_ROLE_WATCHDOG` | no | unchanged | handle id, token | **does not defeat** a valid terminal (benign) |
| `EXCLUDED_OWNERSHIP_CONTRADICTED` | no | unchanged | handle id, token | no — non-benign |
| `DEDUPLICATED` | n/a | unchanged | collapse count | **does not defeat** (benign) |
| `SCOPE_STALE_GENERATION_HANDLE` / `GROUP_FORBIDDEN_TARGET` | no | unchanged | handle id, token | terminates the classifier at `FREEZE_NOT_ATTEMPTED` |

`ABSENT` is never death anywhere in this table: `GROUP_LEADER_ABSENT` yields no
signal and no valid terminal, consistent with §P1-10.4 row I-5 and with "only
`REAPED_POSITIVE` … is the only proof of death anywhere in this contract"
(composite `:1595-1597`).

### §3.8 The classifier terminal — exactly three values

```text
FREEZE_TOTAL_PROVED     every group in SCOPE has GROUP_FROZEN_PROVED, and no
                        NON-BENIGN exclusion was recorded. This is the ONLY
                        valid terminal and the ONLY terminal on which a
                        COMPLETED journal append is permitted.
FREEZE_INCOMPLETE       any other per-group token, or any NON-BENIGN exclusion.
FREEZE_NOT_ATTEMPTED    GROUP_FORBIDDEN_TARGET or SCOPE_STALE_GENERATION_HANDLE
                        during scope computation; no signal was sent to any
                        group.
```

### §3.9 What every terminal settles to — invalidity dominance, stated once

```text
S-1  UNDER BOTH OPTIONS, AN EXECUTED FREEZE DETERMINISTICALLY YIELDS
     WHOLE-GENERATION PROCESS INVALIDITY WITH FULL CHARGE. There is no branch,
     including FREEZE_TOTAL_PROVED, in which a freeze produces a valid
     terminal, a completion, a resource success, a capacity fact, a custody
     disposition, a qualification input, a comparison input, a Q or C fact, or
     a scientific outcome. The peer witness is ABSENT in every case (§6), and
     §N5.3's routing is record-first live-process invalidity, the all-live
     batch, the unknowable pool, public cause PROCESS, and full §4c charging
     (…V2_1_2_CORRECTION.md:876-886).
S-2  FREEZE_INCOMPLETE and FREEZE_NOT_ATTEMPTED settle IDENTICALLY to
     FREEZE_TOTAL_PROVED at the peer layer. The terminal governs only the P1
     journal state and the P1 unresolved accounting.
S-3  A classifier that does not reach any terminal — because the PCS died, or
     because a live failure escaped every handler — leaves its journal entry at
     ACCEPTED, which is INCONCLUSIVE, which is whole-generation process
     invalidity per §P1-11.6 with invalidity dominant (composite :1849-1866,
     §P1-13.5 :2323-2330).
S-4  NO P1 JOURNAL FACT IS PEER FREEZE EVIDENCE. The journal is P1-owned; the
     peer freeze witness is a t-freeze-observation.v1 the watchdog no longer
     writes. See §8.
```

### §3.10 A named residual the classifier cannot remove

```text
TARGET-INDUCED GROUP ESCAPE. A controller or worker target program runs after
SIGCONT and may call setsid() or setpgid(). If it does, KV-5 fails with
GROUP_CHANGED, NO SIGNAL IS SENT to that group, and the terminal is
FREEZE_INCOMPLETE. The escaped tree keeps running as an orphan.

This is FAIL-CLOSED and correct — the PCS must never killpg a group it did not
create and cannot verify — but it is a real residual and it is not removed by
either option. It is an infrastructure fact and never a scientific or resource
outcome. It is covered by L7 and L9 (§8).

The activation protocol's "process group is immutable while open"
(…OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md:300-305) is a DECLARATION
about the lease, not a kernel enforcement; nothing in the chain prevents a
contaminated target from changing its group, and this packet does not claim
otherwise.
```

---

## §4. Option W-A — watchdog requests, PCS executes (repaired)

The watchdog holds **no PID**, and after update EOF sends **one** request on a
dedicated, single-opcode, target-free capability. The PCS executes §3.

### §4.1 Endpoint and slot

```text
The PCS creates, immediately before the SPAWN_WATCHDOG posix_spawn:
    _socketpair(_AF_UNIX, _SOCK_SEQPACKET, 0)
The WATCHDOG file-action vector's explicit (CLOSE, 6) is REMOVED and replaced
by (DUP2, h[6], 6). The watchdog's slot 6 becomes the freeze-request socket.
The PCS retains the other end with FD_CLOEXEC set.

Watchdog slot set becomes {3,4,5,6,7,8,9,10}, identical in shape to
SUPERVISOR and CONTROLLER/WORKER. No other role's slot map changes.
```

**Descriptor leak proof.** The added descriptor is created by `_socketpair`,
whose descriptors CPython creates non-inheritable, so the PCS's retained end
carries `FD_CLOEXEC` and is closed by every later role's `execve` — the §P1-6.4
proof stands with one more member in the "every PCS descriptor other than 3
through 8 has `FD_CLOEXEC` set" set. The watchdog's end reaches slot 6 by `DUP2`,
which clears `FD_CLOEXEC` on the destination, exactly as for slots 3 through 10
today. No controller, worker or supervisor receives it, because file actions are
per-role. The socket is point-to-point, so no third process can join it. The X
line verified this construction as sound.

**`A-5`'s assertion, with the type pinned (closes X's first non-blocking gap).**

```text
A-5 for WATCHDOG asserts /proc/self/fd is exactly {0,1,2} together with
{3,4,5,6,7,8,9,10}, AND additionally that slot 6 satisfies:
  A5W-1  _fstat(6).st_mode is S_ISSOCK
  A5W-2  the descriptor's access mode from _fcntl(_F_GETFL) & _O_ACCMODE is
         _O_RDWR
  A5W-3  its socket type is SOCK_SEQPACKET, read by the same mechanism §P1-7.x
         uses for the supervisor's slot 6, which is already a SOCK_SEQPACKET
         assertion site
Any failure is os._exit(3) with nothing written, exactly as every other A-5
deviation. v1 left slot 6's type unspecified; this closes that gap.
```

**Descriptor accounting (closes X's second non-blocking gap).** The retained PCS
end is a **persistent non-handle PCS descriptor**, the fourth of its kind
alongside `lock_fd`, `sv_sock` and `journal_fd`. §P1-6.5's PCS row requires
`P-f`'s pre-fork enumeration to be exactly `{0,1,2,3,4,5,6,7,8}` plus the
transient listing descriptor. The freeze socket is created **after** `P-f` —
`P-f` is pre-fork and is the PCS's only enumeration (composite `:725-740`) — so `P-f`'s required set is **byte-unchanged**. The new descriptor is
added to §P1-6.4's leak-proof enumeration of `FD_CLOEXEC`-carrying PCS
descriptors and to §P1-6.5's statement of which PCS descriptors persist. No
sweep rule applies to it, because §P1-6.5 forbids PCS enumeration after the
first role handle exists.

### §4.2 Request grammar — constant, one-shot, target-free (closes Y-C2)

```text
WITHDRAWN, v1 §3.2 fields 3 and 5, verbatim:
  "3  request_seq  decimal, 1..6 digits, no leading zero, strictly increasing"
  "5  table_seq    decimal, 1..19 digits — the lease table sequence the
                   watchdog last acked"

WHY: a strictly increasing sequence makes request 2 a FRESH operation, not a
replay, so the channel authorized repeated freezes. And no specified event can
create the PCS record of a published table_seq that v1's binding required:
lease tables are peer-owned and the PCS holds no peer-layer state.
```

The repaired grammar has **four** fields and no variable part other than the
generation:

```text
0  "philosophia.officina.t-wd-freeze.v1"    literal
1  "1"                                       version
2  generation_id                             64 lowercase hex
3  "FREEZE_ALL_LEASED"                       the ONLY opcode token

There is no sequence number, no table sequence, no pid, no pgid, no handle, no
role, no index, no count, and no field of any other kind. A conforming request
is a CONSTANT byte string for a given generation.
```

```text
REQUEST IDENTITY: the constant pair (generation_id, watchdog_handle_id), where
  watchdog_handle_id is the PCS's own handle id for the live watchdog. The
  watchdog does not send it and cannot name it; the PCS supplies it from its
  own handle table. The journal key is
      (generation_id, "WDFREEZE", watchdog_handle_id)
  and it is CONSTANT for the life of a watchdog handle.

EXACTLY ONE ACCEPTED ACTION: at most one record per (generation_id,
  watchdog_handle_id) is ever ACCEPTED. Every subsequent record on the socket —
  duplicate, replay, malformed, wrong generation, wrong opcode, or arriving
  after the terminal — is REFUSED or REPLAYED and PERFORMS NO SYSCALL, appends
  no ACCEPTED entry, and changes no handle state.

A REPLACEMENT WATCHDOG gets a new handle id and therefore a new constant key,
  which is correct: it is a different sensor in the same generation, and the
  first watchdog's action, if any, is already durable and is not repeated.
  The PCS additionally refuses any second ACCEPTED action in a generation
  regardless of handle id, by the generation-terminal rule of §4.5 T-4.
```

### §4.3 The PCS-side gate — invocation before endpoint loss is **forbidden**

Y-C2 requires either a mechanically verifiable gate or explicit pricing. **v2
gives the gate, and states the pricing anyway.**

```text
G-1  A t-wd-freeze.v1 record is ACCEPTED only if, at the instant of receipt,
     the PCS has ALREADY recorded PEER_CONTROL_ENDPOINT_LOST for this
     generation on its own protocol socket (§5.2 defines that event, and it is
     shared by both options).
G-2  A record received while the peer control endpoint is still live is
     REFUSED with detail PEER_ENDPOINT_LIVE. No syscall is performed, no
     ACCEPTED entry is appended, and no handle state changes. Only the
     rejection is recorded.
G-3  THE GATE IS A PCS-SIDE FACT. It is the PCS's own observation on its own
     descriptor. It is not a watchdog assertion, not a supervisor report, and
     not derived from any peer artifact. It is therefore mechanically
     verifiable: a fixture that sends a well-formed request on a live
     generation must observe REFUSED / PEER_ENDPOINT_LIVE and zero signals.
G-4  Watchdog prose is not a gate. v1's "the watchdog waits for update-pipe
     EOF" constrained only a conforming watchdog and is NOT relied on here.
```

### §4.4 Reply, ack, timeout, replay

```text
REPLY, one SOCK_SEQPACKET record per received record:
  0  "philosophia.officina.t-wd-freeze.v1"
  1  "1"
  2  generation_id  echoed
  3  status         OK | REFUSED | INVALID | REPLAYED
  4  detail         one token of §P1-2.6, extended with PEER_ENDPOINT_LIVE
  5  terminal       FREEZE_TOTAL_PROVED | FREEZE_INCOMPLETE |
                    FREEZE_NOT_ATTEMPTED | "-"
  6  groups_attempted   decimal count, or "-"
  7  groups_proved      decimal count, or "-"
  NO pid, NO pgid, NO handle_id, NO path, NO freeze_ns. The reply is a P1
  receipt, not evidence, and §8's L8 forbids it from ever becoming evidence.

ACK: none. The reply IS the ack; SOCK_SEQPACKET delivers one record or nothing
  (composite :1169-1173).

TIMEOUT: the watchdog waits at most T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS
  (60_000_000_000) for the reply, polling at T_SUPERVISOR_POLL_INTERVAL_NS.
  On expiry it writes nothing and exits. It NEVER sends a second record,
  and even if a compromised watchdog did, §4.2 makes it a no-syscall replay.

REPLAY: the PCS journals ACCEPTED before acting (§4.6). A later record whose
  key is already journalled returns the recorded reply with status REPLAYED and
  performs NO syscall — identical in shape to the J1-J6 rule of §P1-8.6.
```

### §4.5 Ordering against endpoint loss and the non-returning reaper (closes Y-M3)

The signed architecture already has the PCS, on `PEER_EOF` of `t-pcs.v1`, "hold
every live handle in the carried non-returning reaper state rather than
abandoning any, and … not free the singleton"
(`…V2_1_10_4_P1_BINDING.md:629-632`; composite `:1888`). v1 gave W-A a dispatch
path but never ordered it against that transition. v2 orders it:

```text
T-1  On PEER_CONTROL_ENDPOINT_LOST the PCS records the event, stops accepting
     t-pcs.v1 requests (there is no peer to send one), and ENTERS A BOUNDED
     W-A SERVICE WINDOW before the non-returning reaper transition.
T-2  THE WINDOW: from the endpoint-loss instant, at most
     T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS (60 s), polling the watchdog socket at
     T_SUPERVISOR_POLL_INTERVAL_NS. During the window the PCS services EXACTLY
     the watchdog socket and no other descriptor. No handle is created,
     released or reaped during the window, so §3.5 SC-4's "no handle can be
     created after the trigger" holds.
T-3  THE WINDOW ENDS, deterministically, on the FIRST of:
       (a) one record ACCEPTED and its classifier terminal appended  ⇒ done
       (b) the watchdog socket returns EOF (the watchdog exited)     ⇒ no freeze
       (c) the watchdog handle is proved dead by REAP_ROLE's
           REAPED_POSITIVE                                            ⇒ no freeze
       (d) the 60 s bound expires                                     ⇒ no freeze
     In (b), (c) and (d) the PCS appends a terminal record naming the reason
     and PERFORMS NO FREEZE. No freeze is ever INFERRED from the window's end.
T-4  AFTER THE WINDOW the PCS enters the non-returning reaper state of
     §P1-11.4 and §P1B.8.1 and services the watchdog socket NO FURTHER. A
     record arriving after the window is REFUSED with GENERATION_TERMINAL, no
     syscall. The non-returning transition can therefore never "win first": it
     is defined to happen after the window, not concurrently with it.
T-5  STALE GENERATION: field 2 not equal to the PCS's current generation_id is
     INVALID with WRONG_GENERATION, no action, no state destroyed, at any point
     inside or outside the window.
T-6  PCS RESTART: a new PCS started against a non-terminal generation responds
     GENERATION_NOT_ADOPTABLE, acts on nothing, and exits (composite
     :1774-1777). It never services the watchdog socket, never adopts, and
     never repeats an ACCEPTED action.
T-7  SIMULTANEOUS ENDPOINT LOSS AND WATCHDOG DEATH: T-3(b)/(c) fire, the window
     ends, no freeze occurs, and the generation settles invalid. This is the
     W-A liveness residual and it is priced at §9.3.
```

### §4.6 Journal, and the explicit price of the one authorized action

```text
JOURNAL KEY: (generation_id, "WDFREEZE", watchdog_handle_id) — constant, in the
  autonomous keyspace, disjoint from (generation_id, request_id) of §P1-8.6 by
  its middle member, so no collision is expressible.

ORDER, record-first:
  A1. receive one record; validate the four fields; evaluate the G-1 gate
  A2. append { key, state: ACCEPTED } and fsync
  A3. run the §3 classifier
  A4. append { key, state: COMPLETED, terminal, per-group tokens } and fsync
      ONLY IF the terminal is FREEZE_TOTAL_PROVED
      OTHERWISE append { key, state: TERMINAL_INVALID, terminal, per-group
      tokens } and fsync
  A5. send the reply
  There is no A6: the reply is the terminus and no descriptor is transferred.
```

**The price, stated explicitly as Y-C2 requires.**

```text
P-1  THE ONE AUTHORIZED ACTION FORCES WHOLE-GENERATION PROCESS INVALIDITY WITH
     FULL CHARGE. Whatever its terminal, the freeze stops the leased trees, the
     peer witness is ABSENT, and §N5.3's route is record-first live-process
     invalidity with full §4c charging. There is no branch in which the action
     yields a completion or a resource success (§3.9 S-1).
P-2  UNDER THE G-1 GATE THE MARGINAL PRICE IS ZERO. The action is reachable
     only after PEER_CONTROL_ENDPOINT_LOST, at which point the generation has
     no valid continuation and is already headed to invalidity. A compromised
     watchdog therefore cannot force invalidity of a HEALTHY generation, which
     is exactly the channel Y-C2 identified and G-1 closes.
P-3  WITHOUT THE GATE THE PRICE WOULD BE REAL: a compromised watchdog could
     force invalidity and full charge on a live, healthy generation. v2 states
     this so that a reviewer who rejects G-1 knows exactly what W-A then costs.
P-4  WHAT REMAINS EVEN WITH THE GATE: a compromised watchdog can send nothing,
     which denies the freeze entirely (T-3(d)). That is a liveness denial, is
     non-citable under L1-L5 and L7, and is the W-A residual of §9.3.
```

### §4.7 Amendment to "the watchdog holds no capability"

**This is a real weakening and W-A does not present it otherwise.**

```text
SIGNED TODAY (v1.2 §P1-9.2 properties 1, 2, 6, composite :1440-1446):
  "it holds no lock of any kind"; "it holds no capability object";
  "it communicates only over its two sealed pipes at slots 3 and 4"

PROPOSED UNDER W-A:
  "it holds no lock of any kind; it holds no capability object other than a
   single-opcode, target-free freeze-request socket at slot 6, which can
   express exactly one constant request naming no target, is gated on a
   PCS-side endpoint-loss fact it cannot influence, is accepted at most once
   per generation, and can reach no other operation; it communicates only over
   its three sealed endpoints at slots 3, 4 and 6."

TOKEN: P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1
```

**Does the watchdog remain the dedicated freezer in the meaningful sense?**
Partly, and v2 is explicit about which part. It remains the process that
**initiates**. It ceases to be the process that **executes** the stop, and it
ceases to be the **witness of record**, since it writes no observation. C1's
"the watchdog … writes their observations" is **not** retained under W-A. §7
enumerates every sentence this touches.

---

## §5. Option W-B — the PCS freezes on peer-control-endpoint loss (repaired)

The PCS detects loss of its own peer control endpoint and executes §3 itself.
The watchdog becomes a pure liveness sensor.

### §5.1 Topology — unchanged

**W-B adds no descriptor, no socket, no slot and no opcode.** The watchdog's
slot set stays `{3,4,5,7,8,9,10}` with slot 6 explicitly closed. §P1-6.2,
§P1-6.4's leak proof and `A-5`'s assertion are **byte-unchanged**. This is W-B's
principal structural property and it survived both reviews intact.

### §5.2 The trigger is endpoint loss, not death (closes X F2 / Y-M1)

```text
WITHDRAWN, v1 §4.2, verbatim:
  "The supervisor's end was closed by the kernel at its exit, so this is a
   kernel fact, not a report."
  "The two EOFs are the same kernel event observed on two descriptors."
  and the state name SUPERVISOR_LOST.

WHY: a zero-length SOCK_SEQPACKET receive arises from at least four distinct
causes, three of which do not involve the supervisor dying, and the protocol
socket and the update pipe are two independent descriptors that can be lost
independently and in either order.
```

**The repaired event.**

```text
E-1. THE OBSERVATION. r := the PCS's _recvmsg on the protocol socket.
     r[0] is the data, r[2] is msg_flags.

     E-1a  len(r[0]) == 0  AND  (r[2] & _MSG_EOR) == 0
             ⇒ PEER_CONTROL_ENDPOINT_LOST. This is end-of-stream.
     E-1b  len(r[0]) == 0  AND  (r[2] & _MSG_EOR) != 0
             ⇒ A GENUINE EMPTY DATA RECORD, which the grammar forbids.
               This is REQUEST_MALFORMED, classified as TRANSPORT_STRUCTURAL,
               routed to §P1-11.6. IT IS NOT ENDPOINT LOSS and it never fires
               the freeze.
     E-1c  len(r[0]) > 0   ⇒ an ordinary record; the nine opcodes apply.

     _MSG_EOR must be added to the PCS's pinned integer-constant set
     (§P1-3.4, composite :419-423, which today pins _MSG_CMSG_CLOEXEC,
     _MSG_CTRUNC and _MSG_TRUNC but NOT _MSG_EOR). That one-name extension of
     the binding block, checked by the existing S-3 and S-5 rules, is disclosed
     in W-B's blast radius at §9. Without it E-1a and E-1b are not
     distinguishable, which is exactly X F2's mechanical point.

E-2. WHAT IT PROVES, AND WHAT IT DOES NOT.
     PEER_CONTROL_ENDPOINT_LOST proves EXACTLY ONE THING: the supervisor's
     write end of the protocol socket is no longer open, so NO FURTHER
     AUTHORIZED PEER REQUEST CAN ARRIVE ON THIS GENERATION.
     IT DOES NOT PROVE THAT THE SUPERVISOR PROCESS DIED.
     These four causes are INDISTINGUISHABLE at this interface, and v2 asserts
     no way to tell them apart:
       (a) supervisor exit — the kernel closed the end;
       (b) supervisor crash — likewise;
       (c) orderly close() of the socket by a live supervisor;
       (d) half-close, shutdown(SHUT_WR), by a live supervisor.
     All four route IDENTICALLY (§5.3), which is why the conflation is
     fail-safe rather than unsafe. The X line reached the same conclusion.

E-3. THE STATE NAME. The generation is marked PEER_CONTROL_ENDPOINT_LOST.
     The name SUPERVISOR_LOST is withdrawn and appears nowhere in v2, because
     it asserts a fact the observation does not establish.

E-4. THE TWO EOFs ARE TWO EVENTS. The PCS's protocol-socket loss and the
     watchdog's update-pipe EOF are observations on two independent
     descriptors. Either can occur without the other, in either order: a
     supervisor can close the protocol socket while holding the update write
     end, or close the update write end while holding the socket. v2 asserts NO
     ordering, NO simultaneity, and NO causal identity between them. W-B does
     not depend on the watchdog's observation at any step, which is why no race
     between them exists — but the reason is INDEPENDENCE, not identity.
```

### §5.3 The single continuation for all four causes

```text
Whichever of (a)-(d) occurred:
  1. record PEER_CONTROL_ENDPOINT_LOST for the generation;
  2. accept no further t-pcs.v1 request; a later record on that socket, if the
     kernel delivers one at all, is REFUSED with GENERATION_TERMINAL;
  3. run the record-first sequence of §5.5;
  4. hold every live handle in the non-returning reaper state of §P1-11.4 and
     §P1B.8.1 and free the singleton for no one;
  5. the generation settles as PROCESS invalidity with full charge (§3.9 S-1),
     through the ABSENT witness route of §6.

INDEPENDENTLY, and with NO ordering relation to the above:
  W-1. The watchdog observes update-pipe EOF on its own descriptor.
  W-2. It writes NO freeze observation, because it can prove nothing: it has no
       numeric identity, no signal authority and no channel to the PCS.
  W-3. It exits. The PCS reaps it on the next REAP_ROLE, or its adopter does.
```

### §5.4 Which process establishes what

| Fact | Established by | How | Not established |
|---|---|---|---|
| no further authorized peer request can arrive | **PCS** | `PEER_CONTROL_ENDPOINT_LOST` on its own socket end | **that the supervisor died** |
| the watchdog's own channel to the supervisor is gone | **watchdog** | EOF on its own update read end | that the supervisor died; that the protocol socket is also gone |
| each in-scope group is stopped or dead | **PCS** | its own `_killpg` plus §3's quiescence passes over its own `/proc` enumeration | anything about groups it could not verify (§3.10) |
| the freeze instant, when proved | **PCS** | `freeze_ns` sampled on the proving pass | that this instant is peer evidence — it is not (§8 `L8`) |
| the generation is invalid | the peer layer at the next takeover | from the `ABSENT` witness, per §6 | — |

**No fact is established by a process lacking the authority to establish it**,
and **no fact is claimed beyond what its observation supports** — which is the
property v1 violated in its death language.

### §5.5 Record before act (closes Y-M2)

```text
WITHDRAWN, v1 §4.2 ordering: E-3 executed the whole freeze and E-4 then
appended the SOLE journal entry. A live PCS receiving a denied or structural
signal result, or an enumeration exception, after some groups were already
stopped, left NO durable marker that an autonomous operation had begun.
```

```text
REPAIRED ORDERING, using the already-selected B1 discipline:

  R1. VALIDATE the endpoint-loss event per §5.2 E-1a. An E-1b empty record is
      NOT this event and takes the malformed route instead.
  R2. Read the journal head. If the constant key (generation_id, "PEEREOF", 1)
      is ALREADY PRESENT in any state:
        ACCEPTED          ⇒ INCONCLUSIVE: perform NO second freeze, no syscall;
                            whole-generation PROCESS invalidity
        COMPLETED         ⇒ redeliver nothing (there is no peer to reply to);
                            perform NO syscall; the recorded terminal stands
        TERMINAL_INVALID  ⇒ as COMPLETED; no syscall
      This is the stale-head/state check, and it is evaluated BEFORE any
      side effect.
  R3. APPEND { (generation_id,"PEEREOF",1), state: ACCEPTED } and FSYNC.
      The key is CONSTANT within the generation, so the entry is naturally
      singular and no second ACCEPTED is expressible.
  R4. RUN the §3 classifier, in full, to one of its three terminals.
  R5. APPEND and FSYNC:
        terminal == FREEZE_TOTAL_PROVED ⇒ { …, state: COMPLETED, terminal,
                                            per-group tokens }
        otherwise                        ⇒ { …, state: TERMINAL_INVALID,
                                            terminal, per-group tokens }
      COMPLETED IS APPENDED ONLY ON THE EXACT VALID TERMINAL.
  R6. Enter the non-returning reaper state (§5.3 step 4).

REPLAY: there is no requester and therefore no reply. "Replay" here means a
  restart or a re-entry that re-reads the journal; R2 is the whole replay rule
  and it performs no syscall in any branch.

PARTIAL SIDE EFFECTS: if the classifier stops mid-run for any reason, the
  groups already signalled STAY signalled. Nothing un-stops them. The entry
  remains ACCEPTED, which R2 classifies as INCONCLUSIVE on any later read, and
  §3.9 S-3 routes it to whole-generation PROCESS invalidity with invalidity
  dominant. A partial freeze is NEVER a completion and NEVER a valid terminal.
```

### §5.6 The deterministic failure and crash matrix

| Cut / failure | Last durable marker | Freeze state | Single continuation |
|---|---|---|---|
| PCS dies before `R1` | none | none | no freeze; whole-generation invalidity; leased roles orphaned and still running (`L7`) |
| PCS dies between `R1` and `R3` fsync | none | none | as above; nothing journalled; a restart sees no key and may not adopt (`GENERATION_NOT_ADOPTABLE`) |
| PCS dies after `R3` fsync, before any signal | `ACCEPTED` | none | inconclusive ⇒ PROCESS invalidity; a restart may not adopt and performs no freeze |
| PCS dies mid-`R4`, some groups stopped | `ACCEPTED` | partial | inconclusive ⇒ PROCESS invalidity; the partial stop stands and is never undone |
| live failure mid-`R4` (denied / structural / enum exception) | `ACCEPTED` | partial | the classifier completes over the remaining groups, then `R5` appends `TERMINAL_INVALID`; PROCESS invalidity |
| PCS dies after `R5` | `COMPLETED` or `TERMINAL_INVALID` | as recorded | the generation is still invalid; no adoption; the record is a P1 fact only (`L8`) |
| PCS restart against a non-terminal generation | any | any | `GENERATION_NOT_ADOPTABLE`, acts on nothing, exits (composite `:1774-1777`) |
| endpoint loss observed twice | `ACCEPTED`+ | any | `R2` returns without a syscall |
| `E-1b` empty record with `MSG_EOR` | none | none | `REQUEST_MALFORMED` ⇒ `TRANSPORT_STRUCTURAL` ⇒ §P1-11.6; **no freeze** |
| stale generation on any received record | any | any | `WRONG_GENERATION`; no action; no state destroyed |
| watchdog dies before, during or after any of it | — | — | **no effect** — W-B depends on the watchdog at no step |
| watchdog does not exit after its update-pipe EOF | — | — | `WATCHDOG_UNREAPED`; no signal; §P1-11.6 (unchanged) |
| PCS and supervisor lost together | none | none | no freeze; invalidity; `L7` |
| target escaped its group (§3.10) | `ACCEPTED` | partial | `TERMINAL_INVALID` with `GROUP_CHANGED`; the escaped tree keeps running; `L7`/`L9` |

### §5.7 The one genuinely new thing in W-B, named

**The PCS acts without a request.** Today every PCS action is request-driven.
`R4` is the first autonomous PCS side effect in this architecture. It is bounded
by construction: triggered by exactly one PCS-side descriptor fact, operating on
exactly the §3 scope computed from the PCS's own handle table, at most once per
generation by a constant journal key, record-first, and not inducible by any
request. But it is new initiative and a reviewer should weigh it as such.

**What the signed chain already had.** §P1B.8.1 (`…P1_BINDING.md:629-632`) and
composite `:1888` already have the PCS observe protocol peer loss and hold every
live handle in the non-returning reaper state. W-B adds the freeze **action** at
a detection point the architecture already has; it does not add the detection.
The X line verified this.

### §5.8 Amendment to C1

```text
SIGNED TODAY — see §7 for the COMPLETE list of twelve sentences. The two most
often quoted are v1.2 §P1-9.2 properties 7 and 12 (composite :1446-1451, :1464):
  the watchdog "physically emits freeze observations"; "on observing
  update-pipe EOF it freezes the groups it knows, writes their observations,
  and exits"

PROPOSED UNDER W-B:
  "The watchdog is the dedicated supervisor-channel-liveness sensor. It
   observes update-pipe EOF and exits, writing nothing. It neither executes nor
   witnesses a freeze; the PCS executes the freeze on its own
   PEER_CONTROL_ENDPOINT_LOST and records it in the process-control journal,
   which is a P1 fact and never peer evidence; and the absent peer witness
   routes through the ABSENT-sentinel fallback as amended by §6."

TOKEN: P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1
```

C1's "dedicated" and "holds no lock, no capability, no `runtime/` write, no
ledger append, settles nothing" survive **strengthened** — the watchdog holds
strictly less than before. What is lost is its *freezer* and *witness* role.

---

## §6. The common `ABSENT` amendment (closes Y-C3 and X F3)

### §6.1 The withdrawn claim

```text
WITHDRAWN, v1 §4.5, verbatim:
  "W-B invents no settlement route. It routes an absent witness exactly where
   the signed chain already routes one."
and v1 §5.3's four-way "compatible; no interaction" table, insofar as it
asserted that the ABSENT route is CONSTRUCTIBLE under both identity outcomes.

WHY IT IS FALSE. The route terminates in a supervisor-written
t-freeze-fallback-observation.v1 whose key set (§N5.2,
…V2_1_2_CORRECTION.md:855-869) is:
  schema, scientific_outcome, supervisor_generation_sha256,
  fallback_witness_id, process_id, pgid, start_identity, deadline_ns,
  table_seq, rejected_witness_path_or_null, rejected_object_sha256_or_null,
  rejection_conjunct, unknown_reason, current_unresolved_member_count,
  supervisor_quiescence, killer, created_utc
`pgid` and `start_identity` carry NO `_or_null` suffix, unlike the sibling
`rejected_witness_path_or_null` in the same key list — so the suffix convention
is deliberate and these two fields are MANDATORY AND NON-NULL. The ABSENT
sentinel nulls only the rejected path and the rejected object hash
(:849-851). A P1 supervisor "holds opaque handles and cannot express a PID"
(composite :1480), and peer numeric-identity install is itself blocked until
the identity cell is signed (composite :2363). So on the ABSENT branch there is
no rejected witness to read the numbers from and no authorized way to obtain
them.
```

Both lines found this. X asked for a framing repair; **Y asked for a
constructive one, and §0.2 D-1 takes Y.**

### §6.2 The amendment, exactly

```text
AMENDMENT A-ABS, to philosophia.officina.t-freeze-fallback-observation.v1 and
to §N5's predicates. It is BOUNDED to the rejection_conjunct == 0 branch and
changes nothing on any other branch.

A-ABS-1  Rename and re-type two keys:
             pgid            ->  pgid_or_null
             start_identity  ->  start_identity_or_null
         Both are null IF AND ONLY IF rejection_conjunct == 0 (the ABSENT
         sentinel). On every other value of rejection_conjunct, 1..10, both
         remain mandatory non-null integers exactly as today. The biconditional
         is a validity conjunct, not a convention: a record with
         rejection_conjunct == 0 and a non-null pgid_or_null is INVALID, and so
         is a record with rejection_conjunct != 0 and a null one.

A-ABS-2  Rename and re-type one further key, for the same reason:
             current_unresolved_member_count
                             ->  current_unresolved_member_count_or_null
         null IF AND ONLY IF rejection_conjunct == 0.
         DERIVATION: the count is the number of unresolved members of a group
         the writer must enumerate. With pgid_or_null null the group cannot be
         named, so no integer is computable and any integer written would be a
         fabrication. THIS ELEMENT GOES BEYOND THE LITERAL TEXT OF Y-C3 AND IS
         AUTHOR-ADDED; it is stated here rather than left as an unconstructible
         field, per the stricter-rule discipline of §0.2.

A-ABS-3  On the rejection_conjunct == 0 branch, supervisor_quiescence is
         forced to UNKNOWN.
         DERIVATION: §Z4.6 conjunct 10 makes PROVED mean "the supervisor
         independently proves the group quiescent NOW". Proving a group
         quiescent requires naming it. With pgid_or_null null it cannot be
         named, so PROVED is not establishable and UNKNOWN is the only
         truthful value.

A-ABS-4  On that branch unknown_reason is EVIDENCE_ABSENT, and NOTHING IS
         SYNTHESIZED: no freeze instant, no overrun_ns, no numeric identity, no
         member count, no quiescence proof, and no freeze-success claim. There
         is no branch of the fallback that can express "the freeze succeeded".

A-ABS-5  ROUTING IS UNCHANGED. §N5.3's route stands verbatim: record-first
         live-process invalidity, the all-live batch, the §4c(c)/§4d unknowable
         pool, public cause PROCESS, and full §4c charging. No fallback can
         select a valid terminal, a zero-overrun branch, a synthesized freeze
         instant, or an overrun_ns (…V2_1_2_CORRECTION.md:876-886).

A-ABS-6  The fallback remains a SUPERVISOR runtime-authority fact, written only
         by the supervisor under T_RUNTIME.lock, in a namespace the watchdog
         has no path to and never writes (:882-886). Neither option changes
         that, and no P1 root gains an install site for a peer artifact.
```

### §6.3 The exact signed sentences reopened

| Contract sentence | Locus | What A-ABS does to it |
|---|---|---|
| the fallback key list naming `pgid`, `start_identity`, `current_unresolved_member_count` | `…V2_1_2_CORRECTION.md:859-866` | three keys renamed and made conditionally nullable |
| "`rejection_conjunct` (int 0..10; 0 == the `ABSENT` sentinel …)" | `:862-863` | unchanged in meaning; becomes the discriminant of the three biconditionals |
| "`supervisor_quiescence ∈ {PROVED, UNKNOWN}`" | `:867` | unchanged as a type; constrained to `UNKNOWN` on the `0` branch only |
| §N5.4's "`unknown_reason = FREEZE_INSTANT_UNKNOWN` with `current_unresolved_member_count = 0` and `supervisor_quiescence = PROVED` is legal and expected" | `:905-909` | **unchanged** — it is about the `FREEZE_INSTANT_UNKNOWN` branch, which is `rejection_conjunct != 0`; A-ABS does not touch it |
| §N5.1's "`rejected_object_sha256_or_null` … null ONLY for the `ABSENT` sentinel" | `:839`, `:849-851` | **unchanged** |
| §N5.3's routing paragraph | `:876-886` | **unchanged** — `A-ABS-5` restates it, amends nothing |
| §N5.5's production / duplicate / conflict / consumption order | `:912-930` | **unchanged**; the `fallback_witness_id` preimage (`:833-840`) does not contain any of the three amended keys, so ids are stable |
| §Z4.6 conjunct 10 (supervisor proves quiescence now) | `…V2_1_1_CORRECTION.md:1056` | **unchanged**; `A-ABS-3` derives from it rather than amending it |

**Exactly one contract file's schema is reopened, in exactly three keys, on
exactly one branch.** No routing, no id preimage, no consumption order and no
§Z4.6 conjunct changes.

### §6.4 The common token

```text
P1_FREEZE_ABSENT_FALLBACK_NULLABLE_IDENTITY_V1

REQUIRED UNDER EITHER W-A OR W-B. It is not a per-option token: both options
leave the peer witness ABSENT, so both need the fallback to be constructible.
Selecting W-A or W-B without this token leaves a settlement path that cannot be
written, which is the same class of defect as the blocker this packet exists to
repair.
```

### §6.5 What this does and does not do to the identity cell

```text
DOES  It makes the ABSENT settlement constructible WITHOUT any numeric process
      identity, under EITHER outcome of
      AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS. Under identity Option A the
      numbers would exist in the claim but are STILL not written into the
      fallback on the ABSENT branch, because there is no rejected witness to
      bind them to and A-ABS-1 forbids them. Under identity Option B the
      numbers are behind a P1 binding and the fallback does not need them.
      The four-way coexistence table of §9.5 is therefore EARNED rather than
      asserted.

DOES NOT  It does not select, repair, prejudge or constrain the identity cell.
      It does not grant any cross-layer read. It does not make a watchdog-written
      numeric witness constructible. It creates no numeric identity anywhere.

SEPARATION, STATED EXACTLY  Who may EXECUTE the freeze is decided by this cell
      and by nothing in the identity cell: the blocker is S-12, the sole-caller
      sentence, the missing endpoint and the missing relay, none of which is a
      numeric-identity question. What the SETTLEMENT looks like afterwards is
      the fallback representation, and THAT is what Y-C3 found entangled. A-ABS
      disentangles it. So: the freeze-executor choice is separate from the
      identity choice, AND this repaired fallback is what makes settlement
      constructible under either identity outcome.
```

### §6.6 X's framing point, also stated

X F3's narrower reading is recorded because it is true and a reviewer should see
both: "independent of the identity cell" always meant "adds no new dependency",
and the operability of the fallback under P1 was a **pre-existing** peer-layer
item that neither option created and neither option differentiated. **v2 does
not stop there**, because a pre-existing defect on the load-bearing settlement
path of both options is still a defect this packet must not ship over.

---

## §7. The complete freezer / witness sentence audit (closes X F1)

### §7.1 The withdrawn comparison

```text
WITHDRAWN, v1 §5.1, §6, and the v1 closure §6, verbatim:
  "P1 sentences amended: ... W-B: none"
  "W-B amends ZERO P1 sentences"

WHY IT IS FALSE: the sentences below are physically P1-composite sentences.
The claim was defensible only under an unstated taxonomy that re-bucketed every
freezer/witness sentence as "C1". v2 uses the honest distinction instead:

  TOPOLOGY / OPCODE CHANGES   descriptors, slots, file actions, grammars,
                              dispatch paths, leak proofs, A-5 assertions
  NORMATIVE P1 PROSE CHANGES  sentences, invariants and table rows in the
                              composite that assign a role or an obligation

W-B makes ZERO TOPOLOGY / OPCODE CHANGES. W-A makes several.
BOTH make the SAME TWELVE NORMATIVE P1 PROSE CHANGES.
```

### §7.2 The complete audit — twelve sites

Every sentence, invariant and table row in composite v1.2 that assigns the
watchdog the **freezer** or the **witness-of-record** role. Sites 1–7 and 11–12
were named by the X line; sites 8, 9 and 10 were found by re-auditing the whole
composite for this repair and were **not** in either review.

| # | Site | Line(s) | The sentence that becomes false |
|---|---|---|---|
| 1 | C1 intro statement | `202` | "A dedicated watchdog process **witnesses and freezes**." |
| 2 | §P1-9.2 property 7 | `1447-1451` | it "**physically emits freeze observations** under its own witness identifier, in the record class of §P1-13.2 row 4" |
| 3 | §P1-9.2 property 12 | `1464-1465` | "on observing update-pipe EOF it **freezes the groups it knows, writes their observations**, and exits" |
| 4 | §P1-9.2 Termination ¶ | `1469-1470` | "the watchdog observes EOF, **writes its final observations** and exits" |
| 5 | §P1-9.4 `S-4` | `1490` | "the watchdog observes EOF, **writes its final observations**, `os._exit(0)`" |
| 6 | §P1-11.4 continuation step 3 | `1783-1784` | "the watchdog **writes its observations for the groups it knows** and exits" |
| 7 | §P1-11.7 crash matrix row | `1888` | "the watchdog sees update-pipe EOF **and freezes, observes and exits**" |
| 8 | §P1-13.1 process/layer table, watchdog row | `2006` | watchdog runs "**generic-harness peer witness code**"; "it **physically emits a peer-owned record**" |
| 9 | §P1-13.2 row 4, executing process | `2249-2253` | "**EITHER the watchdog role process, normally**, OR the supervisor role process, on the signed dead-watchdog route" |
| 10 | §P1-13.7 single-writer table, freeze row | `2367` | the freeze-witness function is "**called from the watchdog role entry** and from the supervisor's dead-watchdog route" |
| 11 | Invariant 61 | `2730` | "supervisor death produces update-pipe EOF **and the freeze, observe and exit route**" |
| 12 | Invariant 63 | `2732` | "every one of the **thirteen** watchdog properties of §P1-9.2 holds in a live generation" — properties 7 and 12 are two of the thirteen |

**Two further sites are checked and confirmed NOT to need amendment:**

```text
Invariant 60 (:2729) "the watchdog never uses getppid(); a PCS-death fixture
  with the supervisor alive produces no freeze" — TRUE UNDER BOTH OPTIONS and
  strengthened: under W-B the watchdog never freezes at all, and under W-A the
  G-1 gate is keyed on the PCS's endpoint loss, not on PCS death.
Invariant 65 (:2734) "PCS death: ... freeze unavailable ..." — TRUE UNDER BOTH
  OPTIONS, unchanged: PCS death still means no freeze.
§P1-13.2 row 4's SCHEMA, logical writer, and killer discriminator — UNCHANGED:
  the record class still exists and the supervisor's dead-watchdog branch is
  untouched. Only the "EITHER the watchdog, normally" clause changes.
```

### §7.3 Exact replacements — **identical for W-A and W-B** except where noted

```text
R1  line 202:
    "A dedicated watchdog process witnesses the supervisor control channel and
     signals its loss. The PCS executes every freeze."
    W-A VARIANT: "... signals its loss, and requests the freeze the PCS
     executes."

R2  §P1-9.2 property 7:
    "it emits NO freeze observation and writes no record of any class. The
     freeze-witness record class of §P1-13.2 row 4 is written only by the
     supervisor, on the signed dead-watchdog route and on the ABSENT fallback
     route of §N5 as amended."

R3  §P1-9.2 property 12:
    W-B: "on observing update-pipe EOF it writes nothing, freezes nothing, and
     exits, settling nothing."
    W-A: "on observing update-pipe EOF it sends exactly one constant
     t-wd-freeze.v1 record on slot 6, waits at most
     T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS for one reply record, writes nothing,
     and exits, settling nothing."

R4  §P1-9.2 Termination ¶:
    "the watchdog observes EOF, writes nothing, and exits"

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

R9  §P1-13.2 row 4 executing process:
    "the supervisor role process, on the signed dead-watchdog route and on the
     §N5 ABSENT-fallback route. The watchdog executes no write of this class."

R10 §P1-13.7 freeze row:
    "write a freeze observation | ... **one** freeze-witness function, called
     from the supervisor's dead-watchdog route only, setting killer from its
     caller | peer | install, no-replace"

R11 Invariant 61 — REPLACE:
    W-B: "loss of the peer control endpoint produces the PCS's record-first
     §3 classifier and its terminal; supervisor death additionally produces
     update-pipe EOF and the watchdog's write-nothing exit route"
    W-A: "... produces the PCS's bounded service window; an ACCEPTED
     t-wd-freeze.v1 record produces the record-first §3 classifier and its
     terminal; window end without one produces no freeze"

R12 Invariant 63 — the thirteen properties remain thirteen; properties 7 and 12
    are the amended texts R2 and R3. The invariant's WORDING is unchanged; its
    CONTENT changes because two of the thirteen changed.
```

### §7.4 Why this does not shift the comparison

Both options demote the identical executor/witness role and therefore amend the
identical twelve sites, with wording differences only at sites 1, 3, 7, 8 and 11.
**F1 falls equally on both**, exactly as the X line concluded. What it changes is
the honesty of the headline: v2 says "W-B makes zero topology and opcode changes
and twelve normative prose changes; W-A makes the same twelve plus a topology
change, a grammar, a dispatch path and a gate."

---

## §8. Publication and scientific boundary (closes Y-m1)

The `L1`–`L5` non-guarantee list at §P1-12.2 (composite `:1920-1929`) gains four
entries, **required under either option**:

```text
L6. That a freeze occurs, or that freeze evidence becomes available, after the
    peer control endpoint is lost. No route guarantees either, and their absence
    settles through the signed UNKNOWN invalid route with no synthesized
    instant.

L7. That loss of the peer control endpoint is proof that the supervisor process
    died. It proves only that no further authorized peer request can arrive.
    Orderly close, half-close, crash and exit are indistinguishable at that
    interface, and this contract asserts no way to tell them apart. Whether the
    freeze in fact occurred, and over which groups, may remain permanently
    unknown.

L8. That any process-control journal fact is peer freeze evidence. The journal
    is P1-owned. A COMPLETED freeze entry, its terminal, its per-group tokens
    and its freeze_ns are P1 facts and are NEVER a t-freeze-observation.v1,
    never a fallback field, and never an input to any peer validity predicate.

L9. That an ABSENT witness means no freeze happened. ABSENT means the required
    peer evidence is UNAVAILABLE. Some, all, or none of the groups may in fact
    have been stopped, and the record cannot and does not distinguish those
    cases.
```

**The no-distinguishability rule, stated as a closed prohibition:**

```text
ND-1  NO qualification, comparison, Q, C, Proof, capacity observation, custody
      disposition, spend decision, selection, blinding claim or scientific
      datum may DISTINGUISH a generation whose P1 journal records
      FREEZE_TOTAL_PROVED from any other ABSENT case.
ND-2  Every ABSENT case — proved, incomplete, not attempted, inconclusive, or
      never triggered — presents to the peer layer as the SAME input: a missing
      t-freeze-observation.v1, the §6 ABSENT fallback, and §N5.3's record-first
      PROCESS invalidity with the unknowable pool and full charging.
ND-3  Therefore no publication, ledger entry, archive record or downstream
      analysis may read a freeze terminal, and none is exposed to them.
ND-4  Y's correction to the packet's own overclaim is adopted: full charging IS
      a deterministic RESOURCE-ACCOUNTING consequence, and v1's statement that
      the consequence is "never a resource outcome" was too broad. What is true
      is narrower and is what v2 says: it is never a resource SUCCESS, never a
      capacity fact, and never a result-dependent quantity.
```

---

## §9. Comparative audit, corrected

### §9.1 Surface

| | W-A | W-B |
|---|---|---|
| descriptors added | 1 socketpair; watchdog slot 6 reopened | **none** |
| leak proof | re-proved with one more `FD_CLOEXEC` member (§4.1) | **byte-unchanged** |
| `A-5` assertion | extended, with slot-6 type pinned (§4.1) | **byte-unchanged** |
| PCS descriptor accounting | one more persistent non-handle descriptor (§4.1) | **unchanged** |
| opcodes / grammars added | one request, one reply, one dispatch path, one gate | **none** |
| capability surface of the watchdog | one gated single-opcode target-free socket | **strictly reduced** |
| autonomous PCS action | no — but the gate is a PCS-side fact (§9.4) | **yes** — the new thing (§5.7) |
| **topology / opcode P1 changes** | several, above | **zero** |
| **normative P1 prose changes** | **twelve** (§7) | **twelve** (§7) |
| shared classifier changes | §3 in full, incl. `STAT_OBSERVE_G`, `KV`, `pgid_or_null` population, `T_PCS_QUIESCE_MAX_PASSES` | **identical** |
| additional binding-block change | none | `_MSG_EOR` added to the pinned constants (§5.2) |
| peer contracts reopened | **one** — §N5's fallback schema, three keys, one branch (§6) | **one** — identical |
| verifier rules | `S-12` retained; new rules for the one-opcode dispatch, the target-free grammar, and the `G-1` gate | `S-12` retained; one rule that the autonomous path is reachable only from the `E-1a` site |
| tests | endpoint, type, grammar, gate, one-shot, ordering window, scope, classifier, cuts | trigger discrimination, scope, classifier, record-first ordering, each cut, `ABSENT` routing |

### §9.2 Supervisor loss versus PCS death

Identical in both: PCS death is whole-generation invalidity with no adoption
(§P1-11.4, untouched). The difference is peer-endpoint loss — under W-A the
freeze additionally requires a live, unwedged watchdog that sends within 60 s;
under W-B it requires only the PCS.

### §9.3 Residual liveness under A3

```text
W-A residual: the freeze requires a live, unwedged watchdog. Under A3 a
  same-UID actor may SIGSTOP the watchdog, after which the §4.5 window expires
  and no freeze ever occurs. This is a NEW liveness dependency on a process
  whose death is itself one of the conditions C1 exists to handle.
W-B residual: the freeze requires a live PCS. This is NOT new: D1 and §P1-11.4
  already make PCS loss an unrecoverable whole-generation invalidity.
BOTH: §3.10's target-induced group escape; and if the freeze does not occur,
  leased roles keep running as orphans until their adopter or the host reclaims
  them. Infrastructure facts, never scientific or resource outcomes, covered by
  L7 and L9.
```

### §9.4 What the `G-1` gate costs W-A's rationale — stated, not hidden

```text
The gate required by Y-C2 is keyed on the PCS's OWN observation of
PEER_CONTROL_ENDPOINT_LOST. That is precisely W-B's trigger. So under the
repaired W-A the PCS ALREADY KNOWS, by itself, that the freeze is due; the
watchdog's request adds only the decision to proceed and a bounded delay.

THIS IS A REAL ARGUMENT AGAINST W-A AND v2 STATES IT RATHER THAN BURYING IT.
The counter-argument, also stated: under W-A the watchdog remains the process
that DECIDES, which is the part of C1 that binds the freeze to the deadline the
watchdog observed; and a PCS that merely CAN freeze is not the same as a PCS
that freezes unbidden. A reviewer who weighs C1's decider role heavily may
still prefer W-A. The author does not decide this.
```

### §9.5 Coexistence with the identity cell — now earned

With `A-ABS` (§6), the `ABSENT` settlement is constructible with **no** numeric
identity anywhere. Therefore:

| | identity Option A | identity Option B |
|---|---|---|
| W-A | compatible; no interaction | compatible; no interaction |
| W-B | compatible; no interaction | compatible; no interaction |

**This table is now a consequence of `A-ABS-1`, not an assertion.** Without
`A-ABS` it was unproved, exactly as Y-C3 found. The identity cell is neither
selected nor repaired by this packet.

### §9.6 First and replacement watchdog symmetry

| | W-A | W-B |
|---|---|---|
| symmetry | preserved: the replacement receives the same slot-6 socket from the same `SPAWN_WATCHDOG`, with the same constant grammar and the same `G-1` gate; its own constant key is per handle id, and §4.2's generation-terminal rule still permits at most one accepted action per generation | preserved trivially: no watchdog participates in freezing, so first and replacement are indistinguishable |

### §9.7 Counterexample prevented, residual created

| | W-A | W-B |
|---|---|---|
| **prevents** | an implementation that cannot execute its signed C1 obligation at all, and the worse alternative in which an implementer adds `killpg` to `generic_harness.py` and silently fails `S-12` | the same |
| **new residual** | a compromised or stopped watchdog denies the freeze entirely; and the gate makes the watchdog's initiative largely redundant with a fact the PCS already holds (§9.4) | the PCS takes an action no request authorized; a future editor could widen the autonomous path if the reachability rule is not enforced |

---

## §10. Recommendation after repair

On the stated criteria only — **signed-authority fidelity, constructibility,
mechanical testability, liveness, and blast radius** — and predicting no
outcome:

> **W-B remains recommended.**

| Criterion | W-A | W-B |
|---|---|---|
| signed-authority fidelity | amends twelve normative sentences **and** three topology/assertion sites; weakens "holds no capability" | amends the same twelve normative sentences; **zero** topology or opcode changes; strengthens the watchdog's no-capability property |
| constructibility | constructible after §3, §4.2, §4.3, §4.5 and §6 | constructible after §3, §5.2, §5.5 and §6 |
| mechanical testability | new socket, type assertion, grammar, dispatch, gate, one-shot key and ordering window — all new surface | the change is one reachability-constrained path with a PCS-side descriptor trigger and a record-first ordering |
| liveness | fails if the watchdog is dead or wedged — a **new** dependency | works whenever the PCS lives; **no new** dependency |
| blast radius | §3 + §6 + §7 + a topology change + a grammar + a gate | §3 + §6 + §7 + one pinned constant (`_MSG_EOR`) |

**What the repairs changed about the comparison, stated honestly.**

```text
1. W-B's headline is WEAKER than v1 claimed. "Zero P1 sentences" is withdrawn;
   W-B amends twelve normative P1 sentences, exactly as W-A does.
2. BOTH options now reopen a peer contract. v1 said neither did. §6 reopens
   §N5's fallback schema in three keys under a common token.
3. BOTH options now carry §3, which is substantial: a parse extension, a
   kernel-verification rule, a pgid_or_null population rule, a sixteen-token
   classifier and a new count constant. v1 hid all of this behind an
   eight-line SCOPE block that did not work.
4. W-A is BETTER than v1 made it look in one respect — the G-1 gate removes the
   repeatable-early-freeze channel Y-C2 found — and WORSE in another: the same
   gate makes its initiative largely redundant (§9.4).
5. THE ROWS THAT DECIDE DID NOT MOVE. W-B still makes zero topology and opcode
   changes, so §P1-6.2, §P1-6.4 and A-5 stand byte-unchanged; and W-B still
   introduces no new liveness dependency, where W-A makes the freeze contingent
   on a process whose loss is one of the conditions C1 exists to handle. §3, §6
   and §7 fall IDENTICALLY on both options and therefore cannot separate them.
```

**This is a recommendation on the stated criteria only. The author selects
nothing, accepts no token, and predicts no outcome.**

---

## §11. Tokens

Selection tokens are mutually exclusive. **None is signable until a bounded X/Y
confirmation round confirms this packet on identical bytes.**

```text
SELECTION, exactly one:
  I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
  I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS

PER-OPTION AMENDMENT, conditional on the selection:
  P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1        with W-A only (§4.7)
  P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1          with W-B only (§5.8)

COMMON AMENDMENTS, required under EITHER selection:
  P1_FREEZE_ABSENT_FALLBACK_NULLABLE_IDENTITY_V1 the §6 peer-schema amendment
  P1_PCS_FREEZE_CLASSIFIER_V1                    the §3 classifier, the
                                                 STAT_OBSERVE_G extension, the
                                                 KV rule, the pgid_or_null
                                                 population rule and
                                                 T_PCS_QUIESCE_MAX_PASSES
  P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1       the §7 twelve-site amendment
  P1_FREEZE_PUBLICATION_L6_L9_V1                 the §8 wording and ND-1..ND-4
```

The W-B selection token is **renamed** from v1's
`…_B_PCS_FREEZES_ON_PEER_EOF` to `…_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS`,
because `PEER_EOF` carried the death claim Y-M1 required withdrawn. **No token
in this packet has been selected or accepted by the author.**

---

## §12. Deterministic v1.3 handoff

### §12.0 Common to both selections

1. §P1-2.2: add `T_PCS_QUIESCE_MAX_PASSES = 16`. **Do not** add any
   `100_000_000` value; the `:267-268` sentence stays byte-true.
2. §P1-10.3: extend `STAT_OBSERVE` to `STAT_OBSERVE_G` per §3.3.
3. New §P1-10.6: `KV`, the `pgid_or_null` population rule `P-1`..`P-3`, and the
   §3.5 scope with its total inclusion/exclusion table.
4. New §P1-10.7: the §3.6 per-group classifier, the sixteen-token set, the §3.7
   continuation table, the §3.8 terminals and §3.9's invalidity dominance.
5. §P1-14.6: add the rules that the sixteen-token set is closed, that
   `_killpg` appears only inside the classifier and the `SIGNAL_GROUP` handler,
   and that `KV` precedes every `_killpg`. **Retain `S-12` unchanged.**
6. **§7's twelve sites**, replaced with the `R1`..`R12` texts, in the option's
   variant. Replace contradictory rows; do not add beside them.
7. §P1-12.2: add `L6`..`L9` and `ND-1`..`ND-4`.
8. §N5 of `…V2_1_2_CORRECTION.md`: apply `A-ABS-1`..`A-ABS-6`.
9. §P1-15: add test rows for the classifier, every token, every exclusion class,
   `KV-6`'s forbidden target, the dedup assertion, and the `A-ABS` biconditionals.
10. Recompute `H_FILE`, `H_BODY`, `H_GUARDDATA`, `H_NORMATIVE`, sentinel counts,
    the placeholder audit and guard fires; required placeholder and guard-fire
    counts remain **zero**.

### §12.1 If W-A is signed

11. §P1-6.2: watchdog slot 6 becomes the freeze socket; slot set `{3,4,5,6,7,8,9,10}`.
12. §P1-6.4: remove `(CLOSE, 6)` from the `WATCHDOG` vector; restate the leak
    proof per §4.1.
13. §P1-6.5: record the retained socket as the fourth persistent non-handle PCS
    descriptor; `P-f`'s required set is unchanged because `P-f` is pre-fork.
14. §P1-7.4: extend `A-5`'s watchdog assertion with `A5W-1`..`A5W-3`.
15. New §P1-8.9: the `t-wd-freeze.v1` channel — §4.2, §4.3, §4.4 verbatim.
16. §P1-8.6: add the constant autonomous key of §4.6.
17. New §P1-11.8: the §4.5 ordering window `T-1`..`T-7`.
18. §P1-11.7: replace the row of §7.2 site 7 per `R7` W-A, then add §4.5's routes.

### §12.2 If W-B is signed

11. **No change to §P1-6.2, §P1-6.4, §P1-6.5, §P1-7.4 or any descriptor rule.**
12. §P1-3.4: add `_MSG_EOR` to the pinned integer constants.
13. New §P1-11.8: the §5.2 trigger `E-1`..`E-4`, the §5.3 continuation and the
    §5.5 record-first ordering `R1`..`R6`.
14. §P1-8.6: add the constant `(generation_id,"PEEREOF",1)` autonomous key.
15. §P1-11.7: replace the row of §7.2 site 7 per `R7` W-B, then add §5.6's matrix.

### §12.3 If neither is signed

v1.2 stands with a second unimplementable obligation. No implementation may
begin: a conforming build cannot satisfy C1's freeze requirement, and a build
that tries fails `S-12`.

---

## §13. Invariants this packet leaves exactly as they were

```text
N-1  THE BLOCKER REMAINS PROVED, on the same four mechanisms (§1), both lines
     concurring.
N-2  THE PCS NEVER RETAINS THE WATCHDOG UPDATE-PIPE WRITE END, under either
     option. §P1-8.7's unconditional close (composite :1398) is untouched, and
     update-pipe EOF remains the single supervisor-death detector. W-A's slot-6
     socket is a SEPARATE socketpair, not a second update-pipe write end.
N-3  THE PCS REMAINS THE SOLE CALLER of fork, posix_spawn, kill, killpg and
     every wait-family primitive. S-12 is retained unchanged under both
     options, and §3's classifier executes in the PCS root only.
N-4  W-B MAY REMAIN RECOMMENDED and does (§10) — but NO OPTION IS SELECTED.
N-5  THE IDENTITY CELL IS NEITHER SELECTED NOR REPAIRED HERE (§6.5).
N-6  T = NOT_ACTIVATED; the programme claim is OPEN.
```

---

## §14. Negative space

This packet creates nothing executable and authorizes no selection, X/Y verdict,
implementation, commit, verifier or manifest edit, process, socket, pipe, fork,
exec, signal, wait or `prctl` operation, supervisor, PCS, controller, worker or
watchdog, capability, world, learner, entropy, capacity artifact, custody
disposition, result manifest, spend, datum, outcome, Proof or claim movement. It
predicts no qualification and no comparison outcome. It selects neither option
and accepts no token. `T` remains `NOT_ACTIVATED`; the programme claim remains
`OPEN`.
