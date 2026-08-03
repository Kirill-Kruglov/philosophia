READY_FOR_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2_XY_CONFIRMATION

# Author closure — P1 watchdog-freeze choice packet v2

**Author:** Claude Code Opus 5, **specification author only**. I authored the
whole supervisor/control-channel chain, v1 through v1.2, the identity packet
that reported this blocker, the v1 choice packet and this v2 repair. I am
therefore **disqualified** as its independent X-line or Y-line reviewer, and
**this closure is an untrusted author self-assessment**.

**No choice was made and no token was accepted or minted.** Both selection
tokens and all six amendment tokens exist only as text in a draft packet
awaiting a bounded independent confirmation round.

`T = NOT_ACTIVATED`; programme claim `OPEN`. This round produced no selection,
X/Y verdict, implementation, code or test edit, verifier or manifest change,
process or behavioural probe, activation, entropy, E1/E2/E3 spend, Q/C work,
datum, outcome, Proof or claim movement.

---

## 1. Deliverables and untouched-file confirmation

Exactly two new files. **No existing file was modified.**

| Path | Lines |
|---|---|
| `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md` | 1637 |
| `reviews/opus5_officina_p1_watchdog_freeze_choice_v2_closure.md` | this file |

`successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`,
`reviews/opus5_officina_p1_watchdog_freeze_author_choice_packet.md`,
`reviews/opus_officina_p1_watchdog_freeze_choice_review.md` and
`reviews/sol_officina_p1_watchdog_freeze_choice_review.md` are **byte-untouched**,
as §2.1 demonstrates by recomputing their digests.

Only read-only commands were run: `git show`, `grep`, `sed`, `awk`, `wc`,
`sha256sum`. No test, behavioural probe or process-control operation was
executed. No code was implemented. No `T` state was touched.

---

## 2. Hashes and custody

### 2.1 Reviewed inputs, recomputed on committed bytes

```text
15937b84b2e2a61de3d908ea014cbded902ca5ba15f58b988920c99be0702f09  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
d8d3ced2aee226673903223250d810a5e574362132aafa644515c150c05f0cdb  reviews/opus5_officina_p1_watchdog_freeze_author_choice_packet.md
c87cc69f93ddd64c8364bcbcce3fa97e32855b55597a57a44bb05bffeee04ae1  reviews/opus_officina_p1_watchdog_freeze_choice_review.md
37474607e46394178d9dca1f946fd68e58f852cf3157b7948a6e7de6ef13808b  reviews/sol_officina_p1_watchdog_freeze_choice_review.md
```

The first two match the digests **both** review lines independently recomputed
and declared matching, so the bytes the X and Y lines reviewed are exactly the
bytes v2 repairs. The last two pin the defect reports themselves, so a
confirmation round can prove it is dispositioning the same findings.

### 2.2 Governing contracts, recomputed on committed bytes

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/…SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md
6197d2a4073d35fc978119db32128c50d12594343ac87731640a1d8e19f09e84  successor/…SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/…SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/…SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/…SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

Every previously pinned digest matches what v1's closure and the X line
recorded. **The custody chain is byte-intact across this round.** The C1
selection whose role this packet reassigns is
`I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER`
(`…SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md:18`).

### 2.3 Produced this round

```text
72212a986d9551ef47718e871a81951b55a849a10d34eb12e6276499cb675505  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
```

**On this closure's own digest.** A file cannot contain the SHA-256 of its own
committed bytes without a fixpoint, so this closure does not embed it. It is
recomputed by:

```text
sha256sum reviews/opus5_officina_p1_watchdog_freeze_choice_v2_closure.md
```

Custody stays acyclic: v2 packet → this closure → X/Y confirmation → any future
signature. The v2 packet contains none of its own digests.

### 2.4 Evidence used, by source location

Every citation in v2 was read from the committed bytes of the contracts, not
from v1's or either review's quotations:

