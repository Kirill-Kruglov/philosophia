# Officina T activation protocol v2.1 correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`.

V1 as corrected by v2 carries forward except for the exact replacements below.
This file closes the five Sol v2 findings and the three non-blocking Opus wording
notes. It changes no scientific cell, envelope numeric, or phase boundary.

## 1. Enforced liability and quiescence

This replaces v2 section D's watchdog/process-loss paragraph.

The liability interval is an enforced maximum of behavior-capable execution,
not a heartbeat target. Every controller tree runs under a separate supervisor
that owns its process group and real-T capability. At or before the recorded
deadline the supervisor must:

1. revoke oracle, learner-update, checkpoint, and output authority;
2. freeze or terminate every behavior-capable member of the declared group;
3. synchronize the selected CPU/off-CPU backend so previously submitted work is
   complete or cancelled;
4. prove quiescence from the process-group membership, process states, backend
   synchronization result, monotonic reading, and unchanged boot identity;
5. durably settle actual E1 through that quiescence reading before any result,
   checkpoint, close, recovery, or new work is admitted.

Capability refusal alone is not quiescence. If timely quiescence is proven, the
lease liability remains an upper bound. If quiescence is later but its monotonic
time is known, recovery charges the full actual interval through verified
quiescence. If the interval or backend cessation is unknowable, recovery
conservatively consumes all remaining E1 that was lease-eligible at the last
durable cursor. No work or recovery resumes until the charge and invalidity route
are durable. The aggregate 240-device-second bound may be asserted only when all
four live trees have timely quiescence proofs; otherwise the conservative rule
governs and the bound is not claimed.

The inactive generic harness implementation must test controllers and children
that ignore heartbeat, retain a T response, continue computation, resist normal
termination, and cross the deadline. A backend without a reviewed, testable
quiescence/synchronization adapter is ineligible for activation.

## 2. Behavior-capable concurrency unit

This replaces v2's one-unit process-tree paragraph.

One device-unit admits exactly one concurrent behavior-capable execution stream.
Children may perform behavior-inert orchestration, storage, and communication
under that unit. A child that independently queries a T world, evaluates or
trains a learner, performs a behavior-relevant update, or creates a
behavior-bearing checkpoint is another stream and requires its own liability
and concurrent slot.

A declared multi-stream controller consumes one unit per simultaneous
behavior-capable stream. Total live units remain capped at four. Process-group
membership never collapses multiple streams into one unit. Every supervisor
reconciles declared streams against observed active workers and backend queues at
each admission, heartbeat, and quiescence proof; excess or unclassifiable
parallelism revokes the group and invokes the unknown-interval conservative
charge.

## 3. Learner behavior is not infrastructure invalidity

Remove `NONFINITE_DEVELOPMENT` from the public invalid-cause enum. The exact
public invalid causes remain `PROCESS`, `RESOURCE`, `HASH`, `CLOCK`, and
`FILESYSTEM`.

Learner exception or non-finiteness is quarantined adaptive T information.
Public closure uses `T_PROCESS_VOLUNTARY_STOP` after full E1 settlement, with no
learner-behavior cause or metric. It is not runtime invalidity, censoring,
competence failure, or learner impossibility and invokes no infrastructure
recovery. Detailed learner behavior remains only in the dev-non-citable
quarantine and is unavailable to recovery, E3, breathing, Q numerics, and C.

## 4. Total reservation boundary

This replaces the fixed-size refusal paragraph in v2 section D.

For a requested unit, final liability is:

```text
min(60 device-seconds,
    positive E1 device-time remaining after other live liabilities,
    positive E3-device time remaining after other live liabilities)
```

Its watchdog deadline is shortened to that exact positive liability. Zero E1
liability appends the actual `T_ENVELOPE_EXHAUSTED` state. Zero E3-device
liability routes to the nonterminal E3-due gate. Reservation refusal alone never
sets exhaustion, completes an early review, or silently strands a remainder.
The final shorter interval is an engineering consequence of the signed boundary,
not a new numeric or result-dependent choice.

If both boundaries are zero simultaneously, exhaustion is recorded first and E3
is preserved as due in the post-state; neither route resets the other clock.

## 5. Immutable runtime lock

`successor/officina/runtime/T_RUNTIME.lock` is a tracked, immutable,
non-state-bearing infrastructure file created only by the reviewed inactive
implementation. Its canonical contents are the ASCII line:

```text
OFFICINA_T_RUNTIME_LOCK_V1
```

Its path and SHA-256 are present in authorization `canonical_paths` as
`runtime_lock`, and in the activation claim/record immutable-control maps. It is
permitted by pristine preflight, is not an activation output, never enters a
transaction staged set, and is never deleted, replaced, truncated, or written.
Every activation/runtime read opens it `O_RDWR|O_CLOEXEC|O_NOFOLLOW`, validates
canonical path/content/held descriptor identity, then obtains `flock(LOCK_EX)`.

V1's absent-output check applies only to activation claim/state/record and
process artifacts, not to this pre-existing reviewed lock.

## 6. Closed event vocabulary and invalidity authority

The complete post-activation production ledger-event vocabulary is exactly:

```text
T_ACTIVATED
T_PROCESS_STARTED
T_DEVICE_TIME_CHARGED
T_REVIEW_COMPLETED
T_OPERATIONAL_PAUSE
T_PROCESS_STOPPED
T_RUNTIME_INVALID
T_AUTHOR_STOP
T_ENVELOPE_EXHAUSTED
```

No tenth event exists. Clock failure uses `T_RUNTIME_INVALID` with
`invalid_cause=CLOCK`; `T_INVALID_CLOCK` is not an event.

Every invalidity requires both artifacts. First the detailed canonical
`philosophia.officina.t-runtime-invalidity.v1` record is durably created. Then
the state-bearing `T_RUNTIME_INVALID` ledger event commits its hash, typed public
cause, full post-state, and required action. The ledger event is authority that
the runtime entered fail-closed invalidity; the hash-bound record is authority
for its detailed recovery inputs. Missing, extra, mismatched, or reversed-order
artifacts are themselves unrecoverable without signed bounded disposition.

Pre-activation `T_NOT_ACTIVATED_AT_MAINTENANCE`, if separately authorized before
activation, is outside this post-activation vocabulary and cannot appear after
`T_ACTIVATED`.

## 7. Gate

No new author choice is required for inactive implementation. A positive final
confirmation authorizes only the implementation surface already listed in v2:
disposable-mirror activation/runtime primitives and tests. Actual activation
remains blocked until the generic metered harness, including supervisor,
process-tree, backend-quiescence, watchdog, oracle, update, checkpoint, and
test-surface call graphs, receives separate bounded X/Y review.

No authorization record, runtime state, process, world, learner, candidate,
entropy, Q/C object, or spend is created by this correction. T remains
`NOT_ACTIVATED` and the programme claim remains `OPEN`.
