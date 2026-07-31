# Prompt for Claude Code Opus 5: Officina supervisor/control-channel v2.1.6 bounded repair

You are **Claude Code Opus 5 acting only as the specification author**, not an
independent reviewer. Work in `philosophia` at or after commit
`2d24fe0ff8209ca401f552bf091cd2611d64371f`.

Read the complete supervisor v2 through v2.1.5 chain, both signed author
selection records, inherited generic-harness and batch-settlement contracts,
and the completed independent Y-line v2.1.5 review:

- `reviews/sol_officina_supervisor_control_channel_v2_1_5_final_confirmation.md`

Also read the saved X-line chat trace, but record accurately that it stopped
before creating the required formal review and therefore supplies **no X
verdict** for v2.1.5:

- `reviews/opus_officina_supervisor_control_channel_v2_1_5_final_confirmation_chat_response.md`

Pinned hashes:

```text
7ef8e4d3ac8f281dd50191e81d2760ed4467648b45ed2b17f6ce2012e4d017d4  v2.1.5 correction
c8551990a9a794eb907ed31ab29488bb019c2e4d94783c713f66f3426f063906  Sol Y review
f4a4f1d693131360c14d0e42919dbddca81effd688840f20f3c1603e6fe48a70  incomplete Opus X chat trace
```

Sol returned `REVISE_OFFICINA_SUPERVISOR_V2_1_5` with C1, M1, M2, M3 and m1.
That verdict governs. Treat all author closures as untrusted. Static authoring
only: run no code, tests, probes, smoke commands, or Officina process; modify
no runtime state.

## Deliverables

Create exactly two new files and alter nothing else:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_6_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_6_closure.md`

The correction must be a narrow replacement layer over v2.1.5 with an exact
replacement index. Everything not explicitly replaced carries forward
verbatim. Closure line 1 must be exactly one of:

- `READY_FOR_OFFICINA_SUPERVISOR_V2_1_6_FINAL_XY_CONFIRMATION`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_6_AUTHOR_CELL`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_6_CONTRACT_CONFLICT`

No new author cell is expected. Preserve all v2.1.5 repairs not implicated by
the findings below and every earlier independently confirmed closure.

## Mandatory repairs

### R1. Physical presence dominates validated terminal state (Sol C1)

The selector must never interpret malformed canonical data as physical
absence. Define separate physical-presence predicates for settlement,
quarantine and manifest (`PS`, `PQ`, `PF`) and separate valid-decoded
predicates. Compute `MALFORMED` from every physically present canonical object
before any releasing predicate is eligible.

Use one total selector whose first effective rule is:

```text
any physically present malformed/partial canonical object
  -> record-first invalidity/refusal; release nothing; no branch entered