```text
S-12                                        composite :2601
sole-caller sentence                        …P1_BINDING.md:150-153
binding's freeze assertion (§P1B.8.1)       …P1_BINDING.md:627-632
watchdog slot map / slot-6 closure          composite :725-740 (§P1-6.2 table,
                                            §P1-6.4 file actions and leak proof,
                                            §P1-6.5 phases)
watchdog properties 1,2,6,7,10,11,12,13     composite :1440-1466
watchdog Termination ¶                      composite :1469-1473
watchdog setsid=False, never a killpg target composite :1432-1433
§P1-9.3 "cannot express a PID"              composite :1480
§P1-9.4 S-4                                 composite :1490
§P1-8.1 SOCK_SEQPACKET record semantics     composite :1167-1173
§P1-8.3 opcode table, SIGNAL_GROUP's
  kernel-verified-group precondition        composite :1223, :1271, :1427
§P1-8.5 handle shape incl. pgid_or_null     composite :1256-1266
§P1-8.7 PCS closes the supervisor's ends    composite :1398
§P1-10.1 ownership + PID-reuse proof        composite :1519-1550
§P1-10.2 six-way classifier, applied to
  _kill and _killpg verbatim                composite :1595-1610
§P1-10.3 STAT_OBSERVE                       composite :1600-1626
§P1-10.4 identity decision table I-1..I-10  composite :1628-1647
§P1-10.5 SIGNAL_ATTEMPT six-way             composite :1649-1666
§P1-11.4 PCS loss, GENERATION_NOT_ADOPTABLE composite :1757-1785
§P1-11.6 invalidity routing and dominance   composite :1849-1866
§P1-11.7 crash matrix supervisor-death row  composite :1888
§P1-12.2 L1-L5                              composite :1920-1929
§P1-13.0 layers; PCS holds no peer state    composite :1993-2007
R-L4 one-way call direction                 composite :2022-2027
§P1-13.2 row 4 executing process            composite :2249-2253
§P1-13.5 invalidity dominance               composite :2323-2330
§P1-13.7 single-writer table, freeze row    composite :2367
§P1-14.6 code rules, S-11..S-14             composite :2596-2606
invariants 57, 60, 61, 62, 63, 65           composite :2726-2734
§P1-2.2 constants; "100_000_000 appears in
  no rule of this contract"                 composite :254-268
§P1-3.4 primitive binding block             composite :407-417
§P1-3.4 pinned integer constants (no
  _MSG_EOR)                                 composite :419-423
C1 intro "witnesses and freezes"            composite :202
getppid detector deliberately absent        composite :203-205
§W3.3 freeze procedure, <process_id>.json   …V2_1_CORRECTION.md:744-770, :763
§W3.3 quiescence constants                  …V2_1_CORRECTION.md:60-61
§Z4.6 conjunct 10                           …V2_1_1_CORRECTION.md:1056
§N5.1 ABSENT sentinel and id preimage       …V2_1_2_CORRECTION.md:830-851
§N5.2 fallback schema key set               …V2_1_2_CORRECTION.md:853-869
§N5.3 routing                               …V2_1_2_CORRECTION.md:876-886
§N5.4 unknown_reason separation             …V2_1_2_CORRECTION.md:888-910
§N5.5 production/duplicate/conflict/order   …V2_1_2_CORRECTION.md:912-930
process group immutable while open          …T_ACTIVATION_PROTOCOL_V2_CORRECTION.md:300-305
C1 selection token                          …SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md:18
```

---

## 3. Finding disposition — one to one

Every finding of both reviews, with its status, the exact repair, and the
residual. **Nothing is marked closed by restatement.**

### 3.1 X line — `reviews/opus_officina_p1_watchdog_freeze_choice_review.md`

