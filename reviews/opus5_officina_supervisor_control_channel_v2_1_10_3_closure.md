READY_FOR_OFFICINA_SUPERVISOR_CELL_P_AUTHOR_SELECTION

# Author closure — Officina supervisor/control-channel v2.1.10.3 Cell P completion

Date: 2026-08-02
Author line: **Claude Code Opus 5, specification author only.** Not an
independent X-line or Y-line reviewer of this chain.

**This closure is an untrusted self-assessment**, as
`reviews/officina_supervisor_v2_1_authorship_note.md` requires of every author
closure in this chain — including v2.1.10's, v2.1.10.1's, and v2.1.10.2's, all
of which were treated here as claims to be checked rather than as evidence.
§R4 re-audited four of v2.1.10.2's assertions and **refuted three**.

**This is an author-cell completion only. No X/Y acceptance review is requested
in this round, and no option is selected.**

## Custody: base, hashes, and confirmation that nothing was touched

Repository base: commit `39a27667b9331dac40246ff34647b2bfb263dd4e`, which
descends from the required base. The working tree was already dirty at handover;
every pre-existing tracked modification and untracked path was preserved
byte-for-byte.

Governing inputs, recomputed and pinned:

```text
2b4f9cad7be7a69527e828c73928a399209fcd8151780b9b4c839934893e0dc8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md
2d4d4b189e460605ce95f8f464d7ef1c6d0c8ce317ad26033a91b4d2c556759b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md
c7ff27775fd1b394b850be1be3e1d361d95f5e12af251949f8363980bd2900ec  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_2_CORRECTION.md
0016452d3033146976b9dc779455f448c9fd690302ff4879d0d2b949e0fd429a  reviews/opus5_officina_supervisor_control_channel_v2_1_10_2_closure.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e  src/philosophia/officina/verification.py
```

This closure's companion:

```text
02d862e76f76a57cd154ecfd8a67f88abb02c2ce324e4026e4145069cee63143  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_3_CORRECTION.md
```

**Exactly two files were created and nothing else was touched.** v2.1.10,
v2.1.10.1, v2.1.10.2 and their closures are unedited and match the digests
above. `verification.py` is unmodified. `scripts/officina_process_control_bootstrap.py`
and `scripts/officina_role_bootstrap.py` do not exist. No code, test, verifier,
manifest, signature, prompt, contract, prior review, or runtime artifact was
edited, staged, or committed. Method: static authoring only — read-only file and
`git` inspection, literal search, `sha256sum`, and reasoning from pinned
Linux/CPython interfaces.

## Verdict

`READY_FOR_OFFICINA_SUPERVISOR_CELL_P_AUTHOR_SELECTION`.

**P4 is a real architecture.** It is implementable, it preserves both signed C1
detectors on the first watchdog, and it dominates P2. Cell P is therefore
repaired and is now complete enough for an informed selection. **No option is
selected here.** `READY` in this token means *ready for Kirill to choose*, not
ready for acceptance: `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`
remains unavailable until an option is selected **and** the resulting composite
passes fresh independent X/Y review.

## Replacement index over v2.1.10.2 (summary; §V21103.0 is normative)

| # | v2.1.10.2 locus | Action |
|---|---|---|
| 1 | option **P2** in §T7.5 | **withdrawn** — strictly dominated (§R5.2) |
| 2 | §T7.5's option block | replaced by the three-token block of §R5.3 |
| 3–4 | `SPAWN_WATCHDOG` in §T2.3 and its §T1.4 descriptor row | re-scoped to `SPAWN_REPLACEMENT_WATCHDOG`, preconditioned on a proved first-watchdog death, with the degraded-detector consequence journalled |
| 5–7 | §T4.1's watchdog tree branch, §T4.2/§T4.3's watchdog handle rows, §T4.5's `os.fork`-of-watchdog row | replaced — under P4 the watchdog is the supervisor bootstrap's child and the PCS has no first-construction watchdog primitive |
| 8 | §T1.6's "scan `/proc/self/fd` and close every descriptor outside the pinned set" | **deleted as unsafe**, replaced by a bounded exact received-fd rule (§R4.1) |
| 9–10 | §T3.2/§T5.1/§T5.4's role-bootstrap set `{os, sys}` | replaced by `{os, sys, fcntl}` (§R4.5) |
| 11 | §T3.3's `A-1`…`A-13` | extended by `A-8a`…`A-8h`, for `SUPERVISOR` only |
| 12–13 | §T7.2/§T7.3's C1 loss statement | scoped to **P1 only**; under P4 no detector is lost on the first watchdog |
| 14–15 | carried §U2.6 first-ack kill row; carried §W3.5 "forks a new watchdog" | the first retained verbatim (the process is clean there); the second superseded post-import by the PCS replacement route |
| 16–18 | §T8 watchdog test rows; §T9's weakest points; v2.1.10.2's `BLOCKED` verdict | replaced/extended; the cell block is discharged |

