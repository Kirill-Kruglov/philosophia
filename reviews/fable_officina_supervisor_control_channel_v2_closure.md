READY_FOR_OFFICINA_SUPERVISOR_V2_XY_REVIEW

# Fable 5 — Officina supervisor/control-channel v2 closure

Companion:
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`.
Author selections (sole A/B/C/D authority):
`successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md`
→ A3, B1, C1, D1. Exactly two files created; no code, tests, existing
contracts, signatures, reviews, or runtime artifacts edited; no
supervisor/controller/worker/FIFO/watchdog/journal started; no entropy,
authorization, manifest, capability, world, learner, datum, or outcome.
T remains `NOT_ACTIVATED`.

## 1. Verdict

`READY_FOR_OFFICINA_SUPERVISOR_V2_XY_REVIEW`.

Not `BLOCKED_OFFICINA_SUPERVISOR_V2_AUTHOR_CELL`: the per-operation
output byte budget is owned by new control-plane
`t-operation-output-bound.v1` declared before spawn — no universal GiB
and no amendment of signed `t-draft-manifest.v1`. Not
`BLOCKED_OFFICINA_SUPERVISOR_V2_CONTRACT_CONFLICT`: C1’s positive
deadline overrun is pinned to already-authorized invalid/recovery
destinations while retaining signed §4c charging; no physical
non-RT scheduling miracle is claimed.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains
**not signable** until both fresh X/Y reviews accept this v2.

## 2. Embedded selections (normative, not by reference alone)

| Token | Where embedded | Deleted v1 contradiction |
|---|---|---|
| A3 | §V2.2 | mode-bit / `0700`/`0000` secrecy |
| B1 | §V2.5 + idempotency_key in §V2.4.2 | ephemeral replay; durable-state-alone idempotency |
| C1 | §V2.6 | serial-loop physical “at or before deadline” |
| D1 | §V2.1.1 | 60 s idle exit |

A3 states explicitly: mechanical against accidental/contract-following
misuse and endpoint-role violations; procedural only against deliberate
same-UID inspection; **not** citable as Q/C confidentiality.

## 3. Mechanical ledger 1–15 + §S6

Closed in §V2.1 (bootstrap, registry, singleton lock, zombies, logs,
sequence), §V2.2 (roles, observation), §V2.4 (eight-command schemas,
FIFO rules, `PROMOTED` as `detail.phase`), §V2.5 (journal/ack),
§V2.6 (watchdog automata), §V2.7 (bound, grammar, descriptor hash,
`SETTLEMENT.json` commit, streams), §V2.8 (§S6 carry-forward),
§V2.9–V2.11 (states, archival exclusions, crash cuts), §V2.10 (real
`-m` CLI, zero allowlist delta, frozen files). Disposition map:
§V2.13.

## 4. C1 honesty on non-RT Linux

§V2.6.1 disclaims physical deadline execution under every host
schedule. Preserved: independently scheduled freezer that never writes
`runtime/`; sole supervisor settles. Strongest implementable pins:
`CLOCK_MONOTONIC` deadlines, `table_seq` update/ack health,
identity-safe STOP/KILL, durable/re-derivable freeze observation,
`overrun_ns > 0` → invalid/recovery only (never valid T ending), total
death/restart table. Compatible with signed §4c full-interval charge.

## 5. Output bytes before behavior

§V2.7.1–V2.7.2: durable per-operation `max_total_output_bytes` before
spawn; logical `st_size` and allocated `st_blocks*512` both bounded;
sparse/hardlink/symlink rules; refuse before hashing excess; bounded
restartable hash loops; reservation released on exactly one terminal.
No global numerical constant invented; signed draft-manifest untouched.

## 6. Non-regression / surfaces

Batch-settlement amendment and harness composite not weakened. No new
root, manifest, activation, or execution authorized. Implementation
surface after future signature: `generic_harness.py` + tests + signed
accounting amendment only. Frozen: `runtime.py`, `ledger.py`,
`checkpoint.py`, `verification.py`, `activation.py`, events, scientific
constants, roots.

## 7. Bounded questions (≤3 each)

**Opus — Linux/process/crash executability**
1. Is the self-stop + `WIFSTOPPED` + spawn-intent registry path free of
   a behavior-capable window and of undiscoverable pre-claim orphans
   under crash between every pair of steps in §V2.1.4?
2. Under §V2.6, can any reachable schedule leave a controller group
   runnable past deadline without a freeze observation and, if
   `overrun_ns > 0`, without forcing the invalid/recovery route?
3. Is every promotion/journal/watchdog death cut in §V2.11 single-
   valued on real Linux (including reparented `Z` and
   SETTLEMENT-vs-rename ordering)?

**Sol — idempotency, observation, validity, scientific non-regression**
1. Does B1 (§V2.5) make all eight commands exactly-once-effect across
   generations, with ADMIT retry spawning no second worker/cursor and
   release bytes redeliverable until durable ack only?
2. Is A3’s observation claim honest (no mode-bit secrecy; mechanical
   roles/grammar only), and does it block inheritance as Q/C
   confidentiality?
3. Do §V2.7 bounds + §V2.8 batch wiring leave E1/E2/E3 constants,
   nine events, runtime schemas, and scientific cells unmoved while
   still failing closed on sparse/huge outputs and counter-only
   terminals?

## 8. Negative authorization

This closure authorizes only bounded X/Y review of the v2 draft. It
authorizes no implementation, commit of dirty Cursor files, process,
endpoint, journal instance, activation, capability, world, learner,
entropy, E1/E2/E3 spend, Q/C object, datum, outcome, or claim movement.
`successor/officina/runtime/` remains `{T_RUNTIME.lock}`; envelope
remains inactive; programme claim remains `OPEN`.
