# Officina supervisor and control-channel amendment — v2.1.10.7 pre-X/Y consistency repair

Status: `P1_BOUND_REPAIRED_CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`.
Layer prefix: **§P1T**.

> ## WHAT THIS LAYER REPAIRS
>
> One internal inconsistency and three adjacent overstatements, all in my own
> v2.1.10.6 bytes. **Bounded correction only.** No topology change, no new
> syscall, import or process, and no new author choice — so no `BLOCKED_…` is
> owed. The signed `…_P1_FULL_PCS_MEDIATION` selection, A3/B1/C1/D1/K1, the
> process topology, `S-18'`, the `P-f`/`A-5`/`G-5` permissions, the reliance
> audit and all v2.1.10.5 F1–F5 closures are **preserved and re-confirmed**
> (§P1T.8).
>
> **The inconsistency.** §P1S.1.3 gave the caller a *static* row — "Direct
> children: the PCS … May wait on: **the PCS only**" — while §P1S.1.1–§P1S.1.5
> of the same document said a contaminated caller or higher ancestor may be a
> child subreaper and may therefore **adopt and wildcard-reap** the supervisor
> after `m9`, and `pid_mid` and every role after PCS death. Both cannot govern.
> §P1T.1 replaces the table with a **temporally explicit** one: initial direct
> children and wait-set, versus dynamically adopted orphans when that process is
> the nearest living child subreaper — covering the caller **and an arbitrary
> higher ancestor**, not only namespace init.
>
> **Three overstatements, each withdrawn to its earned strength:**
>
> 1. the claim that adopter-observable wait statuses come from a closed set
>    `{0, 3, named PCS exit tokens}` is **false** — under A3 a same-UID actor may
>    terminate an adopted process with any signal. §P1T.2 treats such a status as
>    an **untrusted OS fact** carrying no authorized programme meaning;
> 2. "cannot **forge or block** a death proof" conflated two things. §P1T.3
>    keeps only the true half — **no false-positive** object-bound death proof
>    for a live process — and admits the other: an adopter may **stop** a
>    process and thereby delay or prevent death, keep a channel open, and deny
>    proof availability **indefinitely**;
> 3. "cannot gain Officina process authority" conflated **kernel power** with
>    **authorization**. §P1T.4 admits the kernel power and states the narrower
>    truth: no Officina descriptor, handle, opcode or journal authority is
>    conferred, and no interference is ever accepted as a valid Officina
>    decision.
>
> **§P1T.5 states the safety-versus-liveness boundary explicitly**, and §P1T.6
> preserves the 10.6 reliance result **only at its earned strength**: no valid
> Officina decision consumes an orphan's wait status. **No liveness, no
> confinement, and no uninterruptible death-proof availability is claimed.**

**Authorship.** Written by **Claude Code Opus 5 acting only as the specification
author**. This line wrote v2.1 through v2.1.10.6 and **cannot** serve as the
independent X or Y line for its own bytes
(`reviews/officina_supervisor_v2_1_authorship_note.md`). **The v2.1.10.6 verdict
is treated here as an untrusted author self-assessment, and every defect
repaired in this layer was in my own bytes.** This layer does not self-confirm.

