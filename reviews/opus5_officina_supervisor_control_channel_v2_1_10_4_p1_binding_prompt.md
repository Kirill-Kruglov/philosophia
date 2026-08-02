# Prompt for Claude Code Opus 5: bind the selected P1 supervisor architecture

You are **Claude Code Opus 5 acting only as the specification author**. You are
not an independent X-line or Y-line reviewer. Work in the local `philosophia`
repository. Do not edit any existing file. Do not implement code, run tests or
probes, execute any process/socket/pipe/fork/exec/signal operation, or move any
T/Q/C state. T remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.

## Author selection to bind

Kirill selected exactly:

```text
I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION
```

The formal signature is:

- `successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md`

Read it in full and recompute its hash. Also read and hash the full carried
chain, especially v2.1.10, v2.1.10.1, v2.1.10.2, v2.1.10.3 and their closures,
the A3/B1/C1/D1/K1 signatures, and
`reviews/officina_supervisor_v2_1_authorship_note.md`.

Every prior author closure is an untrusted self-assessment. The purpose of this
round is **binding**, not another choice and not self-review.

## Required deliverables

Create exactly two new files:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_10_4_p1_binding_closure.md`

Do not modify any governing artifact, signature, code, test, verifier, manifest,
prompt, prior review, or runtime object.

## B1. Emit one operative architecture

The binding must be self-contained as a literal correction over the carried
chain and leave **no operative P3/P4 branch**. Historical mentions may appear
only in a provenance/rejection table. Delete every unselected token, conditional
count, conditional process tree, conditional verifier rule, conditional test,
and phrase such as "under P4" from the operative contract.

The selected architecture is exactly:

- one clean Process-Control Server owns every PID and all process-control
  authority for `pid_mid`, controllers, workers, the first watchdog and every
  replacement watchdog;
- the supervisor holds opaque handles only and cannot express any PID;
- every watchdog is a PCS-created isolated role and a direct child of the PCS;
- supervisor death is detected by watchdog update-pipe EOF; the direct-parent
  `getppid()` detector is deliberately absent;
- watchdog death/replacement is observed and mediated through the PCS;
- PCS loss is unrecoverable whole-generation invalidity; no live-generation
  adoption exists;
- the second `t-pcs.v1` journal and non-redelivery of fd capabilities are
  accepted costs, not silently repaired promises.

Recompute one exact process tree, direct-parent/reaper table, handle model,
descriptor table, opcode enum, journal/ACK automaton, crash matrix, shutdown
route, import surface, verifier surface, and test matrix for P1 only.

## B2. Reconcile the v2.1.10.3 engineering corrections

Carry all P1-applicable corrections found in v2.1.10.3, even though P4 was not
selected:

1. The role-bootstrap imports exactly `{os, sys, fcntl}` because its own
   `F_GETFL` check requires `fcntl`; every related count and verifier rule must
   say three, never two.
2. `generic_harness.py` is the supervisor-side `t-pcs.v1` client and therefore
   its scoped allowlist must include `_socket`. It must still exclude `signal`,
   `_signal`, and `sys` unless the binding proves a different exact need.
3. Delete the global remediation rule that scans `/proc/self/fd` and closes
   everything outside a supposedly pinned set. The supervisor's legitimate fd
   set grows with live role handles, so that sweep is unsafe.
4. Re-audit the `POSIX_SPAWN_DUP2` consequence that destination descriptors are
   non-`CLOEXEC`. Give exact PCS-to-role file actions and prove no lock, socket,
   unrelated role fd, source fd, interpreter fd, or journal fd leaks into any
   role.
5. Keep the object-bound `-I -S -E -P`, empty-environment role bootstrap and
   removal of `PYTHONPATH`.

No P4-only clean-parented-watchdog step, watchdog PID in the supervisor, or
first-versus-replacement asymmetry may survive.

## B3. Repair the remaining SCM_RIGHTS cleanup statement

v2.1.10.3 correctly deleted the unsafe global fd sweep but still says that, if
the kernel installed more descriptors than the parsed ancillary vector, the
unreported descriptors would be "a resource fact, not an authority fact".
That classification is false: an installed `SCM_RIGHTS` descriptor is a
capability even if the generation is already invalid.

Give one exact fail-closed rule grounded in the pinned Linux semantics:

- state precisely what Linux does with excess SCM_RIGHTS descriptors when the
  ancillary buffer truncates, and identify the reviewer-verifiable primary
  interface fact on which the rule rests;
- close every descriptor actually returned in parsed control data exactly
  once;
- never close unrelated previously received role descriptors;
- if the interface cannot prove that every installed descriptor is either
  returned or kernel-closed, route to an immediate no-callback process exit and
  name the interval honestly as a possible transient **capability leak**, not a
  resource-only fact;
- account for concurrent code under the signed A3 same-UID procedural threat
  model without upgrading A3 into a security guarantee;
- preserve `MSG_CMSG_CLOEXEC`, `MSG_CTRUNC`, `MSG_TRUNC`, exact fd-count/type
  validation, and the no-redelivery rule.

Do not invent a global fd sweep, proxy, or capability-recovery protocol.

## B4. Bind C1, B1 and D1 honestly

The operative text must state, without softened wording:

- **C1:** P1 retains a dedicated freezer watchdog but intentionally reduces
  supervisor-death detection from two mechanisms to the update-pipe EOF
  mechanism. This is the author's selected trade, not a mechanically unchanged
  C1 implementation.
- **B1:** the client journal remains as signed; `t-pcs.v1` adds a separate
  control-plane journal. Byte replies are replayable, but fd-bearing replies
  cannot redeliver the same capability. An ACK loss therefore invalidates the
  generation rather than retrying the descriptor transfer.
- **D1:** no idle exit remains, but availability now depends on a mandatory PCS
  whose crash cannot be recovered by adoption. This is accepted fail-closed
  invalidity, not a scientific or resource outcome.
- **K1/A3:** their selected meanings and procedural limitations remain exactly
  carried. Nothing in P1 creates Q/C confidentiality or same-UID adversarial
  confinement.

## B5. Static implementability audit

Without executing anything, trace:

- caller → PCS → middle/supervisor and PCS → every role;
- exact socketpair/SCM_RIGHTS ownership at send, receive, ACK, timeout, replay,
  malformed ancillary, supervisor death, PCS death and shutdown;
- exact nine-operation (or correctly recomputed) protocol with no PID/fd/path
  field and no stale watchdog opcode semantics;
- first watchdog, repeated replacement, wedged watchdog, controller/worker
  stop/reap and every handle-release route;
- PCS journal installation, crash cuts, unresolved-generation refusal and
  no-adoption rule;
- every import and builtin/method-descriptor identity class already found in the
  carried chain;
- the full production-root count and source-hash manifest obligations;
- all exact numeric statements and test-row references.

If P1 cannot be made single-valued without another author decision or a signed
contract conflict, stop with an exact `BLOCKED_...` verdict. Do not choose a
repair on Kirill's behalf.

## B6. Review handoff

If and only if the P1 composite is mechanically single-valued and all counts,
tables and replacement indexes close, closure line 1 must be exactly:

```text
READY_FOR_OFFICINA_SUPERVISOR_P1_COMPOSITE_XY_REVIEW
```

The closure must include:

- exact replacement index over v2.1.10.3 and every earlier superseded P1 row;
- one-to-one B1-B6 disposition;
- one operative P1 constants/counts table;
- one process/fd/authority table;
- one crash/invalidity table;
- exact future implementation and verifier edit surface;
- weakest points against your own composite;
- byte/hash custody and confirmation existing files were untouched;
- three bounded questions each for independent X=Claude Code Opus 4.8 and
  Y=GPT-5.6 Sol, asking them to review identical bytes;
- explicit confirmation that the existing acceptance token remains unavailable
  until both lines confirm.

This author round authorizes no X/Y verdict, implementation, code/test edit,
verifier/manifest change, process or probe, T activation, entropy, E1/E2/E3
spend, Q/C work, datum, outcome, Proof, or claim movement.
