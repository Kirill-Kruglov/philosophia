`REVISE_OFFICINA_P1_WATCHDOG_V2_8`

Review written to [sol_officina_p1_watchdog_v2_8_final_y_confirmation.md](/home/master/llm_projects/philosophia/reviews/sol_officina_p1_watchdog_v2_8_final_y_confirmation.md).

Key findings:

- Blocking: Y27-B1 remains open. `IR-3` contradicts `VP-2`/`CK-12`; row 111 assigns missing M4 keys two codes; and `CK-13` lacks deterministic ordering among overlapping mismatch codes.
- Blocking: the 89 rows correctly describe the reduced standard-library closure, but not all code executed at A-10. Python also executes the parent package initializers plus `canonical.py` and `interlock.py`; these are not roots, members, rows, or digest-bound dependencies.
- Major: B14 is present in `IR-4`, §P1-14.5, packet §3, and row 115. Whole-graph completeness remains overstated because the derivation excludes relations defined in `TS-2` and `TS-5`.
- Allowlist decision: removing `subprocess` is a legitimate consistency repair, not a new unsigned watchdog choice. The reduced union triggers no at-fork registration; adding `subprocess` adds exactly eight modules and causes `threading` to call `register_at_fork`. However, the accepted generic-harness chain did originally grant a subprocess launcher capability; the later P1 architecture had already expressly superseded it.
- Topology: exactly two tracked roots, two absent bootstraps, and `generic_harness.py` absent from the commit but present as unrelated untracked work. It supplied no evidence.
- Preserved: A0.4, rollback qualifications, FS-1..FS-5, TR-2(a)/(b), row 106(i) expected PASS, external-freshness absence, option symmetry, identity boundary, `T = NOT_ACTIVATED`, and programme claim `OPEN`.

Next boundary: documentation-only v2.9 or equivalent repair followed by fresh bounded X/Y review. Kirill’s watchdog selection is not yet authorized. No existing files were modified and no commit was made.
