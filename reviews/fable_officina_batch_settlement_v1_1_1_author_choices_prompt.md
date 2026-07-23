# Fable 5: apply two bounded Officina v1.1 author choices before final review

Work in `/home/master/llm_projects/philosophia`.

The v1.1 packet is structurally complete, but its author explicitly exposed two
engineering choices. Resolve them now, before X/Y final confirmation, using the
decisions below. Do not reopen F1..F4/R1..R4 or any scientific cell.

## Authorization boundary

Create exactly three files and change nothing else:

1. `successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md`
2. `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md`
3. `reviews/fable_officina_batch_settlement_v1_1_1_closure.md`

Carry v1 + v1.1 and harness v2/v2.1/v2.2/v2.3 forward except for the exact two
corrections below. Do not implement code or create any runtime artifact.

## Decision 1 — keep deterministic head/cache completion, classify it loudly

Retain v1.1 §4d / v2.3 §H3, but classify this rule as an explicit bounded part of
the author-signed batch-settlement **core amendment**, not as an inherited
clarification and not as a silent repair.

Narrow and pin it:

- only one currently unresolved, valid batch claim may exist;
- the held-lock scan proves the ledger suffix is an exact byte-match to the next
  canonical automaton prefix and that only the external head and/or state cache
  lag; no extra entry, missing dependency, competing claim/override, path/hash/
  lease discrepancy or ambiguous state is permitted;
- because ordinary ledger append revalidates the external head, the lag is at
  most the one just-appended state-bearing entry; state-cache completion copies
  only the exact post-state already embedded in that entry;
- reconstructed authority binds claim hash, prefix index, old/new head and state
  hashes; completion is idempotent under the same lock and immediately followed
  by full verification;
- any non-byte-identical suffix or any second discrepancy follows the inherited
  record-first invalidity/recovery route; it is never repaired by this authority;
- outside unresolved batch claims, the prior sole-completion boundary is
  unchanged.

The compatibility and signature tables must name this as amendment-authorized
control behavior covered by:
`I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT`.
This avoids a Kirill-signed recovery decision for a fully pre-authorized,
byte-identical crash cut without weakening general record-first invalidity.

## Decision 2 — inline meter evidence into the claim

Delete the separate `t-meter-evidence.v1` artifact family and every
`T_METER_EVIDENCE/` path, hash, orphan rule, crash cut and archive obligation.
The signed four-stream cap makes a separate family unnecessary.

Replace each stream entry's `meter_evidence_sha256` with one exact nested
`meter_evidence` object. Avoid duplicated fields already fixed by the containing
stream entry. Pin its exact keys as:

```text
clock_kind, boot_identity, adapter_identity,
interval_start_reading_ns, interval_end_reading_ns,
backend_synchronized, observed_utc
```

Carry forward the v1.1 evidence rules and nullability:

- `clock_kind = CLOCK_MONOTONIC`;
- `boot_identity` and adapter identity match the owning durable lease/adapter;
- known classifications: end is integer > start ≥ last charged reading,
  backend synchronized true, known charge recomputes as end-start;
- `UNKNOWABLE`: end null and backend synchronized false;
- observed time is canonical and derived/captured before claim installation;
- the outer claim's `scientific_outcome:false` and recursive scientific-field
  rejection govern the nested object; no learner/output/result fact is allowed.

The claim hash now directly binds every meter fact. Update validator duties,
worked examples, schemas, prefix automaton, archival sets and harness references.
No pre-claim evidence file exists, so no orphan-evidence state exists. State the
maximum four-stream bound as the reason claim size remains bounded, not as a
scientific choice.

## Closure

First line exactly one verdict:

- `READY_FOR_OFFICINA_BATCH_SETTLEMENT_V1_1_1_FINAL_XY_CONFIRMATION`
- `REVISE_OFFICINA_BATCH_SETTLEMENT_V1_1_1`
- `BLOCKED_OFFICINA_BATCH_SETTLEMENT_V1_1_1`

Then include:

1. exact two-row replacement index;
2. final inline claim/stream schema and validator delta;
3. final head/cache completion preconditions and compatibility classification;
4. proof no F1..F4/R1..R4 closure regressed;
5. updated code/control surface and two-token order;
6. one literal yes/no question for Opus and one for Sol;
7. negative authorization confirmation.

The next step is one final bounded X/Y confirmation, then the two signatures in
order. Neither token is eligible from this correction alone. T remains
`NOT_ACTIVATED`.
