READY_FOR_OFFICINA_BATCH_SETTLEMENT_V1_1_FINAL_CONFIRMATION

# Fable 5 — Officina batch-settlement amendment v1.1 closure memo

Author: Fable 5. Companion to
`successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_CORRECTION.md`
and `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_CORRECTION.md`.
Inputs: Opus (`REVISE…_XLINE`, F1..F4) and Sol (`REVISE…_YLINE`,
R1..R4) on the v1 amendment packet. Exactly three files were created;
nothing else changed; no code edited, nothing committed or run beyond
reading; no runtime claim/manifest/authorization/artifact created; T
remains `NOT_ACTIVATED`; `successor/officina/runtime/` still contains
only `T_RUNTIME.lock`. Neither author token is eligible; the two-token
order is unchanged.

## 1. One-to-one disposition (F1..F4, R1..R4)

| Finding | Disposition | Where |
|---|---|---|
| **Opus F1** — claim completeness not pinned/verified; live lease strandable | **Adopted**: full-live-set equality for `E1_BOUNDARY`/`E3_BOUNDARY`/`RUNTIME_INVALIDITY` against the durable lease directory under the held lock; `RECOVERY_SETTLEMENT` subset with per-lease omission proofs (`TERMINAL_RECORD_DURABLE` or one named unresolved ancestor claim); validator duty 11; probes | amend. §1e, §1f.11; v2.3 §H4.2, §H5 |
| **Opus F2** — "runtime.py untouched" achievable but unpinned | **Adopted**: exact orchestration table — new `charge_batch_settlement` produces the post-cap state; existing `ledger.append`/`validate_ledger_event`/`build_process_record`/`validate_invalidity_record`/`validate_active_lease` produce artifacts; `settle_active_lease`/`settle_monotonic_delta` unchanged **and unused** for batch charges; pre-settlement lease binding and record-cumulative consequence pinned; control pins named | amend. §3d; v2.3 §H4.3 |
| **Opus F3** — pure method under-binds consumption | **Adopted (signature verbatim)**: `charge_batch_settlement(*, process_id, active_lease_sha256, value, envelope, authority) -> (TState, BatchSettlementAuthority)`; authority binds claim hash, ordered entries, consumed count, expected head/state; refuses stale head/state, consumed index, reorder, duplicate, omission, value change, claim substitution; returns successor | amend. §3b |
| **Opus F4** — re-derived tuple artifacts not byte-pinned | **Adopted**: deterministic timestamp table (every tuple field = claim `created_utc`, override-routed = override `created_utc`; no recovery clock) plus exact derivation rules for detail record, invalid event, and final records; two recovery runs hash-equal | amend. §4e |
| **Sol R1** — claim cannot re-derive its own accounting | **Adopted**: witness extended **into the claim itself** — global integers (`remaining_ns`, `known_total_ns`, `unknown_stream_count`, `unknown_pool_ns`, quotient, remainder), per-stream entries (global `stream_index`, `TIMELY_KNOWN|LATE_KNOWN|UNKNOWABLE`, known charge/share nullability, meter-evidence hash with a closed `t-meter-evidence.v1` artifact), per-process decomposition + aggregate, disposition/cause↔`batch_reason` relation table; twelve validator duties before authority exists | amend. §1a–§1g |
| **Sol R2** — claim order vs execution order contradiction; circular "crossing" predicate | **Adopted (first branch)**: one global ascending `process_sequence` order for claim array and execution, all batches; class ordering removed; crossing descriptive only, never inferred from evolving state; every worked ledger updated | amend. §2; v2.3 §H1, §H2 |
| **Sol R3** — shadowed claims; stale pre-state authority | **Adopted**: unresolved-claim registry scanned at every lock entry with a three-clause resolution predicate; unresolved claim blocks every new claim/admission/renewal/behavior (sole exception: disposition-authorized `RECOVERY_SETTLEMENT` naming the ancestor); restart reconstructs the next-step authority from the exact durable prefix — the pre-state match applies only before tuple 1 | amend. §3a–§3c |
| **Sol R4** — intra-tuple and pre-terminal crash cuts unspecified | **Adopted**: complete prefix automaton — every durable substep of valid and invalid tuples enumerated with exactly one next action (finish head/cache; finish the charged tuple without another charge; append next claimed charge; append the authorized terminal; archive; remain blocked); the final-removal→`T_ENVELOPE_EXHAUSTED` cut explicit; §3 record-first reconciliation (in-batch detail-awaiting-event is expected prefix, not orphan; head-behind outside batches unchanged); in-flight fault rule via the §5 override | amend. §4, §5; v2.3 §H2.7, §H3, §H4.4 |

