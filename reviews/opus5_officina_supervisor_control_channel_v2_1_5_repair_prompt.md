# Prompt for Claude Code Opus 5: Officina supervisor/control-channel v2.1.5 bounded repair

You are **Claude Code Opus 5 acting only as the specification author**, not an
independent reviewer. Work in `philosophia` at or after commit
`bf379f29dae0e2645f78a276a3cf62150e0b93de`.

Read the complete v2/v2.1/v2.1.1/v2.1.2/v2.1.3/v2.1.4 supervisor chain, both
signed author-selection records, inherited generic-harness and batch-settlement
contracts, and both independent v2.1.4 reviews in full:

- `reviews/opus_officina_supervisor_control_channel_v2_1_4_final_confirmation.md`
- `reviews/sol_officina_supervisor_control_channel_v2_1_4_final_confirmation.md`

Pinned hashes:

```text
cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62  v2.1.4 correction
4bb6961b21bb010745ab5093cf25545a4ea6440dacff238d53cbc089fda13625  Opus X confirmation
0e20212d7258b4462a23a67750fa886aca8a82a4f5a0cb62f55205f5b8ef7310  Sol Y review
```

The X line confirmed v2.1.4. The Y line returned
`REVISE_OFFICINA_SUPERVISOR_V2_1_4` with two Major and two Minor findings.
The Y verdict governs the authorization state. Treat every author closure as
untrusted self-assessment. Static authoring only: run no repository code,
test, probe, smoke command, or Officina process; alter no runtime state.

## Deliverables

Create exactly two new files and alter nothing else:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_5_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_5_closure.md`

The correction must be a narrow replacement layer over v2.1.4 with an exact
replacement index. Everything not explicitly replaced carries forward
verbatim. Closure line 1 must be exactly one of:

- `READY_FOR_OFFICINA_SUPERVISOR_V2_1_5_FINAL_XY_CONFIRMATION`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_5_AUTHOR_CELL`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_5_CONTRACT_CONFLICT`

No new author cell is expected. Preserve every closure independently confirmed
by X and every v2.1.4 repair not implicated below.

## Mandatory repairs

### R1. Make terminal disposition branches exclusive (Sol M1)

The mandatory both-terminal invalidity/refusal must dominate branch selection.
Define one total ordered selector over physical durable objects:

1. settlement and quarantine both durable: record-first invalidity/refusal,
   release nothing;
2. settlement durable and quarantine absent: B-P only;
3. quarantine durable and settlement absent with non-null manifest binding:
   B-QM only;
4. quarantine durable and settlement absent with null binding plus physical
   manifest absence: B-QN only;
5. every other state, including neither terminal, binding/file mismatch,
   orphan file without binding, binding without file, duplicate or partial
   object: record-first invalidity/refusal, release nothing.

State the predicates literally, not as an ordered prose implication. Re-run a
complete truth table over settlement present/absent, quarantine present/absent,
binding null/non-null, manifest present/absent, hash match/mismatch, and partial
or malformed objects. Every row must have exactly one continuation. Preserve
the legitimate B-QM K1 release and all no-reread/custody constraints.

### R2. Totalize bootstrap construction and cleanup (Sol M2)

Define one idempotent bootstrap-fd cleanup routine over **every successfully
created end** of all four channels, parameterized only by the current ownership
table. It must close every still-owned bootstrap descriptor exactly once,
treat already-closed as success, pin every close error, and be invoked on every
CLI refusal/failure path. After `c2` has installed `SPAWNING.json`, every such
route must also perform the inherited §U6.3 singleton cleanup in its exact
order while holding `SPAWN.lock`; no live or partial singleton may remain.

Pin all construction cuts:

- first, second, third or fourth `pipe2` failure;
- every `fpathconf` failure or invalid `PIPE_BUF` result after any creation;
- `c4` first `os.fork` failure: stage 0, no kill, fd cleanup plus singleton
  cleanup and lock release;
- `m7` second `os.fork` failure: close the middle's still-owned ends and
  `_exit(3)` so the CLI's bounded `c13` path observes EOF and performs stage-2
  cleanup;
- every BOUNDED_READ/BOUNDED_WRITE/helper failure at c8/c9/c12/c13/c16,
  including EINTR/EAGAIN/EOF/EPIPE/malformed/deadline routes;
- every kill/prove-death/record-removal/lock-release crash prefix.

Make the normal close table and the failure cleanup table jointly exhaustive.
No uncaught language exception, eventual process exit, garbage collection, or
implementer convention may own a lifecycle transition. Re-run c2 through c18,
m0 through m9 and g0 through identity for every construction/fork/helper cut;
prove no descriptor leak, live `SPAWNING` conflict, pipe cycle, or retained
`SPAWN.lock` remains.

### R3. Make the grandchild bound claim honest (Sol m1)

Keep the signed constants unchanged. Delete the universal claim that
`2 * T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS` is mathematically sufficient for every
healthy c14/c15 verification and durable install unless an executable bound
for those operations already follows from signed text. State instead that it
is the fixed anti-wedge policy: expiry is a permitted fail-closed bootstrap
refusal even for an otherwise valid but slow install. Pin the resulting cleanup
route and ensure it cannot become scientific/resource evidence or a retry-
shopping channel.

### R4. Correct the provenance table (Sol m2)

Replace v2.1.4 §V214.8.3's stale “six rows” with the exact seven-row mapping:

```text
C1 -> §V214.1
C2 -> §V214.2
M1 -> §V214.3
M2 -> §V214.4
M3 -> §V214.5
M4 -> §V214.6
m1 -> §V214.7
```

Do not relabel findings or imply the X confirmation carries across changed
v2.1.5 bytes. This is provenance repair only.

## Required proof obligations

Include all of the following in the correction and closure:

1. Exact v2.1.4-to-v2.1.5 replacement index and declaration that no other text
   moves.
2. One-to-one disposition of Sol M1/M2/m1/m2 and an explicit record that X
   confirmed v2.1.4 but fresh X/Y confirmation is required for v2.1.5.
3. Exhaustive mutually exclusive disposition truth table, including the
   both-terminal row first.
4. Complete descriptor ownership and idempotent cleanup table for every
   partial construction, fork, helper, close, kill, record and crash cut.
5. Exact c2-c18/m0-m9/g0 traces for first-fork and second-fork failure.
6. Honest fixed anti-wedge bound semantics and slow-valid-install trace.
7. Correct seven-row provenance mapping.
8. No-regression table for A3/B1/C1/D1/K1, v2.1.4's closed C1/C2/M1-M4/m1,
   inherited generic harness/batch settlement, nine events, E1/E2/E3, Q/C,
   T inactivity and claim OPEN.
9. Exact future implementation/test obligations, but no implementation or
   authorization.
10. One bounded final-confirmation question each for independent Opus 4.8 X
    and GPT-5.6 Sol Y, requiring recomputation of the v2.1.5 SHA-256 and attack
    of all four repairs plus no-regression.

## Prohibitions and authorization boundary

Do not edit prior specs, reviews, prompts, signatures, code, tests, runtime
trees, Cursor's dirty implementation, or unrelated dirty/untracked files. Do
not execute tests or processes. Do not create entropy, worlds, candidates,
capacity/custody/result artifacts, Q/C objects, or science.

Do not authorize the signature token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`. It remains
unavailable until both fresh independent X and Y confirmations accept the exact
v2.1.5 bytes. Do not authorize implementation, T activation, E1/E2/E3 spend,
or any later gate.

Confirm exactly two deliverables, T remains `NOT_ACTIVATED`, the programme
claim remains `OPEN`, and no runtime or scientific artifact was created.
