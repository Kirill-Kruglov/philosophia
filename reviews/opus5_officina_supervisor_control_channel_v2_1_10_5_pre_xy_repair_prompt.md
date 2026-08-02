# Prompt for Claude Code Opus 5: repair P1 composite before X/Y review

You are **Claude Code Opus 5 acting only as the specification author**. You are
not an independent reviewer. Work in the local `philosophia` repository. Do
not modify any existing file. Do not implement code, run a test or probe, or
execute any process/socket/pipe/fork/exec/signal operation. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.

## Governing input

Read and hash:

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md`
- `reviews/opus5_officina_supervisor_control_channel_v2_1_10_4_p1_binding_closure.md`
- `successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md`
- the full carried v2.1…v2.1.10.3 chain and signatures cited by the binding.

The P1 author selection remains fixed. This is a bounded pre-X/Y repair of four
concrete contradictions found by Codex's static check. It is not a new author
choice and must not reopen P3/P4.

## Required deliverables

Create exactly two new files:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_5_P1_PRE_XY_REPAIR.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_10_5_p1_pre_xy_repair_closure.md`

Do not edit the binding, its closure, code, tests, verifiers, manifests,
signatures, prompts, prior reviews, or runtime state.

## F1 — `SPAWN.lock` leak proof is false

The binding's §P1B.3.3 simultaneously says:

- the PCS's `SPAWN.lock` descriptor is deliberately non-`CLOEXEC`;
- every PCS descriptor outside 3–8 is `CLOEXEC`;
- controller/worker/watchdog file actions close only mapped destinations and
  their hoisted sources;
- a leaked lock at another number would merely be caught by role `A-5`.

That is not an exact descriptor map. The PCS-side table does not give the lock a
3–8 slot: 3–8 are request, reply, runtime root, package root, PCS source and
interpreter. A kernel-numbered non-`CLOEXEC` lock outside that range survives
every controller/worker/watchdog `execve` at its original number. `A-5` then
refuses after the leak; it does not make the production spawn work or prove the
claimed map.

Apply one exact repair, unless it conflicts with a signed invariant:

1. acquire/retain the PCS's original `SPAWN.lock` descriptor with
   `FD_CLOEXEC` set (prefer creation with `O_CLOEXEC`, otherwise an exact
   pre-spawn `F_SETFD` step with readback);
2. forks inherit that descriptor, but every ordinary role `execve` closes it;
3. on the unique supervisor-grandchild path, immediately before the reviewed
   supervisor `execve`, perform an exact collision-free `dup2(lock_fd, 3)`
   (which clears `CLOEXEC` on destination 3), then close the original source;
4. no controller, worker or watchdog file-action vector maps the lock;
5. after every role `execve`, the fd set must be exact without depending on a
   post-exec refusal as the normal route.

Recompute the PCS descriptor table, process tree steps, stage-M/grandchild
handoff, role maps, file actions, crash cuts, verifier rules and tests. If the
suggested repair conflicts with the carried fork-shared-lock theorem, stop and
name the exact conflict rather than improvising.

## F2 — PCS authority wording overstates the process tree

The binding says the PCS "holds every PID in the system" and is the "sole
holder of every PID", but its own tree says the supervisor grandchild is a
child of `pid_mid` until `m9`, then is re-parented to `init`. The PCS is not the
supervisor's direct parent or reaper and cannot prove its death by direct
`waitpid(supervisor_pid)`.

Replace every universal claim with the exact boundary selected by the
signature:

- PCS directly owns/reaps and holds numeric process authority for `pid_mid`,
  every controller, every worker and every watchdog;
- the supervisor receives no PID and exercises no numeric process authority;
- the PCS observes the supervisor through the `t-pcs.v1` peer/channel and may
  have group authority only through an already-proved `pid_mid`/group route;
- the supervisor itself is not silently added to the PCS direct-child set;
- the caller owns/reaps only the PCS, and `init` reaps the orphaned supervisor.

