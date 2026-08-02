# X-line prompt: final independent engineering review of the Officina P1 supervisor composite

You are **Claude Code Opus 4.8/5 acting only as the independent X-line
reviewer**. You did not author this review layer. Work in the local
`philosophia` repository. Do not modify any existing file, implement code, run
tests or probes, or execute any process/socket/pipe/fork/exec/signal/wait/prctl
operation. T remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.

## Identical review bytes

Review the committed composite at current `HEAD`, beginning with:

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_7_PRE_XY_CONSISTENCY_REPAIR.md`
  - expected SHA-256:
    `66dc6fdc26d8b27f50e8de9603e8ac217492a13385c04822a1450a938495d51a`
- `reviews/opus5_officina_supervisor_control_channel_v2_1_10_7_pre_xy_consistency_closure.md`
  - expected SHA-256:
    `02d13b9d8a6b34fd1d53a98de6e17ef9eeb8efb67f7f2981ba9c7bf51ada32a9`

Recompute both hashes. Read the **entire carried chain**, not only 10.7:
v2.1 through v2.1.10.7, every replacement index they incorporate, the signed
A3/B1/C1/D1/K1 selections, output-capacity K1, P1 process-authority selection,
the generic-harness and batch-settlement contracts, and the current frozen
implementation/verifier surfaces. Treat every author closure and verdict as an
untrusted claim.

## Review task

Attack the P1 composite as an executable Linux process-control specification.
Do not merely confirm that 10.7 copied its mandate. Try to construct a concrete
interleaving, descriptor state, process tree, crash cut, parser exception,
subreaper configuration, PID reuse, signal/wait race, or verifier escape that
causes any of:

- a wrong-PID or non-owned process action;
- a false-positive death proof or removal of a record naming a possibly-live
  process;
- an fd capability reaching an unauthorized process or surviving an invalid
  receive path;
- two actors believing they own the same handle/lease/generation;
- a replayed or inconclusive PCS operation becoming a valid one;
- a watchdog being signalled despite the signed no-signal route;
- `SPAWN.lock` leaking through a controller/worker/watchdog exec or failing to
  survive the middle→grandchild→supervisor route;
- an adopter's wait status, signal interference or liveness stall being consumed
  as a valid Officina decision;
- implementation ambiguity between two reasonable implementers;
- a static verifier/test obligation that contradicts another required path.

At minimum independently trace:

1. caller → PCS → `pid_mid` → supervisor, and PCS → controller/worker/watchdog;
2. all `fork`, `execve`, `posix_spawn`, `DUP2`, `CLOSE`, `FD_CLOEXEC` and
   `/proc/self/fd` phases, including `P-f`, `A-5`, `G-1`…`G-6` and `S-18'`;
3. every `SCM_RIGHTS` send/receive/ACK/replay/truncation/exception path and the
   non-aborting ancillary parser;
4. child-subreaper adoption for caller and an arbitrary higher ancestor,
   wildcard waits, A3 interference, proof availability versus false-positive
   safety, and `AWAIT_STOP` non-interception;
5. supervisor, PCS, watchdog and role death; PCS loss; shutdown; PID reuse;
6. journal state, handle state and every crash cut before/after durable writes;
7. the exact production roots/import allowlists, AST rules S-1'…S-28, hashes,
   verifier rows and test matrix for implementability.

Verify relevant Linux interface facts from primary local/system documentation
or the interface definitions themselves; do not accept author prose as the
source. Do not execute a probe.

## Deliverable

Create exactly one new file:

`reviews/opus_officina_supervisor_p1_final_xy_review.md`

Do not edit anything else. Put findings first, ordered Critical/Major/Minor,
with exact file/section references and concrete counterexamples. Answer:

1. Is the full P1 composite mechanically single-valued and implementable?
2. Are F1–F5 genuinely preserved through 10.6/10.7?
3. Are the subreaper and A3 safety/liveness claims exact?
4. Can the verifier/test surface distinguish a shape-correct but
   authority-wrong implementation?
5. What exact implementation scope is authorized if confirmed?

Verdict line 1 must be exactly one of:

```text
OFFICINA_SUPERVISOR_P1_XLINE_CONFIRMED_FOR_IMPLEMENTATION
REVISE_OFFICINA_SUPERVISOR_P1_COMPOSITE
BLOCKED_OFFICINA_SUPERVISOR_P1_COMPOSITE
```

Use `CONFIRMED` only if no Critical/Major defect remains and no new author
choice is required. A confirmed verdict authorizes only Codex/Cursor to prepare
an implementation and tests for later review. It authorizes no code execution,
T activation, entropy, E1/E2/E3 spend, T/Q/C datum, outcome, Proof or claim
movement.
