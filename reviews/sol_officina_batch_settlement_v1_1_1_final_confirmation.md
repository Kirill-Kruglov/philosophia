OFFICINA_BATCH_SETTLEMENT_V1_1_1_YLINE_CONFIRMED

# Literal Y-line confirmation

No Critical, Major, or Minor blocker remains within this bounded confirmation.
The v1 amendment as corrected by v1.1 and v1.1.1, together with the harness
contract through v2.3.1, closes Sol R1–R4 without changing a scientific cell or
the inactive boundary.

## Direct answer to Fable §6

**Yes.** Inline `meter_evidence` preserves R1's full recomputability. For each
known stream, the exact non-outcome start/end readings re-derive
`known_charge_ns = end - start`; the closed claim then re-derives
`K`, `m`, `U = max(m, remaining_ns - K)`, the quotient/remainder allocation in
the one frozen global stream order, and every per-process aggregate. Exact
nullability, clock, boot, adapter, synchronization, deadline, and timestamp
rules are also claim-hash-bound. No claimed stream charge or process total is a
free input.

The outer `scientific_outcome: false` rule and recursive scientific-field
rejection reach the nested evidence object, so this witness cannot carry a
learner/output/result fact. The signed `live_units + requested_units <= 4`
boundary limits the claim to at most four stream entries; inlining neither
enlarges concurrency nor creates another accounting route.

## Bounded closure checks

1. **No orphan evidence state.** Deleting the separate
   `T_METER_EVIDENCE/` family removes its pre-claim write, orphan, crash-cut,
   and archive states. Before atomic claim installation there is no durable
   batch witness to recover; after installation the one retained claim contains
   and hash-binds all meter facts. Nothing has merely been moved to an
   ungoverned side artifact.

2. **Narrow head/cache completion.** Section D1 applies only to exactly one
   unresolved, fully valid claim and one byte-exact canonical prefix whose only
   discrepancy is a head/cache lag of at most the just-appended state-bearing
   entry. Its authority binds the claim, prefix index, and old/new head and
   state hashes, performs no new charge or clock read, and requires immediate
   full-tree verification. A second claim, stale authority, extra/missing or
   noncanonical prefix element, lease/path/hash mismatch, second discrepancy,
   or ambiguous state cannot use D1 and remains on the inherited
   record-first invalidity/recovery route. Thus D1 permits neither re-charge,
   shadowing, stale-authority use, nor ambiguous recovery.

3. **R1–R4 remain closed.** The claim is a complete accounting witness; stream
   allocation and process execution retain one global canonical order; the
   retained unresolved-claim registry blocks shadow claims and admits only its
   single-use next-step authority; and the complete prefix automaton still
   covers every intra-tuple cut, override, terminal, lease-removal, and archive
   step. Inline evidence had no automaton substep, so its removal introduces no
   missing prefix. Every mismatch outside D1 remains blocked or invalid rather
   than becoming admission.

4. **Determinism across implementations.** Closed key sets and enums, canonical
   JSON, exact integer recomputation, frozen stream/process order, deterministic
   timestamps and dependent artifacts, exact prefix recognition, and a unique
   next action make accounting, artifact order, and admission single-valued.
   Two conforming independent implementations must therefore produce the same
   charges, hashes, continuation, and terminal routing from the same durable
   inputs.

The correction commit adds only the two correction documents and Fable closure;
`git diff --check` is clean. The inactive runtime inventory still contains only
`T_RUNTIME.lock`.

## Signature disposition and negative space

The following two author tokens are eligible in this exact order:

1. `I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT`
2. `I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT`

This confirmation authorizes only Kirill's informed ordered signatures. It
authorizes no code or implementation, manifest, authorization, activation,
claim, override, capability, process, lease, learner, world, entropy, resource
spend, T/Q/C datum, outcome, or scientific interpretation. T remains
`NOT_ACTIVATED`; E1/E2/E3 constants, WP-3/WP-4 boundaries, WP-6/WP-9
ownership, all scientific estimands, all negative destinations, and the
non-citability of T/Q for C1–C6 remain unchanged.
