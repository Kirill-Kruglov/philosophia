This task is already complete from earlier in this session. Let me verify nothing has drifted rather than rebuild from memory.

All intact and unchanged. Re-verifying the load-bearing claims independently rather than restating them from memory.

All claims re-verified. One precision defect surfaced in my own closure's census block that a reviewer recomputing it would flag.

This task was already delivered earlier in this session. I re-verified everything from disk rather than restating it, and made one precision fix.

## Verdict

```text
READY_FOR_OFFICINA_P1_WB_BINDING_XY_REVIEW
```

## Paths and hashes

| File | SHA-256 |
|---|---|
| [binding draft](successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V1_DRAFT.md) (894 ln) | `73d9cfeb…3942` unchanged |
| [implementation handoff](successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V1_DRAFT.md) (857 ln) | `96cda63a…d440` unchanged |
| [closure](reviews/opus5_officina_p1_wb_post_selection_binding_closure.md) (590 ln) | `8441a108…dfd8` **changed** — see below |

All six governing hashes re-matched on recompute, including the identity signature. HEAD is still `6e1f407`; base `6306e28` untouched.

**The one correction.** The closure's census read `lines carrying BOTH markers  4  (2277, 6363, 6391, 6402)` with no region qualifier. Over the whole file it is **6** — lines 83 and 6501 also carry both. The four are the *body* loci, i.e. the ones that must be edited in place at OR-4; line 83 is preamble (deleted) and 6501 is guard data (retained). A reviewer recomputing over the whole file would have gotten 6 and flagged a discrepancy in a document where counts are load-bearing. The census now states both numbers and why they differ. Nothing else moved.

## Re-verified, not recalled

- **Marker census:** 20 marker lines, 13 `[W-A]` + 13 `[W-B]`, **0 in the amendment** — OR-4 edits one file and has not run.
- **Three-region split**, computed against sentinels at 248 / 6461 / 6463 / 6504: **3 preamble / 16 body / 1 guard data, 0 unaccounted, total 20.**
- **F1:** amendment defines **15** CK rules; §A9 H-3 (line 1149) says `CK-1..CK-12`, while line 1202, §P1-14.8 (line 6283) and packet §6.1 all say fifteen.
- **F2:** `KV` occurs **0** times in the amendment, **2** in the composite (both bare references), **0** in the governing packet.
- **Identity:** `attested_pid` / `attested_pgid` occur **0** times in both governing files.

## W-B binding

One operative branch: W-B / `P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1` — two sealed pipes, slot 6 explicitly closed, no socket, no transport-request capability; on EOF the watchdog writes/freezes/signals/sends nothing and exits; the PCS detects endpoint loss, classifies record-first, and is sole group-stop executor for that route. W-A and `P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1` rejected. The four common amendments are bound by reference to their owning loci, with the owning clause governing on any divergence.

The structural result that matters: **G-10 matches only `REGION(BODY)`**, so a body-only resolution satisfies OR-4's stated success condition while leaving the Cell-2 blocking notice in the file — hence `PO-2`, a stronger whole-file-minus-guarddata check. And **line 6501 must be retained byte-identical**; deleting it destroys G-10's patterns and moves `H_GUARDDATA`.

## Identity gate

Resolved **stricter than the proposed minimum: no identity code at all.** Not blocked-by-identity, because the governing pair defines no such surface and §P1-10.7 computes scope from the PCS's own handle table — W-B is identity-free by construction. Three states kept separate: binding *not blocked*; implementation scope *excluded*; the XS-1 **combined binding** carried in the ledger as `BLOCKED_PENDING_IDENTITY_WEAKENING_REVIEW`, not as this task's closure. The token is nowhere treated as accepted.

## Cursor scope, provenance, negative space

Seven allowed paths; frozen list covers five production roots, the MS-5 baseline, both absent MS-6 modules, all Stage A/B/M4/M7 paths and the four MS-13 modules. Matrix: 16 unit / 18 adversarial / 5 multi-fault / 4 disposable integration; no `test_p1_row_NNN_` may exist. `generic_harness.py` is production root #3 and its untracked bytes violate §P1-3.2 and S-12 (subprocess, Popen, os.kill, os.killpg) — conforming to its own lineage, not to P1; not edited, not adopted, fresh recorded audit mandatory before reuse. The four deferred MS-2 rows enter at the first genuine generational round, not at OR-4.

No key, Stage A/B, resolved bytes, manifest, attestation, install record, OR step, process operation or acceptance. Nothing committed; the twelve pre-existing modified files and four pre-existing untracked files are byte-unchanged.

## Exact next boundary

Bounded X/Y review of the three files — 10 questions, led by F1 (the `CK-1..CK-12` vs fifteen-checks contradiction, whose omitted range contains CK-14/B14) and F2 (`KV-1..KV-6` undefined, fencing the classifier scope predicate). Nothing proceeds to `I_ACCEPT_…_AMENDMENT_V1_7` before that, and that token — when signed — still starts no OR-3, generates no key, executes no OR-4, installs no code and activates no T. Two further separate author acts are required.
