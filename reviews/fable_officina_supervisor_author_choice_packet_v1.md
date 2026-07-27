READY_FOR_OFFICINA_SUPERVISOR_AUTHOR_SELECTION

# Fable 5 — Officina supervisor author-choice packet v1

Companion:
`successor/OFFICINA_SUPERVISOR_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`.
Evidence commit: `913dc69`. Inputs: supervisor v1 draft + closure, Opus
and Sol `REVISE` confirmations, Codex implementation review, signed
harness composite. Exactly two files created; v1, code, tests,
signatures, runtime artifacts, and existing reviews untouched; nothing
committed; no supervisor/controller/worker started; no entropy,
manifest, activation, or spend. T remains `NOT_ACTIVATED`.

## 1. Verdict

`READY_FOR_OFFICINA_SUPERVISOR_AUTHOR_SELECTION`. Executable options
exist for every load-bearing gap Opus/Sol refused to leave to Cursor.
No existing token is signable yet — including
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`.

`BLOCKED` is not used: A2/A3 close the confinement cell honestly; A1 is
offered but not recommended because full Sol C2 observation is not
closed on the present `/proc` (no `hidepid`) without collapsing into
deployment primitives.

## 2. Mutual exclusivity and sufficiency

| Choice | Mutually exclusive? | Sufficient for the blocked cell? |
|---|---|---|
| A confinement+roles | A1 / A2 / A3 pairwise exclusive; each carries the same endpoint-role obligation | Yes: A2 = literal §5b; A3 = honest re-scope; A1 = byte-secrecy+preflight with stated metadata residual |
| B idempotency+release | B1 / B2 exclusive on release delivery; both cover all eight commands and forbid blind re-exec | Yes: closes Opus F1 / Sol C3 |
| C watchdog | C1 / C2 exclusive topologies; neither makes the watchdog a runtime writer | Yes: closes Opus F6 / Sol C5 |
| D lifetime | D1 / D2 exclusive | Yes: closes Sol M5 / idle-exit cuts |

Choices are not silently combined: confinement does not imply journal
policy; freezer watchdog does not imply idle exit; tokens are
line-replaceable in the response template.

## 3. Recommendations (packet-internal)

Recommended quadruple: **A3 + B1 + C1 + D1**.

- A3 over A1/A2: epistemic repair of an over-claim; A1 fails the
  mandate's "recommend only if fully enforceable" bar for Sol C2 on
  this host; A2 is the correct pick only if Kirill demands mechanical
  secrecy against a deliberate same-UID controller.
- B1 over B2: lost-reply double-effect is the defect; repeatable token
  bytes until durable ack preserve one-use effect without multiplying
  recovery dispositions.
- C1 over C2: only C1 keeps multi-lease concurrency while making
  stop-at-deadline true; C2 forces sibling settlement before archival.
- D1 over D2: smaller state space; no resource pressure justifies idle
  exit.

## 4. Platform audit summary

Recorded in the packet: `ptrace_scope=1`, no `hidepid`, `memfd_create` /
`O_TMPFILE` / `pipe2` available under already-allowed `os`,
`pidfd_getfd` absent, `PC_PIPE_BUF=4096` on a probe pipe, systemd
present with user manager `offline`. Current-platform facts are
distinguished from portable guarantees; only A1 elevates
`ptrace_scope≥1` to a preflight contract condition.

## 5. Mechanical ledger and v2 supersession

All Opus F3–F15 and Sol mechanical items are listed as non-choices in
the packet (bootstrap, spawn registry, singleton lock, zombie reaping,
schemas, FIFO rules, role checks, output grammar, one commit point,
stream table, archival exclusions, subset settlement, observation
contract consistent with selected A, full §S6 carry-forward). Numeric
bounds use signed caps/`device_units` formulas; a hard output **byte**
cap is explicitly **not** invented and would need a separate token if
required. v2 must embed selected tokens, apply the ledger, delete
contradicted v1 claims, and still leave the amendment token unsignable
until a fresh X/Y confirmation.

## 6. Bounded questions for later Opus / Sol (after selection + v2)

**Opus (≤2):**
1. Given the selected Choice A token, does every §5b / endpoint-role
   promise in v2 become a single Linux-observable property (including
   preflight, if any), with no residual path that re-introduces v1's
   same-UID mode-bit fiction?
2. Under the selected Choice C token, is there any reachable schedule
   where a live controller group remains runnable past its lease
   deadline while the sole supervisor is inside archival/hash/Git
   work?

**Sol (≤2):**
1. Under the selected Choice B token, is lost-reply retry of every
   eight commands exactly-once-effect and generation-total without
   inspecting outputs, including `OPERATION_ADMIT` (no second worker /
   cursor) and release delivery/ack (or fail-closed recovery)?
2. Does the mechanical stream-ownership table plus the selected
   confinement option close pre-settlement result signaling
   (path/metadata/timing) to the level that option itself claims —
   and is that claim stated without over-reach?

## 7. Negative authorization / token status

No author token is signable from this packet. Kirill's next act is only
to return the consolidated template with exactly one A/B/C/D token
each. That selection authorizes drafting v2; it does not authorize
implementation, activation, credentials/units beyond what A2 would
later require after signature, or any scientific movement. Programme
claim remains `OPEN`; T remains `NOT_ACTIVATED`.
