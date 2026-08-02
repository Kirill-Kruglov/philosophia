BLOCKED_OFFICINA_SUPERVISOR_V2_1_10_2_AUTHOR_CELL

# Author closure — Officina supervisor/control-channel v2.1.10.2 PCS transport correction

Date: 2026-08-02
Author line: **Claude Code Opus 5, specification author only, never an independent reviewer.**

**This closure is an untrusted self-assessment.** It is not an X-line review,
not a Y-line review, and not evidence. The same author line wrote v2.1 through
v2.1.10.2. `reviews/officina_supervisor_v2_1_authorship_note.md` records that
this line cannot serve as an independent reviewer of its own bytes.

**No independent review of v2.1.10, v2.1.10.1, or this layer has occurred, and
none is requested here.**

## Base, bytes, and method

Repository base: commit `251c51eae495fed488c13dc2a46b840a4a8df2d2`, verified to
descend from the required `2660a056e0434c6ff433066c0c43a9e885d71bc1`
(`git merge-base --is-ancestor`). The working tree was already dirty at
handover; every pre-existing tracked modification and untracked path was
preserved untouched.

Pinned inputs, independently recomputed and matching exactly:

```text
2d4d4b189e460605ce95f8f464d7ef1c6d0c8ce317ad26033a91b4d2c556759b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md
f7a866f9100cae1abf80623cd6a7d689cbdca1001fb33dffe98966a727582008  reviews/opus5_officina_supervisor_control_channel_v2_1_10_1_closure.md
```

Digest of the artifact this closure accompanies:

```text
c7ff27775fd1b394b850be1be3e1d361d95f5e12af251949f8363980bd2900ec  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_2_CORRECTION.md
```

Method: static authoring only. Read-only file and `git` inspection, literal
search, `sha256sum`, and reasoning from pinned Linux/CPython interfaces. **No
code, test, probe, spawn/socket/fork/signal experiment, or Officina process ran.
No implementation was written. No existing file, implementation, verifier,
activation artifact, entropy, T/Q/C object, datum, claim, or prior document was
modified.**

## Verdict: `BLOCKED_OFFICINA_SUPERVISOR_V2_1_10_2_AUTHOR_CELL`

`READY` is **not** available, and the reason is not that the engineering is
incomplete — §T1 through §T6 are specified bit-exactly and are, as far as I can
determine, implementable. `READY` is unavailable because **T7's answer is (2)**:
the PCS is a new architecture on signed surfaces, not a mechanical
implementation of already-selected policies, and the prompt's own instruction
governs — *"If an author signature is required for the expanded trust/control
surface, emit `BLOCKED_..._AUTHOR_CELL` with the exact bounded choice instead of
declaring `READY`."*

`BLOCKED_..._CONTRACT_CONFLICT` is also **not** the right token: nothing here is
an irreconcilable conflict with a signed contract. Every affected sentence is
namable and scopeable. What is missing is an **author decision**, not a
resolution.

### The finding that forced this, stated against my own prior layer

Carried v2.1 §W3.5 gives supervisor death **two independent detectors** —
"watchdog's `getppid()` ≠ recorded, **or** update pipe EOF" — and gives watchdog
death the supervisor's own `waitpid` on its own child.

Under the PCS the watchdog's parent becomes the **PCS**, so `getppid()` no
longer changes when the supervisor dies. **One of the two supervisor-death
detectors is deleted**, and watchdog-death detection now depends on the PCS
channel being alive.

**v2.1.10.1 §V21101.6.5 asserted that the exec'd watchdog "strengthens C1 rather
than weakening it". That claim was wrong.** It was right about the address space
— an exec'd watchdog has no capability by construction — and silent about the
parent. It is withdrawn in §T7.2. Deliberately halving a redundant safety
detector on the **C1-selected** watchdog is a trade, and possibly the right one,
but it is not the author's to make.

## One-to-one disposition of the seven defects

