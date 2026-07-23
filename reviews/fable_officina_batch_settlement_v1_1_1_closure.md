READY_FOR_OFFICINA_BATCH_SETTLEMENT_V1_1_1_FINAL_XY_CONFIRMATION

# Fable 5 — Officina batch-settlement v1.1.1 closure memo

Author: Fable 5. Applies exactly the two author-decided engineering
choices exposed in the v1.1 closure — nothing else. Companions:
`successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md`
and `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md`.
Exactly three files were created; nothing else changed; no code
edited; no runtime artifact created; `successor/officina/runtime/`
still contains only `T_RUNTIME.lock`; T remains `NOT_ACTIVATED`. No
F1..F4/R1..R4 closure and no scientific cell is reopened.

## 1. Exact two-row replacement index

| Decision | Replaced loci | Replacement |
|---|---|---|
| 1 — head/cache completion retained, reclassified and narrowed | amendment v1.1 §4d + its §6 classification; harness v2.3 §H3 + its compatibility row | amendment §D1 (six mandatory preconditions; token-1 classification); harness §J1 (by reference) |
| 2 — meter evidence inlined | amendment v1.1 §1b `meter_evidence_sha256`, §1d artifact family, §1f duties 4/9, §3a archival item; harness v2.3 §H4.1, §H2.3 parenthesis, evidence probes in §H5 | amendment §D2 (nested `meter_evidence`, rules, validator delta, four-stream bound); harness §J2/§J3 |

## 2. Final inline claim/stream schema and validator delta

Claim keys (18, unchanged from v1.1 — only the stream entry changed):

```text
schema, scientific_outcome, batch_reason, pre_ledger_entry_sha256,
pre_ledger_head_sha256, pre_state_sha256, created_utc, remaining_ns,
known_total_ns, unknown_stream_count, unknown_pool_ns,
unknown_share_quotient_ns, unknown_share_remainder_count,
dominant_cause, streams, processes, omitted,
recovery_disposition_sha256
```

Stream entry: `{stream_index, process_id, classification,
known_charge_ns, unknown_share_ns, meter_evidence}` with
`meter_evidence` exactly `{clock_kind, boot_identity,
adapter_identity, interval_start_reading_ns, interval_end_reading_ns,
backend_synchronized, observed_utc}` — no field duplicated from the
containing entry or outer claim. Validator delta: duty 4 now validates
the nested object and recomputes every known charge as `end − start`
(timely/late split against the lease deadline; `UNKNOWABLE` ⇒ `end`
null, `backend_synchronized` false); duty 9 drops the
evidence-hash-distinctness clause; the archival staged set drops the
evidence artifacts; `observed_utc` ≤ claim `created_utc`; the outer
`scientific_outcome: false` and recursive scientific-field rejection
govern the nested object. All other duties (1–3, 5–8, 10–12), the
prefix automaton, and the §4e derivation rules are byte-unchanged. No
pre-claim evidence file exists, so no orphan-evidence state exists;
the claim hash directly binds every meter fact.

## 3. Head/cache completion — final preconditions and classification

Amendment §D1: (1) exactly one unresolved, fully re-validated batch
claim; (2) held-lock scan proves an exact byte-match to the next
canonical automaton prefix with only head and/or cache lagging — no
extra entry, missing dependency, competing claim/override,
path/hash/lease discrepancy, or ambiguous state; (3) lag ≤ the one
just-appended state-bearing entry (ordinary `ledger.append`
revalidates the head), cache completion copying only that entry's
embedded post-state; (4) reconstructed authority binds claim hash,
prefix index, old/new head and state hashes; completion idempotent
under the same lock and immediately followed by full verification;
(5) any non-byte-identical suffix or second discrepancy → inherited
record-first invalidity/recovery, never this authority; (6) outside
unresolved batch claims the prior sole-completion boundary is
unchanged. Classification: **amendment-authorized control behavior**
covered by `I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT` — named
as such in both compatibility/signature tables; not an inherited
clarification, not a silent repair; no Kirill-signed recovery decision
is required for this fully pre-authorized, byte-identical cut, and
general record-first invalidity is not weakened.

## 4. No F1..F4/R1..R4 closure regressed

| Closure | Effect of v1.1.1 |
|---|---|
| F1 / §1e full-live-set and recovery-subset rules | untouched |
| F2 / §3d orchestration pins (`runtime.py` unchanged) | untouched; the deleted evidence family removes a planned artifact, adds no code surface |
| F3 / §3b core API and successor authority | untouched; §D1 strengthens the restart path's preconditions only |
| F4 / §4e byte-identical recovery | improved: evidence is no longer a separate re-derivable artifact; all meter facts are claim-hash-bound; timestamp table unchanged |
| R1 / recomputable witness | preserved and strengthened: the same interval facts, nullability, and recomputation duties now live inside the claim the hash of which binds them directly |
| R2 / one canonical order | untouched |
| R3 / registry and stale-authority refusal | untouched; §D1 precondition 1 additionally re-proves single-claim status before any completion |
| R4 / prefix automaton and in-flight fault rule | untouched (evidence never had an automaton substep; the override §5 is unchanged) |

## 5. Updated code/control surface and two-token order

Future code surface (eligible only after final X/Y confirmation and
the signatures, unchanged in shape): `accounting.py` gains exactly
`BatchSettlementAuthority` and `TState.charge_batch_settlement`;
`generic_harness.py` (future, v2 §11) owns claim/override/registry/
automaton construction and validation — now including the §D1
completion and inline-evidence validation; `runtime.py`, `ledger.py`,
`checkpoint.py`, all signed schemas, events, constants, and
`PRODUCTION_ROOTS` remain byte-unchanged. Deleted from the planned
surface: the `t-meter-evidence.v1` family and its paths (never
instantiated). Token order unchanged and **not yet eligible**:
1. `I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT` — now
   explicitly covering §D1 completion behavior and the inline-evidence
   claim content;
2. `I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT`.

## 6. One literal yes/no question per reviewer

**Opus:** Under §D1's six preconditions, is the head/cache completion
fully pre-authorized and byte-deterministic at every reachable cut —
with every non-pre-authorized or ambiguous cut still refusing into the
inherited record-first invalidity/recovery route — yes or no?

**Sol:** Does the inline `meter_evidence` object preserve R1's full
recomputability — every claimed charge derivable from closed
non-outcome meter facts directly bound by the claim hash, with no
orphan-evidence state and claim size bounded by the signed four-stream
cap — yes or no?

## 7. Negative authorization confirmation

This packet authorizes only one final bounded X/Y confirmation, then —
only after both confirmations — Kirill's two ordered signatures.
Neither token is eligible from this correction alone. Created here:
exactly the three mandated files. Not created, not run, not
authorized: any code or code edit, any `accounting.py`/
`generic_harness.py` content, any claim/override/manifest/
authorization/capability/world/learner/process/lease/entropy/spend
instance, any T/Q/C datum, ledger event, outcome, or claim movement.
No implementation hash, reviewed HEAD, or production source set is
pinned. No learner, candidate, architecture, optimizer, device winner,
certificate numeric, Q predicate, alpha, margin, or scientific
endpoint is selected. T remains `NOT_ACTIVATED` at genesis; the
predecessor line remains immutable, `OPEN`, and
`BLOCKED_LEVEL1_FEASIBILITY`; T and Q remain permanently non-citable
for C1–C6; no prediction is made about any learner or about
Philosophia being proved, falsified, or bounded; the programme claim
remains `OPEN`.