**Signed state, carried unchanged:**

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
P: I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION
```

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable**. Creates nothing executable. Edits no existing file, code, test,
verifier, manifest, signature, prompt, prior review, or runtime artifact. Starts
no process, socket, pipe, fork, exec, signal, wait, or `prctl` operation. T
remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.

## Governing hashes (recomputed)

```text
8f806e33d85c00933871072dadda30110f18ea6bf34b5ebc388f23f8b067143e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_6_PRE_XY_REPAIR.md
65a32a6eeb0834b13207d1a6cf3ceff6501d4a895dab84ed0226b7500fa711cd  reviews/opus5_officina_supervisor_control_channel_v2_1_10_6_pre_xy_repair_closure.md
798d0cbd51e93cc1f4c0a443785f90d90a2e121d35738189cbee9c61acf557cc  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_5_P1_PRE_XY_REPAIR.md
68cf3b872f54346c2c03f646644318f585b51b99cf12cf037ce4cf1159c58041  reviews/opus5_officina_supervisor_control_channel_v2_1_10_5_p1_pre_xy_repair_closure.md
6197d2a4073d35fc978119db32128c50d12594343ac87731640a1d8e19f09e84  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md
5889461b86870c357a61e1b7327c1285773c4263dd9640bf3e2da202b9bde302  reviews/opus5_officina_supervisor_control_channel_v2_1_10_4_p1_binding_closure.md
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
02d862e76f76a57cd154ecfd8a67f88abb02c2ce324e4026e4145069cee63143  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_3_CORRECTION.md
c7ff27775fd1b394b850be1be3e1d361d95f5e12af251949f8363980bd2900ec  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_2_CORRECTION.md
2d4d4b189e460605ce95f8f464d7ef1c6d0c8ce317ad26033a91b4d2c556759b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md
2b4f9cad7be7a69527e828c73928a399209fcd8151780b9b4c839934893e0dc8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md
1468c9ab1806c1eb25523e6a9fd8567592076f0dc74418ca698a52f933c7f3b0  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md
33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e  src/philosophia/officina/verification.py
```

---

## §P1T.0. Literal replacement index over v2.1.10.6

**Everything not named carries verbatim**, including §P1S.1.1's `prctl(2)`
interface fact, §P1S.1.2's adoption wording, §P1S.1.4's crash cuts, §P1S.1.6's
reliance audit (at the strength §P1T.6 fixes), §P1S.1.7's
nothing-architectural list, §P1S.1.8's A3 statement, §P1S.2 in full (`S-18'`,
the phase/permission table, the `G-5` disjointness proof), and the whole carried
P1 composite.

| # | v2.1.10.6 locus, quoted | Action |
|---|---|---|
| 1 | §P1S.1.3's caller row cells "Direct children: **the PCS** … May wait on: **the PCS only**" | **replaced** by §P1T.1.2 — the wait-set is temporally explicit and includes dynamically adopted orphans |
| 2 | §P1S.1.3's table as a whole (a static six-row table with a single "Adopter if orphaned" column) | **replaced** by §P1T.1.2's dynamic table, which adds an arbitrary higher ancestor `A*` as an explicit row |
| 3 | §P1S.1.5's "can" row "learn each orphan's PID and wait status \| … those values come from a **closed, small set** — `0`, `3`, and the named PCS exit tokens — and carry **no** scientific, capacity, custody, resource, or Q/C content" | **replaced** by §P1T.2 — the closed-set claim is **withdrawn as false**; the no-programme-meaning half is retained and re-grounded |
| 4 | §P1S.1.5's "cannot" row "**forge or block** a death proof \| the proofs are object-bound `/proc` facts with start-identity matching, never reap-based" | **replaced** by §P1T.3 — only the **false-positive** half survives; blocking/denial is **admitted** |
| 5 | §P1S.1.5's "cannot" row "**gain Officina process authority** \| §P1S.1.6" | **replaced** by §P1T.4 — the authorization distinction |
| 6 | §P1S.1.5's two tables as a whole | **replaced** by §P1T.1.3's single dynamic capability table |
| 7 | §P1S.1.6's result sentence, insofar as it could be read as a liveness or availability claim | **scoped** by §P1T.6 — it is a **safety** result only |
| 8 | §P1S.4.2 test row **503** ("a fixture in which an ancestor is a child subreaper produces **the same contract behaviour** … identical decisions, identical records, identical routes") | **replaced** by §P1T.7.2 rows 503R and 514 — identical **decisions and records** under a *non-interfering* adopter; a separate row for the interfering case asserting fail-closed, **not** identical behaviour |
| 9 | §P1S.4.1's verifier rule list | **extended** by §P1T.7.1's `S-26`, `S-27`, `S-28` |
| 10 | §P1S.5's weakest-points list | **extended** by §P1T.9 |
| 11 | §P1S.1.4's crash-cut language, wherever it implies that a death proof or a channel EOF must eventually become available | **scoped** by §P1T.3.3 and §P1T.5 |

