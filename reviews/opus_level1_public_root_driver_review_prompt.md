# Opus 4.8 X-line review: Level 1 one-shot public-root driver

Work in `/home/master/llm_projects/philosophia`. Do not commit and **do not run
the driver**. No entropy call is authorized by this review. Write the full audit
to `reviews/opus_level1_public_root_driver_review.md` and return a concise verdict.

Read the signed Level 1 v3 lineage, especially v3.1 A2/A5, v3.1.1 C2/C3/C7,
the signature records, and the accepted gated-implementation confirmations.
Audit:

- `src/philosophia/level1/public_root.py`
- `scripts/level1_draw_public_root.py`
- `tests/test_level1_public_root.py`
- allocation/serialization/model runtime helpers they call

You may run unit/full tests and static/AST checks. You may run `--help`. Never
invoke the driver with a valid `--expected-head`, never monkeypatch its entropy
call into a full orchestration, and never create any file under
`experiments/level_1_contact/allocation/`.

## Required questions

1. Is there exactly one reachable `secrets.token_bytes(32)` call, outside every
   loop/retry, after all safe preflight work and a durably written exclusive
   claim sentinel?
2. Does the claim make crash-after-draw and crash-before-transcript states
   fail-closed? Audit final/tmp refusal, fsync/replace ordering, invalidity
   routing, and whether any failure can permit a quiet second draw.
3. Are deterministic/fallible inputs computed before the claim where possible?
   After the draw, is the remaining surface bounded and deterministic?
4. Is the canonical transcript complete and unambiguous: public root bytes,
   v3/v3.1 hashes, governing lineage hashes, reviewed pre-draw HEAD, UTC time,
   exact environment + fingerprint, process/witness attestation, public D/roles,
   and explicit forbidden secret-panel derivations?
5. Is automatic git staging/commit restricted to exactly claim+transcript, with
   an empty index/tracked tree precondition and fixed co-author trailers? Analyze
   failures before, during and immediately after `git commit`.
6. Is `--expected-head` sufficient to bind execution to the reviewed driver?
   State exactly what docs-only commits may occur before execution and how the
   final authorized HEAD must be recorded.
7. Is the public root strictly separated from the later escrow-secret panel seed?
   Confirm this driver cannot build/write/encrypt a real panel, run feasibility,
   sample post-N3 blocks, create a lock, or execute a trajectory/outcome.
8. Are tests strong enough to catch a second entropy call, reordered claim/draw,
   nonexclusive overwrite, schema drift, early R_h sampling, or disappearance of
   the invalidity route? Name exact missing tests or code fixes.
9. Does the immutable pre-draw claim sentinel faithfully implement the signed
   no-redraw protocol, or does it introduce a contradiction requiring a bounded
   spec clarification?

Return exactly one verdict:

- `LEVEL1_PUBLIC_ROOT_DRIVER_ACCEPTED`
- `REVISE_LEVEL1_PUBLIC_ROOT_DRIVER`
- `BLOCKED_LEVEL1_PUBLIC_ROOT_PROTOCOL`

Lead with Critical/Major/Minor findings and file:line references. If accepted,
give one exact execution command template using `<FINAL_AUTHORIZED_HEAD>` and
post-run verification checklist. Acceptance authorizes preparing a final
execution record only; it does not itself authorize or perform the draw.
