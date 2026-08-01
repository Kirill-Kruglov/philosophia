# Prompt for Claude Code Opus 4.8: independent Officina supervisor v2.1.9 X-line confirmation

Act as the **independent clean-context X-line reviewer**. Claude Code Opus 5
authored v2.1.9; its closure/chat response are untrusted. Reconstruct the repair
from normative bytes, with the v2.1.8 Y-line counterexamples governing.

Work in `philosophia` at or after commit
`8ba4ba9371347326d46f63dce1f4cab2728149bf`. Read the full supervisor v2 through
v2.1.9 chain, signed generic-harness and batch-settlement composites, author
signatures, and both v2.1.8 reviews.

Recompute the SHA-256 of
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md`;
expected:

```text
1468c9ab1806c1eb25523e6a9fd8567592076f0dc74418ca698a52f933c7f3b0
```

Static review only. Read-only inspection and literal hashing/arithmetic are
allowed. Run no code, test, probe, subprocess, signal/fork experiment, smoke
command, or Officina process. Alter no existing file or runtime state.

## Required question

Does v2.1.9 close C218-1, M218-1, M218-2, M218-3 and m218-1 with an
implementable, total contract, especially a genuinely closed executor set from
pre-fork through final reap, rather than substituting clean argv and repository
AST constraints for clean runtime state?

Attack at least:

1. **Sole-root identity:** `/proc/self/cmdline` records argv bytes, not an
   attestation of the current Python object graph or an immutable proof of the
   most recent executable/module path. Test fork inheritance, writable argv,
   wrapper launch, `runpy`, in-process calls with matching cmdline, and a process
   that legitimately exec'd the CLI but accumulated state during Python startup.
   Decide whether G-1 proves P-1 as stated.
2. **Startup/runtime contamination:** enumerate `.pth` executable lines,
   `sitecustomize`, `usercustomize`, import/audit hooks, trace/profile hooks,
   weakref/finalizer callbacks, monkeypatched `os.fork`/`os.waitpid`/
   `signal.signal`, retained callable references, and preloaded extension state.
   `execve` destroys the old address space but Python startup can recreate these
   before the sole root runs. Show mechanically why none can create a task,
   wildcard-wait, or substitute a reviewed syscall after `c3t`; otherwise C218-1
   remains open.
3. **Native executor set:** the verifier scans Python imports/calls, while
   allowed C extensions and native libraries may create threads or helper
   waiters synchronously without importing `threading`/`ctypes`. Audit every
   allowed reachable dependency and all calls between the final task readback
   and final reap. A single-task snapshot does not itself preserve
   single-taskness.
4. **Signal reset:** exhaust every possible `SigCgt` bit, reserved/invalid
   numbers, exceptions, mutations between G-4/N-1/V-4, and semantics of clearing
   SIGINT/faulthandler/site handlers. Verify `SigCgt == 0` plus the executor-set
   proof actually closes asynchronous callbacks, and that default termination
   at every bootstrap cut preserves the signed record/lock invariants.
5. **`WAIT_ONE` product:** independently instantiate every result at W-1…W-5.
   Attack `(0,0)`, repeated `EINTR`, `ECHILD`, other errors, deadline equality,
   prior reap, stop/continue, and W-5 after `m8` but before `m9`, including a
   SIGSTOPed middle that never reaches exit. Confirm each site has one lawful
   continuation and only targeted positive pid sets `REAPED`.
6. **Contradiction sink:** prove all four sources of `CONTRADICTED` are excluded
   in supported history without circularly assuming the executor-set theorem.
   Only then may `B-CONTRADICTED` be outside supported history. Confirm
   `B-OWNED`, T2 zombie, restart, second CLI and all locks/records remain total;
   `s5` is never called a resolver.
7. **Importer/verifier exactness:** confirm `generic_harness.py` is now the sole
   root and sole importer and that all four conflicting sentences are exactly
   superseded. Attack aliases, rebinding, `from signal import`, indirect calls,
   stored callable references, dynamic attribute access and monkeypatching.
   Verify the proposed AST/call-graph checks are implementable and permit only
   the four names and two functions, with no unnamed module or new root.
8. **Mask and regression:** independently verify Linux's exact 16-hex-digit
   rendering on every declared supported architecture, grammar/width ordering,
   duplicates, prefixes, whitespace, over/under-width, and `SIGCHLD` bit
   indexing. Then re-run the object-bound barriers, PID/identity table, T3
   deletion, stage-M proof, bound sweep, A3/B1/C1/D1/K1, generic harness/batch
   settlement, E1/E2/E3, Q/C and T inactivity.

Author assertions and examples are not evidence. A fail-closed label is not a
repair if supported operation can enter a permanent sink. Report every finding
with severity, exact locus, counterexample, and smallest repair.

## Deliverable

Create exactly one file and alter nothing else:

`reviews/opus_officina_supervisor_control_channel_v2_1_9_final_confirmation.md`

Line 1 exactly one of:

- `CONFIRM_OFFICINA_SUPERVISOR_V2_1_9_X`
- `REVISE_OFFICINA_SUPERVISOR_V2_1_9`

Include hash/base, disposition of all five findings, eight attack traces,
findings, no-regression table, author-cell/contract-conflict determination, and
exact authorization boundary.

If confirmed, authorize only Kirill's token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`, conditional on Y
confirming identical bytes. Authorize no implementation, commit, verifier edit,
activation, entropy, runtime construction, spend, Q/C, or science. If revised,
keep it unavailable. Confirm T `NOT_ACTIVATED`, claim `OPEN`.
