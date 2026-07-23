# Officina generic metered harness contract — v2.3 bounded correction

Status: `CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`. Carries
the complete harness contract — v2 as corrected by v2.1 and v2.2 —
forward verbatim except for the exact replacements below, applying the
harness-side consequences of the companion
`successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_CORRECTION.md`
(Opus F1..F4; Sol R1..R4). Prior versions are preserved unedited as
review evidence. Creates nothing executable; changes no code; the
contract token remains ineligible until the amendment token is signed
first. T remains `NOT_ACTIVATED`.

**Replacement index (everything else in v2/v2.1/v2.2 carries forward):**

| Locus | Action |
|---|---|
| v2.2 §A2 ordering paragraph ("all unknown-share-only and non-crossing known processes first … then every crossing process") | **replaced** by §H1 (one global ascending `process_sequence` order) |
| v2.1 §A "Ordering" paragraph (non-crossing-before-crossing; crossing-last rationale) | **replaced** by §H1; the "fails closed before charging" sentence stands only for a batch attempted **without** the frozen-batch authority (as v2.2 already narrowed) |
| v2.1 §A worked batches 2 and 5; v2.2 §A2 60/60/60 order note ("all crossing-class") and mixed multi-process order sentence; v2.2 §A3 batch-4 order note | **replaced** by §H2 (recomputed ledgers, one order, complete witness integers) |
| v2 §3a sentence "This is the sole silent completion" | **replaced** by §H3 (adds the claim-authorized batch head/cache completion; amendment §4d) |
| v2 §2c.6 clause "cumulative charge includes the final event" | **narrowed** to ordinary (non-batch) closes; batch closes per §H4.3 |
| v2 §10 matrix | **extended** by §H5 probes |
| v2.2 §C generational overdue-resume path | **unchanged and closed** — carried forward verbatim; nothing in this correction touches pause/resume |

## H1. One canonical batch order (Sol R2)

Every settlement batch — every `batch_reason`, zero or many
crossings — executes its per-process tuples in **exactly the claim's
`processes` array order: global ascending `process_sequence`.** The
claim array order and the execution order are identical by
construction. "Crossing"/"non-crossing" is descriptive commentary
only: it is never an ordering predicate, never a claim field, and
never inferred from evolving state. The frozen-batch authority makes
every claimed positive charge appendable regardless of the cap, so no
order-dependent representability exists; tuple adjacency
(each `T_RUNTIME_INVALID` the immediate successor of its own charge)
and one-positive-event-per-process are unchanged.

## H2. Recomputed worked ledgers (complete witness integers; cap = 604,800 device-s)

All batches below list the §1b/§1c witness values
(`remaining`, `K`, `m`, `U`, quotient `q`, remainder `r`) and are
independently recomputable from them; v2.1 batches 1 and 3 stand
unchanged (batch 1 has no pool; batch 3's single process needed no
reordering).

1. **Batch 2′ (replaces v2.1 batch 2).** `D0 = cap − 100 s`;
   P1 (seq 1) `LATE_KNOWN` 95 s; P2 (seq 4), P3 (seq 6) `UNKNOWABLE`.
   `remaining = 100 s`; `K = 95 s`; `m = 2`;
   `U = max(2 ns, 5 s) = 5 s`; `q = 2.5 s`; `r = 0` → shares
   2.5 s / 2.5 s. **Order P1 → P2 → P3** (ascending sequence): states
   `cap − 5 s` → `cap − 2.5 s` → `cap` exactly. Reason
   `RUNTIME_INVALIDITY`; all `T_PROCESS_INVALID`, one dominant cause;
   **G5, no exhaustion event**; cap retained as a numeric fact.
2. **Low-sequence crossing beside higher-sequence unknowables
   (replaces v2.1 batch 5).** `D0 = cap − 40 s`; P1 (seq 2)
   `LATE_KNOWN` 70 s; P2 (seq 5), P3 (seq 8) `UNKNOWABLE`.
   `remaining = 40 s`; `K = 70 s`; `remaining − K < 0` →
   `U = max(2 ns, ·) = 2 ns`; `q = 1 ns`; `r = 0` → shares 1/1 ns.
   **Order P1 → P2 → P3**: charge P1 70 s → `cap + 30 s` (**the
   crossing appends first; the batch authority permits it**); P2
   1 ns → `cap + 30 s + 1 ns`; P3 1 ns → `cap + 30 s + 2 ns`. Known
   overrun retained in full; G5; no exhaustion event. (Under v2.2's
   class order this batch ran P2, P3, P1; the class order is
   withdrawn.)
