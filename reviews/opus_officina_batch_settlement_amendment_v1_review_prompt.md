# Opus 4.8 X-line: Officina batch-settlement amendment v1 review

Work read-only in `/home/master/llm_projects/philosophia`.

Review as one bounded engineering packet:

- `successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md`
- `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_2_CORRECTION.md`
- `reviews/fable_officina_harness_v2_2_core_amendment_closure.md`

against the current accounting/runtime/ledger constructors, signed activation
protocol, your confirmed M-1..M-6 repairs, Sol's A1/A2/A3/C counterexamples, and
the inactive production boundary. Do not reopen scientific or learner choices.

Required attacks:

1. Independently reproduce the 60/60/60 ns multi-cross impossibility under the
   old core and verify a bounded core amendment is genuinely necessary.
2. Audit `t-batch-settlement-claim.v1` byte-for-byte: exact keys/types/enums,
   path uniqueness, pre-head/state/lease binding, sorted order, charge and
   disposition validity, no-replace/fsync/archive rules. Identify any field that
   is insufficient to reconstruct or reject a batch.
3. Make the future authority operationally single-valued. In particular, attack
   the proposed pure-method surface: how does one invocation select the exact
   `process_id`, `active_lease_sha256`, `charge_ns`, and next unconsumed claim
   entry; how is authority consumption represented without reuse; how are
   mismatch, reorder, duplicate and value substitution refused? State the
   smallest exact signature/state surface if the draft is ambiguous.
4. Audit every crash cut, especially charge durable but invalid/valid terminal
   tuple incomplete. Verify recovery can distinguish an already consumed charge
   from a missing charge using only durable facts, never charge twice, preserve
   immediate ancestry, and complete-or-block without resuming behavior.
5. Verify the amendment does not weaken ordinary post-E1 refusal, authorize new
   work/admission, add a signed event field, or require an unnamed change outside
   the declared core/control files. Check whether `runtime.py` truly remains
   unchanged and whether verifier/control pins must be named.
6. Verify v2.2 A1/A2/A3 and generational C remain compatible with M-1..M-6:
   mixed per-stream preservation, multiple crossings, per-process aggregation,
   exact tuple order, G5/G7 distinction, recomputable batches, and two overdue
   resume cycles.
7. Decide whether two implementers can emit identical claims, accounting states,
   ledger tuples, crash recovery and terminals. Report concrete output-changing
   gaps only; distinguish mandatory repair from implementation-test detail.

Write exactly one file and change nothing else:
`reviews/opus_officina_batch_settlement_amendment_v1_review.md`.

First line exactly one token:

- `OFFICINA_BATCH_SETTLEMENT_AMENDMENT_V1_XLINE_APPROVED`; or
- `REVISE_OFFICINA_BATCH_SETTLEMENT_AMENDMENT_V1_XLINE`; or
- `BLOCKED_OFFICINA_BATCH_SETTLEMENT_AMENDMENT_V1_XLINE`.

A positive verdict authorizes only bounded Y/X confirmation and Kirill's two
ordered signatures. It authorizes no code, implementation, activation or spend.
