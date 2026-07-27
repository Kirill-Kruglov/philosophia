# Officina supervisor author selections v1

Selected by Kirill Kruglov on 2026-07-27.

Selection base: commit
`f396d183866234df1ebd9a7b65b4e3cd2a6b2995`.

Governing packet verdict:
`READY_FOR_OFFICINA_SUPERVISOR_AUTHOR_SELECTION`.

## Selected packet

```text
OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1

A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
```

## Selected meanings

- The T-development supervisor remains under one login UID. Its confinement
  claim is procedural against a deliberate same-UID controller and mechanical
  only against accidental path, descriptor, and endpoint misuse. This choice
  is not a confidentiality guarantee for Q or C and cannot be inherited as
  one.
- All eight control commands use a durable, retry-stable, exactly-once-effect
  journal. Identical replies and release-token bytes remain redeliverable until
  a durable acknowledgement records the one-use effect.
- A dedicated watchdog/freezer process may stop controller groups independently
  while the sole supervisor remains the only runtime writer and later performs
  settlement.
- The supervisor has no idle timeout. It persists until a signed terminal,
  pause, blocked, crash/power-loss, or author-stop route applies.

## Authorization boundary

This selection authorizes only preparation of a self-contained v2 supervisor
control-channel draft that embeds the four choices and all already-required
mechanical repairs. It does not accept that future draft and does not make
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` signable.

The v2 draft requires fresh bounded X/Y review before an acceptance token can
be signed. This selection authorizes no implementation, commit of the dirty
Cursor implementation, supervisor/controller/worker process, control endpoint,
journal instance, activation artifact, capability, world, learner, entropy,
E1/E2/E3 spend, Q/C object, datum, outcome, or claim movement. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.

## Governing hashes

```text
14f798efba2fc664632a15477ea38aea1762481486c8f3fe4ea7bcfe9290d189  successor/OFFICINA_SUPERVISOR_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
a7e21dbc1ca225bdcff75ecfffd5c80f7cb1afa366b3944a59c4e9a61d31b88c  reviews/fable_officina_supervisor_author_choice_packet_v1.md
02de5bfdfc0db05b50b7128950ce5a9e1ded5b675a12096765a26ec097231a55  reviews/opus_officina_supervisor_control_channel_v1_confirmation.md
25ab6a8e6247a0261b510762deec486e39f55a5cd06af8518d400b2c250d19d4  reviews/sol_officina_supervisor_control_channel_v1_confirmation.md
```

Saved chat responses are provenance aids. The author-selection tokens and the
formal packet govern.
