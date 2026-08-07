# LEGION_DEVICE_BENCHMARK

NON-CITABLE engineering one-step wall-clock probe only.
No scientific datum, comparative result, or claim.
Does not reopen frozen Level 1 feasibility records.

env: torch=2.7.0+cu128; device=NVIDIA GeForce RTX 4060 Laptop GPU; cuda_available=True; interpreter=ComfyUI .venv (no project venv created).

Runtime notes: skipped `configure_canonical_runtime()` pins. DEV-ONLY monkeypatch of `ContactTransformer.forward` CPU-device guard. Warmup excluded from timing; `torch.cuda.synchronize()` around timed CUDA regions. Each (device, length) run is an isolated subprocess.

DEV memory note: stock `feasibility_committee_step` retains four attention autograd graphs; at history_len>=512 that spills past 8GB VRAM into system RAM (cuda@512 then ~matched CPU). CUDA timings use a DEV monkeypatch: sequential per-member fwd+bwd+opt, with microbatch=512 when history_len>512 (mean-CE via sum/batch; finite-path equivalent) so timings reflect in-VRAM GPU compute. `cpu` row is stock full_history_committee_step (shape anchor); `cpu_seq` is the FLOP-matched baseline for the speedup ratio.

## One-step timings (seconds/step)

| history_len | device | seconds/step |
| ---: | --- | ---: |
| 512 | cpu | 22.606054 |
| 512 | cpu_seq | 9.437214 |
| 512 | cuda | 1.431451 |
| 1024 | cuda | 2.558858 |
| 2000 | cuda | 4.988217 |

## GPU-vs-CPU speedup at history_len=512

fair (cpu_seq/cuda) speedup at 512 = 9.437214 / 1.431451 = 6.59x; vs stock cpu anchor = 22.606054 / 1.431451 = 15.79x (stock retains 4 graphs; not FLOP-matched to sequential cuda)

## Estimated full B=2000 run wall-clock on GPU

Estimate (not a measurement): assume near-linear `seconds/step ≈ c * history_len` through origin on measured CUDA points; full-history cost `sum_{h=1..B} c*h = c*B*(B+1)/2`. Fit used successful CUDA lengths [512, 1024, 2000].

Measured OLS slope c = 0.002509943 s per history token-step.
Estimated full-run wall-clock on GPU ≈ 1.40 h (5022.4 s).

## Lever sentence

Yes — GPU is the lever: at history_len=512 the RTX 4060 Laptop sequential step is 6.6x faster than the matched CPU path (1.4315s vs 9.437s), and the near-linear extrapolation puts a full B=2000 GPU trajectory near 1.40 h (5022.4 s) rather than tens of CPU hours.
