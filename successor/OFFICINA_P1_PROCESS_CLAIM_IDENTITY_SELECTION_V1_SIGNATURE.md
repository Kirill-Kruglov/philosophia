# Officina P1 process-claim identity selection v1

Selected by Kirill Kruglov on 2026-08-04.

Selection base: commit
`00c58808e3652f0f7b9e789a80b6607d98194243`.

Governing independent X-line verdict:
`OFFICINA_P1_IDENTITY_V2_4_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION`.

Governing independent Y-line verdict:
`OFFICINA_P1_IDENTITY_V2_4_YLINE_CONFIRMED_FOR_AUTHOR_SELECTION`.

## Selected token

```text
I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY
```

## Selected meaning

- The P1 Process-Control Server may return the PCS-attested `attested_pid` and
  `attested_pgid` pair only in the signed `AWAIT_STOP` / `STOPPED` response.
  The tuple is an observation of the stopped, unreaped direct child and its
  process group; it is not a process capability.
- The opaque `handle_id` remains the only addressable process name. The two
  integers may not select, signal, wait for, route to, allocate resources to,
  or otherwise control a process.
- The immediate and persistent uses of both identity fields are limited by the
  v2.4 closed occurrence, carrier, mapping, consumer and destination rules.
  Both identity-bearing durable families, `T_PROCESS_CLAIMS` and
  `T_ACTIVE_LEASES`, are governed symmetrically.
- External filesystem aliasing is not claimed impossible. Symlink, hard-link,
  descriptor-alias and copied-byte consequences are contained by the signed
  descriptor/path/schema gate and dominant invalidity before ordinary value
  binding.
- The third evaluation `EV-3` is a whole-lease integrity evaluation only. It
  adds no persistent identity destination and does not change `D-1`, `D-2` or
  `L-1` through `L-5`.
- This cell supplies no confidentiality guarantee. The bounded identity search
  claim applies only when the other eighteen canonical claim fields are known;
  no recoverability or entropy claim is made without those conditioning
  fields.
- Identity fields, their carriers and their integrity values remain
  control-plane facts. They are not scientific data, evidence, endpoints,
  qualification inputs, Q/C facts, outcomes or Proof.

Option B, `I_SELECT_P1_PROCESS_CLAIM_IDENTITY_B_OPAQUE_BINDING`, is not
selected.

## Outstanding gates

This selection does **not** sign or authorize the separately named token:

```text
P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1
```

The governing packet requires that bounded weakening to be reviewed and
accepted separately before Option A can become operative. The watchdog-freeze
author cell also remains unresolved. Therefore this identity selection may be
bound into the next reviewed specification, but it does not yet authorize an
operative P1 composite.

## Authorization boundary

This signature authorizes only recording Option A as the selected identity
architecture and preparing the bounded documentation needed to bind that
selection with the future watchdog choice.

It authorizes no implementation, verifier or manifest edit, key generation,
authorization artifact, install record, T activation, process/socket/pipe/
signal operation, learner, world, entropy, E1/E2/E3 spend, Q/C object, datum,
outcome, Proof or programme-claim movement.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
P1 WATCHDOG-FREEZE CELL = NOT SELECTED
```

## Governing hashes

```text
bef7012a5fce59857372755c23f6da87d1d1045f7d62d8945914cb60d9c48fda  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_4_CORRECTION.md
5ac5fbc31faa565d44729bf814726e97e491fcfa5acf70ffa55fd4373eddf4f3  reviews/opus5_officina_p1_process_claim_identity_choice_v2_4_closure.md
f60f520b1b4683add40b82150e13a83e092b4a0bc88a2af5ee66fe482a879f74  reviews/fable_officina_p1_identity_v2_4_independent_x_confirmation.md
87aa3cb4b8715d3720557bfdce1c19f9dab3fc00e9d868f547d166e4cd02d9ff  reviews/sol_officina_p1_identity_v2_4_bounded_y_confirmation.md
```

The exact selected token and this formal signature govern. Saved chat
responses are provenance aids only.