| # | Defect | Disposition | Where |
|---|---|---|---|
| **T1** | byte pipes cannot transfer descriptors, so `SPAWN_ROLE`/`SPAWN_WATCHDOG` were unimplementable | **Resolved, single-valued.** One `AF_UNIX`/`SOCK_SEQPACKET`/`0` pair per generation, created by the PCS **before** the fork that leads to the supervisor, peer end inherited to a pinned role fd. Descriptors travel only as `SCM_RIGHTS` ancillary data. Pinned: `CMSG_SPACE(12)`, max 3 descriptors, `MSG_CMSG_CLOEXEC` mandatory on every `recvmsg`, no credentials, 4-byte little-endian packing via `int.to_bytes`/`from_bytes` — so **neither `array` nor `struct` is added**. A per-opcode legal fd-count-and-type vector; a nine-row ownership table across send/ack/timeout/duplicate/malformed/peer-death/PCS-death; unconditional close of every received descriptor plus a `/proc/self/fd` sweep before any invalidity routing | §T1 |
| **T2** | the six-field `SPAWN_SUPERVISOR` grammar cannot carry nine operations; v2.1.10.1's "framing unchanged" was false | **Resolved.** Two channels, two protocols: the carried grammar is **scoped** to the caller↔PCS pipe and its one operation; a fresh `philosophia.officina.t-pcs.v1` runs on the socket with one closed request and one closed response per operation, generation id, strictly increasing request id, handle id, single outstanding request, and the J1–J6 journal order with every crash cut. Partial reads/writes are impossible by socket type. **One exception to B1 is stated loudly**: fd-bearing responses are never re-sent, so they are not retry-stable | §T2 |
| **T3** | the role exec re-enabled `site`/`.pth`/customization and used `PYTHONPATH` | **Resolved.** A second object-bound isolated root, `scripts/officina_role_bootstrap.py`, `-I -S -E -P`, **empty environment**, with a thirteen-step refusal order that ends by setting `sys.path[:]` to exactly one object-bound entry and importing exactly the role module, then re-verifying its inode. **`PYTHONPATH` is deleted from the design.** `SUPERVISOR` and `WATCHDOG` are fully isolated; `CONTROLLER` and `WORKER` cannot be, by the signed design that makes their target client-supplied, so §T3.4 gives the six-vector proof that they cannot affect process, capacity, custody or scientific validity | §T3 |
| **T4** | PCS lifetime, fd and custody totality | **Resolved.** Full process tree with direct-child/reaper columns; PCS-side and per-role fd tables; the handle binding; the mapping of every signed object onto handles with unchanged scientific meaning; PCS crash with `init` adoption and an explicit **prohibition on adopting a live generation**; supervisor EOF, caller crash, watchdog/role crash, shutdown with live handles, resource stop. Every unknown outcome routes through the **signed** `T_PROCESS_INVALID` and §4c(c)/§4d unknowable semantics. §T4.5 proves the primitive→operation→consumer mapping **and names the two detectors for which "relocate the primitive" does not hold** | §T4 |
| **T5** | import closure and the invalid read-only test | **Resolved.** `{os, sys, _signal, time, fcntl, _socket}` for the PCS root, `{os, sys}` for the role root, with `_socket`'s empty Python closure audited and its socket-object finalizer disclosed. The zero-byte-write "access-mode proof" is deleted and replaced by `fcntl(fd, F_GETFL) & O_ACCMODE == O_RDONLY` with pinned constants. Verifier CHANGES 1'–5' add the fifth root, the scoped maps, and rules `S-14`…`S-17` | §T5 |
| **T6** | launcher and object provenance must stay exact | **Resolved.** The fd-bound `/proc/self/fd/7` and `/proc/self/fd/8` mechanism and the `posix_spawn` file actions carry; the hoist and collision proof are generalized to an arbitrary target set and reused for every PCS→role spawn. An identity/hash obligation table separates run-time object identity from deploy-time byte provenance, and §T6.2 shows a wholly fabricated caller tree produces a closed system with no path into any signed object | §T6 |
| **T7** | governance boundary | **Answered (2): a new architecture.** Three signed surfaces change in substance — C1 (§T7.2), D1 (a new mandatory resident process whose loss is an unrecoverable whole-generation invalidity), B1 (a second journal plus the retry-stability exception) — plus five production roots, `_socket`, and `SCM_RIGHTS` capability transfer, a class of mechanism no prior control channel had. **Cell P is proposed with three exclusive, fully-specified options and is not decided** | §T7 |

