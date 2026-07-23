# Officina batch-settlement core amendment — v1.1 bounded correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`. Carries
the v1 amendment
(`successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md`,
preserved unedited as review evidence) forward except for the exact
replacements below, applying Opus F1..F4 and Sol R1..R4 one-to-one.
Companion: `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_CORRECTION.md`.
This correction implements nothing, edits no code, creates no
manifest/authorization/claim instance/capability/process/world/learner/
entropy/spend/datum, and leaves T `NOT_ACTIVATED`. Neither author token
is eligible; the two-token order is unchanged
(`I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT`, then
`I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT`).

The claim schema id remains `philosophia.officina.t-batch-settlement-claim.v1`:
no instance and no validator of the v1 key set ever existed, so v1.1
redefines the key set before first use rather than versioning it.

**Replacement index (all other v1 text carries forward):**

| v1 locus | Action |
|---|---|
| §2b (claim schema and keys) | **replaced** by §1 (closed accounting witness; completeness rules) |
| §2c authority semantics, "constructed … from a validated batch claim + pre-state match" | **extended** by §3 (registry, exact core API, restart reconstruction; pre-state match applies only before tuple 1) |
| §2d ordering sentence ("unknown/non-crossing … before crossing processes") | **replaced** by §2 (one global ascending `process_sequence` order) |
| §2d post-verifier list | **extended** by §1f duties and §4 automaton acceptance |
| §2e crash-cut table | **replaced** by §4 (complete prefix automaton; deterministic derivation) |
| §3 (future code surface) | **extended** by §3d orchestration pins (runtime.py unchanged and unused for batch charges) |
| — (new) | §5 in-flight infrastructure fault override |

---

## 1. Closed accounting witness and claim completeness (Sol R1; Opus F1)

### 1a. Claim schema (redefined; keys exactly)

`philosophia.officina.t-batch-settlement-claim.v1`, canonical path
`successor/officina/runtime/T_BATCH_SETTLEMENT_CLAIMS/<pre_ledger_head_sha256>.json`
(atomic no-replace; at most one claim per ledger position; retained
forever), canonical ASCII JSON, keys exactly:

```text
schema, scientific_outcome, batch_reason, pre_ledger_entry_sha256,
pre_ledger_head_sha256, pre_state_sha256, created_utc, remaining_ns,
known_total_ns, unknown_stream_count, unknown_pool_ns,
unknown_share_quotient_ns, unknown_share_remainder_count,
dominant_cause, streams, processes, omitted,
recovery_disposition_sha256
```

Types/enums (exact): `scientific_outcome` exactly false; `batch_reason`
∈ {`E1_BOUNDARY`, `E3_BOUNDARY`, `RUNTIME_INVALIDITY`,
`RECOVERY_SETTLEMENT`}; all `*_ns` and `*_count` values non-negative
integers; `dominant_cause` null or one of
{`PROCESS`, `RESOURCE`, `HASH`, `CLOCK`, `FILESYSTEM`};
`recovery_disposition_sha256` null except for `RECOVERY_SETTLEMENT`,
where it is the SHA-256 of the verified
`t-recovery-disposition.v1` artifact authorizing the claim;
`created_utc` canonical UTC whole-second, ≥ the pre-head entry's
timestamp (refused otherwise — this is what makes every later
derived timestamp ledger-monotone).

### 1b. `streams` (global witness array)

Sorted ascending `stream_index`; entry keys exactly:

```text
stream_index, process_id, classification, known_charge_ns,
unknown_share_ns, meter_evidence_sha256
```

- `stream_index`: 1-based, contiguous, globally unique across the
  batch; assigned in ascending (`process_sequence`, adapter-canonical
  stream order). The adapter contract must define a deterministic
  stream enumeration (CPU adapter: ascending kernel start-identity,
  then PID). Once the claim is durable the indexes are frozen; it is a
  batch-computation field of this closed artifact only — **no signed
  event/runtime schema gains any field**.
- `classification` ∈ {`TIMELY_KNOWN`, `LATE_KNOWN`, `UNKNOWABLE`}
  (fixed enum; exactly the signed §4c cases a/b/c).
- Nullability (exact): `TIMELY_KNOWN`/`LATE_KNOWN` ⇒ `known_charge_ns`
  positive integer, `unknown_share_ns` null; `UNKNOWABLE` ⇒
  `known_charge_ns` null, `unknown_share_ns` positive integer.
