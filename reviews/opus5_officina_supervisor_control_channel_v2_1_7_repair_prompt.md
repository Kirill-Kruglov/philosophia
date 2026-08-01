# Prompt for Claude Code Opus 5: Officina supervisor/control-channel v2.1.7 bounded repair

You are **Claude Code Opus 5 acting only as the specification author**, not an
independent reviewer. Work in `philosophia` at or after commit
`da3b22f9f3114f6534e4d4b390934e1991b35437`.

Read the complete supervisor v2 through v2.1.6 chain, both signed author
selection records, inherited generic-harness/batch-settlement contracts, and
both completed independent v2.1.6 reviews:

- `reviews/opus_officina_supervisor_control_channel_v2_1_6_final_confirmation.md`
- `reviews/sol_officina_supervisor_control_channel_v2_1_6_final_confirmation.md`

Pinned hashes:

```text
e4aa9ef4f0de2fe705d54cb7ac016212098cfe71b8575ef2b435e8c9b09f5609  v2.1.6 correction
e395da8b6366b35da19dfeaf28a0fb25bedd9e07245ffb97b60f7f3b870ad9db  Opus X review
b38488cfeb422f16eda48561d5706d160ca7dc25969533e32265fa8a31c648c8  Sol Y review
```

Both lines returned `REVISE_OFFICINA_SUPERVISOR_V2_1_6`. Their findings are
complementary and all govern. Treat prior author closures as untrusted. Static
authoring only: run no repository code, test, probe, smoke command, or Officina
process; alter no runtime state.

## Deliverables

