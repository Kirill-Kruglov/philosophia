READY_FOR_OFFICINA_SUPERVISOR_P1_COMPOSITE_XY_REVIEW

# Author closure — Officina supervisor/control-channel v2.1.10.4 P1 binding

Date: 2026-08-02
Author line: **Claude Code Opus 5, specification author only.** Not an
independent X-line or Y-line reviewer of this chain.

**This closure is an untrusted self-assessment**, as
`reviews/officina_supervisor_v2_1_authorship_note.md` requires of every author
closure here — including v2.1.10's, v2.1.10.1's, v2.1.10.2's and v2.1.10.3's,
none of which was used as evidence. The governing inputs are the **signed
selection** and the operative bytes of the carried chain.

**This round is binding, not choosing and not self-review.** Cell P is signed;
this layer emits one operative architecture and asks X and Y to review identical
bytes.

## Byte and hash custody

Repository base: commit `c9f883d98375c0d961dae4821b44e0a2a818bd65`. The
selection's own base, `ee7a1973e752ac11442ac8cde6c12b00c859484c`, is verified an
ancestor. The working tree was already dirty at handover; every pre-existing
tracked modification and untracked path is preserved byte-for-byte.

**The signature was read in full and all three of its governing hashes
reproduce exactly against this repository:**

```text
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
02d862e76f76a57cd154ecfd8a67f88abb02c2ce324e4026e4145069cee63143  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_3_CORRECTION.md
d46414389187bb87068e5105a0a914a56f5f49f1244bdb5b527ccea89acba18c  reviews/opus5_officina_supervisor_control_channel_v2_1_10_3_closure.md
0b9b67f7d57892012df3ad44e6f943a8c8ccf0eb8ed71d966d88b694b8ca5163  reviews/opus5_officina_supervisor_control_channel_v2_1_10_3_cell_p_completion_chat_response.md
```

Selected token, recorded verbatim from the signature:

```text
P: I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION
```

This closure's companion:

```text
6197d2a4073d35fc978119db32128c50d12594343ac87731640a1d8e19f09e84  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md
```

**Exactly two files were created and nothing else was touched.** The signature,
v2.1.10, v2.1.10.1, v2.1.10.2, v2.1.10.3, every closure, the A3/B1/C1/D1/K1
signatures, the harness and batch composites, the authorship note, and
`verification.py` (`327b1bb2…`) are all unedited and match their digests.
`scripts/officina_process_control_bootstrap.py` and
`scripts/officina_role_bootstrap.py` do not exist. No code, test, verifier,
manifest, prompt, prior review, or runtime artifact was edited, staged, or
committed. Method: static authoring only — read-only file and `git` inspection,
literal search, `sha256sum`, and reasoning from pinned Linux/CPython interfaces.

## Verdict

`READY_FOR_OFFICINA_SUPERVISOR_P1_COMPOSITE_XY_REVIEW`.

The P1 composite is mechanically single-valued: one architecture, one process
tree, one opcode enum, one descriptor model, one journal automaton, one crash
matrix, one shutdown route, and one set of counts. No further author decision
was reached, and no signed contract conflict was found, so no `BLOCKED_…`
verdict is emitted. `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`
remains **unavailable** until **both** independent lines confirm the identical
bytes.

## Replacement index over v2.1.10.3 and earlier superseded rows

