REVISE_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2

# Bounded X-line confirmation — P1 watchdog-freeze choice packet v2

**Reviewer:** Claude Code Opus, independent X-line (engineering/mechanical). I
authored the v1 X-line review (F1–F3); I did not author the packet, the closure,
the composite, or the binding. Bounded confirmation round: I check, on the
committed v2 bytes, whether each v1 finding is closed and whether the repairs
introduced a new defect. Read-only; SHA-256 only; the one deliverable is the sole
file written. No code, probe, or process-control run. `T = NOT_ACTIVATED`;
programme claim `OPEN`; identity-cell non-selection preserved. A `REVISE` verdict
authorizes nothing.

---

## 0. Custody — all recomputed on committed bytes

**Targets:**

```text
72212a986d9551ef47718e871a81951b55a849a10d34eb12e6276499cb675505  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
7b3708550806fcd5742accb5858a2da05a87c4b22ee7fbdffe73ecdbad07759e  reviews/opus5_officina_p1_watchdog_freeze_choice_v2_closure.md
```

**v1 reviews + v1 packet/closure, byte-untouched (match the closure's §2.1):**

```text
c87cc69f93ddd64c8364bcbcce3fa97e32855b55597a57a44bb05bffeee04ae1  reviews/opus_officina_p1_watchdog_freeze_choice_review.md   [MATCH]
37474607e46394178d9dca1f946fd68e58f852cf3157b7948a6e7de6ef13808b  reviews/sol_officina_p1_watchdog_freeze_choice_review.md    [MATCH]
15937b84…  successor/…WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V1_DRAFT.md   [MATCH]
d8d3ced2…  reviews/opus5_officina_p1_watchdog_freeze_author_choice_packet.md   [MATCH]
```

**Governing contracts — every digest matches the closure's §2.2:**

```text
2c857fa8…  …P1_OPERATIVE_COMPOSITE_V1_2.md
6197d2a4…  …V2_1_10_4_P1_BINDING.md
9f1d018e…  …V2_1_CORRECTION.md
ee317172…  …V2_1_1_CORRECTION.md
2cd8b7b5…  …V2_1_2_CORRECTION.md
```

The bytes v2 repairs are the bytes both v1 lines reviewed, and the contracts I
re-derive from are byte-intact.

---

## Verdict

**`REVISE_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2`.**

Nine of the ten v1 findings are confirmed closed (F2, F3, Y-C1, Y-C2, Y-C3, Y-M1,
Y-M2, Y-M3, Y-m1). The new §3 PCS classifier is mechanically sound in structure —
`STAT_OBSERVE_G` indices, `KV-1..KV-6`, `pgid_or_null` population, deduplication,
the total handle-state table, the sixteen closed tokens, the three terminals and
every continuation all check out. Determinations 4, 5, 7 are confirmed in full.

**Two concrete residual defects remain, and F1 is not fully closed:**

- **R-A (determination 3):** the classifier's `freeze_ns` sample —
  `_clock(CLOCK_MONOTONIC)`, §3.6 C-4 — needs the integer constant
  `CLOCK_MONOTONIC`, which is **not** in the §P1-3.4 pinned constant set and is
  **not disclosed** as an addition (only `_MSG_EOR` is). So the answer to the
  bounded X-question is **NO**.
- **R-B (determination 6):** the "complete" twelve-site freezer/witness audit is
  **incomplete** — at least two further normative composite sites (invariant 89,
  and the §P1-13.2 row-4 rationale paragraph) become false/contradictory under
  the amendment and are neither replaced nor listed as checked-fine. This is the
  same class of defect F1 named; F1 is improved (10→12 sites, 2 I missed found)
  but not closed.

Both repairs are small, bounded, mechanism-preserving, and fall **identically on
W-A and W-B**, so they do not shift the comparison: **W-B remains the
mechanically preferable option after repair.**

---

## R-A — undisclosed constant `CLOCK_MONOTONIC` (determination 3)

§3.6 C-4 samples `freeze_ns := _clock(CLOCK_MONOTONIC)`. Direct inspection:

- `_clock` is bound as `time.clock_gettime_ns` — the composite states the
  monotonic sample is "the writer's `time.clock_gettime_ns` sample on the
  monotonic clock" (composite :636). `clock_gettime_ns(clk_id)` **requires** a
  clock-id integer argument.
- `CLOCK_MONOTONIC` appears **nowhere** in the composite: it is not in the pinned
  integer-constant set (:419–423, which pins `_SIGCHLD … _MSG_TRUNC …
  _POSIX_SPAWN_*` but no clock id) and occurs in no other line (grep: zero
  `CLOCK_` tokens).
- The closure discloses exactly one binding-block addition, `_MSG_EOR` (O-3), and
  the bounded X-question asserts "no further … constant … required." That is not
  met: `CLOCK_MONOTONIC` is a second required constant, undisclosed.

This is genuinely small and non-corrupting: `freeze_ns` is journaled as a
P1-owned fact and is **never** consumed as evidence (§3.9 S-1 / §8 L8 route
through `ABSENT` with no synthesized instant), and the composite itself already
samples the monotonic clock for `reported_monotonic_ns` without pinning the
constant — so this is partly a **pre-existing** composite under-specification the
PCS-side freeze now makes concrete. It nonetheless makes the classifier not
literally constructible from "bound primitives + `_MSG_EOR`."

**Smallest repair.** Disclose `CLOCK_MONOTONIC` as a second pinned-integer-constant
addition to §P1-3.4 (companion to `_MSG_EOR`), counted in **both** options' §9
blast radius. Alternatively, if a no-argument monotonic sampler is intended,
restate C-4 as `_clock()` and reconcile with the composite's
`reported_monotonic_ns` description (:636). Falls equally on W-A and W-B (both run
§3). All other classifier primitives verified bound: `_open/_read/_close`
(STAT_OBSERVE_G), `_listdir` (`/proc` enumeration), `_killpg`, `_getpid` (KV-6),
`_clock` — all in §P1-3.4 (:409–414). Signal numbers `19`/`9` are bare integer
literals, an established contract pattern (A-12 uses literal `19` at :1027;
`SIGNAL_ATTEMPT(pid, 9)` at :1676/:1806; `SIGKILL=9 … SIGSTOP=19` documented at
:302), so no new signal constant is required. `STAT_OBSERVE_G` adds no primitive.

---

## R-B — the twelve-site freezer/witness audit is incomplete (determination 6)

§7.2 claims to list "**every** sentence, invariant and table row in composite
v1.2 that assigns the watchdog the freezer or witness-of-record role" — twelve
sites, plus two (invariants 60, 65) checked and confirmed fine. An independent
exhaustive grep of the composite for watchdog+freeze/witness/observation/emit and
for every `freeze observation` / `SIGNAL_GROUP`-mediation sentence finds **at
least two normative sites that become false or contradictory under the amendment
and are in neither list:**

| Missed site | Line(s) | Why it breaks under R2/R3/R8/R9 (watchdog writes/freezes nothing; PCS freezes autonomously) |
|---|---|---|
| **Invariant 89** ("wrong freeze writer") | `2758` | "a freeze observation written by a process that is **neither the watchdog role nor the supervisor role** is rejected" — still names the watchdog as a **permitted** freeze-observation writer, contradicting R2/R8/R9. And "a supervisor-executed freeze that **did not go through `SIGNAL_GROUP`** is rejected" — the new freeze is the PCS's **autonomous §3-classifier `_killpg`**, not the `SIGNAL_GROUP` opcode. |
| **§P1-13.2 row-4 rationale ¶** | `2278–2287` | "There is exactly **one** logical writer … it has **two possible executing processes**"; "C1 selected a **dedicated freezer watchdog as the normal witness**"; "the freeze it performs is **PCS-mediated exactly like every other group stop**" via `SIGNAL_GROUP`. Under the amendment the watchdog is not an executing process at all, so "two possible executing processes" and "the normal witness" are false, and the autonomous classifier is not `SIGNAL_GROUP`-routed. |

A third, weaker instance: the negative-space reader sentence at **line 2389** —
"the freeze-observation record, which **a P1-created role physically emits** and
which the supervisor branch **reaches only through `SIGNAL_GROUP`**" — is at least
partly stale on the same two counts.

**This is more than enumeration.** The composite enforces a single model — every
group freeze is `SIGNAL_GROUP`-mediated (invariant 89; lines 2287, 2389;
§P1-13.7). The §3 classifier introduces a **new** freeze-execution path: the PCS
calls `_killpg` **directly and autonomously**, not through the `SIGNAL_GROUP`
opcode. The packet is aware `_killpg` now has two call sites — its own new
verifier rule reads "`_killpg` appears only inside the classifier and the
`SIGNAL_GROUP` handler" (packet :1567) — but it never reconciles **invariant 89**,
which would reject a freeze that "did not go through `SIGNAL_GROUP`." So the §7
audit and §12 handoff, followed literally, leave a composite in which an invariant
rejects the very freeze path both options depend on. That is exactly the
"contradictory old row or invariant" failure determination 6 asks me to rule out,
and F1's stated closure ("no contradictory old row or invariant") is therefore
not yet earned.

**Smallest repair.** Add invariant 89 (2758) and the §P1-13.2 row-4 rationale ¶
(2278–2287) — and, for completeness, the reader sentence at 2389 — as sites 13–15
in §7.2/§7.3, with replacements that (a) demote the watchdog to non-writer
("written by a process that is not the supervisor role is rejected"), and
(b) admit the PCS's autonomous §3-classifier `_killpg` as a signed
freeze-execution site alongside `SIGNAL_GROUP`, so invariant 89 no longer rejects
it. Reconcile the "two possible executing processes / dedicated freezer watchdog
as the normal witness" prose with the single supervisor-witness/PCS-executor
regime. Falls identically on W-A and W-B (both demote the same role and both use
the same autonomous classifier), so it does not move the recommendation — exactly
as F1 concluded for the sites it did find.

*Related disclosed residual (determination 8):* the closure's weak point #6 admits
the peer/settlement chain outside the composite "was searched by key name only"
for readers that assume a watchdog-written witness. That chain is a separate
contract and outside this bounded round's target set, so this confirmation cannot
certify it closed; it is a real, disclosed, still-open item that the R-B repair
should be paired with before any implementation.

---

## Determination 1 — finding-by-finding, verified against the bytes

| Finding | Class | v2 status | Verification |
|---|---|---|---|
| **F1** freezer/witness sentences not fully enumerated; handoff self-contradicting | must fix | **SUBSTANTIALLY CLOSED — residual R-B** | §7 withdraws "zero P1 sentences" verbatim, distinguishes topology/opcode vs normative-prose changes, lists twelve sites (found 2 the reviews missed: §P1-13.2 row-4 executor 2249-2253, §P1-13.7 freeze row 2367), and §7.3 R7/R6/R11 **replace** the contradictory rows rather than adding. But the audit misses invariant 89 and the row-4 rationale ¶ — **R-B**. |
| **F2** `PEER_EOF` not unique to death; no `MSG_EOR`; half-close unaddressed | must fix | **CLOSED** | §5.2 withdraws "kernel fact, not a report" and "same kernel event" verbatim; E-1a/E-1b/E-1c make `_MSG_EOR` the discriminator (empty record with `MSG_EOR` ⇒ `REQUEST_MALFORMED`, never freezes); E-2 names four indistinguishable causes routing identically (fail-safe). `_MSG_EOR`-not-bound disclosed (O-3), verified against :419-423. |
| **F3** `ABSENT` route presented as unconditional; fallback needs numeric identity | should fix | **CLOSED (constructively, Y's stricter framing)** | §6 amends the fallback schema (below); §6.6 also states X's framing point. Taken as Y-C3. |
| **Y-C1** freeze scope not constructible/total; per-handle continuation incomplete | Critical | **CLOSED** | §3 verified in full (determination 2 below). Withdraws `SCOPE`/`table_seq`/lease verbatim; §3.5 total handle-state table incl. STOPPED; §3.4 `KV-1..6`; §3.3 `P-1..3` population; §3.6 sixteen closed tokens; §3.7 one continuation each; §3.8 three terminals. |
| **Y-C2** W-A repeatable; pricing false | Critical | **CLOSED** | §4.2 withdraws `request_seq`/`table_seq`; constant key `(generation_id,"WDFREEZE",watchdog_handle_id)`, handle id PCS-supplied; exactly one accepted action; §4.3 gate `G-1..4` (PCS-side endpoint-loss fact, mechanically verifiable); §4.6 `P-1..4` prices full-charge invalidity and shows the gate makes the marginal price zero. |
| **Y-C3** orthogonality fails at `ABSENT` fallback | Critical | **CLOSED** | §6 `A-ABS-1..6` (determination 7 below), verified serializable and preimage-stable. |
| **Y-M1** `PEER_EOF` proves endpoint loss not death | Major | **CLOSED** | §5.2 `PEER_CONTROL_ENDPOINT_LOST` replaces `SUPERVISOR_LOST` everywhere; E-4 two independent descriptors, no ordering/identity asserted; §5.4 "not established" column. |
| **Y-M2** W-B journals only after side effect | Major | **CLOSED** | §5.5 `R1..R6`: `R3` appends `ACCEPTED`+fsync **before** the classifier; `R2` routes an existing `ACCEPTED` to inconclusive invalidity, no second freeze; §5.6 thirteen-row matrix keyed to last durable marker. |
| **Y-M3** W-A lacks ordering vs the PCS `PEER_EOF` terminal | Major | **CLOSED** | §4.5 `T-1..T-7`: bounded 60 s window **before** the non-returning reaper (`T-4` makes it strictly after by definition); ends on first of accepted+terminal / socket-EOF / `REAPED_POSITIVE` / bound; `T-6` restart never adopts/repeats. |
| **Y-m1** publication caveat uses overclaimed death semantics | Minor | **CLOSED** | §8 splits into `L6`–`L9` with Y's three sentences; `ND-1..4` forbid distinguishing a `COMPLETED` PCS journal from any other `ABSENT` case; `ND-4` adopts the full-charge-is-a-resource-consequence correction. |

---

## Determinations 2, 4, 5, 7, 8 — confirmations

**2 — the §3 classifier. CONFIRMED (modulo R-A).**
- `STAT_OBSERVE_G` indices: **correct.** Linux `/proc/<pid>/stat`, counting tokens
  after the final `)`: token 1 = state (field 3), 2 = ppid (4), 3 = pgrp (5),
  4 = session (6), 20 = starttime (22). Consistent with §P1-10.3's existing
  "20th token = start time." Reuses the same five-way result and failure
  classes; no new primitive.
- `KV-1..KV-6`: sound. Re-evaluated before **every** `_killpg`, never cached;
  `KV-4` identity-mismatch ⇒ `CONTRADICTED` (§P1-10.4 I-2); `KV-6` forbids the
  PCS's own group, any watchdog group, and the supervisor group — load-bearing,
  since the `setsid=False` watchdog shares the PCS group (composite :1432-1433).
- `pgid_or_null` population `P-1..P-3`: correctly fills a genuine v1.2 gap
  (verified: `pgid_or_null` occurs once, at :1260, unpopulated; `P-1`
  `setsid=True` ⇒ pgid=pid at :480-481; `P-2` watchdog stays null; `P-3` write-once).
  Disclosed as O-1.
- Deduplication `SC-3`: distinct ascending pgids, collapse asserted zero (correct,
  given the reuse proof :1541-1550).
- Total handle-state table: covers every signed `state`/`ownership` value
  (:1261-1263) incl. `STOPPED` (v1's omission), with benign/non-benign/structural
  classes.
- Sixteen tokens: closed set, reusing §P1-10.5's six-way `_killpg` classifier
  verbatim (:1607-1610, :1649-1666); three terminals with `FREEZE_TOTAL_PROVED`
  the only valid one; §3.7 one durable continuation per token; §3.9 invalidity
  dominance. All internally consistent.

**4 — W-B endpoint-loss classifier. CONFIRMED.** E-1a/E-1b/E-1c distinguish
empty-SEQPACKET-record (`MSG_EOR` set ⇒ `REQUEST_MALFORMED`) from EOF/half-close
(`MSG_EOR` clear ⇒ endpoint loss); recvmsg indexing `r[0]` data / `r[2]` msg_flags
is correct. `R3` journals `ACCEPTED`+fsync before the classifier; `R2` never
retries after an accepted prefix (constant key, inconclusive on re-read). E-2/E-3
never claim supervisor death; `SUPERVISOR_LOST` withdrawn everywhere.

**5 — W-A repaired. CONFIRMED.** One-shot (constant four-field request; key
`(generation_id,"WDFREEZE",watchdog_handle_id)`, handle id PCS-supplied not sent);
no-target; gated (`G-1` PCS-side endpoint-loss, `G-2` `PEER_ENDPOINT_LIVE` refusal,
`G-3` verifiable fixture); descriptor-accounted (§4.1 closes both v1 non-blocking
gaps — `A5W-1..3` pin slot-6 `S_ISSOCK`/`SEQPACKET`/`O_RDWR`; the retained end is
the 4th persistent non-handle PCS descriptor, created after `P-f` so `P-f`'s set
is byte-unchanged); ordered (`T-1..T-7`); cannot repeat (one `ACCEPTED` per
generation, `T-4` generation-terminal); and does **not** retain the update-pipe
write end (the slot-6 socketpair is a separate endpoint; §P1-8.7 :1398 unchanged).

**7 — nullable `ABSENT` amendment. CONFIRMED.** `A-ABS-1` renames
`pgid → pgid_or_null`, `start_identity → start_identity_or_null`, null **iff**
`rejection_conjunct == 0` (biconditional validity conjunct, both directions);
`A-ABS-2` same for `current_unresolved_member_count` (author-added, sound: an
unnamed group has no computable count); `A-ABS-3` forces `supervisor_quiescence =
UNKNOWN` on that branch (from §Z4.6 conjunct 10); `A-ABS-4` synthesizes nothing.
Verified against V2_1_2_CORRECTION: the fallback key set (:855-869) indeed lists
`pgid`/`start_identity` without `_or_null` today; the `fallback_witness_id`
preimage (:833-840) contains **none** of the three amended keys, so ids stay
stable as §6.3 claims; §N5.4's `FREEZE_INSTANT_UNKNOWN` branch (:905-909) is the
`!= 0` branch and is untouched. Crucially, `process_id` is left mandatory and is
**constructible** — it is a claim-content identifier (recomputed from a signed
preimage), not a raw kernel PID, so an opaque-handle supervisor can supply it.
No PCS journal state becomes peer evidence: §3.9 S-4 / §5.4 / §8 L8 keep
`freeze_ns` and the P1 journal out of the peer witness; the witness is the
supervisor-written fallback via the `ABSENT` route.

**8 — author-disclosed weak points.**
- `setsid()` escape (O-4, §3.10): **fail-closed and sound** — a leader that calls
  `setsid`/`setpgid` fails `KV-5` (`GROUP_CHANGED`, no signal); an escaped child is
  caught by the quiescence enumeration's session/parent-chain reach (⇒
  `GROUP_QUIESCENCE_UNKNOWN`). Either way `FREEZE_INCOMPLETE` ⇒ invalidity; no
  false evidence. Correctly noted that "process group immutable while open"
  (:300-305) is a lease declaration, not kernel enforcement. Real residual,
  honestly unpriced-beyond-`L7`/`L9`.
- Quiescence interval substitution (O-2): **sound.** §W3.3 uses 100 ms × 8 = 800 ms
  (verified V2_1_CORRECTION :60-61); the composite states "100_000_000 appears in
  no rule of this contract" (:267); v2 reuses `T_SUPERVISOR_POLL_INTERVAL_NS`
  50 ms × 16 = 800 ms, adding one count constant and no new nanosecond numeral.
  Correct avoidance of a signed-sentence contradiction.
- `_MSG_EOR` binding (O-3): correctly disclosed as a one-name §P1-3.4 addition,
  counted in W-B's blast radius. (Its sibling constant `CLOCK_MONOTONIC` is the
  one that was **not** caught — R-A.)
- `current_unresolved_member_count` (A-ABS-2): sound derivation, verified above.
- Hidden peer reader assuming a watchdog-written record: **disclosed, not closed**
  (weak point #6) — see the R-B addendum.

---

## Answer to the bounded X-question

> Is the §3 classifier executable using only §P1-3.4 primitives plus the single
> disclosed `_MSG_EOR`, with no further primitive/constant/import/module?

**NO.** The one undisclosed item is the integer constant **`CLOCK_MONOTONIC`**,
required as the argument to `_clock` (= `time.clock_gettime_ns`) for the
`freeze_ns` sample at §3.6 C-4, and absent from the pinned §P1-3.4 set (:419-423).
Everything else the classifier needs is bound or is the disclosed `_MSG_EOR`.

---

## Scope

`REVISE`. Two bounded repairs (R-A: disclose `CLOCK_MONOTONIC`; R-B: complete the
freezer/witness audit and reconcile invariant 89 with the autonomous classifier),
both mechanism-preserving and both falling equally on W-A and W-B, after which
W-B remains mechanically preferable. This verdict authorizes **no** selection, no
amendment acceptance, no implementation, no activation, no manifest/verifier edit,
and no programme movement. Were the packet confirmed on repaired bytes,
confirmation would authorize **only Kirill's informed W-A/W-B selection** and the
associated disclosed amendments — not implementation and not activation. `T`
remains `NOT_ACTIVATED`; the programme claim remains `OPEN`;
`AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS` is neither selected nor repaired
here. No existing file was modified in producing this review; its sole product is
this file.
