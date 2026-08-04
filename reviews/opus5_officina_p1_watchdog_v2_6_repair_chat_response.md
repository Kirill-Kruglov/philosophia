Now I'll build the v2.6 shared normative block.

Now the closure.

Done. Four new files; no existing file modified, nothing committed.

## Deliverables

| File | SHA-256 | Lines |
|---|---|---|
| [packet v2.6](successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_6_CORRECTION.md) | `1dbb99b7390c943a…` | 566 |
| [amendment v1.3](successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_3_DRAFT.md) | `c3da2a7d24d0cea0…` | 2189 |
| [composite v1.6](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_6.md) | `6283d081df3eb397…` | 4518 |
| [closure](reviews/opus5_officina_p1_watchdog_freeze_choice_v2_6_closure.md) | `6fc35260b2a594a6…` | — |

Closure emits `READY_FOR_OFFICINA_P1_WATCHDOG_V2_6_INDEPENDENT_XY_CONFIRMATION`. Joint block byte-identical in both files (`4addce73…`).

## R1 — schemas and validators
`MS-4` now fixes all 20 keys with types, plus one canonical `reachable_closure` shape (6-key elements, `kind` from 4 literals, inner array sorted+distinct, outer array sorted by `module`, distinct, closed under itself). `MS-7`/`IR-3` fix mandatory schema literals, versions, nested shapes and array order. `MS-10` gives one `created_utc` grammar + semantic validator, provenance-only. `TS-1` states the three pre-selection paths as literal strings (the v2.6 successors). `TS-2` → `A1..A17`, `TS-5` → `B1..B18`, exhaustive, each clause naming its code; no field passes on presence alone. Fixtures: rows 105, 106(j), 111, 113.

## R2 — temporal honesty
New `FS-1..FS-5`. `FS-1` enumerates what `G-11` proves; `FS-2` names each withdrawn claim (OR-11's early-record refusal, 106(h), packet §3.2, closure §4.1) and lists the four indistinguishable pairs; `FS-3` keeps `OR-1..OR-11` a mandatory operator obligation; `FS-4` adds `PROCEDURE_VIOLATION_OBSERVED` (25th code) for contemporaneous violations → process/control invalidity, no production entry; `FS-5` puts the rest inside the residual. No HSM/oracle/notary/log added — stated in the bytes.

## R3 — rollback
`TR-2` now has clause (b): complete coherent rollback passes and is **not** refused. The "every post-hoc substitution" claim is replaced by the exact eleven proper-subset cases with their clauses, plus a forbidden-sentence list. Row 106(i) `OUTSIDE_GUARANTEE_COHERENT_ROLLBACK` asserts `G-11` **passes** — the row fails if it asserts a refusal. Threat-model string extended so Kirill reads the rollback residual at signing.

## R4 / R5
`IR-4` states the actual directed graph edge by edge; row 115 asserts the redundant `M4`/`M7` edges positively; no uniqueness of attester or external attester claimed. Members 53 → **57** (M2 39→43, mechanical only); 21/21 pairs reproved disjoint; 51 provenance rows = 43+7+1; all 50 M2+M3 digests verified against disk. Counts: **225 = 171 + 54**, 141 amendment tags, 25 failure codes.

The identity signature is at `XS-1`: recorded as author state, **not** a member (with the reason), does not accept `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`, not scientific evidence, does not unblock either cell — and four named obligations on the later combined binding.

## Worth flagging

- **The property Y asked for is not delivered.** Sol said fail-closed order/replay rejection *requires* an external freshness anchor, and that confirmation on that property depends on it. You directed the honest procedural route, so v2.6 narrows instead. A Y reviewer may still return `REVISE` on that basis — the closure §8.2 says so explicitly rather than burying it.
- **`reachable_closure`'s canonical shape is fixed, but its correctness against §P1-3.3 is unproven** — §P1-3.3 stays a prose aid that `MS-4` never reads. Closure §8.6.
- Rows stayed at 92..115 (M6 rule and `row_count 24` preserved); the new schema fixtures went into existing rows rather than extending the range.
