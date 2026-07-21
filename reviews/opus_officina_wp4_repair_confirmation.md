# Opus 4.8 X-line — Officina WP-4 R1/R2 stricter-boundary confirmation

**`OFFICINA_WP4_R1_R2_XLINE_CONFIRMED`**

Reviewer: Opus 4.8 (X-line, bounded repair confirmation). Repository:
`/home/master/llm_projects/philosophia`, repair range `3132f79..7786137` (three
files: `world.py`, the WP-4 note, `test_officina_world.py`; HEAD `a0f07d9`
differs only by prompts). **I created no real world, entropy, candidate, root,
lock, escrow, datum, outcome, or T/Q/C execution; I prepared no T-activation
candidate; the committed T state remains at genesis and `NOT_ACTIVATED`; my
probes used `/tmp` fixtures only. Nothing committed; no existing file edited.**
`git diff --check` clean. I recorded the committed genesis hashes before and
after an adversarial probe battery and confirmed byte-identity.

Both Y-line dataflow blockers are closed and independently reproduced-then-rejected;
the previously accepted frame, verifier, classifier, oracle, and fail-closed
entry points are unregressed and no WP-3 cell moved. Only accepted procedural
residuals remain — now strictly weaker in impact.

---

## Bounded questions

### Q1 — R1 committed-ledger counterexample: CLOSED.

The former `record_test_t_contact(state, envelope, ledger)` signature — the route
Sol exploited by passing an activated dummy state + the production ledger — no
longer exists; the only route is an **internally issued `TestTContactHarness`**
that owns a **fresh temporary ledger and its own accounting state/envelope**.
`issue_test_t_contact_harness` requires a `TestOnlyCapability` and the private
`_CONTACT_TOKEN`, an **absolute, non-symlink, resolve-stable** `temp_root` that is
a directory **outside the repository** (`not is_relative_to(_REPOSITORY_ROOT)`),
and a **newly created** ledger, and it rejects any file that `os.path.samefile`s a
committed T artifact. Reproduced (all rejected):

| Attack | Result |
|---|---|
| harness root in-repo (`successor/officina`) | `PermissionError` "outside the repository" |
| relative-path root | `PermissionError` "must be an absolute Path" |
| symlink root → repo | `PermissionError` "must not use path aliases" |
| duck/forged harness (no issued token) | `PermissionError` "requires an issued test harness" |
| post-issuance hardlink of temp ledger → committed `T_LEDGER.md` | `PermissionError` "test contact ledger changed identity" |
| caller supplying production state/envelope/ledger | signature no longer accepts them |

A legitimately issued harness returns a `TestTContactState`. Even a
deliberately forged harness (private-sentinel import) cannot touch the committed
artifacts: `_require_test_contact_harness` re-runs `_reject_protected_alias`
(samefile vs both committed T paths) and re-checks `is_symlink`, resolved-parent,
and `(st_dev, st_ino)` identity on **every** use.

### Q2 — validation order and inode handling: CORRECT.

In `record_test_t_contact`, `_require_world_capability` → **`_require_test_contact_
harness`** (root identity, no-symlink, resolved-parent-is-root, inode identity,
protected-alias, ledger re-parse) runs **before** the surface/charge checks, the
oracle evaluation, the accounting charge, and the ledger append — so protected-path
separation and ledger integrity are established before any oracle/accounting/
persistence. The legitimate atomic append replaces the **head** file (new inode);
the repair re-pins `harness._head_identity` to the post-append inode, while the
**ledger** file (appended in place under `flock`, same inode) stays pinned
throughout — so the re-pin absorbs the legitimate head-inode change without
weakening later substitution detection (a malicious head swap between calls yields
a different inode than the last legitimate append and is caught).

### Q3 — return value cannot be a production `TState`/checkpoint: CONFIRMED.

`record_test_t_contact` now returns a `TestTContactState` (frozen dataclass:
`device_nanoseconds`, `purpose`, `test_only=True`) — `isinstance(_, TState)` is
`False`, it has no `to_mapping`/schema, so it cannot be fed to `TState.from_mapping`
or any checkpoint. Every durable entry is `event=T_TEST_ONLY_WORLD_CONTACT`,
`test_only:true`, `schema=…test-t-contact.v1`, in a temp ledger outside the repo.

### Q4 — R2 Q/C capability before roots: CLOSED.

