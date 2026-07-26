# Opus 4.8 X-line prompt: Officina generic harness implementation

Work read-only in `/home/master/llm_projects/philosophia`.

Write exactly one new file:

```text
reviews/opus_officina_generic_harness_implementation_review.md
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

Audit these uncommitted Cursor files:

```text
src/philosophia/officina/accounting.py
src/philosophia/officina/generic_harness.py
tests/test_officina_accounting.py
tests/test_officina_generic_harness.py
```

Diff them against HEAD `2af5720`. Preserve every unrelated dirty file.

## X-line mandate

Take an adversarial implementability and control-path stance. Do not infer
completeness from the 416 green tests. Trace actual production calls.

Independently verify or reject every Codex C1-C4 and M1-M6 finding, with exact
file/line and contract-section references. In particular:

1. Prove whether any production path actually starts and owns the claimed
   controller, checks PID start identity/group membership, installs a watchdog,
   revokes/quiesces it, confines output, settles, and only then promotes.
2. Determine whether `run_isolated_operation(lambda)` can satisfy signed §5b
   or is necessarily a test facade that exposes pre-settlement information.
3. Trace E1/E3 crossing from an ordinary heartbeat through all live siblings.
   Decide whether the fallback `Reservation(...)` can leave behavior-capable
   work live after the cap.
4. Trace the exact batch automaton including archival. Decide whether current
   `RESOLVED` is reachable before the mandatory Git boundary and whether the
   existing signed v2 §B sets/trailers are sufficient to implement archival.
5. Reproduce the ledger-ahead-of-head D1 cut using disposable files. Determine
   whether current normal ledger parsing makes the authorized repair
   unreachable.
6. Exercise recovery followed by a fresh start and then a heartbeat. Check the
   "since last admission" scope.
7. Exercise the actual
   `python -m philosophia.officina.generic_harness` entry point.
8. Audit every signed transaction cut, especially orphan dependent artifact,
   start-event-without-lease, ledger/head lag, cache/lease lag, and close
   interleaving.
9. Audit full-live-set batch revalidation, process-sequence non-reuse, lock
   ownership, and capability binding/use.
10. Assess whether the missing supervisor/IPC/output-confinement mechanics are
    fully determined by the signed contract. If two compliant implementations
    could make materially different choices, return `BLOCKED_CONTRACT` for that
    surface and state the smallest bounded correction required. Do not design
    it silently.

Answer the three Codex clarification questions:

- Is pre-review head the forced meaning of review-record
  `ledger_entry_sha256`/`ledger_head_sha256`?
- Is the extra current-head keyword in `charge_batch_settlement` faithful to
  the prose?
- Does archival need a contract correction or only implementation?

## Required verdict

First line exactly one:

```text
OFFICINA_GENERIC_HARNESS_IMPLEMENTATION_ACCEPTED
REVISE_OFFICINA_GENERIC_HARNESS_IMPLEMENTATION
BLOCKED_OFFICINA_GENERIC_HARNESS_CONTRACT
```

Use Critical/Major/Minor findings. State:

- exact mandatory repairs;
- whether Cursor may repair immediately or must wait for a bounded contract
  correction;
- tests that must be added because the current matrix is green-but-incomplete;
- whether any of the four implementation files are eligible to commit;
- confirmation that no activation, entropy, spend, real process, manifest, or
outcome was created.
