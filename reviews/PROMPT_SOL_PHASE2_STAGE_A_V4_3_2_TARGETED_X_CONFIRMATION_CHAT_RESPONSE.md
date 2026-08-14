CONFIRM_STAGE_A_V4_3_2_X

1. Confirmed: `init_seed` accepts exact non-bool integers only in `[0, 2**32-1]` at [phase2_spec.py](/tmp/minimo_stagea_v432_x_confirm_20260814/learning/phase2_spec.py:202).

2. Confirmed: `2**32-1` passed the public boundary; `2**32` raised `IsolatedInvalidSpec` before multiprocessing context creation. Regression: [test_phase2_root.py](/tmp/minimo_stagea_v432_x_confirm_20260814/learning/test_phase2_root.py:809).

3. Confirmed: the included probe and an independent 64-draw probe reproduced byte-identical CPU streams for seeds `0` and `2**32` under Torch `2.13.0+cu130`.

4. Confirmed: the complete Stage-A gate passed 126/126 in 49.160 seconds, with no direct regression in previously confirmed cells.

Commands/counts:

- Patch SHA-256 and pinned commit matched.
- Fresh clone, detached checkout, `git apply --check`, patch application, and `git diff --check`: passed.
- Independent boundary probe: 3 valid and 5 invalid seed cases passed; public acceptance/refusal passed.
- Backend alias probe: 64/64 draws identical.
- Stage-A gate: 126/126 passed.

This confirmation authorizes no training, carrier, SELF/YOKED execution, commit, or push.
