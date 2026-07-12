# Level 0: platform replication

Status: companion-fidelity v2 is implemented, accepted by Opus, and certified by a
matching bounded determinism-prefix report. Reconstruction fidelity is closed;
a draft scientific preregistration, schema-2 lock machinery, outcome driver,
and independent decision verifier are implemented but not yet accepted. The
design is not locked, and full training and scientific outcome runs remain
forbidden pending adversarial review and Kirill's signature.

The only scientific task at this level is to reproduce published modular-addition
grokking with checkpoints, representation probes, and seeded replications. It is
not evidence for the Philosophia thesis.

Before locking, establish a canonical CPU path and evaluate any accelerated
backend separately. Record environment, determinism limits, wall time, memory,
checkpoint schema, and the bounded platform-repair policy.

Execution capabilities and contamination guards are defined in
`EXECUTION_INTERLOCK.md`.

The single authorized non-outcome CPU resource scout is recorded in
`scout/timing-storage-scout_non-outcome.json`; planning-only derivations are in
`RESOURCE_SCOUT.md`. Its resource measurements remain applicable to v2, while
its v1 deterministic prefix is superseded.

Opus selected `REVISE_TO_COMPANION`. The binding implementation specification is
`COMPANION_CONFIG_TRACE.md`, the adopted choices are in
`RECONSTRUCTION_CHOICES_V2.md`, and v1 choices are historical. The proposed
scientific cells are in `PREREGISTRATION_DRAFT.md` and `SCIENTIFIC_SPEC.json`.
No `PREREG.lock`, outcome directory, or Philosophia `decision.json` exists.
