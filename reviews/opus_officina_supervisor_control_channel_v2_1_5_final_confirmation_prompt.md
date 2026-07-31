# Prompt for Claude Code Opus 4.8: independent Officina supervisor v2.1.5 X-line confirmation

Act as the **independent clean-context X-line reviewer**. Claude Code Opus 5
authored v2.1.5; its closure and chat response are untrusted author claims.
Re-derive the result from the normative bytes.

Work in `philosophia` at or after commit
`36b458ae721d9fb5d0cd4f822949e77dc6385962`. Read the complete supervisor
v2 through v2.1.5 chain, both author signatures, inherited generic-harness and
batch-settlement contracts, and both independent v2.1.4 reviews. Your v2.1.4
confirmation applies only to v2.1.4; do not carry it across by assumption.

Recompute the SHA-256 of
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_5_CORRECTION.md`;
expected:

```text
7ef8e4d3ac8f281dd50191e81d2760ed4467648b45ed2b17f6ce2012e4d017d4
```

Static review only. Read-only inspection and literal arithmetic/hashing are
allowed. Run no repository code, tests, probes, smoke commands, or Officina
processes. Alter no existing file or runtime state.

## Required question

Are Sol M1, M2, m1 and m2 closed by exact, executable and total text; are all
v2.1.4 repairs and every earlier independently confirmed closure carried
forward unless named in the replacement index; and does v2.1.5 introduce no
new Critical/Major, no hidden author choice, and no regression in
A3/B1/C1/D1/K1 or inherited signed surfaces?

Attack at least:

1. **Disposition selector:** independently enumerate settlement/quarantine/
   manifest/binding/hash/malformed combinations. The both-terminal layout must
   satisfy only invalidity, B-P must imply no quarantine, B-QM/B-QN no
   settlement, and every admitted/not-yet/impossible state must have exactly
   one continuation with the correct release behavior.
2. **Partial channel construction:** inject failure conceptually at each of
   four `pipe2` calls and every `fpathconf`. Verify the ownership set, exact
   descriptor closure, singleton removal under the lock, lock release,
   retryability and absence of leaks or stale `SPAWNING` state.
3. **Close semantics:** audit `BOOTSTRAP_FD_CLEANUP` against the pinned OS and
   Python semantics, especially `close()` returning `EINTR`, fd-number reuse,
   `EBADF`, other errno, duplicate ownership and idempotence. Confirm that
   treating the fd as closed without retry is truthful on the actual signed
   platform, or report the smallest repair.
4. **Fork and helper cuts:** first-fork failure must be stage 0/no kill;
   second-fork failure must close the last relevant writers and give c13 one
   deterministic EOF/stage-2 route. Trace every helper, kill, prove-death,
   record-removal and cleanup crash prefix and every participant's fd copies.
5. **Refusal ordering:** kill/prove-death must retain the identity records it
   needs; cleanup, §U6.3 record removal and lock release must then be ordered,
   complete and idempotent. No uncaught exception, GC or eventual process exit
   may own a lifecycle transition.
6. **Anti-wedge bound:** verify the universal sufficiency claim is gone;
   slow-valid c14/c15 expiry has one fail-closed cleanup route and cannot become
   evidence, resource fact, retry-shopping state, or a new author cell.
7. **Provenance:** verify the exact seven-row C1/C2/M1-M4/m1 mapping and that no
   stale “six-row” or shifted mapping remains operative.
8. **No regression:** nonblocking bootstrap, quarantine K1 release, GC
   authority, lock-first preflight, watchdog partition, A3 stream-hash truth,
   timestamp arithmetic, schemas, custody, nine events, E1/E2/E3, Q/C and T
   inactivity.

Do not accept examples or the author's closure in place of total rules. Report
new findings by severity, exact locus, counterexample and smallest repair.

## Deliverable

Create exactly one file and alter nothing else:

`reviews/opus_officina_supervisor_control_channel_v2_1_5_final_confirmation.md`

Line 1 exactly one of:

- `CONFIRM_OFFICINA_SUPERVISOR_V2_1_5_X`
- `REVISE_OFFICINA_SUPERVISOR_V2_1_5`

Include hash/base, one-to-one disposition of Sol M1/M2/m1/m2, all eight attack
traces, findings by severity, no-regression table, author-cell determination,
and exact authorization boundary.

If confirmed, authorize only Kirill's signature token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`, conditional on an
independent Y confirmation of the same bytes. Authorize no implementation, T
activation, entropy, runtime construction, spend, Q/C or science. If revised,
keep the token unavailable and require another bounded X/Y review.

Confirm no code/test/probe/process ran, no existing file changed, no runtime or
scientific artifact was created, T remains `NOT_ACTIVATED`, and claim `OPEN`.
