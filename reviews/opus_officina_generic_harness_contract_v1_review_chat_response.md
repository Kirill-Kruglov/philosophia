I completed the bounded X-line review and wrote exactly one file: `reviews/opus_officina_generic_harness_contract_v1_review.md`. First line is the required token.

## Verdict: `REVISE_OFFICINA_GENERIC_HARNESS_CONTRACT_XLINE`

The contract is faithful in spirit and selects no scientific/authority cell, but it is **not yet bit-exactly implementable** and contradicts itself, the pinned C4-confirmed code, and — in three places — the *signed* v2.1. Four Critical findings:

- **C-1 (event-before-record inversion):** §2.6/§2.7 emit `T_PROCESS_STOPPED` before the process record, but the stopped event's payload must carry `process_record_sha256` (`runtime.py`), and §3's own template puts the record first. Unimplementable as written.
- **C-2 (missing INVALID process record; process- vs global-invalidity conflated):** §2.12/§2.13 never build the `t-process-record.v1` that v2 §B requires an invalid close to archive, and treat every fault as simultaneously process- and global-scoped.
- **C-3 (recovery charge contradicts signed v2.1 §1 — undercount):** the contract reinstates the deleted flat "charge the full outstanding liability" rule for process loss / watchdog-without-quiescence, undercharging exactly the deadline-overrunning adversary v2.1 §1 was written to catch. This is a silent policy amendment, not a clarification.
- **C-4 (production roots/CLI vs pinned verifier):** §9/§11 introduce a new `scripts/officina_t_process.py` root, but `verification.py:PRODUCTION_ROOTS` (immutable-control, C4-confirmed) pins `generic_harness.py` as the root and the manifest must match exactly — so the contract is either unimplementable or an undisclosed amendment to signed control code.

Plus Major/Minor repairs (R5–R12): a §3 self-contradiction on silent cache re-derivation vs record-first invalidity; unspecified handling of sibling live leases when one process forces G5; unpinned initial `prior_charge_event_sha256`; the exhaustion-append vs realized-E1 edge; static-import constraint on adapters and the harness's confinement to the pinned import allowlist (which makes off-CPU adapters structurally a control amendment); and coarse §11 ownership/type pinning.

I answered Fable's four X-line questions (Q1 totality NO; Q2 containment PARTIAL pending C-3; Q3 closure NO pending C-4/R10/R11; Q4 no-amendment REJECTED for the C-3 and C-4 clauses) and gave a finite mandatory repair list with exact replacement text/tables for each. Mandate point 7 (no executable authority or scientific/learner choice) is confirmed clean.

The review authorizes nothing beyond a later confirmation of the repairs; T remains `NOT_ACTIVATED`, and no hash/HEAD/source set was pinned. I edited no existing file and committed nothing.

Two questions to reduce uncertainty and improve the chain (per your standing rules):

1. On **C-4**, do you want the recommended fix (make `generic_harness.py`'s `__main__` the CLI, matching the pinned root) baked in as the *only* acceptable repair, or should the confirmation round also allow a reviewed amendment to `verification.py:PRODUCTION_ROOTS` to add a dedicated `scripts/officina_t_process.py`? The former keeps §1's "no core change" true; the latter is cleaner ergonomically but is a control-file amendment needing its own review.

2. Architecturally: the recurring root cause of C-1/C-2/R5/R7 is that the harness contract re-narrates ordering in prose that must match the already-signed hash dependencies in `runtime.py`. Would you want the v1.1 draft to **replace the §2 prose transitions with a single normative table generated directly from the code's `_EVENT_DATA_KEYS`/`build_*` hash-dependency graph** (event ⇽ record ⇽ charge edges), so contract and code cannot drift again? That would materially raise bit-exactness and cut future review rounds.