| # | Locus | Action |
|---|---|---|
| 1 | v2.1.10.3 §R5.1/§R5.3 option definitions and token block | **deleted**; Cell P is signed |
| 2 | v2.1.10.3 §R1 in full (the P4 trace `A-8a`…`A-8h`), §R2.1's opcode rename, §R2.3's replacement handle role, §R2.4's rows, §R2.5's EOF route, §R5.2, §R5.4 | **deleted as operative text**; retained only in §P1B.0.2's provenance table |
| 3 | every "first-versus-replacement" asymmetry statement and the degradation flag | **deleted**; `SPAWN_WATCHDOG` has one uniform meaning |
| 4 | v2.1.10.3 §R4.1's "a resource fact, not an authority fact" | **replaced** by §P1B.6 — an installed `SCM_RIGHTS` descriptor is a **capability** |
| 5 | v2.1.10.2 §T1.6 step 2, the global `/proc/self/fd` sweep | **deleted as unsafe**; replaced by §P1B.6.3 |
| 6 | v2.1.10.2 §T3.2/§T5.1/§T5.4's role-bootstrap `{os, sys}` and `S-1'`'s "exactly two" | **replaced** by `{os, sys, fcntl}`, three |
| 7 | v2.1.10.2 §T5.4's `generic_harness` set excluding `_socket` | **replaced**; it gains `_socket`, still excludes `signal`, `_signal`, `sys` |
| 8 | v2.1.10.2 §T7 in full (the governance finding and the cell) | **discharged**; §P1B.13 states the bound consequences |
| 9–10 | v2.1.10.3 §R6 rows 405–436 and v2.1.10.2 §T8 rows 354/356/362/381 | **replaced** by §P1B.14's 354R/356R/362R/381R and 437–486 |
| 11 | v2.1.10.2 §T4.2's PCS-to-role descriptor statement | **replaced** by §P1B.3.3's leak proof |
| 12 | carried §W3.5 "watchdog's `getppid()` ≠ recorded, **or** update pipe EOF" | **replaced** by §P1B.7.2 — one detector; the watchdog must **ignore** `getppid()` |
| 13 | carried §W3.5 "**`waitpid` on own child**, or parent-check failure" | **replaced** by §P1B.7.3 — `REAP_ROLE` plus ack absence; the supervisor performs no `waitpid` |
| 14 | carried §W3.5 "**forks a new watchdog**" | **replaced** by §P1B.7.4 — `SPAWN_WATCHDOG`, uniform |
| 15 | carried §W2.1's in-process watchdog fork bullet | **replaced** by §P1B.7.1 — a PCS-created isolated `execve`'d role |
| 16 | carried §U2.6's "kill the watchdog by `WATCHDOG_CHILD.json`" | **replaced** by §P1B.7.5 — close the update write end, then `REAP_ROLE`; **no signal to a watchdog on any path** |

## One-to-one B1–B6 disposition

| Req | Disposition |
|---|---|
| **B1 — one operative architecture** | §P1B.1 states it in seven clauses. §P1B.0.1 deletes every P3/P4 operative row; §P1B.0.2 confines P2/P3/P4 to a provenance table with the explicit rule that **no operative text may condition behaviour on them**. One process tree and direct-parent/reaper table (§P1B.2), descriptor tables (§P1B.3), handle model (§P1B.4), nine-opcode protocol and journal/ACK automaton (§P1B.5), crash and invalidity matrix (§P1B.8), shutdown route (§P1B.9), imports (§P1B.10), verifier surface (§P1B.11), counts (§P1B.12), test matrix (§P1B.14) — all for P1 only |
| **B2 — carry the v2.1.10.3 corrections** | (1) role bootstrap `{os, sys, fcntl}`, **three**, in §P1B.10.2, §P1B.11 CHANGE 2, `S-1'`, §P1B.12 and row 465. (2) `generic_harness.py` gains `_socket` and still excludes `signal`, `_signal`, `sys` — §P1B.10.3, CHANGE 2, row 466. (3) the global sweep is deleted, with the reason stated: the supervisor's legitimate set **grows with every live role handle** and its members are at kernel-chosen numbers — §P1B.6.1, `S-18`, rows 445–446. (4) the `POSIX_SPAWN_DUP2` non-`CLOEXEC` consequence is re-audited in §P1B.3.3 with a five-step proof and per-role file actions, including the explicit `(CLOSE, 6)` the `WATCHDOG` map needs — rows 442–444. (5) the object-bound `-I -S -E -P`, empty-environment role bootstrap and the removal of `PYTHONPATH` are carried — §P1B.10.5, row 470. **No P4-only step, no watchdog PID in the supervisor, and no first-versus-replacement asymmetry survives** — row 437 |
| **B3 — the `SCM_RIGHTS` cleanup statement** | §P1B.6. The false classification is **deleted**: an installed descriptor is a capability. §P1B.6.2 pins the primary interface fact from `net/core/scm.c`'s `scm_detach_fds()` — Linux installs `min(space, queued)` descriptors, reports **exactly** those in the returned control data with `cmsg_len = CMSG_LEN(i·4)`, sets `MSG_CTRUNC`, and **releases every queued descriptor it did not install** — and marks it reviewer-verifiable. Hence an installed-but-unreported descriptor **cannot exist** at the kernel boundary. The one uncovered interval is an interpreter-side raise inside `_recvmsg`, handled by an immediate `_exit_(T_PCS_EXIT_RECV_UNENUMERABLE)` with **no callback, finalizer, `atexit`, flush, or unwinding**, and named in §P1B.6.5 as a possible transient **capability leak**, bounded and terminated by the kernel's closure at exit. The cleanup closes exactly the parsed vector, de-duplicated, ascending, once each, `EBADF` tolerated, and **never** an unrelated live role's descriptors. A3 is invoked as the procedural home of the concurrent-actor case and is **explicitly not upgraded** to a security guarantee. `MSG_CMSG_CLOEXEC`, `MSG_CTRUNC`, `MSG_TRUNC`, fd-count/type validation and the no-redelivery rule are preserved. **No global sweep, proxy, or capability-recovery protocol is introduced** |
| **B4 — bind C1, B1, D1, K1/A3 honestly** | §P1B.13, in four unsoftened paragraphs. C1: a dedicated freezer watchdog is retained with every carried property, **and P1 intentionally reduces supervisor-death detection from two mechanisms to update-pipe EOF — the author's selected trade, not a mechanically unchanged C1 implementation**; the address-space strengthening is stated separately and is not used to obscure the reduction (row 483). B1: the client journal is unchanged; `t-pcs.v1` adds a separate control-plane journal; byte replies replay, **descriptor-bearing replies cannot redeliver the same capability, so an ACK loss invalidates the generation**. D1: no idle exit, ground intact, **availability now depends on a mandatory PCS whose crash is unrecoverable — accepted fail-closed invalidity, never a scientific or resource outcome**. K1/A3: carried exactly; **nothing in P1 creates Q/C confidentiality or same-UID adversarial confinement** (row 484) |
| **B5 — static implementability audit** | Traced without executing anything: caller → PCS → middle/supervisor and PCS → every role (§P1B.2); socketpair and `SCM_RIGHTS` ownership at send, receive, ACK, timeout, replay, malformed ancillary, supervisor death, PCS death and shutdown (§P1B.5.4, §P1B.6, §P1B.8, §P1B.9); the nine-operation protocol with **no PID, descriptor, or path field** and **no stale watchdog opcode semantics** (§P1B.5.2); first watchdog, repeated replacement, wedged watchdog, role stop/reap and every handle-release route (§P1B.7, §P1B.8.3, §P1B.9); journal installation, crash cuts, unresolved-generation refusal and the no-adoption prohibition (§P1B.5.4, §P1B.8.2); every import and the per-primitive plus method-descriptor identity classes, with **no universal builtin predicate** (§P1B.10.4); five roots and `root_source_sha256` (§P1B.11); and every numeric statement in one table (§P1B.12). **The audit found one real defect in my own draft** — §U6.1's carried preflight steps are literally named `P0`–`P3`, so a naive "no `P3` anywhere" test would have collided with them; row 437 now matches option **tokens and phrases**, never bare letters, and exempts the preflight names explicitly. **P1 required no further author decision and produced no signed contract conflict** |
| **B6 — review handoff** | This closure. §P1B.17 carries three bounded questions per line, both on identical bytes |

