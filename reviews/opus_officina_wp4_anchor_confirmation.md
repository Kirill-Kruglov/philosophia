# Opus 4.8 X-line — Officina WP-4 descriptor/use-time confirmation

**`OFFICINA_WP4_DESCRIPTOR_USE_XLINE_CONFIRMED`**

Reviewer: Opus 4.8 (X-line, bounded delta confirmation). Repository:
`/home/master/llm_projects/philosophia`, repair range `b9e2ed3..c359aa4` (four
files: `ledger.py`, `world.py`, the WP-4 note, `test_officina_world.py`; HEAD
`29c49db` differs only by prompts). **I created no real world, entropy, candidate,
root, lock, escrow, datum, outcome, or T/Q/C execution; I prepared/executed no
T-activation candidate; the committed T state remains pristine and `NOT_ACTIVATED`;
my probes used `/tmp` fixtures only. Nothing committed; no existing file edited.**
`git diff --check` clean. I recorded committed genesis hashes before and after the
adversarial battery and confirmed byte-identity.

Sol's two residual counterexamples — pathname-based (not descriptor-anchored)
ledger identity, and a use-time surface relabel falling through to C membership —
are closed and independently reproduced-then-rejected. The accepted WP-3 design and
all previously confirmed WP-4 surfaces are unregressed.

---

## Bounded confirmation

### Q1 — ledger/head substitution after issuance: CLOSED via held descriptors.

The harness now opens and **holds** anchor descriptors for the root, ledger, and
head at issuance (`_open_anchor` with `O_RDONLY|O_CLOEXEC|O_NOFOLLOW`, plus
`O_DIRECTORY` for the root, and an `st_mode` file-type check), and
`_require_test_contact_harness` re-verifies each on every use via
`_anchor_matches` = `os.path.samestat(os.fstat(fd), path.stat(follow_symlinks=
False))` — the current path must resolve to the **same inode** the held descriptor
already anchors. Reproduced (all rejected before any mutation):

| Attack | Result |
|---|---|
| ledger inode swap at the same path (even identical bytes) | `PermissionError` "test contact ledger changed identity" |
| head inode swap at the same path | `PermissionError` "test contact ledger changed identity" |

The check is stricter than the prior path-stat: an inode substitution with
byte-identical content is now caught (the held fd anchors the original inode).
Descriptor lifetime: FDs live in `__slots__`, are `O_CLOEXEC` (not leaked to
subprocesses), and are released by `close()` / the `__enter__`/`__exit__` context
manager / `__del__` (with partial-open cleanup on a failed `__init__`); `_closed`
makes close idempotent and use-after-close raises. Protected-alias
(`os.path.samefile` vs both committed T paths), symlink, resolved-parent-is-root,
and full ledger integrity (`entries()` → hash-chain + `_verify_head`) are checked
on every use.

### Q2 — the append operates on the anchored object, not a matching pathname: PROVEN.

`AppendOnlyLedger.append` now accepts `expected_file_descriptor` and, after opening
the path (`O_CLOEXEC|O_NOFOLLOW`), verifies
`os.path.samestat(fstat(opened), fstat(expected))` **before** the `flock` and any
write, raising `LedgerIntegrityError("opened ledger differs from its anchor")`
otherwise. Reproduced: with an anchor fd on file A and a swap to a new inode B at
the path, `append(expected_file_descriptor=anchor)` raises and **B is left
unmutated** — rejection occurs before mutation, even when the caller reaches
`append` directly (the harness `_require` bypass). `record_test_t_contact` passes
`expected_file_descriptor=harness._ledger_fd`, so every contact append is
double-anchored (harness re-check + append re-check).

### Q3 — atomic-head handoff: CORRECT; no falsely advanced state.