- `meter_evidence_sha256`: SHA-256 of the stream's closed non-outcome
  meter-evidence artifact (§1d).

### 1c. `processes` (per-process decomposition) and `omitted`

`processes` sorted ascending `process_sequence`; entry keys exactly:

```text
process_id, process_sequence, active_lease_sha256, known_charge_ns,
unknown_share_ns, charge_ns, disposition, invalid_cause
```

- `active_lease_sha256` = SHA-256 of the durable pre-settlement lease
  file; `known_charge_ns` = Σ its streams' known charges (0 if none);
  `unknown_share_ns` = Σ its streams' shares (0 if none); `charge_ns`
  = `known_charge_ns + unknown_share_ns`, positive, never clipped.
- `disposition` ∈ {`T_PROCESS_E1_EXHAUSTED`, `T_PROCESS_E3_DUE`,
  `T_PROCESS_INVALID`}; `invalid_cause` null for valid dispositions,
  else **exactly equal to `dominant_cause`** (the B.3 inheritance:
  one cause per batch).

`omitted` (array; **must be empty** except for `RECOVERY_SETTLEMENT`);
entry keys exactly `{process_id, omission_reason,
ancestor_claim_sha256}` with `omission_reason` ∈
{`TERMINAL_RECORD_DURABLE`, `ANCESTOR_CLAIM_ENUMERATED`};
`ancestor_claim_sha256` null for the first value and the SHA-256 of the
one specifically named unresolved ancestor batch claim for the second.

### 1d. Meter-evidence artifact (closed, non-outcome)

Schema `philosophia.officina.t-meter-evidence.v1`, canonical path
`successor/officina/runtime/T_METER_EVIDENCE/<sha256-of-content>.json`
(content-addressed, atomic no-replace, file+dir fsync, written and
verified **before** the claim, retained forever), keys exactly:

```text
schema, scientific_outcome, process_id, stream_index, classification,
clock_kind, boot_identity, adapter_identity,
interval_start_reading_ns, interval_end_reading_ns,
backend_synchronized, observed_utc
```

Rules: `clock_kind` = `CLOCK_MONOTONIC`; `boot_identity` equals the
owning lease's; known classifications ⇒ `interval_end_reading_ns`
integer > `interval_start_reading_ns` ≥ the lease's
`last_charged_reading_ns`, `backend_synchronized` exactly true;
`UNKNOWABLE` ⇒ `interval_end_reading_ns` null, `backend_synchronized`
exactly false. It contains only process/resource/integrity/clock fact
classes (v2 §F); `reject_scientific_fields` applies recursively; no
learner observation, result hash, loss, or output fact may appear.

### 1e. Completeness (Opus F1)

For `E1_BOUNDARY`, `E3_BOUNDARY`, and `RUNTIME_INVALIDITY`:
`processes` must equal **exactly the entire durable active-lease set**
at `pre_ledger_head_sha256` — the verified contents of
`successor/officina/runtime/T_ACTIVE_LEASES/` read under the held lock
in the same epoch that writes the claim — sorted ascending
`process_sequence`; `omitted` is empty.

For `RECOVERY_SETTLEMENT`: `processes` ∪ `omitted` (by `process_id`)
must equal exactly that durable active-lease set, with no duplicate id
across the two arrays. Every omitted lease must be proved either
(i) `TERMINAL_RECORD_DURABLE` — its verified final process record
exists in `T_PROCESS_RECORDS/` and only its lease removal remains
pending under an ancestor claim's automaton, or (ii)
`ANCESTOR_CLAIM_ENUMERATED` — it is enumerated by the one named
unresolved ancestor claim, whose completion (or override, §5, or
superseding disposition) governs it. **No live lease may be silently
stranded**: an active lease neither enumerated nor covered by an
omission proof refuses the claim.

### 1f. Validator duties (all before any authority exists)

1. exact key sets, types, enums, nullability, sort orders, path/name
   identity (filename = `pre_ledger_head_sha256`), no-replace;
2. `pre_ledger_entry_sha256`/`pre_ledger_head_sha256`/`pre_state_sha256`
   match the durable ledger tail, external head, and state cache;
   pre-state `device_nanoseconds` **below** the E1 cap;
