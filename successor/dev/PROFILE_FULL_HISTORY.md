# PROFILE_FULL_HISTORY

NON-CITABLE engineering wall-clock attribution only.
No scientific datum, comparative result, or claim.
Does not reopen the censored Level 1 feasibility v2 record.

Runtime: CPU via `configure_canonical_runtime()`; modulus=66 (shape realism only).

## Per-step phase times (seconds)

| history_len | (a) stack | (b) committee fwd+bwd+opt | (c) isfinite scan | sum |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0.000111 | 0.057152 | 0.003151 | 0.060414 |
| 32 | 0.000029 | 1.912532 | 0.042915 | 1.955475 |
| 64 | 0.000052 | 3.888585 | 0.058143 | 3.946780 |
| 128 | 0.000082 | 7.755768 | 0.085035 | 7.840884 |
| 256 | 0.000139 | 16.669233 | 0.003143 | 16.672515 |
| 512 | 0.000201 | 33.436834 | 0.003190 | 33.440225 |

## Growth exponent

Fit: `log(sum_seconds) = alpha * log(history_len) + beta` over history_len in {1, 32, 64, 128, 256, 512}.

Measured growth exponent alpha = 1.011912

Interpretation check: alpha≈1 is linear in history_len; measured alpha=1.012.

## cProfile top 20 (cumulative)

```
         107436 function calls (106234 primitive calls) in 63.930 seconds

   Ordered by: cumulative time
   List reduced from 183 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        6    0.006    0.001   63.916   10.653 /home/master/llm_projects/philosophia/successor/dev/profile_full_history.py:41(_timed_full_history_committee_step)
        6    0.000    0.000   63.714   10.619 /home/master/llm_projects/philosophia/src/philosophia/level1/train.py:47(feasibility_committee_step)
       24    0.000    0.000   37.811    1.575 /home/master/llm_projects/philosophia/.venv/lib/python3.12/site-packages/torch/_tensor.py:570(backward)
       24    0.001    0.000   37.810    1.575 /home/master/llm_projects/philosophia/.venv/lib/python3.12/site-packages/torch/autograd/__init__.py:243(backward)
       24    0.000    0.000   37.808    1.575 /home/master/llm_projects/philosophia/.venv/lib/python3.12/site-packages/torch/autograd/graph.py:832(_engine_run_backward)
       24   37.808    1.575   37.808    1.575 {method 'run_backward' of 'torch._C._EngineBase' objects}
   192/24    0.001    0.000   25.864    1.078 /home/master/llm_projects/philosophia/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py:1771(_wrapped_call_impl)
   192/24    0.411    0.002   25.864    1.078 /home/master/llm_projects/philosophia/.venv/lib/python3.12/site-packages/torch/nn/modules/module.py:1779(_call_impl)
       24    0.217    0.009   25.864    1.078 /home/master/llm_projects/philosophia/src/philosophia/level1/model.py:155(forward)
       48   18.026    0.376   25.124    0.523 /home/master/llm_projects/philosophia/src/philosophia/level1/model.py:108(forward)
       48    2.971    0.062    2.971    0.062 {method 'masked_fill' of 'torch._C.TensorBase' objects}
       48    2.737    0.057    2.737    0.057 {built-in method torch.softmax}
       48    0.672    0.014    0.672    0.014 {built-in method torch.relu}
      120    0.001    0.000    0.588    0.005 /home/master/llm_projects/philosophia/.venv/lib/python3.12/site-packages/torch/nn/modules/normalization.py:228(forward)
      120    0.001    0.000    0.588    0.005 /home/master/llm_projects/philosophia/.venv/lib/python3.12/site-packages/torch/nn/functional.py:2880(layer_norm)
      120    0.586    0.005    0.586    0.005 {built-in method torch.layer_norm}
       48    0.233    0.005    0.233    0.005 {method 'contiguous' of 'torch._C.TensorBase' objects}
      108    0.000    0.000    0.197    0.002 {built-in method builtins.all}
      726    0.001    0.000    0.195    0.000 /home/master/llm_projects/philosophia/successor/dev/profile_full_history.py:72(<genexpr>)
      744    0.190    0.000    0.190    0.000 {built-in method torch.isfinite}
```

## CUDA / HIP availability (report only)

`torch.cuda.is_available()` = False
`torch.version.hip` = None

## Dominating phase (raw measurement)

Across reported lengths, phase dominance is: (b) committee fwd+bwd+opt at history_len=1 (94.6% of sum); (b) committee fwd+bwd+opt at history_len=32 (97.8% of sum); (b) committee fwd+bwd+opt at history_len=64 (98.5% of sum); (b) committee fwd+bwd+opt at history_len=128 (98.9% of sum); (b) committee fwd+bwd+opt at history_len=256 (100.0% of sum); (b) committee fwd+bwd+opt at history_len=512 (100.0% of sum). Phase (b) grows with history_len (ratio 33.436834/0.057152 = 585.051 from len 1 to 512; log-log exponent of sum = 1.012). Phase (c) stays a small absolute overhead (range 0.003143–0.085035 s; its own log-log exponent vs history_len = 0.062, not tracking the linear growth of (b)), i.e. independent of history length at the scale of the step; phase (a) remains negligible.
