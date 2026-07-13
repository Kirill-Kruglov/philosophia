# Level 1 public-root execution protocol

Status: implementation/review candidate. This document does not authorize an
entropy draw.

The durable claim is the operational irreversibility boundary. Once
`PUBLIC_ROOT_DRAW_CLAIM.json` exists, it must never be deleted and the draw
command must never be invoked again, regardless of whether a transcript exists.
The declared threat model is procedural, not protection against a determined
operator who deletes local files.

State routing:

- no claim and no transcript: pre-execution only;
- claim only after an interrupted attempt: signed invalidity review, never rerun;
- claim plus canonical durable transcript plus a failed git commit:
  `PUBLIC_ROOT_COMMIT_PENDING.json`; the root is valid and must not be discarded;
  complete a separately reviewed recovery commit, never redraw;
- `PUBLIC_ROOT_INVALIDITY_REQUIRED.json`: signed invalidity decision, never a
  quiet retry;
- claim and transcript in the enclosing successful git commit: root gate
  complete, subject to post-run verification and push.

Before execution, the final authorization must name both the final docs-only
`EXPECTED_HEAD` and the reviewed code commit `REVIEWED_CODE_HEAD`. The driver
mechanically verifies byte identity for itself plus `public_root.py`,
`allocation.py`, `serialization.py`, `model.py`, and `config.py` between those commits. It
also rechecks an empty index immediately before staging and verifies that only
the claim and transcript are staged.

No recovery command is authorized by this candidate. If commit-pending occurs,
stop and request bounded review of the existing durable artifacts; do not invoke
the draw driver again.
