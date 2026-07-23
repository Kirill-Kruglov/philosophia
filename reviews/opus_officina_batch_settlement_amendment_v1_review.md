REVISE_OFFICINA_BATCH_SETTLEMENT_AMENDMENT_V1_XLINE

# Opus 4.8 X-line — Officina batch-settlement core amendment v1 review

Reviewer: Opus 4.8 (X-line, adversarial metering-core implementability).
Repository: `/home/master/llm_projects/philosophia`. Bounded packet:
`successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md`,
`successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_2_CORRECTION.md`,
`reviews/fable_officina_harness_v2_2_core_amendment_closure.md`, against the
current `accounting.py`/`runtime.py`/`ledger.py` constructors, the signed
activation protocol, my confirmed M-1..M-6, and Sol's A1/A2/A3/C. **I edited no
existing file, created exactly one file (this review), committed nothing, ran only
read-only reads/greps and in-memory arithmetic on non-production `TState` values,
implemented nothing, created no code/manifest/authorization/runtime artifact,
activated no T, and spent no E1/E2/E3.** The real tree is pristine and
`NOT_ACTIVATED` (`runtime/` = `{T_RUNTIME.lock}`). No scientific or learner choice
is touched.

## Verdict

**REVISE.** The amendment is **genuinely necessary and fundamentally sound**: I
independently reproduced the multi-cross impossibility, and the frozen-batch
authority is the honest, correctly-scoped fix. But two concrete gaps in the
amendment's own §2b/§2d/§3 leave the future authority under-determined for
**rejectability** and for the **"runtime.py untouched" scope claim**, and two
further tightenings are needed for single-valued crash recovery and the pure-method
surface. All are localized to the amendment (v2.2's A1/A2/A3/C are confirmable as
written); none reopens the X-line-confirmed C-1..C-4/R5..R12/M-1..M-6 material or
any scientific/learner cell.

## Attack 1 — impossibility reproduced; amendment necessary (CONFIRMED)

Against the current `TState.charge_device_nanoseconds` (which refuses once
`exhausted()`, i.e. `device_nanoseconds ≥ cap`, before any charge), `D0 = cap −
100 ns` with three proved case-(b) charges of 60 ns is representable in **0 of 6
permutations**: the first reaches `cap − 40`, the second `cap + 20` (exhausted),
the third is refused. A single crossing (e.g. 30 then 60-last) appends; a second
does not. The signed case-(b) full-interval rule plus the process-scoped, no-
aggregation event/lease binding therefore cannot be honored through the unchanged
core when more than one known-late process must charge past the cap, and no
pre-batch invariant excludes it (each 60 ns reservation fit the 100 ns remainder at
admission; the actual intervals legally exceeded it). **My v2.1 M-1 closure was
sound only for ≤ 1 crossing;** the amendment's loud withdrawal of v2.1's
unconditional no-core-amendment classification is correct and honest.

## Attack 2 — `t-batch-settlement-claim.v1` audit (one mandatory gap)

Keys `{schema, scientific_outcome(false), batch_reason, pre_ledger_entry_sha256,
pre_ledger_head_sha256, pre_state_sha256, processes, dominant_cause, created_utc}`,
path `runtime/T_BATCH_SETTLEMENT_CLAIMS/<pre_ledger_head_sha256>.json` (no-replace,
one batch per ledger position, retained), the `processes` entry shape
`{process_id, process_sequence, active_lease_sha256, charge_ns, disposition,
invalid_cause}`, `batch_reason`/`invalid_cause`/`dominant_cause` enums, and
fsync/post-verify-before-charge are all exact and sufficient to bind a batch to its
pre-head/state, bind each charge to its exact pre-settlement lease, and (with the
post-verifier's conservation + per-entry consumption + per-event process/lease
binding) to **reject** value substitution, reorder, duplicate, extra, and missing
charges. Byte-level reconstruction is determinate.

**Finding F1 (mandatory) — claim completeness is not pinned or verified.** §2d
proves "every *enumerated* lease reached its mandated terminal and removal"
(enumerated ⊆ settled) but never that `processes` **equals the full set of active
leases at `pre_ledger_head_sha256`** (active ⊆ enumerated). For `E1_BOUNDARY`,
`E3_BOUNDARY`, and `RUNTIME_INVALIDITY` — where every live lease must settle — a
batch that omits a live lease is **not rejectable** by the stated duties: it would
strand a live lease and still emit the terminal (e.g. a G7 `T_ENVELOPE_EXHAUSTED`
with a live lease surviving). **Repair:** pin that for those three reasons
`processes` enumerates exactly the durable active-lease set at
`pre_ledger_head_sha256` (sorted by `process_sequence`), and add a post-verifier
check of the claim's process set against the durable lease directory; for
`RECOVERY_SETTLEMENT` state precisely which subset is admissible and how the
remainder's liveness is verified.