Recompute every process/authority table and every phrase such as "every PID".
Do not change the selected P1 meaning; make the prose match the actual tree.

## F3 — watchdog signalling contradiction

The v2.1.10.4 replacement index row 16 says the carried first-ack timeout becomes
a PCS `SIGNAL_ROLE + REAP_ROLE` pair. Operative §P1B.4, §P1B.7.5 and tests 440,
455, 456 say `SIGNAL_ROLE` is refused for `WATCHDOG` and **no signal is sent to
a watchdog on any path**.

One rule must govern. Retain the operative selected P1 rule:

- close the watchdog update write end through the exact owner;
- wait through `REAP_ROLE` for `REAPED_POSITIVE`;
- timeout/wedge routes to `WATCHDOG_UNREAPED` and process invalidity;
- no TERM/KILL/STOP/CONT/PROBE to a watchdog.

Correct the replacement index, all carried citations, crash/shutdown rows and
tests. Search the whole operative composite for any surviving watchdog signal.

## F4 — "no callback before `_exit`" is not mechanically true

The receive side is the contaminated Python supervisor. If `_recvmsg` raises,
making `_exit_` the first statement of the `except` body does **not** prove that
no Python trace/profile/audit hook, signal handler, exception machinery,
finalizer, or other same-process callback can run between the C call's failure
and that statement. The binding itself places this process inside the signed A3
procedural residual.

Repair the claim without inventing confinement:

- retain `_exit_` as the first **contract-authored handler statement** and
  forbid any explicit cleanup/callback/unwind logic in that handler;
- withdraw every absolute "NO callback/finalizer/unwinding" theorem for the
  contaminated receiver;
- name the interval from possible FD installation through actual process exit
  as a transient capability exposure in which same-process hooks/threads may
  run under A3;
- state that the contract offers procedural discipline, not adversarial
  same-process security, and that this surface is non-citable and never Q/C
  evidence;
- adjust `S-19` and its tests so they prove only the AST property they can
  actually prove;
- preserve the kernel `scm_detach_fds()` claim as reviewer-verifiable, not
  author-proven evidence.

If truthful containment requires moving `recvmsg` into a clean proxy process,
that is a new architecture not authorized by P1; stop with a precise
`BLOCKED_..._AUTHOR_CELL` rather than introducing it.

## F5 — literal consistency sweep

Fix the duplicated `B-4. ON ANY VIOLATION...` line in §P1B.6.3. Then perform a
literal static sweep of the correction for:

- exact P1-only option tokens;
- exact parent/reaper claims;
- exact lock `CLOEXEC` state at each process and exec boundary;
- zero watchdog signal paths;
- nine uniform operations and their descriptor vectors;
- five roots and 6/3/17 import counts;
- no global `/proc/self/fd` remediation sweep;
- no absolute no-callback claim in the contaminated receiver;
- exact test-row and replacement-index references.

## Verdict and handoff

If F1–F5 close without a new author decision or signed conflict, closure line 1
must be exactly:

```text
READY_FOR_OFFICINA_SUPERVISOR_P1_V2_1_10_5_XY_REVIEW
```

The correction and closure must contain:

- literal replacement index over v2.1.10.4;
- one-to-one F1–F5 disposition;
- corrected process/fd/authority and crash tables;
- corrected verifier and test delta;
- hashes and proof existing files were untouched;
- weakest points against your repair;
- three bounded questions each for independent X=Claude Code Opus 4.8 and
  Y=GPT-5.6 Sol on the identical corrected composite.

If any issue is not mechanically resolvable, emit a precise `BLOCKED_...`
verdict. Do not self-confirm. The acceptance token remains unavailable until
fresh X and Y confirmation of identical bytes.

No implementation, code/test/verifier/manifest edit, process/probe, activation,
entropy, E1/E2/E3 spend, Q/C work, datum, outcome, Proof, or claim movement is
authorized.
