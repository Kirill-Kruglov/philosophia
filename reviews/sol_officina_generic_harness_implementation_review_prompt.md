# GPT-5.6 Sol Y-line prompt: Officina generic harness implementation

Work read-only in `/home/master/llm_projects/philosophia`.

Write exactly one new file:

```text
reviews/sol_officina_generic_harness_implementation_review.md
```

Do not edit implementation, contracts, tests, signatures, runtime artifacts, or
any existing review. Do not commit. Do not activate T or create a production
call-graph manifest.

## Governing authority

Read:

```text
successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md
successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_CORRECTION.md
successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_1_CORRECTION.md
successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_2_CORRECTION.md
successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_CORRECTION.md
successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
reviews/codex_officina_generic_harness_implementation_review.md
```

Audit these uncommitted Cursor files against HEAD `2af5720`:

```text
src/philosophia/officina/accounting.py
src/philosophia/officina/generic_harness.py
tests/test_officina_accounting.py
tests/test_officina_generic_harness.py
```

Preserve every unrelated dirty file.

## Y-line mandate

Take a state-machine, accounting, validity-first, and test-sufficiency stance.
Independently verify or reject every Codex C1-C4 and M1-M6 finding.

Build explicit reachable traces for:

1. an ordinary heartbeat crossing E1 with one and with multiple live leases;
2. simultaneous E1/E3 and invalidity-dominance endings;
3. the 60/60/60 batch from claim installation through the required archival
   boundary;
4. every batch crash prefix, including ledger written but external head stale;
5. recovery disposition, fresh admission, then another heartbeat/close;
6. start event durable but lease absent;
7. charge event durable but state or lease cursor stale;
8. a closed process followed by another claim, checking global sequence/id
   non-reuse;
9. result production before settlement and promotion after an unrelated charge;
10. actual module CLI parsing.

For each trace, state the signed terminal/global/process state and compare it to
the implementation. Identify tests that assert a weaker surrogate. Check that:

- full-live-set batch completeness is revalidated at every registry entry;
- unknown-pool arithmetic and multiple-crossing accounting remain correct;
- ordinary charging stays unchanged and batch authority cannot be forged,
  substituted, replayed, or advanced against a stale head/state;
- G5 scope is exactly invalidities since last admission, not all history;
- archive absence keeps capability blocked;
- review records and decisions are closed and non-circular;
- all public reads/admissions/capability operations use the runtime lock;
- `scientific_outcome:false` and recursive forbidden-field rejection cover all
  nested inputs;
- the acceptance matrix is genuinely capable of failing a facade-only
  supervisor/isolation implementation.

Answer:

1. Is binding both review-record ledger fields to the durable pre-review head
   the forced non-circular interpretation?
2. Is the caller-supplied current-head keyword in
   `charge_batch_settlement` required by the prose?
3. Are the signed archival set and trailers enough, or is one bounded contract
   cell still missing?
4. Can §5 supervisor/isolation be implemented without choosing an unsigned IPC,
   temporary-output, watchdog-lifetime, or CLI-control policy? If not, identify
   the smallest missing contract surface.

## Required verdict

First line exactly one:

```text
OFFICINA_GENERIC_HARNESS_IMPLEMENTATION_ACCEPTED
REVISE_OFFICINA_GENERIC_HARNESS_IMPLEMENTATION
BLOCKED_OFFICINA_GENERIC_HARNESS_CONTRACT
```

Use Critical/Major/Minor findings. Give exact mandatory repairs, the required
new tests, and whether the repair may go directly to Cursor or first requires a
bounded Fable contract closure. Confirm that T remains `NOT_ACTIVATED`, the
production manifest is absent, and none of the four implementation files is
committed.