Create exactly two new files and alter nothing else:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_7_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_7_closure.md`

The correction must be a narrow replacement layer over v2.1.6 with an exact
replacement index. Everything not explicitly replaced carries forward
verbatim. Closure line 1 must be exactly one of:

- `READY_FOR_OFFICINA_SUPERVISOR_V2_1_7_FINAL_XY_CONFIRMATION`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_7_AUTHOR_CELL`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_7_CONTRACT_CONFLICT`

No new author cell is expected. Preserve `CLOSE_OWNED`, physical-presence
dominance, death-before-unlink and every earlier closure except where the
findings below require a named replacement.

## Mandatory repairs

### R1. Object-bound selector observation and revalidation (Sol C1)

The fixed-snapshot Boolean cross-product is not sufficient while name
observations and decoded bytes are unbound and mutable. Define one closed
observation record per canonical settlement, quarantine and manifest name.
Each observation must bind, as applicable:

- parent-directory enumeration membership and canonical name;
- `lstat` identity and file type without following symlinks;
- an `O_NOFOLLOW` opened descriptor for a present valid regular-file candidate;
- `fstat` identity matching the name observation;
- exact bytes read from that descriptor, canonical decode, and content hash;
- paired absence evidence when the name is absent;
- one observation epoch/id tying all three names into one selector snapshot.

Every `PS/PQ/PF`, `VS/VQ/VF`, binding and hash predicate must consume only this
record. A symlink, directory, truncated/partial/zero-byte or replaced object
must never become absence.

Require two explicit revalidation barriers using the same closed observation
algorithm:

1. immediately before entering B-P/B-QM/B-QN;
2. immediately before installing `.disposed.json` or releasing capacity.

At each barrier, present objects must have the same bound identity and bytes;
objects observed absent must still satisfy paired absence; the cross-object
binding/hash relation must still hold. Any create/remove/rename/replace/content
change, validation error or inconclusive observation routes to record-first
refusal/invalidity and releases nothing. Re-run every mutation cut between
enumeration, lstat, open, fstat, read, branch, custody proof and disposition.

State honestly that a deliberate same-UID mutation **after the final
revalidation** is the already-signed A3 procedural residual. It is permanently
non-citable and does not justify an unconditional “impossible” claim. Do not
invent a security boundary or new author choice.

### R2. Total syscall-result state machine for stage M (Sol M1; Opus X216-m1)

Define a closed result enum for `/proc/<pid>/stat` observation:

```text
ABSENT | PRESENT_VALID | UNREADABLE | UNPARSABLE | ERROR
```

Only ABSENT and PRESENT_VALID may prove identity/death. UNREADABLE,
UNPARSABLE and ERROR must take an exact no-kill/no-unlink bounded continuation.
No exception may escape.

Pin every result for both SIGTERM and SIGKILL attempts:

- success;
- `ESRCH` -> proceed to own-child death proof, never infer death alone;
- `EINTR` -> bounded retry under an existing signed deadline;
- `EPERM` and every other error -> exact no-unlink fail-closed/recovery route.

Pin every `waitpid(pid_mid, WNOHANG)` outcome:

- returned `pid_mid` and status;
- returned `0`;
- `EINTR` bounded retry;
- `ECHILD`;
- every other error.

State exactly which outcomes prove this own child dead and why, including PID
reuse and prior reaping. Pin SIGTERM-to-SIGKILL timing, deadline edges and all
ordinary-exit races. No syscall error, parser error, permission outcome, or
wait result may be left to implementation convention.

### R3. Executable SPAWNING-only terminal without a long-lived-CLI wedge (Sol M2)

Preserve death-before-unlink. A failure at c5/c6, where only `SPAWNING.json`
may exist, must not return into a state that P2b refuses forever while the
original CLI remains alive.

Define a total, executable own-child resolution using the successful fork
relationship and `waitpid` authority, independent of readable `/proc`. The
preferred route is bounded kill/proof/reap followed by ordered removal under
the still-held lock. If the bounded proof cannot complete, specify a durable
recoverable identity/state and an exact same-CLI or successor continuation
that eventually reaches either proved-dead cleanup or an explicitly named
blocked terminal; it must not falsely mark the singleton free, require caller
exit/GC, depend on an unstated operator, or leave P2b with no forward route.

Re-run at least: long-lived CLI; stopped middle; middle exits before/between
signals; unreadable/unparsable `/proc`; `ESRCH`/`EPERM`/`EINTR`; `waitpid` 0,
pid, `ECHILD`, error; PID reuse attempt; restart before/after the middle's own
bound; crash before/after any durable recovery state, death proof, unlink,
fsync and lock close. Every state must have one continuation and no live record
may be removed.

If an additional closed control-plane record/schema/path is mechanically
unavoidable, declare it loudly, prove its acyclic ownership/custody/GC and
scientific exclusion, and explain why it is not an author cell. Prefer reuse of
already signed singleton records where that is total and truthful.

### R4. Remove the full CLI-total-bound contradiction class (Opus X216-M1)

Extend the operative search beyond v2.1.6's incomplete five loci. Replace at
least these carried claims and every equivalent occurrence:

- v2.1.3 §U2.4 “Total CLI bound ... No wait is unbounded”;
- v2.1.2 §N12 test row 86 “CLI's total bound equals the stated arithmetic
  sum”;
- v2.1.2 §N3.5 “always releases within that arithmetic sum”;
- v2.1.3 §U2.7 equivalent fixed-total/release wording.

The accurate invariant is:

- lock acquisition and bootstrap pipe reads/writes are bounded by their signed
  deadlines;
- `/proc` reads, canonical installs and file/directory `fsync`s have no
  executable duration bound in signed text;
- D1 holds because no supervisor waits on `SPAWN.lock`, not because total CLI
  lifetime is fixed-bounded.

Correct v2.1.6's false “no statement anywhere” and “exactly five loci; no
others” assertions. Provide an exhaustive phrase-and-semantic search table,
replace row 86 and every conflicting test obligation, and make rows
121/126/159-162 plus the revised row 86 jointly satisfiable. Do not introduce
unsigned deadlines or a new resource constant.

## Required proof obligations

1. Exact v2.1.6-to-v2.1.7 replacement index; nothing else moves.
2. One-to-one disposition of Sol C1/M1/M2 and Opus X216-M1/X216-m1, recording
   both v2.1.6 REVISE verdicts accurately.
3. Object-bound three-name observation schema/algorithm, branch and final
   revalidation traces, and complete create/remove/rename/replace cut table.
4. Total stat/signal/waitpid enum and transition table with no uncaught result.
5. Complete SPAWNING-only long-lived-CLI recovery automaton, crash table and
   proof of death-before-unlink plus eventual executable continuation.
6. Exhaustive operative bound-language search/replacement table, including
   §U2.4, §N12 row 86, §N3.5 and §U2.7.
7. No-regression proof for `CLOSE_OWNED`, physical malformed dominance,
   selector branch bodies, A3/B1/C1/D1/K1, bootstrap/GC/watchdog/custody,
   generic harness, batch settlement, events, E1/E2/E3, Q/C and T.
8. Exact implementation/test obligations, but no implementation or
   authorization.
9. One bounded fresh-confirmation question each for Opus 4.8 X and GPT-5.6 Sol
   Y, requiring SHA recomputation and re-running every counterexample.

## Prohibitions and authorization boundary

Do not edit prior specs, reviews, prompts, signatures, code, tests, runtime
trees, Cursor's dirty implementation, or unrelated dirty/untracked files. Do
not execute tests/processes or create entropy, worlds, candidates,
capacity/custody/result artifacts, Q/C objects, or science.

Do not authorize
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`. It remains unavailable
until both fresh independent X and Y reviews confirm the exact v2.1.7 bytes.
Do not authorize implementation, T activation, E1/E2/E3 spend, or later gates.

Confirm exactly two deliverables, T remains `NOT_ACTIVATED`, the programme
claim remains `OPEN`, and no runtime or scientific artifact was created.