| Finding | Class | Status | Repair, and where |
|---|---|---|---|
| **F1** the freezer/witness sentences are not fully enumerated; the v1.3 handoff is incomplete and self-contradicting; "W-B amends zero P1 sentences" rests on a private taxonomy | must fix | **CLOSED** | v2 §7 **withdraws** "zero P1 sentences" verbatim and replaces it with the honest distinction — **topology/opcode changes** versus **normative P1 prose changes**. §7.2 audits the whole composite and lists **twelve** sites: the seven X named (`202`, `1447-1451`, `1464-1465`, `1469-1470`, `1490`, `1783-1784`, `1888`, `2006`, `2730`, `2732`) plus **three the reviews did not find** — §P1-13.2 row 4's "EITHER the watchdog role process, normally" (`2249-2253`), §P1-13.7's freeze row "called from the watchdog role entry" (`2367`), and invariant 63's thirteen-property clause (`2732`). §7.3 gives exact replacement texts `R1`..`R12` **for both options**, with the W-A/W-B variants marked. §12's handoff **replaces** the contradictory §P1-11.7 row rather than adding beside it (`R7`), and adds §P1-11.4 step 3, §P1-9.4 `S-4`, the §P1-9.2 Termination ¶, §P1-13.1, §P1-13.2 row 4, §P1-13.7 and invariant 61 — every one of which v1's handoff omitted. §7.2 also records the two sites checked and confirmed **not** to need amendment (invariants 60 and 65), so the audit is closed in both directions. |
| **F2** `PEER_EOF` is not unique to death; `MSG_EOR` is never inspected; the half-close route is unaddressed | must fix | **CLOSED**, at Y's stricter framing | v2 §5.2 **withdraws** "kernel fact, not a report" and "the two EOFs are the same kernel event" verbatim, and withdraws the state name `SUPERVISOR_LOST`. `E-1a`/`E-1b`/`E-1c` make `MSG_EOR` the exact discriminator: a zero-length receive **with** `MSG_EOR` is a genuine empty record, is `REQUEST_MALFORMED`/`TRANSPORT_STRUCTURAL`, and **never fires the freeze**. `E-2` names four indistinguishable causes — exit, crash, orderly close, half-close — and §5.3 gives them one identical continuation, which is why the conflation is fail-safe. v2 additionally discloses what X's repair implies and X did not name: **`_MSG_EOR` is not in the PCS's pinned integer-constant set** (composite `:419-423`), so the discrimination requires a one-name extension of the §P1-3.4 binding block, now counted in W-B's blast radius (§9.1, §12.2 item 12). |
| **F3** the `ABSENT` route is presented as unconditionally available; the fallback still needs numeric identity the P1 supervisor cannot express | should fix | **CLOSED**, constructively | §0.2 `D-1` records that X asked for a **framing** repair and Y for a **constructive** one, and that v2 takes Y. §6 amends the fallback schema (`A-ABS-1`..`A-ABS-6`), names every reopened sentence (§6.3), and adds a dedicated common token. X's framing point is **also** stated at §6.6 — "independent" always meant "adds no new dependency", and the defect was pre-existing and non-differentiating — but v2 says plainly that a pre-existing defect on the load-bearing settlement path of both options is still a defect this packet must not ship over. |

### 3.2 Y line — `reviews/sol_officina_p1_watchdog_freeze_choice_review.md`