3. `remaining_ns` = E1 cap − pre-state `device_nanoseconds`;
4. every stream's evidence artifact present, hash-exact, and
   consistent: recomputed known charge =
   `interval_end_reading_ns − interval_start_reading_ns` equals
   `known_charge_ns`; `TIMELY_KNOWN` iff `interval_end_reading_ns` ≤
   the lease's `heartbeat_deadline_ns`, `LATE_KNOWN` iff greater;
   boot identity and clock kind match the lease;
5. `known_total_ns` = Σ all known charges;
   `unknown_stream_count` = m = count of `UNKNOWABLE` streams;
6. recompute the pool: m = 0 ⇒ `unknown_pool_ns`, quotient, and
   remainder all exactly 0 and no stream carries a share; m > 0 ⇒
   `unknown_pool_ns` = U = `max(m, remaining_ns − known_total_ns)`
   (nanoseconds), `unknown_share_quotient_ns` = `floor(U/m)`,
   `unknown_share_remainder_count` = `U mod m`; share of the j-th
   `UNKNOWABLE` stream in ascending `stream_index` =
   quotient + 1 ns for the first remainder streams, quotient
   thereafter; Σ shares = U exactly;
7. every stream's `process_id` names an enumerated process; every
   process aggregate (`known_charge_ns`, `unknown_share_ns`,
   `charge_ns`) equals the recomputed sums of its streams;
   `charge_ns` > 0;
8. full-sum conservation: Σ `charge_ns` =
   `known_total_ns + unknown_pool_ns`;
9. no missing, extra, or duplicate stream index, process id, or
   evidence hash (evidence hashes pairwise distinct);
10. disposition/reason relation (§1g); `invalid_cause` =
    `dominant_cause` on every invalid entry;
11. completeness per §1e against the durable lease directory;
12. `recovery_disposition_sha256` present, verified, and binding this
    claim's pre-head for `RECOVERY_SETTLEMENT`; null otherwise;
    `reject_scientific_fields` recursively over the whole claim.

A claim failing any duty is refused before creation; a durable claim
failing re-validation at any later lock entry is record-first
invalidity. Recovery can therefore enforce "charge exactly what the
claim proves," not merely "what the claim says": every `charge_ns` is
recomputable from closed meter facts, never trusted.

### 1g. Disposition/reason relation (exact)

| `batch_reason` | admissible dispositions | `dominant_cause` | terminal route |
|---|---|---|---|
| `E1_BOUNDARY` | all `T_PROCESS_E1_EXHAUSTED` (all streams known) | null | one `T_ENVELOPE_EXHAUSTED` after all valid tuples → G7 |
| `E3_BOUNDARY` | all `T_PROCESS_E3_DUE` (all streams known) | null | G2; no terminal event |
| `RUNTIME_INVALIDITY` | all `T_PROCESS_INVALID` | one cause (§2a precedence) | G5; no valid event |
| `RECOVERY_SETTLEMENT` | all `T_PROCESS_INVALID` | one cause | G5; no valid event |

Any `UNKNOWABLE` stream anywhere in the batch forces
`batch_reason` ∈ {`RUNTIME_INVALIDITY`, `RECOVERY_SETTLEMENT`} and all
dispositions invalid with the one dominant cause (per-stream
classification per v2.2 A1; whole-batch invalid dominance per v2.1
B.3/B.4). Mixed valid/invalid dispositions inside one claim do not
exist (§5 handles a fault arising *after* an all-valid claim).

## 2. One canonical order (Sol R2)

The claim's `processes` array order and the execution order are
**identical: global ascending `process_sequence`, for every batch and
every `batch_reason`.** All class ordering is removed.
Crossing/non-crossing is **descriptive only** — never an ordering
predicate, never a claim field, and never inferred from evolving
state: the frozen-batch authority (§3) permits every claimed positive
charge to append regardless of its position relative to the cap, so no
order-dependent representability exists. `streams` order (§1b) is the
allocation order; `processes` order is the execution order; both are
frozen in the claim. All worked ledgers are updated in the companion
harness v2.3 §H2.

## 3. Unresolved-claim registry and exact core authority (Sol R3; Opus F3)

### 3a. Registry scan (every runtime-lock entry)

