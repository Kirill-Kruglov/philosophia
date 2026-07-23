READY_FOR_OFFICINA_BATCH_SETTLEMENT_AMENDMENT_XY_REVIEW

# Fable 5 — Officina harness v2.2 and batch-settlement core amendment closure

Author: Fable 5. Companions:
`successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md` and
`successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_2_CORRECTION.md`.
Inputs: Opus (`OFFICINA_GENERIC_HARNESS_V2_1_XLINE_CONFIRMED`) and Sol
(`REVISE_OFFICINA_GENERIC_HARNESS_V2_1_YLINE`, A1/A2/A3/C). v2 and
v2.1 preserved unchanged. Exactly three files created; nothing else
changed; nothing committed; no code edited or executed beyond
read-only verification probes. The prior conditional harness signature
was **not** accepted and is not claimed.

## 1. Independent counterexample verification — CONFIRMED

Reproduced against the current
`accounting.py:TState.charge_device_nanoseconds` (in-memory states
only): from `D0 = E1_cap − 100 ns`, three proved case-(b) charges of
60 ns each are representable in **0 of 6 permutations** — the first
append reaches `cap − 40`, the second `cap + 20` (state exhausted),
the third refuses with `T envelope is already exhausted`. A single
150 ns crossing appends, and any subsequent 1 ns charge refuses —
confirming v2.1's crossing-last rule handled exactly one crossing and
no more. No pre-batch invariant can exclude the case (reservations of
60 ns each legally fit the 100 ns remainder; actual case-(b) intervals
legally exceed them). Sol is correct; the harness-wording route is
impossible; the explicit bounded core amendment is the honest path,
and v2.1's unconditional no-core-amendment classification is
superseded loudly in both new documents.

## 2. Disposition table

| Finding | Disposition | Where |
|---|---|---|
| **Sol A1** — mixed streams not single-valued | **Adopted**: per-stream classification always; proved intervals stay in `K`; unknowable streams only enter `m`; process with any unknowable stream takes the invalid route with known sibling charges preserved in its one aggregated event; ambiguity affects only ambiguous streams; the 50/100 ns example worked exactly (charge 101 ns, not 50) | v2.2 §A1 |
| **Sol A2** (Critical) — multi-cross unrepresentable | **Adopted via the explicit amendment route**: frozen-batch settlement authority (claim-before-charges, post-cap appends within one batch only, ordinary refusal unchanged outside); deterministic order for zero/one/many crossings; the 60/60/60 ledger worked event-by-event with intermediate above-cap states | amendment §2; v2.2 §A2 |
| **Sol A3** — batches 3/4 not recomputable | **Adopted**: complete integer inputs for both; "no crossing" corrected to "no **known** crossing; cap reached through the unknown pool" | v2.2 §A3 |
| **Sol C** — singleton pending-checkpoint path | **Adopted**: immutable generation keyed by the preceding pause event hash; prior generations retained forever; two-cycle acceptance route with distinct hashes; per-generation crash cuts | v2.2 §C |
| **Opus M-1..M-6 interaction** | M-1's crossing-last device was necessary but insufficient — superseded by the batch authority (M-1's floor rule, unknown-first rationale, and no-zero-charge-constructor stance all survive); M-2 (exhaustion only on all-valid), M-3 (tuple adjacency, preserved inside every batch tuple), M-4 (inherited dominant cause), M-5 (single-cause schema), M-6 (pending checkpoint, now generational) all carry forward unchanged | both files |

## 3. Amendment invariants/schema/path/crash/archival (summary)

Claim `philosophia.officina.t-batch-settlement-claim.v1` at
`runtime/T_BATCH_SETTLEMENT_CLAIMS/<pre_ledger_head_sha256>.json`
(no-replace; one batch per ledger position; retained forever); keys
and the `processes` entry shape pinned; `batch_reason` enum fixed.
Authority: non-reusable, claim-bound, pre-existing leases only, cannot
admit/renew/authorize/increase/add/charge-ordinary-work-post-cap;
first charge may cross, later claimed charges append within the same
batch only; events remain unmodified `T_DEVICE_TIME_CHARGED`; no new
field in any signed schema; auditability via the closed artifact
family (claim binds pre-head; records and post-head bind the rest);
no tenth event. Crash cuts: before-claim (nothing), after-claim
(complete-or-blocked), between-tuples (complete missing
claim-enumerated work only, in order, charges immutable, no
recomputation from outcomes, no behavior), after-last (archival under
signed disposition). Post-verifier: each entry consumed once; no
extra/missing/reorder; post E1 = pre + Σ claimed; every lease at its
mandated terminal; global terminal matches batch reason. Smallest
future surface: one dataclass + one pure method in `accounting.py`
plus tests — a reviewed immutable-control change eligible only after
X/Y approval and the amendment token; `charge_device_nanoseconds`
itself is not weakened.

## 4. Worked ledgers (all independently recomputable)

- **Multi-cross 60/60/60, remaining 100 ns** (the verified
  counterexample): claim P1/P2/P3; tuples in ascending sequence;
  states `cap−40`, `cap+20`, `cap+80`; full charges; G5; no
  exhaustion event.
