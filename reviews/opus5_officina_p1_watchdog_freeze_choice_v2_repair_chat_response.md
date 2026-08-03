Now writing the v2 packet.

Now the closure.

Done. Two files created; nothing existing was modified.

## Created

- [OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md](successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md) — 1637 lines, `72212a986d9551ef47718e871a81951b55a849a10d34eb12e6276499cb675505`
- [opus5_officina_p1_watchdog_freeze_choice_v2_closure.md](reviews/opus5_officina_p1_watchdog_freeze_choice_v2_closure.md) — 469 lines, `7b3708550806fcd5742accb5858a2da05a87c4b22ee7fbdffe73ecdbad07759e`

`git diff HEAD` is empty for v1, the v1 closure and both reviews.

## Verdict

`READY_FOR_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2_XY_CONFIRMATION` — all ten findings closed one-to-one.

## Recommendation after repair

**W-B**, on signed-authority fidelity, constructibility, mechanical testability, liveness and blast radius. Nothing selected.

The repairs made the comparison *worse for W-B's headline* and I said so rather than restating v1's claim: **W-B amends twelve normative P1 sentences, not zero.** Both options now reopen a peer contract (§N5), and both now carry the whole §3 classifier that v1 hid behind an eight-line scope block that did not work. What survives is the rows that didn't move — W-B still makes zero topology/opcode changes, and still adds no liveness dependency. §3, §6 and §7 fall identically on both options and therefore cannot separate them.

## Four things you should look at

**The §4.3 gate is the most consequential author choice.** Y-C2 offered gate-or-pricing; I took the gate (invocation forbidden before the PCS's own endpoint loss) because it's strictly safer — it closes the "compromised watchdog forces invalidity on a healthy generation" channel entirely. But the gate keys on *exactly W-B's trigger*, so under repaired W-A the PCS already knows the freeze is due and the watchdog only adds a decision plus a 60-second delay. That's a real argument against W-A, it's stated in §9.4 rather than buried, and it is not outcome-neutral.

**Three defects neither review found.** §7.2's audit turned up three further freezer/witness sites beyond X's seven — §P1-13.2 row 4's "EITHER the watchdog role process, normally", §P1-13.7's freeze row, and invariant 63. §3.2 found that v1.2 **never populates `pgid_or_null`** and never defines a kernel-verified group for a role handle; §3.4 fills it. §5.2 found that `_MSG_EOR` isn't in the PCS's pinned constants, so X's `MSG_EOR` repair needs a binding-block extension.

**Two places I deviated deliberately.** §W3.3's quiescence interval is `100_000_000`, but the composite says that value "appears in no rule of this contract" — so §3.6 uses 16 passes of `T_SUPERVISOR_POLL_INTERVAL_NS` for the same 800 ms budget rather than contradict a signed sentence. And `A-ABS-2` (nulling `current_unresolved_member_count`) goes beyond Y's literal text; it's flagged as author-added with its derivation.

**A residual neither option removes.** A target that calls `setsid()` after SIGCONT escapes the freeze entirely — `KV-5` fails, no signal is sent, the tree keeps running. Fail-closed and correct, but the activation protocol's "process group is immutable while open" is a lease declaration, not kernel enforcement. §3.10, covered by `L7`/`L9`.

## Residual author choices

1. W-A **xor** W-B (W-B's token renamed to `…_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS` — `PEER_EOF` carried the death claim Y-M1 required withdrawn).
2. The per-option token: `P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1` or `P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1`.
3. **Four common amendments required under either selection** — the `ABSENT` fallback nullable-identity amendment, the PCS freeze classifier, the twelve-site role reassignment, and the `L6`–`L9` publication wording. These aren't a separate choice; they're the price of any selection, and a selection without them leaves an unimplementable path.

The identity cell is untouched: §6 makes its settlement constructible under *either* of its outcomes without selecting or repairing it. `T = NOT_ACTIVATED`; programme claim `OPEN`.
