Written to `reviews/opus_level1_public_root_driver_review.md`.

## Verdict: `REVISE_LEVEL1_PUBLIC_ROOT_DRIVER`

The protocol core is sound and safe — but two Major issues must be fixed before an irreversible draw. **No Critical: no path yields a *quiet* second draw.**

**What's verified solid:** exactly one AST-pinned `secrets.token_bytes(32)` (`driver:157`), after a durable exclusive pre-draw claim, in the order claim→draw→transcript→commit; `atomic_create` uses `O_EXCL`→fsync→`os.replace`→dir-fsync; rerun is blocked by `_preflight` (claim/transcript/invalidity existence); the transcript is complete and canonical (root, pre-draw HEAD, all nine lineage hashes, D/roles with `R_h` deferred, forbidden-panel-derivations); strict separation from the escrow-secret panel seed. My whole-module entropy scan confirms the only entropy primitive is that one call (`model.py:71`'s `manual_seed` is deterministic PRF-seeding, off the driver's path). Tests pass (7); `--help` clean; no real artifacts exist.

**Major findings:**
- **M1 — a benign `git commit` failure discards a valid root (`driver:156–174`).** The transcript is durably written *before* `_commit_transcript`, so if only the commit fails, the `except` mislabels a durable, recoverable root as "permanently spent" and records invalidity — following that literally wastes the precious one-shot. Fix: branch on transcript durability — commit-pending recovery if the transcript exists, invalidity only if it's absent (root truly lost).
- **M2 — safety-critical surfaces under-tested.** The AST entropy check scans only the driver script (not imports); `_preflight` refusals, the `git add` path restriction, and the M1 failure routing are untested. Fix: add a reachable-module entropy scan, preflight-refusal tests against a temp git repo, a staging-path assertion, and a failure-injection test.

**Minor:** the pre-draw claim is durable but uncommitted/deletable (procedural per the declared threat model — document that crash-after-draw requires a *signed invalidity*, never a rerun); recheck the empty index immediately before `git add`; and confirm the driver/allocation/public_root/model bytes are byte-identical at the final HEAD (`--expected-head` binds the tree, sufficient with that check).

**Q9 (claim faithfulness):** the pre-draw claim is a faithful *strengthening* of the signed no-redraw protocol, not a contradiction — it makes the draw→transcript window fail-closed. The only clarification is documentary: the claim, not the draw, is the irreversibility boundary.

Because REVISE, I withheld the execution command template; after M1/M2 land and a bounded re-confirmation passes, an execution record may be prepared (single run from repo root, clean tree/empty index, byte-identity confirmed, Kirill's authorization). **This audit authorizes no draw**; every negative destination is preserved; nothing was committed or run.
