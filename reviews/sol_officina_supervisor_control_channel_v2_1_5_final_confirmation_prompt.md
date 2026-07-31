# Prompt for GPT-5.6 Sol: independent Officina supervisor v2.1.5 Y-line confirmation

Act as the **independent clean-context Y-line reviewer**. Claude Code Opus 5
authored v2.1.5. Treat its correction closure and chat response as untrusted
self-assessment. Re-test the repair against your v2.1.4 counterexamples.

Work in `philosophia` at or after commit
`36b458ae721d9fb5d0cd4f822949e77dc6385962`. Read the complete supervisor
v2 through v2.1.5 chain, both author signatures, inherited generic-harness and
batch-settlement contracts, and both independent v2.1.4 reviews.

Recompute the SHA-256 of
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_5_CORRECTION.md`;
expected:

```text
7ef8e4d3ac8f281dd50191e81d2760ed4467648b45ed2b17f6ce2012e4d017d4
```

Static review only. Read-only inspection and literal arithmetic/hashing are
allowed. Run no code, test, probe, smoke command, or Officina process. Modify
no existing file or runtime state.

## Required question

Are your v2.1.4 M1, M2, m1 and m2 closed exactly, with no new contradiction,
valid-history misclassification, fd/resource leak, silent wedge, hidden author
judgment or regression in the previously closed supervisor contract?

Re-run independently:

1. **M1 exhaustive selector trace:** enumerate all physical terminal,
   binding, manifest, hash and malformed states. Prove branch predicates are
   structurally exclusive rather than saved by reading order; both-terminal
   releases nothing; ordinary not-yet-terminal and impossible durable layouts
   receive the correct distinct continuation.
2. **M2 construction trace:** fail each `pipe2` and `fpathconf` at every prefix;
   account for every fd copy and singleton record; verify cleanup happens under
   the held lock in the inherited order and leaves neither leaks nor wedges.
3. **M2 close/errno trace:** challenge the claim that Linux/Python `close`
   returning `EINTR` has already released the fd, and that never retrying is
   correct under the pinned platform. Include fd reuse, `EBADF`, other errno,
   second invocation and partial ownership. Reject any reliance on destructor,
   GC or caller exit.
4. **M2 fork/helper trace:** first and second fork failures, EOF ownership at
   c13, all bounded read/write failures, middle/grandchild death orderings,
   kill/prove-death requirements, record cleanup and `SPAWN.lock` release.
5. **Crash-prefix trace:** interrupt before/after every close, kill, proof,
   singleton unlink/fsync and lock release. Confirm restart has exactly one
   legal continuation and no live identity record is removed prematurely.
6. **m1 bound trace:** a slow but valid c14/c15 path may expire; verify the text
   calls this policy rather than proof, routes it deterministically, and creates
   no citable validity/resource/scientific fact or shopping state.
7. **m2 provenance trace:** verify the seven exact mappings and search the full
   carried chain for stale operative reconciliation language.
8. **No regression:** rerun your v2.1.4 A3/K1, spawn, C1 replacement, B1/GC,
   manifest/custody, singleton, author-authority and exactness traces, including
   the repairs v2.1.5 does not name.

Fail-closed is insufficient if valid history is misclassified or forward
progress/resource release is silently wedged. Do not accept worked examples or
author assertions in place of governing rules.

## Deliverable

Create exactly one file and modify nothing else:

`reviews/sol_officina_supervisor_control_channel_v2_1_5_final_confirmation.md`

Line 1 exactly one of:

- `CONFIRM_OFFICINA_SUPERVISOR_V2_1_5_Y`
- `REVISE_OFFICINA_SUPERVISOR_V2_1_5`

Include hash/base, one-to-one disposition of M1/M2/m1/m2, the eight traces,
new findings by severity with exact loci and smallest repair, no-regression
table, author-cell determination, and exact authorization boundary.

If confirmed, authorize only Kirill's signature token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`, conditional on the X
line confirming the same bytes. Authorize no implementation, T activation,
entropy, runtime construction, spend, Q/C or science. If revised, keep the
token unavailable and require another bounded X/Y review.

Confirm no code/test/probe/process ran, no existing file changed, no T/Q/C,
runtime or scientific artifact was created, T remains `NOT_ACTIVATED`, and the
programme claim remains `OPEN`.
