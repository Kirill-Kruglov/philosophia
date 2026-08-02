# Prompt for Claude Code Opus 5: architectural Officina supervisor v2.1.10 repair

Act as the **specification author, never an independent reviewer**. Both
independent lines rejected v2.1.9. Their common result governs: repository AST
and `/proc/self/cmdline` cannot establish a clean Python runtime or exclusive
reaping. Do not repair that theorem with another observation or stronger prose.

Work in `philosophia` at or after commit
`ad3d0396f4a6fe9c14168062e0b66a24a8fe0df4`. Existing artifacts are immutable.
Read the complete supervisor chain, signed harness/batch composites, author
signatures and both v2.1.9 reviews. Recompute:

```text
1468c9ab1806c1eb25523e6a9fd8567592076f0dc74418ca698a52f933c7f3b0  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md
1970986325c75e8f4c2dd72e57e0640ae88b165f3556920e85cae7efc8cc93be  reviews/sol_officina_supervisor_control_channel_v2_1_9_final_confirmation.md
f49dcbf9900c0d3fe2e45abbc28193d8b4b4c20c8640dfab508aff15dcc90984  reviews/opus_officina_supervisor_control_channel_v2_1_9_final_confirmation.md
```

Static authoring only. Run no code, test, probe, fork/signal/subprocess
experiment, or Officina process. Change no existing file, implementation,
verifier, runtime state, activation, entropy, T/Q/C object, datum, or claim.
Create only the two named deliverables.

## Binding findings

Close the union, using the stricter disposition where the lines differ:

- **C219-1 / X-F1 Critical:** argv is not clean-exec or runtime-executor
  evidence. `.pth`, site/user customization, at-fork/audit/import/trace hooks,
  monkeypatching, retained callables and native extensions survive every v2.1.9
  gate relevant to the counterexample.
- **M219-1 Major:** the current/future verifier does not establish a closed
  runtime executor or call-target theorem.
- **M219-2 / X-F2 Major:** `WAIT_ONE` totality and
  `B-CONTRADICTED` unreachability depend on the failed premise; unexpected
  callable results/exceptions are not total.
- **m219-1 Minor:** 16 hex digits are false over the stated Linux architecture
  scope because Linux MIPS uses `_NSIG = 128` and renders 32 digits.

Preserve the accepted progress: the abstract W-1…W-5 automaton, the resolved
sole-importer contradiction, short-mask rejection principle, `SIGCHLD` full
disposition reset, `ECHILD`/`ESRCH` non-death, ten-row identity table,
ownership-gated signals, no T3, stage-M `m0`/`rel1` proof, object-bound barriers,
bound sweep, A3/B1/C1/D1/K1, and all scientific/resource boundaries.

## Required architectural route

Use **one named, site-free, environment-isolated process-control bootstrap** as
the primary repair. Do not retain v2.1.9's clean-runtime theorem for
`generic_harness.py`, and do not introduce pidfd unless the isolated route is
proved impossible. If you do use pidfd, acquisition must be atomic with process
creation; `pidfd_open(numeric_pid)` after fork does not close the reaping/reuse
race and is forbidden as a purported repair.

### A1 — construct, do not infer, the clean runtime

Specify one exact new process-control surface, including its canonical path,
owner and invocation. The expected shape is a minimal standalone bootstrap
script executed by a fresh interpreter with exact isolation flags
`-I -S -E -P` (or a strictly stronger reviewed invocation), using an absolute,
object-bound script path. It must:

1. run no `site`, `.pth`, `sitecustomize`, `usercustomize`, user environment,
   project package import, backend, torch, native extension or arbitrary hook
   before child creation;
2. have a closed, minimal stdlib import set and no dynamic imports;
3. bind genuine process primitives immediately from that clean import state and
   never look them up again through mutable module attributes;
4. contain the process-control/fork/wait/signal state machine itself rather than
   call back into a contaminated `generic_harness.py` runtime;
5. validate its request through a closed canonical wire schema whose fields
   cannot name code, modules, callbacks, paths outside the pinned set, or
   process primitives;
6. exec the appropriate reviewed role only after the custody/fork boundary in a
   way that cannot run parent-side Python at-fork callbacks;
7. state exact fd inheritance, close-on-exec, lock, record, crash, restart,
   parent/child ownership and handshake semantics.