Step 1 of **every** §3-template transaction additionally enumerates
`T_BATCH_SETTLEMENT_CLAIMS/`. A claim is **unresolved** iff its
`pre_ledger_entry_sha256` is an ancestor of (present in) the current
ledger chain (or equals the genesis hash for an empty tail) and its
resolution predicate is incomplete. Resolution predicate — all of:

1. the ledger/artifact suffix after `pre_ledger_entry_sha256`,
   restricted to batch work, is the **complete** canonical automaton
   (§4) for the claim (every tuple through verified lease removal, plus
   the authorized terminal event for an all-valid `E1_BOUNDARY`
   claim), as possibly extended by exactly one verified override (§5);
2. the batch archival commit exists (staged set: claim, its evidence
   artifacts, override if any, every tuple record/detail file, state,
   ledger, head; fixed trailers); **or**
3. a verified `t-recovery-disposition.v1` names this claim as
   superseded and its named `RECOVERY_SETTLEMENT` successor claim is
   itself resolved.

**Blocking rule:** while any claim is unresolved, every new batch
claim, process claim/admission, lease renewal, capability issuance,
and behavior-capable operation refuses. The only permitted actions are:
the unresolved claim's single next automaton action (§4), creation of
its override when §5's predicate holds, the signed
recovery-disposition route, and the archival commit. Exception, exact:
a `RECOVERY_SETTLEMENT` claim may be created while an ancestor claim
is unresolved **only** under a verified recovery disposition that
names that ancestor claim hash, and must satisfy §1e's omission
proofs. Shadowing a partial batch by a new claim at the advanced
prefix head is therefore impossible: the advanced head's claim slot is
free, but the registry blocks creation while the ancestor is
unresolved.

### 3b. Exact core API (Opus F3)

```text
TState.charge_batch_settlement(
    *, process_id, active_lease_sha256, value, envelope, authority
) -> (TState, BatchSettlementAuthority)
```

`BatchSettlementAuthority` is a frozen type binding exactly:
`claim_sha256`; the frozen `entries` tuple
(`(process_id, active_lease_sha256, charge_ns)` in the claim's §2
order); `consumed_count` (the validated consumed prefix length);
`expected_ledger_head_sha256`; `expected_state_sha256`. It is
constructed only from a §1f-validated claim (plus, on restart, the
§3c-validated durable prefix) and is single-use per entry.

The call **refuses** (raises; no partial effect) unless all hold:
`(process_id, active_lease_sha256, value)` equals
`entries[consumed_count]` exactly (any reorder, duplicate, omission/
skip, value increase or decrease refuses); `consumed_count <
len(entries)` (an already-consumed index refuses); the caller-supplied
current durable ledger-head hash equals
`expected_ledger_head_sha256` and the current state's canonical hash
equals `expected_state_sha256` (stale head/state refuses); the
authority's `claim_sha256` equals the claim being executed (claim
substitution refuses); `value` > 0. On success it returns the
post-charge `TState` (permitted to be at or above the E1 cap — this
narrow method, not `charge_device_nanoseconds`, is the only post-cap
route) and the successor authority with `consumed_count + 1` and
`expected_state_sha256` advanced to the post-charge state; the harness
updates the head expectation from the durable ledger under the same
lock before the next call. The initial pre-state/pre-head match
(`expected_* = pre_state_sha256 / pre_ledger_head_sha256`) applies
**only before tuple 1**.

### 3c. Restart reconstruction

