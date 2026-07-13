# Level 1 public-root one-shot execution signature

Signed by Kirill Kruglov on 2026-07-14, after the reviewed public-root driver
and its execution-authorization contract were committed, and before any Level 1
public-root entropy draw or allocation artifact existed.

```text
I_AUTHORIZE_LEVEL1_PUBLIC_ROOT_DRAW_FROM_THIS_SIGNATURE_COMMIT
```

## Bound commits

```text
AUTHORIZATION_CONTRACT_COMMIT=4981ecf59434ba5cb7cad2854741e18c0ec1ee54
REVIEWED_CODE_HEAD=95adcb5011c170fe9076894f6439f1248538600f
EXPECTED_HEAD=the commit containing this signature file
```

The commit containing this file must add only this signature record. Its hash is
the value passed to `--expected-head`; no tracked commit or modification may
occur between that commit and the one-shot draw. The six reviewed execution
paths must remain byte-identical to `REVIEWED_CODE_HEAD`.

## Authorization boundary

This token authorizes exactly one invocation of the reviewed Level 1
public-root/allocation driver and its automatic claim-and-transcript commit,
subject to every pre-execution predicate and recovery rule in
`PUBLIC_ROOT_EXECUTION_AUTHORIZATION_CANDIDATE.md` and
`PUBLIC_ROOT_EXECUTION_PROTOCOL.md`.

It does not authorize real evaluator-panel generation, feasibility execution,
the comparative scout, N3 selection, a preregistration lock, escrow generation,
learner trajectories, scientific outcome execution, or any redraw after a
failure.
