READY_FOR_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_XY_REVIEW

# Author closure — P1 watchdog-freeze mechanism choice packet v1

**Author:** Claude Code Opus 5, **specification author only**. I authored the
whole supervisor/control-channel chain, v1 through v1.2, the identity packet
that reported this blocker, and this packet. I am therefore **disqualified** as
its independent X-line or Y-line reviewer, and **this closure is an untrusted
author self-assessment** — as is the identity packet whose §6 report this round
was told to treat as untrusted and re-derive.

**No choice was accepted and no token was accepted.** Both selection tokens and
both amendment tokens exist only as text in a draft packet awaiting bounded
independent review.

`T = NOT_ACTIVATED`; programme claim `OPEN`. This round authorized no selection,
X/Y verdict, implementation, activation, entropy, resource spend, T/Q/C datum,
outcome, Proof or claim movement.

---

## 1. Deliverables and untouched-file confirmation

Exactly two new files. **No existing file was modified.**

| Path | Lines |
|---|---|
| `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V1_DRAFT.md` | 616 |
| `reviews/opus5_officina_p1_watchdog_freeze_author_choice_packet.md` | this file |

Only read-only commands were run: `grep`, `sed`, `wc`, `cat`, `sha256sum`. No
test, behavioural probe or process-control operation was executed.

## 2. Hashes and custody

```text
15937b84b2e2a61de3d908ea014cbded902ca5ba15f58b988920c99be0702f09  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
```

