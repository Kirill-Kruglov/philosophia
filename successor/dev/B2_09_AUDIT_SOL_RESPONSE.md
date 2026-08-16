# B2_INSTRUMENT_REPAIR_09 — bounded numerical audit

## Answer

No number actually emitted in `B2_INSTRUMENT_REPAIR_09.md` is shown to be wrong, leaked, or non-comparable to a number against which it is compared. The decisive qualification is that this is not a completed instrumentation result: the artifact is explicitly `STOP_NO_CUDA`, and every experimental section 3–10 is `NOT_PRODUCED`. The verdict below therefore covers only the emitted hashes, frozen constants, stopped-run metadata, and the accurately disclosed absence of measurements. It does not validate nonexistent held-out, `road_gap`, probe, component, conditional-fix, M3, or two-seed results.

The four supplied authority pins match their files. The emitted script hash `f5b23a9026111870d6cc93b858b807868f2fd072bbbcfab0802213cc4bb0a2e6` also matches the current script bytes. The report, JSON, and log consistently state `STOP_NO_CUDA`. Pilot 08's exact JSON wall time is `2431.7828259998932` seconds, which supports the repair log's rounded `~2432 s`. The separate partial-attempt log supports the reported stop after checkpoint 350; its `~29 min` is explicitly approximate and is not used as an experimental comparison.

## Eight-item audit

1. **Held-out contamination (R2): `NO_FINDING`.** No held-out curve or held-out scalar was emitted: [B2_INSTRUMENT_REPAIR_09.md](B2_INSTRUMENT_REPAIR_09.md) lines 32–34 say `NOT_PRODUCED`. Consequently there is no logged held-out number that contamination could have changed in this record.

2. **Firewall breach in new metrics (R3): `NO_FINDING`.** No `road_gap` or alignment number was emitted: report lines 40–42 say `NOT_PRODUCED`. There is therefore no logged new-metric number in which a firewall leak can be demonstrated.

3. **Length ruler in `road_gap` (R3): `NO_FINDING`.** No `align_same`, `align_diff`, or `road_gap` value exists in the emitted Markdown or JSON. Under the prompt's numerical-only rule, a concern that could affect a future execution but changes no emitted number is not a finding in this audit.

4. **Init baseline mismatch (R4): `NO_FINDING`.** No `init`, trained probe accuracy, or `delta_*` was produced: report lines 44–46. There is no logged delta whose baseline can be mismatched.

5. **Component arithmetic (R1): `NO_FINDING`.** No loss/component or `mean_std` observation was produced. The source formulas for the optimized total at [b2_instrument_repair_09.py](b2_instrument_repair_09.py) lines 566–580 and the logged decomposition at lines 583–606 are algebraically identical, but no runtime arithmetic or pre/post surface comparison exists to audit numerically.

6. **Frozen constants (silent drift): `OK`.** The constants emitted at report lines 17–29 equal the source values at [b2_instrument_repair_09.py](b2_instrument_repair_09.py) lines 93–109 and the corresponding Pilot 08 values. The optimized `vicreg_pair_loss` expression is unchanged from Pilot 08. All input hashes and the stated repair-script hash recompute exactly.

7. **Conditional-fix discipline: `NO_FINDING`.** The report says `conditional_fix_fired = not evaluated` and `mean_std ... NOT_PRODUCED` at lines 58–61. No pre-fix/post-fix number or rerun result exists, so no logged number can have been altered by an undeclared conditional change.

8. **Seed accounting: `NO_FINDING`.** The frozen seed tuple is correctly emitted as `(0, 1)`, while the report and JSON explicitly say the full seed-0/seed-1 pilot was not executed. No seed outcome was emitted, dropped, or re-rolled; equally, there is no two-seed result to validate.

No repair or recomputation is required for the numbers in the stopped artifact. A scientific or instrumentation verdict cannot be extracted from it because the requested measurements do not exist.

B2_09_NUMBERS_TRUSTWORTHY=YES
