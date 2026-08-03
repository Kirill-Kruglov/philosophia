REVISE_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_PACKET

# Independent X-line review — P1 watchdog-freeze author choice packet v1

**Reviewer:** Claude Code Opus, independent X-line (engineering/mechanical).
I did not author the packet, the composite, the binding, or the identity packet
whose §6 report this round re-derives. Work was read-only except this one file.
No code was implemented, no process-control probe run, no `T` activation, no
programme-state change.

`T = NOT_ACTIVATED`; programme claim `OPEN`; no selection; no process control;
no spend, datum or outcome; no implementation authority. This review moves none
of them. A `REVISE` verdict authorizes **nothing** — not selection, not
implementation, not activation.

---

## 0. Custody — recomputed on identical bytes

```text
15937b84b2e2a61de3d908ea014cbded902ca5ba15f58b988920c99be0702f09  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
d8d3ced2aee226673903223250d810a5e574362132aafa644515c150c05f0cdb  reviews/opus5_officina_p1_watchdog_freeze_author_choice_packet.md
```

The packet self-reports 616 lines — confirmed (`wc -l` = 616). The governing
composite hash was recomputed and **matches** the author's pinned digest, so
this review reads the same architecture the author read:

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/…P1_OPERATIVE_COMPOSITE_V1_2.md   (matches author §2)
```

The author closure was treated as untrusted; every determination below rests on
direct inspection of the composite v1.2, the P1 binding, the control-channel
§W3.3/§N5 correction, and the `S-12`/slot contracts, cited by line.

---

## Verdict

**`REVISE_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_PACKET`.**

The blocker is independently **PROVED** and every mechanical attack on both
options **holds** — W-A's capability is genuinely non-general and W-B's autonomy
is genuinely bounded. But three defects, ordered by severity below, keep the
packet from being a clean bit-exact basis for an author A/B selection. **All
three are wording / enumeration / spec-completeness repairs; none touches the
mechanism of either option, and W-B remains mechanically preferable on the three
stated criteria after all of them are applied** (§Recommendation-after-repair).

---

## Findings, by severity

### F1 — the watchdog-freezer/witness sentences are **not fully enumerated**; the "deterministic v1.3 handoff" is therefore incomplete and self-contradicting (determination 6) — **must fix**

The packet's §4.8 and §5.1/§6 rest on the claim that W-B "amends **zero** P1
sentences" and changes only "C1's freezer and witness roles," and §8 presents a
section-by-section "deterministic v1.3 handoff." The amendment box (§4.8) and
the §8 W-B handoff name only **§P1-9.2 properties 7 and 12**.

Direct inspection of composite v1.2 finds **at least seven further sentences**
that assign the watchdog the freezer/witness role and become false or
contradictory the moment the watchdog is demoted to a pure liveness sensor —
none of them enumerated or scheduled for amendment:

| Composite site | Line | The sentence that breaks under W-B (and W-A) |
|---|---|---|
| C1 intro statement | 202–203 | "A dedicated watchdog process **witnesses and freezes**." |
| §P1-9.2 Termination ¶ | 1469 | "the watchdog observes EOF, **writes its final observations** and exits" |
| §P1-9.4 S-4 (shutdown) | 1490 | "the watchdog observes EOF, **writes its final observations**, `os._exit(0)`" |
| §P1-11.4 continuation step 3 (PCS-death path) | 1783 | "the watchdog **writes its observations for the groups it knows** and exits" |
| §P1-11.7 crash matrix | 1888 | "the watchdog sees update-pipe EOF **and freezes, observes and exits**" |
| §P1-13.1 executor matrix | 2006 | watchdog "**physically emits a peer-owned record**" |
| Invariant #61 (and #63) | 2730 | "supervisor death produces update-pipe EOF **and the freeze, observe and exit route**" |

Two consequences make this more than cosmetic:

1. **The §8 handoff, followed literally, produces a contradictory composite.**
   §8 W-B item 5 says *add* the six races of §4.4 to §P1-11.7 — but it leaves the
   **existing** line-1888 row ("the watchdog … freezes, observes and exits")
   in place. New rows say the PCS freezes and the watchdog has no effect; the
   untouched row says the watchdog freezes. §P1-11.4 is not mentioned in the
   W-B handoff at all, yet its step 3 embeds watchdog-freeze semantics. So the
   handoff is not deterministic: an implementer would be left with directly
   opposed statements.

2. **The headline comparison is true only under a private, unstated taxonomy.**
   "W-B amends zero P1 sentences" is defensible only if "P1 sentence" is read as
   "descriptor/structural sentence" and every freezer/witness sentence is
   re-bucketed as "C1." Properties 7 and 12 and all seven sentences above are
   *physically P1-composite sentences*. The claim needs restating as "zero
   **descriptor/structural** P1 sentences," accompanied by the **complete**
   C1-role sentence list.

**Smallest repair.** In §4.8, replace the enumeration with the full list above
(properties 7 and 12 **plus** lines 202–203, 1469, 1490, 1783, 1888, 2006, 2730,
and invariants #61/#63). In §8, change W-B item 5 from "add" to "replace the
supervisor-death row of §P1-11.7 and add the six races," add an explicit
§P1-11.4-step-3 amendment, add §P1-9.4 S-4 and the §P1-9.2 Termination ¶, and
amend the §P1-13.1 executor-matrix row and invariant #61. Restate §5.1/§6's
"zero P1 sentences" as "zero descriptor/structural sentences." **This repair
falls identically on the W-A handoff (§8 W-A), which demotes the same
executor/witness role and misses the same seven sentences.** Because both
options must amend the identical C1-role set, the repair does **not** change
their relative standing.

### F2 — `PEER_EOF` is **not a unique trigger for supervisor death**, and the required half-close route is unaddressed (determinations 3 and 4) — **must fix (wording); safety is intact**

§4.2 E-1 defines the trigger as "a zero-length record with no ancillary data ⇒
`PEER_EOF`" and asserts "The supervisor's end was closed by the kernel at its
exit, so this is a kernel fact, not a report." Mechanically, on a
`SOCK_SEQPACKET` socket, `_recvmsg` returning length 0 arises from **three**
distinct causes:

- **(a) peer exit** — the intended case;
- **(b) peer half-close** — a live supervisor calling `shutdown(SHUT_WR)`
  produces a genuine, kernel-delivered EOF while the process is still alive.
  This is exactly the "half-close" route the round requires to have one
  deterministic disposition, and the packet does not name it;
- **(c) a zero-length data record** — distinguishable from a true EOF only by
  `MSG_EOR` in `msg_flags`, which E-1 never inspects. As written, E-1 cannot
  tell an empty datagram from end-of-stream.

So `PEER_EOF` is **sufficient** to fire but **not unique to death**: the true
predicate is "loss of the supervisor write stream by any cause." The packet
overclaims uniqueness ("kernel fact, not a report").

**Why this is F2 and not the blocker.** All three causes route identically —
`SUPERVISOR_LOST`, the once-per-generation freeze, `ABSENT` witness, `UNKNOWN`
invalidity, no synthesized instant, no spend. The conflation is therefore
**fail-safe**: any loss of the stream conservatively freezes and invalidates.
The defect is (i) the false uniqueness claim, (ii) E-1's missing `MSG_EOR` /
non-empty check, and (iii) the missing half-close disposition — not an unsafe
behaviour. In the trusted topology the supervisor process runs only contract +
harness code (the client target runs in `CONTROLLER`/`WORKER`, composite
line 2007), so a spurious half-close is an A3-residual, not a normal path; but a
packet at this rigor must still route it.

**Smallest repair.** In §4.2 E-1: (1) require that a zero-length receive with
`MSG_EOR` set (a real empty record) is `REQUEST_MALFORMED`, not `PEER_EOF`;
(2) state that exit-EOF and `shutdown(SHUT_WR)` half-close both yield `PEER_EOF`
and route identically to the freeze + `SUPERVISOR_LOST` + `ABSENT`-witness
invalidity; (3) reframe the trigger as "loss of the supervisor write stream,
fail-safe to freeze-and-invalidate," dropping "uniquely death." No E-1..E-5
step changes.

### F3 — the `ABSENT`-route independence claim is **narrowly true but presented as unconditional**; the fallback still needs numeric identity the P1 supervisor cannot yet express (determination 5) — **should fix (framing)**

The `ABSENT` sentinel is a **legitimate signed witness route, not fabricated
evidence** — confirmed: §N5.1 defines `rejected_object_sha256_or_null = null`
"null ONLY for the ABSENT sentinel," §N5.2 gives `rejection_conjunct 0 == the
ABSENT sentinel` with `unknown_reason = EVIDENCE_ABSENT`, and §N5.3 routes it to
the signed `UNKNOWN` invalid route with **no synthesized freeze instant** and no
`overrun_ns`. Neither option writes a numeric peer witness; neither is
conditioned on the identity cell's *outcome*. In the narrow sense the packet
states its claim (§5.3: "neither writes a numeric peer witness"), the claim
**holds**.

But the packet presents the route as unconditionally available ("routes exactly
where the signed chain already routes one", §4.5). The route terminates in a
**supervisor-written** `t-freeze-fallback-observation.v1` whose mandatory key
set (§N5.2) includes `process_id`, `pgid`, `start_identity` — listed with **no**
`_or_null` suffix, unlike the sibling `rejected_witness_path_or_null`. A P1
supervisor "holds opaque handles only … cannot express a PID" (composite
§P1-9.3, line 1480), and peer numeric-identity install is itself "**blocked by
§P1-13.2 row 2 until the author cell is signed**" (composite line 2363). So the
`ABSENT` fallback's numeric-identity population under P1 is a **pre-existing
peer-layer question, shared with `AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS`**
— not resolved by this packet, and not differentiating W-A from W-B (both
inherit it, neither creates it). This is precisely the author's own flagged
weakest points #2 and #5.

**Smallest repair.** State in §4.5/§5.3 that "independent of the identity cell"
means "**adds no new dependency**," and that the operability of the `ABSENT`
fallback under P1 — specifically how the supervisor populates
`process_id`/`pgid`/`start_identity` for an `EVIDENCE_ABSENT` record while
holding opaque handles — is a pre-existing peer-layer item the identity cell
governs, not something this packet clears. No mechanism changes.

---

## What is confirmed (survives review on identical bytes)

**Blocker — PROVED, and understated as the packet claims (determination 1).**
All four mechanisms verified directly:

1. **`S-12`** at composite line 2601, verbatim: "subprocess, Popen, fork,
   waitpid, kill, killpg and system appear on no path of `generic_harness.py`."
   The watchdog's operative behaviour **is** on that path: `A-4` requires
   `argv[7]` to be one of four literals, `A-10` imports
   `philosophia.officina.generic_harness` as "the only import," `A-11` pins its
   `(st_dev, st_ino)`, and `A-13` "call[s] exactly one pinned entry function,
   selected by `argv[7]` from a closed four-entry mapping." The role bootstrap
   (`A-1..A-13`) is a fixed verification-then-dispatch sequence with no room for
   target behaviour, so the watchdog cannot legally freeze from the bootstrap
   root either. `killpg` on the watchdog path is rejected by the selected
   verifier. **Dispositive alone**, and it answers the author's X-question 1 in
   the negative: no conforming build can relocate the watchdog freeze out of
   `generic_harness.py`.
2. **Sole-caller sentence**, P1 binding §P1B.1 item 1 (lines 150–153), verbatim:
   the PCS "is the sole caller of `fork`, `posix_spawn`, `kill`, `killpg` and
   every `wait`-family primitive." Independently dispositive.
3. **No endpoint**: watchdog slot set `{3,4,5,7,8,9,10}` (§P1-6.2), slot 6 "not
   used; explicitly closed by a file action," and §P1-6.4 makes `{6}` the
   `WATCHDOG` explicit-close group. Slot 5 is the harness source, so the
   watchdog also holds **no runtime-root descriptor** — it cannot `openat` the
   `WATCHDOG/FREEZE/` directory to write the witness. Both halves confirmed.
4. **No relay**: the trigger *is* the supervisor's death, and §P1-8.7 (line 1398)
   has the PCS "close[] its copies of the supervisor's ends unconditionally"
   after the send, so the PCS holds no channel to the watchdog.

**Corollary verified.** The PCS closing its copy of the update-**write** end
(line 1398) is what makes update-pipe EOF fire on supervisor death; retaining it
would suppress EOF, and update-pipe EOF is the **single remaining** detector
(§P1-9.2 property 10 "by no other"; the `getppid()` detector is deliberately
deleted, property 11 / line 204). So the packet's §1.5 "inadmissible" corollary
is correct.

Minor: packet §1.1 step 6 transcribes the witness path as
`WATCHDOG/FREEZE/<witness_id>.json`; the source §W3.3 (`…V2_1_CORRECTION.md:763`)
says `<process_id>.json`. Immaterial to the proof.

**Determination 7 — CONFIRMED.** Neither option makes the PCS retain the
watchdog update-pipe **write** end. §P1-8.7 (line 1398) closes the PCS's copy
unconditionally after the send. W-A adds a **separate** `SOCK_SEQPACKET`
socketpair at slot 6, not a second update-pipe write end; the PCS legitimately
retains *that socket* (with `FD_CLOEXEC`) as its freeze-request receive
endpoint. W-B adds nothing. Update-pipe EOF on supervisor death is preserved
under both.

**W-A capability is genuinely non-general (determination 2).** One-element
opcode set (field 4), **no target field of any kind** (no pid/pgid/handle/role/
index), generation binding (field 2) plus published-`table_seq` binding
(field 5), journal-before-act replay returning `REPLAYED` with no syscall, a
single non-retried request, and a receipt-only reply carrying **no** numeric
identity. The watchdog-side send is itself `S-12`-clean: `sendmsg`/`recvmsg` are
not in `S-12`'s forbidden set. Bounded to "one freeze per generation of a set it
cannot name, narrow, widen or redirect" — answers the author's X-question 3 in
the negative. Descriptor/leak topology is sound: CPython `socketpair` descriptors
are non-inheritable (`FD_CLOEXEC` set), the watchdog end reaches slot 6 by `DUP2`
(clearing `FD_CLOEXEC` on the destination), point-to-point so no third joiner;
the §P1-6.4 proof extends with one more `FD_CLOEXEC`-carrying PCS descriptor.
Two **non-blocking** W-A spec gaps to close only if W-A is ever selected (it is
not recommended): the updated `A-5` assertion must fix slot 6's **type** as
`S_ISSOCK`/`SEQPACKET` (currently unspecified), and the retained socket is a
persistent **non-handle** PCS descriptor that should be reconciled with the PCS
descriptor-accounting rules of §P1-6.5.

**W-B autonomy is bounded initiative, not general authority (determination 3).**
One kernel-fact trigger, the pre-existing SCOPE of §3.4, at most once per
generation via the constant journal key `(generation_id,"PEEREOF",1)`, not
request-inducible, and reachable **only** from the `PEER_EOF` site (the §8-item-8
verifier rule). Corroborated by the binding: §P1B.8.1 (composite line 1888)
**already** has the PCS "observe[] `PEER_EOF` on `t-pcs.v1`, hold[] every live
handle in the … non-returning reaper state," so W-B adds only the freeze
**action** at a detection point the signed architecture already has — which is
why W-B's "no new descriptor, no topology change" claim is real (§P1-6.2 /
§P1-6.4 / `A-5` are byte-unchanged, verified).

**Failure routing (determination 4).** Supervisor death (W-B: PCS `PEER_EOF`
freeze; watchdog EOF-exit), PCS death (§P1-11.4 → `GENERATION_NOT_ADOPTABLE`,
whole-generation invalidity, no adoption), watchdog death (§P1-9.2 detection +
`SPAWN_WATCHDOG`), stale generation (`WRONG_GENERATION`), replacement watchdog
(symmetry — §5.4, trivial under W-B), and simultaneous failures each have one
deterministic route — **except** the half-close case (F2). One noted non-blocker
matching author weakest-point #3: E-3 runs §W3.3 quiescence over the PCS's *own
recorded* member set, which may be narrower than §W3.3's session/parent-chain
reach; because the W-B witness is `ABSENT` regardless, this bears only on
best-effort stop completeness, not on any cited evidence, and is covered by the
"orphans keep running" fact + the `L6` non-guarantee.

**Comparative audit that survives (determination 6, comparative parts).** W-B
adds zero descriptors/opcodes/capabilities and leaves the §P1-6.4 leak proof
byte-unchanged; W-A's leak-proof extension is sound; W-A's residual is a **new**
liveness dependency on a process whose death is itself a C1 condition, while
W-B's is **not** new (D1 already makes PCS loss total, §P1-11.4). These
comparative claims hold. Only the "zero P1 sentences" phrasing and the
freezer/witness **enumeration** are defective (F1). No PID/PGID identity choice
is required by either option's freeze path (determination 5), subject to the F3
framing caveat about the shared downstream fallback.

---

## Recommendation after repair

After F1–F3 — all enumeration/wording/framing, none altering a single E-step,
grammar field, slot, or journal key — **W-B remains mechanically preferable on
the three stated criteria** (signed-authority fidelity, mechanical testability,
minimal reopened contracts):

- it still changes **no descriptor topology**, so the §P1-6.4 leak proof stands
  byte-unchanged;
- it still introduces **no new liveness dependency**, where W-A makes the freeze
  contingent on a live, unwedged watchdog — a process whose death is one of the
  conditions C1 exists to handle;
- its single genuine cost, the first autonomous PCS action, is still bounded by
  a kernel-fact trigger (now correctly framed as fail-safe stream-loss, F2), a
  pre-existing scope, and a once-per-generation key.

F1 lands equally on both options (both demote the same executor/witness role),
so completing the enumeration does not shift the comparison. F2 tightens exactly
W-B's trigger but leaves it fail-safe. F3 is shared and non-differentiating.
None of the repairs flips the recommendation; they correct overclaims
("uniquely death," "zero P1 sentences," "routes exactly where the signed chain
routes one") and make the §8 handoff genuinely deterministic.

---

## Scope statement

This is a `REVISE` verdict. It authorizes **no** selection, no X/Y clearance
of the packet, no implementation, no activation, no manifest or verifier edit,
and no programme movement. Were the packet later confirmed on repaired bytes,
that confirmation would authorize **only Kirill's informed A/B selection** — not
implementation and not activation. `T` remains `NOT_ACTIVATED`; the programme
claim remains `OPEN`. No existing file was modified in producing this review;
its sole product is this file.