| Finding | Class | Status | Repair, and where |
|---|---|---|---|
| **Y-C1** the common freeze scope is neither a constructible "leased" scope nor total over the signed handle model; the per-handle continuation is incomplete | Critical | **CLOSED** | v2 §3 is a new section replacing v1 §3.4 entirely. §3.1 **withdraws** the v1 `SCOPE` block and every `table_seq`/lease reference verbatim, on Y's four verified counts. §2's rejected-family table gains a new row rejecting the supervisor-to-PCS lease-publication opcode Y named as the alternative, with its authority cost (`R-L4`, §P1-13.0). §3.5 defines the scope solely from P1-owned state — current-generation `CONTROLLER`/`WORKER` handles, `OWNED`, unreaped, non-null `pgid_or_null`, KV-verified — with a **total** inclusion/exclusion table over every signed `state` and `ownership` value, including `STOPPED` which v1 omitted, and a **benign / non-benign / structural** classification for every exclusion. §3.4 pins the kernel verification `KV-1`..`KV-6`, re-evaluated **before every** `_killpg` and never cached, with `KV-6` forbidding the PCS's own group, the watchdog's group and the supervisor's group. §3.3 pins `pgid_or_null`'s population (`P-1`..`P-3`), which **v1.2 never defined** — §3.2 discloses that gap. §3.5 `SC-3` deduplicates before signalling and asserts the collapse count is zero. §3.6 gives a **closed sixteen-token** per-group result set covering identity, signal, `/proc`, enumeration, quiescence, timeout, denial, structural error and exception, reusing §P1-10.5's signed six-way `_killpg` classifier verbatim. §3.7 gives one durable continuation per token. §3.8 gives exactly three terminals with `FREEZE_TOTAL_PROVED` the only valid one. §3.9 states invalidity dominance: an executed freeze **always** yields whole-generation `PROCESS` invalidity with full charge, never a completion, resource success, witness evidence, qualification, Q/C or science. |
| **Y-C2** W-A is not a one-request capability; the sequence key authorizes repeated fresh freezes, and the pricing is false | Critical | **CLOSED** | v2 §4.2 **withdraws** `request_seq` and `table_seq` verbatim with Y's reason. The repaired grammar has four fields, is a **constant byte string** per generation, and the journal key is the constant `(generation_id, "WDFREEZE", watchdog_handle_id)` — the handle id supplied by the PCS from its own table, never sent by the watchdog. **Exactly one accepted action**; every duplicate, replay, refusal, wrong generation, wrong opcode or post-terminal record performs **no syscall**. §4.3 answers Y's "specify whether invocation is permitted before endpoint loss" with **it is not**, and gives the mechanically verifiable PCS-side gate `G-1`..`G-4`: the gate is the PCS's own observation on its own descriptor, not watchdog prose, and its fixture is stated. §4.6 `P-1`..`P-4` prices it anyway, as Y requires: the one authorized action **forces** whole-generation `PROCESS` invalidity and full charge; under the gate the marginal price is zero because the generation is already terminal; without the gate the price would be real, and v2 says so for a reviewer who rejects `G-1`. §5.7 of v1's "one freeze per generation, denial only" is withdrawn at §0.3 `W-3`. |
| **Y-C3** orthogonality from the identity cell fails at the `ABSENT` fallback | Critical | **CLOSED** | v2 §6 **withdraws** "routes exactly where the signed chain already routes one" and the unproved four-way table. `A-ABS-1` makes `pgid_or_null` and `start_identity_or_null` null **if and only if** `rejection_conjunct == 0`, as a biconditional validity conjunct in both directions. `A-ABS-3` forces `supervisor_quiescence = UNKNOWN` on that branch, derived from §Z4.6 conjunct 10 (a group that cannot be named cannot be proved quiescent). `A-ABS-4` forbids synthesizing any instant, overrun, identity, member count or freeze-success. `A-ABS-5` keeps §N5.3's routing, the unknowable pool and full charging verbatim. §6.3 enumerates the exact reopened sentences — **one contract file, three keys, one branch** — and confirms the id preimage, the routing, §N5.4 and §Z4.6 conjunct 10 are untouched. §6.4 adds the dedicated common token `P1_FREEZE_ABSENT_FALLBACK_NULLABLE_IDENTITY_V1`, **required under either option**. §6.5 states the separation exactly: the freeze-executor choice is decided by `S-12`, the sole-caller sentence, the missing endpoint and the missing relay — none a numeric-identity question — while this repaired fallback is what makes settlement constructible under either identity outcome. §9.5's coexistence table is now a **consequence** of `A-ABS-1` rather than an assertion. |
| **Y-M1** `PEER_EOF` proves endpoint loss, not death; the two EOFs are not one event | Major | **CLOSED** | §5.2 as under X F2, at Y's framing: `PEER_CONTROL_ENDPOINT_LOST` replaces `SUPERVISOR_LOST` **everywhere** and the name appears nowhere in v2; `E-2` states that the event proves only that no further authorized peer request can arrive; `E-4` states that the protocol socket and the update pipe are two independent descriptors losable in either order, and that v2 asserts no ordering, simultaneity or causal identity — the absence of a race follows from **independence**, not identity. §5.4's "which process establishes what" table gains a **"not established"** column. The selection token is renamed to `…_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS` (§11). §8 `L7` carries the wording. |
| **Y-M2** W-B journals only after its side effect | Major | **CLOSED** | §5.5 **withdraws** v1's `E-3`-then-`E-4` ordering with Y's reason (a live denied/structural/enumeration failure after some groups were stopped left no durable marker). The repaired ordering is `R1` validate, `R2` stale-head/state check **before any side effect**, `R3` append `ACCEPTED` + fsync under the constant key, `R4` run the §3 classifier, `R5` append `COMPLETED` + fsync **only** on `FREEZE_TOTAL_PROVED` and `TERMINAL_INVALID` otherwise, `R6` enter the non-returning reaper state. `R2` routes an existing `ACCEPTED` to inconclusive `PROCESS` invalidity with **no second freeze and no syscall**. §5.6 is a thirteen-row deterministic matrix keyed to the last durable marker, covering every crash cut, live failure, replay, restart, malformed record, stale generation, watchdog state, simultaneous loss and the §3.10 group escape. Partial side effects are stated explicitly: signalled groups stay signalled, nothing un-stops them, and a partial freeze is never a completion. |
| **Y-M3** W-A lacks an ordering contract with the existing PCS `PEER_EOF` terminal | Major | **CLOSED** | §4.5 `T-1`..`T-7`. `T-2` defines a bounded service window from the endpoint-loss instant, 60 s, polling only the watchdog socket, during which no handle is created, released or reaped. `T-3` ends it deterministically on the first of: one accepted record and its terminal; watchdog-socket EOF; `REAPED_POSITIVE` on the watchdog handle; or the bound — and in the last three **no freeze occurs and none is inferred**. `T-4` places the non-returning reaper transition **after** the window by definition, so it can never "win first"; a later record is `REFUSED` with `GENERATION_TERMINAL`. `T-5` stale generation, `T-6` PCS restart (`GENERATION_NOT_ADOPTABLE`, never adopts, never repeats an `ACCEPTED` action), `T-7` simultaneous endpoint loss and watchdog death. §9.4 states the governance cost Y identified, and adds the one v2 found: the gate makes W-A's initiative largely redundant with a fact the PCS already holds. |
| **Y-m1** the publication caveat uses the overclaimed death semantics | Minor | **CLOSED** | §8 splits `L6` into `L6`–`L9` with Y's three mandated sentences: `L7` endpoint loss is not proof of supervisor death and actual freeze occurrence may remain unknown; `L8` no process-control journal fact is peer freeze evidence; `L9` `ABSENT` means evidence unavailable even if some or all groups were stopped. `ND-1`..`ND-3` state the closed prohibition that no qualification, comparison, Q/C, Proof, capacity, custody, spend, selection, blinding or scientific datum may distinguish a `COMPLETED` PCS freeze journal from any other `ABSENT` case, and that no freeze terminal is exposed to them. `ND-4` adopts Y's correction to the packet's own overclaim: full charging **is** a deterministic resource-accounting consequence, so v1's "never a resource outcome" was too broad; what is true is that it is never a resource **success**, never a capacity fact, and never a result-dependent quantity. |