---

## §P1T.1. The dynamic parent / adopter / wait / authority model

### §P1T.1.1 Why the old table was wrong

A wait-set is **not a static property of a process**. Under
`PR_SET_CHILD_SUBREAPER` (§P1S.1.1, carried) a process's direct-child set —
and therefore the range of its wildcard waits — **grows** whenever a descendant
is orphaned and that process is the nearest still-living ancestor subreaper.
Writing "May wait on: the PCS only" for the caller stated a property that the
same document elsewhere denied. **The table is replaced by one that names the
initial set and the dynamically adopted set separately.**

### §P1T.1.2 The dynamic table

`A*` denotes an **arbitrary higher ancestor** of the caller — any process in the
ancestor chain, of which the caller is only the nearest possible instance. The
contract observes none of them and names none of them.

| Process | Initial direct children | Initial wait-set | Dynamically adopted, **iff** it is the nearest living ancestor subreaper at that moment | Wait-set after adoption | Officina authority |
|---|---|---|---|---|---|
| **`A*`** (any higher ancestor) | whatever the host gave it | its own children | the supervisor after `m9`; and after PCS death `pid_mid`, every controller, worker and watchdog — **if the caller and every nearer ancestor is not a living subreaper** | its own children **plus** every process it has adopted; a wildcard wait ranges over that union | **none** — §P1T.4 |
| **caller** | the PCS | the PCS | the same set as `A*`, **if the caller is itself a subreaper and is nearer** | the PCS **plus** every process it has adopted; a wildcard wait ranges over that union | **none** beyond launching the PCS and the `L-1`…`L-4` pipe exchange; §P1T.4 |
| **PCS** | `pid_mid`, controllers, workers, watchdogs | exactly those | nothing — it never sets the subreaper attribute, and its own descendants are orphaned only when it is already dead | unchanged | **full**: the only holder of numeric process authority (carried) |
| middle (`pid_mid`) | the grandchild until `m9` | **nothing** — it never waits | nothing | nothing | none |
| **supervisor** | **none** | **nothing** — a wildcard wait returns `ECHILD` | nothing | nothing | **handles only, never a PID** (carried) |
| watchdog | none | nothing | nothing | nothing | none |
| controller / worker | per the carried role contracts | unchanged | nothing | unchanged | none |

**The adopter's wildcard waits range over its adopted direct children.** That is
stated affirmatively, not denied.

### §P1T.1.3 What adoption does and does not add, precisely

A same-UID actor may already signal any of this contract's processes **without**
adopting anything — that is the carried A3 rescope. **Adoption therefore adds
exactly two powers and no others:**

| Adoption adds | Detail |
|---|---|
| **reaper status** | the adopter may `wait`-family-reap the adopted process, including by wildcard, and thereby observes its wait status and controls when the zombie clears |
| **`getppid()` visibility** | `getppid()` in the adopted process returns the adopter's PID. **No Officina route reads `getppid()` on any process** — the supervisor's is explicitly unused (carried v2.1 §W2.1 as corrected by §P1S.1.2 row 7), and the watchdog is required to ignore it (carried §P1B.7.2) — so this confers nothing |

| Adoption does **not** add | Why |
|---|---|
| the ability to signal, stop or kill | already available to any same-UID actor under A3, with or without adoption |
| any descriptor or capability | reaping conveys none; capabilities move only by `SCM_RIGHTS` on the sealed socket or by inheritance |
| any Officina handle, opcode, journal entry or control-plane participation | §P1T.4 |
| the ability to create a false-positive death proof | §P1T.3.1 |

