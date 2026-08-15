# Phase-2 Stage-B recovery checkpoint — 2026-08-15

## Status

This directory is a durable forensic checkpoint recovered after the loss of
`/tmp` in a power outage. Recovery used recorded Claude and Codex tool payloads;
it did not regenerate scientific data and did not call the frozen
`select_l2_code_gate_rows` scan.

`SHA256SUMS` contains the previously pinned hash of every recovered artifact.
The recovery script refuses both a hash mismatch and an overwrite of differing
bytes.

## Directory meanings

- `accepted_l2/` contains the byte-exact accepted final L2 annex, production
  generator, V5 test, frozen code-gate JSON and exclusion ledger V3.
- `accepted_authority/` contains the byte-exact Stage-B development-core
  charter v1.1.1 recovered from three mutually identical full-file Claude Read
  payloads and verified against its previously pinned SHA-256.
- `archive/accepted_l01/` contains the byte-exact accepted L0/L1 source tree and
  exclusion ledger V2.
- `patches/` contains the byte-exact accepted L0/L1 V3 and L2 V5 delta and
  cumulative patches.
- `archive/unaccepted_l3/` contains the exact L3 draft payloads for provenance.
  They were never accepted and have no implementation authority.
- `science_inputs/` snapshots the six surviving route, novelty, engineering and
  scientific-contract reports that determine the next scientific decision.
- `tools/recover_from_transcripts.py` is the reproducible extraction and hash
  verification procedure. It also regenerates all four patch artifacts from the
  pinned MINIMO base and durable Stage-A patch.
- `RECOVERY_VERIFICATION.md` records the independent patch-route and Stage-B
  execution checks performed after recovery.

## Authority boundary

This checkpoint proves recovery of historical bytes. It does not convert L2
fixtures into scientific evidence, accept L3, authorize L4, mint a root, run a
selector scan, train a learner, or authorize a scientific experiment.

The original Philosophia repository remains at accepted Stage A commit
`41adcaa96e3281746a6e59247d0fed5d1c42260c`. The historical MINIMO base is
`6066f482c6752915ad21119f93dc162f4cb9db72`.

## Storage rule learned from the outage

`/tmp` is disposable execution space only. A contract, accepted disposition,
patch, frozen JSON object, manifest or scientific decision is authoritative only
after it has a versioned durable copy. A temporary worktree must be reproducible
from a pinned base plus durable patches; it must not be the sole copy of work.