```

Then make both-terminal presence physical, not validation-dependent. Every
releasing predicate must require `not MALFORMED` and physical absence of the
opposite terminal: B-P requires `not PQ`; B-QM/B-QN require `not PS`. Keep
binding/file/hash predicates explicit. Rebuild the complete cross-product over
PS/PQ/PF, validity/malformed, binding null/non-null and hash match/mismatch.
Each row must satisfy exactly one rule; malformed settlement plus valid
quarantine and malformed quarantine plus valid settlement must release nothing.

Preserve normal B-P/B-QM/B-QN branch bodies, K1 accounting, no-reread and
complete-custody rules. No author choice is needed.

### R2. One close transition everywhere (Sol M1)

Define one single-fd `CLOSE_OWNED(owner, fd, context)` transition, with the
pinned Linux/Python semantics stated once, and use it at **every** normal and
failure close site, including `SPAWN.lock`. The multi-fd cleanup must be only a
fixed-order loop over this primitive; no separate close semantics may survive.

The transition must pin, without implementer discretion:

- ownership is removed exactly once for every returned outcome;
- success removes ownership and continues;
- `EBADF` is classified exactly and never retried;
- Linux `EINTR` and every other non-EBADF error remove ownership and never
  retry the fd number because it may have been reused;
- whether each non-EBADF error continues normal flow or changes to the exact
  context-specific refusal route **after ownership removal**;
- diagnostics, if any, are closed control-plane facts and cannot alter science,
  resources, custody or author decisions;
- a second call cannot close a reused number and is a no-op/refusal as pinned.

Replace or extend every inherited c5/m1/m6/c8/c12/c13/m8/c16/g1/g3/c18 and
lock-close clause explicitly. Audit forked copies as distinct ownership. Pin
normal, failure and restart behavior. Do not rely on exceptions, destructor,
GC, caller exit, or an unspoken POSIX convention.

### R3. Kill/prove death before c5-c7 record removal (Sol M2)

Split c5, c6 and c7 into exact individual failure routes. For every post-first-
fork failure:

1. identify the current middle child using the strongest exact in-memory and
   durable identity available at that instruction;
2. if identity-safe, use the inherited pre-group `kill(pid)` route;
3. prove death under the signed identity rules;
4. only then close every owned fd through `CLOSE_OWNED`;
5. remove only records belonging to this attempt in the inherited P1/P2/P3 and
   §U6.3 order while still holding `SPAWN.lock`;
6. release the lock through `CLOSE_OWNED` and refuse.

If identity cannot be proved at a cut, specify one fail-closed continuation
that does not unlink a potentially live record or silently release the lock.
Do not claim c5-c7 CLI closure yields EOF while the middle owns a writer. Pin
the exact stage, kill authority, durable/in-memory fields and crash recovery for
each of c5, c6 and c7. Re-run every prefix before/after kill, proof, close,
unlink/fsync and lock release.

### R4. Remove contradictory universal bound language (Sol M3)

Replace, rather than merely extend, every carried assertion that no bootstrap
syscall can outlive the deadline or that every healthy launch releases within
the bound. The accurate invariant is narrower: no bootstrap **pipe read or
write** can block past its bounded helper deadline. `/proc` verification,
canonical file install and file/directory `fsync` have no executable duration
bound in the signed text.

Explicitly replace v2.1.4 §V214.1.1/§V214.1.5 universal assertions and test rows
121 and 126. Row 126 must test the deterministic slow-valid refusal and its
non-citability; reconcile rows 159-162 so the test contract is satisfiable and
contains no contradictory carry-forward sentence.

### R5. Correct the EOF ownership annotation (Sol m1)

Move the causal annotation for c13 boot EOF to the `boot_w` ownership row.
Closing the last `boot_w`, not `rel3_r`, produces EOF on `boot_r`. Leave the
`rel3_r` row as ownership cleanup only. Check every analogous causal annotation
against the actual read/write pair.

## Required proof obligations

1. Exact v2.1.5-to-v2.1.6 replacement index and statement that nothing else
   moves.
2. One-to-one disposition of Sol C1/M1/M2/M3/m1; explicit record that no formal
   v2.1.5 X verdict exists and fresh X/Y reviews are required for v2.1.6.
3. Full physical-presence/validity/malformed selector truth table with every
   row exclusive and all malformed opposite-terminal counterexamples included.
4. One `CLOSE_OWNED` state machine applied by name to every normal, cleanup and
   lock close, including errno, ownership, fd-reuse and second-call traces.
5. Exact c5/c6/c7 identity, kill, death-proof, fd, record, fsync, lock and crash
   tables; no live removal and no false EOF claim.
6. Search-and-replacement table for every stale universal bound assertion and
   test row 121/126/159-162 reconciliation.
7. Correct boot_w/boot_r EOF provenance and complete descriptor annotation
   audit.
8. No-regression table for A3/B1/C1/D1/K1, all v2.1.4/v2.1.5 closures not
   replaced, generic harness, batch settlement, nine events, E1/E2/E3, Q/C,
   T inactivity and claim OPEN.
9. Exact future implementation/test obligations, but no implementation or
   authorization.
10. One bounded fresh-confirmation question each for independent Opus 4.8 X
    and GPT-5.6 Sol Y, requiring SHA-256 recomputation and re-running all five
    counterexamples plus no-regression.

## Prohibitions and authorization boundary

Do not edit prior specs, reviews, prompts, signatures, code, tests, runtime
trees, Cursor's dirty implementation, or unrelated dirty/untracked files. Do
not execute tests or processes. Do not create entropy, worlds, candidates,
capacity/custody/result artifacts, Q/C objects, or science.

Do not authorize
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`. It remains unavailable
until both fresh independent X and Y reviews confirm the exact v2.1.6 bytes.
Do not authorize implementation, T activation, E1/E2/E3 spend, or later gates.

Confirm exactly two deliverables, T remains `NOT_ACTIVATED`, the programme
claim remains `OPEN`, and no runtime or scientific artifact was created.