### §P1T.1.4 `AWAIT_STOP` cannot be intercepted while PCS custody is live

> `AWAIT_STOP` is the **single** decision in the composite that branches on a
> wait status (carried §P1S.1.6). Its target is a controller or worker that is a
> **direct child of the PCS**. A controller or worker becomes an orphan **only**
> if the PCS dies. Therefore:
>
> - **while PCS custody is live**, the target is a non-orphan, no adopter can
>   have adopted it, and no adopter's wildcard wait can reach it — so no adopter
>   can intercept the `WIFSTOPPED` result on which the decision depends;
> - **if the PCS dies**, custody is lost, the generation is already
>   unrecoverable invalidity by the carried route, and **no `AWAIT_STOP`
>   decision is being taken** — so there is nothing to intercept.
>
> Both halves are required, and together they preserve the carried result. ∎

---

## §P1T.2. Adopter-observable wait status — the closed-set claim withdrawn

> **Deleted:** "those values come from a closed, small set — `0`, `3`, and the
> named PCS exit tokens".
>
> **It is false.** Under the carried A3 same-UID rescope an actor may terminate
> an adopted process with any signal, so an adopter may observe a
> `WIFSIGNALED` status naming any deliverable signal, or an exit code produced
> by a path this contract did not author. **The set is not closed and the
> contract must not enumerate it.**

```text
OPERATIVE RULE. A wait status observed by an adopter is an UNTRUSTED OPERATING
SYSTEM FACT. It:
  - may reflect A3 same-UID interference, including a signal the actor itself
    delivered;
  - carries NO authorized programme meaning of any kind;
  - is never consumed by any Officina decision, record, journal entry,
    settlement, capacity accounting, custody disposition, or Q/C input;
  - is never a scientific or resource datum, and is permanently non-citable.
```

The half of the old row that survives — that the value carries no scientific,
capacity, custody, resource or Q/C content — is **retained and re-grounded**:
it holds not because the value comes from a small set, but because **no route
anywhere reads it** (§P1T.6).

---

## §P1T.3. Death proof — false positive versus availability

### §P1T.3.1 What the adopter cannot do (retained)

> **No false-positive object-bound death proof for a live process.** The carried
> death predicates are: `/proc/<pid>` **absent**; or present in state `Z` with a
> **matching start identity**; or present and live with a **different** start
> identity, which §U6.1 P3 routes to "treat as not live and **never kill**". A
> live process with a matching start identity satisfies none of them, and an
> adopter cannot make `/proc` report absence for a process that is running or
> stopped. **Reaping cannot fabricate liveness or death; it can only follow an
> actual exit.** This half of the old claim is correct and is kept.

### §P1T.3.2 What the adopter can do (admitted, previously denied)

> **Deleted:** "cannot **forge or block** a death proof".
>
> **An adopter — or, under A3, any same-UID actor — may deny proof availability
> indefinitely.** Concretely:
>
> | Interference | Effect |
> |---|---|
> | `SIGSTOP` an adopted or same-UID process | it stays alive; `/proc` shows state `T`, never `Z` or absent; **no death proof ever becomes available** |
> | keep a stopped process alive | it retains every open descriptor, so a sealed channel it holds **never reaches EOF** — including the `t-pcs.v1` socket and the watchdog update pipe |
> | decline to reap an adopted zombie | `/proc` state `Z` persists; this is *harmless*, because state `Z` with a matching identity is itself an accepted death proof |
> | reap promptly | `/proc` absence occurs sooner; also an accepted proof |
>
> **The first two are genuine liveness attacks and the previous wording denied
> them.** They are admitted here.

### §P1T.3.3 Every such effect fails closed

Each interference lands in a route that already exists and already fails closed;
**none becomes a valid status, outcome, resource datum, or scientific evidence:**

