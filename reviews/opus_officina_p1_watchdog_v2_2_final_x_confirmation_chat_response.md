All 17 custody digests reproduce. Now the independent locus sweep.

The composite's §P1-18 provenance region is decisive here. Let me verify the 40 declared loci line-by-line and hunt for undeclared hits in the same files.

Found a strong candidate. Verifying whether §W6.5 is superseded anywhere in the chain.

§W6.5 is carried by name as a live rule in at least eight later documents. Let me confirm its status and spot-check the declared loci.

Now verifying the remaining audit items — declared loci, read cluster, R16 endpoints, killer enum.

Audit complete. I found a live governing locus omitted from the declared 40. Writing the X-line confirmation.

**Verdict: `REVISE_OFFICINA_P1_WATCHDOG_V2_2`** — written to [opus_officina_p1_watchdog_v2_2_final_x_confirmation.md](reviews/opus_officina_p1_watchdog_v2_2_final_x_confirmation.md). No existing file was modified; nothing committed.

**Hash recomputed and matches** (`651dba04…c77f4`), as do all 25 custody digests in §1.8.

## The 41st tier-1 locus exists

**§W6.5 of `…SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md:1331-1342`** — in a file v2.2 declares tier 1 and edits at 14 loci, none of them this one. It reads:

> "That sentence is **explicitly superseded** by §W3.1/§W3.3/§W3.4: … the watchdog owns the deadline and executes the sequence … records the conservative proved-freeze instant"

That is a freeze **executor** and freeze **evidence-recording** assignment in one sentence. It passes v2.2's own `AUTH-2` test more strongly than any of the declared 40: it's carried by name as a live rule in ten places, and is the *single named protocol amendment* the whole correction chain declares itself to make over the signed harness composite (v2.1.3:1382, v2.1.4:1114, v2.1.5:663, v2.1.6:776, v2.1.7:836, v2.1.8:1414, v2.1.9:1194, v2.1.10:1457). Nothing replaces it. After `PH1` lands, §W6.5 — which *governs* §5a's supersession — says the opposite of §5a.

**Why it was missed:** `O-9`'s method greps `watchdog` within 80 chars of `freez|writ|observ|witness|settle`. §W6.5 uses **`executes`** and **`records`**, and subject and verb straddle a line break. The alphabet has a blind spot for `execut|kill|quiesc`. Compounding it, §1.6's checked-and-clean list enumerates §Z, §N and §U sections but **no §W section at all** — §W6 was neither tier 1, tier 2, nor checked.

Smallest exact replacement given as `PW15`/`PW16`/`PW17` (three loci, one file, inside the existing token, no new mechanism or cell; recommendation unmoved).

## Two further blocking findings

- **`AUTH-3` classifies the P1 binding as tier-1 operative**, but composite `:42-49` makes "corrections v2.1 through v2.1.10.7" provenance and the binding appears only in §P1-18 at `:2851`. `AUTH-1`'s peer-boundary carve-out can't save it — the binding is entirely P1-boundary text. So `PB1`..`PB10` edit immutable evidence, which `AUTH-4` calls a defect. Also: `V2_1_10_5/6/7` postdate the binding and appear nowhere in any watchdog packet (I swept them — no hidden executor, but the inventory didn't reach the chain's end).
- **`PH1`/`PW2` open an ordinary-deadline supervisor write route** that `R2`/`R9`/`R10` ("dead-watchdog route **only**") and `PA-1` don't admit.

## Confirmed clean

`killer == WATCHDOG` unreachable (writer side, predicate side, no defaulting/recovery clause; enum correctly retained as a rejection surface); the four retained reads `RD-1`..`RD-4` reproduce verbatim and grant identity observation only; `R16`'s W-A/W-B variants verify against composite §P1-6.2 and v2 §4.1/§4.7 with no aliasing, duplication, inheritance or alternate write path; the filename supersession is on the bytes at `…V2_1_1:174`; no regression; no authorization of anything.

The Y line independently returned REVISE on the same digest. We converge on the authority partition, handoff atomicity, and the ordinary-deadline route. **§W6.5 is X-line only** — and it survives either authority reading, so it can't be dispositioned away by re-partitioning.
