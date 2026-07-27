# Officina supervisor output-capacity selection v1

Selected by Kirill Kruglov on 2026-07-27.

Selection base: commit
`9142d0d6ecd3400daf0a23de41e256fc59abcb0f`.

Governing packet verdict:
`READY_FOR_OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_SELECTION`.

## Selected token

```text
OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_SELECTION_V1

K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

## Selected envelope and provider

- Worker output is supervisor-mediated. A contract-following worker receives
  no writable output pathname or file descriptor and sends bounded framed
  bytes through an inherited pipe. The supervisor writes and hashes each byte
  once and closes the transport at the frozen ceiling.
- `T_OUTPUT_PER_STREAM_MAX_BYTES = 67_108_864` (64 MiB).
- Per-operation capacity is that value times the number of declared stream
  indexes, at most `268_435_456` bytes (256 MiB).
- `T_OUTPUT_AGGREGATE_MAX_BYTES = 34_359_738_368` (32 GiB) across the complete
  T custody set.
- `T_OUTPUT_FS_SAFETY_MARGIN_BYTES = 8_589_934_592` (8 GiB).
- `T_OUTPUT_COPY_CHUNK_BYTES = 4_194_304` (4 MiB).
- Aggregate custody includes live reservations, pending settlement,
  quarantine, and retained `runtime/T_PROMOTED/**`. Rename, promotion,
  settlement, and failure do not replenish capacity.
- Capacity is released only after an authorized disposition proves custody
  absent. Outputs otherwise remain retained for all of T.
- The A3 same-UID residual remains procedural against deliberate processes and
  is not Q/C-citable.

## Authorization boundary

This selection authorizes only a later bounded v2.1 supervisor/control-channel
correction that embeds K1 and applies the already-reviewed mechanical repairs.
It does not accept that correction and does not make
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` signable.

The corrected contract requires fresh bounded X/Y confirmation. This selection
authorizes no code or test edit, host change, supervisor/controller/worker,
pipe/FIFO/journal/capacity artifact, activation, capability, world, learner,
entropy, E1/E2/E3 spend, Q/C object, datum, outcome, or claim movement. T
remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.

## Governing hashes

```text
9db9f263ebcf705c2e8b5486bc6673104f94f6d8b59fd764e92bd946e5245168  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
9e3871a0287982efd94f48ca3428606143c69728020a5920a0710b6e38ca3bac  reviews/fable_officina_supervisor_output_capacity_author_choice_packet_v1.md
bc731d96d13c8bc6741a94d320ed51ae35cfcbdc38417fedee3ddf3684cec9b2  reviews/opus_officina_supervisor_control_channel_v2_review.md
edfbef915246080a6e022ec5e95e177603c83e542f4068dc1f3ad8d367fcf591  reviews/sol_officina_supervisor_control_channel_v2_review.md
```

The selected token, exact packet envelope, and formal X/Y reviews govern.
