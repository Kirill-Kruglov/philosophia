READY_FOR_OFFICINA_GENERIC_HARNESS_V2_1_FINAL_CONFIRMATION

# Fable 5 — Officina generic harness contract v2.1 closure memo

Author: Fable 5. Companion to
`successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_1_CORRECTION.md`
(bounded correction; v2 carries forward verbatim except the stated
replacement index; v2, both confirmations, and all captures preserved
unedited). Inputs: Opus (`REVISE…_V2_XLINE`, M-1..M-6) and Sol
(`REVISE…_V2_YLINE`, corrections A..E); both confirm C-1..C-4/R5..R12
and the majority of Sol 1..14 closed — none reopened. The C4 verifier
gate is independently closed at `fbac493`. Exactly two files created;
nothing else changed; nothing committed or run.

## 1. One-to-one disposition table

| Finding | Disposition | v2.1 |
|---|---|---|
| **Opus M-1** (Crit) — zero-share/R=0 stream unclosable by the pinned constructor | **Adopted, code-compatible route**: zero-share branch and Example C deleted; `U = max(m ns, remaining − K)` guarantees ≥ 1 ns per unknowable stream; unknown/non-crossing tuples precede the crossing charge (append-refusal past cap makes this the only order); fail-closed before charging if the floor is unrepresentable; **no zero-charge constructor added** | §A |
| **Opus M-2** (Crit) / Sol B.4 — exhaustion vs invalidity not single-valued | **Adopted**: `T_ENVELOPE_EXHAUSTED` only when every stream in the crossing settlement closes valid (B.1); invalid batches retain cap-level numeric facts, append no valid event, terminal G5; Example B corrected (G5, no exhaustion event) | §B.1/B.4 |
| **Opus M-3** / Sol B.3 — batch order vs charge→invalid adjacency | **Adopted**: indivisible per-process tuples, strictly interleaved, invalid event = immediate successor of its own charge; "all charges first" wording removed | §A, §B.3 |
| **Opus M-4** / Sol B.3 — collateral sibling cause unspecified | **Adopted**: sibling inherits the batch's dominant triggering cause per the §2a precedence; one cause per record/event | §B.3 |
| **Opus M-5** / **Sol D** — "lists every observed cause" unrepresentable | **Adopted**: sentence deleted; single signed `invalid_cause`; co-observed causes test-only, never a field, never recovery input | §D |
| **Opus M-6** / Sol C — second pause collides with immutable helpers; G4 power-loss unresumable | **Adopted**: original checkpoint immutable; **new** pending-resume checkpoint artifact (`ledger_head_before` = first pause entry hash; byte-identical payload hashes); second pause via the generic §3 transaction, not the helper; verifier relation, archive set, and crash cuts pinned; G4 power-loss re-enters G4 | §C.2 |
| **Sol A** — settlement not representable in signed lease/event | **Adopted verbatim in substance**: per-stream computation then per-process aggregation; at most one positive event per process against its pre-settlement lease; coextensive-cursor default with adapter-proved summation else whole-process unknowable; no `stream_index` field | §A |
| **Sol B** — boundary artifact routes incomplete | **Adopted verbatim in substance**: B.1 (E1: per-process `T_PROCESS_E1_EXHAUSTED` record → stopped → removal, ascending; one exhaustion event; G7), B.2 (E3: `T_PROCESS_E3_DUE` records; G2; review only), B.3, B.4; exhaustive B.5 pair table | §B |
| **Sol C** — clean resume/recovery not durable | **Adopted**: C.1 one-lock-epoch rule, G3→G1 durable only via `T_PROCESS_STARTED` on the verified head, crash cuts; C.3 full recovery-disposition schema/path/bindings/tokens/ordering/archive/predicate/cuts; readmission without a tenth event (next `T_PROCESS_STARTED` is the first post-recovery entry); C.4 deferred-event clarification | §C |
| **Sol E** — decision inputs not enumerated | **Adopted**: five closed schemas with exact ids/keys/enums; no free text; no learner-derived hash values; signed schemas reference them only via already-permitted hashes; author cognition honestly left open, machine input closed | §E |

Nothing dropped; every repair is a formula, ordering, schema, route,
or probe — no prose-only resolution. The strict reconciliation asked
for (code-compatible, no core amendment) is exactly what landed.

## 2. Replacement index

As tabled in the correction's header: §2a cause-list sentence deleted;
§2c.8 replaced by B.1/B.4; §2c.12b replaced by B.3; §4c never-zero
sentence replaced by the §A floor; §4d wholly replaced by §A; §6b
replaced by C.1/C.2; §6c replaced by C.3; §7 completed by §E; §10
extended by §F; closure Examples B/C superseded by the §A worked
batches. All other v2 text carries forward verbatim.

## 3. Accounting proofs and worked batches

