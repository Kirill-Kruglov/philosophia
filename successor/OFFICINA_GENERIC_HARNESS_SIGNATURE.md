# Officina batch-settlement and generic-harness signature

Signed by Kirill Kruglov on 2026-07-26.

Signature base: commit
`32214da6c5082dcf48686daf8b2fd896d53a47f7`.

Governing X-line verdict:
`OFFICINA_BATCH_SETTLEMENT_V1_1_1_XLINE_CONFIRMED`.

Governing Y-line verdict:
`OFFICINA_BATCH_SETTLEMENT_V1_1_1_YLINE_CONFIRMED`.

## Signed packet

```text
I_ACCEPT_OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT
I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT
```

The token order is normative: the bounded core amendment is accepted first;
the harness contract is accepted against that amended control surface.

## Accepted meanings

- The first token accepts the explicit, bounded batch-settlement amendment:
  the frozen claim and its closed accounting witness; inline meter evidence;
  global process-sequence order; exact prefix automaton and restart authority;
  the narrowly conditioned, amendment-authorized head/cache completion;
  invalidity override; and the generational pending-resume protocol.
- The amendment adds one `BatchSettlementAuthority` value object and one pure
  `TState.charge_batch_settlement` path in
  `src/philosophia/officina/accounting.py`. The ordinary
  `charge_device_nanoseconds` path is not weakened or repurposed.
- The second token accepts
  `OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md` as corrected, in order, by
  v2.1, v2.2, v2.3, and v2.3.1. Earlier drafts and review captures remain
  provenance; this ordered composite is the governing harness contract.
- The accepted harness covers only the generic metered T-process control
  surface: lifecycle, reservation and settlement, isolation and promotion,
  pause/resume/recovery, closed decision artifacts, the CPU meter adapter,
  refusal-first CLI behavior, and the executable test matrix.
- The author decisions incorporated by v2.3.1 are final: the sole
  head/cache-completion case is amendment-authorized control behavior, and
  meter evidence is embedded inside the claim rather than stored in a separate
  artifact family.

## Resulting gate

Inactive implementation and test construction are now eligible. Cursor may
implement the signed accounting amendment, the generic harness, and disposable
test-only fault-injection coverage. Codex may integrate and audit that work.
The completed implementation requires bounded X/Y review before any further
gate can move.

The future production call-graph manifest remains absent until implementation
review explicitly authorizes its creation. The immutable production roots
remain exactly:

```text
scripts/officina_activate_t.py
scripts/verify_officina_active.py
src/philosophia/officina/generic_harness.py
```

This signature does not authorize changing `runtime.py`, `ledger.py`, or
`checkpoint.py`; modifying signed events, schemas, constants, roots, or import
allowlists; adding another entry point; creating a production call-graph
manifest; or activating T.

It authorizes no capability issuance, real T world, learner, process, entropy,
device breathing check, E1/E2/E3 spend, candidate registration, Q attempt,
Q/C root, scientific datum, outcome, Proof, or claim movement. Officina
remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.

## Governing hashes

```text
4afca93172a39cb8924b48285965a791707cec71330b2a8f81328961f92ec01a  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md
3ce629ed5afe567b5aba936906c114008df989acb1a946443a6ede1e31dca7de  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
6bbaf4d17295a8a4d4fa0f42a9347707e4e2319ea5183163c756b94008764077  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_1_CORRECTION.md
624dfc9b34c8009ee4c1610bfff91f5cfceea128e84d850c3e90ffb1e7be9e2f  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_2_CORRECTION.md
b2288b0a9fb44d23c19d853aeb6d57edd4de888c6058af8001a379f9237d3154  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_CORRECTION.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
fb1408a150c822b4af4ce7196e3c2fc45f8d00ccbf4ff67db40c17aa797951b4  reviews/fable_officina_batch_settlement_v1_1_1_closure.md
04523a8614e8f39b4252e36ce5206991e712f1d32a6dd9be17bc8586a2fcfd5b  reviews/opus_officina_batch_settlement_v1_1_1_final_confirmation.md
fdd3968fb1e3cdc58b28f1c8e0874128dbde742dbae7f40c72fd7badbdbc2ac7  reviews/sol_officina_batch_settlement_v1_1_1_final_confirmation.md
```

Saved chat responses are provenance aids. The formal contracts,
confirmations, ordered tokens, and hashes above govern.