At a lock entry with an unresolved claim, the harness re-derives the
next-step authority **from the exact durable prefix, never by
requiring the current state to equal the old pre-state**: validate the
ledger suffix after `pre_ledger_entry_sha256` as a prefix of the
canonical automaton (§4); `consumed_count` = the number of durable
`T_DEVICE_TIME_CHARGED` entries matching claim entries in order
(each must match `process_id`, `active_lease_sha256`, `charge_ns`, and
the deterministic timestamp byte-exactly, else record-first
invalidity); `expected_state_sha256` = the deterministic post-state
after those charges (pre-state plus the consumed prefix's charges);
`expected_ledger_head_sha256` = the current durable head. Any
non-conforming suffix entry, artifact, or hash is record-first
invalidity and the signed recovery route; nothing is recomputed from
outcomes.

### 3d. Orchestration pins — `runtime.py` unchanged (Opus F2)

| Batch operation | Producer | Status |
|---|---|---|
| post-cap accounting state | `TState.charge_batch_settlement` (new, `accounting.py`) | the amendment |
| `BatchSettlementAuthority` | new frozen type, `accounting.py` | the amendment |
| `T_DEVICE_TIME_CHARGED` event | `ledger.append` + `validate_ledger_event` | existing, unchanged |
| invalidity detail record | `validate_invalidity_record` | existing, unchanged |
| INVALID / valid process records | `build_process_record` | existing, unchanged |
| lease reads | `validate_active_lease` (durable pre-settlement lease) | existing, unchanged |
| claim/evidence/override construction & validation; registry; automaton | `generic_harness.py` | future new file (v2 §11) |

`settle_active_lease` and `settle_monotonic_delta` remain byte-for-byte
**unchanged and are not used for batch charges** (both route through
`charge_device_nanoseconds`, which correctly refuses at/above cap and
is not weakened). No existing constructor imposes an upper-cap
ceiling on states, events, leases, or records (verified in the X-line
review), so `runtime.py`, `ledger.py`, and `checkpoint.py` are
untouched. Batch charge events bind the **durable pre-settlement lease
hash** (= the claim entry's `active_lease_sha256`); consequently a
batch-closed process record's `cumulative_charge_ns` equals the
pre-settlement lease's cumulative, and the final claimed charge is
carried solely by the bound `final_charge_event_sha256`'s `charge_ns`
(total process E1 = record cumulative + final charge, witness-checked;
ordinary non-batch closes keep their existing settled-lease binding).
Control pins, named honestly: `accounting.py` is on the
immutable-control allowlist — this is a reviewed control change
eligible only after final X/Y confirmation and the amendment token;
`generic_harness.py` is added to reviewed sources and
`PRODUCTION_ROOTS` membership stays exactly the pinned tuple; the
production manifest remains absent until implementation review.

## 4. Complete prefix automaton and byte-identical recovery (Sol R4; Opus F4)

### 4a. Canonical tuple sequences

Per claim entry i, in the §2 order (head/cache: every ledger append
replaces the external head within the append; the state cache is
replaced before the next durable step of the same epoch):

```text
invalid tuple:  C_i  charge event (T_DEVICE_TIME_CHARGED)
                D_i  invalidity detail record (file)
                E_i  T_RUNTIME_INVALID (previous = C_i hash, sequence+1)
                R_i  INVALID process record (file)
                L_i  verified lease removal
valid tuple:    C_i  charge event
                V_i  valid process record (file)
                S_i  T_PROCESS_STOPPED (binds V_i hash)
                L_i  verified lease removal
terminal:       X    one T_ENVELOPE_EXHAUSTED (all-valid E1_BOUNDARY only)
                A    archival commit (exact staged set)
```

### 4b. Prefix table — exactly one next action per durable prefix

| Durable prefix at lock entry | Sole next action |
|---|---|
| claim durable; no tuple work | append `C_1` under the reconstructed authority |
| `C_i` in ledger; head and/or cache behind | **finish head/cache** (§4d batch-authorized completion); no new clock, no new charge |
| `C_i` complete; invalid tuple; `D_i` absent | write `D_i` (derived bytes, §4e); finish the already-charged tuple **without another charge** |
| `D_i` durable; `E_i` absent | append `E_i` |
| `E_i` durable; `R_i` absent | write `R_i` |
| `R_i` durable; lease present | perform `L_i` |
| `C_i` complete; valid tuple; `V_i` absent | write `V_i` |
| `V_i` durable; `S_i` absent | append `S_i` |
| `S_i` durable; lease present | perform `L_i` |
| tuple i complete; i < n | **append the next claimed charge** `C_{i+1}` |
| all n tuples complete; all-valid `E1_BOUNDARY`; `X` absent | **append the already-authorized global terminal** `X` — never archive first, never a new claim |
| all tuples complete (+ `X` where authorized); archival absent | **archive** the exact staged set; capability blocked until done |
| archival durable | claim resolved; ordinary rules resume |
| any suffix entry/artifact not byte-conforming to the claim automaton | **remain blocked**: record-first invalidity + signed recovery disposition |

No prefix permits a re-charge, abandonment, nesting, reordering, or
recomputation from outcomes; between-tuple and intra-tuple crashes
alike resume the single canonical continuation.

### 4c. Reconciliation with the inherited §3 rules

- **Record-first preserved:** `D_i` strictly precedes `E_i`; a durable
  `D_i` awaiting its `E_i` inside an authorized batch is the expected
  prefix, **not** an orphan. An artifact *not* derivable from the
  claim automaton remains an orphan → record-first invalidity,
  unchanged.
- **Head-behind cut:** outside an authorized batch, ledger-ahead-of-head
  remains record-first invalidity with head repair only under the
  signed recovery route (v2 §3 / v2.1 C.4, unchanged). Inside one, §4d
  applies because the appended entry must byte-match the outstanding
  claim entry.
- **Archival:** never a runtime safety precondition; the "during 8"
  rule carries forward (charge untouched; capability blocked; commit
  completed under a signed process disposition when the batch itself
  cannot).

### 4d. Batch-authorized head/cache completion (loud extension of §3a)

Within an unresolved claim, if the durable ledger suffix after
`pre_ledger_entry_sha256` byte-matches a valid automaton prefix and
only the external head and/or state cache lag it, the harness completes
them idempotently at the next lock entry **under the reconstructed
authority**. This is not a silent repair: the durable claim is itself
the prior authorization of exactly that entry, and any non-matching
entry still refuses into record-first invalidity. The harness contract's
§3a "sole silent completion" wording is replaced accordingly (v2.3
§H3); outside claim-authorized suffixes §3a's original scope is
unchanged.

### 4e. Deterministic derivation — byte-identical recovery (Opus F4)

Every otherwise-variable field of every tuple artifact is a
deterministic function of durable parent facts (the claim, the durable
charge event, and — for §5 routes — the override). **No recovery
clock exists.**

Timestamp table (exact):

| Field | Value |
|---|---|
| claim `created_utc` | captured once at claim creation; ≥ pre-head entry timestamp |
| `C_i` `timestamp_utc` | claim `created_utc` (override-routed post-override charges: override `created_utc`) |
| `D_i` `observed_utc` | = its tuple's terminal timestamp (below) |
| `E_i` `timestamp_utc` | claim `created_utc`; override-routed: override `created_utc` |
| `R_i`/`V_i` `closed_utc` | = its tuple's terminal event timestamp |
| `S_i` `timestamp_utc` | claim `created_utc` |
| `X` `timestamp_utc` | claim `created_utc` |
| override `created_utc` | captured once at override creation; ≥ last durable entry timestamp |

Equal timestamps are ledger-legal (monotonicity refuses only
backward motion); §1a/§5 creation checks make every derived value
monotone. Derivation rules for dependent artifacts:

- **`D_i`** (`t-runtime-invalidity.v1`, signed keys unchanged):
  `invalid_cause` = the entry's cause (§1g; override: dominant cause);
  `transaction_kind` = `T_BATCH_SETTLEMENT`; `durable_step_index` = i
  (the entry's 1-based claim position); `affected_path_sha256` =
  {claim relative path: claim SHA-256, lease relative path: the
  entry's `active_lease_sha256`} plus, for override routes, the
  override path/hash; `clock_kind` = `CLOCK_MONOTONIC`;
  `boot_identity` = the lease's; `observed_utc` per the table;
  `outstanding_liability_ns` = the durable lease's value;
  `required_action` fixed.
- **`E_i`**: `invalidity_record_sha256` = SHA-256 of `D_i`; `t_state` =
  the deterministic post-charge state (pre-state plus the claim's
  charges through entry i — pure integer arithmetic).
- **`R_i`/`V_i`** via the unchanged `build_process_record`: lease = the
  durable pre-settlement lease; `final_charge_event` = the durable
  `C_i`; disposition/cause from the claim (or override); `closed_utc`
  per the table; `final_state` = the same deterministic post-charge
  state.

Two recovery attempts, or two independent implementers, therefore emit
byte-identical artifacts and hashes for every re-derived object.

## 5. In-flight infrastructure fault override

### 5a. Crash vs verified invalidity (exact predicate)

At a lock entry with an unresolved claim: if anchors, control bytes,
and every referenced artifact verify, and the durable suffix is a
byte-conforming automaton prefix — it is a **recoverable crash**;
resume the canonical prefix (§4b). Otherwise, or when a §2a-typed
infrastructure fault (`HASH`/`FILESYSTEM`/`CLOCK`/`PROCESS`/`RESOURCE`)
is durably observed during batch work: it is a **verified
infrastructure invalidity**. For a claim whose remaining dispositions
are valid, the override below applies; for a claim already carrying
invalid dispositions, the claim's own invalid route continues if
conforming, else the runtime **remains blocked** on the signed
recovery-disposition route. If the invalidity prevents durable
creation or verification of the override itself, the runtime remains
blocked; **it never improvises a route.**

### 5b. Override artifact (closed control artifact; no tenth event)

Schema `philosophia.officina.t-batch-settlement-invalidity-override.v1`,
canonical path
`successor/officina/runtime/T_BATCH_SETTLEMENT_OVERRIDES/<batch_claim_sha256>.json`
(atomic no-replace — **at most one override per claim, ever**; file +
directory fsync; post-verify; retained forever), created **before any
further tuple work**, keys exactly:

```text
schema, scientific_outcome, batch_claim_sha256, validated_prefix_count,
pre_override_ledger_head_sha256, pre_override_state_sha256,
dominant_cause, remaining_process_ids, replacement_dispositions,
created_utc
```

`validated_prefix_count` = the number of fully complete tuples at
creation; `pre_override_*` = the exact durable head/state hashes at
creation (validator refuses mismatch — this excludes competing
overrides built on divergent views); `dominant_cause` = the one
§2a-precedence cause; `remaining_process_ids` = the claim-order ids of
every process after the validated prefix (including the current
partially complete tuple's process); `replacement_dispositions` = a
claim-order array of `{process_id, disposition, invalid_cause}` with
`disposition` exactly `T_PROCESS_INVALID` and `invalid_cause` exactly
`dominant_cause`, covering exactly `remaining_process_ids`.
`reject_scientific_fields` applies. Uses only existing events and
signed schemas — no signed event/schema change is required, so this
correction is not `BLOCKED`.

### 5c. Override semantics

- The claim is **never mutated**; already valid-closed processes and
  every durable ledger entry remain immutable — no relabelling.
- Each remaining process follows the **invalid route with the one
  dominant cause** and its **unchanged claimed `charge_ns`**: if its
  charge is already durable, the tuple is finished on the invalid
  route without another charge; otherwise the claimed charge is
  appended first (post-override timestamps per §4e).
- **No global valid exhaustion/stop/pause event is appended; the final
  global route is G5** even when the batch reason was `E1_BOUNDARY`
  (the cap value is retained as a numeric fact in the invalid
  post-states).
- Resolution predicate (§3a) extends to the override-adjusted
  automaton; the archival staged set additionally includes the
  override. Crash cuts: before the override file — the §5a predicate
  re-evaluates at next entry; after the file, before further work —
  the override governs (its bindings pin the resume point); nested or
  second overrides are impossible (no-replace path keyed by claim
  hash; head/state bindings).

## 6. Governance, classification, and negative space

**Amendment surfaces** (eligible only after final X/Y confirmation and
token 1): the `accounting.py` authority type and
`charge_batch_settlement` method; the closed claim, meter-evidence, and
override schemas; the registry/blocking rule; the automaton and its
authorized head/cache completion — the control semantics under which
the metering core's post-cap authority may exist at all.
**Harness clarifications** (token 2 scope, companion v2.3): the global
execution order, the recomputed worked ledgers, witness construction
duties, the batch-close lease binding, and the §10 probes. The
two-token order is unchanged and **not yet eligible**; no author
choice is invented here — every constant, event, schema key of signed
artifacts, phase rule, and scientific boundary is untouched.

No learner, candidate, architecture, optimizer, training rule, device
winner, certificate numeric, Q predicate, alpha, margin, endpoint, or
scientific result is selected; no code is edited; no runtime artifact,
claim, evidence, override, authorization, capability, world, process,
lease, entropy, or E1/E2/E3 spend is created. T remains
`NOT_ACTIVATED`; T and Q remain permanently non-citable for C1–C6;
WP-3/WP-4 boundaries, WP-6/WP-9 ownership, and every negative
destination are unchanged; the programme claim remains `OPEN`.