### 3.3 Y's eight required determinations

| # | Determination | v2 status |
|---|---|---|
| 1 | the blocker is real and separate from the identity cell; Y-C3 is a defect in the fallback representation, not a merger of the two cells | **Adopted.** §1 (four mechanisms, both lines concurring); §6.5 states the separation in exactly those terms. |
| 2 | a genuinely constant one-shot target-free capability could preserve PCS authority; the sequence-keyed channel did not | **Implemented.** §4.2 constant key, §4.3 gate, §4.6 pricing. |
| 3 | after Y-C1/Y-M1/Y-M2 are repaired, PCS action on endpoint loss is narrow, pre-outcome, once-per-generation and mechanically bounded; the token is a real C1 role replacement | **Adopted.** §5.7, §5.8, and §7 which shows the replacement spans twelve sites, not two. |
| 4 | neither successful signalling nor a PCS journal timestamp is scientific evidence; `ABSENT` never means freeze success | **Implemented.** §3.9 `S-4`, §8 `L8`/`L9`, `ND-1`..`ND-3`, `A-ABS-4`. |
| 5 | the recommendation basis is authority, surface, testability and liveness only; "never a resource interpretation" was too broad | **Adopted.** §10's criteria are signed-authority fidelity, constructibility, mechanical testability, liveness and blast radius. `ND-4` corrects the overclaim. |
| 6 | the failure matrix: PCS death, simultaneous death and incomplete freeze remain whole-generation invalidity; restart may not adopt or repeat; replays perform no syscall; half-close is endpoint loss, not death | **Implemented.** §5.6 (W-B), §4.5 `T-1`..`T-7` (W-A), §3.7/§3.8/§3.9 (shared). |
| 7 | W-B does not change who may call `killpg`; treating endpoint loss as a fail-closed process fact preserves the A3 line | **Preserved.** §13 `N-3`; `S-12` retained unchanged under both options; §3's classifier executes in the PCS root only. |
| 8 | corrected `L6` must cover both death and endpoint loss and state that freeze occurrence and peer evidence are independently unavailable | **Implemented.** §8 `L6`–`L9`. |

### 3.4 Findings v2 opened on itself

```text
None creates a new author cell. Four are disclosed inside the packet:

O-1  §3.2 — v1.2 NEVER POPULATES pgid_or_null and never defines "a
     kernel-verified group" for a role handle. The key appears exactly once in
     the composite, at :1260, in the handle-table shape. This is a pre-existing
     v1.2 gap that Y-C1 exposed; §3.4 fills it with P-1..P-3 and KV-1..KV-6,
     using only already-bound primitives.

O-2  §3.6 — §W3.3's quiescence pass interval is
     T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS = 100_000_000, but the composite
     states at :267-268 that "A value of 100_000_000 appears in no rule of this
     contract." Importing it would contradict a signed sentence. v2 reuses
     T_SUPERVISOR_POLL_INTERVAL_NS = 50_000_000 with sixteen passes, preserving
     §W3.3's 800 ms total budget and adding no new nanosecond numeral, at the
     cost of one new count constant. Disclosed rather than silently deviating.

O-3  §5.2 — _MSG_EOR is not in the PCS's pinned integer-constant set
     (composite :419-423). X F2's repair therefore requires a one-name
     extension of the §P1-3.4 binding block. Neither review named this.
     Counted in W-B's blast radius.

O-4  §3.10 — TARGET-INDUCED GROUP ESCAPE. A controller or worker target runs
     after SIGCONT and may call setsid()/setpgid(); KV-5 then fails with
     GROUP_CHANGED, no signal is sent, and the tree keeps running. This is
     fail-closed and correct, but it is a real residual that neither option
     removes, and the activation protocol's "process group is immutable while
     open" (:300-305) is a lease declaration, not kernel enforcement. Covered
     by L7 and L9; not a new cell.
```

