# Closure — Officina executable-contract migration charter v1.1

**Author:** Claude Code Opus 5. This is the author's own closure on the sole bounded revision
permitted in this migration episode. It is an untrusted self-assessment, normative for nothing.

## Verdict

```text
READY_FOR_OFFICINA_MIGRATION_CHARTER_V1_1_FINAL_XY_CONFIRMATION
```

Every X mandatory edit E1–E9 and every Y mandatory edit 1–6 lands in
`successor/OFFICINA_EXECUTABLE_CONTRACT_MIGRATION_CHARTER_V1_1_DRAFT.md`, one-to-one, inside the
650-line / 48-KiB limit and without reopening any signed science. The budgets are mechanically
satisfiable and the arithmetic is below. One residual author choice remains genuine (T-3); the
KG-2 4-vs-6 question is resolved structurally and is **no longer** an author choice.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
```

## Input gate

All four pinned hashes recomputed before substantive work; all four reproduce exactly. The task
pins commit `5e6094a`; the live checkout is `0078627`, of which `5e6094a` is an ancestor. Each of
the four pinned objects is byte-identical at `5e6094a` and in the working tree, verified by
`git show 5e6094a:<path> | sha256sum`. The single intervening commit adds only this revision's
own prompt file and touches no pinned object. **Not `BLOCKED`.** This file contains none of its
own digests and none of the pinned digests.

## Deliverables and hard limits

| File | Lines | Cap | Bytes | Cap |
|---|---|---|---|---|
| `successor/OFFICINA_EXECUTABLE_CONTRACT_MIGRATION_CHARTER_V1_1_DRAFT.md` | 650 | 650 | 44,657 | 49,152 |
| `reviews/opus5_officina_migration_charter_v1_1_closure.md` | this file | 350 | this file | 24,576 |

Exactly two files created. No copied old contract block, member list, digest table or review
chronology appears in either.

---

## §1. X mandatory edits E1–E9 — one-to-one

| X edit | Where it lands in v1.1 | Disposition |
|---|---|---|
| **E1** — Class-B claim conditional on G-TPL/G-SRC/G-CARD | §2.6 restates the theorem narrowly and conditionally on the **unchanged, independently reviewed** provenance gate; §2.2 supplies the three guards; §2.6's second paragraph enumerates what it does not claim | **Superseded by a stricter form.** The v1 "eliminated by construction" table is deleted outright rather than annotated, per Y2's requirement that the theorem be restated, not repaired |
| **E2** — delete the false independence sentence; add O1 and O2 | §4.1 ¶2 deletes it and re-labels the projection pair a generator and ordering test; §4.2 defines O1 (standing, weak, test-only) and O2 (disposable, M4-only, from `generated/CONTRACT.md` alone) | **Landed verbatim in substance** |
| **E3** — G-TPL, G-SRC, G-CARD; templates emit layout, never sentences; `NORMATIVE_TEXT` | §2.2 (all three gates); §2.3 (`NORMATIVE_TEXT` mapping, generated non-editable header) | **Landed, strengthened.** G-TPL is stated as an allowlisted grammar and G-SRC additionally forbids a `DERIVED` field from carrying a `PROTOCOL` citation |
| **E4** — add I-16, I-17, I-18; state control-plane scope | §3.3 families **A-16** (parser layout, grammar, `V0..V39`), **A-17** (persistence and durability), **A-18** (deadline, interruption, retry); the control-plane sentence precedes the family table | **Landed inside the wider Y4-M1 repair** — the three become families of the closed register rather than three more thematic items |
| **E5** — sum-type collapse; delete the forcing clause; emit both counts; no author choice | §4.3 in full | **Landed verbatim in substance** |
| **E6** — G-DIM-1..4; replace §4.7's fourth bullet | §4.4 (all four gates, G-DIM-4 carrying both product faithfulness and register completeness); §4.4's closing paragraph is the bounded statement replacing the open concession | **Landed** |
| **E7** — `canonical.py` as dependency under observation; crash-cut not an M3 terminal failure; strict xfail + blocker id; M5 states the derived blocker count | §5.3; §9's disposition row for `CANON`; §6's M3 gate condition | **Landed, with one strict change:** the blocker count is **reported by the release check**, not stated in the acceptance material, because §1.3 forbids any count in author-authored acceptance material |
| **E8** — delete the 120-KiB aggregate; keep 2,500 LOC and 64 KiB data; add the 400-line generator cap; restate the file cap | §7's ledger table and counting rule | **Landed inside the stricter Y4-M1 budget** — the LOC cap now covers every regular file under `contract/**`, not only `*.py`, and the trusted base gains its own joint cap |
| **E9** — scope the duplicated-literal kill switch; exempt and require test/oracle duplication | §7's last ledger row | **Landed verbatim in substance.** Without it, §7's kill switch would forbid O1, which is the charter's only standing oracle |

**X's logged, non-mandatory items.** (i) and (ii) concern the v1 §2.4 lemma mapping and the v1
§1.2 grading of `X15-M1`/`X15-M2`; both surfaces are removed from v1.1 rather than corrected, so
neither survives to be wrong. (iii) the interaction between the round limit and M4 — itself a
review package — is resolved mechanically by §8.1's round definition, under which simultaneous
X/Y evaluation of identical bytes is one round regardless of label.

## §2. Y mandatory edits 1–6 — one-to-one

| Y edit | Where it lands in v1.1 | Disposition |
|---|---|---|
| **1** — token-only signed Git tag; mechanically checked candidate/review/closure DAG; no signature-carried manifest digest | §1.2(4) deletes the v1 exception; §1.3 defines `C` → `RX`/`RY` → `L` → signed annotated tag and the mandatory `--check --release-ref` mode | **Landed.** No second manifest, no generated release envelope, no copied object id |
| **2** — independent provenance gate; mutation fixtures; narrow theorem; protected trust root; ledger moved out of `contract/**` | §2.1 (eight requirements, renderer-import forbidden); §2.5 (MF-1..MF-10); §2.6 (narrow theorem and its disclaimers); §2.4 (trust root); §2.7 (ledger at `successor/officina/migration/`) | **Landed in full** |
| **3** — logical in-place archive; v2.15 aggregate status not accepted | §9: primary `STATUS_POLICY.json` plus a generated path index, no path moved, the five status lines preserved exactly, signed files kept as live Class-C, live resolution rejecting `HISTORICAL_NONOPERATIVE`; §10.1 redefines what T-1's "archive" means | **Landed in full** |
| **4** — closed semantic-atom inventory with exact Git-bound locators; no delegated readings | §3.1 (register, dual closure, `G-ATOM`); §3.2 (blocked decision slots); §3.3 (path aliases and 20 families with sources and closure rules) | **Landed.** Closure is achieved by fixing the source set and deriving atoms mechanically per family, not by transcribing clauses — the only form that fits the line limit without copying prose |
| **5** — implementation outside the budget; mechanical counting; 1,000-line/64-KiB trusted-base cap; three-way M6 rule | §7 (ledgers, counting rule, `src/**` exclusion); §5.4 (the three-way rule and the prohibition on Case 3 amending, resetting or authorizing) | **Landed in full** |
| **6** — episode/round/scope identity; non-resettable two-round and 21-day limits | §8.1, §8.2, §8.3 | **Landed in full**, including §8.2's statement that the charter-design and implementation counters cannot be relabelled into each other |

**Y's minor prose items.** §5 M4's "cannot diverge" prediction is replaced by an explicit gate
condition in §6's closing paragraph ("X and Y cannot diverge on provenance *while `G-PROV` is
unchanged and green*"). The ledger's contradictory status is resolved by the path move in §2.7.
`PROGRAMME CLAIM = OPEN` now appears only in fenced state blocks.

## §3. Where X and Y differ — the stricter rule taken

1. **Release binding.** X (X1.5) proposed that the M5 signature name the route-vector digest that
   O2 agreed with. Y1 forbids any digest in author-authored acceptance material. **Y is stricter
   and wins.** §4.2's `G-STALE` keeps X's staleness detector but relocates the recorded digest to
   the M4 **reviewer's** evidence file under `reviews/` — outside `contract/**`, outside
   `generated/**`, and outside the acceptance material — where it functions as a pinned
   expectation whose mismatch is the signal. The acceptance tag carries the token and nothing
   else. **This is the one location in the whole architecture where a digest string appears
   outside `MANIFEST.json`, and it is named here so the confirming lines can rule on it directly.**
2. **Blocker count at M5.** X's E7 asked the M5 signature to state the derived open-blocker count.
   Same conflict, same resolution: §5.3 and §1.3 make the release **check** report it.
3. **Budget scope.** X's E8 capped `contract/**/*.py`; Y's edit 5 requires physical-line counting
   over **every regular file** with symlinks refused. **Y is stricter and wins** (§7).
4. **Trusted-base cap.** X proposed 400 LOC on `tools/officina_contract/**`; Y proposed 1,000
   lines and 64 KiB over the whole non-test trusted base. **Both are kept**, with X's 400 as a
   sub-cap on the generator/template layer inside Y's 1,000 (§7).
5. **Extraction boundary.** X's E4 adds three invariants; Y's edit 4 demands a closed atom
   inventory. **Y's form is stricter**; X's three become families A-16..A-18 within it, so neither
   requirement is diluted.
6. **Archive.** X took no position (referred to Y). Y3's logical archive is adopted whole.

No case required choosing X over Y on a point where Y was stricter, and no divergence between the
lines needed an author choice to resolve.

## §4. Budgets are mechanically satisfiable

**Measured density, this repository.** Tracked `src/philosophia/officina/**` at `HEAD`: 4,854
physical lines in 193,989 bytes = **39.97 B/line**. Including the uncommitted salvage work:
7,349 lines in 305,045 bytes = **41.51 B/line**. Per-file range: 28.3 B/line (`canonical.py`) to
44.7 B/line (`activation.py`).

**The v1 defect, arithmetically.** v1 §6.1 capped `contract/**` at 2,500 LOC **and** 120 KiB
jointly, with `data/**` at 64 KiB **inside** that byte cap:

```text
2,500 lines x 41.5 B/line             ~ 103,750 B   leaves ~19,130 B for data/** = 29% of 64 KiB
data/** at its full 64 KiB            leaves (122,880 - 65,536) / 41.5 ~ 1,382 lines = 55% of cap
```

At most two of the three caps could ever bind. Under v1 §6.3 that is a redesign event, not a
repairable finding. **Deleted in §7.**

**Why v1.1's caps are jointly satisfiable.**

| Ledger | Cap | Implied constraint | Satisfiable |
|---|---|---|---|
| `contract/**` | 2,500 physical lines | line axis only | Yes — no byte cap on source, so the axes are disjoint and cannot conflict |
| `contract/data/**` | 64 KiB | byte axis only | Yes — disjoint from the line cap above |
| Non-test trusted base | 1,000 lines **and** 64 KiB | ≥ 65.5 B/line permitted | Yes — 47% above the densest file observed anywhere in this repository (44.7 B/line) |
| Generator/template layer | 400 lines | sub-cap inside the 1,000 | Yes — see the allocation below |

**Sizing the trusted base.** Renderer plus templates 250–400; provenance gate (walk, independent
hash, manifest equality, schema check, template-grammar check, parse-back and recomputation,
literal rejection) 250–350; contract schema 80–150; verifier including `--release-ref` 150–220.
Midpoint total ≈ 900 of 1,000 lines. **This is the tightest budget in the charter** and the
pessimistic end (~1,120) exceeds it. Two mechanical reliefs are already available inside §7
without any override: the MF-1..MF-10 mutation fixtures are **tests** and sit outside the base;
and the template **grammar declaration** may live as a declarative table under
`contract/data/**` (byte-capped) while only its **checker** counts as base code. If neither
suffices at M3, §8.3 makes the overrun a redesign event rather than a silent expansion — which is
the correct behaviour, not a defect.

**Sizing `contract/**`.** Constants 400–600; schemas 400–600; machines, being the KG-2 evaluator
plus the classifier phases, 600–900; parser grammar 200–300. Total ≈ 1,600–2,400 against 2,500,
i.e. 4–36% headroom — and only because the transition table, dimension declaration, classifier
fixtures, atom register and the `V0..V39` vectors are JSON under `data/**`, not Python.

**The second tight budget: `contract/data/**` at 64 KiB.** The atom register dominates it. At a
plausible 250–450 atoms across the twenty families and ~100 B per compact canonical-JSON record
(id, family, locator, closure-rule reference, test id), the register is 25–45 KB, leaving 19–39 KB
for dimensions, the transition table, fixtures and forty parser vectors. Reachable, not
comfortable. Named here as the budget most likely to bind first at M1, and mechanically detected
before review by §7's counting rule rather than discovered in it.

## §5. Residual author choices

| # | Choice | Status |
|---|---|---|
| 1 | **T-3 dependency policy** — stdlib only, or stdlib plus Hypothesis as a test-only dev extra | **Genuine and open.** Recommended: stdlib only (§1.4) |
| 2 | **T-1 halt / T-2 route acceptance** | Route decisions, recommended in §10.1 and §10.2. Not engineering questions |
| 3 | **T-4 timing** | Constrained, not chosen: signable only after the final byte-identical X/Y confirmation of these bytes **and** Kirill's T-1 and T-3 choices |
| 4 | **The pinned author identity** for the §1.3 release tag signature | An **input** the author supplies at M0/M5, not a choice this charter may make. Flagged so it is not discovered at M5 |
| 5 | Any **blocked decision slot** M1 records under §3.2 | Deferred **to the author by construction.** M1 and M2 are forbidden to resolve one |
| 6 | The §8.3 destination on a stop trigger | Arises only on trigger; three fixed destinations, no fourth |

**Removed as an author choice.** The KG-2 4-vs-6 write-count question. §4.3 resolves it
structurally: the mis-factored dimension pair becomes one `ObservationOutcome` sum type,
impossible tuples become unrepresentable, the forcing clause is deleted rather than interpreted,
and both the full sum-type population and the feasible counts are published as `len(...)` values.
No reading is adopted and no figure is fixed by the charter. This is the strongest single piece
of evidence for the route: a question that survived fifteen prose generations dissolves under a
correct factorization.

## §6. Negative space

This closure and the charter together created exactly **two** files:
`successor/OFFICINA_EXECUTABLE_CONTRACT_MIGRATION_CHARTER_V1_1_DRAFT.md` and this file. Nothing
else was created, modified, moved, staged, committed or deleted — verified against
`git status --porcelain`, which reports the two new paths and, unchanged, the pre-existing
modified and untracked work.

No W-B amendment, composite, binding or handoff was created or repaired. No existing file, code,
test, signature, runtime artifact, governing or historical document or prior review was edited.
The uncommitted `generic_harness.py`, the accounting edits and the two modified test files remain
exactly as found. No commit, tag, branch or other Git object was created. No archive or path-moving
operation was performed. No implementation, M0 act, token, install or activation occurred.

No contract module, schema, fixture, generator, verifier, provenance gate, manifest, test or
oracle was created. No machine was executed and no cross-product was enumerated: §4 of the charter
and §5 here describe what M2 will compute and fix no route, write or population figure. No `/proc`
was read; no socket, pipe, FIFO or descriptor was opened; no `fork`, `exec`, `signal`, `wait` or
`prctl` was called; no clock was sampled for any contract purpose; no key, entropy, seed or world
was generated; no `E1`/`E2`/`E3` was spent. No Philosophia production module was imported or
executed — `src/philosophia/officina/**` was measured with `wc` and `grep` only, for §4's density
arithmetic.

This closure predicts no X or Y verdict and no scientific outcome. It reopens no signed science,
designs no v2.16, and asserts no acceptance: amendment `v1.12` remains not accepted,
`P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` remains not accepted, and the X line's v2.15
confirmation is neither completed nor withdrawn by anything here.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 WATCHDOG-FREEZE CELL = SELECTED: OPTION W-B, SENSOR-ONLY
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, OBSERVATION-ONLY
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
WATCHDOG AUTHORITY AMENDMENT V1.12 = NOT ACCEPTED
INACTIVE-SCAFFOLD AUTHORIZATION = NOT GRANTED
RUNTIME IMPLEMENTATION AUTHORIZATION = NOT GRANTED
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
```

## §7. What the confirming lines should attack first

Ranked by where I judge v1.1 weakest, stated plainly rather than defended:

1. **`G-STALE`'s digest in the M4 review file** (§3.1 above). It is the single digest outside
   `MANIFEST.json`. I argue it is a pinned expectation in reviewer evidence, not an authority
   assertion in acceptance material, and that deleting it would delete X's only staleness
   detector. A line that disagrees should say so as a structural finding.
2. **Atom closure by derivation rather than enumeration** (§3.1, §3.3 of the charter). The
   register is closed because the source set is fixed and each family carries a mechanical
   closure rule. Whether that is genuinely closed, or merely relocates the judgement into the
   closure rules, is the sharpest open question in the revision.
3. **The trusted-base line budget** (§4 above). Midpoint fits; pessimistic end does not.
4. **`G-DIM-2`'s recording proxy** presumes enumeration reaches every dimension through attribute
   access. An evaluator that destructures its input once could defeat the read-coverage check.
5. **The three-way M6 rule's Case 2** ("consequence of an existing atom") is the classification an
   implementer under deadline pressure will over-use.

## §8. Exact next boundary

Byte-identical independent X-line and Y-line confirmation of
`successor/OFFICINA_EXECUTABLE_CONTRACT_MIGRATION_CHARTER_V1_1_DRAFT.md` — the same bytes to both
lines. That is **round 2** for the charter-design scope, and this episode's last. There is no
`REVISE` destination and no v1.2: a structural failure at round 2 fires §8.3's redesign rule and
one of its three terminal destinations is selected.

If confirmation closes, then and only then: Kirill's consideration of T-1, T-2 and T-3, with T-4
separately and afterwards. No M0–M6 work, implementation, archive operation, Git object, token or
activation is in scope before that.

No token is authorized by this closure.
