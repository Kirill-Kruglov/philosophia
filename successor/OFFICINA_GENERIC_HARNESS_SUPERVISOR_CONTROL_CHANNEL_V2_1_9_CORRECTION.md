# Officina supervisor and control-channel amendment — v2.1.9 bounded correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`.

> ## WHAT THIS LAYER CHANGES, STATED FIRST
>
> 1. **A single supported production entry topology is pinned and mechanically
>    gated before the first fork** (§V219.2). The CLI bootstrap is reachable in
>    production only from a fresh `execve` of the sole root as `__main__`; a new
>    step `c3t` verifies single-taskness, zero caught signals, and the sole-root
>    `cmdline` from the kernel. Every other entry **refuses before fork**. The
>    sole-reaper premise stops being a prohibition and becomes a theorem about
>    the process's executor set (§V219.2.2).
> 2. **All caught signal dispositions are reset to `SIG_DFL` at `c3n`** and
>    `SigCgt == 0` is verified, so **no asynchronous callback can enter this
>    task** for the whole ownership lifetime. This uses **no new `signal`
>    member**: the signal numbers are derived from the kernel's own mask.
> 3. **One shared wait automaton `WAIT_ONE` governs all five wait sites**
>    W-1…W-5 (§V219.3), each with an exact entry condition, existing-constant
>    deadline, transition, cleanup, lock behaviour, and continuation.
> 4. **`src/philosophia/officina/generic_harness.py` is the sole executable root
>    *and* the exact permitted importer of `signal`** (§V219.4). The signed
>    harness §9 no-`signal` sentence, §V2.10's byte-unchanged `verification.py`
>    clause, and v2.1.8 §V218.1.2's forbidden-importer row are **explicitly
>    superseded**. There is no second module and no undeclared dependency.
> 5. **`B-CONTRADICTED` is proved unreachable in every supported execution** and
>    is reclassified as a non-returning safety sink outside supported history
>    (§V219.5).
> 6. **Signal masks are width-checked before conversion** (§V219.6); short,
>    empty, prefixed, or over-wide masks route to `VERIFY_INCONCLUSIVE` and no
>    fork occurs.
>
> **Zero new numeric constants, resource values, schemas, records, tokens,
> commands, events, or scientific choices. No new author-choice cell.** The
> import-allowlist delta remains exactly the one member `signal` named in
> v2.1.8.

**Authorship and provenance, stated literally.** This correction was written by
**Claude Code Opus 5 acting only as the specification author**, because Claude
Code Fable 5 was unavailable. The same author line wrote v2.1 through v2.1.8.
It is **not** an independent X-line or Y-line review of its own bytes and must
never be counted as one, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` records. Every author
closure in the chain — including this layer's — is an untrusted self-assessment.

**Review state of v2.1.8, recorded exactly, and the disagreement resolved.**
The X line returned `CONFIRM_OFFICINA_SUPERVISOR_V2_1_8_X`; the Y line returned
`REVISE_OFFICINA_SUPERVISOR_V2_1_8` with C218-1 (Critical), M218-1, M218-2,
M218-3 (Major) and m218-1 (Minor). **The Y verdict governs and every Y finding
is treated as sound.** §V219.1 records why the X confirmation was reasonable on
the facts it re-derived and why it was nonetheless insufficient against Y's
counterexamples. **No part of this layer is defended by appeal to the X
verdict**, and neither review is author support for these new bytes: v2.1.9
requires a **fresh** independent X-line review and a **fresh** independent
Y-line review of its own bytes.

This is a **narrow replacement layer** over
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md`
(v2.1.8), which layers over v2.1.7 … v2 — all ten preserved unedited as review
evidence. **Everything not named in the §V219.0 replacement index carries
forward verbatim.**

Signed author cells embedded; **none reopened, weakened, or reinterpreted**:

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

**Repairs both lines independently accepted, carried forward byte-for-byte**
(§V219.9 audits each): the CPython/Linux `SIGCHLD := SIG_DFL` full-disposition
replacement and its `execve`/`fork` provenance analysis; `ECHILD` and `ESRCH`
never proving death; the ten-row identity table I-1…I-10; ownership-gated
signals; the deletion of `T3`; the `T1`/`T2`/`B` no-discard invariant; the
stage-M causal proof at `m0`/`rel1` and the fork-shared lock; §V217.1's
object-bound observation and both revalidation barriers; §V217.4's
bound-language sweep; and every signed A3/B1/C1/D1/K1 and harness /
batch-settlement science and resource boundary.

Author token candidate, still **not signable**, and not made signable here:

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

Creates nothing executable. Edits no code, verifier, test, contract, signature,
review, prompt, or runtime artifact. Starts no process. Creates no entropy,
activation, capability, world, learner, candidate, datum, Q/C object, capacity
artifact, custody disposition, result manifest, or outcome. Authorizes no
implementation. T remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.

## Governing hashes (recomputed for this correction)

```text
746bcf3694a67d04eacaec66190cf68cb92ac0070ec3d8cb24abf6eb22efee0c  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md
7ef8e4d3ac8f281dd50191e81d2760ed4467648b45ed2b17f6ce2012e4d017d4  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_5_CORRECTION.md
e4aa9ef4f0de2fe705d54cb7ac016212098cfe71b8575ef2b435e8c9b09f5609  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_6_CORRECTION.md
789732476938ca8c1436eebb49e54a1f994c2c000b7689e1eb9aad082f6871a8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_7_CORRECTION.md
33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md
2e4bee2305bafb5825a6ac1cca4d131dcbdf730aa048f29c7023cf679c9936e6  reviews/opus_officina_supervisor_control_channel_v2_1_7_final_confirmation.md
5c82f7c1894d3e76239ee26a611731d102a2891486a9c2d667ce9738956d533b  reviews/sol_officina_supervisor_control_channel_v2_1_7_final_confirmation.md
e879b39cf6e22c93bcf309ed4a15a7a1f56e00fbcc17fd8cfc2398b04aec099a  reviews/opus_officina_supervisor_control_channel_v2_1_8_final_confirmation.md
663184378fc6fa48c5d83e96cf659d2d9eb58f67a18fd8c7ba0efcb528caea34  reviews/sol_officina_supervisor_control_channel_v2_1_8_final_confirmation.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e  src/philosophia/officina/verification.py
```

`verification.py` is recorded **unamended**; this correction does not edit it.

## Engineering constants (replaces v2.1.8's "Engineering constants")

**Zero new constants, durable objects, paths, durable schemas, schema keys,
wire enum tokens, refusal or `INVALID` tokens, public commands, private argv
tokens, signed events, resource values, roots, or archival-set changes.** The
labels `TOPOLOGY_OK`, `WAIT_ONE`, `OWNED`/`CONTRADICTED`/`REAPED`, `T1`/`T2`/`B`
and the observation records of §V217.1 are internal control-plane labels: never
persisted, never transmitted, never a durable schema, never a wire token.

**Exactly one import-allowlist delta, unchanged from v2.1.8: `signal`.** Its
permitted API surface is unchanged at **two callables and one sentinel** —
`signal.signal`, `signal.getsignal`, `signal.SIG_DFL` — plus the constant
`signal.SIGCHLD`. §V219.2.4's reset pass introduces **no additional member**:
the signal numbers it resets are derived from the kernel's own `SigCgt` mask.
`select`, `selectors`, `ctypes`, `sys`, `socket`, `threading`, `_thread`,
`multiprocessing`, `concurrent`, `asyncio`, `atexit`, and `gc` remain **outside**
the allowlist and are not added.

Deadlines used: `T_SUPERVISOR_POLL_INTERVAL_NS` and
`T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` only, both already signed. **No new numeric
constant is introduced anywhere in this layer**, which is why no
`BLOCKED_..._AUTHOR_CELL` verdict is emitted.

---

## V219.1. The X/Y disagreement, resolved explicitly

Both reviews re-derived the same Linux/CPython facts and reached opposite
verdicts. This layer records why, because the reason determines the shape of
the repair.

| Question | X line | Y line | This layer's finding |
|---|---|---|---|
| Does `signal.signal(SIGCHLD, SIG_DFL)` on the pinned CPython clear an inherited `SIG_IGN` **and** an inherited `SA_NOCLDWAIT`? | Yes, by full `sigaction` replacement | Yes, identically | **Agreed and carried.** Both lines verified `PyOS_setsig` independently; the Y line cited CPython 3.12.3 `signal_signal_impl`/`PyOS_setsig` and `sigaction(2)` directly. |
| Is `ECHILD`/`ESRCH` ever death? | No | No | **Agreed and carried.** |
| Is the ten-row identity table total? | Yes | Yes | **Agreed and carried.** |
| Is `T3` gone and is the stage-M causal proof correct? | Yes | Yes | **Agreed and carried.** |
| Is the **sole-reaper** premise mechanically established? | Treated as established, because the *contract* forbids every wildcard reaper in the CLI and the prohibition is statically testable over Officina source | **No** — the prohibition governs Officina source, not **inherited host state**; an in-process host thread can wildcard-reap between `IDENTITY_OBSERVE` and `os.kill` | **Y is right.** §V218.2.6 was a rule about *what the implementation may contain*, and v2.1.8 permitted an in-process entry, so it never constrained *what the process already contained*. A static search of our own source cannot exclude a thread the host created before our first instruction. |
| Are W-2…W-5 total? | Judged sound because each is a targeted `waitpid` under an existing route | **No** — targeting is not totality; `(0,0)`, `EINTR`, `ECHILD`, other errno, and the `m8`-before-`m9` race have no continuation | **Y is right.** v2.1.8's §V218.2.6 explicitly said "no route's behaviour changes", which **preserved** the gaps it enumerated. |
| Is the importer topology implementable? | Judged consistent, because "the harness imports no `signal`" and "the CLI bootstrap imports `signal`" were read as claims about different components | **No** — §V2.10 and §Z3.3 put the CLI in `generic_harness.py`, so the two claims are about the **same file** | **Y is right.** Module imports are file-level facts. The X reading required a second module that no layer names. |
| Is `B-CONTRADICTED` acceptable? | Yes, as an honest fail-closed sink reachable only under a contract violation | **No**, because the competing reaper was not excluded, so it is reachable from a *supported* history and has no lawful next action | **Y is right, conditionally.** The X judgment was sound **given** an established sole-reaper premise; it fails exactly because that premise was not established. Closing C218-1 is therefore a precondition for R4, not independent of it. |
| Do short `/proc` masks pass verification? | Not examined at the grammar level | **Yes, they do** — `SigIgn: 0` satisfies V3–V5 | **Y is right.** The grammar accepted any non-empty hex string. |

**Why the X confirmation was reasonable.** It correctly and independently
re-derived every *disposition-reset* fact — the `sigaction` semantics, the
`execve`/`fork` provenance asymmetry, the `SigIgn`/`SigCgt` readback limits, the
`SA_NOCLDWAIT` gap, the pre-fork placement, and the per-attempt reset — and
those facts genuinely closed the two inherited v2.1.7 findings that were about
**dispositions**. On the *reaper* half it applied the criterion "does the
contract forbid every wildcard reaper in the CLI, and is that statically
testable?", answered yes, and stopped.

**Why it was insufficient.** The correct criterion is "can a wildcard reaper
**exist in this process** at the instant of the fork, whatever the contract
says about our source?" v2.1.8 answered that only for code the contract writes,
and its own §V218.2.4 pinned nothing but main-thread eligibility, which implies
neither single-taskness nor exclusive wait ownership. The same gap propagated
to M218-3, because the sink's acceptability was argued from the unestablished
premise. **The repair below therefore starts at C218-1 and lets R4 follow from
it**, and nothing in this layer is justified by the X verdict.

---

## V219.0. Exact replacement index (v2.1.8 → v2.1.9)

**Nothing else moves.** Everything in v2.1.8 and in every layer it carries — in
particular **§V218.2.2** (the `NORMALIZE_REAPING_STATE` operation and its
`sigaction` analysis), **§V218.3 in full** (ownership, the PID-reuse proof, the
ten-row identity table, `SIGNAL_ATTEMPT`, the TERM→KILL schedule, the `c5`/`c6`/`c7`
mapping), **§V218.4.1** (the no-discard invariant), **§V218.4.2**'s `T1`/`T2`
bodies and terminal-selection rule, **§V218.4.3**, **§V218.4.4**, **§V218.5 in
full** (the corrected causal trace), **§V217.1 in full**, **§V217.4 in full**,
§V216.2, §V216.4.1, §V216.5, and the entire carried
§V216/§V215/§V214/§U/§N/§Z/§W/§V2 chain — carries forward verbatim except at the
rows below.