---

## 4. Corrected W-A / W-B comparison

| Dimension | **W-A**, repaired | **W-B**, repaired |
|---|---|---|
| **topology / opcode P1 changes** | socketpair; slot 6 reopened; `(CLOSE,6)` removed; `A-5` extended with the slot-6 type; leak proof re-proved; one persistent non-handle PCS descriptor; one request grammar; one reply grammar; one dispatch path; one gate; one service window | **zero** |
| **normative P1 prose changes** | **twelve** (§7.2) | **twelve** (§7.2) — v1's "zero" is withdrawn |
| shared classifier (§3) | required in full | **identical** |
| peer contracts reopened | **one** — §N5's fallback schema, three keys, one branch | **one** — identical |
| binding-block change | none | `_MSG_EOR` added to the pinned constants |
| new constants | `T_PCS_QUIESCE_MAX_PASSES = 16` (shared) | identical |
| watchdog capability | one gated single-opcode target-free socket | **strictly reduced to zero** |
| autonomous PCS action | no — but its gate is the PCS's own endpoint-loss fact | **yes**, the one new thing |
| one-shot guarantee | constant key per `(generation, watchdog_handle)`; exactly one accepted action; every other record no-syscall | constant key `(generation,"PEEREOF",1)`; naturally singular |
| gate / trigger | `G-1`: the PCS's own `PEER_CONTROL_ENDPOINT_LOST`, mechanically verifiable | `E-1a`: the same PCS-side fact, with `MSG_EOR` discrimination |
| forced-invalidity channel | **closed** by `G-1`; priced anyway at `P-1`..`P-4` | none — the trigger is not requestable |
| liveness dependency | **new**: a dead or wedged watchdog denies the freeze | **none new**: depends on the PCS, which D1 already makes total |
| ordering surface | a 60 s service window ordered against the non-returning reaper (`T-1`..`T-7`) | none — record-first, then the reaper state |
| verifier rules added | one-opcode dispatch, target-free grammar, `G-1` gate, plus the shared classifier rules | autonomous path reachable only from `E-1a`, plus the shared classifier rules |
| **`S-12` retained unchanged** | **yes** | **yes** |

**What the repairs changed, stated honestly.** W-B's headline is weaker than v1
claimed: it amends twelve normative P1 sentences, not zero. Both options now
reopen a peer contract, where v1 said neither did. Both now carry §3, which v1
hid behind an eight-line scope block that did not work. W-A improved in one
respect (the gate closes Y-C2's channel) and worsened in another (§9.4: the same
gate makes its initiative largely redundant). **The rows that decide did not
move**, and §3, §6 and §7 fall identically on both options and therefore cannot
separate them.

---

## 5. Deterministic failure and crash matrix — where each row lives

| Class | W-A | W-B |
|---|---|---|
| per-group identity / signal / `/proc` / enumeration / quiescence / exception | §3.6, §3.7 — sixteen closed tokens, one continuation each | identical |
| scope exclusions, benign vs non-benign vs structural | §3.5 table | identical |
| classifier terminals and their settlement | §3.8, §3.9 | identical |
| record-first ordering and its cuts | §4.6 `A1`..`A5` | §5.5 `R1`..`R6`, §5.6 thirteen rows |
| trigger malformation (`MSG_EOR`) | inherits §5.2 via the `G-1` gate | §5.2 `E-1b`, §5.6 |
| ordering vs the non-returning reaper | §4.5 `T-1`..`T-7` | §5.3 step 4, §5.5 `R6` |
| watchdog death / socket EOF / timeout | §4.5 `T-3(b)(c)(d)` | §5.6 — no effect at any step |
| stale generation | §4.5 `T-5` | §5.6 |
| PCS restart / adoption | §4.5 `T-6` | §5.6 |
| simultaneous endpoint loss and watchdog death | §4.5 `T-7` | §5.6 |
| PCS death at every boundary | §4.6 + §3.9 `S-3` | §5.6 rows 1–6 |
| target-induced group escape | §3.10 | identical |

