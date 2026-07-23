# Sol Y-line: Officina batch-settlement amendment v1 review

Work read-only in `/home/master/llm_projects/philosophia`.

Review as one bounded governance/accounting packet:

- `successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md`
- `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_2_CORRECTION.md`
- `reviews/fable_officina_harness_v2_2_core_amendment_closure.md`

against your v2.1 final corrections A1/A2/A3/C, the signed resource semantics,
current constructors, charter, WP-3 and WP-4. This is not a scientific redesign.

Required checks:

1. Recompute the original 60/60/60 counterexample and every v2.2 ledger in
   integer nanoseconds. Verify proved per-stream charges remain in `K`, unknown
   shares are allocated once, per-process aggregation is exact, and no known
   charge is clipped, multiplied or erased.
2. Verify the amendment is the narrowest honest authority: only pre-existing
   claim-enumerated leases/values under one below-cap frozen pre-state; no
   ordinary post-cap charge, admission, renewal, omitted process, increased
   value or behavior can use it. Check the two-token governance order.
3. Audit resource conservation through multiple crossings and all-valid/invalid
   terminals. Verify post E1 = pre + full claimed sum, every process gets one
   positive event, invalid batches remain G5 without a valid exhaustion event,
   and all-valid E1 ends with exactly one exhaustion event.
4. Audit crash/recovery conservation. At every prefix of claim and tuples, state
   whether the next action is uniquely charge, finish-terminal, archive, or
   remain blocked. Ensure no charge is repeated and no batch is abandoned,
   recomputed from outcomes or used to admit work.
5. Check the closed claim schema and immutable path provide enough durable
   information for the post-verifier and recovery without adding a signed event
   field. Attack reuse at the same/different pre-head, partial tuples, reordered
   processes and a stale authority after restart.
6. Verify A1's mixed 50/100 result is 101 ns, batches 3/4 are fully recomputable,
   and the generational pending-resume path supports two complete cycles without
   deletion, substitution or an admission-policy fork.
7. State whether the amendment changes only engineering/control semantics and
   leaves E1/E2/E3 constants, scientific estimands, WP-6/WP-9 and negative
   destinations unchanged. Report a blocker only if it changes accounting,
   ordering, admissibility or evidence.

Write exactly one file and change nothing else:
`reviews/sol_officina_batch_settlement_amendment_v1_review.md`.

First line exactly one token:

- `OFFICINA_BATCH_SETTLEMENT_AMENDMENT_V1_YLINE_APPROVED`; or
- `REVISE_OFFICINA_BATCH_SETTLEMENT_AMENDMENT_V1_YLINE`; or
- `BLOCKED_OFFICINA_BATCH_SETTLEMENT_AMENDMENT_V1_YLINE`.

A positive verdict authorizes only bounded final confirmation and Kirill's two
ordered signatures. It authorizes no code, implementation, activation or spend.
