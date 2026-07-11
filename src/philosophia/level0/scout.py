from __future__ import annotations

import hashlib
import json
from pathlib import Path
import resource
import statistics
import subprocess
import time
from typing import Iterable

import torch

from .checkpoint import (
    build_metadata,
    load_checkpoint,
    model_state_hash,
    optimizer_state_hash,
    save_checkpoint,
)
from .config import RunConfig, config_hash, paper_mainline_arm
from .data import LearnerView, build_dataset
from .interlock import (
    SCOUT_MAX_SECONDS,
    SCOUT_MAX_STEPS,
    ExecutionInterlock,
    ExecutionNotAuthorized,
)
from .model import GrokkingTransformer
from .train import make_optimizer, optimization_step


SCOUT_KIND = "timing-storage-scout / non-outcome"
PRIMARY_STEPS = 25
REPLAY_STEPS = 25
REPORT_NAME = "timing-storage-scout_non-outcome.json"
CHECKPOINT_NAME = "timing-storage-scout_non-outcome.pt"


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _combined_state_hash(
    model: GrokkingTransformer,
    optimizer: torch.optim.Optimizer,
) -> str:
    payload = f"{model_state_hash(model)}:{optimizer_state_hash(optimizer)}"
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def _aggregate_latencies(latencies: Iterable[float]) -> dict[str, float | int]:
    values = tuple(latencies)
    if not values:
        raise ValueError("at least one latency is required")
    return {
        "count": len(values),
        "mean_ms": statistics.fmean(values) * 1000.0,
        "median_ms": statistics.median(values) * 1000.0,
        "min_ms": min(values) * 1000.0,
        "max_ms": max(values) * 1000.0,
    }


def _repository_head(root: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def _step_prefix(
    *,
    model: GrokkingTransformer,
    optimizer: torch.optim.Optimizer,
    learner: LearnerView,
    interlock: ExecutionInterlock,
    steps: int,
    deadline: float,
    record_latency: bool,
) -> list[float]:
    latencies: list[float] = []
    for _ in range(steps):
        if time.monotonic() >= deadline:
            raise ExecutionNotAuthorized("scout driver reached its wall-clock cap")
        started = time.perf_counter()
        optimization_step(model, optimizer, learner, interlock=interlock)
        elapsed = time.perf_counter() - started
        if time.monotonic() > deadline:
            raise ExecutionNotAuthorized("scout step crossed its wall-clock cap")
        if record_latency:
            latencies.append(elapsed)
    return latencies


def run_timing_storage_scout(*, output_dir: Path) -> Path:
    if PRIMARY_STEPS + REPLAY_STEPS > SCOUT_MAX_STEPS:
        raise RuntimeError("scout source exceeds the interlock step cap")

    report_path = output_dir / REPORT_NAME
    checkpoint_path = output_dir / CHECKPOINT_NAME
    if report_path.exists() or checkpoint_path.exists():
        raise FileExistsError("scout artifacts already exist; refusing a second run")
    output_dir.mkdir(parents=True, exist_ok=True)

    root = Path(__file__).resolve().parents[3]
    config = RunConfig(arm=paper_mainline_arm(), master_seed=0)
    if torch.get_default_dtype() != torch.float32:
        raise RuntimeError("scout requires default float32")
    torch.use_deterministic_algorithms(True)

    interlock = ExecutionInterlock.timing_storage_scout()
    scout_started = time.monotonic()
    deadline = scout_started + SCOUT_MAX_SECONDS
    rss_before_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    dataset = build_dataset(config)
    learner = dataset.learner
    primary_model = GrokkingTransformer(config.model, init_seed=config.init_seed)
    primary_optimizer = make_optimizer(primary_model, config)
    primary_latencies = _step_prefix(
        model=primary_model,
        optimizer=primary_optimizer,
        learner=learner,
        interlock=interlock,
        steps=PRIMARY_STEPS,
        deadline=deadline,
        record_latency=True,
    )
    primary_prefix_hash = _combined_state_hash(primary_model, primary_optimizer)

    source_paths = {
        "config_trace": root / "experiments/level_0_grokking/CONFIG_TRACE.md",
        "reconstruction_choices": (
            root / "experiments/level_0_grokking/RECONSTRUCTION_CHOICES_V1.md"
        ),
        "execution_interlock": (
            root / "experiments/level_0_grokking/EXECUTION_INTERLOCK.md"
        ),
    }
    metadata = build_metadata(
        purpose=SCOUT_KIND,
        config=config,
        split_hash=dataset.split_hash,
        repository_head=_repository_head(root),
        source_hashes={
            name: _sha256_file(path) for name, path in source_paths.items()
        },
        model=primary_model,
        optimizer=primary_optimizer,
    )
    save_checkpoint(
        checkpoint_path,
        step=PRIMARY_STEPS,
        config=config,
        model=primary_model,
        optimizer=primary_optimizer,
        metadata=metadata,
    )

    loaded_model = GrokkingTransformer(config.model, init_seed=999)
    loaded_optimizer = make_optimizer(loaded_model, config)
    load_checkpoint(
        checkpoint_path,
        model=loaded_model,
        optimizer=loaded_optimizer,
        expected_config_hash=config_hash(config),
        expected_split_hash=dataset.split_hash,
    )
    if _combined_state_hash(loaded_model, loaded_optimizer) != primary_prefix_hash:
        raise RuntimeError("checkpoint round-trip changed the scout prefix state")

    replay_model = GrokkingTransformer(config.model, init_seed=config.init_seed)
    replay_optimizer = make_optimizer(replay_model, config)
    _step_prefix(
        model=replay_model,
        optimizer=replay_optimizer,
        learner=learner,
        interlock=interlock,
        steps=REPLAY_STEPS,
        deadline=deadline,
        record_latency=False,
    )
    replay_prefix_hash = _combined_state_hash(replay_model, replay_optimizer)
    if replay_prefix_hash != primary_prefix_hash:
        raise RuntimeError("deterministic scout prefix replay diverged")

    wall_seconds = time.monotonic() - scout_started
    rss_after_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report = {
        "kind": SCOUT_KIND,
        "scientific_outcome": False,
        "arm": "A",
        "master_seed": 0,
        "device": "cpu",
        "dtype": "torch.float32",
        "torch_version": str(torch.__version__),
        "config_hash": config_hash(config),
        "split_hash": dataset.split_hash,
        "steps": {
            "primary": PRIMARY_STEPS,
            "replay": REPLAY_STEPS,
            "total": interlock.steps_used,
            "hard_cap": SCOUT_MAX_STEPS,
        },
        "wall_seconds": wall_seconds,
        "wall_hard_cap_seconds": SCOUT_MAX_SECONDS,
        "primary_step_latency": _aggregate_latencies(primary_latencies),
        "peak_rss_kib": rss_after_kib,
        "peak_rss_delta_kib": max(0, rss_after_kib - rss_before_kib),
        "checkpoint": {
            "name": CHECKPOINT_NAME,
            "bytes": checkpoint_path.stat().st_size,
            "sha256": _sha256_file(checkpoint_path),
            "purpose": metadata.purpose,
        },
        "deterministic_prefix": {
            "primary_hash": primary_prefix_hash,
            "replay_hash": replay_prefix_hash,
            "match": True,
        },
        "contamination_guards": {
            "held_out_evaluated": False,
            "verdict_derived": False,
            "loss_series_persisted": False,
            "preregistration_created": False,
            "decision_created": False,
        },
    }
    temporary = report_path.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(report_path)
    return report_path