**Every row terminates in exactly one of:** whole-generation `PROCESS`
invalidity with full charge (the overwhelming majority), a no-syscall replay, or
a no-action refusal. **No row terminates in a completion, a resource success, a
capacity fact, a custody disposition, a qualification input, a Q/C fact or a
scientific outcome.**

---

## 6. Invariants confirmed preserved

| Invariant | Where v2 keeps it |
|---|---|
| the blocker remains proved | §1, four mechanisms, both lines concurring; `N-1` |
| the PCS never retains the watchdog update-pipe write end | §1.5 corollary, `N-2`; §P1-8.7 `:1398` untouched; W-A's slot-6 socket is a **separate** socketpair, as the X line verified |
| the PCS remains the sole caller of signal/process-control primitives | `N-3`; `S-12` retained unchanged under both options; §3's classifier executes in the PCS root only |
| W-B may remain recommended if the corrected comparison supports it | §10 — it does, on the rows that did not move; **no option is selected** |
| the identity choice is not selected or repaired here | §6.5, `N-5` |
| `T = NOT_ACTIVATED`; programme claim `OPEN` | §14, `N-6`, and this closure |

---

## 7. Verdict and recommendation after repair

```text
READY_FOR_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2_XY_CONFIRMATION
```

**Meaning precisely.** All ten findings of the two binding defect reports are
dispositioned one-to-one at §3, each by a named repair at a named locus, with
seven v1 sentences withdrawn verbatim rather than paraphrased away. Where the
lines differed, §0.2 records the difference and the stricter rule taken. The
packet is a self-contained replacement.

**Recommendation after repair: W-B**, on signed-authority fidelity,
constructibility, mechanical testability, liveness and blast radius only. Both
review lines independently reached the same recommendation after their own
repairs. **The author selects nothing and predicts no outcome.**

**It does not mean the packet is correct.** This is an author self-assessment by
the party that wrote the defects being repaired.

---

## 8. One bounded confirmation question per reviewer

### For the X line — one question, yes or no

> **Is the §3 classifier mechanically executable by the PCS as written — the
> `STAT_OBSERVE_G` parse extension, the `KV-1`..`KV-6` verification, the
> `pgid_or_null` population rule `P-1`..`P-3`, the sixteen-token per-group set
> and the `/proc` enumeration — using only primitives already bound in the
> composite's §P1-3.4 block plus the single disclosed `_MSG_EOR` addition, with
> no further primitive, import, constant or module required?**

Answer `YES` or `NO`. A `NO` should name the primitive, constant or import the
classifier needs and v2 did not disclose.

### For the Y line — one question, yes or no

> **Do the §6 `A-ABS-1`..`A-ABS-6` amendments make the `EVIDENCE_ABSENT`
> settlement fully constructible without any numeric process identity, under
> either outcome of `AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS`, while
> reopening no signed sentence beyond the three keys and one branch enumerated
> at §6.3 and preserving §N5.3's routing, the unknowable pool and full charging
> unchanged?**

Answer `YES` or `NO`. A `NO` should name the field that remains unconstructible
on the `rejection_conjunct == 0` branch, or the signed sentence §6.3 failed to
list.

Both lines should also confirm, as part of the same bounded round, that the
remaining eight findings are closed as dispositioned at §3, that the §7 twelve-site
audit is complete against the whole composite, and that the §4 comparison is
exact.

---

## 9. Weakest points in v2, stated by the author

1. **§3 is large and is mine.** No signed document contains a PCS-side freeze
   classifier. `KV`, the sixteen-token set, the benign/non-benign exclusion
   classification and the three terminals are author constructions built to
   Y-C1's specification. If any of them is wrong, both options inherit the
   error equally.
2. **`STAT_OBSERVE_G`'s field indices are asserted from the Linux `/proc/<pid>/stat`
   layout**, not from any document in this chain. I read the offsets as
   `state, ppid, pgrp, session` at tokens 1–4 after the final `)`, consistent
   with §P1-10.3's existing "20th token after the final `)`" for start time. A
   reviewer should check the indices.
3. **`A-ABS-2` goes beyond Y's literal text.** Nulling
   `current_unresolved_member_count` was my addition, derived from the fact
   that an unnamed group has no computable member count. If a reviewer holds
   that Y's amendment should be exactly two keys, that field is left
   unconstructible and the amendment is incomplete rather than over-wide.
4. **§3.6's pass-interval substitution changes §W3.3's literal constants.** I
   preserved the 800 ms budget and avoided contradicting the composite's
   "100_000_000 appears in no rule" sentence, but §W3.3 is a signed procedure
   and I did not run its quiescence semantics past its own authority.