- **Mixed 50/100 ns**: `K=100, m=1, U=1 ns`; one event 101 ns;
  `cap+51`; G5.
- **Mixed multi-process**: P1 50 (non-crossing first), P2 135
  (120+15), P3 15; final exactly `cap`; G5; numeric cap fact retained.
- **Batch 3**: `D0=cap−4 ns, K=0, m=2, U=4` → one event 4 ns; cap
  exactly; no known crossing.
- **Batch 4**: `D0=cap−30 s−3 ns, K=30 s, m=3, U=3` → events 30 s /
  2 ns / 1 ns; cap exactly.
- Fault-free all-valid E1 batch: same authority; per-process valid
  record → stopped → removal; then exactly one `T_ENVELOPE_EXHAUSTED`;
  G7.

## 5. v2.1 → v2.2 replacement index

As tabled in the v2.2 header: A1 replaces the whole-process-ambiguity
cursor sentence; A2 replaces the single-crossing ordering; A3 replaces
batches 3–4 and the "no crossing" wording; the fail-closed-floor
sentence is narrowed to batches attempted without authority; §C
replaces the singleton pending path; §G's no-core-amendment half is
withdrawn (the no-zero-charge-constructor half stands). Everything
else in v2 + v2.1 carries forward verbatim, including all X-line-
confirmed material (B routes, D, E, C.1/C.3/C.4).

## 6. Two-implementer determinacy

Charges: per-stream classification + the U-formula + per-process
aggregation force integer values; the frozen claim then makes them
immutable inputs. Ordering: claim array order (non-crossing ascending,
then crossing ascending) + indivisible tuples + adjacency force one
ledger. Terminals: batch reason + all-valid vs any-invalid force
G7/G2/G5 uniquely. Resume/recovery: generational keyed paths + the
C.3 predicate force one admission decision, including the two-cycle
route. The previously divergent cases (mixed process, multi-cross,
second overdue resume) each now have exactly one derivation.

## 7. Two-token signature order

1. `I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT` — after both
   X/Y approvals (and any literal confirmation) of the amendment;
   authorizes only the named `accounting.py`
   surface + tests, under implementation review. Without it, no core
   change may occur and the harness contract cannot function on
   multi-cross batches — refusing it routes the harness back to
   redesign, not to silent wording.
2. `I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT` — only after token 1
   and the X/Y confirmation of v2 + v2.1 + v2.2; accepts the harness
   contract as corrected; authorizes `generic_harness.py`
   implementation per v2 §11 under its own review.

Neither token is eligible from these drafts; the prior conditional
signature is void and not claimed.

## 8. Bounded questions

**Opus (three):**
1. Does the frozen-batch authority (claim-before-charges, non-reuse,
   claim-bound values, post-cap appends inside one batch only) close
   the multi-cross case without weakening ordinary charging anywhere —
   and is the §2e complete-or-blocked recovery loop-free?
2. Is the smallest-surface claim right — one dataclass + one pure
   method in `accounting.py`, `runtime.py` untouched, no signed-schema
   field — or does any part of §2d's tuple/verifier duty force a wider
   core change that must be named now?
3. Do A1/A2 preserve your M-1..M-5 dispositions exactly (floor rule,
   adjacency, single cause, exhaustion-only-on-all-valid) under the
   new order?

**Sol (three):**
1. Does §A1 + the 50/100 example make mixed settlement single-valued
   (per-stream classification, proved intervals never clipped, one
   aggregated event), and §A3 make all five batches independently
   recomputable with the known-crossing/pool-cap distinction stated?
2. Does the amendment's conservation contract (post E1 = pre + Σ
   claimed; claimed values from the signed rules, never clipped;
   pool debited once) plus the 60/60/60 and mixed multi-process
   ledgers satisfy your A2 requirement for one exact interleaved
   order per batch class?
3. Does §C's generational path close the second-overdue-resume
   lifecycle (no deletion, no replacement, distinct hashes, per-
   generation cuts) without touching the original-checkpoint/head
   relations?

## 9. Negative authorization confirmation

Created: exactly the three mandated files. Not created, edited, or
run: any code (`accounting.py`, `runtime.py`, `generic_harness.py`
untouched); any manifest, authorization, activation, capability,
process, world, learner; entropy; E1/E2/E3 spend; any T/Q/C/runtime
datum, ledger event, claim instance, root, lock, escrow, outcome, or
claim movement. Verification probes used in-memory `TState` values
only and mutated nothing. No learner, candidate, architecture,
optimizer, device winner, Q predicate, alpha, endpoint, margin, or
scientific result selected; WP-6/WP-9 ownership and all negative
destinations unchanged. T remains `NOT_ACTIVATED` at genesis
(`runtime/` holds only `T_RUNTIME.lock`); the predecessor line remains
immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`; T and Q remain
permanently non-citable for C1–C6; no prediction is made about any
learner or about Philosophia being proved, falsified, or bounded; the
programme claim remains `OPEN`. Next step: one bounded X/Y review of
the amendment and correction, any required literal confirmation, then
Kirill's two informed signatures in the §7 order.