## Operative P1 constants and counts

| Statement | Value |
|---|---|
| production roots | **5** |
| PCS import closure | **6** — `{os, sys, _signal, time, fcntl, _socket}` |
| role-bootstrap import closure | **3** — `{os, sys, fcntl}` |
| `generic_harness.py` scoped set | **17** — sixteen signed members + `_socket`; not `signal`, `_signal`, `sys` |
| `t-pcs.v1` operations | **9**, with one uniform `SPAWN_WATCHDOG` |
| max descriptors per message | **3**; ancillary buffer `CMSG_SPACE(12)` |
| PCS descriptor constants | **6** (values 3–8) |
| role descriptor slots | **8** numbers (3–10); `WATCHDOG` uses 7 and closes slot 6 |
| role classes | **4** |
| supervisor-death detectors | **1** — watchdog update-pipe EOF |
| watchdog-death detectors | **2** — ack absence, `REAP_ROLE` `REAPED_POSITIVE` |
| new numeric resource values / timeouts / K1 ceilings / E1/E2/E3 values / T bands | **0** |
| platform | `Linux x86_64`, `CPython 3.12.3` |

## Process / fd / authority

| Process | Direct children | May `wait` | May signal | Names PIDs |
|---|---|---|---|---|
| caller | the PCS | the PCS only; result irrelevant | **nothing** (forbidden) | its own children |
| **PCS** | `pid_mid`, every controller, worker, watchdog | **all of them, solely** | **all of them, solely** | **yes, and only it** |
| supervisor | **none** | nothing — a wildcard wait returns `ECHILD` | **nothing** | **no** — handles only |
| watchdog | none | nothing | nothing | no |
| controller / worker | per the carried role contracts | unchanged | unchanged | no |