5. **§4.3's gate is the single most consequential author choice in v2.** It
   closes Y-C2's channel completely, and it also substantially undercuts W-A's
   rationale (§9.4). I chose it because Y offered gate-or-pricing and the gate
   is strictly safer, but it is not outcome-neutral for the comparison, and I
   have said so in the packet rather than letting it operate silently.
6. **I did not audit the whole peer chain** for other consumers that assume a
   watchdog-written witness exists. §7 audits the composite exhaustively; §N5
   and §Z4.6 were read directly; the rest of the harness and settlement chain
   was searched by key name only.
7. **§3.10's residual is real and unpriced.** A target that calls `setsid()`
   escapes the freeze entirely under both options. It is fail-closed and
   covered by `L7`/`L9`, but I did not investigate whether any signed route
   assumed it could not happen.

---

## 10. The exact residual author choices

```text
RESIDUAL CHOICE 1 — the cell AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM.
  Exactly one of:
    I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
    I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
  Both are selectable after this repair. The W-B token is RENAMED from v1's
  …_B_PCS_FREEZES_ON_PEER_EOF, because PEER_EOF carried the death claim Y-M1
  required withdrawn.

RESIDUAL CHOICE 2 — the per-option amendment, conditional on choice 1:
    P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1        with W-A only
    P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1          with W-B only

RESIDUAL CHOICE 3 — four COMMON amendments, required under EITHER selection.
  These are not separate choices from choice 1; they are the price of any
  selection, and a selection without them leaves an unimplementable path:
    P1_FREEZE_ABSENT_FALLBACK_NULLABLE_IDENTITY_V1   §6
    P1_PCS_FREEZE_CLASSIFIER_V1                      §3
    P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1         §7
    P1_FREEZE_PUBLICATION_L6_L9_V1                   §8

NONE IS SIGNABLE UNTIL THE BOUNDED X/Y CONFIRMATION ROUND CONFIRMS v2 ON
IDENTICAL BYTES.

NOT A CHOICE IN THIS PACKET, AND NOT OPENED BY IT:
  AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS — neither selected nor repaired
  here. §6 makes this cell's settlement constructible under EITHER of its
  outcomes; it does not touch the cell itself.
```

---

## 11. Negative authorization — explicit

This closure and the v2 packet authorize **nothing**. In particular:

```text
NO SELECTION. Neither W-A nor W-B is selected, recommended into effect, or
   treated as selected. No selection token is minted, accepted, signed, or made
   signable by this round.
NO AMENDMENT ACCEPTED. All six amendment tokens exist only as proposed text in
   a draft packet. A-ABS is a PROPOSAL; §N5 is unamended on disk.
NO X/Y VERDICT. The first line of this file is an author readiness claim, not
   an X-line or Y-line verdict, and not a signature.
NO IMPLEMENTATION. No code, test, verifier rule, manifest entry or schema was
   written, edited, or executed. The §3 classifier, KV, STAT_OBSERVE_G, the
   S-rules and every test row are specification text, not artifacts.
NO ACTIVATION. T remains NOT_ACTIVATED. No activation record, claim, lease,
   process record, review record, freeze observation, fallback observation or
   invalidity record was created or read for effect.
NO PROCESS EXECUTION. No fork, exec, posix_spawn, kill, killpg, signal, wait,
   prctl, socket, socketpair, pipe or lock operation was performed. No PCS,
   supervisor, controller, worker, middle or watchdog was created or contacted.
   No process was frozen, stopped, signalled, enumerated or observed. No /proc
   read was performed against any live process. No behavioural probe was run.
NO SPEND. No E1, E2 or E3 resource was reserved, charged or released. No
   capacity artifact, custody disposition, liability or ledger entry was
   created or moved. The full-charge consequences described in §3.9 and §6 are
   SPECIFICATIONS OF A FUTURE ROUTE, not charges taken.
NO DATUM, NO OUTCOME, NO PROOF. No scientific datum, observation, qualification,
   comparison, blinding claim, Q or C fact, entropy draw, world, learner or
   result manifest was produced, predicted, or optimized toward.
NO CLAIM MOVEMENT. The programme claim remains OPEN.
NO FILE MODIFIED. Exactly two files were created. v1, the v1 closure and both
   review files are byte-untouched, as §2.1 demonstrates.
NO IDENTITY-CELL MOVEMENT. AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS is
   untouched, unselected and unrepaired by this round.
```

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
READY_FOR_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2_XY_CONFIRMATION
```
