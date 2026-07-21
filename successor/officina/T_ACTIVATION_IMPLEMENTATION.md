# Officina T activation implementation

Status: `IMPLEMENTED_INACTIVE_AWAITING_XY_REVIEW`.

This package implements the signed T activation and metered-runtime control
surface without activating it. The real tree remains at pristine genesis:
there is no activation authorization, claim, state, record, process, lease,
real T world, learner, candidate, entropy draw, or E1/E2/E3 charge.

Implemented boundaries:

- canonical activation authorization, claim, active-envelope, state, and record
  validation;
- an atomic, exact-stage activation transaction exercised only in disposable
  git mirrors;
- a tracked immutable `T_RUNTIME.lock` with held-descriptor locking;
- the closed nine-event vocabulary and active-state re-derivation from the
  hash-linked ledger;
- fixed liability constants, shortened E1/E3 reservation arithmetic,
  monotonic additive settlement, typed invalidity and process dispositions;
- a static production boundary that rejects test-world capability symbols;
- mutually exclusive inactive and active verifiers.

The exact-type real-T capability has no issuer. Actual activation remains
mechanically blocked until a separately reviewed generic metered learner
harness is present in the reviewed source set and an exact author-signed
activation authorization is committed at HEAD.
