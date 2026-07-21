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
- a direct-symbol production lint; activation additionally requires the absent
  reviewed generic harness and a canonical closed production call-graph manifest.
  The complete functional E1 boundary is not claimed until that separate package
  and its supervisor/backend paths pass bounded review;
- mutually exclusive inactive and active verifiers.

The exact-type real-T capability has no issuer. Actual activation remains
mechanically blocked until a separately reviewed generic metered learner
harness is present in the reviewed source set and an exact author-signed
activation authorization is committed at HEAD.

The process objects in `runtime.py` are pure constructors and validators, not
completed runtime transactions. This package does not implement process start
or lease installation, watchdog supervision, heartbeat archival, deadline
revocation, process-loss/backend reconciliation, conservative unknown-interval
charge, E1 exhaustion, E3 review, voluntary close, author stop, or transaction
commits. Those routes belong to the separately reviewed generic harness. Their
enums and schemas confer no execution authority and are not evidence that a
terminal branch has run.
