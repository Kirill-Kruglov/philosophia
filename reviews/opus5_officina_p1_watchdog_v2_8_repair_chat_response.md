All six inputs match. Reading the two new reviews.

Now the decisive technical work — auditing the real role-import closure.

The empirical diff hides startup-preloaded modules. Computing the static edge closure — the same method the confirmed 14-row value uses.

**Decisive finding.** `threading.py` line 1705–1706 at module scope calls `os.register_at_fork`. Let me confirm the full impact and test the reduction.

The reduction is clean and decisive. Now the full audit of the reduced closure.

Driver imports polluted the measurement. Redoing with a clean two-phase measurement.

All 14 confirmed bootstrap rows reproduce exactly. Now the boolean and branch audit.

Runtime differential is clean: no signal handler changed, no thread created, no hook installed. Finalizing the canonical value with correct relative-import resolution.

Audit complete and decisive. Verifying repository state for R4.

Building the v2.8 governing bytes. First the canonical closure table text, generated mechanically.

Now the core repair — replacing the validation phases and check chain.

Block is consistent. Now building composite v1.8.

Composite verified. Building amendment v1.5 with the re-anchored line.

All counts verified. Writing the packet.

Both remaining occurrences are explicit withdrawals. Writing the closure.

## Verdict

```text
READY_FOR_OFFICINA_P1_WATCHDOG_V2_8_FINAL_XY_CONFIRMATION
```

`BLOCKED` was not returned — but only just. The audit **did** find a real violation, and a contract-compatible reduction closed it without a new author decision.

## Outputs

| Path | SHA-256 |
|---|---|
| [packet v2.8](successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_8_CORRECTION.md) | `5666d2bf9cee3c4404cc1f26ac13050a40403af9b4631fa774a1bfacbe481ca8` |
| [amendment v1.5](successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_5_DRAFT.md) | `28b57c47f89f775199095717111e37a4e588628aa64b2801812f30814711efd4` |
| [composite v1.8](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_8.md) | `6b867790707ae7999b31c1ad3dd56a1d4b195efd8f7a8b2bda4c2b065a352176` |
| [closure](reviews/opus5_officina_p1_watchdog_freeze_choice_v2_8_closure.md) | `fd0045041516baa419b9c8fd01054bcf2fab360d7af874203626070454db3585` |

Joint block byte-identical in both files, 2108 lines, `8dd14435…5361c2c1`. Anchor token re-scoped to `V2_8`, cardinality 1, zero stale `V2_7` lines. All six inputs unchanged; the untracked `generic_harness.py` untouched (mtime 2026-08-03); nothing committed.

## Combined closure cardinality

**89 rows** — BUILTIN 29, FROZEN 13, EXTENSION 2, PURE_PYTHON 45; 76 distinct names in `transitive_imports`, all rows; 267/267 booleans false. `CANON` = 20534 bytes, `aa974e0c…20ee`, with direct value comparison as the primary check. **The 14 confirmed bootstrap rows are preserved byte-identically in kind and array** — verified mechanically.

## Allowlist reduction

`generic_harness.py`'s scoped entry loses exactly one name, **`subprocess`** (17→16). With it present, `threading` enters every role process including the WATCHDOG — and **`threading`'s module-level code calls `os.register_at_fork`**, alongside `signal`, `select` and `selectors`, all four named by §P1-3.2 itself as permitted in no file. The removal is *determined*, not chosen: `S-12`, test 8 and the future-edit surface already forbid `subprocess` on every path of that file. Global 19-name default and both bootstrap entries untouched. After the reduction, zero rows start a task, register at fork, or install a handler — confirmed by runtime differential (no signal disposition changed, thread frames 1→1).

## Check topology

13 → **15 checks**, now a literal topological order: `CK-5` locate record → `CK-6` validate record → `CK-7` members exist/hashed → `CK-8` M4,M7 structural → `CK-9` `TS-2B` (A15–A17) → `CK-10` M4 semantics → `CK-11`–`CK-15`. `TS-2` split into `TS-2A` (A1–A14, reads only Stage A) and `TS-2B` (M4-dependent). Both duplications removed: `HISTORICAL_BYTE_MOVED` owned only at `CK-7`, `MEMBER_STALE` only at `CK-13`. All six mandated multi-fault states resolve to one code each. Codes stay 26; members 61→65; loci 233→236.

## Graph delta

Added `Stage B --selected_option_token equality (B14)--> Stage A` at `IR-4`, §P1-14.5, packet §3, row 115. `IR-4` now re-derives over **option-, id-, key-, count- and assertion-bearing** relations, not just digest/path/signature — closing the class of error, not the instance. `A9` named as deliberately intra-object.

## Residuals

`TR-2(a)/(b)` unnarrowed; the §A0.4 anchor limitation; **MS-11.1 is now an 89-row factual claim** — six times what X reproduced, and the most falsifiable thing in the pair; and one new disclosure: **`_thread` is resident before any contract import runs**, so §P1-3.2's rationale for excluding `signal` is factually obsolete (rule preserved, test row 13 clarified).

Two items are put to the reviewers as questions rather than presented as settled: the 89-row value (X2), and whether the reduction was legitimate or `BLOCKED` was the better call (Y4).

## Next boundary

Bounded independent X/Y confirmation on these exact bytes by reviewers who did not author v2.3–v2.8. No selection, key, artifact, code edit, test run, install, activation or claim movement authorized. `T = NOT_ACTIVATED`; programme claim `OPEN`.
