All hashes verify. Before writing, I need to resolve T7, since it determines the verdict — and checking it surfaced a regression in my own v2.1.10.1.

Confirmed — the PCS deletes a signed C1 detector. Writing the correction.

Custody verified: exactly two new files; v2.1.10.1 and its closure unchanged at their pinned digests; `verification.py` unmodified; both specified roots correctly absent.

## Done — v2.1.10.2, ending in `BLOCKED_..._AUTHOR_CELL`

| Deliverable | SHA-256 |
|---|---|
| [OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_2_CORRECTION.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_2_CORRECTION.md) | `c7ff2777…00ec` |
| [opus5_officina_supervisor_control_channel_v2_1_10_2_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_10_2_closure.md) | `0016452d…429a` |

Both pinned hashes verified. Closure line 1: `BLOCKED_OFFICINA_SUPERVISOR_V2_1_10_2_AUTHOR_CELL`.

**The engineering is done.** T1: one `AF_UNIX`/`SOCK_SEQPACKET` pair per generation with `SCM_RIGHTS`, `CMSG_SPACE(12)`, max 3 fds, mandatory `MSG_CMSG_CLOEXEC`, and 4-byte little-endian packing via `int.to_bytes` — so neither `array` nor `struct` is added. T2: a fresh `t-pcs.v1` on its own channel; the carried six-field grammar is *scoped*, not extended. T3: a second isolated root; **`PYTHONPATH` deleted from the design**. T5: `{os, sys, _signal, time, fcntl, _socket}`, and the zero-byte-write "access-mode proof" replaced by `F_GETFL & O_ACCMODE`.

**Why it stops.** Checking T7 against v2.1 §W3.5 surfaced a regression in my own v2.1.10.1: parenting the watchdog to the PCS **deletes one of two signed supervisor-death detectors** (`getppid() ≠ recorded`) and makes watchdog-death detection depend on the PCS channel. v2.1.10.1 §V21101.6.5 claimed the exec'd watchdog "strengthens C1" — right about the address space, silent about the parent. That claim is withdrawn. Together with a new unrecoverable resident process (D1's availability model) and a second journal with fd-bearing responses that are explicitly *not* retry-stable (a narrowing of B1), three signed cells change in substance. That is not mechanical implementation, so the prompt's instruction applies.

**Cell P** is presented with three exclusive, fully-specified options — P1 full PCS, P2 with the watchdog left parented to the supervisor (preserving both C1 detectors at the cost of a contaminated fork), P3 defer B6 — and **decides none**. No scientific or resource value is reached by any option.

Two things worth flagging plainly: `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` was framed against a byte-only control channel, so it does not silently cover a capability-passing wire; and I have now twice shipped a layer whose governance conclusion was wrong, which is stated in the weakest-points list as a reason to discount this layer's own self-assessment.

T `NOT_ACTIVATED`; claim `OPEN`; token unavailable; cell P unsigned.
