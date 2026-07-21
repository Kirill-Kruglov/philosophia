Written to `reviews/opus_officina_wp4_anchor_confirmation.md`.

## Verdict: `OFFICINA_WP4_DESCRIPTOR_USE_XLINE_CONFIRMED`

Sol's two residual counterexamples — pathname-based (not descriptor-anchored) ledger identity, and a use-time surface relabel falling through to C membership — are closed and independently reproduced-then-rejected; no regression, no WP-3 cell moved.

**Q1 — descriptor-anchored identity.** The harness now holds `O_NOFOLLOW|O_CLOEXEC` anchor fds for root/ledger/head at issuance and re-verifies each use via `os.path.samestat(fstat(fd), path.stat())`. Reproduced: a ledger inode swap **with identical bytes** and a head inode swap are both rejected ("test contact ledger changed identity") — stricter than the old path-stat. FD lifetime is `__slots__`-held, `O_CLOEXEC`, closed via `close()`/context-manager/`__del__` with partial-open cleanup.

**Q2 — append operates on the anchored object.** `append(expected_file_descriptor=…)` verifies `samestat(opened, anchor)` **before** `flock`/write. Reproduced: after a swap to a new inode, `append` raises `LedgerIntegrityError("opened ledger differs from its anchor")` and the file is **left unmutated** — rejection before mutation even on a direct-`append` bypass.

**Q3 — atomic-head handoff.** The old head fd is retained until the new one is opened, self-verified, and the ledger re-parses integrity; only then is it swapped and the old closed; failure advances no state. Reproduced: two sequential contacts succeed (cumulative device_ns 3000; two chained entries).

**Q4 — use-time T-only + no fall-through.** `_require_world_capability` re-checks `surface is Surface.T` at use, and `_surface_moduli` raises for any non-T/Q/C surface. Reproduced via `object.__setattr__` relabel to `Surface.C` and to a fake surface — both raise "pre-root test world capability is T-only at use" *before* classification; `_surface_moduli("FAKE")` raises rather than returning C membership.

**Q5 — no regression.** Frame hash (`cc54cd2e…`), classifier/oracle, artifact non-promotion (`require_promotable(Q)` → `QuarantineViolation`), and the four raising real stubs all intact; source-quarantine allowlist still covers the new `os`/`pathlib`/`fcntl` usage.

**Suites/genesis:** targeted **69 passed**, full **236 passed**, verifier **OK**, committed `T_LEDGER.md`+head **byte-identical** before/after the battery, still `NOT_ACTIVATED`.

**Residuals (accepted, weaker):** A-r1 (private-sentinel forge is now inert — fails fd-anchor/protected-alias/append-anchor and use-time T-only), A-r2 (sub-call head-handoff TOCTOU bounded by the append anchor + integrity re-parse), A-r3 (minor: `__del__` fd cleanup defers to GC — recommend the context-manager form in the note). No Critical/Major/blocking.

**Next gate:** authorizes **only preparation of a separately reviewed T-activation candidate** — no activation, real world, entropy, E1/E2/E3 spend, registration, learner run, Q/C activity, or claim movement; committed T stays `NOT_ACTIVATED`.

**Confirmed:** no existing file edited, one new confirmation file, no candidate prepared, T not activated, nothing committed; predecessor stays `OPEN`/`BLOCKED_LEVEL1_FEASIBILITY`, programme claim `OPEN`.
