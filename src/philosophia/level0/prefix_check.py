from __future__ import annotations

import hashlib
import json
from pathlib import Path
import struct

import torch

from .checkpoint import model_state_hash, optimizer_state_hash
from .config import (
    RECONSTRUCTION_ID,
    RunConfig,
    configure_canonical_torch_runtime,
    config_hash,
    paper_mainline_arm,
)
from .data import build_dataset
from .interlock import ExecutionInterlock
from .model import GrokkingTransformer
from .train import make_optimizer, optimization_step


PREFIX_KIND = "companion-v2-determinism-prefix / non-outcome"
PREFIX_STEPS = 10
REPORT_NAME = "companion-v2-determinism-prefix_non-outcome.json"


def _sequence_hash(values: tuple[float, ...]) -> str:
    digest = hashlib.sha256()
    for value in values:
        digest.update(struct.pack("!d", value))
    return digest.hexdigest()


def _combined_state_hash(
    model: GrokkingTransformer,
    optimizer: torch.optim.Optimizer,
) -> str:
    value = f"{model_state_hash(model)}:{optimizer_state_hash(optimizer)}"
    return hashlib.sha256(value.encode("ascii")).hexdigest()


def _run_prefix(config: RunConfig) -> dict[str, str | int]:
    dataset = build_dataset(config)
    model = GrokkingTransformer(config.model, init_seed=config.init_seed)
    optimizer = make_optimizer(model, config)
    initial_hash = model_state_hash(model)
    permit = ExecutionInterlock.bounded_check(PREFIX_STEPS)
    losses = tuple(
        optimization_step(
            model,
            optimizer,
            dataset.learner,
            interlock=permit,
        ).loss
        for _ in range(PREFIX_STEPS)
    )
    return {
        "steps": permit.steps_used,
        "init_hash": initial_hash,
        "split_hash": dataset.split_hash,
        "loss_sequence_hash": _sequence_hash(losses),
        "final_state_hash": _combined_state_hash(model, optimizer),
    }


def run_companion_v2_prefix_check(*, output_dir: Path) -> Path:
    """Run the reviewed non-outcome check; execution requires separate authorization."""
    report_path = output_dir / REPORT_NAME
    if report_path.exists():
        raise FileExistsError("v2 prefix report already exists; refusing a second run")
    configure_canonical_torch_runtime()
    if torch.get_default_dtype() != torch.float32:
        raise RuntimeError("v2 prefix check requires default float32")
    torch.use_deterministic_algorithms(True)

    config = RunConfig(arm=paper_mainline_arm(), master_seed=0)
    primary = _run_prefix(config)
    replay = _run_prefix(config)
    match = primary == replay
    if not match:
        raise RuntimeError("companion-v2 deterministic prefix replay diverged")

    report = {
        "kind": PREFIX_KIND,
        "scientific_outcome": False,
        "reconstruction_id": RECONSTRUCTION_ID,
        "arm": "A",
        "master_seed": 0,
        "device": "cpu",
        "dtype": "torch.float32",
        "torch_version": str(torch.__version__),
        "torch_num_threads": torch.get_num_threads(),
        "torch_num_interop_threads": torch.get_num_interop_threads(),
        "config_hash": config_hash(config),
        "steps": {
            "per_replay": PREFIX_STEPS,
            "total": PREFIX_STEPS * 2,
            "bounded_check_cap": 16,
        },
        "deterministic_prefix": {
            "primary": primary,
            "replay": replay,
            "match": match,
        },
        "contamination_guards": {
            "held_out_evaluated": False,
            "verdict_derived": False,
            "loss_values_persisted": False,
            "checkpoint_created": False,
            "preregistration_created": False,
            "decision_created": False,
        },
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    temporary = report_path.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(report_path)
    return report_path