## Cell P — the exact bounded choice

Presented, not decided. **No option decides a scientific or resource value; none
moves a K1 constant, an E1/E2/E3 value, a T band, a capacity ceiling, a custody
rule, or a Q/C boundary.**

| Option | Adopts | Gains | Costs |
|---|---|---|---|
| **P1** `…_P1_FULL_PCS_MEDIATION` | §T1–§T6 in full | every PID held by a clean constructed process; the supervisor holds handles and cannot express a PID; the watchdog gains a capability-free address space by construction | C1's `getppid()` supervisor-death detector **deleted**; watchdog-death detection depends on the PCS channel; the PCS is an unrecoverable single point of failure; B1 gains a second journal and fd-bearing responses are not retry-stable; five roots; `SCM_RIGHTS` capability transfer enters the contract |
| **P2** `…_P2_PCS_WITH_SUPERVISOR_PARENTED_WATCHDOG` | §T1–§T6 for supervisor, controllers and workers; the **watchdog stays a supervisor in-process fork** | both C1 detectors preserved exactly as signed | the watchdog is created by a contaminated interpreter — bounded by argument (no lock, no capability, no PID authority, freeze observations only) rather than by construction |
| **P3** `…_P3_DEFER_SUPERVISOR_AUTHORITY` | none of §T1–§T4; PCS scope stays exactly v2.1.10's | no new signed surface, no new journal, no single point of failure, no C1 change | the supervisor's own `Popen`/`waitpid`/`kill`/`killpg`/watchdog-fork defect stays **OPEN** as a named Major defect for its own signed layer. §T3 and §T5 may still be adopted independently, since neither depends on the PCS |

