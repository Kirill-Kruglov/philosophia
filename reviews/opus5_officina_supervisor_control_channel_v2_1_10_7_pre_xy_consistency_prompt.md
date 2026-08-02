# Prompt for Claude Code Opus 5: close the final P1 subreaper consistency defect

You are **Claude Code Opus 5 acting only as the specification author**. You are
not an independent X-line or Y-line reviewer. Work in the local `philosophia`
repository. Do not edit any existing file. Do not implement code, run tests or
probes, execute any process/socket/pipe/fork/exec/signal/wait/prctl operation,
or move any T/Q/C state. T remains `NOT_ACTIVATED`; the programme claim remains
`OPEN`.

## Governing layer

Read in full and recompute the hashes of:

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_6_PRE_XY_REPAIR.md`
- `reviews/opus5_officina_supervisor_control_channel_v2_1_10_6_pre_xy_repair_closure.md`
- their complete carried P1 chain and signed P1 selection.

Treat the 10.6 verdict as untrusted author self-assessment. Preserve its valid
closures: exact child-subreaper-or-namespace-init adoption, the reliance audit,
the phase-scoped `S-18'`, and all v2.1.10.5 F1--F5 closures. Do not reopen P1,
A3/B1/C1/D1/K1, the process topology, or any prior author selection.

## Confirmed internal inconsistency

10.6 correctly says that a contaminated caller or higher ancestor may already
be a child subreaper and may therefore adopt and wildcard-reap the supervisor
after `m9`, and may adopt/reap `pid_mid` and roles after PCS death. But its own
parent/reaper/authority table says:

```text
caller ... Direct children: the PCS ... May wait on: the PCS only
```

Those statements cannot both govern. Three adjacent claims also overstate what
the accepted A3 procedural model supports:

1. adopted wait-status values are said to come from the closed small set
   `{0, 3, named PCS exit tokens}`; under A3, a same-UID ancestor may terminate
   an adopted process with other signals, so the observed status need not be in
   that set;
2. the ancestor is said to be unable to "forge or block a death proof", while
   the same table admits it may stop an adopted live process; it can therefore
   delay/prevent death and channel EOF indefinitely, although it cannot make a
   live process satisfy the object-bound positive death predicate;
3. "cannot gain Officina process authority" risks conflating authorization
   with kernel power: adoption grants parent/reaper status, and same-UID A3
   already permits signal interference. What remains true is narrower: the
   actor receives no Officina handle/descriptor, is never an authorized
   control-plane participant, and cannot turn interference into a valid
   Officina decision or scientific/resource outcome.

## Required bounded repair

Create exactly two new files:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_7_PRE_XY_CONSISTENCY_REPAIR.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_10_7_pre_xy_consistency_closure.md`

Do not modify any existing file.

The correction must:

1. Replace the 10.6 caller/ancestor table with a temporally explicit table:
   initial direct children and wait-set versus possible dynamically adopted
   orphans when that process is the nearest living child subreaper. Cover the
   caller and an arbitrary higher ancestor, not only namespace init.
2. State that wildcard waits of the adopter range over those adopted direct
   children. Preserve the fact that this cannot intercept `AWAIT_STOP` while
   PCS custody is live, because its target remains a non-orphan direct PCS
   child.
3. Withdraw the closed wait-status set. Treat an adopter-observed status as an
   untrusted OS fact that may reflect A3 interference, carries no authorized
   programme meaning, and is never consumed by an Officina decision.
4. Replace "cannot forge or block a death proof" with the exact distinction:
   the adopter cannot create a **false-positive** object-bound death proof for
   a live process; it may prevent progress, delay/avoid death, keep a channel
   open by stopping a process, or otherwise block proof availability. Those are
   A3 liveness/interference effects and must fail closed, never become a valid
   status, outcome, resource datum or scientific evidence.
5. Replace any ambiguous "cannot gain process authority" claim with the
   authorization distinction: kernel parent/reaper/same-UID interference is
   admitted; no Officina descriptor/handle/opcode/journal authority is
   conferred, and no interference is accepted as an Officina decision.
6. Recompute the 10.6 R1.3 disposition, parent/reaper/authority table, crash
   language, weakest-points section, tests and verifier rules. Add mechanical
   guards against reintroducing `PCS only`, the closed-status-set claim, or
   `cannot block` wording in the adopter context.
7. Preserve 10.6's reliance result only at its earned strength: no valid
   Officina decision consumes an orphan's wait status. Do not claim liveness,
   confinement, or uninterruptible death-proof availability.
8. Preserve `S-18'`, P-f/A-5/G-5 permissions, F1--F5, the P1 topology, and all
   signed cells byte-semantically unchanged.

If this correction changes process topology, adds a syscall/import/process,
or needs a new author choice, stop with an exact `BLOCKED_...` verdict. Do not
choose a repair for Kirill.

## Verdict and handoff

If and only if the inconsistency is closed without reopening architecture,
closure line 1 must be exactly:

```text
READY_FOR_OFFICINA_SUPERVISOR_P1_FINAL_XY_REVIEW
```

The closure must contain:

- an exact replacement index over 10.6;
- one-to-one disposition of all eight requirements above;
- corrected dynamic parent/adopter/wait/authority table;
- exact safety-versus-liveness statement under A3;
- no-regression table for 10.6 R2, v2.1.10.5 F1--F5 and signed cells;
- exact future implementation/verifier/test surface;
- byte/hash custody and confirmation existing files were untouched;
- three bounded questions each for independent X=Claude Code Opus 4.8/5 and
  Y=GPT-5.6 Sol, reviewing identical bytes;
- explicit confirmation that no acceptance token is available from this author
  round.

This author round authorizes no X/Y verdict, implementation, code/test edit,
verifier/manifest change, process or probe, T activation, entropy, E1/E2/E3
spend, Q/C work, datum, outcome, Proof, or claim movement.
