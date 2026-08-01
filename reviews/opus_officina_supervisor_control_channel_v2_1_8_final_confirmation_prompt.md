# Prompt for Claude Code Opus 4.8: independent Officina supervisor v2.1.8 X-line confirmation

Act as the **independent clean-context X-line reviewer**. Claude Code Opus 5
authored v2.1.8; its closure and chat response are untrusted author claims.
Reconstruct the result from the normative bytes and both v2.1.7 `REVISE`
reviews.

Work in `philosophia` at or after commit
`6e158560a8bd452d6780d9e279a079f41f4b78fe`. Read the complete supervisor v2
through v2.1.8 chain, the author selections/signatures, the signed generic
harness and batch-settlement contracts, and both v2.1.7 final reviews.

Recompute the SHA-256 of
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md`;
expected:

```text
33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50
```

Static review only. Read-only file inspection and literal hashing/arithmetic are
allowed. Run no repository code, tests, probes, smoke commands, subprocess
experiments, signal experiments, forks, or Officina processes. Alter no existing
file or runtime state.

## Required question

Does v2.1.8 close Sol C217-1/M217-1/m217-1 and Opus X217-M1/X217-m1 with a
total, implementable process-control contract, while introducing only the
declared one-member `signal` allowlist delta and no false death proof, orphaned
child, PID-reuse signal, silent wedge, hidden operator step, or contract
conflict?

Attack at least:

1. **Reviewed allowlist amendment:** verify that the delta is exactly the string
   `signal`, usable only by the CLI bootstrap at the enumerated members and two
   `c3n` functions. Search for every superseded zero-delta assertion and decide
   whether this supervisor-layer review can validly satisfy the signed generic
   harness's explicit reviewed-amendment clause. No other importer, handler,
   signal API, event, path, schema, constant, token, or scientific cell may be
   introduced.
2. **Kernel disposition normalization:** independently check the claimed pinned
   Linux/CPython semantics of main-thread
   `signal.signal(signal.SIGCHLD, signal.SIG_DFL)`. Does it replace the complete
   disposition and clear both inherited `SIG_IGN` and `SA_NOCLDWAIT`, including
   when the CLI itself inherited either state? Separate what `/proc/self/status`
   can prove (`SigIgn`/`SigCgt`) from what it cannot expose. If clearing
   `SA_NOCLDWAIT` is not mechanically warranted by the pinned call, reject and
   give the smallest repair.
3. **Pre-fork placement and failure closure:** trace every attempt from lock
   entry through `c3n`, verification, and the first fork. Confirm `c3n` runs in
   the main thread immediately before every attempt's first fork and that no
   fork, lease, process record, or later action occurs on any exception,
   unexpected previous disposition, `/proc` read/parse failure, wrong mask, or
   non-`NORMALIZED` result.
4. **Sole reaper and complete wait surface:** enumerate every permitted
   `waitpid` site and every forbidden wildcard/external reaper, thread,
   `subprocess` owner, or SIGCHLD handler. For `(pid,status)`, `(0,0)`, `EINTR`,
   `ECHILD`, all other errors, stopped children, and deadline edges, verify that
   only `waitpid == pid_mid` proves death; `ECHILD` and `ESRCH` under owned,
   unreaped state must be contradictions/inconclusive, never proof.
5. **Ownership, identity, and PID reuse:** reproduce the complete
   `IDENTITY_SAFE` table, including uncaptured `PRESENT_VALID` with mismatching
   `ppid`. Trace `/proc` absent/unreadable/unparsable/error, capture mismatch,
   reap, and contradiction. Every signal must be gated solely by
   `OWNERSHIP == OWNED`; no signal after reap or contradiction, and no PID-reuse
   inference from `/proc` absence.
6. **Terminal totality:** prove `T3` is absent everywhere and T1/T2/B are
   pairwise disjoint and exhaustive. Trace a stopped child, completely
   unreadable `/proc`, inherited auto-reap contradiction, long-lived CLI,
   crash/restart, and a new CLI. Determine whether `B-CONTRADICTED` deliberately
   not returning is an honest fail-closed terminal or an unbounded silent wedge.
7. **T2 residual:** attack the admitted long-lived-CLI zombie residual. Confirm
   that T2's existing `SPAWNING_MIDDLE` plus retained wait ownership and the
   signed resolver form a total, non-competing-reaper route; decide whether a
   zombie can persist indefinitely without a defined resolver action or block
   future progress in a way the contract misclassifies.
8. **Causal and TOCTOU regression:** verify the corrected stage-M proof really
   rests at `m0`/`rel1` and the fork-shared lock, never `m5`/`rel2`. Re-run the
   v2.1.7 object-bound observation, both revalidation barriers, mutation cuts,
   bound-language sweep, A3 residual, CLOSE_OWNED, MALFORMED dominance,
   A3/B1/C1/D1/K1, GC/watchdog/singleton/manifest, generic harness, batch
   settlement, E1/E2/E3, Q/C, and T-inactivity checks.

Do not accept the author closure or examples as proof. Report every finding by
severity, exact normative locus, counterexample, and smallest repair. A
fail-closed label is insufficient if valid history is misclassified, a live
process is abandoned, or progress can wedge without the named terminal status.

## Deliverable

Create exactly one file and alter nothing else:

`reviews/opus_officina_supervisor_control_channel_v2_1_8_final_confirmation.md`

Line 1 exactly one of:

- `CONFIRM_OFFICINA_SUPERVISOR_V2_1_8_X`
- `REVISE_OFFICINA_SUPERVISOR_V2_1_8`

Include the recomputed hash and base, disposition of all five inherited
findings, the eight attack traces, findings, no-regression table, explicit
judgment on the two admitted residuals, author-cell/contract-conflict
determination, and exact authorization boundary.

If confirmed, authorize only Kirill's token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`, conditional on Y
confirming the identical bytes. Authorize no implementation, commit, activation,
entropy, runtime construction, spend, Q/C, or science. If revised, keep the
token unavailable.

Confirm no execution/change/artifact, T `NOT_ACTIVATED`, claim `OPEN`.
