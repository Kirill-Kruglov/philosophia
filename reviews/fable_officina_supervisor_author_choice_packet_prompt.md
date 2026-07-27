# Fable 5 task: Officina supervisor bounded author-choice packet

Work in `/home/master/llm_projects/philosophia`.

Write exactly two new files:

```text
successor/OFFICINA_SUPERVISOR_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
reviews/fable_officina_supervisor_author_choice_packet_v1.md
```

Do not edit v1, code, tests, signatures, runtime artifacts, or existing reviews.
Do not commit. Do not start any supervisor/controller/worker, create entropy,
activate T, create a manifest, or spend a resource.

## Inputs

Read:

```text
successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md
reviews/fable_officina_supervisor_control_channel_v1_closure.md
reviews/opus_officina_supervisor_control_channel_v1_confirmation.md
reviews/sol_officina_supervisor_control_channel_v1_confirmation.md
reviews/codex_officina_generic_harness_implementation_review.md
successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
```

Review evidence commit:

```text
913dc69
```

The converged verdict is `REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V1`.
The existing author token is not signable.

## Goal

Produce a short, bounded author-choice packet for only the choices that cannot
be selected mechanically. Do not write the v2 correction yet. After Kirill
selects exact tokens, a separate task will apply those selections together with
all mechanical F3-F15/Sol repairs into one self-contained v2 draft.

For every choice:

- give 2-3 mutually exclusive executable options;
- name the exact guarantee, residual risk, deployment cost, and effect on the
  signed threat model;
- identify any required import/allowlist/frozen-file delta;
- recommend one option on engineering and epistemic grounds, not convenience
  alone;
- provide one exact selection token per option;
- do not silently combine choices.

## Choice A: result confinement and endpoint roles

The v1 same-UID `0700/0000` path is rejected. Present executable alternatives
that make the promised boundary honest.

At minimum compare:

1. **Kernel-enforced compartment while retaining one login account**, for
   example anonymous worker-to-supervisor pipes plus supervisor-only memory or
   unnamed files, verified `/proc`/ptrace restrictions, endpoint-role binding,
   and no named pre-settlement output. State exactly which kernel property
   prevents the controller from reading supervisor/worker FDs or memory.
2. **Separate OS credential/namespace/service boundary**, naming the deployment
   prerequisite and how the current user launches it without granting the
   controller the supervisor credential.
3. **Explicit same-UID procedural re-scope**, honestly weakening §5b to
   contract-following/accidental controllers and treating deliberate same-UID
   inspection as procedural residual.

Do not recommend option 1 unless it is mechanically enforceable on the current
Linux platform and reproducibly preflightable. A deterministic path, mode bits,
or "no path grant" is not isolation. Consider large checkpoint output: memory
only may be insufficient, so specify unnamed streaming storage or a size-bound
route.

The selected option must also close endpoint roles: CLI commands only from the
CLI endpoint and controller operations only from the bound inherited channel;
workers have no control endpoint.

## Choice B: durable idempotency and release delivery

Choose the semantic policy; byte details will be mechanical in v2.

Options must state:

- whether all eight commands or only a subset use a retry-stable idempotency
  key;
- whether the request/reply journal survives supervisor generations;
- reuse-with-different-bytes invalidity;
- committed-but-lost reply behavior;
- `OPERATION_ADMIT` retry behavior without a second worker or new meter cursor;
- promoted-token delivery and acknowledgement semantics.

Compare at least:

1. durable exactly-once-effect journal for all eight commands, with repeatable
   identical reply until durable acknowledgement/redemption;
2. durable exactly-once-effect journal plus explicitly fail-closed at-most-once
   release delivery to a named recovery destination.

No option may permit blind re-execution after timeout.

## Choice C: watchdog topology

The serial-loop 100 ms promise is false during blocking work. Compare:

1. a dedicated per-lease or singleton watchdog/freezer process that can
   independently stop the controller group at/before deadline, while the sole
   supervisor later performs locked settlement;
2. a topology that quiesces and conservatively settles all live liabilities
   before any potentially blocking operation, with an exact bounded event loop.

State parentage, capability/lock custody, supervisor death, watchdog death,
handoff, and why no deadline can pass with behavior still running. Recommend one
route. The watchdog must not become a second runtime writer.

## Choice D: idle supervisor lifetime

Compare:

1. remove idle exit; supervisor persists until pause, terminal state, power
   loss, or signed author stop;
2. retain idle exit only with a fully specified durable drain protocol and
   request-journal handoff.

Recommend the smaller state space unless there is a concrete resource reason
otherwise.

## Mechanical repairs (not author choices)

List, but do not turn into options, every converged mechanical repair:

- race-free self-stop-before-exec/controller bootstrap;
- discoverable pre-claim spawn intent/child registry and automatic takeover;
- singleton spawn lock through verified identity installation;
- own-child vs reparented-zombie handling;
- exact pre-claim log location;
- exact per-command request and per-status reply schemas;
- exact identity-to-path encoding and FIFO open/PIPE_BUF/partial/EAGAIN rules;
- endpoint role checks;
- safe output grammar, bounds, descriptor/no-follow hashing, whole-directory
  atomic promotion;
- one promotion commit point;
- stream ownership/subset table;
- archival exclusions;
- operation subset settlement;
- all §S6 repairs carried unchanged.

Flag any numeric output bound or journal retention bound that is genuinely an
additional author choice. Prefer a formula from existing signed resource caps
over inventing a tunable number.

## Read-only platform audit

You may inspect current platform facts without starting a process or changing
state, including:

```text
/proc/sys/kernel/yama/ptrace_scope
/proc/mounts
Python/os support for pipe2, O_TMPFILE, memfd_create, pidfd_open
available system service/user-namespace primitives
```

Record what was observed and distinguish a current-platform fact from a
portable contract guarantee.

## Deliverables

The choice packet must contain:

1. exact A-D option tables;
2. recommendations with reasoning;
3. exact selection tokens;
4. a consolidated response template;
5. the mechanical-repair ledger;
6. what a later v2 correction must supersede;
7. negative authorization.

The review memo must verify that choices are mutually exclusive and sufficient,
ask at most two sharp questions each for later Opus/Sol review, and state that
no existing token is signable yet.

First line of the review memo:

```text
READY_FOR_OFFICINA_SUPERVISOR_AUTHOR_SELECTION
```

Use `BLOCKED_OFFICINA_SUPERVISOR_AUTHOR_SELECTION` instead if no executable
choice can meet the signed boundary on the present platform.