Conservation: `Σ share_i = U` exactly (integer quotient + remainder
nanoseconds); `U ≥ m ⇒ floor(U/m) ≥ 1` — every unknowable stream
positive; when `remaining − K ≥ m ns`, post-total = `D0 + K + U =
cap` exactly; when the known crossing exceeds `remaining`, post-total
= `D0 + K + m ns` — the cap is exceeded only by the retained known
overrun plus the necessary conservative floor, and the pool is
debited once, never per lease. The five worked batches (§A 1–5) force:
per-process single events; unknown-first/crossing-last order (batch 5
shows why: after the cap no charge can append); one-process
multi-stream aggregation (batch 3); invalid-batch terminals with no
exhaustion event (batches 2, 5); all in integer nanoseconds.

## 4. Complete boundary/event-order table

B.1–B.4 give the four base routes; B.5 fixes one route for every
compound pair (E1+E3; E1/E3 × author-stop/pause/close; invalidity ×
everything; multi-cause single process; one-fault + healthy siblings).
Terminality: G7 only via B.1; G2 only via B.2; G5 only via B.3/B.4
with `G5→G5` legal; no valid event under unresolved invalidity; no
`T_PROCESS_STOPPED` in an invalid batch. Together with v2 §2c
(unchanged transitions 1–7, 9–11, 13–14) the machine is exclusive and
total.

## 5. New closed artifacts and compatibility

New generic-harness artifacts (not runtime events, not signed-schema
changes): `philosophia.officina.t-pending-resume-checkpoint.v1`
(`runtime/T_PENDING_RESUME_CHECKPOINT.json`),
`philosophia.officina.t-recovery-disposition.v1`
(`runtime/T_RECOVERY_DISPOSITIONS/<invalidity_event_sha256>.json`),
and the five decision schemas of §E. Compatibility (correction §G): no
signed event, runtime schema, constant, root, phase rule, or
metering-core constructor changes; the aggregation/ordering/route
clauses are deterministic clarifications forced by the immutable
constructors; the deleted cause-list sentence and corrected examples
are repairs of non-derivable text back toward the signed schema. **No
amendment is required and none is hidden**; had one been unavoidable
the correction would have returned `BLOCKED` and named it.

## 6. Two-implementer determinacy checklist

- **Charge-event counts/values:** forced — per-process aggregation,
  integer U-formula, deterministic stream order (✓ §A).
- **Tuple/event ordering and hashes:** forced — interleaved
  indivisible tuples, ascending sequence, crossing last, adjacency to
  the immutable constructor (✓ §A/§B.3).
- **Terminal state per compound boundary:** forced — exactly one B
  route per pair (✓ §B.5).
- **Invalid cause and artifact key sets:** forced — single
  precedence-selected cause; exact schemas (✓ §D/§E/§C).
- **Pause/resume/recovery admission:** forced — durable artifacts and
  the C.3 predicate; in-memory state never admits (✓ §C).

## 7. Bounded yes/no questions

**Opus (two):**
1. Do §A and §B close M-1..M-5 exactly — every unknowable live stream
   positively charged before the crossing, tuples interleaved per the
   pinned adjacency, exhaustion only on all-valid settlements,
   collateral cause inherited, single-cause schema preserved — with no
   metering-core change and no path a second implementer could take
   differently?
2. Does §C.2 close M-6 — immutable original checkpoint, fresh pending
   artifact bound to the first pause entry, second pause via the
   generic transaction, G4 power-loss resumable — with every crash cut
   pinned?

**Sol (two):**
1. Do §A's aggregation/cursor/pool rules and the five worked batches
   land your correction A exactly (representable in the signed
   lease/event, `U = max(m ns, remaining − K)`, unknown-first order,
   fail-closed floor), and do §B routes land correction B including
   the retained-numeric-facts rule of B.4?
2. Do §C's clean-resume lock-epoch rule, the pending-checkpoint
   relation, the full recovery-disposition schema and predicate, and
   §E's five enumerated decision schemas land corrections C and E —
   closed inputs only, no free text, no learner-derived values, no
   tenth event, fresh ids?

## 8. Negative authorization surface and confirmation

This correction and memo authorize only: one literal bounded final
confirmation by each line, then Kirill's contract signature
(`I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT`). No new design round is
authorized. Created here: exactly the two mandated files. Not created,
not run, not authorized: any code or amendment to `runtime.py`;
`generic_harness.py`; any CLI, production manifest, or
`runtime_control/`; any activation authorization or activation; any
capability, world, learner, process, lease; entropy; any
draft-manifest instance; E1/E2/E3 spend; any T/Q/C datum, ledger
event, root, lock, escrow, outcome, or claim movement. No
implementation hash, reviewed HEAD, or production source set pinned.
No learner, candidate, architecture, optimizer, device winner,
breathing threshold, Q predicate, alpha, endpoint, margin, or
scientific result chosen; WP-6/WP-9 ownership and all negative
destinations unchanged. T remains `NOT_ACTIVATED` at genesis; the
predecessor line remains immutable, `OPEN`, and
`BLOCKED_LEVEL1_FEASIBILITY`; T and Q remain permanently non-citable
for C1–C6; no prediction is made about any learner or about
Philosophia being proved, falsified, or bounded; the programme claim
remains `OPEN`.