Governing inputs, previously pinned and re-confirmed byte-intact this round:

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/…P1_OPERATIVE_COMPOSITE_V1_2.md
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
ad8b5791f043f201c00812a11de2ab3b765664e65e6d0ebf9778e150913096d3  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
```

Custody is acyclic: the packet contains none of its own digests; packet → this
closure → X/Y review → any future signature.

**Evidence locations used for the proof:** §W3.3 freeze procedure,
`…V2_1_CORRECTION.md:744-770`; §W3.5 watchdog failure table, same file `:825-836`;
`S-12`, v1.2 line 2601; watchdog slot map and the explicit slot-6 closure, v1.2
§P1-6.2 and §P1-6.4; PCS as sole caller of the process primitives,
`…V2_1_10_4_P1_BINDING.md:150-153`; the binding's freeze assertion,
`…V2_1_10_4_P1_BINDING.md:627-633`; descriptor ownership after the
`SCM_RIGHTS` send, v1.2 §P1-8.7; §N5 fallback and the `ABSENT` sentinel,
`…V2_1_2_CORRECTION.md:833-871`, `:911-920`.

---

## 3. Independent blocker proof

The identity packet's §6 report was treated as untrusted and re-derived.
**The blocker is confirmed, and it is stronger than the report stated.** The
report gave two mechanisms; there are four, and the two strongest were not among
them.

**What a freeze mechanically requires** (§W3.3, to which the P1 binding routes
verbatim): a numeric pgid, the `killpg` syscall, `/proc` enumeration, and a
write under the runtime root.

| # | Mechanism | Status |
|---|---|---|
| 1 | **`S-12` of the selected composite** — "subprocess, Popen, fork, waitpid, kill, killpg and system appear on no path of `generic_harness.py`". The watchdog's role entry is in that file: `A-10` imports it as the only import and `A-13` calls one pinned entry function from it. **The verifier of the selected architecture forbids the watchdog from freezing.** | **dispositive on its own**; not in the report |
| 2 | **The signed sole-caller sentence** — the PCS "is the sole caller of `fork`, `posix_spawn`, `kill`, `killpg` and every `wait`-family primitive". A watchdog `killpg` contradicts the selection directly. | dispositive on its own; not in the report |
| 3 | **No endpoint** — watchdog slot set `{3,4,5,7,8,9,10}`, slot 6 "not used; explicitly closed by a file action", and no runtime-root descriptor. | as reported |
| 4 | **No relay at the only moment it matters** — the trigger *is* the supervisor's death, and §P1-8.7 has the PCS close its copies of the supervisor's ends, so the PCS has no channel to the watchdog either. | as reported |

**Verdict: PROVED.** Update-pipe EOF is observable; no specified route can
execute the freeze.

### 3.1 A load-bearing corollary the report did not contain

**The PCS must never retain a write end on the watchdog update pipe.** If it
did, that pipe would not reach EOF when the supervisor dies — and update-pipe
EOF is the **single remaining supervisor-death detector** under P1, the
`getppid()` detector having been deliberately deleted. Any design that gives the
PCS a channel to the watchdog by retaining that write end destroys C1's only
detector. This constrains the whole option space and rules out the most obvious
naive repair.

### 3.2 The numeric half, and why it does not contaminate this cell

Even granting a signal mechanism, §W3.3 needs a numeric pgid and the witness
record requires `process_id`, `pgid` and `start_identity` — the same root cause
as `AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS`. **Both options are therefore
specified so that no numeric peer witness is written**: each routes the absent
witness through §N5's already-signed `ABSENT` sentinel. That is what keeps this
cell independent of the identity cell (§5).

---

## 4. Complete option table

| Dimension | W-A — watchdog requests, PCS executes | W-B — PCS freezes on `PEER_EOF` |
|---|---|---|
| endpoint / slot | `SOCK_SEQPACKET` socketpair; watchdog slot 6 reopened; `(CLOSE, 6)` removed from the `WATCHDOG` file actions | **none added** |
| descriptor topology | slot set becomes `{3,4,5,6,7,8,9,10}`; `A-5` assertion updated | **byte-unchanged** |
| leak proof | re-proved: PCS end is `_socketpair`-created hence `FD_CLOEXEC`; watchdog end arrives by `DUP2`; point-to-point so no third joiner | **§P1-6.4 stands byte-unchanged** |
| request grammar | six fields; opcode drawn from a **one-element** set; **no target field of any kind** | n/a |
| why no arbitrary target | the request names nothing; scope is computed from PCS-side handle state alone | n/a |
| why no other opcode | one-element opcode set; separate dispatch path not connected to the `t-pcs.v1` handler | n/a |
| generation/handle binding | generation must match; `table_seq` must be one the PCS published; **no handle is ever named by the watchdog** | scope is the PCS's own handle table |
| ack / reply | the reply record is the ack; receipt only — counts, no pid, pgid, handle or path | none needed |
| timeout | `T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS`, then write nothing and exit; **never retried** | n/a |
| replay / idempotency | journalled before acting; repeat key ⇒ `REPLAYED`, no syscall | key is constant per generation ⇒ naturally singular |
| PCS action & scope | live `CONTROLLER`/`WORKER` handles, `OWNED`, ascending handle id; `SIGSTOP`, quiescence passes, `SIGKILL` after the first failed pass; never the supervisor's group, never a watchdog handle | identical scope and steps |
| journal key | `(generation_id, "WDFREEZE", request_seq)` | `(generation_id, "PEEREOF", 1)` |
| crash cuts | seven, incl. watchdog-dies-before-sending ⇒ **no freeze at all** | six races, incl. PCS-dies-before-`E-1` ⇒ no freeze; **watchdog death has no effect** |
| who proves what | watchdog proves the decision; PCS proves the stop | PCS proves both; watchdog proves only that the supervisor is gone |
| witness | **none written**; `ABSENT` route | **none written**; `ABSENT` route |
| first/replacement symmetry | preserved — same socket from the same `SPAWN_WATCHDOG` | preserved trivially — no watchdog role in freezing |
| P1 sentences amended | "holds no capability", "two sealed pipes", `A-5` slot set | **none** |
| C1 sentences amended | executor and witness roles; decider role retained | freezer and witness roles; watchdog becomes a liveness sensor |
| peer contracts reopened | **none** | **none** |
| autonomous PCS action | no | **yes — the one new thing**, bounded by a kernel-fact trigger, pre-existing scope, once per generation |
| A3 liveness residual | **new** dependency: a `SIGSTOP`ped watchdog denies the freeze forever | not new: depends on the PCS, which D1 already makes total |
| token | `P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1` | `P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1` |

**Rejected families**, each with its reason in packet §2: watchdog PID
knowledge; watchdog signal syscalls; a general PCS client; a post-mortem
supervisor relay; a PCS write end on the update pipe (inadmissible, §3.1); and
terminate-instead-of-freeze, which deletes signed C1 rather than implementing it
and destroys the `freeze_ns` evidence §W3.4 consumes.

---

## 5. Separation from the identity cell

**Both options are independent of `AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS`,
and neither choice is conditioned on its outcome.** Both avoid a numeric peer
witness by routing through §N5's signed `ABSENT` sentinel, so neither needs a
pgid in the watchdog or the supervisor.

**Can the two selected repairs coexist?** Yes — all four combinations
(W-A or W-B) × (identity A or identity B) are compatible, with no interaction at
any step. The identity outcome does not change which of W-A or W-B is better on
any criterion in the table above.

One forward-looking note, stated so it is not mistaken for a dependency: if
identity Option A is later signed, the peer layer could in principle publish
numeric lease rows, which would make a watchdog-written numeric witness
constructible again. That would be a **new cell**; it is not proposed, and
neither option here assumes it.

---

## 6. Recommendation

On the three stated criteria only — signed-authority fidelity, mechanical
testability, minimal reopened contracts:

> **W-B.**

W-B amends **zero** P1 sentences, adds **zero** descriptors, opcodes and
capabilities, leaves the §P1-6.4 descriptor leak proof byte-unchanged, and
*strengthens* the watchdog's no-capability property. W-A amends three P1
sentences, reopens the leak proof, adds a socket, a grammar, a dispatch path, a
replay rule and a timeout, and makes the freeze contingent on a live watchdog —
a **new** liveness dependency on a process whose death is itself one of the
conditions C1 exists to handle. Neither reopens a peer contract.

W-B's single genuine cost is that the PCS acts without a request for the first
time in this architecture. That is bounded by a kernel-fact trigger, a
pre-existing handle scope, and a once-per-generation journal key — and the
packet names it as new initiative rather than as a routine extension.

W-B's honest loss: the watchdog stops being the freezer and the witness of
record, keeping only its liveness-sensor role. That is a real C1 change and it
carries its own token.

**Recommendation on stated criteria only. The author selects nothing and
predicts no outcome.**

---

## 7. Tokens

Mutually exclusive; **none signable until bounded X/Y review confirms the packet
on identical bytes**:

```text
I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_EOF
```

Plus, per selection: `P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1` (W-A) or
`P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1` (W-B). Both additionally require the
`L6` publication wording: *that a freeze occurs, or that freeze evidence becomes
available, after supervisor death, is not guaranteed.*

Deterministic v1.3 handoffs for each selection are in packet §8, itemized
section by section.

---

## 8. Bounded questions

### Three for the X line

1. **Is the `S-12` argument airtight?** `S-12` forbids `killpg` in
   `generic_harness.py`, and I claim the watchdog role entry lives there via
   `A-10`/`A-13`. Could a conforming build place the watchdog entry elsewhere —
   in the role bootstrap root, whose allowlist is `{os, sys, fcntl}` — and
   thereby freeze without violating `S-12`?
2. **Is W-B's `PEER_EOF` detection unambiguous?** Is a zero-length
   `SOCK_SEQPACKET` record with no ancillary data distinguishable, at the
   `_recvmsg` boundary, from a legitimate empty message, and can a hostile
   supervisor induce a false `PEER_EOF` before dying?
3. **Is W-A's capability genuinely non-general?** The request names no target
   and carries one opcode. Can a compromised watchdog obtain anything beyond
   one freeze per generation — through `request_seq` growth, `table_seq`
   choice, or timing against `SPAWN_ROLE`?

### Three for the Y line

1. **Does W-B still satisfy signed C1 in the scientifically meaningful sense**,
   or does "dedicated freezer watchdog" name the *executor* such that a
   sensor-only watchdog requires a fresh C1 selection rather than an amendment?
2. **Is routing every supervisor-death generation through the `ABSENT` sentinel
   sound**, or does making the always-taken path what §N5 designed as an
   exception change the meaning of the `UNKNOWN` route and its charging?
3. **Is the first autonomous PCS action acceptable governance?** Every PCS
   action today is request-driven; W-B's is not. Is a kernel-fact trigger with
   a pre-existing scope sufficient, or does unrequested authority require its
   own signature?

---

## 9. Weakest points

1. **§3.1's corollary is mine**, not any signed document's, and it eliminates a
   whole family of repairs. If it is wrong, the option space is larger.
2. **The `ABSENT`-route reuse is the load-bearing move in both options.** I
   verified §N5.1 admits a null rejected-witness path and §N5.3 routes it, but I
   did not audit every consumer of that route for an assumption that it is rare.
3. **W-B's `E-3` reuses §W3.3's quiescence passes over the PCS's own member
   set.** Whether the PCS's recorded member set equals the set §W3.3 intends —
   which reaches processes by session and parent chain — is asserted, not
   proved.
4. **`T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS` is reused as W-A's reply timeout**
   without deriving that it is the right bound; it is the only existing constant
   of the right class, and inventing one would have been an author choice.
5. **I did not audit the whole peer chain** for other places that assume a
   watchdog-written witness exists.

---

## 10. Confirmation and verdict

**No choice was accepted. No token was accepted. No token is signable.** No
existing file was modified; only the two new files exist. `T` remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.

```text
READY_FOR_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_XY_REVIEW
```

Meaning precisely: the blocker is independently proved by four mechanisms, two
of them stronger than the ones originally reported; two mutually exclusive
architectures are specified bit-exactly with their topology, capability surface,
crash cuts, journal treatment, amended sentences, symmetry and residuals;
rejected families are named with reasons; the comparative audit, recommendation,
tokens and deterministic v1.3 handoffs are present; and the cell is kept
separate from the concurrent identity cell with coexistence shown for all four
combinations.

It does **not** mean the packet is correct, and it clears nothing. The X and Y
lines should recompute the §2 hashes, treat every sentence here as untrusted,
and begin with §9.
