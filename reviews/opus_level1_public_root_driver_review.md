# Opus 4.8 X-line — Level 1 one-shot public-root driver audit

Reviewer: Opus 4.8 (X-line, safety-critical). Repository:
`/home/master/llm_projects/philosophia` (not committed; **driver not run**; no
entropy authorized). Audited: `scripts/level1_draw_public_root.py`,
`src/philosophia/level1/public_root.py`, `tests/test_level1_public_root.py`, and
the `allocation`/`serialization`/`model` helpers they call, against the signed v3
lineage (v3.1 A2/A5; v3.1.1 C2/C3/C7). I ran the unit tests and `--help`, and
performed static/AST + whole-module entropy scans. I did **not** invoke the draw,
monkeypatch its entropy, or create any file under `.../allocation/`.

---

## Verdict

**`REVISE_LEVEL1_PUBLIC_ROOT_DRIVER`**

The protocol core is sound and safe: exactly one AST-pinned `secrets.token_bytes(32)`
call, after a durable exclusive pre-draw claim, in the order claim → draw →
transcript → commit, with a fail-closed invalidity route, `R_h` deferred, strict
separation from the escrow-secret panel seed, and a complete canonical transcript.
No Critical (no path yields a *quiet* second draw). But two Major issues must be
fixed before an irreversible draw is authorized: (M1) a benign `git commit` failure
mislabels a **durable, valid root** as "permanently spent," risking discard of the
one-shot; and (M2) the safety-critical failure/preflight/entropy surfaces are
under-tested. This is not a protocol contradiction (the pre-draw claim faithfully
implements no-redraw), so it is not blocked.

