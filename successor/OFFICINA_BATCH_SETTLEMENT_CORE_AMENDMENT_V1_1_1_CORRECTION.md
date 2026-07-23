# Officina batch-settlement core amendment — v1.1.1 bounded correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`. Carries
the v1 amendment as corrected by v1.1
(`successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md`,
`…_V1_1_CORRECTION.md`, both preserved unedited as review evidence)
forward verbatim except for the **exact two author-decided
corrections** below. Companion:
`successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md`.
No F1..F4/R1..R4 closure is reopened; no scientific cell is touched.
This correction implements nothing, edits no code, creates no runtime
artifact, and leaves T `NOT_ACTIVATED`. Neither author token is
eligible; the two-token order is unchanged.

**Replacement index (all other v1+v1.1 text carries forward):**

| v1.1 locus | Action |
|---|---|
| §4d (batch-authorized head/cache completion) and its §6 classification as a harness-side extension | **replaced** by §D1 below: same rule, narrowed preconditions, reclassified as an explicit bounded surface of the author-signed core amendment (token 1) |
| §1b `meter_evidence_sha256` key; §1d (`t-meter-evidence.v1` artifact family, `T_METER_EVIDENCE/` path, pre-claim write, orphan/crash/archive obligations); §1f duties 4 and 9 (evidence-artifact resolution; "evidence hashes pairwise distinct"); §3a archival item "its evidence artifacts" | **replaced** by §D2 below: one exact nested `meter_evidence` object per stream entry; no separate evidence family exists anywhere |

## D1. Deterministic head/cache completion — amendment-authorized (Decision 1)

The v1.1 §4d completion is **retained** with the following narrowed,
exhaustive preconditions, and is **reclassified**: it is an explicit
bounded part of the author-signed batch-settlement **core amendment**,
covered by `I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT` — not
an inherited §3 clarification and not a silent repair.

Preconditions (all mandatory, proved under the held lock):

1. exactly **one** currently unresolved batch claim exists, and it
   validates in full under §1f (a second unresolved claim, or a claim
   failing re-validation, refuses into the record-first
   invalidity/recovery route);
2. the held-lock scan proves the ledger suffix after
   `pre_ledger_entry_sha256` is an **exact byte-match** to the next
   canonical automaton prefix (§4a/§4b) and that **only** the external
   head and/or state cache lag it — no extra entry, no missing
   dependent artifact, no competing claim or override, no
   path/hash/lease discrepancy, and no ambiguous state is permitted;
3. because ordinary `ledger.append` revalidates the external head
   before writing, the lag is **at most the one just-appended
   state-bearing entry**; state-cache completion copies only the exact
   post-state already embedded in that durable entry — nothing is
   computed, chosen, or read from a clock;
4. the reconstructed authority (§3c) binds the claim hash, the
   validated prefix index, and the **old and new** head and state
   hashes; the completion is idempotent under the same lock epoch and
   is **immediately followed by full verification** of the completed
   tree before any further automaton action;
5. any non-byte-identical suffix, or any **second** discrepancy of any
   kind, follows the inherited record-first invalidity/recovery route
   — it is never repaired by this authority;
6. outside unresolved batch claims, the prior sole-completion boundary
   (v2 §3a original scope; v2.1 C.4 head-behind rule) is **unchanged**.

Rationale, stated once: the durable claim pre-authorizes exactly the
lagging entry, so requiring a Kirill-signed recovery decision for a
fully pre-authorized, byte-identical crash cut adds an author action
without adding information; general record-first invalidity is not
weakened because every non-pre-authorized or ambiguous cut still
refuses into it.

## D2. Inline meter evidence (Decision 2)

The separate `t-meter-evidence.v1` artifact family is **deleted**:
every `T_METER_EVIDENCE/` path, content-addressed hash, pre-claim
write duty, orphan rule, crash cut, and archive obligation is removed.
No pre-claim evidence file exists, so **no orphan-evidence state
exists**. The claim hash now directly binds every meter fact.

### D2a. Stream entry (replaces §1b key list)

