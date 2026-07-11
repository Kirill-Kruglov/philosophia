# Level 0 hardware baseline

Observed 2026-07-11. Platform metadata, not a scientific outcome.

- Ubuntu 24.04.4 LTS, kernel 6.17.0-1023-oem.
- AMD Ryzen AI Max+ 395 / Radeon 8060S; 16 cores, 32 threads.
- 123 GiB visible memory; 78 GiB available at inspection.
- amdgpu device 1002:1586; /dev/kfd and renderD128 accessible.
- User belongs to video and render groups.
- No ROCm/HIP utilities, PyTorch, or JAX were initially in the venv.
- Official CPU PyTorch 2.9.1+cpu is now the canonical smoke backend.
- llama-server Vulkan inference is not a training backend.

Install the pinned canonical backend with:

    .venv/bin/pip install -r requirements/train-cpu.txt

## Backend gate

CPU remains canonical until acceleration passes forward/backward/optimizer,
determinism tolerance, identical data and initial hashes, fixed-prefix
loss/gradient equivalence, and checkpoint round-trip.

AMD lists gfx1151 / Ryzen AI Max+ 395 with ROCm 7.2, PyTorch 2.9, and Python
3.12, but lists Ubuntu 24.04.3 and calls support preliminary. This host is
24.04.4 and lacks ROCm user space, so installing it is a separate platform
change.

- [AMD support matrix](https://rocm.docs.amd.com/projects/radeon-ryzen/en/docs-7.2/docs/compatibility/compatibilityryz/native_linux/native_linux_compatibility.html)
- [PyTorch installation](https://docs.pytorch.org/get-started/locally/)

The likely constraint is long-run optimizer time across seeds, not memory. A
timing scout must project the locked battery before preregistration.