| Interference | Carried route | Outcome |
|---|---|---|
| a stopped process denies a death proof | §U6.1 P3 / §U2.5 obtain no proof ⇒ **no record is removed and nothing is killed** | the carried A3 stopped-process residual (§U2.7, `B-OWNED`) — a fail-closed stall |
| a stopped supervisor keeps the `t-pcs.v1` socket open | the PCS sees no `PEER_EOF`, holds every handle in the carried non-returning reaper state, and frees the singleton for no one | fail-closed stall |
| a stopped watchdog keeps the update pipe open, or ignores its EOF | `WATCHDOG_UNREAPED` (carried §P1B.7.5) — **no signal is sent** | `T_PROCESS_INVALID` + §4c(c)/§4d |
| any operation whose control outcome cannot be established | the carried §P1B.8.4 routing | `T_PROCESS_INVALID` + §4c(c)/§4d, with invalidity dominance; never a completion, capacity fact, custody disposition, E1/E2/E3 fact, or Q/C input |

**A stall is the intended behaviour, not a defect being concealed.** The
contract's guarantee is that nothing false is recorded — not that progress
occurs (§P1T.5).

---

## §P1T.4. Kernel power versus Officina authorization

> **Deleted:** the unqualified "cannot gain Officina process authority".
>
> **Admitted, without hedging:** adoption confers **kernel** parent and reaper
> status over the adopted process, and the carried A3 same-UID rescope already
> permits signal interference with or without adoption. The actor therefore
> holds real kernel power over these processes, and this contract does not
> remove it, confine it, or claim to.
>
> **What remains true, and is the whole of the claim:**
>
> 1. **No Officina descriptor or handle is conferred.** Reaping transfers no
>    descriptor. Capabilities move only by `SCM_RIGHTS` on the sealed
>    `t-pcs.v1` socket — a point-to-point channel between the PCS and the
>    supervisor — or by inheritance at a fork or exec the PCS controls. An
>    adopter is on neither path.
> 2. **The actor is never an authorized control-plane participant.** It holds no
>    `t-pcs.v1` endpoint, so no opcode is reachable to it; it appears in no
>    journal as an actor; it can issue no request, receive no response, and hold
>    no handle. Every `t-pcs.v1` precondition is evaluated against handles the
>    PCS itself assigned.
> 3. **No interference can be turned into a valid Officina decision or into a
>    scientific or resource outcome.** Every route it can perturb fails closed
>    into `T_PROCESS_INVALID` and the signed §4c(c)/§4d unknowable route
>    (§P1T.3.3), and no decision consumes an orphan's wait status (§P1T.6).
>
> **That is an authorization statement, not a power statement**, and it is the
> only one this contract is entitled to make.

---

## §P1T.5. The exact safety-versus-liveness boundary under A3

```text
GUARANTEED (safety), and claimed:
  S1. No false-positive death proof: no live process is ever recorded dead, and
      no record naming a possibly-live process is removed without an
      object-bound proof or an authoritative reap by its own parent.
  S2. No capability transfer to any unauthorized actor: no descriptor, handle,
      opcode, or journal authority reaches a process outside the PCS/supervisor
      control plane.
  S3. No unauthorized decision: no interference is accepted as an Officina
      decision, and no adopter-observed value is consumed by one.
  S4. Fail-closed routing: every perturbed or unestablished control outcome
      settles through T_PROCESS_INVALID and the signed §4c(c)/§4d unknowable
      route, with invalidity dominance; never as a completion, capacity fact,
      custody disposition, E1/E2/E3 fact, Q/C input, or scientific evidence.

NOT GUARANTEED (liveness), and explicitly NOT claimed:
  L1. That any generation completes.
  L2. That a death proof ever becomes available for a stopped process.
  L3. That a sealed channel ever reaches EOF.
  L4. That a fail-closed stall ever terminates.
  L5. That a same-UID actor is confined, detected, or prevented in any way.

A3 is a PROCEDURAL rescope. It is not confinement, not adversarial
same-process or same-UID security, and it is not upgraded here. Every liveness
loss above is permanently non-citable, forbidden from selection, Q, C, C1--C6,
any blinding claim, and any scientific or resource interpretation.
```