3. **60/60/60 (the verified counterexample).** `D0 = cap − 100 ns`;
   P1 (seq 3), P2 (seq 5), P3 (seq 9), each one `LATE_KNOWN` stream of
   60 ns (evidence-proved intervals). `remaining = 100 ns`;
   `K = 180 ns`; `m = 0`; `U = q = r = 0`. Order P1 → P2 → P3: states
   `cap − 40` → `cap + 20` → `cap + 80`. Reason
   `RECOVERY_SETTLEMENT` (deadline-missed recovery), all
   `T_PROCESS_INVALID`, dominant `PROCESS`; G5. (The "all
   crossing-class" note is deleted; from the frozen pre-state P1's
   charge does not cross — the label was descriptive anyway and no
   longer orders anything.)
4. **Mixed multi-process.** `D0 = cap − 200 ns`; P1 (seq 2)
   `LATE_KNOWN` 50 ns; P2 (seq 4) `LATE_KNOWN` 120 ns + one
   `UNKNOWABLE` stream; P3 (seq 6) one `UNKNOWABLE` stream.
   `remaining = 200 ns`; `K = 170 ns`; `m = 2`;
   `U = max(2, 30) = 30 ns`; `q = 15`; `r = 0` → shares 15/15 by
   ascending global `stream_index`. Events: P1 `50` (`cap − 150`),
   P2 `135` = 120 + 15 (`cap − 15`), P3 `15` (`cap` exactly) — the
   order is unchanged from v2.2 but is now *by sequence*, not by
   class. G5; no exhaustion event.
