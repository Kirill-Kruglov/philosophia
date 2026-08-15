# Phase-2 Stage-B recovery verification — 2026-08-15

## Recovered boundary

- MINIMO base: `6066f482c6752915ad21119f93dc162f4cb9db72`
- Stage-B development-core charter v1.1.1 SHA-256:
  `703bf39cfe8f875f9be3781659a7365c1bc99c42f7523e43fef2c0a2c47b8311`
- durable Stage-A patch SHA-256:
  `e08a8d29d67d82297216722b3e13e6c1a3f4bd354962a2865b1cfc57a9980bbd`
- L0/L1 V3 delta SHA-256:
  `1a67b09fb63784662cce56359c5cff897023cceec2f3dd445739d0a04cf00736`
- L0/L1 V3 cumulative SHA-256:
  `c0b0e9ab79a66696231e356a92f6ccace67911d2bbe5906918ca6f4cbbe9a065`
- L2 V5 delta SHA-256:
  `299114e32cbf59edced992a94cdf5c1e03e322cb32dbdb7a3f94f63dc4276b95`
- final cumulative SHA-256:
  `3a570b2e35b15dc796d86cd8a997230c00bbf5aed3b5c06f3b14dca78b46b683`

All four patch hashes were obtained by regenerating Git diffs from the
transcript-recovered source bytes, not by copying a surviving temporary patch.
They equal the hashes pinned before the outage.

## Route equivalence

Two fresh local clones were checked out at the pinned base.

- Route A applied Stage A, then the L0/L1 V3 delta, then the L2 V5 delta.
- Route B applied only the final cumulative patch.
- Every patch passed `git apply --check` before application.
- Both resulting trees contained 96 non-`.git` files and had the same
  path/mode/length/content manifest SHA-256:
  `566ec1e597311b1e9291c8cd1ae51141159314cc7079cb52b0b4153a28cdd88c`.
- Each route changed the same 34 paths relative to the pinned base.
- The L0/L1 delta names exactly its authorized nine paths; the L2 delta names
  exactly `learning/phase2_stageb_generator.py` and
  `learning/test_phase2_stageb_generator.py`.

## Executable verification

The final cumulative patch was applied to another fresh base clone and run with
the existing MINIMO virtual environment:

```text
python -m unittest discover -s learning -t learning \
  -p 'test_phase2_stageb*.py' -v
Ran 67 tests in 0.603s
OK
```

Ordinary discovery does not treat `select_l2_code_gate_rows` as a test. The
frozen `5 x 256` selector scan was not called, no key or root was minted, and no
L3/L4 or scientific execution occurred.

## Manifest verification

From this directory:

```text
sha256sum -c SHA256SUMS
```

verifies all 29 recovered artifacts. Running
`tools/recover_from_transcripts.py` again is idempotent: it replays the recorded
payloads, including the full-file Stage-B charter Read payload, regenerates the
patches and refuses any pinned hash or existing-byte mismatch.
