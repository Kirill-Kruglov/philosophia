I'll start by verifying the exact committed state and file hashes before reading anything.

All four hashes match exactly. Let me confirm the working tree matches the committed bytes so I can read them safely, then read the files.

Working tree equals committed bytes. Now let me read the primary correction packet (the bounded v2.6 repair) and the signature file.

Now the core normative file. Let me map its structure before reading the critical sections.

This is the heart of the specification. Let me read the metadata schema and integrity sections (MS through XS).

Now let me verify concrete claims: MS-2 (43) and MS-3 (7) row counts and that every listed digest matches the real file on disk.

All 50 M2+M3 digests are real and match. Now verify full path disjointness (57 distinct paths, M2∩M3=∅, M1 not in M2/M3) and the joint-block byte identity between the two governing files.

Joint block is byte-identical (same SHA-256, 1071 lines) across both governing files, and all 57 paths are distinct. Now let me examine the composite v1.6 structure for the test rows, region digests, variant balance, and status.

Let me examine the composite test rows (92-115), the region-digest definitions, variant-marker balance, and status lines.

Body region variant markers 13/13 whole-file balanced, and test rows 104-115 are richly enumerated. Now the crux — item 7. Let me read composite §P1-3.1 through §P1-3.4 to determine whether `reachable_closure`'s *value* is contract-derivable.

Now let me verify the remaining counts (§P1-18 provenance rows, rule-family cardinalities) and sweep for any `created_utc` ordering use.

Rule-family counts all match the packet's tally. Let me pin down the composite provenance region (§P1-18) row count precisely.

All item-8 counts confirmed (225/171/54/141/57/25/51/24) and provenance = 51 with all 50 M2+M3 digests present. Now let me confirm TS-4 (Stage-B format) is byte-unchanged from the v2.5-era v1.2 amendment, and sweep for any hidden authorization/activation.

The v1.2 digest matches its MS-2 record. Let me directly diff the TS-4 text between v1.2 and v1.3 to check "verbatim", and rerun the authorization sweep cleanly.

TS-4 differs only by a cosmetic reflow (both specify 128 lowercase hex `0123456789abcdef`, pure Ed25519, detached, no prehash) — the *format* is unchanged, though "verbatim/byte-unchanged" is slightly loose wording. Let me run the authorization/activation sweep cleanly.

All authorization/activation/selection leaks clean. Let me do final preservation checks (no live §P1-19, blocking notice, option symmetry) before writing the review.

All ten items verified. Every claim recomputed from the bytes. Let me write the independent X-line review to the prescribed path.

Review written to [reviews/fable_officina_p1_watchdog_v2_6_independent_x_confirmation.md](reviews/fable_officina_p1_watchdog_v2_6_independent_x_confirmation.md). No existing file edited, nothing committed.

## Verdict

**`OFFICINA_P1_WATCHDOG_V2_6_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION`**

Reviewer: Claude Code, `claude-opus-4-8`, fresh session (Fable 5 unavailable; packet's Opus-4.8 fallback used). I did not author v2.3–v2.6. The Opus 5 closure was treated as untrusted and every claim recomputed.

## Hashes checked (recomputed from HEAD `92c7012`, all MATCH)

```text
1dbb99b7…369a9  …PACKET_V2_6_CORRECTION.md
c3da2a7d…b3d1   …AMENDMENT_V1_3_DRAFT.md
6283d081…3d49c  …COMPOSITE_V1_6.md
7a8ab2da…3e1f   …IDENTITY_SELECTION_V1_SIGNATURE.md
b839a668…ba8f   JOINT BLOCK — byte-identical in both governing files (1071 lines each)
```

## Findings by severity
- **BLOCKING / MAJOR:** none.
- **LOW:** (1) §7's "TS-4 carried forward verbatim / byte-unchanged" is loose — TS-4 was cosmetically reflowed; format substance and validity predicate unchanged. (2) `reachable_closure` content-derivation is genuinely under-specified vs §P1-3.3 — must be closed before manifest authoring, but non-blocking (see item 7).
- **INFO:** amendment `CK-7`/`CK-8` prose don't individually name codes; codes are in FC-1's closed 25-set and are test-pinned by composite rows 105/106(e)/112.

What recomputed clean: member cardinalities **2/43/7/1/1/2/1 = 57** (57 distinct paths, 21 pairs disjoint, all 50 M2+M3 digests real on disk), provenance **51 = 43+7+1**, counts **225 = 171+54**, **141** tag-family sum, **25** codes, **51** provenance rows, **24** test rows; MS-10 single grammar + provenance-only (zero ordering uses); TS-2/TS-5 exhaustive over all 11+13 keys; Ed25519 Stage-B format unchanged and non-circular; T=NOT_ACTIVATED, watchdog NOT SELECTED, bounded-weakening token NOT ACCEPTED, no option pre-filled, no hidden key/artifact/activation.

## Item 7 answer
Primarily **(a): a legitimate implementation-and-test obligation under a now single-valued shape contract — not a selection blocker** — with an explicit caveat. The *shape* of `reachable_closure` is canonical and single-valued; the *content* is genuinely under-specified (§P1-3.3's "Kind" vocabulary has no stated mapping to MS-4's four literals, and its transitive closures name modules — `abc`, `stat`, `posixpath`, `genericpath`, `_collections_abc` — that aren't rows, so MS-4's closure rule can't be satisfied from that table). I do **not** accept "shape is fixed" as proof content is derivable. It does not block author selection because the field lives in `M4` (written at OR-6, downstream of the option token), is option-independent, is never an input to the watchdog choice, and `G-11` verifies only the shape — no check recomputes the real import graph. The documents make no over-claim (MS-4 conditions on "the same audited closure"; §P1-3.3 is labelled "NOT a canonical value"). The content-mapping is a correctly-declared obligation that must be discharged before any manifest is authored.

## Next authorization boundary
Confirmation means **only** that Kirill may emit exactly one of the two existing watchdog-freeze option tokens. It authorizes **no** keys/entropy, Stage A/B, signature, manifest/attestation/install record, implementation, tests, install, T activation, or scientific execution. `T = NOT_ACTIVATED`; programme claim `OPEN`; identity cell SELECTED Option A (recorded, bound into nothing); identity bounded-weakening token NOT ACCEPTED; watchdog cell moves from NOT SELECTED to author-selectable.