**Results:** `pytest tests/test_level1_public_root.py` → 7 passed; `--help` →
clean, no side effects; whole-module entropy scan → the only entropy primitive is
the single driver call (`model.py:71` `manual_seed` is deterministic PRF-seeding
and is not on the driver's path); `.../allocation/` does not exist.

---

## Findings

### Critical
None.

### Major

- **M1 — post-draw failure routing discards a valid root (`scripts/level1_draw_public_root.py:156–174`).**
  In the post-draw `try`, the transcript is durably written (`atomic_create`,
  fsync+replace) at `:168` *before* `_commit_transcript` at `:169`. If only the
  `git commit` fails (a hook, lock, or transient git error), the `except` at
  `:170–174` calls `_record_invalidity` and raises "public-root attempt is
  permanently spent," even though the root is safe in the committed-pending
  transcript. Following that message literally discards a valid one-shot root and
  (via a signed invalidity) authorizes a fresh draw — a wasted precious artifact.
  **Fix:** in the post-draw `except`, branch on transcript durability — if
  `TRANSCRIPT_RELATIVE` exists and parses, route to a **commit-pending recovery**
  state ("root durable; complete the commit; never redraw"), and record invalidity
  **only** when the transcript is absent (root truly lost).

- **M2 — safety-critical surfaces are under-tested (`tests/test_level1_public_root.py`).**
  The AST test (`:104–126`) scans only the driver script, not its imports, so a
  second entropy source hidden in a helper would pass (my manual scan confirms none
  today, but the guard should be mechanical). Untested: `_preflight` refusal on a
  dirty tree / non-empty index / HEAD mismatch / pre-existing artifact
  (`driver:54–75`); that `_commit_transcript` stages **exactly** `CLAIM`+`TRANSCRIPT`
  (`driver:109–122`); and that a transcript/commit failure routes to invalidity vs
  commit-pending (M1). **Fix:** add (a) a reachable-module entropy AST scan over
  `public_root`, `allocation`, `serialization`, and the driver (allowing the
  deterministic `manual_seed`); (b) `_preflight` refusal tests against a temp git
  repo in each bad state; (c) a `git add` path-restriction assertion; (d) a
  failure-injection test for the M1 branch.

### Minor

- **m1 — pre-draw claim is durable but uncommitted (`driver:141–147`).** The claim
  is fsync'd (blocks accidental rerun via `_preflight`) but committed only later
  with the transcript, so the crash-after-draw / before-transcript window is
  protected by a deletable local file. This matches the declared
  `procedural-not-cryptographic` threat model; document explicitly that the claim
  must not be deleted and that a crash after the draw requires a **signed
  invalidity**, never a rerun.
- **m2 — index-empty precondition is checked at preflight, not rechecked
  immediately before `git add` (`driver:65,111`).** For a one-shot, re-assert an
  empty index right before staging so nothing unexpected is swept into the commit.
- **m3 — HEAD binding needs a byte-identity confirmation.** `--expected-head`
  binds the *whole tree* to the reviewed commit (preflight requires HEAD == expected
  and a clean tracked tree), which is sufficient **iff** the driver/allocation/
  public_root/model bytes at the final HEAD equal the reviewed bytes; the operator
  must confirm `git diff <reviewed> <final> -- <those paths>` is empty.

---

## Answers to the required questions

1. **One reachable entropy call, outside loops, after preflight + durable claim?**
   Yes. Single `secrets.token_bytes(32)` at `driver:157`, AST-verified outside any
   loop, after `_preflight` and after the durable exclusive claim
   (`atomic_create(CLAIM)` at `:147`); whole-module scan finds no other entropy
   primitive (the `manual_seed` at `model.py:71` is deterministic and off-path).

2. **Crash states fail-closed; no quiet second draw?** Yes, mechanically.
   `atomic_create` (`public_root.py:127–149`) refuses if final/tmp exists, writes
   via `O_EXCL` tmp → fsync → `os.replace` → dir fsync. Any rerun is blocked by
   `_preflight` (`:67–71`) because CLAIM/TRANSCRIPT/INVALIDITY exist. **Gap (M1):**
   a post-draw commit failure over-routes a durable valid root to "spent." No path
   permits a *quiet* second draw; deliberate deletion is procedural per the declared
   threat model (m1).

3. **Deterministic/fallible inputs before the claim; bounded surface after?**
   Yes. Git checks, runtime config, environment, and all spec/lineage hashes are
   computed before the claim (`driver:132–140`). After the draw the surface is the
   deterministic `derive_public_allocations`/`build_transcript` plus two I/O steps
   (transcript write, git commit); the only non-deterministic post-draw step is the
   git commit, whose failure handling is M1.

4. **Transcript complete and unambiguous?** Yes (`public_root.py:49–94`): root
   hex, pre-draw HEAD, UTC timestamp, environment + fingerprint, `required_spec_hashes`
   (v3, v3.1) and `governing_lineage_hashes` (all nine lineage files incl. both
   signature records), public D/roles with `outcome_sample:"deferred-until-N3"`,
   process + witness attestation (`os_csprng_calls:1`, `root_bytes:32`, no-redraw),
   and explicit `forbidden_derivations` (real panel, realizations, ordering, salt,
   plaintext). Canonicalized (`canonical_json`) and golden-hash pinned.

5. **Commit restricted to claim+transcript; empty precondition; fixed trailers;
   failure analysis?** `_commit_transcript` (`:109–122`) `git add -- CLAIM
   TRANSCRIPT` only, `--no-gpg-sign`, four fixed co-author trailers; preflight
   requires a clean tracked tree and empty index (`:63–66`). Before/at commit
   failure → M1 (over-conservative invalidity); after commit success → durable,
   rerun blocked. Recommend the m2 recheck and the M1 split.

6. **Is `--expected-head` sufficient binding?** Yes for the tree, given
   preflight's HEAD-equality + clean-tree + empty-index checks (`:55–66`), **plus**
   the m3 byte-identity confirmation. Only **docs/review commits** (no change to the
   driver, `public_root`, `allocation`, `model`, or signed specs) may occur between
   this review and execution; the **final authorized HEAD** is the commit hash at
   draw time, recorded in the transcript's `git_head_before_draw` and matched to
   `--expected-head`, after confirming the source paths are byte-identical to the
   reviewed commit.

7. **Public root separated from the escrow-secret panel seed?** Yes.
   `derive_public_allocations` (`:97–124`) computes only D and roles and defers
   `R_h`; the driver never calls `sample_outcome_pairs` (test-asserted), never
   builds/writes/encrypts a panel (no panel/escrow code on the path;
   `forbidden_derivations` names them), runs no feasibility, creates no lock, and
   executes no trajectory/outcome. The public-root key cannot build a real panel
   (the real panel is keyed by a separate escrow-secret seed, and `DummyPanelBuilder`
   rejects a non-`test_only` key).

8. **Tests strong enough?** Partly. They catch a second driver-script entropy call,
   claim/draw/transcript/commit reordering, nonexclusive overwrite, transcript
   schema drift (golden hash), early `R_h` (`sample_outcome_pairs` absent +
   `deferred-until-N3`), and invalidity-route removal (`marker count==2`, after
   commit). **Missing (M2):** reachable-module entropy scan, `_preflight` refusal
   tests, `git add` path-restriction assertion, and the M1 failure-routing test.

9. **Claim sentinel faithful to the signed no-redraw protocol?** Yes — it is a
   faithful *strengthening*, not a contradiction. The signed A2 refuses if the
   transcript exists; the implementation adds a durable pre-draw claim so that the
   draw→transcript window is also fail-closed, enforcing "a failure before the
   durable commit routes to a signed invalidity, never a quiet second draw." The
   only bounded clarification (m1) is documentary: the **claim**, not the draw, is
   the irreversibility boundary, and its presence mandates a signed invalidity.

---

## Exact mandatory edits (before any draw)

1. **M1** — split the post-draw `except` (`driver:170–174`): if the transcript is
   durable, route to commit-pending recovery ("never redraw; complete the commit"),
   and record invalidity only when the transcript is absent.
2. **M2** — add the four tests named above (reachable-module entropy scan;
   `_preflight` refusals; `git add` path restriction; M1 failure routing).
3. **m1/m2/m3** — document the pre-draw-claim irreversibility + crash-after-draw
   recovery; recheck empty index immediately before `git add`; add the byte-identity
   confirmation of the driver/allocation/public_root/model paths at the final HEAD.

After these land and a bounded re-confirmation passes, an execution record may be
prepared. **This audit authorizes no draw.** The eventual command will be
`.venv/bin/python scripts/level1_draw_public_root.py --expected-head <FINAL_AUTHORIZED_HEAD>`
run once from the repo root after (a) the final HEAD is committed with only
docs/review changes, (b) `git status` is clean with an empty index, (c) the source
paths are byte-identical to the reviewed commit, and (d) Kirill authorizes the
one-shot — but that template is withheld pending the revisions.

## Negative space (preserved, unweakened)

Adjacent-only detector scope; the operational-modulus certificate and its sole S4
tooth; the public-reservation / secret-realization confidentiality boundary and
the public-root / escrow-secret-panel separation; `R_h` deferred until N3;
`PROOF_CORE`/`PROOF_STRONG` and C6-as-annotation; `UNKNOWN`/censored never
success; donor transcripts encode `n_donor`, never `n_target`; development
contrasts non-citable forever; Level 1 never evidence for `PROOF_CORE`.

**No entropy, real panel, feasibility/scout, N3 selection, lock, escrow,
trajectory, or outcome is authorized by this audit.**

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