## One-to-one R1–R5 disposition

| Req | Disposition |
|---|---|
| **R1 — decide only whether P4 is real** | **It is.** §R1 gives the mechanical trace from the isolated `SUPERVISOR` role bootstrap to normal shutdown: the insertion point is between `A-8` and `A-9`, before `sys.path` gains any project entry; creation is **one route only**, `os.posix_spawn` with the same object-bound `/proc/self/fd/9` interpreter and `/proc/self/fd/7` source the bootstrap is itself running; parent and reaper relations are tabulated before and after `A-10` and are **identical**, because importing a module does not change the process; the PCS never learns `wd_pid`; descriptor maps, `CLOEXEC` behaviour and ownership transfers are given per descriptor; C1 registration, heartbeat/freeze, supervisor-death, watchdog-death and shutdown are mapped to the signed sections; PCS/supervisor/watchdog death and every construction-time crash cut have one continuation each; controllers and workers stay PCS-only behind **two independent barriers** (no pid field in `t-pcs.v1`, and they are not the supervisor's children); and §R1.12 enumerates the eight contamination vectors and shows each absent at `A-8a`. **No fallback to P2 was taken.** |
| **R2 — recompute the PCS under P4** | `SPAWN_WATCHDOG` is **retained with a proved different single-valued purpose** — replacement after a proved death, which the contaminated supervisor must not fork itself — and renamed `SPAWN_REPLACEMENT_WATCHDOG`, so the operation count stays **nine** and every field/count statement agrees. The PCS journal holds **no** watchdog entry for the first watchdog. §R1.8 gives the refusal and partial-construction cleanup automaton with no invented outcome. §R2.5 gives the exact supervisor/watchdog continuation on PCS EOF: watchdog retained and governed, freeze unavailable, generation to `T_PROCESS_INVALID`, **no false valid continuation**. §R1.10 proves watchdog death is observed and reaped before the supervisor exits, with a stated fail-closed alternative in every branch. Role-bootstrap allowlists corrected (§R4.5) with **no universal builtin-identity shortcut** — the chain already refuted that predicate. P1 and P3 are carried accurately; **P2 is withdrawn as dominated**; §R5.4 gives a bounded, explicitly non-absolute exhaustiveness argument. |
| **R3 — keep the costs loud** | §R3 states all five required items plus two P4-specific ones: the PCS remains mandatory and unrecoverable for controller/worker authority; `t-pcs.v1` remains a second durable journal; fd-bearing replies remain non-redeliverable as capabilities; `_socket`/`SCM_RIGHTS`/five roots/Linux-specific transfer remain, with an exact recount; and **the supervisor's one-child watchdog PID authority is named a narrow signed trust surface, not "no PID authority"**. P4-specific: the two-then-one detector asymmetry, and the fail-closed stall when a watchdog ignores EOF. No option is recommended, and none is defended by discounting these. |
| **R4 — engineering honesty checks** | Four re-audits, three refutations. (i) The `/proc/self/fd` sweep **would close legitimate authority descriptors of live roles**, because the supervisor's pinned set grows with every `SPAWN_ROLE`; deleted and replaced by "close exactly the parsed vector", with the safety argument given in **both** directions if the kernel truncation-granularity fact is wrong. (ii) `SCM_RIGHTS` close/ACK/crash cuts re-checked with the watchdog messages removed. (iii) `SOCK_SEQPACKET`, truncation flags and `MSG_CMSG_CLOEXEC` unchanged, still flagged reviewer-verifiable. (iv) The watchdog's exec introduces **no new provenance obligation** — it reuses the objects already proved. Plus: the role bootstrap needs `fcntl` (its own `A-6` uses `F_GETFL`), and `generic_harness.py` must gain `_socket` because the supervisor is the PCS client — both stated in v2.1.10.2 to the contrary. Full numeric recount in §R4.7. |
| **R5 — governance output** | `READY_FOR_OFFICINA_SUPERVISOR_CELL_P_AUTHOR_SELECTION`, three exact mutually exclusive tokens, a compact gains/costs table, **and no selection**. |

## Process / fd / authority table for each surviving option

| | **P1** | **P4** | **P3** |
|---|---|---|---|
| `pid_mid` parent/reaper | PCS | PCS | PCS |
| controller / worker parent/reaper | PCS | PCS | **contaminated supervisor** |
| watchdog parent/reaper (first) | PCS | **supervisor bootstrap, verified clean at creation** | contaminated supervisor |
| watchdog parent (replacement) | PCS | PCS | supervisor |
| supervisor names PIDs | never | `wd_pid` only, `waitpid` only | all |
| supervisor may signal a PID | never | **never** (kill withdrawn post-import) | yes |
| C1 supervisor-death detectors, first watchdog | 1 | **2** | 2 |
| C1 watchdog-death detector | PCS round trip | supervisor `waitpid`, direct | supervisor `waitpid`, direct |
| watchdog address space | fresh, isolated | **fresh, isolated** | inherited, contaminated |
| watchdog holds `SPAWN.lock` | no | **provably no** (§R1.5) | inherits unless separately closed |
| PCS single point of failure | yes | yes | no |
| second durable journal | yes | yes | no |
| production roots | 5 | 5 | 4 (role root optional) |
| known Major defect left open | none | none | **supervisor process authority** |

## Weakest points, against my own proposal

1. **P4's load-bearing step is "importing a module does not change the
   process".** True and mechanical, but if `generic_harness.py`'s entry can
   re-exec, fork, or daemonize, the option collapses. The contract forbids it and
   row 407 tests it, but the property lives in imported code.
2. **P4 narrows the C218-1 class to one PID; it does not eliminate it.** A
   competing reaper in the contaminated supervisor can steal the watchdog's
   reap. Removing the signal half makes the residual fail-closed, not absent.
3. **P4 makes a wedged watchdog unrepairable** — no post-import kill means a
   stall into invalidity where P1 could kill through the PCS. Which is better is
   exactly the trade the cell exists for, and I did not decide it.
4. **The two-then-one detector asymmetry is inelegant**, and a reviewer may
   prefer P1's uniform model.
5. **The `POSIX_SPAWN_DUP2` `CLOEXEC` leak was found only by tracing P4.** The
   same class of omission may exist in the carried PCS→controller and
   PCS→worker spawns, which I asserted but did not re-derive descriptor by
   descriptor.
6. **§R4.1 rests on a kernel truncation-granularity fact** I made safe in both
   directions but could not verify, correctly, since no probe was permitted.
7. **The exhaustiveness argument is bounded by my framing of two questions.** A
   reviewer who asks whether the supervisor needs to be a separate process at all
   would find options outside this cell.
8. **Three of my layers have now needed a governance correction** — v2.1.10.1
   declared `READY` over an unimplementable transport; v2.1.10.2 offered a
   dominated option and asserted a two-module role bootstrap. Weight this
   closure accordingly; it is why the verdict is a cell completion rather than a
   readiness claim.

## Exact next gate and explicit negative authorization

1. **Kirill selects exactly one** of
   `I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION`,
   `I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P3_DEFER_SUPERVISOR_AUTHORITY`,
   `I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P4_CLEAN_BOOTSTRAP_PARENTED_WATCHDOG`.
   **This layer selects none.**
2. A **separate correction** binds the selected option, deletes the unselected
   branches from the operative text, and recomputes every count, table and
   verifier rule against the single surviving architecture.
3. **Only then** is a fresh independent X-line and Y-line review of that
   composite requested. **This round asks nothing of X or Y.**
4. `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` becomes available
   **only** after both lines confirm the identical bytes of that composite.

**Negative authorization.** Nothing here authorizes implementation; any code,
test, verifier, manifest, allowlist, signature or contract edit; a commit; a
host change; any process, socket, pipe, FIFO, fork, exec or signal; any
supervisor, controller, worker, watchdog, adapter, middle child, grandchild,
endpoint, journal instance, spawn record, lease, capability, operation, capacity
artifact, custody disposition, freeze witness or result manifest; T activation;
entropy; E1/E2/E3 spend; Q/C work; a world, learner, candidate, Q attempt,
datum, outcome or Proof; or any claim movement.

**Confirmed: no code was written, no test was run, no probe, spawn, socket,
fork, or signal experiment was executed, and no Officina process was started.
No entropy, activation, T/Q/C object, datum, or outcome was created.**

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. **T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.**
