# Level 0 CPU timing and storage scout

Status: completed exactly once under SCOUT_DRIVER_ACCEPTED; non-outcome resource
evidence only.

Source report: scout/timing-storage-scout_non-outcome.json.

The run used Arm A, master seed 0, PyTorch 2.9.1+cpu, CPU float32, 25 measured
full-batch steps and an independent 25-step replay. It evaluated no held-out
data, persisted no loss series, and derived no scientific verdict.

## Guard result

- 50 total steps under the 100-step cap;
- 2.840 seconds under the 120-second wall;
- primary and replay combined model/optimizer hashes match;
- every contamination flag is false;
- no PREREG.lock or decision.json was created;
- the 2,740,993-byte checkpoint is local, ignored, and not a warm-start.

## Measurements

| Quantity | Value |
|---|---:|
| Mean full-batch step | 56.065 ms |
| Median full-batch step | 56.697 ms |
| Minimum / maximum step | 46.833 / 63.608 ms |
| Absolute process peak RSS | 482,628 KiB (471.3 MiB) |
| Checkpoint size | 2,740,993 bytes (2.614 MiB) |

Use the absolute RSS for planning. The reported RSS delta is informational
because ru_maxrss is a process-wide monotonic high-water mark.

## Time projection

A linear compute-only projection from the measured mean gives:

| Battery | Fixed steps | Projected compute time |
|---|---:|---:|
| Arm A, one seed | 40,000 | 37.38 min |
| Arm A, five seeds | 200,000 | 3.11 h |
| Arm A five seeds + Arm B one seed | 320,000 | 4.98 h |
| Arm A five seeds + Arm B three seeds | 560,000 | 8.72 h |
| Arm A five seeds + Arm B five seeds | 800,000 | 12.46 h |

These are planning projections, not runtime guarantees. They exclude evaluation,
Fourier probes, checkpoint I/O, orchestration, and scheduling overhead. The scout
did not record the PyTorch thread count, so portability to a changed process or
host configuration is not established.

## Storage projection

For a fixed cadence c that includes step zero and the final divisible step:

- Arm A checkpoints per seed: 40,000 / c + 1;
- Arm B checkpoints per seed: 120,000 / c + 1;
- projected bytes: checkpoint count times 2,740,993.

Illustrative values below compare candidate cadences without selecting one:

| Cadence | A count | B count | A x5 | A x5 + B x1 | A x5 + B x3 |
|---:|---:|---:|---:|---:|---:|
| 100 | 401 | 1,201 | 5.12 GiB | 8.18 GiB | 14.32 GiB |
| 500 | 81 | 241 | 1.03 GiB | 1.65 GiB | 2.88 GiB |
| 1,000 | 41 | 121 | 0.52 GiB | 0.83 GiB | 1.45 GiB |
| 10,000 | 5 | 13 | 0.06 GiB | 0.10 GiB | 0.16 GiB |

The measured checkpoint contains optimizer state after step 25 and is used as a
conservative uniform-size estimate. Cadence and retention remain lock-stage
choices.

## What this cannot decide

This scout does not inform grokking, convergence, generalization, FIT,
GENERALIZE, DELAYED, persistence window W, delta_min, quorum, thresholds,
control semantics, the null set, or Arm B seed count.
