I'll start by locating and reading the governing files for this confirmation review.

This is a substantial confirmation task. Let me read the governing prompt and the core deliverables. First, let me recompute the hashes and read the key files.

Hashes match committed bytes exactly. Now let me read the core deliverables — the v2.1 correction packet and the untrusted closure.

Now let me read the untrusted closure and the two prior confirmation reviews, and verify the CLOCK_MONOTONIC constant independently.

CLOCK_MONOTONIC == 1 confirmed on the exact platform pin. Now let me independently audit the composite bytes — verify the CLOCK_ token count, invariant 89, the path discrepancy, and hunt for a 23rd site.

Composite bytes confirm every quoted site verbatim, and `CLOCK_` count is 0. Now the hardest determination — independently hunting for a 23rd site. Let me run exhaustive greps over the composite.

Let me inspect the lines that fall outside the 22 enumerated sites and the checked-fine list, to confirm no 23rd load-bearing site exists.

§P1-13.8 line 2382 is the peer out-of-scope list (covered by invariant 85, checked-fine); line 2389 is site 20. No 23rd site in the composite. Now let me perform determination 4 — the peer-chain audit that O-6 leaves open — and verify O-8. This is the crux for the verdict.

My independent peer-chain audit has surfaced something decisive. Let me verify the §W3.3 procedure, the §Z4.5 path supersession, and the current governing freeze-observation writer assignment.

The peer-chain audit is now decisive. Let me confirm the two prior v2 confirmation verdicts and check the parallel Y-line final's status for situational awareness (my determination remains independent).

My independent audit is complete and conclusive. The peer-chain surface that O-6 discloses as open is load-bearing and, in one respect, mischaracterized against committed bytes. Per determination 4's explicit rule, this is a `REVISE`. Let me write the deliverable.

Deliverable written. Here is the outcome.

## Verdict: `REVISE_OFFICINA_P1_WATCHDOG_V2_1`

I created exactly one file — [opus_officina_p1_watchdog_freeze_choice_v2_1_final_confirmation.md](reviews/opus_officina_p1_watchdog_freeze_choice_v2_1_final_confirmation.md) — read-only otherwise. Committed hashes recomputed and match the closure; the closure was treated as untrusted and every citation read from contract bytes.

**What confirmed (determinations 1–3, 6):**
- **`_CLOCK_MONOTONIC`** — verified `== 1` (`int`) on the exact Linux/x86_64/CPython 3.12.3 pin; `grep -c CLOCK_` over the composite = **0**, so it was genuinely undisclosed. Source, validation (fail-closed `PRIMITIVE_NOT_GENUINE`), and every `_clock` call signature (`S-25`) are correctly pinned. Underscore spelling is contract-conformant.
- **The 22-site audit** reproduces verbatim at every cited line; I ran an independent exhaustive `freez|witness|observ` sweep and **found no 23rd site** in the composite. The two-site model (`R19`/`R21`) correctly admits the PCS `_killpg` classifier as execution site (b), distinct from the `SIGNAL_GROUP` opcode, retaining `S-12`/sole-caller.
- Count-key rename (`K1`–`K5`), R2 schema separation, R9/R10, classifier primitives, totality, W-A/W-B replay, `O-7` accounting, and all previously-closed findings — all clean.

**Why `REVISE` (determination 4 — the decisive one):** I performed the peer-chain audit `O-6` leaves open. The required *common* amendment `P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1` (falls on both W-A and W-B) makes the watchdog write/freeze nothing, but the **governing peer chain still says the watchdog writes the freeze observation**, in load-bearing text v2.1 neither audits nor repairs:
- **§W3.3** is literally titled *"…watchdog-written"* and every step is the watchdog's (step 6 "write …json itself"). `O-6`'s claim that §W3.3 "remains the supervisor's dead-watchdog procedure; no option amends it" is **false against the bytes**.
- **§W3.5** supervisor-death row: "watchdog freezes all known groups per §W3.3, writes their observations, exits."
- Current governing file-tables (`…V2_1_2:1353` hash `2cd8b7b5`, `…V2_3_1:1353`) still give the writer as "watchdog (or supervisor when the watchdog is dead)."
- **§Z4.6 conjunct 9** binds "the watchdog-written witness."

These are the direct object of the reassignment, in the byte-intact accepted contract set — the exact "two governing documents disagree" hazard the correction named at `O-5` and closed for the binding but not for the harness/settlement chain. The mandate states a still-open unaudited load-bearing surface is a `REVISE`, not a disclosure.

**Determination 5 (`O-8`):** classified **non-governing** — §W3.3's `<process_id>.json` was already superseded by §Z4.5 (`…V2_1_1:174`) to `<witness_id>.json`, matching the composite. It does not independently block, but `O-8` missed that supersession, corroborating the unaudited-peer pattern.

The fix is bounded (enumerate/replace the peer-chain freeze-writer surface, same kind already applied to the composite, plus an accurate re-statement of §W3.3) — no new mechanism or cell. `T = NOT_ACTIVATED`, claim `OPEN`, both cells unselected; no selection authorized.
