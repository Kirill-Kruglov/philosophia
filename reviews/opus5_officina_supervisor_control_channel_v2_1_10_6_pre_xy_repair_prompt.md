# Prompt for Claude Code Opus 5: repair the remaining P1 pre-X/Y Linux-process defects

You are **Claude Code Opus 5 acting only as the specification author**. You are
not an independent X-line or Y-line reviewer. Work in the local `philosophia`
repository. Do not edit any existing file. Do not implement code, run tests or
probes, execute any process/socket/pipe/fork/exec/signal/wait/prctl operation,
or move any T/Q/C state. T remains `NOT_ACTIVATED`; the programme claim remains
`OPEN`.

## Governing state

Kirill selected and signed:

```text
I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION
```

The current author layer is:

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_5_P1_PRE_XY_REPAIR.md`
- `reviews/opus5_officina_supervisor_control_channel_v2_1_10_5_p1_pre_xy_repair_closure.md`

Read those files in full and recompute their SHA-256 values. Read the complete
carried chain that they incorporate, especially v2.1.10, v2.1.10.3,
v2.1.10.4 and their closures/signatures. Treat every prior author verdict as an
untrusted self-assessment.

v2.1.10.5 closes the spawn-lock, watchdog-signal, authority-wording,
SCM_RIGHTS parser and no-callback-theorem defects. Preserve those closures.
Do **not** reopen P1, A3/B1/C1/D1/K1, the process topology, the output-capacity
selection, or the selected process-authority architecture.

## Two remaining pre-X/Y defects

### R1. Linux orphan adoption is not necessarily by `init`

The carried text repeatedly says that after the middle exits, the supervisor is
re-parented to and reaped by `init`, and that on PCS death roles are
re-parented to and reaped by `init`. This is not a total Linux statement.
Under `PR_SET_CHILD_SUBREAPER`, an orphan is re-parented to the nearest still
living ancestor subreaper; only if none exists does namespace init receive it.
Officina's statement that it does not itself call `PR_SET_CHILD_SUBREAPER` does
not prove that a contaminated caller or another ancestor is not already a
subreaper.

Repair this **without selecting a new architecture on Kirill's behalf**:

1. Replace every operative `init adopts/reaps`, `pid 1`, or equivalent absolute
   claim in the P1 chain with the exact nearest-living-child-subreaper,
   otherwise namespace-init semantics.
2. Recompute the direct-parent/reaper tables and every affected crash cut for:
   supervisor orphaning after `m9`, supervisor exit, PCS death, and role exit
   after PCS death.
3. State exactly what a contaminated ancestor that is a child subreaper can
   reap, including wildcard waits, and what information it may thereby steal.
4. Prove or reject the following proposed bounded interpretation: this does
   **not** grant that ancestor Officina process authority, because no PCS or
   supervisor decision uses the orphan supervisor's/role's reaped status or a
   numeric PID after custody is lost; supervisor loss is observed by the
   channel/EOF route, later death proof is object-bound `/proc` absence or
   zombie identity as already signed, and a PCS loss remains unrecoverable
   generation invalidity. If any carried decision actually relies on exclusive
   init reaping or on preservation of an exit status, identify it and stop with
   `BLOCKED_...` rather than silently changing architecture.
5. Do not add `prctl`, `ctypes`, a child-subreaper role, a long-lived middle,
   PID namespace, cgroup, new signal path, or new adoption/recovery protocol.
   Those would be architectural choices, not this bounded repair.
6. Keep the A3 same-UID procedural limitation honest: a contaminated ancestor
   may already kill, delay, or reap processes it becomes parent of. Do not
   upgrade the contract into adversarial confinement.

Ground the correction in the reviewer-verifiable Linux child-subreaper
interface semantics, naming the primary interface/man-page fact, without
executing a probe.

### R2. S-18 contradicts required `/proc/self/fd` verification

The carried S-18 says:

```text
no `/proc/self/fd` directory enumeration appears anywhere
```

But the same operative contract requires:

- role-side `A-5` to enumerate/check `/proc/self/fd` as a verification;
- the grandchild's pre-exec G-5 scrub to close inherited descriptors outside
  its exact slot set before importing project code;
- tests 442R and related descriptor-topology assertions.

The scientific/engineering intent was narrower: forbid the **supervisor receive
error handler's global remediation sweep**, which might close another live
handle, while retaining bounded construction-time scrubbing and read-only
topology verification.

Repair S-18 and every derived test/verifier sentence so the grammar is
single-valued:

1. Define exactly which roots/functions/phases may enumerate
   `/proc/self/fd`, and whether each may inspect only or may close descriptors.
2. Permit A-5's read-only exact-set verification.
3. Permit G-5 only as the clean grandchild's pre-project-import construction
   step, with its pinned keep-set and close rule; prove it cannot touch a live
   supervisor handle because it occurs before that process becomes the
   supervisor and acts only on its own inherited descriptor table.
4. Continue to forbid any `/proc/self/fd` enumeration/close sweep in the
   supervisor's SCM_RIGHTS receive cleanup, runtime error remediation, or any
   phase where unrelated live role handles coexist.
5. Preserve v2.1.10.5's parser-local `scm_detach_fds()` cleanup and immediate
   no-callback exit rule. Do not replace either with a sweep.
6. Recompute S-18, rows 425/445/442R and every other affected exact test count
   or reference. No sentence equivalent to "nowhere" may survive if A-5/G-5
   remain required.

## Required deliverables

Create exactly two new files:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_6_PRE_XY_REPAIR.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_10_6_pre_xy_repair_closure.md`

Do not modify any governing artifact, signature, code, test, verifier, manifest,
prompt, prior review, or runtime object.

The repair must be a literal, bounded correction over v2.1.10.5 with an exact
replacement index. It must explicitly confirm that all five F1--F5 repairs,
the P1 selection, and all previously closed A3/B1/C1/D1/K1 meanings remain
unchanged.

## Static audit and verdict

Without execution, audit every occurrence of `init`, `pid 1`, `reparent`,
`reap`, `subreaper`, `S-18`, `/proc/self/fd`, `A-5`, `G-5`, rows 425/442R/445,
and "global sweep" in the operative carried chain. The replacement index must
make it mechanically clear which historical clauses no longer govern.

If either repair requires a new author choice, new process, new syscall/import,
or changes the signed P1 authority topology, stop with an exact `BLOCKED_...`
verdict and explain why. Do not choose.

If and only if both defects are closed without reopening architecture, closure
line 1 must be exactly:

```text
READY_FOR_OFFICINA_SUPERVISOR_P1_PRE_XY_REPAIR_FINAL_CONFIRMATION
```

The closure must include:

- exact replacement index and one-to-one R1/R2 disposition;
- corrected parent/reaper/authority table;
- corrected `/proc/self/fd` phase/permission table;
- no-regression table for v2.1.10.5 F1--F5 and the signed cells;
- exact future implementation/verifier/test surface;
- byte/hash custody and confirmation existing files were untouched;
- one bounded yes/no question each for independent X=Claude Code Opus 4.8/5
  and Y=GPT-5.6 Sol, asking them to confirm identical repair bytes;
- explicit confirmation that no acceptance token is available from this author
  round.

This author round authorizes no X/Y verdict, implementation, code/test edit,
verifier/manifest change, process or probe, T activation, entropy, E1/E2/E3
spend, Q/C work, datum, outcome, Proof, or claim movement.