5. **Mixed single process (Sol's 50/100).** `remaining = 50 ns`;
   P (seq 7): s1 `LATE_KNOWN` 100 ns, s2 `UNKNOWABLE`. `K = 100`;
   `m = 1`; `U = max(1, −50) = 1 ns`; `q = 1`; `r = 0`. One event
   `charge_ns = 101` → `cap + 51 ns`; invalid tuple; G5. (Identical to
   v2.2 A1; restated with witness fields.)
6. **Batch 4 (order note updated only).** `D0 = cap − 30 s − 3 ns`;
   P1 (seq 1) `LATE_KNOWN` 30 s; P2 (seq 2) two `UNKNOWABLE` streams;
   P3 (seq 4) one `UNKNOWABLE`. `remaining = 30 s + 3 ns`; `K = 30 s`;
   `m = 3`; `U = max(3, 3) = 3 ns`; `q = 1`; `r = 0`. Order
   P1 → P2 → P3 (ascending sequence — numerically identical to
   v2.2's ledger): 30 s, 2 ns, 1 ns → `cap` exactly; G5.
7. **All-valid `E1_BOUNDARY` batch with a crash before the terminal.**
   `D0 = cap − 30 s`; P1 (seq 1) `TIMELY_KNOWN` 12 s; P2 (seq 6)
   `LATE_KNOWN` 20 s. `remaining = 30 s`; `K = 32 s`; `m = 0`;
   `U = q = r = 0`; dispositions both `T_PROCESS_E1_EXHAUSTED`,
   causes null. Ledger: charge P1 12 s (`cap − 18 s`) → valid record →
   `T_PROCESS_STOPPED` → removal; charge P2 20 s (`cap + 2 s`) →
   valid record → `T_PROCESS_STOPPED` → removal; **crash here** (after
   the final valid removal, before `T_ENVELOPE_EXHAUSTED`). At the
   next lock entry the registry finds the unresolved claim,
   reconstructs the prefix (two complete tuples, terminal absent), and
   the **sole next action is appending the one already-authorized
   `T_ENVELOPE_EXHAUSTED`** (timestamp = the claim's `created_utc`;
   post-state `cap + 2 s`) → G7 → archival commit. Never a re-charge,
   never archival first, never a new claim.

## H3. §3a extension (replaces the "sole silent completion" sentence)

The §3a cache/lease-successor completion keeps its exact original
scope. In addition, **within one unresolved batch-settlement claim**,
a durable ledger suffix that byte-matches a valid prefix of the
claim's canonical automaton may have its lagging external head and/or
state cache completed idempotently at the next lock entry under the
reconstructed batch authority (amendment §4d). This is
claim-authorized, not silent: the durable claim pre-authorizes exactly
that entry, and any non-matching suffix remains record-first
invalidity with head repair only under the signed recovery route
(v2.1 C.4 unchanged outside batches). These two are the only
non-invalidity completions; everything else in §3 carries forward.

## H4. Witness, completeness, and terminal references (binding)

1. **Per-stream witness and per-process aggregation.** Every
   settlement batch is constructed and verified per amendment §1: the
   claim's `streams` array (per-stream classification, known charge or
   share, meter-evidence hash) plus its `processes` decomposition
   replace all prose accounting; the v2.1 §A aggregation rule
   (at most one positive `T_DEVICE_TIME_CHARGED` per process, bound to
   the pre-settlement lease) is unchanged, and every `charge_ns` is
   now recomputable from closed non-outcome meter facts — never
   trusted.
2. **Full-live-set rule (Opus F1).** For `E1_BOUNDARY`,
   `E3_BOUNDARY`, and `RUNTIME_INVALIDITY` the claim's process set
   equals **exactly the entire durable active-lease set at the
   pre-head**; for `RECOVERY_SETTLEMENT` the enumerated-plus-omitted
   union equals it, with each omission proved per amendment §1e. No
   live lease can be silently stranded; a terminal event over a
   surviving live lease is unreachable.
3. **Batch-close lease binding.** Batch charge events bind the durable
   pre-settlement lease hash; a batch-closed process record's
   `cumulative_charge_ns` therefore equals the pre-settlement lease's
   cumulative, with the final claimed charge carried by the bound
   `final_charge_event_sha256` (total = record cumulative + final
   charge, witness-checked). Ordinary voluntary/resource closes keep
   the v2 §2c.6 settled-lease binding, whose "includes the final
   event" clause now applies to them only.
4. **Prefix and override terminal behavior.** Batch crash recovery
   follows the amendment §4 automaton exclusively (one next action per
   durable prefix; deterministic timestamps; byte-identical
   re-derivation). An in-flight verified infrastructure fault on an
   all-valid claim follows the amendment §5 override: prefix
   immutable, remaining processes invalid with the one dominant cause,
   **no valid exhaustion event, final route G5**; a blocked override
   blocks the runtime — no improvised route exists.
5. **Generational overdue-resume (v2.2 §C)** is unchanged and closed;
   batches do not interact with pause/resume (pause requires zero
   live leases; a batch requires the lock and settles leases to zero
   before any pause could begin).

## H5. Added §10 probes

Claim witness: recomputation of `U`/`q`/`r` and every share; process
aggregates vs stream sums; tampered `charge_ns` vs evidence →
rejection; duplicate/missing/extra stream index, process id, evidence
hash → rejection; every enum/nullability violation → rejection.
Completeness: omitted live lease under each of the three full-set
reasons → claim refused; `RECOVERY_SETTLEMENT` omission proofs
(terminal-record and named-ancestor branches; a stranded live lease →
refusal). Order: low-sequence crossing first (ledger H2.2 forced
bit-exactly); claim-array/execution divergence → post-verifier
rejection. Registry: unresolved claim blocks new claim/admission/
renewal/behavior; shadow claim at an advanced prefix head → refused;
`RECOVERY_SETTLEMENT` creation allowed only under a verified
disposition naming the ancestor. Core API: refusal on stale
head/state, consumed index, reorder, duplicate, omitted process, value
change, claim substitution; successor-authority chaining; restart
reconstruction from every prefix of H2.7 and of an invalid batch.
Automaton: crash injected at **every** §4a substep of valid and
invalid tuples (charge/head lag, detail, event, record, removal,
terminal, archival) → exactly the one pinned next action;
byte-identical re-derived detail/event/record artifacts (hash-equal
across two recovery runs); the H2.7 final-removal→exhaustion cut.
Override: creation before further tuple work; no-replace second
override → refused; already-charged vs uncharged remaining tuples;
G5 terminal with no valid event; blocked-override → runtime blocked.

## Compatibility (correction level)

| Element | Classification |
|---|---|
| signed events (nine), runtime schemas, constants, roots (pinned tuple), phase rules, T bands, WP-3/WP-4, WP-6/WP-9 ownership | **unchanged** |
| amendment surfaces (accounting authority + method; claim/evidence/override schemas; registry; automaton) | **companion core amendment** — token 1 |
| H1 order, H2 ledgers, H3 extension, H4 bindings, H5 probes | **deterministic harness clarifications** — token 2 scope |

No learner, candidate, architecture, optimizer, device winner,
breathing numeric, Q predicate, alpha, endpoint, margin, or scientific
result is selected; nothing executable is created; T and Q remain
permanently non-citable for C1–C6; the programme claim remains `OPEN`.
