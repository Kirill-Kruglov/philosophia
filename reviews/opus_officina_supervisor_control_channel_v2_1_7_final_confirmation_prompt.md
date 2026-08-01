# Prompt for Claude Code Opus 4.8: independent Officina supervisor v2.1.7 X-line confirmation

Act as the **independent clean-context X-line reviewer**. Claude Code Opus 5
authored v2.1.7; its closure/chat response are untrusted author claims. Rebuild
the result from normative bytes and both v2.1.6 REVISE reviews.

Work in `philosophia` at or after commit
`063d29042175e05d35eb3fee2b7403cca300c1a9`. Read the complete supervisor
v2 through v2.1.7 chain, author signatures, inherited generic-harness and
batch-settlement contracts, and both v2.1.6 reviews.

Recompute the SHA-256 of
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_7_CORRECTION.md`;
expected:

```text
789732476938ca8c1436eebb49e54a1f994c2c000b7689e1eb9aad082f6871a8
```

Static review only. Read-only inspection and literal arithmetic/hashing are
allowed. Run no code, tests, probes, smoke commands, or Officina processes.
Alter no existing file or runtime state.

## Required question

Are Sol C1/M1/M2 and X216-M1/X216-m1 closed by exact, total text, with no new
TOCTOU release, false death proof, untracked live process, stale bound claim,
hidden author choice, resource leak or silent wedge?

Attack at least:

1. **Object-bound observation:** trace enumerate/lstat/open(O_NOFOLLOW)/fstat/
   read/decode/hash for absent, regular, symlink, directory, hardlink, zero,
   truncated and concurrently replaced objects. A retained fd pins an inode,
   not its name; prove barriers rebind the canonical name and all three records
   to one coherent rule or release nothing.
2. **Two barriers:** mutate each name before/after every observation step,
   between initial snapshot and branch, between branch and barrier 2, and after
   barrier 2. Verify same identity/bytes/paired absence and same-rule checks;
   only the post-final-barrier window may remain, honestly as signed A3
   procedural residual, never as an “impossible” or citable result.
3. **Stat/signal/wait automaton:** enumerate every `/proc`, SIGTERM, SIGKILL and
   `waitpid` result, deadline edge, ordinary exit and PID-reuse race. No
   exception or parser/signal/wait result may escape or infer death indirectly.
4. **`ECHILD` premise:** independently verify the contract, launcher and
   inherited process state actually guarantee default `SIGCHLD`, no
   `SIG_IGN`, no `SA_NOCLDWAIT`, no other reaper and no prior reaping. “This
   contract installs none” is insufficient if a disposition can be inherited.
   If the premise is not mechanically pinned before fork, reject
   `ECHILD => PROVED_DEAD` and give the smallest repair.
5. **T1/T2/T3 recovery:** trace a long-lived CLI, stopped middle, unreadable
   `/proc`, all signal/wait errors, crash cuts and restart. T2 must install a
   truthful existing `SPAWNING_MIDDLE` record before removing SPAWNING. T3 must
   not erase the last handle to a live middle that can later act.
6. **Two-supervisor safety:** for every scheduling cut, prove a middle surviving
   T3 cannot pass m5 or later fork a grandchild after the CLI closes `rel2_w`.
   Include stopped/resumed middle, buffered release data, inherited writer
   copies, timeout edges and a new CLI starting immediately after SPAWNING
   removal.
7. **Bound-language sweep:** reproduce the declared semantic search over all
   operative layers, including §N11, §N3.5, §N12 row 86, §U2.4 and §U2.7.
   Confirm no fixed total CLI bound survives and all revised tests are jointly
   satisfiable; only lock acquisition and pipe I/O have signed deadlines.
8. **No regression:** `CLOSE_OWNED`, MALFORMED dominance, branch bodies, K1
   custody/release, A3/B1/C1/D1, GC/watchdog/singleton/manifest, generic
   harness, batch settlement, events, E1/E2/E3, Q/C and T inactivity.

Do not accept author examples/closure as proof. Report findings by severity,
exact locus, counterexample and smallest repair.

## Deliverable

Create exactly one file and alter nothing else:

`reviews/opus_officina_supervisor_control_channel_v2_1_7_final_confirmation.md`

Line 1 exactly one of:

- `CONFIRM_OFFICINA_SUPERVISOR_V2_1_7_X`
- `REVISE_OFFICINA_SUPERVISOR_V2_1_7`

Include hash/base, disposition of all five inherited findings, eight attack
traces, findings, no-regression table, author-cell determination and exact
authorization boundary.

If confirmed, authorize only Kirill's token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`, conditional on Y
confirming the same bytes. Authorize no implementation, activation, entropy,
runtime construction, spend, Q/C or science. If revised, keep it unavailable.

Confirm no execution/change/artifact, T `NOT_ACTIVATED`, claim `OPEN`.