**Why the existing token does not cover this by itself.**
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` was framed against an
amendment whose control channel carried **bytes and no capability**, whose
watchdog was a supervisor fork, and whose failure model had no unrecoverable
resident component. Treating it as silently extending to a capability-passing
wire, a second durable journal, a new mandatory process, and a deleted C1
detector would be exactly the over-reach the last four review rounds rejected.
After cell P is signed it remains the right instrument for the resulting
composite — but not before.

## Required contents

| Required | Where |
|---|---|
| literal v2.1.10.1 → v2.1.10.2 replacement index | §V211002.0, sixteen rows, each quoting the superseded text |
| complete wire and ancillary schemas | §T1.3, §T1.4, §T2.2, §T2.3 |
| fd / process / ownership tables | §T1.5, §T4.1, §T4.2, §T4.3 |
| operation / state / idempotency automata | §T2.3–§T2.7, §T4.3, §T4.5 |
| import / primitive / verifier changes | §T5.1–§T5.4 |
| isolated role-entry contract | §T3.2–§T3.4 |
| crash / cut matrix | §T1.6, §T2.6, §T4.6, §T4.8 |
| platform scope | §T9, unchanged from the carried pin |
| no-regression | §T9, over §V21101.9 and §V2110's carried surfaces |
| exact future edit surface and tests | §T9 and §T8, rows 353–404 |
| weakest points against myself | §T9, eight items |

## Weakest points, against myself

1. **`SCM_RIGHTS` portability** — `SOCK_SEQPACKET` over `AF_UNIX` and
   `MSG_CMSG_CLOEXEC` are Linux-specific; the platform pin makes this
   consistent but deepens the dependence on one kernel.
2. **Received-fd `CLOEXEC`** rests on `MSG_CMSG_CLOEXEC` being atomic with
   installation; a kernel that ignored the flag would open a window no static
   rule can detect.
3. **The PCS is a single point of failure** whose loss is an unrecoverable
   whole-generation invalidity, with an explicit no-adoption prohibition. Correct
   fail-closed direction, strictly worse availability than the signed §W2.9
   two-phase takeover it displaces.
4. **Protocol/journal coupling** — a second durable journal doubles the
   crash-cut surface, and fd-bearing responses are explicitly not retry-stable,
   a narrowing of B1 I could not avoid without inventing capability accounting.
5. **`_socket.socket`'s finalizer** is a finalizer in a closure whose value is
   having none. It can only close, but it is there.
6. **A fourth identity kind** (method descriptors for `sendmsg`/`recvmsg`) joins
   a table that exists because a universal predicate was already wrong. A fifth
   kind would signal the approach failing.
7. **I have now twice shipped a layer whose governance conclusion was wrong.**
   v2.1.10.1 declared `READY` while carrying an unimplementable transport and a
   withdrawn C1 claim. A reviewer should weight this layer's self-assessment
   accordingly — which is part of why it stops at a cell rather than declaring
   readiness.
8. **Cell P's options may not be exhaustive.** A per-operation short-lived clean
   instance was considered and is not offered, because handles and the
   PID-holding property would not survive between calls. If a reviewer sees a
   fifth option, the cell is under-specified.

## Questions

§T10 carries **three** bounded questions per line, framed as *is the engineering
right and is cell P correctly framed* — **not** as a request for acceptance
review, which cannot begin until P is signed. X-Q1 attacks the transport; X-Q2
the protocol and the role isolation; X-Q3 the governance finding and the cell's
exclusivity and completeness, with an explicit invitation to rule that no cell
is needed. Y-Q1 attacks single-valuedness; Y-Q2 totality and the invalidity
routing; Y-Q3 the cell, including an explicit invitation to rule either that
this layer should have declared `READY`, or that even a cell is insufficient and
the whole PCS needs a separate signed layer. Verdict line 1 is exactly
`CONFIRM_OFFICINA_SUPERVISOR_V2_1_10_2_CELL_FRAMING_X` / `..._Y` or
`REVISE_OFFICINA_SUPERVISOR_V2_1_10_2`.

## Custody, authorization boundary, and programme state

Exactly **two** files were created by this work, and nothing else in the
repository was touched:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_2_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_10_2_closure.md` (this file)

Neither `scripts/officina_process_control_bootstrap.py` nor
`scripts/officina_role_bootstrap.py` exists; both are specified, not created.
`src/philosophia/officina/verification.py` is unmodified — digest `327b1bb2…` —
and the production call-graph manifest does not exist. v2.1.10 and v2.1.10.1 and
their closures are **not edited**; their digests are recorded in the correction
and match. No prior artifact, contract, signature, review, prompt, code file,
verifier, or test file was edited, staged, or committed; the untracked
`src/philosophia/officina/generic_harness.py`,
`tests/test_officina_generic_harness.py`, `essay/OUTLINE.md`, and the modified
`accounting.py`, `test_officina_accounting.py`, and review/prompt files are
preserved byte-for-byte.

Confirmed explicitly, as required: **no code, no test, no run of any kind — no
implementation, probe, smoke command, spawn/socket/fork/signal experiment, or
Officina process — and no activation, entropy, T/Q/C work, datum, outcome, or
claim movement.** T remains `NOT_ACTIVATED`; the programme claim remains `OPEN`;
no artifact was produced.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` is **not authorized and
remains unavailable**. **Cell P is unsigned and no option is selected by this
layer.** Nothing here authorizes implementation, code, test, verifier, manifest,
or allowlist change, commit, host change, T activation, entropy, E1/E2/E3 spend,
Q/C work, capability, lease, operation, capacity artifact, custody disposition,
result manifest, world, learner, candidate, Q attempt, datum, outcome, Proof, or
claim movement, and no later gate.

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`.