## Attack 3 — future authority operationally single-valued (one tightening)

The **result** is single-valued: the claim's sorted `processes` order + indivisible
tuples fix the ledger, and the §2d post-verifier rejects any deviation because each
`T_DEVICE_TIME_CHARGED` carries `process_id`, `active_lease_sha256`, and `charge_ns`
that must match its claim entry, and conservation (`post E1 = pre + Σ claimed`)
catches over/under-consumption even when charges collide (60/60/60).

**Finding F3 (tightening) — the pure-method signature under-binds consumption.**
`TState.charge_batch_settlement(value, envelope, authority)` gates only on
value-membership; with equal claimed charges it cannot, at the **core** level,
select the specific claim entry, enforce the next-unconsumed-in-order entry, or
bound the batch to the claimed multiset — it defers all of that to the post-verifier
after durable appends. **Smallest exact surface:** have the method take the entry
identity and represent consumption, e.g.
`charge_batch_settlement(*, process_id, active_lease_sha256, value, envelope,
authority) -> (TState, BatchSettlementAuthority)`, where `authority` carries the
frozen claim entries plus a consumed cursor; the call **refuses** unless
`(process_id, active_lease_sha256, value)` equals the next unconsumed entry in the
claim's sorted order, and returns a successor authority with that entry marked
consumed (no reuse, no reorder, no duplicate, no value substitution, no
over-budget append) — so the core, not only the post-verifier, is fail-closed.

## Attack 4 — crash cuts (sound distinguishability; one tightening)

Recovery distinguishes an already-consumed charge from a missing one using only
durable facts: each claimed process's `T_DEVICE_TIME_CHARGED` carries its
`process_id` (I verified the event data carries `process_id`+`active_lease_sha256`),
so recovery matches ledger charges since the pre-head to claim entries by
`process_id`, completes **only** the missing claim-enumerated tuples in order,
never re-charges an already-appended entry, and preserves immediate ancestry
(`T_RUNTIME_INVALID.previous = charge hash`, `sequence+1`) because the durable
charge is the current head. Complete-or-block with no behavior resume is coherent
and loop-free (an uncompletable batch routes to record-first invalidity + signed
recovery disposition). **Finding F4 (tightening):** for the "between tuples" cut
where the charge is durable but the detail record / `T_RUNTIME_INVALID` must be
re-derived, pin that every tuple artifact's content — `observed_utc`, the
`T_RUNTIME_INVALID` timestamp, `closed_utc` — is a deterministic function of durable
facts (the frozen claim and the durable charge event), so recovery reconstructs
**byte-identical** artifacts and two implementers (or two recovery attempts) emit
the same hashes; `build_process_record` already couples these timestamps to each
other but not to a durable source.

## Attack 5 — no weakening / runtime.py unchanged / pins (one mandatory gap)

Ordinary post-E1 refusal is **not** weakened: the amendment adds a *separate*
method and leaves `charge_device_nanoseconds` byte-for-byte unchanged; it authorizes
no admission/renewal/behavior-capable work and adds **no** field to any signed
event/runtime schema (auditability via the closed claim artifact; no tenth event).
`accounting.py` is on the immutable-control pin (`activation.py:124`,
`IMMUTABLE_CONTROL_PATHS`), so the change is correctly a reviewed-control change
captured by the existing pin and re-hashed at activation; the production manifest is
named for implementation review.