## Crash and invalidity

| Cut | Continuation |
|---|---|
| caller crash / early pipe close | `EPIPE`; changes no record, custody, ownership, or terminal decision |
| caller helper reaps the PCS | only an exit status is lost; the pipe reply is authoritative |
| `_recvmsg` raises | `_exit_(T_PCS_EXIT_RECV_UNENUMERABLE)`, no callback; named capability-leak interval |
| ancillary violation | close exactly the parsed vector; invalidity route |
| ACK lost on an fd-bearing reply | `FD_DELIVERY_UNCONFIRMED`; **no re-send**; generation invalid |
| supervisor death | watchdog update-pipe EOF ⇒ freeze, observe, exit; PCS holds every handle in the reaper state |
| **PCS death** | `init` adoption; supervisor loses all authority; **freeze unavailable**; watchdog closed out; **unrecoverable whole-generation invalidity**; **no adoption** — a new PCS refuses `GENERATION_NOT_ADOPTABLE` |
| watchdog death | ack absence and `REAP_ROLE`; replacement by `SPAWN_WATCHDOG`, uniform |
| wedged watchdog | `WATCHDOG_UNREAPED`; **no signal ever**; invalidity route |
| `STRUCTURAL_VIOLATION` at any wait site | never death; `CONTRADICTED`; no further signal; no record touched |
| `SHUTDOWN` with a live handle | `REFUSED`/`HANDLES_LIVE`; nothing released |
| every unknown control outcome | `T_PROCESS_INVALID` + §4c(c)/§4d unknowable, with invalidity dominance; never a success, capacity, custody, E1/E2/E3, or Q/C fact |

## Future implementation and verifier edit surface

| Path | Permitted change | Status |
|---|---|---|
| `scripts/officina_process_control_bootstrap.py` | the PCS and its `t-pcs.v1` server | **does not exist** |
| `scripts/officina_role_bootstrap.py` | the four-role isolated entry | **does not exist** |
| `src/philosophia/officina/verification.py` | CHANGES 1–5 of §P1B.11 only | unmodified |
| `successor/officina/runtime_control/PRODUCTION_CALL_GRAPH.json` | five roots, closure, `root_source_sha256` | does not exist |
| `src/philosophia/officina/generic_harness.py` | launcher, `t-pcs.v1` client, four role entries; **removal** of every `Popen`/`fork`/`waitpid`/`kill`/`killpg` | untracked Cursor work — **preserved** |
| tests | §P1B.14 | untracked Cursor work — **preserved** |
| everything else | none | byte-unchanged |

## Weakest points against my own composite

1. **The C1 reduction to one detector is a real loss**, and §P1B.3.3's leak
   proof is now load-bearing for C1 in a way it was not under two detectors: if
   the update write end were ever duplicated into another process, EOF would not
   fire on supervisor death and the sole detector would be defeated.