`TestWorldCapability.__post_init__` now raises `PermissionError` for any surface
other than `T` ("pre-root test world capability is T-only"). Reproduced: the
factory `test_world_capability(Surface.Q|Surface.C)` and the direct constructor
(even with the `_WORLD_TOKEN`) both **raise**; no test callable can obtain a Q/C
capability, so **no test callable returns Q/C oracle bytes**. A T capability
contacting a frame modulus (26, 65) is refused ("modulus is outside the T test
surface"), and the T surface set `[10,25]∪[166,205]` is disjoint from the frame
`[26,65]` — **T rejects the full frame**. Q/C admission remains structurally
fail-closed in the WP-1/WP-2 provenance layer (promotability is a property fixed
to `False`; `admit(Q|C)` always raises), so any test artifact fails Q/C admission.

### Q5 — no regression; no WP-3 cell moved: CONFIRMED.

The frame hash (`cc54cd2e…`), `SIGNED_CONTRACT_SHA256` (`6085d9b6…`),
`SIGNED_WP3_SIGNATURE_SHA256`, the canonical verifier, the total ordered raw-wire
classifier (valid → `0`; STRUCTURE/BYTE/LENGTH ordering intact), the T oracle
semantics, and `N_MIN=26`/`N_MAX=65`/`LAMBDA=140`/`C_POSITIONS={1,3,5}`/
`Q_POSITIONS={2,4}`/tokens are all unchanged (probed). `generate_real_world`,
`run_real_t`, `launch_q`, `execute_c` still raise `ExecutionNotAuthorized`. The
diff adds only the harness machinery, the T-only constraint, and the contact-hook
signature change; it touches no frame formula, verifier, classifier, oracle, real
stub, or WP-3 constant.

### Q6 — suites, verifier, genesis identity: CONFIRMED.

Targeted four-file suite → **65 passed**; full `pytest` → **232 passed**;
`scripts/verify_officina_wp12.py` → **OK: quarantined and inactive**. The
committed `T_LEDGER.md` and `T_LEDGER.md.head.json` are **byte-identical** before
and after the adversarial probe battery (SHA-256 `61cf79e0…` / `04bff996…`
unchanged); the exact `successor/officina/` bootstrap set is untouched and remains
`NOT_ACTIVATED`.

---

## New or residual findings

No Critical, Major, or blocking finding within the bounded repair. Residuals
(accepted procedural threat model, unchanged in kind and **weaker in impact** than
before):

- **R-r1 — private-sentinel forge still constructible, but now inert against the
  committed ledger.** Importing `world._CONTACT_TOKEN`/`_WORLD_TOKEN` can forge a
  harness/capability (deliberate, per the stated "accidental-execution guard, not
  a security sandbox" model), but a forged harness still fails
  `_require_test_contact_harness`'s protected-alias/inode/symlink re-checks on use,
  so it cannot write a committed T artifact and grants only a test-only, T-surface,
  temp-ledger contact. No real execution is reachable.
- **R-r2 — within-call filesystem TOCTOU** between the protected-alias check and
  the append is bounded by the ordering (check before persist) and the per-call
  inode re-pin; it is the accepted procedural (non-adversarial-filesystem) model.

## Next gate

A positive verdict authorizes **only the preparation (drafting) of a separately
reviewed T-activation candidate** — subject to its own bounded X/Y review. It does
**not** authorize T activation, a real world, entropy, an E1/E2/E3 spend,
candidate registration, a learner run, any Q/C activity, a root, lock, escrow,
datum, outcome, or claim movement. The committed T state remains `NOT_ACTIVATED`;
WP-6 (Q contract) remains a separate downstream gate.

## Negative space

The predecessor line remains immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`;
its records are non-citable and chose no value here. Officina's T and Q can never
earn, kill, or boundary-label C1–C6; a future Q pass is a spendability gate fact
only; S is unavailable; only a valid, independently locked C execution may move an
Officina claim — within its selection-conditional, selected-frame, orientation,
device, and learner-seed scope. Test-only oracle contacts are non-citable
engineering, never scientific evidence. Censored/`UNKNOWN`/every invalid state are
never success, equivalence, a boundary, or learner impossibility.
`PROOF_CORE`/`PROOF_STRONG` remain earned by nothing; the programme claim stays
`OPEN`.

I edited no existing file, created exactly one new file (this confirmation),
prepared no T-activation candidate, activated no T state, and committed nothing.
`essay/OUTLINE.md` untouched. My actions were reading the repair diff, code, and
note, and running the read-only reproductions, suites, verifier, and genesis
byte-identity check above.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
