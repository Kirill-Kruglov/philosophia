# Officina generic metered harness contract — v2.2 bounded correction

Status: `CANDIDATE_FOR_XY_REVIEW_NOT_AUTHORIZED`. Carries the v2
contract as corrected by v2.1 forward verbatim except the exact
replacements below, applying Sol's final-confirmation corrections
A1/A2/A3/C with the X-line-confirmed material untouched. Depends on
the companion
`successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md`; the
contract token is not eligible before that amendment is reviewed and
signed. Creates nothing executable; changes no code; preserves v2 and
v2.1 unedited as review evidence; T remains `NOT_ACTIVATED`.

**Replacement index (all other v2/v2.1 text carries forward):**

| v2.1 locus | Action |
|---|---|
| §A cursor rule ("ambiguity selects the unknowable case for the whole process") | **replaced** by §A1 (per-stream classification) |
| §A ordering paragraph ("the final known case-(b) tuple whose charge crosses E1"; single-crossing assumption) | **replaced** by §A2 (frozen-batch order, multiple crossings) |
| §A worked batches 3 and 4 | **replaced** by §A3 (complete integer inputs) |
| §A "fail closed before charging if the floor is unrepresentable" | **narrowed**: applies only to a batch attempted without the frozen-batch authority; with the authority every claimed positive charge is representable |
| §C.2 singleton path `runtime/T_PENDING_RESUME_CHECKPOINT.json` | **replaced** by §C's generational path |
| §G "no metering-core amendment; no zero-charge constructor added" | **superseded**: the zero-charge half stands (no such constructor exists); the no-core-amendment half is withdrawn in favor of the explicit, separately signed batch-settlement amendment |

## A1. Mixed known/unknown streams (per-stream classification)

Classification is **per stream**, always. Every proved case-(a)/(b)
interval remains in `K`; only genuinely unknowable streams enter `m`
and receive unknown-pool shares. If any stream of a process is
unknowable, the **process** takes the invalid route — but its known
sibling charges are preserved, never erased or reclassified: the
process's one `T_DEVICE_TIME_CHARGED` aggregates **all its known
charges plus all its unknown shares**. Non-coextensive proved streams
use adapter-proved individual intervals summed into that one event;
ambiguity affects **only the ambiguous streams** (they join `m`), not
proved siblings.

