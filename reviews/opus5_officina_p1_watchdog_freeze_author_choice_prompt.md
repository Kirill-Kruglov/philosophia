# Prompt for Claude Code Opus 5: author the P1 watchdog-freeze mechanism choice packet

You are **Claude Code Opus 5 acting only as the specification author**. Do not
choose for Kirill and do not act as X/Y reviewer. Work in the local
`philosophia` repository. Read-only inspection and hashes are permitted. Do not
edit existing files, implement code, run probes or execute process-control
operations. T remains `NOT_ACTIVATED`; claim remains `OPEN`.

## Re-derive the reported blocker

The identity choice packet reports an orthogonal conflict:

- signed C1 requires the dedicated watchdog to witness/freeze after supervisor
  death;
- selected P1 places every PID and signal authority in the PCS;
- the watchdog receives no PID and no usable PCS endpoint, and its slot 6 is
  explicitly closed;
- supervisor death is precisely the moment no supervisor relay exists;
- therefore update-pipe EOF can be observed, but no specified route can execute
  the freeze.

Read the full C1/P1 chain, watchdog slot maps, `SPAWN_WATCHDOG`, update/ack
channels, `SIGNAL_GROUP`, PEER_EOF, supervisor-death and PCS-death crash cuts.
Independently prove or refute the blocker. Treat the reporting author as
untrusted.

## Deliverables

Create exactly two files:

1. `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`
2. `reviews/opus5_officina_p1_watchdog_freeze_author_choice_packet.md`

Do not modify anything else.

## Required choices

Provide mutually exclusive, bit-exact architectures. At minimum analyze:

### W-A — watchdog requests, PCS executes

The watchdog keeps no PID and sends one closed freeze request through a
dedicated PCS-mediated capability after update EOF. Specify exact endpoint/slot,
request grammar, generation/handle binding, ack, timeout, replay/idempotency,
PCS action, freeze scope, crash cuts and why the capability cannot express an
arbitrary target or another opcode. State the required amendment to "watchdog
holds no capability" and whether it remains the dedicated freezer in the
scientifically meaningful sense.

### W-B — PCS automatically freezes on supervisor PEER_EOF

The PCS detects loss of the supervisor channel and executes the precommitted
freeze plan itself; the watchdog independently witnesses/records. Specify exact
ordering between PEER_EOF, update EOF, freeze, witness, replacement/invalidity,
which process proves what, and every race with PCS death. State the required
amendment to C1 if the watchdog becomes a witness rather than the actor that
requests the freeze.

Include another route only if it is genuinely distinct and closed. Reject
routes that give the watchdog PID knowledge, direct signal syscalls, a general
PCS client, or a supervisor relay after the supervisor is dead unless a signed
choice explicitly accepts that cost.

For every selectable option give exact:

- process/fd topology and descriptor leak proof;
- authority and opcode/capability surface;
- supervisor-death versus PCS-death semantics;
- first/replacement watchdog symmetry;
- B1 journal/replay and crash cuts;
- C1 and P1 sentences amended/retained;
- generic-harness/batch/invalidity interaction;
- code/verifier/test/manifest surface;
- residual liveness under A3 and publication wording;
- author token and deterministic v1.3 handoff.

Compare blast radius and recommend one only from signed-authority fidelity,
mechanical testability and minimal reopened contracts. Keep the concurrent
process-claim identity cell separate; explain whether the two selected repairs
can coexist but do not condition either choice on the other's outcome.

No token is signable until bounded X/Y review. Closure line 1 exactly one of:

```text
READY_FOR_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_XY_REVIEW
BLOCKED_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_PACKET
```

The closure must include the independent blocker proof, complete option table,
recommendation, exact tokens, hashes/custody, three X and three Y questions,
and confirmation no choice was accepted.

This round authorizes no selection, implementation, activation, resource spend,
T/Q/C datum, outcome, Proof or claim movement.