`streams` entries carry keys exactly:

```text
stream_index, process_id, classification, known_charge_ns,
unknown_share_ns, meter_evidence
```

with `stream_index`/`process_id`/`classification` and the
known-charge/share nullability rules unchanged from v1.1 §1b.
`meter_evidence` is one exact nested object, keys exactly:

```text
clock_kind, boot_identity, adapter_identity,
interval_start_reading_ns, interval_end_reading_ns,
backend_synchronized, observed_utc
```

No field fixed by the containing stream entry or the outer claim is
duplicated (no schema id, no `scientific_outcome`, no process id, no
stream index, no classification inside the nested object).

### D2b. Evidence rules (carried forward from v1.1 §1d, now inline)

- `clock_kind` = `CLOCK_MONOTONIC` exactly;
- `boot_identity` equals the owning durable lease's;
  `adapter_identity` equals the admitted adapter's pinned identity;
- known classifications (`TIMELY_KNOWN`/`LATE_KNOWN`):
  `interval_end_reading_ns` integer > `interval_start_reading_ns` ≥
  the lease's `last_charged_reading_ns`; `backend_synchronized`
  exactly true; the known charge **recomputes** as
  `interval_end_reading_ns − interval_start_reading_ns` and must equal
  `known_charge_ns`; `TIMELY_KNOWN` iff `interval_end_reading_ns` ≤
  the lease's `heartbeat_deadline_ns`, `LATE_KNOWN` iff greater;
- `UNKNOWABLE`: `interval_end_reading_ns` null and
  `backend_synchronized` exactly false
  (`interval_start_reading_ns` remains the integer last durable
  cursor);
- `observed_utc` canonical UTC, captured/derived **before claim
  installation** and ≤ the claim's `created_utc`;
- the outer claim's `scientific_outcome: false` and the recursive
  scientific-field rejection govern the nested object; no
  learner/output/result fact may appear at any depth.

### D2c. Validator delta (replaces §1f duties 4 and 9; all else unchanged)

- Duty 4 (replaced): for every stream, validate the nested
  `meter_evidence` object's exact keys, types, and the §D2b rules,
  recomputing every known charge from the inline interval facts;
- Duty 9 (replaced): no missing, extra, or duplicate stream index or
  process id (the "evidence hashes pairwise distinct" clause is
  deleted with the hashes themselves).

The §3a resolution predicate's archival staged set drops "its evidence
artifacts"; the claim alone now carries all meter facts into the
archive. The §4 prefix automaton is unchanged (evidence never had a
substep — it preceded the claim); the §4e derivation rules are
unchanged.

### D2d. Bounded size (engineering fact, not a scientific choice)

The signed concurrency boundary (`MAX_CONCURRENT_LEASES = 4`;
admission refuses `live_units + requested_units > 4`) caps any batch
at **four streams** across at most four processes. A claim therefore
contains at most four stream entries with one nested evidence object
each, so inlining keeps the claim bounded and a separate
content-addressed family is unnecessary. This restates a signed
constant; it selects nothing.

## Compatibility and signature classification (updated rows only)

| Element | Classification |
|---|---|
| §D1 head/cache completion under an unresolved batch claim | **amendment-authorized control behavior** — an explicit bounded surface of the core amendment, covered by `I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT`; neither an inherited clarification nor a silent repair |
| §D2 inline `meter_evidence` object | **amendment surface** (claim schema content), same token; deletes a planned artifact family before first use — no instance ever existed |
| general record-first invalidity, v2 §3a original scope, v2.1 C.4 | **unchanged** outside unresolved batch claims |

All other v1.1 classifications, the two-token order
(`I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT` first, then
`I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT`), and every negative
boundary carry forward: no learner, candidate, optimizer, device
winner, Q predicate, alpha, endpoint, margin, or scientific result is
selected; no code is edited; no claim/override/manifest/authorization/
capability/process/lease/entropy/spend or T/Q/C datum is created. T
remains `NOT_ACTIVATED`; T and Q remain permanently non-citable for
C1–C6; the programme claim remains `OPEN`.