Nothing was dropped; every repair is a schema, formula, table,
automaton row, API rule, or probe — no prose-only resolution.

## 2. Exact replacement index

Amendment v1.1 replaces v1 §2b (claim schema), §2d ordering sentence
and post-verifier list, §2e crash table; extends §2c (registry, API,
restart) and §3 (orchestration pins); adds §5 (override). Harness v2.3
replaces the v2.2 §A2 / v2.1 §A ordering paragraphs and the affected
worked ledgers (v2.1 batches 2, 5; v2.2 order notes), extends v2 §3a
and §10, narrows v2 §2c.6's final-event clause to non-batch closes,
and carries v2.2 §C (generational overdue-resume) forward unchanged.
Both files open with their full index tables.

## 3. Closed schemas (summary; normative text in the amendment)

- **Claim** `philosophia.officina.t-batch-settlement-claim.v1`
  (id unversioned — no instance or validator of the v1 key set ever
  existed): 18 keys incl. witness integers, `streams`, `processes`,
  `omitted`, `recovery_disposition_sha256`; path keyed by
  `pre_ledger_head_sha256`, no-replace, retained.
- **Meter evidence** `philosophia.officina.t-meter-evidence.v1`:
  content-addressed, pre-claim, non-outcome interval facts
  (`interval_start/end_reading_ns`, `backend_synchronized`, boot/clock
  identity); known charges recomputed as end − start.
- **Override**
  `philosophia.officina.t-batch-settlement-invalidity-override.v1`:
  keyed by claim hash (one ever, no-replace), binds validated prefix
  count, pre-override head/state, one dominant cause, remaining ids,
  claim-order replacement dispositions (all `T_PROCESS_INVALID`); a
  closed control artifact — **no tenth event and no signed
  event/schema change is required**, so no `BLOCKED` verdict applies.

## 4. Prefix automaton and deterministic timestamps

Amendment §4a/§4b give the canonical substep sequences
(invalid: charge → detail → `T_RUNTIME_INVALID` → INVALID record →
removal; valid: charge → record → `T_PROCESS_STOPPED` → removal;
terminal `T_ENVELOPE_EXHAUSTED` only for all-valid `E1_BOUNDARY`;
then archival) and a fourteen-row prefix table with exactly one next
action each, including Sol's demanded final-removal→terminal cut
(worked in v2.3 §H2.7). §4e pins every otherwise-variable field:
tuple timestamps = the claim's `created_utc` (override-routed work =
the override's `created_utc`); `created_utc` is checked ≥ the pre-head
timestamp at creation, so all derived values are ledger-monotone;
detail-record fields (`transaction_kind = T_BATCH_SETTLEMENT`,
`durable_step_index` = claim position, `affected_path_sha256` =
claim+lease(+override) hashes, liability from the durable lease) are
derivation rules, not choices. Recovery is byte-identical; no fresh
recovery clock exists.

## 5. Core API and restart authority

The method takes entry identity (`process_id`,
`active_lease_sha256`) plus `value` and refuses anything but the next
unconsumed claim entry at the expected head/state; the returned
successor advances the consumed cursor and state expectation. Restart
never requires the current state to equal the old pre-state: the
authority is reconstructed from the validated durable suffix after
`pre_ledger_entry_sha256` (charges matched to claim entries in order,
byte-exactly, including the deterministic timestamp), with
record-first invalidity on any non-conforming entry. The initial
pre-state/pre-head match gates only tuple 1.

## 6. Full-live-set and recovery-subset proofs