---

## §P1T.6. The reliance result, at its earned strength

> **Retained, as a SAFETY result only:** no valid Officina decision consumes an
> orphan's wait status. §P1S.1.6's audit stands — exactly one decision in the
> composite branches on a status word (`AWAIT_STOP`'s `WIFSTOPPED`), and its
> target is never an orphan while the decision is being taken (§P1T.1.4). Every
> other consumer uses the returned **pid** of a direct PCS child, an
> object-bound `/proc` fact, or a channel EOF.
>
> **Not claimed, and explicitly withdrawn from any reading of that result:**
> that the composite is live under interference; that a death proof or a channel
> EOF remains available; that a stall terminates; or that adoption is prevented,
> detected, or made harmless in any sense beyond S1–S4.

---

## §P1T.7. Mechanical guards, verifier and tests

### §P1T.7.1 Verifier rules

```text
S-26  (new) No operative sentence states an exclusive wait-set — "only", "sole",
      "exactly" — for the caller or any ancestor process without the
      dynamically-adopted-orphan qualification of §P1T.1.2.
      ⇒ "exclusive ancestor wait-set asserted"

S-27  (new) No operative sentence enumerates, bounds, or otherwise closes the
      set of wait-status values an adopter may observe.
      ⇒ "closed adopter status set asserted"

S-28  (new) In the adopter or same-UID context, no operative sentence asserts
      that the actor "cannot block", "cannot delay", "cannot prevent", or
      "cannot deny" a death proof, a channel EOF, or progress; and no sentence
      asserts an unqualified "cannot gain process authority". The permitted
      forms are exactly: "cannot create a false-positive object-bound death
      proof", and the three authorization clauses of §P1T.4.
      ⇒ "adopter liveness or authority overclaim"

Rules S-1'…S-25 and CHANGES 1--5 are unchanged.
```

### §P1T.7.2 Tests

Replaced:

- **503R** — with a **non-interfering** ancestor subreaper, the contract
  produces **identical decisions and identical durable records** to a run with
  no subreaper; assert equality of decisions and records only, **not** of
  timing, liveness, or process lifetimes.

Added:

| # | Test |
|---|---|
| 514 | with an **interfering** adopter (it `SIGSTOP`s an adopted process), assert the run **fails closed**: no death proof is fabricated, no record naming a possibly-live process is removed, and the generation routes to `T_PROCESS_INVALID` + §4c(c)/§4d. **Do not assert identical behaviour** |
| 515 | the caller's and an arbitrary ancestor's wait-sets are the dynamic sets of §P1T.1.2; assert no operative text says "the PCS only" or any equivalent exclusive form (`S-26`) |
| 516 | a wildcard wait in an adopter reaches its adopted orphans; assert this is stated affirmatively in the operative text |
| 517 | **`AWAIT_STOP` non-interception**: while PCS custody is live the target is a non-orphan direct PCS child and no adopter can reach it; after PCS death no `AWAIT_STOP` decision is taken |
| 518 | no operative text enumerates or bounds adopter-observable wait-status values (`S-27`); an injected `SIGKILL`-terminated adopted process yields a status outside any previously claimed set and changes no decision |
| 519 | the adopter cannot produce a false-positive death proof: a live or stopped process with a matching start identity satisfies none of the carried death predicates |
| 520 | a stopped process denies death-proof availability and keeps its channels open indefinitely; assert the routes stall **fail-closed** and that no operative text denies this (`S-28`) |
| 521 | a stopped supervisor keeps the `t-pcs.v1` socket open, the PCS sees no `PEER_EOF`, holds every handle in the carried reaper state, and frees the singleton for no one |
| 522 | no descriptor, handle, opcode, or journal authority reaches any adopter; `SCM_RIGHTS` is point-to-point between the PCS and the supervisor only |
| 523 | no operative text asserts an unqualified "cannot gain process authority"; the three §P1T.4 authorization clauses are present verbatim (`S-28`) |
| 524 | the §P1T.5 safety set S1–S4 is asserted and the liveness set L1–L5 is asserted **as not guaranteed**; no operative text claims any of L1–L5 |
| 525 | `getppid()` is read by no Officina route, in any process |
| 526 | 10.6's `S-18'`, the `P-f`/`A-5`/`G-5` permissions, the reliance audit, and v2.1.10.5's F1–F5 all still hold verbatim |
| 527 | whole-composite no-regression diff over every carried surface |

---

## §P1T.8. No-regression

| Surface | Status |
|---|---|
| **10.6 R1** — child-subreaper-or-namespace-init adoption wording, the seven replaced loci, the four crash cuts, the group-anchor row, §P1S.1.7's nothing-architectural list, §P1S.1.8's A3 statement | **unchanged**; this layer corrects only the table's staticness and three overstatements adjacent to it |
| **10.6 R2** — `S-18'`, the phase/permission table, the `G-5` disjointness proof, rows 359R/442R/445R/425 | **unchanged, byte-semantically** |
| **10.6 reliance audit** (§P1S.1.6) | **retained**, scoped by §P1T.6 to a safety result |
| **v2.1.10.5 F1** — lock `O_CLOEXEC` + `F_GETFD` readback, `G-1`…`G-6`, the fork-shared-lock theorem, `A-5` as verification | unchanged |
| **F2** — authority boundary, supervisor outside the PCS child set, post-`c11` group route | unchanged; §P1T.1.2's PCS row restates it |
| **F3** — one watchdog rule, no signal on any path | unchanged; §P1T.3.3 adds no signal |
| **F4** — withdrawn no-callback theorem, `S-19` AST-only, the named capability exposure inside A3 | unchanged; §P1T.5 is its generalization to the adopter case |
| **F5** — non-aborting `B-2`/`B-3`, `B-4` the only actor | unchanged |
| **P1 selection**, topology, nine opcodes, five roots, 6/3/17 imports, `CMSG_SPACE(12)`, 3-fd maximum | unchanged; **no syscall, import, process or role is added** |
| **A3** | carried and **not upgraded**; §P1T.4 and §P1T.5 make its limits more explicit, never stronger |
| **B1, C1, D1, K1**, output-capacity selection | unchanged; no journal, ack, redelivery, watchdog-detector, idle-exit, ceiling, accounting or custody rule is touched |
| object-bound observation, both revalidation barriers, bound-language sweep, `CLOSE_OWNED`, custody P1–P7, §Z3.3 layout, §Z3.2 role enum | carried byte-unchanged |

---

## §P1T.9. Weakest points of this repair

1. **This layer makes the composite honestly weaker, not stronger.** It admits
   that a same-UID actor can stall any generation indefinitely and that no
   liveness property is guaranteed. A reviewer may reasonably judge that a
   control plane with no liveness guarantee under its own stated threat model is
   not acceptable — in which case the answer is confinement, which A3 explicitly
   is not, and which would require a new author cell.
2. **The safety set S1–S4 is my own enumeration.** If a fifth safety property is
   needed and I have not listed it, the boundary statement is incomplete rather
   than wrong, and nothing mechanical would catch that.
3. **`S-26`/`S-27`/`S-28` are wording guards.** They forbid the phrasings that
   went wrong, which is exactly the class of defect that recurred — but a future
   layer could restate the same overclaim in words the rules do not match.
4. **§P1T.1.4's `AWAIT_STOP` argument depends on the topology.** It holds only
   because controllers and workers are direct PCS children. Any future change to
   who spawns them would break it silently, and only `S-25` (carried) guards the
   related status-consumption property.
5. **Four consecutive author layers have each found defects in the previous
   one**, all mine. That is the strongest reason to weight this closure low and
   to check §P1T.0's index and §P1T.1.2's table literally rather than trusting
   them.

---

## §P1T.10. The bounded review questions

Both lines review the **identical bytes** of this repair together with the
carried composite, recompute every governing hash, and treat every author
verdict in this chain — including this one — as untrusted.

### For the X line (Claude Code Opus 4.8 / 5, clean context)

> **X-Q1.** Is §P1T.1.2's dynamic table now internally consistent with the
> carried subreaper semantics — initial versus adopted sets, an arbitrary higher
> ancestor `A*` as well as the caller, and wildcard waits stated affirmatively
> as ranging over adopted children — and does §P1T.1.4's `AWAIT_STOP`
> non-interception argument hold in **both** halves (custody live, and custody
> lost)?
> **X-Q2.** Are the three withdrawals correct and complete: the closed
> wait-status set gone and replaced by an untrusted-OS-fact rule; "forge or
> block" split into a retained **false-positive** impossibility and an admitted
> **availability denial**; and "cannot gain process authority" replaced by the
> three authorization clauses of §P1T.4? Does any operative sentence anywhere in
> the composite still carry one of the withdrawn forms?
> **X-Q3.** Is §P1T.5's safety-versus-liveness boundary the right one — S1–S4
> claimed, L1–L5 explicitly not — and is §P1T.6's reliance result correctly
> scoped to safety, with `S-26`/`S-27`/`S-28` sufficient as mechanical guards
> against reintroduction, **without** reopening P1, the topology,
> A3/B1/C1/D1/K1, `S-18'`, or any F1–F5 closure?
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_P1_V2_1_10_7_X` or
> `REVISE_OFFICINA_SUPERVISOR_P1_V2_1_10_7`. Static review only: run no code,
> test, probe, or process/socket/pipe/fork/exec/signal/wait/prctl operation;
> create exactly one review file; modify nothing; authorize no implementation,
> activation, entropy, spend, Q/C work, datum, outcome, Proof, or claim
> movement.

### For the Y line (GPT-5.6 Sol, clean context)

> **Y-Q1.** Is the inconsistency genuinely closed — does any statement anywhere
> in the operative composite still give a process a static exclusive wait-set
> that its own subreaper analysis contradicts?
> **Y-Q2.** Is §P1T.3's distinction exact and honest: that no false-positive
> object-bound death proof is possible, while an adopter or any same-UID actor
> may stop a process and thereby deny a death proof and a channel EOF
> **indefinitely** — and does §P1T.3.3 route every such effect into a carried
> fail-closed path with nothing becoming a valid status, outcome, resource datum
> or scientific evidence?
> **Y-Q3.** Is §P1T.4's authorization-versus-kernel-power distinction the right
> repair, and is §P1T.5 honest about what is **not** guaranteed — including that
> the contract offers no liveness and no confinement under A3? If you judge that
> a control plane with no liveness guarantee under its stated threat model
> cannot be accepted, say so explicitly, since that would be a new author cell
> rather than a defect in these bytes.
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_P1_V2_1_10_7_Y` or
> `REVISE_OFFICINA_SUPERVISOR_P1_V2_1_10_7`. Static review only: run no code,
> test, probe, or process/socket/pipe/fork/exec/signal/wait/prctl operation;
> create exactly one review file; modify nothing; authorize no implementation,
> activation, entropy, spend, Q/C work, datum, outcome, Proof, or claim
> movement.

---

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** and is not made signable here. **No acceptance token is available
from this author round.** It becomes available only if both independent lines
confirm the identical corrected composite. This layer authorizes no
implementation, no code, test, verifier or manifest edit, no commit, no host
change, no process or probe, no T activation, no entropy, no E1/E2/E3 spend, no
Q/C work, no datum, no outcome, no Proof, and no claim movement.
`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. **T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.**
