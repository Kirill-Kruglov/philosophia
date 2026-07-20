# Officina author selections and WP-1/WP-2 authorization

Signed by Kirill Kruglov on 2026-07-20.

Signature base: commit
`2418367de7341e5f27baeec0c2804a9925b02ac2`.

Governing X-line verdict:
`SUCCESSOR_AUTHOR_SELECTIONS_V1_XLINE_CONFIRMED`.

Governing Y-line verdict:
`SUCCESSOR_AUTHOR_SELECTIONS_V1_YLINE_CONFIRMED`.

## Signed packet

```text
I_NAME_SUCCESSOR_LINE_OFFICINA
I_SELECT_SUCCESSOR_LAYOUT_SAME_REPO
I_SELECT_C_INTERPRETATION_FINITE_FRAME_SAMPLE
I_SELECT_Q_ENTROPY_SEALED_POSTFREEZE_ROOT
I_SELECT_T_ENVELOPE_ONE_WEEK
E1=168_DEVICE_HOURS
E2=12_CANONICAL_CANDIDATES
E3=48_WALL_HOURS_OR_40_DEVICE_HOURS
I_SELECT_DEVICE_POLICY_OFFCPU_WITH_BREATHING_CHECK
I_AUTHORIZE_SUCCESSOR_WP1_WP2_IMPLEMENTATION
```

## Selected meanings

- The successor line identifier is `officina`; its publication title remains
  open. It stays in this repository under `successor/officina/`.
- Scientific quarantine is enforced by signed semantics and a fail-closed,
  realpath-resolved path allowlist. Repository layout is not scientific
  independence.
- C uses a probability sample from a fixed finite frame with locked inclusion
  probabilities, weights, and finite-population correction. Its values remain
  WP-3/WP-9 cells.
- Q uses one sealed post-freeze OS-CSPRNG root. The first entropy byte is the
  launch boundary; any ambiguous post-invocation state is conservatively
  charged. Concrete Q custody, attestation, caps, spending, and competence
  numerics remain WP-6 cells.
- Off-CPU development is permitted, but an off-CPU stack family must pass a
  later bounded, deterministic, non-citable breathing check before its first Q
  registration. Level 0's CPU result does not transfer.
- Strict S remains unavailable. The signed base has exactly T, Q, and C.

## T envelope and power-cycle semantics

`E1=168_DEVICE_HOURS` is cumulative aggregate active time for processes
training registrable learners on real T worlds. Concurrent processes consume
time additively. Test-only fixtures and smoke tests mechanically unable to touch
real T worlds consume no E1.

`E2=12_CANONICAL_CANDIDATES` limits behavior-distinct registrations.
Conservative canonicalization treats an unknown change as behavior-relevant;
behavior-inert changes cannot replenish or consume a new slot.

`E3=48_WALL_HOURS_OR_40_DEVICE_HOURS` requires a full review at the first of 48
elapsed calendar hours or 40 newly consumed E1 hours after activation or the
previous completed E3 review. Calendar time includes powered-off intervals. A
maintenance checkpoint alone does not reset either E3 clock.

A planned host power-off is a non-scientific operational pause. Once real T
exists, every real-T process must be quiesced; E1 must be charged through that
boundary; a resumable state checkpoint, hashes, counters, linked append-only
ledger entry, file flush, and parent-directory flush must be durable before
power removal. The pause is neither `T_AUTHOR_STOP` nor
`T_ENVELOPE_EXHAUSTED`, erases no E1/E2 use, and resets no E3 clock. Resume must
verify the checkpoint/ledger chain, restore the counters, and complete any
overdue E3 review before new real-T work. If T has never been activated, the
ledger records that fact and no fictitious learner checkpoint is created.

## Authorization boundary

This signature authorizes only:

1. WP-1 lineage/bootstrap implementation and tests: the
   `successor/officina/` namespace, manifests, hash-pinned lineage, fail-closed
   quarantine path allowlist, non-promotable engineering-fixture tags, and an
   empty append-only T-ledger skeleton.
2. WP-2 governance-library implementation and tests on dummy/test-only
   fixtures: validity-first terminal taxonomy, canonical serialization and
   hashing, PRF/domain machinery, one-shot claim/driver primitives, accounting,
   atomic checkpoint/ledger flush, pause/resume verification, and escrow
   building blocks.

It does not authorize an actual breathing-check qualification, entropy draw,
real world, T activation or run, candidate registration, Q attempt, promotion,
scientific specification, preregistration lock, C-root generation, escrow,
C execution, outcome, or claim movement. WP-3 must be independently drafted,
reviewed, and signed before any real T world exists. WP-6 and every later gate
retain their own review and signature requirements.

The earlier out-of-sequence bare WP token was non-operative. This complete,
reviewed packet is the first effective WP-1/WP-2 authorization.

## Governing hashes

```text
03c4d52bd286956ada8930a20e74111d291e8684e1a36a7d0402d07b526913bb  successor/CHARTER_SIGNATURE.md
0f62759274fc558fed0a83e3545891f64481c983eac6c898fd0908694ebf6f73  successor/AUTHOR_CHOICE_PACKET_V1_DRAFT.md
e49390adb35aa6de5a5be3224defd408a2b236bb3798a19e9efd1bc3350086cd  successor/AUTHOR_SELECTIONS_V1_PROVISIONAL.md
212434f3df8f642692112cf21788d9b6407cc0973828a7a5f509f4d0b94fd259  reviews/opus_successor_author_selections_v1_review.md
47d869c7b8d972e8be35b9eda7b1e3709be0311d4f459ca86ac31f8e17257bc1  reviews/sol_successor_author_selections_v1_review.md
```

Saved chat responses are provenance aids. The formal documents and hashes above
govern.
