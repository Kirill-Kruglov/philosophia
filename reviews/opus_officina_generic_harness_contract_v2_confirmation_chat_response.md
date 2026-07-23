I completed the single bounded confirmation and wrote exactly one file: `reviews/opus_officina_generic_harness_contract_v2_confirmation.md` (first line the required token; git shows only that new untracked file, nothing else changed).

## Verdict: `REVISE_OFFICINA_GENERIC_HARNESS_V2_XLINE`

The v2 draft is a strong, faithful replacement. **All twelve of my v1 findings are correctly and durably closed:**

- **C-1..C-4** (record-before-event valid close; INVALID record + no-process split; three-case recovery charge restored verbatim from v2.1 §1; roots/CLI aligned to the pinned tuple) — confirmed against `runtime.py`, `activation.py`, and `verification.py:PRODUCTION_ROOTS`.
- **R5..R12** (single §3a idempotent cache successor; G5 sibling settlement adopted; charge-hash seed pinned; exhaustion-vs-reservation split; draft-manifest ordering channels *removed*; static adapters; CPU-only import allowlist; ownership/type pins) — all honored in rule/schema/ordering form.
- Roots/CLI/import/ownership (mandate point 3) match the pinned immutable verifier exactly; isolation-and-promotion, closed recovery disposition, and the crash-cut table are sound.

**Why REVISE (finite, localized, in the exact compounds you asked me to check):** the *new* Y-line machinery (§4d conserving batch, §2a dominance, §2c.12b sibling force-close) contradicts the immutable, tested constructor `runtime.py:build_process_record`:

- **M-1 (Critical):** a zero-share / `R=0` unknowable live stream cannot be invalid-closed by the pinned constructor (it demands a positive `T_DEVICE_TIME_CHARGED` immediately preceding the `T_RUNTIME_INVALID`, and `charge_device_nanoseconds` refuses at cap). Closure **Example C** is unimplementable via the intended path — and may require a reviewed metering-core amendment, which would falsify the §12 "no core change" claim.
- **M-2 (Critical):** exhaustion-vs-invalidity dominance is not single-valued — §2a ("never reinterpreted as valid exhaustion", terminal G5) contradicts §2c.8/§4d/**Example B** ("appends `T_ENVELOPE_EXHAUSTED` once"). Terminal state (G5 vs G7) and the ledger event set diverge.
- **M-3 (Major):** §4d's "charges then terminals" order is incompatible with the pinned charge→`T_RUNTIME_INVALID` per-stream adjacency (`sequence+1`, `previous = charge hash`); interleaving must be pinned.
- **M-4 (Major):** the `invalid_cause` of a collaterally force-closed *healthy* sibling is unspecified (the 5-value enum has no fitting value).
- **M-5 (Minor):** "the detail record lists every observed cause" isn't representable in the single-`invalid_cause` signed schema.
- **M-6 (Major):** the overdue-resume second `T_OPERATIONAL_PAUSE` reusing "the same checkpoint" collides with `checkpoint.py:verify_resume`'s `ledger_head_before` check and the non-pending pre-state requirement.

Each has exact replacement guidance (R-M1..R-M6), all localized to §2a/§2c.8/§2c.12b/§4d/§6b + Examples B–C — not a redesign of the resolved material. Two independent implementers would currently diverge on terminal classification, the ledger event set, zero-share closes, sibling cause, and G4-power-loss resumability. A v2.1 applying these should be confirmable and two-implementer-deterministic. The verdict authorizes nothing beyond a future informed signature; T remains `NOT_ACTIVATED`.

One process question, since it bears on whether this can close in one more round: **M-1** may not be fixable by wording alone. Do you want the v2.1 author to (a) constrain the batch so a case-(b) overrun crossing the cap always settles siblings with ≥1 ns *before* the cap (pure contract fix, no code change), or (b) treat a zero-charge invalid-close as a named, reviewed `runtime.py` amendment? Option (b) would mean the "no core change" claim must be dropped, and the metering-core amendment would need its own bounded review before signature.