**Mixed integer example (Sol's 50/100 ns case).** `remaining = 50 ns`.
Process P (sequence 7): stream s1 proved late 100 ns; stream s2
unknowable. Then `K = 100`, `m = 1`,
`U = max(1 ns, remaining − K = −50) = 1 ns`. P's single event:
`charge_ns = 101 ns` (100 known + 1 share), bound to P's
pre-settlement lease. Post-state: `D0 + 101 ns = cap + 51 ns` — the
proved interval retained in full, not clipped to 50. Terminal: invalid
batch → tuple `[charge 101 → detail record → T_RUNTIME_INVALID →
INVALID record → verified lease removal]`, cause per precedence;
**G5, no exhaustion event**. (The whole-process-unknowable reading,
which would have charged 50 ns and clipped a proved interval, is
withdrawn.)

## A2. Multiple crossings (frozen-batch authority)

The single-crossing-last assumption is **withdrawn**. Every boundary
or invalidity settlement that may append more than one process charge
executes as one **frozen batch** under the companion core amendment:
claim first (all per-process charges computed and frozen), then
deterministic per-process tuples.

**Order (zero, one, or many crossings):** all unknown-share-only and
non-crossing known processes first, ascending `process_sequence`; then
every crossing process, ascending `process_sequence`. Adjacency is
preserved inside every tuple (each invalid event is the immediate
successor of its own charge); every known charge is full; exactly one
positive event per process; invalidity dominance holds; **an invalid
batch appends no valid exhaustion/stop/pause event** (numeric E1/E3
facts retained in the invalid post-states). **A fault-free all-valid
E1 batch still emits exactly one final `T_ENVELOPE_EXHAUSTED` after
every valid per-process record → `T_PROCESS_STOPPED` → removal**, per
v2.1 B.1, now via the same batch authority when more than one charge
must append.

**Worked ledger — three processes, 60/60/60 ns, `remaining = 100 ns`
(the verified counterexample).** `D0 = cap − 100`. Claim enumerates
P1 (seq 3), P2 (seq 5), P3 (seq 9), each `charge_ns = 60`,
dispositions `T_PROCESS_INVALID` (recovery settlement), dominant cause
`PROCESS`. Order P1 → P2 → P3 (all crossing-class, ascending
sequence). Ledger: `charge P1 (60)` → state `cap − 40` → P1 detail →
`T_RUNTIME_INVALID` → P1 INVALID record → removal; `charge P2 (60)` →
state `cap + 20` (**first crossing; batch authority permits the
append**) → P2 tuple; `charge P3 (60)` → state `cap + 80` (**post-cap
append, same batch**) → P3 tuple. Final aggregate `cap + 80 ns`; every
known charge full; terminal **G5**, no exhaustion event. Under the
unchanged ordinary core this batch had zero representable orders.

**Mixed multi-process example.** `D0 = cap − 200 ns`; P1 (seq 2)
proved non-crossing 50 ns; P2 (seq 4) mixed — known 120 ns + one
unknowable stream; P3 (seq 6) single unknowable stream. `K = 170`,
`m = 2`, `U = max(2, 200 − 170) = 30 ns` → shares 15/15. Events: P1
`50` (state `cap − 150`), P2 `135` (120 + 15; state `cap − 15`), P3
`15` (state `cap` exactly). Order: P1 (non-crossing) first, then P2,
P3 ascending sequence among the remainder. Invalid batch (unknowables
present) → three invalid tuples, **G5**, no exhaustion event;
post-state `device_nanoseconds = cap` retained as a numeric fact.

## A3. Recomputable worked batches (replaces v2.1 batches 3 and 4)

- **Batch 3 (one process, two unknowable streams).**
  `D0 = cap − 4 ns` → `remaining = 4 ns`; `K = 0`; `m = 2`;
  `U = max(2, 4) = 4 ns` → shares 2/2 → **one** process event of
  `4 ns`. Post-state = `cap` exactly; terminal G5 (invalid batch);
  **no known crossing — the cap is reached through the unknown pool**,
  and that distinction is now stated wherever "no crossing" appeared.
- **Batch 4 (three processes).** `D0 = cap − 30 s − 3 ns` →
  `remaining = 30 s + 3 ns`. P1 (seq 1) known 30 s; P2 (seq 2) two
  unknowable streams; P3 (seq 4) one unknowable stream. `K = 30 s`;
  `m = 3`; `U = max(3 ns, 3 ns) = 3 ns` → shares 1/1/1 → events: P1
  `30 s`, P2 `2 ns`, P3 `1 ns` (order: P1 non-crossing first, then P2,
  P3). Post-state = `cap` exactly; G5; no known crossing; cap reached
  through the pool.
- Batches 1, 2, and 5 of v2.1 stand and were independently confirmed;
  batch 5's crossing-last order is now the `A2` order's special case
  (one crossing process).

All five batches now carry complete integer inputs (`D0`, `remaining`,
`K`, `m`, `U`, every share, every process aggregate, post-state,
terminal) and are independently recomputable.

## C. Repeatable overdue resume (replaces the singleton path)

Pending-resume checkpoints form an **immutable generation keyed by the
immediately preceding ordinary-pause event hash**:

```text
successor/officina/runtime/T_PENDING_RESUME_CHECKPOINTS/<pause_event_sha256>.json
```

Schema `philosophia.officina.t-pending-resume-checkpoint.v1` (keys as
in v2.1 C.2, unchanged: `schema`, `scientific_outcome`,
`original_checkpoint_sha256`, `payload_sha256`, `ledger_head_before`
(= the keying pause event's hash), `created_utc`). Atomic no-replace
per generation; **prior generations are never deleted or replaced**
(retained in the archive forever); lookup is by the keying pause event
hash. The second `T_OPERATIONAL_PAUSE` binds the artifact keyed by its
immediately preceding ordinary pause; the verifier relation is
unchanged: the pending artifact's `ledger_head_before` equals the
entry immediately preceding the second pause. Original checkpoints,
payload byte-identity, head relations, crash cuts, and the
no-tenth-event rule carry forward from v2.1 C.2 verbatim.

**Two-cycle acceptance route:** pause A (checkpoint CK-A, entry
`h_A`) → power-off, E3 overdue → pending artifact
`T_PENDING_RESUME_CHECKPOINTS/h_A.json` → second pause
(`RESUME_E3_REVIEW_PENDING`, binds that artifact) → durable
`T_REVIEW_COMPLETED` → work → pause B (checkpoint CK-B, entry `h_B`)
→ power-off, overdue again → **distinct** artifact
`…/h_B.json` (distinct hash, no collision with the retained
`h_A.json`) → second pause → review. Crash cuts at every step are the
v2.1 C.2 cuts applied per generation; a cut between artifact creation
and the second pause orphans only that generation's artifact
(record-first invalidity naming it), never a prior generation.

## Compatibility (correction-level)

Unchanged: all signed events (nine), runtime schemas, constants,
roots, phase rules, T bands, WP-3/WP-4 boundaries, WP-6/WP-9
ownership, and every scientific contract and negative destination.
**Bounded core amendment:** exactly the companion draft's
`accounting.py` surface, eligible only after X/Y approval and
Kirill's amendment token. **Harness-only deterministic corrections:**
A1's per-stream rule, A2's batch order, A3's recomputable examples,
C's generational path — clarifications of the harness contract, not
schema or core changes. **Future implementation files/tests/verifier
pins** (eligible only after both signatures):
`generic_harness.py` + its tests (v2 §11), the amended
`accounting.py` + its tests (companion §3), and the production
call-graph manifest at implementation review.

No learner, candidate, architecture, optimizer, device winner, Q
predicate, alpha, endpoint, margin, or scientific result is selected;
T stays `NOT_ACTIVATED`; T and Q remain permanently non-citable for
C1–C6; the programme claim remains `OPEN`.
