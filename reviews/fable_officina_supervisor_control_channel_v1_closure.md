READY_FOR_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_XY_REVIEW

# Fable 5 — Officina supervisor/control-channel v1 closure memo

Author: Fable 5. Companion:
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md`.
Inputs: the signed composite (`OFFICINA_GENERIC_HARNESS_SIGNATURE.md`
and its governing hashes) and the three implementation reviews at
review-evidence commit `5c00d5ffa9f67b6907bd370b9efccaf542646ba4`
(Codex `REVISE_IMPLEMENTATION`, C1–C4/M1–M6; Opus `REVISE…` with the
`BLOCKED_CONTRACT` sub-finding; Sol `BLOCKED…`, R0 + C1–C4/M1–M7). The
four uncommitted Cursor files were read **only as evidence** and were
not modified. Exactly two files were created; nothing else changed;
nothing committed; no entropy, authorization, manifest, runtime
artifact, process, capability, world, learner, spend, Q/C object,
datum, or outcome exists; T remains `NOT_ACTIVATED`.

The `READY` verdict is justified by §7 below: the draft pins one
topology, one channel byte format, one watchdog rule, one promotion
order, and one continuation per crash cut; two independent
implementers no longer choose any policy inline.

## 1. Verdict

`READY_FOR_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_XY_REVIEW` — one
bounded X/Y confirmation of this correction is the only next step;
after both confirmations the author token candidate (§9) becomes
signable; after that signature, Cursor repairs proceed per §S6 with no
remaining design authority.

## 2. Exact replacement/addition index over the signed composite

| Signed locus | Action |
|---|---|
| v2 §1 ownership paragraph | completed by §S1 (singleton supervisor; creation; lifetime; lock/capability custody) |
| v2 §2c.1–2c.3 | completed by §S1.3 (controller spawned frozen **before** the claim; the signed claim keys `controller_pid`/`controller_start_identity`/`process_group_id`/`argv` carry the real observed values — no schema change) |
| v2 §2c.4–2c.5 | completed by §S1.5/§S3 (autonomous at-or-before-deadline settlement; channel-admitted operations) |
| v2 §2c.6 | completed by §S1.5 (whole close sequence in one supervisor lock epoch) |
| v2 §5a "separate supervisor" sentence | **replaced** by §S1.1 (one supervisor; per-tree sessions/groups) — the only replaced signed sentence |
| v2 §5b | completed by §S3 (channel, promotion order, one-use delivery, quarantine/disposal, crash cuts) |
| v2 §9 argv/import paragraphs | completed by §S5 (exact `-m` pair parsing; zero-allowlist-delta proof) |
| v2 §10 | extended by §S7 rows |
| new | §S2 closed channel; §S4 boundary-integration references; §S6 repair ledger; five engineering control constants; six closed control-artifact schemas |

## 3. One-to-one disposition of findings

| Finding | Disposition |
|---|---|
| Opus BLOCKED_CONTRACT (a): who holds deadline/capability between CLI invocations; lazy vs persistent watchdog | Pinned §S1.1/§S1.5: a genuinely persistent supervisor holds both; firing rule `now + poll ≥ deadline` guarantees action at or before the deadline with no CLI; lazy detection remains only for the supervisor-death **fault** class, proved to be exactly the signed §4c process-loss route (no process exists that could act) |
| Opus BLOCKED_CONTRACT (b): exact confined worker→supervisor result channel | Pinned §S3.3: supervisor-spawned worker (never controller-parented), one status-pipe fd, output confined to the supervisor-private operation directory, supervisor computes the hash itself; controller sees nothing before the post-settlement `PROMOTED` reply |
| Sol R0 / C1 five bullets (supervisor lifetime/restart; closed request/reply protocol + identity; IPC/memory/temp/buffer custody; operation↔lease/meter/charge binding + atomic promotion + one-use delivery + disposal authority; per-cut watchdog behavior) | Pinned respectively in §S1.2/§S1.6; §S2.2–§S2.3; §S2.4/§S3.3; §S3.1/§S3.4–§S3.6; §S1.5 + §S3.6 cut table |
| Codex/Opus C1 (determined portion) and Sol C1 (implementation half) | Carried as §S6 obligations with the topology now fixed |
| Codex/Opus/Sol C2 (boundary not wired; counter-only G7) | §S4 + §S6.1–2 (automatic batch routing; event-backed terminals) |
| Codex/Opus C3, Sol C4 (archival skipped) | §S6.4 (`ARCHIVE` before `RESOLVED`; registry blocks until the staged commit) — implementation-only, per both reviews' answer 3 |
| Codex/Opus C4, Sol C4 (D1 head lag unreachable) | §S6.5 (raw statically parsed ledger suffix; exact bindings; immediate full verification) |
| Codex/Opus/Sol M1 (G5 scope) | §S6.6 ("since last admission"; author-parent verification per Sol M7) |
| M2 (ordinary cuts; close epochs) | §S6.7 (+ §S1.5 pins close in one epoch) |
| M3 (identity/sequence) | §S1.3/§S1.4 topology + §S6.8 (complete-durable-history sequence; kernel start identity) |
| M4 (registry revalidation) | §S6.9 |
| M5 (real CLI) | §S5 exact parsing rule + §S6.11 |
| M6 (unlocked reads/promotion) | §S6.10 (+ §S3.4 settle-and-promote under lock) |
| Sol C3 (stream enumeration `device_units > 1`; mixed streams; forgeable public authority; `bool` charges) | §S4 + §S6.3 + §S6.13 |
| Sol M7 (semantic parent validation) | §S6.6/§S6.9 |
| Codex clarifications 1–3 (review-record heads; caller-supplied current head; archival) | Confirmed verbatim in §S6.12 and the §S6 closing paragraph, exactly as both reviews answered |

## 4. Proof that only the blocked engineering surface changed

The draft replaces exactly **one** signed sentence (v2 §5a "separate
supervisor"), which is the blocked topology itself, and otherwise only
*completes* the sections the reviews named (§1, §2c.1–2c.6, §5b, §9,
§10). Untouched: all nine events, every runtime schema (the claim's
controller/argv keys are *populated*, not changed), every constant,
the batch arithmetic/witness/automaton/D1/override (referenced, §S4),
the recovery/pause/resume protocol, the roots tuple, the T/Q/C
boundaries, and every scientific cell. The six new schemas are
transient/control-plane generic-harness artifacts (the accepted closed
artifact family), not signed runtime schemas, with no result-bearing
field before settlement and no entropy. The five new constants are
engineering control values, not resource or scientific constants.

## 5. Import/allowlist/control-file delta: none — explicit proof

Every primitive the topology uses is a member of a module already in
the pinned `ALLOWED_ABSOLUTE_IMPORTS` (`verification.py:35-39`):
`os` (fork, setsid, pipe2, mkfifo, open with
`O_NONBLOCK/O_CLOEXEC/O_DIRECTORY`, read, write, close, waitpid,
WNOHANG, kill, killpg with integer signals, replace, chmod, readlink,
devnull), `fcntl` (flock), `subprocess`
(Popen with `start_new_session`, `pass_fds`), `time`
(clock_gettime_ns, sleep), plus the already-used `hashlib/json/
pathlib/dataclasses/enum/datetime/re`. The verifier checks top-level
module names, so no delta is needed and none is taken; `socket`,
`select`, `signal`, `sys`, `threading`, and `multiprocessing` are not
used anywhere. `verification.py`, `runtime.py`, `ledger.py`,
`checkpoint.py`, and `activation.py` remain byte-unchanged. A §S7
probe runs the quarantine verifier over the implementation to enforce
this claim mechanically. No new production root, no `scripts/*.py`
entry point, no daemon executable (the supervisor is a double-forked
continuation of the sole root's own image), no dynamic import.

## 6. Cursor handoff

Allowed files (after both X/Y confirmations **and** the §9 token —
not before): `src/philosophia/officina/generic_harness.py`,
`tests/test_officina_generic_harness.py`,
`src/philosophia/officina/accounting.py` (only the already-signed
amendment surface), `tests/test_officina_accounting.py`. Forbidden:
`runtime.py`, `ledger.py`, `checkpoint.py`, `verification.py`,
`activation.py`, `canonical.py`, every `scripts/*.py`, every signed
contract/schema/constant, any new module, entry point, or import, the
production call-graph manifest (remains absent until implementation
review authorizes it), and every runtime artifact (no real claim,
lease, batch, supervisor generation, or promoted object outside
disposable test roots). Ambiguities route back as contract questions;
Cursor retains zero design authority — §S1–§S5 pin the topology,
bytes, timing, and cuts, and §S6 is a closed mechanical list.

## 7. Complete new-test matrix and two-implementer determinacy

The §S7 table is the executable matrix: process-death at every cut;
watchdog firing with no client invocation; PID-reuse/start-identity
probes; framing partial/duplicate/replay/substitution/generation
probes; fd/pipe/memory/filesystem/temp/process-group escape probes;
result-not-settled and wrong-charge probes; promotion/token crash
probes; one- and multi-stream boundary probes; spawn/exit/takeover
probes; the real `python -m` six-command probe; the quarantine-verifier
probe; and every §S6 review-mandated repair test. All run in
disposable roots with test-only processes; none creates a
production-compatible real-T artifact. Determinacy: topology (§S1.1),
spawn/takeover (§S1.2/§S1.6), identity string (§S1.4), watchdog rule
and constants (§S1.5), frame bytes/limits/refusals (§S2.3), descriptor
custody (§S2.4), operation identity (§S3.1), promotion order (§S3.4),
delivery at-most-once (§S3.4), disposal authority (§S3.6), argv rule
(§S5) — each is a single exact rule; two implementers produce the same
process tree, channel bytes, watchdog behavior, promotion visibility,
and crash route.

## 8. Bounded questions

**Opus (two):**
1. Does §S1.5's persistent poll-loop watchdog (with the
   `now + poll ≥ deadline` firing rule) satisfy the signed "at or
   before the deadline" rule in every non-fault execution, and is the
   §S1.5/§S1.6 treatment of supervisor death correctly proved to be
   exactly the signed §4c process-loss route rather than forbidden
   lazy detection?
2. Are the §S3.4/§S3.6 promotion and crash-cut rules single-valued at
   every cut — in particular, is it correct that a charged-but-
   unpromoted operation follows quarantine + §6c in a later
   generation (never late promotion), with no cut exposing a result
   without its own settlement and none charging twice?

**Sol (two):**
1. Is the §S2 channel closed in the Y-line sense — deterministic
   endpoint names with zero entropy, `PIPE_BUF`-atomic single-frame
   requests, strict per-client monotonic replay refusal, generation
   binding by identity-record hash, kernel-start-identity peer
   verification — with no residual field, path, or timing channel that
   carries result-bearing information to the controller before
   settlement?
2. Does §S1.3's spawn-frozen-then-claim ordering, populating the
   signed claim's `controller_pid`/`controller_start_identity`/
   `process_group_id`/`argv` keys with observed values, close Sol
   M3/C1 identity requirements without any schema change, and is the
   stopped-controller window (claim→start) correctly uncharged and
   behavior-incapable?

## 9. Author token candidate and negative authorization

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

Declared **not signable** until both bounded X/Y confirmations accept
this correction. This packet authorizes only that one bounded X/Y
confirmation. It authorizes no implementation or code edit (the four
Cursor files remain uncommitted and unmodified), no commit, no
production call-graph manifest, no supervisor process, control
endpoint, FIFO, operation, promoted object, claim, lease, batch,
capability, world, learner, entropy, device spend, E1/E2/E3 use,
candidate, Q/C object, datum, outcome, or claim movement. T remains
`NOT_ACTIVATED` at genesis (`runtime/` contains only
`T_RUNTIME.lock`); the predecessor line remains immutable, `OPEN`, and
`BLOCKED_LEVEL1_FEASIBILITY`; T and Q remain permanently non-citable
for C1–C6; no prediction is made about any learner or about
Philosophia being proved, falsified, or bounded; the programme claim
remains `OPEN`.