The dirty caller may launch the bootstrap, but no state, callback, monkeypatch,
at-fork registry, audit/import hook, native thread, or callable reference from
that caller may cross the `execve` boundary. Explain why a competing waiter in
the caller cannot reap the bootstrap's child: direct-child ownership and process
boundaries must be explicit.

This necessarily supersedes the v2.1.9 “one module/sole executable root” repair.
Name the new root/path/import topology and every affected signed sentence
loudly. It is an engineering amendment, not a scientific author cell. Do not
leave the path or invocation as an implementation choice.

### A2 — closed primitive and runtime theorem

Replace the old AST-equals-runtime theorem with a theorem whose premises follow
from A1's construction. Enumerate:

- exact interpreter identity/version/build and isolation-flag readback;
- exact allowed imports and whether each is pure Python or native;
- every operation before the first child and whether it can register at-fork
  callbacks or create a native task;
- locally bound genuine `fork`/`waitpid`/`kill`/`killpg`/signal primitives,
  their identity validation, and prohibition on later rebinding;
- Python's own internal at-fork callbacks and why none can create/reap a child;
- all asynchronous entries and signal dispositions;
- every public/private entry and why only the constructed bootstrap gets
  process authority.

The future verifier algorithm must be exact, not “add a probe”: name the AST and
manifest invariants, alias/data-flow rules, import graph, prohibited syntax,
runtime preflight fields, source hashes, and fail-closed result for each
violation. If a property cannot be decided statically, bind it through the clean
construction or classify it as a runtime preflight; do not claim the existing
verifier already proves it.

### A3 — total process primitives and `WAIT_ONE`

Carry the accepted abstract W-1…W-5 tables, but bind them to A1's locally held
genuine primitives. Add a total structural classifier for every returned Python
object and every `BaseException`: wrong tuple arity/type, wrong positive pid,
negative value, malformed status, `SystemExit`, `KeyboardInterrupt`, and any
unexpected exception must have one safe continuation. Only a genuine targeted
positive return sets `REAPED`.

Re-prove W-5 with a child stopped between m8 and m9, all deadline cuts and
process exit. Re-prove T1/T2/B, zombie/P3, restart and second launcher. Once A1
is established, prove `B-CONTRADICTED` is outside supported history without
circular reference; otherwise provide a real durable resolver.

### A4 — honest platform scope and mask width

Do not repeat the all-Linux 16-digit claim. The preferred minimal repair is to
pin this supervisor bootstrap to the actual platform identity:

```text
Linux x86_64, CPython 3.12.3, exact reviewed build identity
```

using existing primitives such as `os.uname()` where possible, with 16 digits
then justified only inside that scope. Explain why this narrows an engineering
process-control implementation and does not alter the signed off-CPU scientific
device policy on the present x86_64 host. If you instead derive width, specify
an exact kernel-supported derivation and fail closed on every mismatch; do not
silently add `signal.NSIG` or a new architecture.

## Required evidence in the documents

Provide:

1. literal v2.1.9 → v2.1.10 replacement index;
2. one-to-one disposition of both lines' findings;
3. exact process tree from contaminated caller → isolated bootstrap → middle →
   supervisor/role, with direct-child/reaper ownership at every edge;
4. byte-exact invocation, argv/environment policy and canonical request schema;
5. import/native-operation/callback/at-fork inventory before child creation;
6. genuine-primitive binding and total return/exception tables;
7. exact future verifier and manifest changes;
8. crash/cut matrix and replay of both v2.1.9 counterexamples;
9. platform/mask table including x86_64 and the explicitly unsupported MIPS
   route;
10. no-regression and exact future implementation edit surface, preserving the
    current Cursor work unless a named new bootstrap file is added.

State the weakest points against yourself. Ask each independent line at most
three bounded questions focused on clean construction/runtime closure,
primitive/wait/B totality, and root/verifier/platform containment.

## Deliverables

Create exactly:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_10_closure.md`

Alter nothing else. Closure line 1 exactly one of:

- `READY_FOR_OFFICINA_SUPERVISOR_V2_1_10_FINAL_XY_CONFIRMATION`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_10_AUTHOR_CELL`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_10_CONTRACT_CONFLICT`

Use `READY` only for one bit-exact implementable route. No implementation or
token is authorized by authoring. Confirm no execution, entropy, activation,
T process, spend, Q/C, datum, outcome or claim movement; T `NOT_ACTIVATED`,
claim `OPEN`, amendment token unavailable pending fresh X/Y confirmation.
