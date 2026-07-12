# Level 0 reconstruction choices v2

Status: source-reconciled specification, not yet implemented at this commit.
No outcome run or preregistration lock is authorized.

V2 supersedes only the trajectory-sensitive v1 cells reopened by the official
companion training source:

- R1-v2: AdamW uses the source ten-update warmup pinned in
  COMPANION_CONFIG_TRACE.md; constant LR is superseded.
- R2-v2: optimization uses 114-class CE; reported accuracy/loss and Fourier
  diagnostics use 113 residue classes.
- R4-v2: source-scaled normal initialization replaces Xavier uniform; the
  domain-separated torch seed remains an independent reconstruction choice.
- R5-v2: CPython 3.12.3 Random(seed).shuffle replaces torch.randperm.

R3 attention scaling and R6 arm hierarchy are unchanged. Storage orientations
may remain mathematically equivalent to the source because no source checkpoint
is imported; initialization distributions and draw order must match the trace.

The existing resource scout remains resource evidence only. Its v1 deterministic
prefix is superseded and cannot certify v2.