For the three full-set reasons the validator equates the claim's
process set with the verified `T_ACTIVE_LEASES/` directory contents
read under the same held lock epoch that writes the claim, and the
post-verifier re-checks it; a terminal event with a surviving live
lease is therefore unreachable (F1). For `RECOVERY_SETTLEMENT`,
`processes ∪ omitted` must equal that directory exactly, each omission
carrying either a verified durable terminal record or the hash of the
one named unresolved ancestor claim whose automaton (or override, or
superseding disposition) governs it — a live lease that is neither
enumerated nor proved covered refuses the claim, so none is silently
stranded.

## 7. Worked ledgers and two-implementer determinacy

v2.3 §H2 recomputes all affected ledgers under the single order with
complete witness integers: batch 2′ (95 s + 2×2.5 s to exact cap);
the mandated low-sequence-crossing example (70 s crossing appends
first, then 1 ns + 1 ns); the 60/60/60 counterexample
(`cap−40 → cap+20 → cap+80`); the mixed process (101 = 100 + 1); the
mixed multi-process (50/135/15 to exact cap); batch 4 (30 s/2 ns/1 ns);
and the all-valid E1 batch whose crash after the final removal resumes
with exactly the one authorized `T_ENVELOPE_EXHAUSTED`. Determinacy:
the claim freezes set, order, values, and dispositions; the witness
makes every value recomputable from closed meter facts; the API forces
consumption order at the core; the automaton and timestamp table force
every recovery byte; the registry excludes shadowing and nesting; the
override forces the one fault route. Two independent implementers now
derive identical terminal classifications, charges, artifact ordering,
and admission decisions; any residual divergence would be a concrete
output-changing contradiction for the final confirmation to name.

## 8. Bounded final-confirmation questions

**Opus (two):**
1. Do §3d's orchestration pins plus §H3/§4d keep `runtime.py`,
   `ledger.py`, and `checkpoint.py` byte-unchanged on every batch path
   (F2), and is the claim-authorized head/cache completion correctly
   scoped so that no silent-repair regression against the confirmed
   §3/§3a/C.4 record-first boundary exists?
2. Are the full-live-set equality and the `RECOVERY_SETTLEMENT`
   omission proofs (§1e/§1f.11) rejectable end-to-end — claim
   creation, post-verifier, and registry — such that the F1 stranded-
   lease terminal is unreachable in every reason class?

**Sol (two):**
1. Does the §1 witness make every claimed charge recomputable from
   closed non-outcome meter facts alone (R1) — `U`/quotient/remainder,
   shares by global `stream_index`, per-process aggregates,
   evidence-bound known intervals — with no path that trusts a bare
   `charge_ns`, and does the §1g relation table close the
   disposition/cause/`batch_reason` space?
2. Do the registry, single-use successor authority, prefix automaton,
   and override (§3–§5) exclude re-charge, abandonment, shadowing at
   an advanced prefix head, nested/competing overrides, and any
   non-byte-identical recovery, at **every** enumerated cut including
   the final-removal→exhaustion cut and a blocked override?

## 9. Negative authorization confirmation

This packet authorizes only: one literal bounded X/Y final
confirmation of these repairs, then — only after both confirmations —
Kirill's two ordered signatures
(`I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT`, then
`I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT`); after both, the §11
implementation and its bounded review. Created here: exactly the three
mandated files. Not created, not run, not authorized: any code or code
edit, `generic_harness.py`, any `accounting.py` change, any claim/
evidence/override/manifest/authorization instance, `runtime_control/`,
any activation, capability, world, learner, process, lease, entropy,
draft-manifest instance, E1/E2/E3 spend, or any T/Q/C datum, ledger
event, lock, escrow, outcome, or claim movement. No implementation
hash, reviewed HEAD, or production source set is pinned. No learner,
candidate, architecture, optimizer, training rule, device winner,
certificate numeric, Q predicate, alpha, margin, or scientific
endpoint is selected. T remains `NOT_ACTIVATED` at genesis; the
predecessor line remains immutable, `OPEN`, and
`BLOCKED_LEVEL1_FEASIBILITY`; T and Q remain permanently non-citable
for C1–C6; no prediction is made about any learner or about
Philosophia being proved, falsified, or bounded; the programme claim
remains `OPEN`. The next step is one bounded confirmation, not a new
design round.
