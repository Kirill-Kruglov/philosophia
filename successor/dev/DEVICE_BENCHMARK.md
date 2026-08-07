# DEVICE_BENCHMARK — STOPPED (CUDA unavailable)

NON-CITABLE engineering probe. No scientific datum or claim.
Does not touch canonical/, experiments/, frozen records, or thresholds.

## Precondition check (failed)

| field | value |
| --- | --- |
| `torch.__version__` | `2.9.1+cpu` (project `.venv`) |
| `torch.cuda.is_available()` | `False` (must be `True` to proceed) |
| `torch.cuda.get_device_name(0)` | n/a |
| host | `workbench` |
| DRM vendor (`/sys/class/drm/.../vendor`) | `0x1002` (AMD) |
| `nvidia-smi` | not present |
| `/dev/nvidia*` | not present |

**STOP.** No GPU step timings were collected. Nothing was installed or configured.
No `src/` changes. No CPU/GPU speedup table.

Re-run this task on the Lenovo Legion host with stock PyTorch+CUDA where
`torch.cuda.is_available()` is `True`.