2. **The PCS is a single point of failure** whose loss is unrecoverable —
   strictly worse availability than the signed §W2.9 two-phase takeover.
3. **§P1B.6.2 rests on a kernel-source fact** I could not verify empirically.
   The rule is fail-closed for the interval the fact does not cover, but the
   fact itself must be checked by the reviewers.
4. **The capability-leak interval is real**, bounded and terminated by `_exit`,
   and it lives inside A3, which is procedural and not a guarantee.
5. **`_socket.socket`'s finalizer** is a finalizer in a closure whose value is
   having none; its two containment rules are AST-checked conventions, not
   properties of the type.
6. **A lost ACK on an fd-bearing reply costs a generation** — an ordinary
   transient producing an invalidity. That is the accepted B1 narrowing.
7. **The composite is large**: five roots, two protocols, two journals, four
   role classes, nineteen AST rules, an eleven-step runtime preflight. A
   reviewer may judge the aggregate too large to verify in one pass.
8. **Three of this author line's earlier layers needed governance correction**,
   and this round's own audit caught a `P0`–`P3` name collision in my draft
   test. Weight this closure low and check §P1B.12's counts and §P1B.0.1's
   index literally rather than trusting them.

## Bounded questions for the independent lines

Both review the **identical bytes** of §P1B and the carried chain, recompute
every governing hash, and treat every author closure — including this one — as
untrusted. §P1B.17 carries them verbatim.

**X = Claude Code Opus 4.8.** X-Q1: is P1 single-valued — one architecture, no
unselected branch outside the provenance table, a nine-member enum with a
uniform `SPAWN_WATCHDOG`, every §P1B.12 count literally true? X-Q2: is
§P1B.3.3's `POSIX_SPAWN_DUP2` leak proof correct, and is §P1B.6 right about
`scm_detach_fds()` so that the only unenumerable case is an interpreter-side
raise? X-Q3: are §P1B.13's four cell statements honest and unsoftened, and does
any operative sentence soften one? Verdict line 1 exactly
`CONFIRM_OFFICINA_SUPERVISOR_P1_COMPOSITE_X` or
`REVISE_OFFICINA_SUPERVISOR_P1_COMPOSITE`.

**Y = GPT-5.6 Sol.** Y-Q1: are the crash/invalidity matrix, shutdown route and
journal automaton total, with every unknown outcome reaching
`T_PROCESS_INVALID` and §4c(c)/§4d rather than a success or capacity fact? Y-Q2:
is §P1B.6 the right repair — no global sweep, exact parsed-vector cleanup, a
fail-closed `_exit_` for the unenumerable case named as a **capability leak**,
A3 not upgraded — and does `scm_detach_fds()` verify independently? Y-Q3: is the
one-detector watchdog model coherent, with the watchdog ignoring `getppid()` so a
PCS death cannot cause a false freeze, no `waitpid` in the supervisor, no signal
to a watchdog on any path, and uniform replacement — and do the carried surfaces
hold byte-unchanged? Verdict line 1 exactly
`CONFIRM_OFFICINA_SUPERVISOR_P1_COMPOSITE_Y` or
`REVISE_OFFICINA_SUPERVISOR_P1_COMPOSITE`.

Both lines: static review only — run no code, test, probe, or
process/socket/pipe/fork/exec/signal operation; create exactly one review file;
modify nothing; authorize no implementation, activation, entropy, spend, Q/C
work, datum, outcome, or claim movement.

## Authorization boundary

**`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains unavailable
and is not made signable by this binding.** It becomes available **only** if
**both** the independent X line and the independent Y line confirm the identical
bytes whose digest is `6197d2a4…`, together with the carried chain. Cell P being
signed accepts an architecture for binding; it does not accept this composite.

This author round authorizes no X/Y verdict, no implementation, no code or test
edit, no verifier or manifest change, no commit, no host change, no process or
probe, no T activation, no entropy, no E1/E2/E3 spend, no Q/C work, no datum, no
outcome, no Proof, and no claim movement.

**Confirmed: no code was written, no test was run, no probe was executed, and no
process, socket, pipe, fork, exec, or signal operation was performed.**

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. **T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.**
