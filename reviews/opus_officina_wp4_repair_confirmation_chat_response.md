Written to `reviews/opus_officina_wp4_repair_confirmation.md`.

## Verdict: `OFFICINA_WP4_R1_R2_XLINE_CONFIRMED`

Both Y-line dataflow blockers are closed and independently reproduced-then-rejected; the previously accepted surfaces are unregressed and no WP-3 cell moved.

**Q1 — R1 (committed-ledger) closed.** The exploitable `record_test_t_contact(state, envelope, ledger)` signature is gone; the only route is an internally-issued `TestTContactHarness` owning a **fresh temp ledger outside the repo**. Reproduced-and-rejected: in-repo root, relative path, symlink root, duck/forged harness, and a **post-issuance hardlink of the temp ledger to the committed one** (caught by `(st_dev,st_ino)` inode pinning); a legit harness returns a `TestTContactState`. Even a private-sentinel-forged harness can't touch committed T artifacts (`os.path.samefile` protected-alias re-check every call).

**Q2 — order/inode correct.** Harness + protected-path + ledger integrity are validated *before* oracle evaluation, accounting, and persistence; the legitimate atomic head-replace inode change is re-pinned while the in-place ledger inode stays pinned — so substitution detection isn't weakened.

**Q3 — return can't be production `TState`.** `TestTContactState` is a distinct frozen dataclass (`isinstance(TState)` False, no `to_mapping`, `test_only=True`); durable entries are all `T_TEST_ONLY_WORLD_CONTACT`.

**Q4 — R2 (Q/C before roots) closed.** `TestWorldCapability` is now **T-only**: factory and direct constructor both raise for Q/C; no test callable returns Q/C oracle bytes; a T capability contacting frame moduli 26/65 is refused; T surface `[10,25]∪[166,205]` is disjoint from the frame; Q/C admission stays structurally fail-closed (promotable=False).

**Q5 — no regression.** Frame hash (`cc54cd2e…`), signed contract/signature hashes, canonical verifier, total classifier, T oracle, and all WP-3 constants/tokens unchanged; the four real stubs still raise. The diff adds only the harness, the T-only constraint, and the hook signature.

**Q6 — suites/genesis.** Targeted **65 passed**, full **232 passed**, verifier **OK**; the committed `T_LEDGER.md` + head are **byte-identical** before and after the adversarial battery (`61cf79e0…`/`04bff996…` unchanged), still `NOT_ACTIVATED`.

**Residuals (accepted, weaker than before):** R-r1 (a private-sentinel forge is now inert against the committed ledger — protected-alias/inode re-checks), R-r2 (within-call filesystem TOCTOU under the procedural model). No Critical/Major/blocking.

**Next gate:** authorizes **only preparation of a separately reviewed T-activation candidate** — no activation, real world, entropy, E1/E2/E3 spend, registration, learner run, Q/C activity, or claim movement; committed T stays `NOT_ACTIVATED`.

**Confirmed:** no existing file edited, one new confirmation file, no T-activation candidate prepared, T not activated, nothing committed; predecessor stays `OPEN`/`BLOCKED_LEVEL1_FEASIBILITY`, programme claim `OPEN`.
