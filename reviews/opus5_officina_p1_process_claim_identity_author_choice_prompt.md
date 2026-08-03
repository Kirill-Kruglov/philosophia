# Prompt for Claude Code Opus 5: author the bounded P1 process-claim identity choice packet

You are **Claude Code Opus 5 acting only as the specification author**. You are
not an independent X/Y reviewer and must not choose for Kirill. Work in the
local `philosophia` repository. Read-only file/hash commands are permitted. Do
not edit any existing file, implement code, run tests/probes, or execute any
process-control operation. T remains `NOT_ACTIVATED`; the programme claim
remains `OPEN`.

## Governing block

Read and hash:

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md`;
- `reviews/opus5_officina_supervisor_p1_operative_composite_v1_2_closure.md`;
- the P1 process-authority selection signature;
- the accepted `t-process-claim.v1` schema, activation protocol and
  freeze-evidence predicate;
- all B1/C1/A3/K1/D1 signatures and relevant peer contracts.

The v1.2 author correctly emitted
`BLOCKED_OFFICINA_SUPERVISOR_P1_OPERATIVE_COMPOSITE_V1_2_AUTHOR_CELL` because
the peer layer must write integer `controller_pid` and `process_group_id`, while
the selected nine-opcode P1 protocol exposes no numeric identity to it. Treat
that diagnosis as untrusted and independently re-establish it.

## Required deliverables

Create exactly two files:

1. `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`
2. `reviews/opus5_officina_p1_process_claim_identity_author_choice_packet.md`

Do not modify anything else.

## Choice packet requirements

Present mutually exclusive, mechanically complete choices. At minimum include:

### A — observation-only PCS-attested identity response (recommended unless audit disproves it)

Keep `t-process-claim.v1` and the existing freeze-evidence predicate intact.
Amend the P1 wire so the peer writer can obtain the exact integer
`controller_pid` and `process_group_id` from the PCS **as evidence only**.

Make A bit-exact enough for informed selection:

- which response carries the tuple and on which outcomes;
- exact field order, decimal grammar, bounds, frame-size impact and relationship
  to `handle_id`, `start_identity` and `pgid_is_leader`;
- the PCS proof that both numbers name the same stopped direct child and group
  represented by the opaque handle at that operation;
- whether both numbers are returned only on `STOPPED`, since only that branch
  authorizes a process claim;
- the sole allowed data sink: the two existing claim keys;
- request grammar remains PID-free; no PID may appear in an opcode request,
  handle selection, signal target, journal key, retry key or author decision;
- static/dataflow/runtime tests proving the values cannot flow from a response
  into a later request or process-control primitive;
- replay/B1 treatment: how the identity tuple is durably recorded and replayed
  without becoming a fresh observation;
- PID reuse/start-identity binding and all crash cuts.

State the exact authorial amendment to the signed P1 sentence. It should retain
the safety property at its earned strength, for example:

> The supervisor cannot **address, select, or command** a process by PID and no
> process-control request contains a PID. It may receive a PCS-attested numeric
> PID/PGID tuple only as read-only evidence for the already signed process-claim
> fields; those values have no authorized control-plane sink.

Do not silently declare this equivalent to the old phrase "cannot express a
PID". Name it as a bounded weakening and give it a dedicated token.

### B — identity remains behind the P1 boundary

Keep numeric identity out of the supervisor entirely. Specify a single coherent
replacement, not an open family such as "some means": e.g. a versioned claim
schema using an opaque handle plus a PCS-attested identity-binding artifact,
with exact ownership and verification. Trace every required change to:

- `t-process-claim.v1`/successor schema and all readers;
- freeze-evidence conjunct 7;
- process/lease ids, hashes and activation records;
- batch settlement, generic harness, archive and verification;
- existing evidence compatibility and migration (or explicit no migration).

If B cannot be made single-valued without further author cells, say so and mark
it non-selectable rather than presenting a vague alternative.

### Optional C

Include another option only if it is genuinely distinct, closed and supported
by the signed chain. Do not invent an option merely for symmetry.

## Comparative audit

For every selectable option provide:

- exact signed sentences/contracts amended and untouched;
- authority/confidentiality implications under A3;
- B1 replay and crash semantics;
- code/verifier/test/manifest surface;
- blast radius and rollback/migration cost;
- whether it changes any scientific/resource interpretation;
- concrete counterexample it prevents and new residual risk it creates.

Explicitly answer whether merely observing a PID grants process authority under
this project's **procedural A3 threat model**, as distinct from whether the old
English sentence forbids the observation. Do not confuse OS information,
authorized addressing and same-UID adversarial capability.

Give a recommendation based only on preserving already signed schemas,
minimizing reopened validity predicates and keeping the authority boundary
testable. Do not predict outcomes or optimize toward qualification.

## Tokens and review gate

Give exact mutually exclusive Kirill tokens, but state they are **not signable
until bounded X/Y review confirms the packet**. Suggested neutral token family:

```text
I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY
I_SELECT_P1_PROCESS_CLAIM_IDENTITY_B_OPAQUE_BINDING
```

The closure line 1 must be exactly one of:

```text
READY_FOR_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_XY_REVIEW
BLOCKED_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_PACKET
```

The closure must include the re-derived conflict, option-completeness table,
recommendation, exact future v1.3 handoff for each selection, hashes/custody,
three bounded questions each for X and Y, and confirmation no choice or token
was accepted.

This author round authorizes no selection, X/Y verdict, implementation,
activation, entropy, resource spend, T/Q/C datum, outcome, Proof or claim
movement.