**Finding F2 (mandatory) — the "runtime.py untouched" claim is achievable but not
pinned, risking an unnamed core change.** I verified that `TState.__post_init__`,
`build_process_record`, `validate_ledger_event` (`T_DEVICE_TIME_CHARGED`),
`validate_active_lease`, and `ledger.append` impose **no** upper-cap ceiling, so an
above-cap charge event / state / record **is** representable via the existing
constructors and `runtime.py` need not change. **But** both sanctioned charge
producers — `runtime.py:settle_active_lease` and `settle_monotonic_delta` — route
through `charge_device_nanoseconds` (`runtime.py:283`) and therefore refuse the
post-cap batch charge. The amendment never states that batch charges must compute
their post-cap `t_state` via the new `charge_batch_settlement` and build the
`T_DEVICE_TIME_CHARGED` event / process record / initial lease via the existing pure
constructors, **bypassing** `settle_active_lease`/`settle_monotonic_delta`. Without
that pin, an implementer following today's only sanctioned charge path hits the
refusal and is driven either to modify `runtime.py` (an **unnamed** core change
contradicting the amendment's own scope) or to invent an undocumented bypass — two
implementers can diverge on whether `runtime.py` changes. **Repair:** state the
batch charge-production orchestration explicitly (new method for state; existing
`T_DEVICE_TIME_CHARGED`/`build_process_record`/`build_active_lease` for artifacts;
`settle_active_lease`/`settle_monotonic_delta` unchanged and unused for post-cap
charges), and record that no existing constructor imposes a cap ceiling (verified),
so "runtime.py untouched" is sound and determinate.

## Attack 6 — v2.2 A1/A2/A3 + generational C vs M-1..M-6 (CONFIRMED)

All recomputed with integer-exact inputs: **A1** per-stream classification keeps
every proved interval in `K` and only unknowable streams in `m` (50/100 ns → one
event of **101 ns**, not clipped to 50) — this actually *corrects* a latent clipping
error in my own v2.1 whole-process-unknowable reading, and preserves M-1's ≥1-ns
floor and M-3's one-event-per-process. **A2** batch order (unknown/non-crossing
ascending, then crossing ascending) with indivisible tuples: the 60/60/60 ledger
runs `cap−40 → cap+20 → cap+80`, exactly **one** charge (P3) appending from an
already-≥cap state (verified), G5, no exhaustion event; preserves M-2
(exhaustion only on all-valid E1) and M-3 (adjacency inside every tuple). **A3**
batches 3/4 recompute exactly (`U=4`→2/2→4 ns; `U=3`→1/1/1) to `cap` via the
**unknown pool**, with "no crossing" correctly narrowed to "no *known* crossing."
**C** generational pending-resume path keyed by `pause_event_sha256` (prior
generations retained, distinct hashes, per-generation cuts) closes the
second-overdue-resume lifecycle and *fixes the fixed-path recurrence I flagged
non-blocking in the v2.1 confirmation*, with M-6's original-checkpoint immutability
and verifier relation intact. A2's fault-free all-valid E1 batch still emits one
final `T_ENVELOPE_EXHAUSTED` → G7 (B.1). All compatible with M-1..M-6.

## Attack 7 — two-implementer determinacy

With F1–F4 applied, two implementers emit identical claims, accounting states,
ledger tuples, crash recovery, and terminals. **Without them**, the concrete
output/rejectability-changing gaps are: a batch omitting a live lease is not
rejected (F1); divergence on whether `runtime.py` must change to produce post-cap
charges (F2); and non-byte-identical re-derived tuple artifacts after a between-
tuples crash (F4). F3 is a core-vs-post-verifier hardening (the result is already
single-valued via the post-verifier). All four are localized to the amendment's
§2b/§2d/§3; v2.2 A1/A2/A3/C and the confirmed prior material are untouched. This is
a bounded repair round, not a redesign.

## Gate and negative authorization

REVISE: a v1.1 amendment applying F1–F4 (with the concurrent Y-line confirmation)
would, on my read, be X-line approvable and two-implementer-deterministic. This
review authorizes **nothing** beyond, upon a future positive X/Y confirmation,
Kirill's **two ordered** signatures
(`I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT` then
`I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT`); the prior conditional harness
signature is void and not claimed. It authorizes **no** code, implementation,
`accounting.py`/`generic_harness.py` change, manifest, activation authorization or
activation, capability, world, learner, process, lease, entropy, batch-claim
instance, E1/E2/E3 spend, ledger event, or any T/Q/C datum, outcome, or claim
movement. No implementation hash, reviewed HEAD, or production source set is pinned
here.

T remains `NOT_ACTIVATED` at genesis; the predecessor line remains immutable,
`OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`; T and Q remain permanently non-citable for
C1–C6; invalidity, author stop, and E1 exhaustion remain non-scientific
destinations; WP-6/WP-9 ownership and every negative destination are unchanged; only
a valid, independently locked C execution may ever move an Officina claim. No
prediction is made about any learner or about Philosophia being proved, falsified,
or bounded; the programme claim remains `OPEN`.

I edited no existing file, created exactly one new file (this review), authorized
nothing, activated no T state, implemented no core change, and committed nothing.
`essay/OUTLINE.md` untouched. My actions were reading the amendment, v2.2, Fable's
closure, my prior confirmations, and the current constructors, and running the
read-only reproduction/arithmetic/pin checks above.

— Opus 4.8, X-line. No scientific outcome is asserted or predicted in this
document.