After the append, the repair opens a **new** head descriptor, verifies it against
its own path and re-parses full ledger+head integrity, and only then swaps
`harness._head_fd` and closes the **previous** head fd — the old descriptor is
retained until its successor is open and verified. On any failure it closes the new
fd, keeps the old, and does **not** advance `harness._state` or `_head_fd`.
Reproduced: two legitimate sequential contacts succeed (cumulative
`device_nanoseconds` 1000+2000 = 3000; two hash-chained ledger entries), the head
re-anchoring absorbing each atomic head replacement while the in-place ledger fd
stays anchored.

### Q4 — use-time surface relabel and C fall-through: CLOSED.

`_require_world_capability` now enforces `capability.surface is Surface.T` **at
use** (in addition to construction), and `_surface_moduli` **raises**
`ValueError("world surface has no registered modulus set")` for any surface other
than T/Q/C — eliminating the prior `else → "C"` fall-through. Reproduced via
`object.__setattr__` (bypassing the frozen constructor): relabeling a T capability
to `Surface.C` or to a fake surface both raise `PermissionError("pre-root test
world capability is T-only at use")` at `evaluate_test_query` **before**
classification, and `_surface_moduli("FAKE")` raises rather than returning C
membership. (Direct `_surface_moduli(Surface.C)` still returns the 24 C moduli, but
no T-capability use path can reach it.)

### Q5 — no regression: CONFIRMED.

Frame hash (`cc54cd2e…`) and `SIGNED_CONTRACT_SHA256` unchanged; the total ordered
classifier and T oracle behave identically (`{"u":"RL","v":"R"}` → `0`); artifact
non-promotion is intact (`require_promotable(Q)` → `QuarantineViolation`, promotable
is structurally `False`); the four real entry points still raise
`ExecutionNotAuthorized` (interlock unchanged by this diff); the source-quarantine
allowlist still covers `world.py`/`ledger.py` (the new `os`/`pathlib`/`fcntl` usage
is within the allowed absolute imports, no `getattr`/`eval`/dynamic import). No
WP-3 cell moved.

### Suites, verifier, genesis

Targeted four-file suite → **69 passed**; full `pytest` → **236 passed**;
`scripts/verify_officina_wp12.py` → **OK: quarantined and inactive**. The committed
`T_LEDGER.md` and `T_LEDGER.md.head.json` are **byte-identical** before and after
the adversarial battery; the exact `successor/officina/` bootstrap set is untouched
and `NOT_ACTIVATED`.

---

## Residual findings (this bounded delta)

No Critical, Major, or blocking finding. Residuals (accepted procedural threat
model, unchanged in kind, weaker in impact):

- **A-r1 — private-sentinel forge remains constructible but inert.** Importing
  `world._CONTACT_TOKEN`/`_WORLD_TOKEN` can forge a harness/capability (deliberate,
  per the stated "accidental-execution guard, not a security sandbox" model), but a
  forged harness fails the fd-anchor/protected-alias re-checks and the append's
  `expected_file_descriptor` anchor, and a forged/relabeled capability fails the
  use-time T-only check — so the forge grants no committed-artifact write and no
  real or Q/C execution.
- **A-r2 — sub-call filesystem TOCTOU** in the head handoff (between `_open_anchor`
  and `_anchor_matches`, and between append and re-open) is bounded by the append's
  own anchor verification and the integrity re-parse (`entries()` → `_verify_head`);
  the accepted non-adversarial-filesystem model.
- **A-r3 (minor, non-blocking) — descriptor cleanup relies on `close()`/context
  manager; `__del__` defers to GC** if a caller neither closes nor uses `with`. For
  a short-lived test harness this is immaterial; the WP-4 note should recommend the
  context-manager form.

## Next gate

A positive verdict authorizes **only the preparation (drafting) of a separately
reviewed T-activation candidate** — subject to its own bounded X/Y review. It
authorizes **no** T activation, real world, entropy, E1/E2/E3 spend, candidate
registration, learner run, Q/C activity, root, lock, escrow, datum, outcome, or
claim movement. The committed T state remains `NOT_ACTIVATED`; WP-6 (Q contract)
remains a separate downstream gate.

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
