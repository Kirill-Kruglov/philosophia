# Prompt for GPT-5.6 Sol: independent Officina supervisor v2.1.6 Y-line confirmation

Act as the **independent clean-context Y-line reviewer**. Claude Code Opus 5
authored v2.1.6. Treat its closure/chat response as untrusted self-assessment
and re-run your v2.1.5 counterexamples against the normative text.

Work in `philosophia` at or after commit
`692207aa07ad87fcf46a9827524b25ca54d56c07`. Read the complete supervisor
v2 through v2.1.6 chain, author signatures, inherited generic-harness and
batch-settlement contracts, and your completed v2.1.5 review. Record that no
formal X verdict existed for v2.1.5.

Recompute the SHA-256 of
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_6_CORRECTION.md`;
expected:

```text
e4aa9ef4f0de2fe705d54cb7ac016212098cfe71b8575ef2b435e8c9b09f5609
```

Static review only. Read-only inspection and literal arithmetic/hashing are
allowed. Run no code, tests, probes, smoke commands, or Officina processes.
Modify no existing file or runtime state.

## Required question

Are your v2.1.5 C1, M1, M2, M3 and m1 closed exactly, with no new
contradiction, TOCTOU release path, fd/resource leak, live-record removal,
silent wedge, hidden author judgment or regression?

Re-run independently:

1. **C1 physical/validity cross-product:** physical presence is decode-free;
   malformed dominates; every release requires physical absence of the
   opposite terminal. Test symlink/directory/partial/truncated/zero-byte and all
   five prior counterexamples, plus mutation between presence and validation.
2. **C1 selector totality:** Rule 0 and Rule 1 artifacts/causes, pending versus
   impossible layouts, binding/hash mismatch, and every PS/PQ/PF/VS/VQ/VF
   combination must have one continuation and correct release count.
3. **M1 close state machine:** audit every named close including both lock
   closes. Verify `EINTR`, `EBADF`, other errors, NOT_OWNED, forked fd copies,
   number reuse, restart and second call. Specifically attack whether uniform
   CONTINUE after `CLOSED_ERROR` is sound at lock release and every gate.
4. **M2 c5-c7:** trace the exact identity available at each instruction,
   capture-to-kill races, PID reuse, ppid/start checks, absence/unreadability,
   middle-record rename/durability cuts, kill escalation, death proof and the
   no-unlink/no-free continuation when proof is unavailable.
5. **M2 crash prefixes:** interrupt every identity/kill/proof/close/unlink/fsync/
   lock step; prove restart cannot unlink a live attempt, kill a reused PID,
   close a reused fd or leave a falsely free singleton.
6. **M3 operative-language search:** verify all universal no-blocking and
   healthy-within-bound assertions/tests are actually replaced, not shadowed;
   rows 121/126/159-162 must be jointly satisfiable and slow-valid refusal
   permanently non-citable.
7. **m1 pipe causality:** check all eight ends, readers/writers and inherited
   copies. The final `boot_w` must be the only stated cause of c13 EOF; no
   `rel3_r` or m0 EOF misattribution may remain.
8. **No regression:** rerun v2.1.5's preserved selector bodies, K1 custody,
   bootstrap/fork routes, A3/B1/C1/D1, GC, watchdog, singleton, author
   authority, generic harness/batch settlement, events, E1/E2/E3, Q/C and T.

Fail-closed is insufficient if valid history is misclassified or resource
release/forward progress silently wedges. Do not accept examples or author
assertions in place of total governing rules.

## Deliverable

Create exactly one file and modify nothing else:

`reviews/sol_officina_supervisor_control_channel_v2_1_6_final_confirmation.md`

Line 1 exactly one of:

- `CONFIRM_OFFICINA_SUPERVISOR_V2_1_6_Y`
- `REVISE_OFFICINA_SUPERVISOR_V2_1_6`

Include hash/base, disposition of C1/M1/M2/M3/m1, eight traces, findings by
severity with loci/counterexamples/smallest repair, no-regression table,
author-cell determination and exact authorization boundary.

If confirmed, authorize only Kirill's token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`, conditional on X
confirming the same bytes. Authorize no implementation, T activation, entropy,
runtime construction, spend, Q/C or science. If revised, keep the token closed.

Confirm no code/test/probe/process ran, no existing file changed, no T/Q/C,
runtime or scientific artifact was created, T remains `NOT_ACTIVATED`, and the
programme claim remains `OPEN`.
