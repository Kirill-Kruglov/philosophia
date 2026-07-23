REVISE_OFFICINA_GENERIC_HARNESS_V2_1_YLINE

# Sol Y-line — literal Officina harness v2.1 confirmation

The v2.1 correction closes D and E and most of B/C, but it does not close correction A for all admitted mixed or multi-process settlements. That makes B's claimed total event machine non-representable in a concrete invalid batch. C.2 also has a repeat-resume path collision. These are accounting and admission defects, not speculative implementation questions or scientific-design reopenings.

## Critical — A/B still require a hidden metering-core amendment

### 1. Mixed known/unknown streams are not single-valued

The aggregation rule first classifies **per stream** (`successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_1_CORRECTION.md:38-45`), but the cursor rule says that any ambiguity makes the **whole process** unknowable (`:47-52`). Those instructions differ whenever one non-coextensive stream has a proved case-(a)/(b) interval and a sibling stream is unknowable.

Concrete integer example: let E1 remaining be 50 ns for a two-stream process; one proved late stream owes 100 ns and the other is unknowable. Literal whole-process reclassification gives `K=0, m=2, U=50 ns`, hence a 50 ns process charge. Per-stream classification gives `K=100 ns, m=1, U=1 ns`, hence 101 ns. The first clips a proved known-late interval, contrary to lines 67-69; the second preserves it. Both readings fit current prose, so accounting and the terminal state are not single-valued.

**Mandatory A1 repair:** keep classification per stream. Every proved interval remains in `K`; only genuinely unknowable streams enter `m` and receive shares. If any stream is unknowable, the process takes the invalid route, but that must not erase its known siblings' charges. Aggregate that process's known charges plus unknown shares into its one process-scoped event. Add an exact mixed non-coextensive example and probe.

### 2. More than one known-late process may need a post-cap charge

The unchanged core refuses a charge whenever the pre-charge global state is already exhausted (`src/philosophia/officina/accounting.py:117-128`). V2.1 acknowledges that only one crossing append can occur and therefore places “the” crossing process last (`correction.md:71-81`). But signed case (b) permits the complete actual interval to exceed reservation, and several concurrent processes can be late-known.

Concrete counterexample: start at `D0 = E1_cap - 100 ns`; three existing processes each owe a proved case-(b) charge of 60 ns. Their original positive liabilities can have fit inside the 100 ns remainder, while their later actual intervals exceed those reservations. Under every permutation, the second 60 ns event crosses the cap and the third event is refused. Exhaustive permutation gave zero representable orders. Adding an unknowable sibling does not repair this. Therefore the required positive charge and invalid tuple cannot be emitted for every process, B.3 cannot close all siblings, conservation cannot reach a rest state, and “fail closed before charging” supplies no alternative durable record/event/removal sequence.

This is not merely a missing test: the process-scoped event and lease hash prevent cross-process aggregation, while the current constructor prevents sequential post-cap appends.

**Mandatory A2/B repair:** withdraw the unconditional no-core-amendment classification. Either install and separately review a bounded batch-settlement core rule that permits every frozen pre-existing lease's positive, full, process-scoped charge to append after the first E1 crossing while still forbidding admission and ordinary post-exhaustion charging, or provide an enforceable pre-batch invariant proving that no valid signed case-(b) batch can require a second post-cap append. The latter is not supplied by positive reservation and is contradicted by the example above. The chosen route must give one exact interleaved event/record/removal order for multiple crossing processes and preserve every full known charge.

Until that repair lands, B.1-B.5 are logically well-prioritized but only conditionally representable; invalidity dominance cannot by itself manufacture the missing positive events.

## Major — the five worked batches are not all recomputable

The integer pool formula itself is correct. For `U=max(m, remaining-K)` in nanoseconds, write `U=qm+r`, `0≤r<m`; allocating `q+1` to the first `r` streams and `q` to the rest sums to `U`, and `U≥m` gives every share at least 1 ns. A bounded integer grid found no conservation or minimum-share failure.

Independent batch arithmetic:

| Batch | Recalculation | Result |
|---|---|---|
| 1 | `100,000 s + 42 s + 95 s` | `100,137 s`; correct, no pool. |
| 2 | remaining `100 s`, `K=95 s`, `m=2`; `U=5 s`; shares `2.5 s, 2.5 s` | exact cap `604,800 s`; correct; invalid G5 with no exhaustion event. |
| 3 | claimed `m=2`, shares 2 ns each | Requires `U=4 ns`, hence `max(2 ns, remaining-K)=4 ns`, but `D0`, `K`, and remaining are absent. It is not independently recomputable or bit-exactly forced. |
| 4 | `K=30 s`, `m=3`, claimed `U=3 ns` | Requires `remaining-K≤3 ns`; `D0` is absent. If equality holds, the post-state reaches the cap, so “no crossing” can only mean no **known** crossing and must be stated that way. |
| 5 | remaining `40 s`, `K=70 s`, `m=2`; `U=2 ns`; shares `1 ns, 1 ns` | `604,830 s + 2 ns`; correct; invalid G5 with no exhaustion event. |

**Mandatory A3 repair:** give batches 3 and 4 complete integer inputs (`D0`, `K`, remaining, `m`), their exact post-state and terminal route, and correct batch 4's “no crossing” wording. The §F claim that all five batches are forced bit-exactly is otherwise false.

## Major — C.2 has no lifecycle for a second overdue resume

C.1 correctly makes clean G3→G1 durable only through the next existing `T_PROCESS_STARTED`. C.3 gives the recovery disposition an event-keyed, no-replace path and a closed predicate. C.2 instead assigns every overdue-resume cycle the singleton path `runtime/T_PENDING_RESUME_CHECKPOINT.json` with atomic no-replace (`correction.md:188-219`). After the first durable review, the artifact is neither removed nor given a terminal lifecycle; it is also part of the archive set. A later valid pause followed by another overdue resume cannot create the required artifact. Deleting/replacing it or permanently refusing the second cycle are materially different admission policies, neither authorized by the contract.

**Mandatory C repair:** use a unique immutable path keyed by the immediately preceding ordinary-pause event hash, for example `runtime/T_PENDING_RESUME_CHECKPOINTS/<pause_event_sha256>.json`, or specify an equally exact immutable generation scheme. Bind the second pause to that artifact, preserve the existing original-checkpoint/head/payload relation and cuts, and add a two-complete-pause-cycle acceptance case. Do not silently delete or replace prior evidence.

## Closed bounded cells

- **B semantics:** invalidity dominance, one-cause collateral closure, no valid exhaustion/stop/pause event under unresolved invalidity, retained numeric E1/E3 facts, and the B.5 precedence table are coherent once A's charges are representable.
- **C.1/C.3/C.4:** clean-resume durability, fresh process ids, event-keyed recovery dispositions, no tenth event, no automatic retry, and deferred invalid-event handling are closed. Only C.2's repeat-cycle path remains open.
- **D:** the invalidity schema remains exactly one-cause; the contradictory cause-list sentence is deleted and no public/runtime cause list is introduced.
- **E:** all five decision artifacts have closed key sets and finite enums where applicable; free text and learner/output-derived decision selection are forbidden. Machine inputs are constrained without claiming that Kirill's author-stop cognition is blind.
- **Scientific/governance boundary:** no learner, candidate, device winner, WP-6 Q cell, WP-9 endpoint/margin/analysis cell, frame realization, or scientific interpretation is selected. T/Q remain non-citable; WP-3 and WP-4 capability boundaries are unchanged.

## Determinacy and authorization

Aggregate/rest-state conservation and terminal admission are not yet single-valued for two implementations because A1 permits two different mixed-process charges, A2 has no representable sequence for the concrete multi-cross batch, and C.2 cannot represent a second overdue-resume cycle. These defects directly change accounting, ordering, and admissibility.

This verdict authorizes only bounded corrections A1-A3 and C above, plus another literal final confirmation. Kirill's `I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT` is not yet eligible. No implementation, metering-core amendment, production manifest, authorization, activation, capability, world, learner, process, lease, entropy, E1/E2/E3 spend, T/Q/C datum, outcome, or claim movement is authorized or created by this review. The real tree remains `NOT_ACTIVATED`; `successor/officina/runtime/` contains only `T_RUNTIME.lock`.