| v2.1.8 (or carried) locus (exact sentence / clause / block / row) | Action in v2.1.9 |
|---|---|
| §V218.2.1's step-list extension `c3n` and its five pinned placement properties | **extended** by §V219.2.3 (a new step `c3t` immediately precedes `c3n`; `c3n` gains the reset pass and the re-verification) |
| §V218.2.2's `NORMALIZE_REAPING_STATE` block | **extended** by §V219.2.4 (the derived-mask reset pass runs first; the `SIGCHLD` call and all of its `sigaction` analysis are unchanged) |
| §V218.2.3's `VERIFY_REAPING_STATE` steps `V1`–`V7`, in particular `V3`'s clause "its value not a non-empty string of hexadecimal digits" and `V4`'s conversion | **replaced** by §V219.6 (the mask grammar and width rule; conversion only after the width test) and §V219.2.5 (the post-reset re-verification) |
| §V218.2.4's sentence "`c3n` executes in the CLI process's **main thread of the main interpreter**. The CLI creates no thread … and runs no sub-interpreter." | **replaced** by §V219.2.1–§V219.2.3 (main-thread eligibility is retained but is **no longer** offered as evidence of single-taskness or of exclusive wait ownership) |
| §V218.2.6's **SOLE-REAPER CONTRACT** paragraph and its four bullets | **replaced** by §V219.2.2 (the executor-set theorem) and §V219.2.6 (the verifier-enforced source/call-graph rule); the prohibition is retained but is no longer load-bearing on its own |
| §V218.2.6's five-row permitted-wait-site table and its sentence "W-1 through W-5 are **mutually exclusive per attempt**" | **replaced** by §V219.3 (one shared classifier plus five full instantiation tables); mutual exclusivity is restated as a proved property, not an assertion |
| §V218.1.2's **PERMITTED SIGNAL SURFACE** block, in particular its `Importing module` row and its `Forbidden importers` row naming "the generic harness" | **replaced** by §V219.4.1 (`generic_harness.py` is the sole root **and** the sole permitted importer) |
| §V218.1.2's third carried consequence and §V218.1.4's table row 1 | **extended** by §V219.4.2 (the additional superseded loci: signed harness §9's no-`signal` sentence, §V2.10's byte-unchanged `verification.py` clause, and §V2.10's "Allowlist delta: **none**") |
| §V218.1.3's §S7 probe obligation | **replaced** by §V219.4.3 (the containment probe restated for the sole-root importer) |
| §V218.4.2's `B` block, sub-mode definitions, and exit list | **replaced** by §V219.5.2 (`B-OWNED` retained unchanged in substance; `B-CONTRADICTED` reclassified as a non-returning safety sink outside supported history) |
| §V218.4.5's residual 3 | **replaced** by §V219.5.3 |
| §V218.4.4's table row "`SPAWNING.json` + `SPAWN.lock` held by a CLI in `B`" | **extended** by §V219.5.4 (`s5` is named as a **consequence**, explicitly **not** a resolver) |
| §V218.6's rows for `c3n` verification outcomes and for the `B` states | **replaced**/extended by §V219.7.3 |
| §V218.7 test rows **219**, **220**, **223**, **224**, **233**, **234** | **replaced** by §V219.8; rows 241–272 added |
| §V218.9's "Two-implementer determinacy" and "Compatibility classification" paragraphs | **replaced** by §V219.11 |
| carried §V2.10 clause "Frozen files (byte-unchanged): `runtime.py`, `ledger.py`, `checkpoint.py`, **`verification.py`**, `activation.py`, …" and clause "Allowlist delta: **none**." | **replaced** by §V219.4.2 and §V219.10 (exactly one string added to `ALLOWED_ABSOLUTE_IMPORTS` plus the §S7 containment probe; every other frozen file stays byte-unchanged) |
| carried signed generic-harness §9 clause "it uses no `signal`/`threading`/`multiprocessing`/backend import" | **superseded, narrowly and explicitly**, by §V219.4.2 — `threading`, `multiprocessing`, and backend imports remain forbidden; **only** the `signal` conjunct is replaced, and only for the five names of §V219.4.1 |
| carried §V218.2.4 sentence "The CLI creates no thread (`threading` is outside the allowlist and is not added) and runs no sub-interpreter." | **retained**, and **re-grounded**: §V219.2.6 shows this is enforced by the signed verifier over the reachable production sources, not by prose |

---

## V219.2. Mechanically exclusive reaping (R1)

Closes **C218-1**. The v2.1.8 defect was structural: it wrote a rule about what
Officina source may contain and used it as a premise about what the *process*
contains. This section replaces that with a topology that is (a) pinned to one
supported shape, (b) verified from the kernel before the first fork, and (c)
**preserved by construction** — not re-observed — for the whole ownership
lifetime.

### V219.2.1 The single supported production entry topology

There is **exactly one**. No alternative, no fallback, and no design fork.

> **SUPPORTED PRODUCTION TOPOLOGY (normative).** The CLI bootstrap steps
> `c1`–`c18` execute only in a process that satisfies all four of:
>
> **P-1 — sole-root program.** The program image loaded by the most recent
> `execve` is the signed sole root
> `src/philosophia/officina/generic_harness.py`, entered as `__main__` through
> the already-pinned invocation `python -m philosophia.officina.generic_harness`
> (§V2.10's argv rule and §Z3.3's fixed layout, both carried unchanged).
>
> **P-2 — single task.** The process's thread group contains exactly one task,
> which is the calling task.
>
> **P-3 — no catching disposition.** No signal in the process has a catching
> handler, so no asynchronous callback can enter this task.
>
> **P-4 — normalized child reaping.** `SIGCHLD`'s disposition is `SIG_DFL` with
> neither `SA_NOCLDWAIT` nor a catching handler (v2.1.8 §V218.2.2, carried).
>
> **In-process entry into `c1`–`c18` is removed from the production
> authority.** A caller that reaches the bootstrap without satisfying P-1…P-4
> does not inherit that authority: it **refuses before `c4`** (§V219.2.7).

`execve` is what makes P-1…P-3 attainable rather than merely assertable: on
Linux it terminates every other task in the thread group, destroys the entire
address space and with it every Python object, callback, finalizer, trace
function, audit hook, and import hook, resets every catching disposition to
`SIG_DFL` (`flush_signal_handlers()`), and clears every `sa_flags` to `0`. The
only things that survive are file descriptors and `SIG_IGN` dispositions — and
the latter are exactly what §V218.2.2's `SIGCHLD` write and §V219.2.4's reset
pass address.

### V219.2.2 The executor-set theorem

This is the replacement for v2.1.8's prohibition. It is stated as a theorem so
that reviewers can attack its premises individually.

> **Definitions.** Let *E(t)* be the set of tasks that may execute instructions
> in this process at instant *t*. Let *C(t)* be the set of code that any member
> of *E(t)* may execute.
>
> **Theorem.** If P-2 and P-3 hold at instant *t₀*, and *C(t₀)* contains no
> task-creating call and no wildcard wait, then for every *t ≥ t₀* until this
> process exits, *E(t)* is the singleton {this task} and *C(t)* contains no
> task-creating call and no wildcard wait.
>
> **Proof.**
>
> 1. *E* can grow only by the creation of a new task in this thread group. On
>    Linux a task joins a thread group only through `clone(CLONE_THREAD)` issued
>    by a task **already in that group**. By P-2 the only such task is this one.
>    So *E* can grow only if **this task** executes a task-creating call.
> 2. This task executes instructions from exactly two sources: (a) the
>    program's own control flow, and (b) asynchronous callbacks. There is no
>    third: Python-level finalizers, weakref callbacks, trace/profile functions,
>    audit hooks, import hooks, and `atexit` handlers are all invoked
>    **synchronously from the program's own control flow**, and therefore belong
>    to (a) as far as *C* is concerned; only signal handlers are asynchronous.
> 3. By P-3 no signal has a catching handler, so no asynchronous callback
>    exists: (b) is empty. Every deliverable signal either has its default
>    action (terminate, ignore, stop, or continue — none of which executes
>    process code) or is explicitly `SIG_IGN`.
> 4. Therefore *C(t)* ⊆ the code reachable from the program's own control flow,
>    which is exactly the reachable production-source set the signed verifier
>    walks from `PRODUCTION_ROOTS` (§V219.2.6). By hypothesis that set contains
>    no task-creating call and no wildcard wait.
> 5. By (1) and (4), *E* never grows, so P-2 is preserved. By (4) and the
>    containment rule of §V219.4.1 — under which the only permitted
>    `signal.signal` arguments are `SIG_DFL`, never a callable — no catching
>    handler can be installed, so P-3 is preserved. The hypotheses of the
>    theorem therefore hold at every later instant, and the conclusion follows
>    by induction over instructions. ∎
>
> **Corollary (the property C218-1 demanded).** From *t₀* onward there is no
> instant at which a second task exists, and no instruction anywhere in the
> reachable program performs a wildcard wait. Therefore **no entity other than
> this task can reap `pid_mid`**, and v2.1.8 §V218.3.2's PID-reservation proof
> closes at **every** instruction boundary rather than between observations.
> The closure is by construction; it does not rely on any detector, and in
> particular not on a detector that would run after a signal.

**The three premises, each mechanically established, not assumed:**

| Premise | Established by | Kind of evidence |
|---|---|---|
| P-2 (single task at `t₀`) | §V219.2.3 gates `G-2` and `G-3` | two independent kernel readbacks: `/proc/self/task` and `/proc/self/status` `Threads:` |
| P-3 (no catching disposition at `t₀`) | §V219.2.4's reset pass + §V219.2.5's `SigCgt == 0` re-verification | kernel readback of the process's own signal-handler mask, after the writes |
| *C(t₀)* excludes task creation and wildcard waits | §V219.2.6 | the **signed** `verification.py` import allowlist plus the call-graph rule, applied over the reachable set from `PRODUCTION_ROOTS` |

*t₀* is the instant `c3t`/`c3n` complete, which is immediately before `c4`.

### V219.2.3 Step `c3t` — the topology gate

§U2.2's step list is extended by one further step, placed **before** `c3n`:

```text
c3t. TOPOLOGY_GATE()  →  TOPOLOGY_OK | TOPOLOGY_REFUSED | TOPOLOGY_INCONCLUSIVE
       TOPOLOGY_OK  ⇒ proceed to c3n
       otherwise    ⇒ PRE_FORK_FAIL_CLOSED  (§V218.2.5, carried unchanged)
```

```text
TOPOLOGY_GATE():
 G-1. PROGRAM IDENTITY (P-1).
      read /proc/self/cmdline in full with os.open/os.read/os.close;
      NUL-split; drop a single trailing empty element.
        any OSError, an empty vector, or a vector whose elements cannot be
        split as §V2.10's argv rule requires        ⇒ TOPOLOGY_INCONCLUSIVE
      require the FIRST ("-m", "philosophia.officina.generic_harness") pair to
      exist at indices (1, 2), exactly as §V2.10's carried argv rule and
      §Z3.3's fixed layout already specify
        absent, or present at any other index       ⇒ TOPOLOGY_REFUSED
      — this is a KERNEL fact: /proc/self/cmdline is established by execve and
        is inherited unchanged by fork, so it names the program image actually
        loaded. It is read, not trusted from an in-process variable.

 G-2. SINGLE TASK, first readback (P-2).
      tasks := os.listdir("/proc/self/task")
        any OSError                                 ⇒ TOPOLOGY_INCONCLUSIVE
      require tasks == exactly one entry, and that entry == str(os.getpid())
        more than one entry                         ⇒ TOPOLOGY_REFUSED
        one entry that is not str(os.getpid())      ⇒ TOPOLOGY_INCONCLUSIVE
        an entry that is not a decimal string       ⇒ TOPOLOGY_INCONCLUSIVE
      — a task directory that appears or disappears between listing and use is
        not a hazard: the requirement is EXACTLY ONE at this instant, and
        §V219.2.2 proves none can be created afterwards.

 G-3. SINGLE TASK, second independent readback (P-2).
      read /proc/self/status (the same read that §V219.2.5 will re-do after the
      writes); require a line beginning exactly "Threads:" whose value is the
      decimal string "1"
        missing, duplicated, non-decimal, or != 1   ⇒ TOPOLOGY_REFUSED
        unreadable                                  ⇒ TOPOLOGY_INCONCLUSIVE

 G-4. RECORD the pre-write masks SigIgn and SigCgt from that same read, under
      the §V219.6 grammar and width rule. A grammar or width failure here is
      TOPOLOGY_INCONCLUSIVE (it is the same defect m218-1 names, detected one
      step earlier).

 G-5. ⇒ TOPOLOGY_OK
 No exception may escape TOPOLOGY_GATE. An escaping exception is a contract
 violation; the pinned continuation for an implementation that lets one escape
 is PRE_FORK_FAIL_CLOSED, and in no case may c4 execute.
```

`TOPOLOGY_REFUSED` and `TOPOLOGY_INCONCLUSIVE` differ only in the refusal
**detail string**; both take the identical `PRE_FORK_FAIL_CLOSED` body of
v2.1.8 §V218.2.5 — no fork, `BOOTSTRAP_FD_CLEANUP`, remove only the CLI's own
`SPAWNING.json`, release the lock, `REFUSED`/`BOOTSTRAP` with
`retryable = false`. **This introduces no new refusal or `INVALID` token.**

### V219.2.4 `c3n` — the reset pass, then the carried `SIGCHLD` normalization

```text
NORMALIZE_REAPING_STATE()  →  NORMALIZE_OK | NORMALIZE_INCONCLUSIVE

 N-1. RESET PASS (new; establishes P-3).
      for each bit index i (0-based) set in the SigCgt mask recorded at G-4,
      in ascending order:
          n := i + 1                       # /proc masks are 1-based
          signal.signal(n, signal.SIG_DFL)
        raises ValueError    ⇒ NORMALIZE_INCONCLUSIVE
              (n is un-catchable, out of valid_signals, or the caller is not
               the main thread of the main interpreter)
        raises RuntimeError  ⇒ NORMALIZE_INCONCLUSIVE   (sub-interpreter)
        raises OSError       ⇒ NORMALIZE_INCONCLUSIVE   (sigaction failed)
        raises anything else ⇒ NORMALIZE_INCONCLUSIVE
      the RETURNED previous handler is DIAGNOSTIC ONLY and is never a premise,
      exactly as v2.1.8 §V218.2.4 already pins.

      NO NEW `signal` MEMBER IS USED. The signal numbers come from the kernel's
      own mask, not from module constants. The permitted surface remains
      signal.signal, signal.getsignal, signal.SIG_DFL, signal.SIGCHLD.
      SIGKILL and SIGSTOP can never appear here, because they cannot be caught
      and therefore can never have a SigCgt bit; if one nonetheless appears,
      signal.signal raises ValueError and the route is inconclusive.

 N-2. SIGCHLD NORMALIZATION (carried verbatim from v2.1.8 §V218.2.2, including
      its entire sigaction analysis and its execve/fork provenance argument):
          previous := signal.signal(signal.SIGCHLD, signal.SIG_DFL)
      with the identical four exception routes. It is executed UNCONDITIONALLY,
      whether or not N-1 already touched SIGCHLD, because it is the call whose
      sa_flags argument clears an inherited SA_NOCLDWAIT for SIGCHLD.

 N-3. ⇒ NORMALIZE_OK
```

**What N-1 changes and what it must not change.** N-1 writes only signals whose
`SigCgt` bit is set — i.e. signals that currently have a **catching handler**.
It never touches a `SIG_IGN` disposition, because an ignored signal has no
`SigCgt` bit. Two carried consequences follow and are pinned:

- **CPython's `SIGPIPE = SIG_IGN` is preserved.** It is an *ignored*
  disposition, so it carries no `SigCgt` bit and N-1 does not touch it. The
  carried §U2.3 `m4`/`m8` route "EPIPE (CPython ignores SIGPIPE) ⇒
  `os._exit(3)`" is therefore unchanged under the supported topology.
- **CPython's `SIGINT` handler is removed.** Under a clean CPython the only
  `SigCgt` bit is `SIGINT`'s, so N-1 resets it and `KeyboardInterrupt` is no
  longer raised in this process; a delivered `SIGINT` takes its default action
  and terminates the CLI. For a lock-holding bootstrap this is the safer
  behaviour and loses nothing: process death releases the descriptors and the
  lock reference by kernel action, removes no record, and leaves the middle
  child to exit at its own `m0` bound (§V218.5, carried). The reset is **not**
  undone afterwards; restoring a handler would reintroduce an asynchronous
  callback inside the ownership lifetime and is forbidden.
- **If some host had caught `SIGPIPE`** (not the supported topology), N-1 resets
  it to `SIG_DFL` and a broken-pipe write terminates the writer instead of
  raising `EPIPE`. **No safety property depends on which**: both continuations
  are process death, which is exactly what the carried route produces. This is
  stated rather than concealed.

### V219.2.5 `VERIFY_REAPING_STATE` — the post-write re-verification

Replaces v2.1.8 §V218.2.3's `V1`–`V7`. Every mask read obeys §V219.6.

```text
VERIFY_REAPING_STATE() → NORMALIZED | VERIFY_FAILED | VERIFY_INCONCLUSIVE

 V-1. n := int(signal.SIGCHLD)                       # symbolic, not a literal
 V-2. re-read /proc/self/status IN FULL, after N-1 and N-2
        any OSError                                 ⇒ VERIFY_INCONCLUSIVE
 V-3. parse "SigIgn:", "SigCgt:", "Threads:" under §V219.6's grammar
        any grammar, width, duplication, or absence failure
                                                    ⇒ VERIFY_INCONCLUSIVE
 V-4. require SigCgt == 0                            # P-3, established
        any bit set                                 ⇒ VERIFY_FAILED
      — a bit still set after N-1 means a handler was installed between G-4 and
        V-2, which §V219.2.2 proves impossible under P-2/P-3; observing it is
        therefore a premise contradiction and must never be forked past.
 V-5. require ((SigIgn >> (n - 1)) & 1) == 0         # SIGCHLD not ignored
        set                                         ⇒ VERIFY_FAILED
 V-6. require SigIgn is unchanged from the value recorded at G-4, except that
      the SIGCHLD bit may have gone from 1 to 0
        any other difference                        ⇒ VERIFY_FAILED
      — this proves the reset pass disturbed no ignored disposition, and is
        what preserves the carried SIGPIPE property mechanically rather than by
        argument.
 V-7. require Threads: == "1"                        # P-2, still
        otherwise                                   ⇒ VERIFY_FAILED
 V-8. re-list /proc/self/task; require exactly one entry == str(os.getpid())
        otherwise                                   ⇒ VERIFY_FAILED
        any OSError                                 ⇒ VERIFY_INCONCLUSIVE
 V-9. require signal.getsignal(signal.SIGCHLD) is signal.SIG_DFL
        otherwise                                   ⇒ VERIFY_INCONCLUSIVE
        — CPython's cached view; corroboration only, never load-bearing.
 V-10. ⇒ NORMALIZED.  The NEXT operation of the attempt is c4.
 No exception may escape.
```

**What is now verified against the kernel, and what still is not.**

| Property | Established by | Independent kernel readback? |
|---|---|---|
| single task (P-2) | `G-2`, `G-3`, `V-7`, `V-8` | **Yes**, twice, from two different `/proc` files, before and after the writes |
| no catching handler (P-3) | `N-1` write + `V-4` readback | **Yes** |
| the program is the sole root (P-1) | `G-1` | **Yes** — `/proc/self/cmdline` is set by `execve` |
| `SIGCHLD` not ignored, not caught | `V-4`, `V-5` | **Yes** |
| no ignored disposition disturbed | `V-6` | **Yes** |
| `SA_NOCLDWAIT` clear | the `sigaction` **write** of `N-2` | **No** — Linux exposes the flag nowhere readable from `os`; carried unchanged from v2.1.8 §V218.2.3, including its three backup contradiction detectors |
| no task-creating call or wildcard wait in reachable code | §V219.2.6 | static, by the **signed verifier**, not by prose |

### V219.2.6 The source and call-graph rule, enforced by the signed verifier

This replaces v2.1.8 §V218.2.6's prohibition as the *mechanism*; the
prohibition's content is retained as the statement of what the verifier
enforces.

`src/philosophia/officina/verification.py` already walks the reachable
production sources from `PRODUCTION_ROOTS` and rejects any absolute import
whose top-level name is outside `ALLOWED_ABSOLUTE_IMPORTS` and any relative
import outside `ALLOWED_RELATIVE_IMPORTS`. That is a **signed, executable,
already-existing** enforcement of premise 3 of §V219.2.2, and the following
observations are consequences of it rather than new rules:

| Task/waiter vector | Why it cannot occur in the reachable program |
|---|---|
| `threading`, `_thread` | outside `ALLOWED_ABSOLUTE_IMPORTS`; the verifier rejects the import |
| `multiprocessing`, `concurrent`, `asyncio` | outside the allowlist |
| `ctypes` (raw `clone`/`pthread_create`) | outside the allowlist |
| `sys.settrace` / `setprofile` / `addaudithook` | `sys` is outside the allowlist |
| `atexit` handlers | `atexit` is outside the allowlist |
| a Python-level signal handler | the containment rule of §V219.4.1 permits `signal.signal` only with `signal.SIG_DFL`; a callable argument is a static violation, and `V-4` would also catch the resulting `SigCgt` bit |
| dynamic import of any of the above | `verification.py`'s `DYNAMIC_IMPORT_CALLS` rules already forbid `__import__`, `importlib.import_module`, `eval`, `exec`, `compile`, `getattr`-based import |

Additional call-graph rules this layer states, each statically checkable over
the same reachable set (rows 245–248):

```text
CALL-GRAPH RULE, for the whole ownership lifetime and the whole program:
 R-a. No wildcard wait anywhere: os.wait(), os.wait3(), os.wait4() with a
      non-positive pid, os.waitpid(-1|0, …), os.waitid(P_ALL|P_PGID, …), and
      every negative-pgid form are forbidden.
 R-b. Every wait call is one of the five sites of §V219.3, targets one explicit
      positive pid, and is reached only from that site's entry condition.
 R-c. The CLI bootstrap's call graph creates no subprocess object. `subprocess`
      remains allowlisted and is used by the SUPERVISOR (§W2.5), a different
      process. Defence in depth, recorded because it removes the last doubt:
      even a stray `Popen` could not reap `pid_mid`, because CPython's
      `Popen.__del__`/`subprocess._cleanup` path polls only `self.pid` with a
      TARGETED `waitpid`, never a wildcard.
 R-d. No `__del__`, weakref finalizer, or context-manager exit in the reachable
      set performs a wait or creates a task.
 R-e. `signal.signal` is called only with `signal.SIG_DFL`; `signal.getsignal`
      is called only for `signal.SIGCHLD`; no other `signal` member is
      referenced anywhere (§V219.4.1).
```

### V219.2.7 Entry points: unsupported topology refuses before fork

Every way of reaching the bootstrap is enumerated. **There is exactly one gate,
and it is unconditional**: no entry point may reach `c4` without a
`TOPOLOGY_OK` from `c3t` and a `NORMALIZED` from `c3n` **in the same attempt**.

| Entry point | Reaches `c4`? | Behaviour |
|---|---|---|
| `python -m philosophia.officina.generic_harness <public command>` in a fresh `execve`'d process (the six public commands of §V2.10) | yes | `c3t` passes `G-1`…`G-5`; `c3n` normalizes; the attempt proceeds. **This is the sole supported production topology.** |
| the same invocation under `PYTHONFAULTHANDLER` / `-X faulthandler` / `-X dev` | yes, only if the reset pass succeeds | `faulthandler`'s catching handlers appear in `SigCgt` at `G-4`; `N-1` resets them; `V-4` then requires `SigCgt == 0`. If any handler cannot be reset, the attempt refuses before fork. Fault handling is therefore **off** for the CLI process, which is stated, not hidden. |
| the same invocation with a `sitecustomize`/`usercustomize` that installed handlers | yes, only if the reset pass succeeds | identical: every catching handler is reset and `V-4` proves none remains. A `sitecustomize` that started a **thread** is caught by `G-2`/`G-3` and refuses. |
| `--officina-bootstrap` private argv surface (§Z3.3, the controller/worker adapter) | **no** | the adapter is a different role and never executes `c1`–`c18`; §Z3.3's refusal-first duties are carried unchanged |
| supervisor-serve / watchdog in-process forks (§W2.1) | **no** | they are post-`c4` roles inside the child, not CLI entries; they never re-enter the bootstrap |
| an in-process caller that imports the sole root and calls the bootstrap function directly (a host library, a REPL, a test) | **no, in effect** | it must still pass `c3t`. `G-1` fails whenever the process image is not the sole root; `G-2`/`G-3` fail whenever the host is multi-threaded. If a host is single-tasked *and* its `cmdline` names the sole root, then by P-1 the program **is** the sole root and §V219.2.2 governs it. **In no case does an in-process caller silently inherit the production authority.** |
| any test that wants to exercise `c4` and beyond | **no, in-process** | fork-path tests must `execve` a real CLI process into a disposable root with the pinned argv and observe it from outside. No in-process test may reach `c4`; this is the only way to test a fresh-exec topology honestly, and it is pinned as test rows 249–250. |

### V219.2.8 Preservation, restart, and long-lived behaviour

- **Between `c3t`/`c3n` and `c4`** the only executor is this task (P-2), the
  only code is `c3n`'s and `c4`'s own instructions (P-3 makes callbacks
  impossible), and neither creates a task or waits. **The enumeration-to-fork
  race of R1 item 2 is therefore not "narrow", it is empty.** If any exception
  is raised in that interval — including one raised by a default-action-free
  path — the pinned continuation is `PRE_FORK_FAIL_CLOSED`; `c4` does not run.
- **Between `c4` and the final reap** the same three premises hold by
  §V219.2.2's induction, so no competing reaper can come into existence at any
  instruction boundary. `V-7`/`V-8` are re-run once more immediately before the
  first `SIGNAL_ATTEMPT` of each attempt and before each terminal decision as
  **redundant defence in depth**; the correction states explicitly that these
  re-checks are *not* load-bearing — the theorem already excludes the failure
  they would detect — so that no reviewer mistakes a detector for the proof.
- **Restart.** A CLI crash at any point releases its descriptors and lock
  reference by kernel action; any unreaped child is reparented to `init`, which
  reaps it; no record is removed without an authoritative reap or a signed
  §U6.1 P3 death proof. Carried unchanged from §V218.6.
- **Long-lived CLI.** Under P-1 the process **is** the CLI, so "long-lived"
  now means "a CLI process making several attempts", not "a host library
  embedding the bootstrap". Each attempt re-runs `c3t` **and** `c3n` in full;
  no cached topology or normalization result may be consulted. This also bounds
  the `T2` zombie residual (§V218.4.5 residual 1, carried): a fresh-exec CLI
  either reaps at wait site W-4 on its next attempt or exits, at which point
  `init` reaps.

### V219.2.9 Complete replay of the v2.1.8 counterexample

The Y line's schedule, step by step, under the chosen topology:

| Y's step | v2.1.8 | v2.1.9 |
|---|---|---|
| 1. an in-process host invokes the CLI on the main interpreter thread while a pre-existing helper thread executes `waitpid(-1, WNOHANG)` | permitted: §V218.2.4 checked only main-thread eligibility | **impossible to reach `c4`.** If the helper thread exists, `G-2` sees ≥2 entries in `/proc/self/task` and `G-3` sees `Threads: ≥2` ⇒ `TOPOLOGY_REFUSED` ⇒ `PRE_FORK_FAIL_CLOSED` ⇒ **no fork**. If the host is single-tasked but is not the sole-root image, `G-1` refuses. |
| 2. `c3n` normalizes and `c4` establishes `OWNED` | happened | `c4` is never reached in step 1's world. In the supported world, `OWNED` is established under P-1…P-4. |
| 3. `M2` reads a matching identity | happened | unchanged |
| 4. the child exits and **the helper reaps it** | the load-bearing step | **impossible.** By §V219.2.2 the executor set is a singleton and no wildcard wait exists in the reachable program, so no entity other than this task can reap `pid_mid`. The child becomes and stays `EXIT_ZOMBIE` (P-4). |
| 5. the PID is reused | followed from 4 | **impossible**: Linux cannot reassign a pid held by a task in any state, and the zombie holds it until *this* route's targeted `waitpid` returns it. |
| 6. `M3` signals the reused process | the harm | **unreachable.** No reuse occurred; `os.kill(pid_mid, …)` under `OWNERSHIP == OWNED` reaches this child or its zombie and nothing else. |

**The proof depends on no detector.** Steps 4–6 are excluded by the topology
and the theorem, before any signal is sent — not by `ECHILD`, `ESRCH`, or a
`ppid` mismatch observed afterwards. Those three detectors are retained
unchanged from §V218.3.1 as a **second** line against a violated platform
premise (the unreadable `SA_NOCLDWAIT`), and §V219.5 states exactly what their
firing now means.

---

## V219.3. One shared total wait automaton for W-1…W-5 (R2)

Closes **M218-1**. v2.1.8 enumerated five wait sites and said "no route's
behaviour changes", which preserved four gaps. This section defines **one**
classifier and instantiates it five times. **No new numeric constant is used**:
every deadline is `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` paced at
`T_SUPERVISOR_POLL_INTERVAL_NS`, both already signed.

### V219.3.1 The shared classifier

```text
WAIT_ONE(pid_mid, site) → REAPED_POSITIVE | NOT_YET | CONTRADICTED_ECHILD
                        | RETRY_EINTR     | INCONCLUSIVE_OTHER

  PRECONDITION: OWNERSHIP(pid_mid) != REAPED.
     An invocation after REAPED is a CONTRACT VIOLATION, not a route. The
     pinned continuation for an implementation that reaches it anyway is:
     perform NO syscall, send NO signal, and treat the site as already
     complete.

  os.waitpid(pid_mid, WNOHANG)          # targeted, positive pid, never a
                                        # wildcard, at every one of the five
                                        # sites
    returns (pid_mid, status) ⇒ REAPED_POSITIVE ; OWNERSHIP := REAPED
                                — the ONLY result that may set REAPED, and the
                                  only proof of death anywhere in this contract
    returns (0, 0)            ⇒ NOT_YET — the child exists and has not
                                terminated. It may be RUNNING or STOPPED; the
                                two are indistinguishable here and need not be
                                distinguished, because WNOHANG without
                                WUNTRACED reports neither a stop nor a continue.
                                A stop/continue can therefore NEVER appear as a
                                status at any of the five sites.
    ECHILD                    ⇒ CONTRADICTED_ECHILD ; OWNERSHIP := CONTRADICTED
                                — NEVER death (carried from §V218.3.3). Under
                                  §V219.2.2 this outcome is outside supported
                                  history; §V219.5 governs it.
    EINTR                     ⇒ RETRY_EINTR — re-issue the SAME targeted call at
                                the next T_SUPERVISOR_POLL_INTERVAL_NS tick,
                                within the site's deadline; on deadline expiry
                                the site's result is INCONCLUSIVE_OTHER
    any other OSError         ⇒ INCONCLUSIVE_OTHER
  No exception may escape. An escaping exception is a contract violation.
```

Two invariants hold at **all five** sites and are stated once here rather than
per site: **only `REAPED_POSITIVE` sets `REAPED` and only it proves death**, and
**no site executes after `OWNERSHIP == REAPED`**.

### V219.3.2 Site instantiations

| | **W-1** — stage M | **W-2** — §U2.5 stage-1 route |
|---|---|---|
| **Entry condition** | abandonment at `c5`, `c6`, or `c7`, after `c4` returned `pid_mid > 0` under a `NORMALIZED` `c3n` | `c9` or `c10` failed (no verified group yet); `SPAWNING_MIDDLE.json` is durable from `c7`, so a start identity **is** captured |
| **Deadline** | `t0 + D`, `D = T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`, `t0` = route entry | identical form, `t0` = stage-1 route entry |
| **Signals** | §V218.3.6's TERM→KILL schedule, ownership-gated (carried) | identical schedule, ownership-gated; `killpg` remains **forbidden** (no verified group) |
| **Transitions** | `REAPED_POSITIVE` ⇒ leave loop; `NOT_YET`/`INCONCLUSIVE_OTHER` ⇒ poll; `RETRY_EINTR` ⇒ re-issue; `CONTRADICTED_ECHILD` ⇒ leave loop immediately | identical |
| **Records / handoff** | `T1`: ordered §U6.3 removal of all four. `T2`: install `SPAWNING_MIDDLE.json`, remove only `SPAWNING.json`. `B`: remove nothing | on `REAPED_POSITIVE`: ordered §U6.3 removal (carried §U2.5). Otherwise the durable `SPAWNING_MIDDLE.json` **already exists** and is retained; only `SPAWNING.json` is removed |
| **Lock** | released by `CLOSE_OWNED` in `T1`/`T2`; **retained** in `B` | released by `CLOSE_OWNED` in every outcome, because an identity is always available |
| **Continuation** | §V218.4.2's three-way terminal selection (carried) | the **same** three-way selection. `captured ≠ ⊥` always holds here, so **`B` is unreachable at W-2**; the outcome is `T1` or the `T2`-shaped continuation, and `REFUSED`/`BOOTSTRAP` is returned exactly as the carried stage-1 route specifies |

| | **W-3** — §U2.5 stage-2 route | **W-4** — §U6.1 P3, same process |
|---|---|---|
| **Entry condition** | `c13`, `c14`, or `c17` failed; `SPAWNING_GROUP.json` with `group_verified: true` is durable | a later attempt **in this same CLI process** applies P3 to a record whose pid this process forked and has not reaped |
| **Deadline** | `t0 + D` from stage-2 route entry | one bounded pass: poll at `T_SUPERVISOR_POLL_INTERVAL_NS` to `t0 + D` from P3 entry |
| **Signals** | the carried stage-2 route's `killpg(process_group_id, …)` — permitted **only** here, because `c11` proved the group. `WAIT_ONE` still targets `pid_mid` alone; non-child members are proved dead by `/proc` absence or state `Z`, never waited on | **none.** W-4 performs no signal of any kind |
| **Transitions** | as W-1 | as W-1 |
| **Records / handoff** | records are removed per §U6.3 only after the carried per-member death proof **and** `REAPED_POSITIVE` for `pid_mid` | the P3 removal proceeds on P3's own signed death proof |
| **Lock** | held throughout; released by `CLOSE_OWNED` at the route's end | held (P3 runs under the acquired lock) |
| **Continuation** | the carried stage-2 route's `REFUSED`/`BOOTSTRAP`. If `pid_mid` is not reaped by `t0 + D`, the three-way selection applies with `captured ≠ ⊥` (durable identity), so **`B` is unreachable at W-3** | **W-4's wait is a resource cleanup, not a death proof.** P3's death conclusion rests on `/proc` absence, state `Z`, or a start-identity mismatch — never on the reap. Therefore `CONTRADICTED_ECHILD`, `INCONCLUSIVE_OTHER`, and deadline expiry at W-4 **do not block, delay, or reverse the P3 route**: the record removal continues. What they do change is `OWNERSHIP` for that pid, so that **no later signal to it is authorized**. `NOT_YET` at expiry leaves the zombie in place under the carried residual |

| | **W-5** — the success path (§W2.1's "reaped by the CLI") |
|---|---|
| **Entry condition** | `c13` read a **valid** `t-supervisor-bootstrap.v1` line, so `m8` completed and the middle is between `m8` and `m9` — **exactly the race M218-1 names** |
| **Deadline** | none, and deliberately so: W-5 is **at most two** `WNOHANG` attempts — one immediately after `c13`'s validation, one immediately after `c17` and before `c18`'s lock release. It never polls to a deadline and never delays the success path |
| **Signals** | **none, ever.** The middle is completing legitimate work; signalling it here would abort a successful bootstrap |
| **Transitions** | `REAPED_POSITIVE` ⇒ `OWNERSHIP := REAPED`; the second attempt is then skipped (no site may run after `REAPED`). `NOT_YET` ⇒ the middle has not yet reached `m9`; **the attempt continues unchanged**. `RETRY_EINTR` ⇒ re-issue once within the same attempt, then treat as `NOT_YET`. `CONTRADICTED_ECHILD`/`INCONCLUSIVE_OTHER` ⇒ set the ownership label accordingly and continue |
| **Records / handoff** | none. W-5 installs, removes, and modifies nothing |
| **Lock** | unchanged; `c18` releases the CLI's reference exactly as carried. The middle's own fork-shared reference is released when it exits at `m9`, and the grandchild's reference dominates until `g3` — carried unchanged |
| **Continuation** | **the bootstrap's success does not depend on the reap.** If both attempts return `NOT_YET`, the middle remains an own child that will exit at `m9` within its own bounded execution; it is then a zombie under the carried §V218.4.5 residual 1, reaped by wait site W-4 at this process's next attempt or by `init` after this process exits. No route waits on it, signals it, or reports a failure because of it |

### V219.3.3 Mutual exclusivity, proved rather than asserted

v2.1.8 asserted that W-1…W-5 are mutually exclusive per attempt. The proof:

| Sites | Why they cannot both run for one `pid_mid` |
|---|---|
| W-1 vs W-2/W-3/W-5 | W-1's entry condition is an abandonment at `c5`/`c6`/`c7`; W-2's is a failure at `c9`/`c10`; W-3's is a failure at `c13`/`c14`/`c17`; W-5's is a **successful** `c13`. The bootstrap executes `c5 → … → c18` once per attempt and leaves it at the first failure, so at most one of these four entry conditions is ever met |
| W-2 vs W-3 | the stage-1 route is entered only before `c11`; the stage-2 route only after `c11` |
| W-3 vs W-5 | `c13` either yields a valid line (W-5) or fails (W-3); not both |
| W-4 vs the rest | W-4 belongs to a **later attempt's** preflight in the same process, and it can only observe a `pid_mid` that an earlier attempt left unreaped — which only W-5's `NOT_YET` or `T2` produces. It never coexists with the attempt that forked the pid |
| any site after `REAPED` | forbidden by `WAIT_ONE`'s precondition and by §V218.3.1's `REAPED` semantics (carried) |

### V219.3.4 The complete result × site product

| Result | W-1 | W-2 | W-3 | W-4 | W-5 |
|---|---|---|---|---|---|
| `REAPED_POSITIVE` | `REAPED`; `T1` | `REAPED`; §U6.3 removal; refuse | `REAPED`; per-member proof then §U6.3; refuse | `REAPED`; P3 continues | `REAPED`; attempt continues |
| `NOT_YET` | poll to `t0 + D` | poll to `t0 + D` | poll to `t0 + D` | poll to `t0 + D` | attempt continues; ≤2 tries total |
| `RETRY_EINTR` | re-issue within deadline | re-issue within deadline | re-issue within deadline | re-issue within deadline | re-issue once, then `NOT_YET` |
| `CONTRADICTED_ECHILD` | `CONTRADICTED`; leave loop; `T2`/`B` | `CONTRADICTED`; identity known ⇒ `T2`-shaped; refuse | `CONTRADICTED`; identity known ⇒ `T2`-shaped; refuse | `CONTRADICTED`; **P3 unaffected** | `CONTRADICTED`; attempt continues |
| `INCONCLUSIVE_OTHER` | poll to `t0 + D`, then terminal selection | poll, then terminal selection | poll, then terminal selection | **P3 unaffected** | attempt continues |
| deadline expiry, not reaped | terminal selection | `T2`-shaped (identity always known) | `T2`-shaped (identity always known) | leave the zombie; P3 continues | n/a (no deadline) |
| invoked after `REAPED` | contract violation | contract violation | contract violation | contract violation | contract violation |
| stop / continue status | impossible (`WNOHANG` without `WUNTRACED`) | impossible | impossible | impossible | impossible |

---

## V219.4. One real importer topology (R3)

Closes **M218-2**. The smaller Y repair is adopted. It is not impossible, so no
alternative is considered and no design fork is left.

### V219.4.1 The sole root is the sole importer

> **`src/philosophia/officina/generic_harness.py` is the sole executable root
> (§V2.10, §Z3.3, signed harness §9 — all carried) *and* it is the exact and
> only permitted importer of `signal`.**

```text
PERMITTED SIGNAL SURFACE  (replaces v2.1.8 §V218.1.2's block)
  Importing module   : src/philosophia/officina/generic_harness.py — and no
                       other file in the repository, production or test.
  Permitted names    : signal.signal, signal.getsignal, signal.SIG_DFL,
                       signal.SIGCHLD.  Exactly four; unchanged from v2.1.8.
  Permitted call sites: NORMALIZE_REAPING_STATE (§V219.2.4) and
                       VERIFY_REAPING_STATE (§V219.2.5), both reached only from
                       step c3n, and nowhere else.
  Permitted arguments: signal.signal(<n>, signal.SIG_DFL) where <n> is either
                       signal.SIGCHLD or a signal number DERIVED from the
                       kernel's SigCgt mask (§V219.2.4 N-1);
                       signal.getsignal(signal.SIGCHLD).
                       A callable second argument is forbidden everywhere.
  Forbidden          : signal.SIG_IGN; any handler callable; siginterrupt;
                       pthread_sigmask; pthread_kill; sigwait / sigwaitinfo /
                       sigtimedwait; set_wakeup_fd; alarm; setitimer /
                       getitimer; raise_signal; pidfd_send_signal; strsignal;
                       valid_signals; every other member.
  Forbidden          : any second module importing signal; any dynamic import;
                       any new executable root; any new script, entry point,
                       argv token, dependency, or call-graph edge.
```

**There is no second module.** The c1–c18 bootstrap stays where §V2.10 and
§Z3.3 put it. **No new dependency, importer, API, or executable root is
created**, and the `PRODUCTION_ROOTS` tuple is unchanged.

**The integer signal literals are unchanged.** `SIGKILL = 9`, `SIGTERM = 15`,
`SIGCONT = 18`, `SIGSTOP = 19`, and the liveness probe `0` remain integer
literals at every existing `os.kill`/`os.killpg` site (v1 draft §S0, carried).
`signal.SIGCHLD` remains the single symbolic use, and `N-1`'s numbers are
kernel-derived, so no additional signal-number constant is named anywhere.

### V219.4.2 The superseded sentences, named exactly

v2.1.8 §V218.1.4's fourteen loci are carried. This layer supersedes four more,
each quoted so a reviewer can check it literally:

| # | Locus | Superseded wording | Replaced by | Scope of the supersession |
|---|---|---|---|---|
| 15 | **signed** `OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md` §9 "Import discipline" | "it uses no `signal`/`threading`/`multiprocessing`/backend import" | §V219.4.1 | **Only the `signal` conjunct**, and only for the four names and two call sites above. `threading`, `multiprocessing`, and every backend import remain forbidden. The same §9 sentence's next clause — "requires a reviewed amendment to that allowlist" — is **honoured**: this layer is that amendment, submitted for exactly the review it demands |
| 16 | carried v2 §V2.10 | "Frozen files (byte-unchanged): `runtime.py`, `ledger.py`, `checkpoint.py`, **`verification.py`**, `activation.py`, signed events/schemas/constants, roots tuple." | §V219.10 | **Only `verification.py`, and only by the addition of the single string `"signal"` to `ALLOWED_ABSOLUTE_IMPORTS` plus the §S7 containment probe.** `runtime.py`, `ledger.py`, `checkpoint.py`, `activation.py`, the signed events/schemas/constants, and the roots tuple remain **byte-unchanged** |
| 17 | carried v2 §V2.10 | "Allowlist delta: **none**." | §V218.1.1 (carried) and §V219.4.1 | the delta is exactly one member, `signal` |
| 18 | v2.1.8 §V218.1.2 | the `Forbidden importers` row listing "the generic harness" among modules that may not import `signal`, and the accompanying sentence "the harness still imports no `signal`" | §V219.4.1 | **deleted as unimplementable.** The generic harness is the sole root and therefore the *only* module that can be the importer. Every other forbidden importer in that row — the supervisor-serve path, the watchdog, the controller adapter entry, the worker entry, the batch-settlement modules — is retained, and since they are all inside the sole module, the restriction is enforced at the **call-site** granularity of §V219.4.1 rather than at file granularity |

The last row is the substantive correction: v2.1.8 tried to express containment
as "which file imports `signal`", which is unsatisfiable when the whole program
is one file. v2.1.9 expresses it as **which names may be referenced and from
which functions** — a strictly finer, statically checkable rule that survives
the sole-root topology.

### V219.4.3 The §S7 probe obligation, mechanically single-valued

Replaces v2.1.8 §V218.1.3:

> The future `verification.py` amendment is **exactly**: add the single string
> `"signal"` to `ALLOWED_ABSOLUTE_IMPORTS`, making the set the sixteen
> previously pinned members plus that one. Nothing else in the file changes —
> not `ALLOWED_RELATIVE_IMPORTS`, not `PRODUCTION_ROOTS`, not the dynamic-import
> rules, not the entropy rules, not the production-manifest rules.
>
> The §S7 quarantine-verifier probe must assert, over the reachable production
> source set walked from `PRODUCTION_ROOTS`:
>
> 1. `ALLOWED_ABSOLUTE_IMPORTS` equals the sixteen pinned members ∪ {`"signal"`};
> 2. `ALLOWED_RELATIVE_IMPORTS` and `PRODUCTION_ROOTS` are unchanged;
> 3. `import signal` appears in exactly one file, `generic_harness.py`;
> 4. the only `signal.` attribute references anywhere are `signal`,
>    `getsignal`, `SIG_DFL`, `SIGCHLD`;
> 5. every `signal.signal(...)` call has `signal.SIG_DFL` as its second
>    argument, and every `signal.getsignal(...)` call has `signal.SIGCHLD` as
>    its argument;
> 6. those calls occur only inside the two `c3n` functions;
> 7. the call-graph rules `R-a`…`R-e` of §V219.2.6 hold.
>
> A verifier that merely tolerates the new member without pinning 3–7 does not
> discharge this obligation. **This document does not perform the edit.**

---

## V219.5. `B-CONTRADICTED` as a non-returning safety sink outside supported history (R4)

Closes **M218-3**, and only because §V219.2 closed C218-1 first.

### V219.5.1 Reachability analysis of every contradiction source

`OWNERSHIP := CONTRADICTED` has exactly four sources (§V218.3.1, carried). For
each, the question is whether a **supported** execution — one that passed
`c3t` and `c3n` and therefore satisfies P-1…P-4 — can produce it.

| Source | Requires | Reachable in a supported execution? |
|---|---|---|
| (a) `WAIT_ONE` returns `CONTRADICTED_ECHILD` | `pid_mid` is not a child of this process. Since `c4` forked it and `WAIT_ONE`'s precondition excludes a prior `REAPED`, this requires **some other entity to have reaped it**, or the kernel to have auto-reaped it | **No.** Another reaper is excluded by §V219.2.2's corollary. Auto-reaping is excluded by `N-2`'s `sigaction` write, verified for the `SIG_IGN`/handler half at `V-4`/`V-5`. The one unverifiable component is `SA_NOCLDWAIT`, so (a) is reachable **only** after a **platform contradiction**: the pinned `PyOS_setsig` semantics or the pinned Linux auto-reap condition failing to hold |
| (b) `SIGNAL_ATTEMPT` returns `GONE` (`ESRCH`) on an owned, unreaped child | the task named by `pid_mid` does not exist, although it was forked and not reaped | **No**, for the same reasons: an unreaped own child is a task in some state, and `kill(2)` on a zombie succeeds |
| (c) `STAT_OBSERVE` `PRESENT_VALID`, uncaptured, `ppid ≠ os.getpid()` | `/proc` reports a parent for our own unreaped child that is not us | **No.** Reachable only after a **kernel contradiction** (or a `/proc` that is not this process's own namespace, which `G-1`/`G-2`'s `/proc/self` reads already presuppose) |
| (d) `STAT_OBSERVE` `PRESENT_VALID`, captured identity mismatches | the kernel start-identity of our unreaped child changed | **No.** Reachable only after a **kernel contradiction** |

> **Result.** In every supported execution, `OWNERSHIP` never becomes
> `CONTRADICTED`. Contradiction is reachable **only** after one of exactly
> three stated failures: **(i)** a platform contradiction — the pinned CPython
> `PyOS_setsig` `sigaction` semantics or the pinned Linux
> `SIG_IGN ∨ SA_NOCLDWAIT` auto-reap condition not holding; **(ii)** a kernel
> contradiction — `/proc` reporting a parentage or start identity inconsistent
> with this process's own `fork` return; or **(iii)** an
> implementation-contract contradiction — a build that violates §V219.2.6's
> verifier-enforced import allowlist or call-graph rules `R-a`…`R-e`, i.e. a
> program that is not the reviewed program.

### V219.5.2 The reclassification

```text
B   — the non-returning stage-M state (replaces §V218.4.2's B block)

B-OWNED         UNCHANGED IN SUBSTANCE from v2.1.8 §V218.4.2 and accepted by
                the Y line as a named A3/host-fault residual. Entered when no
                start identity was ever captured and the child is not yet
                reaped, with OWNERSHIP == OWNED. It retains SPAWN.lock,
                SPAWNING.json, the in-process pid_mid handle, and its bootstrap
                ends; installs nothing; returns nothing; and loops at
                T_SUPERVISOR_POLL_INTERVAL_NS on WAIT_ONE + ownership-gated
                SIGKILL + re-observation. Its exits are REAPED_POSITIVE ⇒ T1
                and a valid capture ⇒ T2. Under §V219.2.2 the ordinary outcome
                is T1: SIGKILL is uncatchable and needs no /proc, and even with
                every signal suppressed the middle exits at its own m0 bound
                and is reaped. Non-termination requires a deliberately
                SIGSTOPed child conjoined with a persistent signal fault.

B-CONTRADICTED  RECLASSIFIED. It is a NON-RETURNING SAFETY SINK OUTSIDE
                SUPPORTED HISTORY. It is not a route, not a terminal, not a
                liveness path, and not a resource or scientific state. It is
                entered only from one of the three stated contradictions of
                §V219.5.1, i.e. only when the process is no longer the
                reviewed program running on the pinned platform.
                It performs exactly one action set, forever:
                  - hold SPAWN.lock, SPAWNING.json, the in-process pid_mid
                    handle, and the bootstrap ends;
                  - send NO signal of any number to any pid, ever;
                  - install, remove, and modify NOTHING;
                  - emit NO refusal, reply, event, ledger entry, capacity
                    artifact, custody disposition, result manifest, or any
                    other citable output;
                  - poll WAIT_ONE(pid_mid) at T_SUPERVISOR_POLL_INTERVAL_NS,
                    whose only non-vacuous outcome would be REAPED_POSITIVE
                    ⇒ T1.
```

### V219.5.3 Why this is not a normal liveness route — and what it is not

> **Proof that `B-CONTRADICTED` is not a liveness path.** Every supported
> execution reaches `T1` or `T2`. By §V219.5.1, `OWNERSHIP == CONTRADICTED`
> never occurs in a supported execution; `B` is entered only with
> `captured == ⊥`; and with `OWNERSHIP == OWNED` the `B-OWNED` analysis above
> gives `T1` (ordinarily) or the named A3 residual. Therefore
> **`B-CONTRADICTED` lies outside the supported state space entirely**, and no
> supported schedule — including every schedule in §V219.7 — passes through it.
> Its existence in the text is a **safety sink**: a defined, harmless
> destination for a process that has already been proved to be executing
> outside its own premises, so that such a process does something safe rather
> than something undefined. ∎

Stated plainly, so it is not mistaken for a resolution:

- It is **not** a resolver, and `s5` is **not** offered as one. A later CLI
  meeting a held `SPAWN.lock` takes `s1`→`s5` and returns a retryable
  `REFUSED`/`BOOTSTRAP` with nothing unlinked and nothing killed. **That is a
  consequence of the sink, not a resolution of it**, and this correction does
  not call it forward progress.
- It relies on **no** operator notice, caller exit, garbage collection,
  finalizer, indefinite retry, or invented deadline, and it picks **no**
  resource value.
- It is **process control, never evidence**. It is not `T_PROCESS_INVALID`, not
  an E1/E2/E3 fact, not a resource-exhaustion result, not an invalidity cause,
  and not a Q/C input. Nothing about it is citable.
- It **does not delete a handle to a possibly live child** and **does not
  authorize a signal after ownership is uncertain** — the two prohibitions R4
  names — because it removes nothing and signals nothing.
- It **does not falsely free the singleton**. The alternatives available to a
  process whose premises have failed are to signal a possibly recycled pid or
  to declare a possibly live child dead; both are worse than a visible stall.

### V219.5.4 The `B` row of the forward-progress table

Replaces the corresponding §V218.4.4 row:

| Surviving state | Lock | Later CLI's behaviour | Classification |
|---|---|---|---|
| `SPAWNING.json` + `SPAWN.lock` held by a CLI in **`B-OWNED`** | held | acquisition expires ⇒ `s1`–`s5` ⇒ `s5` retryable `REFUSED`/`BOOTSTRAP`; nothing unlinked, nothing killed | named A3/host-fault residual (§V218.4.5 residual 2, carried); ordinarily terminates at `T1` |
| `SPAWNING.json` + `SPAWN.lock` held by a CLI in **`B-CONTRADICTED`** | held | identical `s5` outcome | **outside supported history.** The `s5` outcome is a consequence, **not** a resolver. The correct response to observing this state is to treat the platform, kernel, or build as contradicted — which is a matter for a fresh review of the premises, not a step of this contract |

---

## V219.6. Signal-mask grammar and width (R5)

Closes **m218-1**. Applies to **every** mask this contract reads — `SigIgn` and
`SigCgt`, at `G-4` and at `V-3` — and is performed **before** any integer
conversion or bit test.

```text
MASK_FIELD(status_bytes, field_name ∈ {"SigIgn", "SigCgt"})
        → mask_value | MASK_MALFORMED

 M-1. split status_bytes into lines on b"\n".
 M-2. select every line whose bytes begin exactly with field_name + b":".
        zero such lines                              ⇒ MASK_MALFORMED
        two or more such lines (duplicate field)     ⇒ MASK_MALFORMED
 M-3. the remainder after the colon must consist of: one or more space or tab
      bytes, then a maximal run of hexadecimal digit bytes, then end of line.
        an empty digit run                           ⇒ MASK_MALFORMED
        any byte that is not [0-9a-fA-F] inside the run
                                                     ⇒ MASK_MALFORMED
        a "0x"/"0X" prefix, a sign, internal whitespace, or any trailing
        non-newline byte after the run               ⇒ MASK_MALFORMED
 M-4. let d := the number of hexadecimal digits in the run.
      REQUIRED WIDTH RULE, both conjuncts:
        (W-a) architecture-independent minimum, mandatory:
                  4 * d >= int(signal.SIGCHLD)
              — the value must actually contain the SIGCHLD bit position.
                A d that fails this encodes NOTHING about SIGCHLD, so a zero
                after conversion is not evidence of a clear bit.
        (W-b) pinned-platform exact width:
                  d == 16
              — Linux renders a sigset_t in /proc/<pid>/status through
                render_sigset_t as a fixed 16-hex-digit (64-bit) value on
                every supported architecture, 32-bit and 64-bit alike, because
                _NSIG is 64 and the words are printed concatenated with
                %016lx-equivalent zero padding.
        either conjunct failing                      ⇒ MASK_MALFORMED
 M-5. mask_value := int(digit_run, 16)   # ONLY now is conversion permitted
```

| Input | `d` | Verdict | Route |
|---|---|---|---|
| `SigIgn:` with no value | 0 | `MASK_MALFORMED` | `VERIFY_INCONCLUSIVE`; **no fork** |
| `SigIgn:\t0` | 1 | fails `W-a` (`4 < 17` on x86-64) **and** `W-b` | `VERIFY_INCONCLUSIVE`; **no fork** — the exact m218-1 counterexample |
| `SigCgt:\t0000` | 4 | fails `W-a` (`16 < 17`) and `W-b` | `VERIFY_INCONCLUSIVE`; **no fork** |
| `SigCgt:\t0000000000004` | 13 | passes `W-a` (`52 ≥ 17`), fails `W-b` | `VERIFY_INCONCLUSIVE`; **no fork** — just-below-width is rejected by the stricter conjunct |
| `SigIgn:\t0000000000001000` | 16 | passes both | converted; SIGCHLD bit tested |
| `SigCgt:\t00000000000000000000` | 20 | over-width; fails `W-b` | `VERIFY_INCONCLUSIVE`; **no fork** — an unrecognized rendering is never guessed at |
| `SigIgn:\t0x0000000000001000` | — | prefix | `MASK_MALFORMED` ⇒ **no fork** |
| two `SigCgt:` lines | — | duplicate | `MASK_MALFORMED` ⇒ **no fork** |
| leading zeros present | 16 | expected and required by the fixed-width rendering | accepted |
| a future kernel widening `_NSIG` to 128 (`d == 32`) | 32 | fails `W-b` | `VERIFY_INCONCLUSIVE`; **no fork**. Fail-closed on a rendering this contract has not reviewed, rather than silently reinterpreting it |

**Architecture behaviour.** `W-a` uses `int(signal.SIGCHLD)` and therefore holds
on every Linux architecture without naming a number (`SIGCHLD` is 17 on
x86/x86-64/ARM/ARM64, 18 on MIPS, 20 on Alpha/SPARC). `W-b` is the pinned-host
exact-width rule and is the stricter of the two; both must pass. A mask failure
is always `VERIFY_INCONCLUSIVE` (never `VERIFY_FAILED`), because an
unparseable rendering means the contract does not understand the readback, not
that the readback disagreed.

---

## V219.7. Totality: product check and schedules

### V219.7.1 Ownership × identity × wait × terminal product

The carried ten-row identity table (§V218.3.4) and the new `WAIT_ONE` results
are checked against the three ownership states and the three stage-M
successors. Every cell is pinned; there is no "as appropriate" and no gap.

| `OWNERSHIP` | Identity rows reachable | `WAIT_ONE` results reachable | Signals authorized | Terminal / state |
|---|---|---|---|---|
| `OWNED`, `captured = ⊥` | I-3 (capture ⇒ leaves this cell), I-4 (⇒ `CONTRADICTED`), I-5…I-8 | `NOT_YET`, `REAPED_POSITIVE`, `RETRY_EINTR`, `INCONCLUSIVE_OTHER`; `CONTRADICTED_ECHILD` only outside supported history | SIGTERM/SIGKILL per §V218.3.6 | `T1` on `REAPED_POSITIVE`; `B-OWNED` at deadline |
| `OWNED`, `captured ≠ ⊥` | I-1, I-2 (⇒ `CONTRADICTED`), I-5…I-8 | as above | SIGTERM/SIGKILL | `T1` on `REAPED_POSITIVE`; `T2` at deadline |
| `CONTRADICTED`, `captured = ⊥` | I-10 only | `NOT_YET`, `REAPED_POSITIVE`, `RETRY_EINTR`, `INCONCLUSIVE_OTHER`, `CONTRADICTED_ECHILD` | **none** | `T1` on `REAPED_POSITIVE`; otherwise `B-CONTRADICTED` (outside supported history) |
| `CONTRADICTED`, `captured ≠ ⊥` | I-10 only | as above | **none** | `T1` on `REAPED_POSITIVE`; otherwise `T2` |
| `REAPED`, either | I-9 (a contract violation if evaluated) | **none** — every site's precondition forbids it | **none** | `T1` |

Disjointness and exhaustiveness of the successors is carried unchanged from
§V218.4.2: `REAPED ⇒ T1`; `¬REAPED ∧ captured ≠ ⊥ ⇒ T2`; `¬REAPED ∧ captured =
⊥ ⇒ B`. `B` splits by `OWNERSHIP` into `B-OWNED` and `B-CONTRADICTED`, which
are disjoint by construction.

### V219.7.2 The eight required schedules

| Schedule | Trace | Outcome |
|---|---|---|
| **inherited thread performing a wildcard wait** | the helper thread exists at CLI entry ⇒ `G-2` lists ≥2 entries in `/proc/self/task` **and** `G-3` reads `Threads: ≥2` | `TOPOLOGY_REFUSED` ⇒ `PRE_FORK_FAIL_CLOSED` ⇒ **no fork**, no child, no ownership. The wildcard waiter never coexists with a `pid_mid` |
| **thread created between the task enumeration and `fork`** | requires this task to execute a task-creating call (§V219.2.2 step 1) or an asynchronous callback (step 3) in that interval. `N-1` + `V-4` prove no catching handler exists, and the verifier proves no task-creating call is reachable | **empty window**, not a narrow one. `V-7`/`V-8` re-verify both readbacks immediately before `c4` as redundant defence |
| **W-2**, `c9` fails, `waitpid` returns `EINTR` then `(0,0)` to the deadline | `RETRY_EINTR` re-issues within `t0 + D`; `NOT_YET` polls; at expiry the durable `SPAWNING_MIDDLE.json` gives `captured ≠ ⊥` | `T2`-shaped continuation, lock released, `REFUSED`/`BOOTSTRAP`; **`B` unreachable** |
| **W-3**, `c14` fails, group verified, `waitpid` returns an arbitrary errno | `INCONCLUSIVE_OTHER` polls to `t0 + D`; per-member death proof proceeds by `/proc`; `killpg` is permitted here and only here | `T2`-shaped continuation; records removed only after the carried per-member proof **and** `REAPED_POSITIVE` for `pid_mid` |
| **W-4**, later attempt, `ECHILD` on a record's pid | `CONTRADICTED_ECHILD` sets the ownership label for that pid so no signal is authorized; **P3's death proof rests on `/proc`, not on the reap** | the P3 removal completes; the attempt proceeds; no wedge |
| **W-5**, `m8` reported before `m9` exit | `c13` validates the line; the first `WNOHANG` returns `NOT_YET`; the attempt continues to `c14`–`c17`; the second `WNOHANG` before `c18` returns `REAPED_POSITIVE` (the middle reached `m9`) or `NOT_YET` | the bootstrap **succeeds** either way; a `NOT_YET` leaves the carried zombie residual, reaped at W-4 or by `init` |
| **PID reuse attempt** | the child exits at any instant between `STAT_OBSERVE` and `os.kill`; under P-4 it becomes `EXIT_ZOMBIE`; under §V219.2.2's corollary no other entity can reap it | the pid is never reassigned before this route's own `REAPED_POSITIVE`; every signal reaches this child or its zombie |
| **short `/proc` mask** | `SigIgn: 0` at `G-4` or `V-3` ⇒ `MASK_MALFORMED` ⇒ `TOPOLOGY_INCONCLUSIVE` / `VERIFY_INCONCLUSIVE` | `PRE_FORK_FAIL_CLOSED`; **no fork** |
| **`T2` zombie** | a `T2` attempt leaves one unreaped zombie: one pid slot, **no descriptors**, **no `SPAWN.lock` reference**, `/proc` state `Z` with a matching start identity | reaped at W-4 or by `init` after the CLI exits; satisfies another process's §U6.1 P3 death proof precisely; carried §V218.4.5 residual 1 |
| **`B-CONTRADICTED`** | requires a platform, kernel, or implementation-contract contradiction (§V219.5.1) | **no supported schedule reaches it**; if reached, the sink of §V219.5.2 holds every handle, signals nothing, emits nothing citable |

### V219.7.3 Added and replaced crash/cut rows

Every §V218.6 row not listed here carries forward unchanged.

| Cut / scenario | Single continuation |
|---|---|
| `/proc/self/task` lists more than one entry at `c3t` | `TOPOLOGY_REFUSED` ⇒ `PRE_FORK_FAIL_CLOSED`; **no fork** |
| `/proc/self/status` `Threads:` ≠ 1 | `TOPOLOGY_REFUSED` ⇒ **no fork** |
| `/proc/self/cmdline` does not carry `("-m", "philosophia.officina.generic_harness")` at indices (1, 2) | `TOPOLOGY_REFUSED` ⇒ **no fork** |
| `/proc/self/task` or `/proc/self/cmdline` unreadable | `TOPOLOGY_INCONCLUSIVE` ⇒ **no fork** |
| a `SigCgt` bit names an un-catchable signal, or `signal.signal` raises during the reset pass | `NORMALIZE_INCONCLUSIVE` ⇒ **no fork** |
| `SigCgt ≠ 0` after the reset pass | `VERIFY_FAILED` ⇒ **no fork** |
| `SigIgn` changed at `V-6` other than the `SIGCHLD` bit clearing | `VERIFY_FAILED` ⇒ **no fork** |
| `Threads:` or `/proc/self/task` changed between `G-3` and `V-7`/`V-8` | `VERIFY_FAILED` ⇒ **no fork** (a state §V219.2.2 proves impossible; observing it is a premise contradiction) |
| any mask fails `MASK_FIELD` at `G-4` or `V-3` | `TOPOLOGY_INCONCLUSIVE` / `VERIFY_INCONCLUSIVE` ⇒ **no fork** |
| a signal is delivered between `c3t` and `c4` | no handler exists (P-3), so the default action applies: terminate (the crash rows govern; the lock and fds are released by the kernel), ignore, stop, or continue. **No process code runs**, so no task and no waiter can be created |
| an exception is raised between `c3t` and `c4` | `PRE_FORK_FAIL_CLOSED`; **no fork** |
| a second attempt in the same CLI process | re-runs `c3t` **and** `c3n` in full; no cached topology or normalization result is consulted |
| `W-5` returns `NOT_YET` on both attempts | the bootstrap succeeds; the middle exits at `m9`; the zombie residual applies |
| `W-4` returns `ECHILD` | the P3 route is **unaffected**; its death proof rests on `/proc` |
| a CLI in `B-CONTRADICTED` | outside supported history; the sink holds every handle and emits nothing; later CLIs receive `s5`'s retryable refusal, which is a consequence and not a resolver |

---

## V219.8. Implementation and test obligations (no implementation authorization)

**Nothing is authorized by this document.** No code, test, verifier edit,
commit, host change, process, signature, activation, entropy, T/Q/C work,
E1/E2/E3 spend, or later gate. Obligations become due only after both fresh
independent v2.1.9 reviews confirm these bytes **and** the author signs the
amendment token.

All carried rows through §V218.7's 240 remain, except:

- **row 219 replaced:** `NORMALIZE_REAPING_STATE` covers both `N-1` and `N-2`;
  assert the reset pass derives its signal numbers from the recorded `SigCgt`
  mask and names **no** additional `signal` member; assert every exception
  route yields `NORMALIZE_INCONCLUSIVE` and that none escapes.
- **row 220 replaced:** `MASK_FIELD` returns `MASK_MALFORMED` for the empty
  value, `0`, `0000`, a 13-digit value, a 20-digit value, a `0x` prefix, a
  sign, internal whitespace, a trailing byte, a missing field, and a duplicated
  field; conversion occurs **only** after `W-a` and `W-b` both pass; every
  malformed case routes to `VERIFY_INCONCLUSIVE`/`TOPOLOGY_INCONCLUSIVE` and
  **no fork occurs**.
- **row 223 replaced:** the call-graph rules `R-a`…`R-e` hold over the reachable
  production set walked from `PRODUCTION_ROOTS`, and the **signed verifier**
  rejects any build importing `threading`, `_thread`, `multiprocessing`,
  `concurrent`, `asyncio`, `ctypes`, `sys`, or `atexit`.
- **row 224 replaced:** the five wait sites are exactly W-1…W-5, each a
  targeted positive-pid `os.waitpid` reached only from its own entry condition;
  the mutual-exclusivity proof of §V219.3.3 holds for every attempt shape; no
  site runs after `REAPED`.
- **row 233 replaced:** `B-OWNED` does not return, does not release the lock,
  does not remove `SPAWNING.json`, installs nothing, emits nothing citable, and
  exits only via `REAPED_POSITIVE ⇒ T1` or a capture `⇒ T2`.
- **row 234 replaced:** `B-CONTRADICTED` is unreachable in every supported
  execution; assert it can be entered only by injecting one of the three stated
  contradictions, and that when injected it signals nothing, installs nothing,
  removes nothing, and emits nothing citable.

Added:

| # | Test | Covers |
|---|---|---|
| 241 | `TOPOLOGY_GATE` returns exactly one of three results for each injected condition at `G-1`…`G-4`; no exception escapes; every non-`TOPOLOGY_OK` result reaches `PRE_FORK_FAIL_CLOSED` with **no `os.fork`** | R1 |
| 242 | **the C218-1 replay**: exec a CLI whose process has a pre-existing second task, and assert `G-2` and `G-3` each independently refuse and that `os.fork` is never called | R1, C218-1 |
| 243 | the same with a single-tasked process whose `cmdline` does not name the sole root ⇒ `G-1` refuses | R1 |
| 244 | after `N-1`, `SigCgt == 0`; after `N-1` + `N-2`, the `SIGCHLD` `SigIgn` bit is clear and `SigIgn` is otherwise unchanged (`V-6`); assert an inherited `SIG_IGN` on `SIGCHLD` and a host-installed catching handler on an arbitrary catchable signal are both cleared | R1 |
| 245 | static: no wildcard wait form (`os.wait`, `os.wait3`, `os.wait4` with non-positive pid, `os.waitpid(-1\|0, …)`, `os.waitid(P_ALL\|P_PGID, …)`, negative pgid) appears anywhere in the reachable production set | R1, R2 |
| 246 | static: the CLI bootstrap call graph creates no `subprocess` object; and the recorded fact that CPython's `Popen` cleanup polls only its own pid with a targeted `waitpid` is asserted as defence in depth | R1 |
| 247 | static: no `__del__`, weakref finalizer, or context-manager exit in the reachable set performs a wait or creates a task | R1 |
| 248 | static: `signal.signal` is never called with a callable; `signal.getsignal` is called only for `SIGCHLD`; no `signal` member outside the permitted four is referenced | R1, R3 |
| 249 | **no in-process test reaches `c4`**: assert every fork-path test spawns a real `execve`'d CLI into a disposable root with the pinned argv and observes it from outside | R1 |
| 250 | an in-process caller that imports the sole root and calls the bootstrap directly refuses at `c3t` and never forks; assert it does **not** inherit the production authority | R1 |
| 251 | per-attempt re-gating: a CLI process making two attempts runs `c3t` **and** `c3n` twice; no cached topology or normalization result exists | R1 |
| 252 | `PYTHONFAULTHANDLER`/`-X dev` fixture: the extra catching handlers appear in `SigCgt`, `N-1` resets them, `V-4` passes, and the attempt proceeds; a handler that cannot be reset refuses before fork | R1 |
| 253 | `sitecustomize` fixture that installs a catching handler on an arbitrary signal ⇒ reset and `V-4 == 0`; a `sitecustomize` that starts a thread ⇒ `G-2`/`G-3` refuse | R1 |
| 254 | the carried `SIGPIPE = SIG_IGN` property survives `N-1` (it carries no `SigCgt` bit) and `V-6` proves no ignored disposition was disturbed | R1, no-regression |
| 255 | `WAIT_ONE` returns exactly one of five results for `pid_mid`, `(0,0)`, `ECHILD`, `EINTR`, and every other errno; only `REAPED_POSITIVE` sets `REAPED`; `ECHILD` never means death; a stop or continue status can never be returned | R2, M218-1 |
| 256 | `WAIT_ONE` invoked after `REAPED` performs no syscall and is asserted a contract violation | R2 |
| 257 | W-1 instantiation matches §V219.3.2 for every result, including deadline expiry and the three-way terminal selection | R2 |
| 258 | W-2 instantiation: `EINTR` then `(0,0)` to the deadline yields the `T2`-shaped continuation; assert **`B` is unreachable at W-2** because the durable identity always exists | R2, M218-1 |
| 259 | W-3 instantiation: arbitrary errno and deadline expiry; `killpg` is used only after `c11`; records are removed only after the per-member proof and `REAPED_POSITIVE` | R2 |
| 260 | W-4 instantiation: `ECHILD`, arbitrary errno, and deadline expiry **do not block or reverse** the §U6.1 P3 route, whose death proof rests on `/proc`; and no signal is ever sent at W-4 | R2, M218-1 |
| 261 | **the W-5 race**: `c13` validates the `m8` line while the middle has not reached `m9`; the first `WNOHANG` returns `(0,0)`; the bootstrap **succeeds**; the second attempt before `c18` reaps or leaves the named zombie; assert no signal is ever sent at W-5 and no failure is reported | R2, M218-1 |
| 262 | the §V219.3.3 mutual-exclusivity proof holds for every attempt shape, including a success followed by a later attempt that reaches W-4 | R2 |
| 263 | the full §V219.3.4 result × site product behaves as tabulated | R2 |
| 264 | **importer containment**: `import signal` appears in exactly one file, `generic_harness.py`; `ALLOWED_ABSOLUTE_IMPORTS` equals the sixteen pinned members plus `"signal"`; `ALLOWED_RELATIVE_IMPORTS` and `PRODUCTION_ROOTS` are unchanged; the §V219.4.3 obligations 1–7 all hold | R3, M218-2 |
| 265 | the superseded sentences of §V219.4.2 rows 15–18 are the **only** harness/supervisor import statements changed; `threading`, `multiprocessing`, and backend imports remain rejected by the verifier | R3 |
| 266 | the frozen-file set minus `verification.py` is byte-unchanged: `runtime.py`, `ledger.py`, `checkpoint.py`, `activation.py`, signed events/schemas/constants, and the roots tuple | R3, R5, no-regression |
| 267 | `B-CONTRADICTED` unreachability: enumerate the four contradiction sources and assert each requires one of the three stated contradictions; assert no supported schedule of §V219.7.2 enters it | R4, M218-3 |
| 268 | when a contradiction is injected, `B-CONTRADICTED` signals nothing, installs nothing, removes nothing, holds every handle, and emits no refusal, event, or artifact; assert `s5` is **not** described anywhere as its resolver | R4 |
| 269 | `B-OWNED` still terminates at `T1` via `SIGKILL` or the middle's own `m0` bound with `/proc` entirely unreadable | R4 |
| 270 | the mask width rule: every row of §V219.6's table behaves as tabulated, including the 13-digit and 20-digit cases | R5, m218-1 |
| 271 | **v2.1.8-vs-v2.1.9 discrimination**: run the C218-1 replay, the W-5 race, the short-mask case, and the sole-root importer check against a v2.1.8-conforming implementation and assert each **fails**, and against a v2.1.9-conforming implementation and assert each **passes** | all five findings |
| 272 | **no-regression sweep**: diff every non-replaced section body of v2.1.8 and every carried layer against the text this correction claims to carry, including §V218.2.2, §V218.3, §V218.4.1–§V218.4.4, §V218.5, §V217.1, and §V217.4; assert the topology repair changes no selector, custody, capacity, filesystem, or scientific rule | R5 obligations, no-regression |

All tests use disposable roots, fake clocks and meters, no
production-compatible real-T artifact, and create no capability, world,
learner, entropy, capacity artifact, custody disposition, result manifest, or
scientific object. Fixtures that need an inherited `SA_NOCLDWAIT` may use
`ctypes`, which the runtime allowlist forbids but which does not govern test
fixtures (carried from §V218.7 row 214).

---

## V219.9. No-regression over every carried signed surface

| Carried surface | Status under v2.1.9 |
|---|---|
| **§V218.2.2's `SIGCHLD := SIG_DFL` full-disposition replacement**, its `sigaction` analysis, and its `execve`/`fork` provenance argument | **byte-for-byte**; `N-2` is that call, executed unconditionally |
| **`ECHILD` and `ESRCH` never proving death** | byte-for-byte; `WAIT_ONE` and `SIGNAL_ATTEMPT` preserve both rules at all five sites |
| **The ten-row identity table I-1…I-10** (§V218.3.4) | byte-for-byte |
| **Ownership-gated signals** (§V218.3.1's single `os.kill` precondition) and the **fork-ownership PID-reuse proof** (§V218.3.2) | byte-for-byte; §V219.2.2 supplies the exclusivity premise the proof needed |
| **`SIGNAL_ATTEMPT`** (§V218.3.5) and the **TERM→KILL schedule** (§V218.3.6) | byte-for-byte |
| **Deletion of `T3`** | unchanged; `T3` has no body, membership, test, or prose implication anywhere |
| **`T1`/`T2`/`B` no-discard invariant** (§V218.4.1) and the `T1`/`T2` bodies | byte-for-byte |
| **Stage-M causal proof at `m0`/`rel1` and the fork-shared lock** (§V218.5) | byte-for-byte; `m5`/`rel2` remains scoped to cuts at or after `c8` |
| **§V217.1 object-bound observation and both revalidation barriers** | byte-for-byte; untouched |
| **§V217.4 bound-language sweep**, revised row 86, D1's true ground | byte-for-byte. `B`'s unbounded loop remains consistent with the already-withdrawn fixed-total-CLI claims |
| **§V216.2 `CLOSE_OWNED`** at every site including both lock closes | byte-for-byte |
| **`MALFORMED` dominance, §V216.1.2 rule ordering, §V216.1.3 cross-product, the three branch bodies `B-P`/`B-QM`/`B-QN`** | byte-for-byte (the stage-M `B` label is unrelated) |
| **§N2.3 P1–P7 custody, §V214.2.4 reconciliation, K1's five constants and one-release accounting** | byte-for-byte |
| **Death-before-unlink** (§V216.3, §V217.3.1's table) | byte-for-byte; `B` still removes nothing |
| **§V216.5's eight-end audit, §V216.4.1's pipe-only invariant, GC order, watchdog partition, singleton preflight, `s1`–`s5`, §U6.1 P0–P3, §U6.3 order** | byte-for-byte. `s5`'s **behaviour** is unchanged; only its **description** is corrected, in that it is no longer implied to resolve anything |
| **§U2.3's `m0`–`m9` middle-child sequence**, including the `m4`/`m8` EPIPE route | byte-for-byte; `V-6` mechanically proves `N-1` disturbed no ignored disposition, so `SIGPIPE = SIG_IGN` survives under the supported topology |
| **§Z3.3's adapter, argv layout, and the `--officina-bootstrap` private surface**; §V2.10's argv rule, six public commands, and unknown-command exit `2` | byte-for-byte; `G-1` **reuses** §V2.10's existing argv rule and adds no token |
| **`PRODUCTION_ROOTS`, the sole-root rule, and the frozen files other than `verification.py`** | unchanged; §V219.4.2 row 16 scopes the one exception precisely |
| **A3 / B1 / C1 / D1 / K1** | no cell reopened, weakened, or reinterpreted. A3's residual set is unchanged except that `B-CONTRADICTED` **leaves** it (it is now outside supported history rather than a residual within it). D1 unaffected: no supervisor waits on `SPAWN.lock` |
| **Generic harness v2→v2.3.1 and batch settlement v1→v1.1.1** (§J1–§J3, §D1 head/cache completion, §D2 inline `meter_evidence`, fixed process order, prefix settlement, archival boundaries) | referenced unchanged. The **only** change to the signed harness text is §V219.4.2 row 15's narrow supersession of the `signal` conjunct of its §9 import-discipline sentence |
| **Nine signed events, E1/E2/E3, invalidity dominance, Q/C boundary, T** | unchanged; every fact added here is control-plane, T-development-only, and non-citable |
| **The A3 filesystem boundary** | untouched. The topology repair proves **nothing** about filesystem exclusion; `T_RUNTIME.lock` still serializes contract actors only, and no security boundary is invented |

---

## V219.10. The exact code and control files a later implementation review may change

Stated so no later step has to infer it. **This document changes none of them.**

| Path | Permitted change | Authority required |
|---|---|---|
| `src/philosophia/officina/generic_harness.py` | the sole root and sole `signal` importer: steps `c3t`, `c3n`, `WAIT_ONE` and its five instantiations, the stage-M automaton, and the mask parser | already the §V2.10 future edit surface; still needs the amendment token **and** a fresh implementation review |
| `src/philosophia/officina/verification.py` | **exactly one string** added to `ALLOWED_ABSOLUTE_IMPORTS` (`"signal"`, 16 → 17 members) plus the §V219.4.3 containment probe. Nothing else | §V219.4.2 row 16's narrow supersession of §V2.10's byte-unchanged clause; the amendment token; a fresh implementation review |
| `tests/test_officina_generic_harness.py` | the test rows of §V218.7 and §V219.8 | the same |
| everything else | **no change.** `runtime.py`, `ledger.py`, `checkpoint.py`, `activation.py`, signed events/schemas/constants, the roots tuple, every `scripts/*.py`, every contract, signature, and prior review remain byte-unchanged | — |

**The current working-tree state is preserved.** The untracked implementation
work in progress at `src/philosophia/officina/generic_harness.py` and
`tests/test_officina_generic_harness.py`, the modified
`src/philosophia/officina/accounting.py` and `tests/test_officina_accounting.py`,
`essay/OUTLINE.md`, and the modified review/prompt files are **not** edited,
staged, committed, or otherwise touched by this correction, and no obligation
here is due before the amendment token exists. The frozen runtime surfaces —
`successor/officina/runtime/` (only `T_RUNTIME.lock`), the absent
`successor/officina/runtime_control/`, and
`successor/officina/T_ENVELOPE.json` — are unchanged.

---

## V219.11. Governance, determinacy, and negative space

**Two-implementer determinacy (added claims).** The supported entry topology is
a four-premise predicate gated by one new step whose five checks each have a
pinned failure route (§V219.2.3). The reset pass derives its signal numbers
from the kernel's own mask and names no new module member (§V219.2.4). The
post-write verification is ten numbered steps with three results (§V219.2.5).
The executor-set theorem has three premises, each with a named mechanical
source, and its conclusion is quantified over instructions rather than over
observations (§V219.2.2). One wait classifier has five results and one
precondition, instantiated five times with an exact entry condition, deadline,
signal policy, transition, record behaviour, lock behaviour, and continuation
each (§V219.3). The importer is one file with four permitted names, two
permitted call sites, and seven verifier obligations (§V219.4). The mask
grammar is five steps with a two-conjunct width rule and an eleven-row decision
table (§V219.6). No clause resolves to "as reviewed", "as appropriate", or
implementer discretion, and no design fork is left open.

**Compatibility classification.** An engineering/control amendment surface over
the signed harness composite. Protocol amendments: §W6.5's carried supersession
of harness §5a's physical at-or-before-deadline sentence, and — new in this
layer — §V219.4.2's narrow supersession of the `signal` conjunct of harness §9's
import-discipline sentence and of §V2.10's byte-unchanged `verification.py`
clause. No signed archival set, event, runtime schema, root, constant, resource
value, T band, or Q/C boundary moves. The import-allowlist delta remains exactly
one member, `signal`.

**No author cell is reopened, and none is required.** The repairs are
mechanical process-topology, wait-totality, importer, sink-classification, and
parsing corrections under the already selected A3/B1/C1/D1/K1 policies. **No new
numeric constant, resource value, or scientific choice was reached at any point**
— every deadline reuses `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` and
`T_SUPERVISOR_POLL_INTERVAL_NS` — which is why this layer emits no
`BLOCKED_..._AUTHOR_CELL` verdict. Both v2.1.8 reviewers independently reached
the same author-cell conclusion.

**Negative space.** This correction creates nothing executable and authorizes no
implementation, commit, host change, verifier edit, process, supervisor,
controller, worker, watchdog, adapter, middle child, endpoint, pipe, FIFO,
journal instance, tombstone, spawn record, lease, capability, operation, output
bound, framed transport, result manifest, quarantine record, promoted object,
capacity artifact, custody disposition, author decision file, freeze witness,
fallback witness, entropy, E1/E2/E3 spend, world, learner, candidate, Q attempt,
Q/C object, datum, outcome, Proof, or claim movement. It predicts no
qualification and no C1–C6 outcome. Process invalidity, resource exhaustion,
missing evidence, the `B-OWNED` residual, and the `B-CONTRADICTED` sink remain
infrastructure facts and are nowhere treated as scientific evidence. No example
in this document was written to any file.

---

## V219.12. The bounded confirmation questions

Three per line, no more, concentrated on R1, R2/R4, and R3/R5. Both lines must
recompute the digest of **this file** and of every governing hash above, and
must treat this author's closure
(`reviews/opus5_officina_supervisor_control_channel_v2_1_9_closure.md`), the
v2.1.8 X confirmation, and the v2.1.8 Y review as untrusted inputs rather than
as support for these bytes.

### For the X line (Claude Opus 4.8, clean context)

> **X-Q1 (R1).** Does §V219.2 mechanically establish and **preserve** exclusive
> reaping from immediately before the first fork through the final reap? Attack
> the executor-set theorem premise by premise: that a task joins a thread group
> only via `clone(CLONE_THREAD)` from a task already in it; that signal handlers
> are the only asynchronous entry into a task and that `SigCgt == 0` after the
> derived reset pass excludes them; that finalizers, weakref callbacks,
> trace/profile functions, audit hooks, and `atexit` are all synchronous and
> therefore governed by the verifier-enforced reachable set; that `execve`
> terminates every other task and erases every Python callback; and that the
> `G-1`/`G-2`/`G-3` readbacks are kernel facts rather than in-process claims.
> Then determine whether the enumeration-to-fork window is genuinely **empty**
> rather than narrow, and whether the Y-line replay of §V219.2.9 is closed
> **before** any signal rather than by a detector.
>
> **X-Q2 (R2/R4).** Is `WAIT_ONE` total, and is its five-site instantiation
> exhaustive and mutually exclusive? Attack the `(0,0)`, `EINTR`-at-deadline,
> `ECHILD`, arbitrary-errno, post-`REAPED`, and stop/continue rows at each of
> W-1…W-5; the claim that W-4's `ECHILD` cannot block the §U6.1 P3 route; and
> the W-5 policy of at most two non-blocking attempts with no signal and no
> deadline. Then judge whether §V219.5's reachability analysis really places
> `B-CONTRADICTED` outside supported history, and whether classifying it as a
> non-returning safety sink — with `s5` explicitly **not** a resolver — is a
> correct fail-closed disposition rather than a renamed wedge.
>
> **X-Q3 (R3/R5).** Is the importer topology implementable exactly as written,
> with `generic_harness.py` as both sole root and sole `signal` importer, no
> second module, and no undeclared dependency? Check that §V219.4.2's four
> supersessions are correctly scoped — in particular that only the `signal`
> conjunct of the signed harness §9 sentence and only the `verification.py`
> entry of §V2.10's frozen list are affected — and that the seven §S7
> obligations make the future verifier delta single-valued. Then check that
> §V219.6's `W-a`/`W-b` width rule rejects every short, empty, prefixed, and
> over-wide mask before conversion, and that the pinned 16-digit Linux
> rendering claim is correct on the supported architectures.
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_V2_1_9_X` or
> `REVISE_OFFICINA_SUPERVISOR_V2_1_9`. Static review only: no code, test,
> probe, signal/fork/subprocess experiment, or Officina process may run; no
> runtime or scientific artifact may be created; no existing file may be
> modified; create exactly one review file. Do not authorize
> `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`, implementation, T
> activation, entropy, spend, or any later gate.

### For the Y line (GPT-5.6 Sol, clean context)

> **Y-Q1 (R1, your C218-1).** Replay your counterexample against §V219.2 in
> full: an in-process host with a pre-existing helper thread doing
> `waitpid(-1, WNOHANG)`. Determine whether it can now reach `c4` at all, and
> whether any *other* competing-reaper schedule survives — including a thread
> created by an asynchronous callback in the enumeration-to-fork window, a
> `sitecustomize`-installed handler, `faulthandler`, a `subprocess` finalizer, a
> `__del__` reached through cyclic GC, and a host whose `cmdline` names the sole
> root. Is the premise **preserved by construction** through the final reap, or
> does any step still rely on a detector or on a prose prohibition?
>
> **Y-Q2 (R2/R4, your M218-1 and M218-3).** Are W-2, W-3, W-4, and W-5 now
> total — specifically your `m8`-reported-before-`m9` race at W-5, and `EINTR`,
> `ECHILD`, and arbitrary errors at W-2/W-3/W-4? Does any site set `REAPED` on
> anything but a positive targeted return, run after `REAPED`, or treat `ECHILD`
> as death? Then judge §V219.5: given your own criterion that naming a wedge
> does not make it acceptable, is `B-CONTRADICTED` now genuinely confined to a
> stated platform/kernel/implementation-contract contradiction, is the sink
> classification honest, and is it clear that `s5` is a consequence rather than
> the resolver you rejected?
>
> **Y-Q3 (R3/R5, your M218-2 and m218-1).** Is there now exactly **one** real
> importer topology with no unnamed module, no undeclared dependency, and no
> unsatisfiable rule? Verify that §V219.4.1's call-site-granularity containment
> is implementable inside the sole module, that §V219.4.2 supersedes every
> conflicting harness and supervisor sentence you identified (including
> §V2.10's byte-unchanged `verification.py` clause, which your finding implies
> but does not name), and that no extra importer, API, durable object, schema,
> constant, token, operator action, resource value, or scientific choice became
> implicitly available. Then verify that `SigIgn: 0` and `SigCgt: 0` now route
> to `VERIFY_INCONCLUSIVE` with no fork, and that the width rule's two
> conjuncts are both justified on the pinned platform.
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_V2_1_9_Y` or
> `REVISE_OFFICINA_SUPERVISOR_V2_1_9`. Static review only: no code, test,
> probe, signal/fork/subprocess experiment, or Officina process may run; no
> runtime or scientific artifact may be created; no existing file may be
> modified; create exactly one review file. Do not authorize
> `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`, implementation, T
> activation, entropy, spend, or any later gate.

---

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** and is not made signable here. The v2.1.8 X confirmation was
conditional on a Y confirmation of the **identical** v2.1.8 bytes; the Y line
revised those bytes, so no conditional authorization survives, and it does not
transfer to v2.1.9. The only next authorization step is a **fresh independent
X-line review and a fresh independent Y-line review of the v2.1.9 bytes**.
`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
