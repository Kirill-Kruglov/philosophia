# Officina generic metered harness contract — v2.3.1 bounded correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`. Carries
the complete harness contract — v2 as corrected by v2.1, v2.2, and
v2.3 — forward verbatim except for the harness-side consequences of
the two author decisions applied in the companion
`successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md`.
No F1..F4/R1..R4 closure is reopened. Creates nothing executable;
changes no code; prior versions preserved unedited as review evidence;
T remains `NOT_ACTIVATED`.

**Replacement index (everything else in v2/v2.1/v2.2/v2.3 carries forward):**

| v2.3 locus | Action |
|---|---|
| §H3 (claim-authorized head/cache completion) and its compatibility-table row under "deterministic harness clarifications" | **replaced** by §J1: the rule is amendment §D1's, applied by reference, and is classified as **amendment-authorized control behavior** under token 1 — not a harness clarification, not a silent repair |
| §H4.1 ("meter-evidence hash … `t-meter-evidence.v1`"), the §H2.3 "evidence-proved intervals" parenthesis, and every §H5 probe naming evidence artifacts/hashes | **replaced** by §J2/§J3: inline `meter_evidence` objects; no evidence family, path, orphan state, or archive item exists |

## J1. Head/cache completion (by reference; classification corrected)

Within exactly one unresolved, fully re-validated batch claim, a
ledger suffix that byte-matches the next canonical automaton prefix
and lags **only** in the external head and/or state cache is completed
idempotently under the reconstructed authority, per amendment §D1's
six mandatory preconditions (single claim; exact byte-match scan with
no extra entry, missing dependency, competing claim/override,
path/hash/lease discrepancy, or ambiguous state; at most the one
just-appended state-bearing entry; old/new head+state bindings;
completion followed immediately by full verification; any second
discrepancy → inherited record-first invalidity/recovery). Outside
unresolved batch claims, the v2 §3a sole-completion boundary and the
v2.1 C.4 head-behind rule are **unchanged**. This behavior is covered
by `I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT`, not by the
harness token.

## J2. Inline meter evidence references

Every reference to a meter-evidence hash, `t-meter-evidence.v1`, or
`T_METER_EVIDENCE/` is replaced: each claim stream entry carries one
nested `meter_evidence` object with keys exactly
`{clock_kind, boot_identity, adapter_identity,
interval_start_reading_ns, interval_end_reading_ns,
backend_synchronized, observed_utc}` per amendment §D2. The claim hash
directly binds every meter fact; known charges recompute inline as
`end − start`; no pre-claim evidence file, orphan-evidence state,
evidence crash cut, or evidence archive obligation exists. The signed
four-stream concurrency cap (`MAX_CONCURRENT_LEASES = 4`) bounds every
claim at four stream entries, which is why inlining keeps the claim
bounded — an engineering restatement of a signed constant, not a
choice.

Worked-ledger reading (all §H2 integers unchanged): each example's
`LATE_KNOWN`/`TIMELY_KNOWN` charge is now witnessed by its stream
entry's inline interval facts. Illustration for §H2.3 (60/60/60), P1's
stream entry: `classification = LATE_KNOWN`, `known_charge_ns = 60`,
`meter_evidence.interval_end_reading_ns −
meter_evidence.interval_start_reading_ns = 60`,
`backend_synchronized = true`, `interval_end_reading_ns >` the lease's
`heartbeat_deadline_ns` (late), `boot_identity` = the lease's. The
`UNKNOWABLE` entries of §H2.1/2/4/5/6 carry
`interval_end_reading_ns = null`, `backend_synchronized = false`, and
their shares from the pool exactly as tabulated.

## J3. §10 probe updates (delta only)

Deleted probes: evidence-artifact resolution, content-address
verification, pairwise-distinct evidence hashes, orphan evidence file.
Replacing probes: nested `meter_evidence` exact-key/type/enum
validation; inline recomputation of every known charge (tampered
`known_charge_ns` vs inline interval → rejection); timely/late
boundary via `interval_end_reading_ns` against the lease deadline;
`UNKNOWABLE` nullability (`end` null, `backend_synchronized` false);
`observed_utc` ≤ claim `created_utc`; recursive scientific-field
rejection **inside the nested object**; duplicated-field injection
(schema id, process id, stream index, classification inside
`meter_evidence`) → rejection; §D1 completion preconditions — each of
the six violated singly (second unresolved claim, extra entry, missing
dependent artifact, competing override, lease-hash discrepancy,
skipped post-completion verification) → refusal into record-first
invalidity, and the sole positive case (one just-appended entry,
head/cache lag only) → idempotent completion then full verification.

## Compatibility (updated rows only)

| Element | Classification |
|---|---|
| §D1 head/cache completion | **companion core amendment surface** — token 1 (moved out of "harness clarifications") |
| inline `meter_evidence` claim content | **companion core amendment surface** — token 1 |
| §J2 reference updates, §J3 probes, worked-ledger reading | **deterministic harness clarifications** — token 2 scope |

Everything else — signed events (nine), runtime schemas, constants,
roots, phase rules, T bands, WP-3/WP-4, WP-6/WP-9 ownership, the v2.2
§C generational overdue-resume path, and all v2.3 §H1/§H2 orders and
integers — carries forward unchanged. No learner, candidate,
architecture, optimizer, device winner, Q predicate, alpha, endpoint,
margin, or scientific result is selected; T and Q remain permanently
non-citable for C1–C6; the programme claim remains `OPEN`.
