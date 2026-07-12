from __future__ import annotations

from dataclasses import asdict
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time
from typing import Any, Mapping

import torch

from .checkpoint import (
    build_metadata,
    load_checkpoint,
    model_state_hash,
    optimizer_state_hash,
    save_checkpoint,
)
from .config import configure_canonical_torch_runtime, config_hash
from .data import DatasetBundle, build_dataset, random_label_control
from .fourier import frequency_energy, project_residue_axis
from .interlock import ExecutionInterlock, ExecutionNotAuthorized
from .metrics import evaluate, full_parameter_l2, scored_parameter_l2
from .model import GrokkingTransformer
from .scientific_spec import (
    RunDefinition,
    ScientificSpecError,
    load_lock,
    load_spec,
    run_config,
    run_definitions,
    sha256_file,
)
from .train import make_optimizer, optimization_step


MANIFEST_NAME = "run_manifest.json"
METRICS_NAME = "metrics.jsonl"
RESUME_NAME = "resume_latest.pt"
COMPLETE_NAME = "run_complete.json"
RESOURCE_STOP_NAME = "RESOURCE_STOP.json"
RECOVERY_LOG_NAME = "recovery_events.jsonl"


class ResourceStop(RuntimeError):
    pass


def _repository_head(root: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def _atomic_json(path: Path, value: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(
        (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")
    )
    os.replace(temporary, path)


def _atomic_torch_save(path: Path, value: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    torch.save(value, temporary)
    os.replace(temporary, path)


def _directory_bytes(path: Path) -> int:
    return sum(item.stat().st_size for item in path.rglob("*") if item.is_file())


def _append_json_line(path: Path, value: Mapping[str, object]) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def _read_metrics(path: Path) -> list[dict[str, Any]]:
    observations: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise ScientificSpecError("cannot read metrics prefix") from error
    for line in lines:
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ScientificSpecError("metrics line is not an object")
        observations.append(value)
    steps = [int(value["step"]) for value in observations]
    if any(right <= left for left, right in zip(steps, steps[1:])):
        raise ScientificSpecError("metrics steps are not strictly increasing")
    return observations


def _recover_uncommitted_metric_tail(
    *,
    metrics_path: Path,
    checkpoint_step: int,
    checkpoint_metrics_hash: str,
    snapshot_dir: Path,
) -> list[dict[str, Any]]:
    raw_lines = metrics_path.read_bytes().splitlines(keepends=True)
    observations = _read_metrics(metrics_path)
    if len(observations) < 2:
        raise ScientificSpecError("checkpoint/metrics step mismatch")
    tail_step = int(observations[-1]["step"])
    prefix_step = int(observations[-2]["step"])
    if checkpoint_step != prefix_step or tail_step <= checkpoint_step:
        raise ScientificSpecError("checkpoint/metrics step mismatch")
    prefix_bytes = b"".join(raw_lines[:-1])
    if hashlib.sha256(prefix_bytes).hexdigest() != checkpoint_metrics_hash:
        raise ScientificSpecError("uncommitted metric prefix does not match checkpoint")

    recovery = {
        "kind": "philosophia-level0-cadence-transaction-recovery",
        "checkpoint_step": checkpoint_step,
        "discarded_tail_step": tail_step,
        "discarded_tail_sha256": hashlib.sha256(raw_lines[-1]).hexdigest(),
        "reason": "metric line committed before resume-checkpoint replacement",
    }
    _append_json_line(metrics_path.parent / RECOVERY_LOG_NAME, recovery)
    temporary = metrics_path.with_suffix(metrics_path.suffix + ".tmp")
    temporary.write_bytes(prefix_bytes)
    os.replace(temporary, metrics_path)
    stale_snapshot = snapshot_dir / f"model_{tail_step:08d}.pt"
    if stale_snapshot.exists():
        stale_snapshot.unlink()
    return observations[:-1]


def _static_source_hashes(
    *,
    root: Path,
    spec_path: Path,
    lock_path: Path,
) -> dict[str, str]:
    return {
        "scientific_spec": sha256_file(spec_path),
        "prereg_lock": sha256_file(lock_path),
        "config_source": sha256_file(root / "src/philosophia/level0/config.py"),
        "data_source": sha256_file(root / "src/philosophia/level0/data.py"),
        "model_source": sha256_file(root / "src/philosophia/level0/model.py"),
        "train_source": sha256_file(root / "src/philosophia/level0/train.py"),
        "outcome_source": sha256_file(root / "src/philosophia/level0/outcome.py"),
    }


def _verify_locked_sources(
    lock: Mapping[str, Any],
    *,
    root: Path,
) -> None:
    raw_hashes = lock.get("source_hashes")
    if not isinstance(raw_hashes, Mapping):
        raise ScientificSpecError("lock has no source hash map")
    for relative_path, expected_hash in raw_hashes.items():
        path = root / str(relative_path)
        if not path.is_file() or sha256_file(path) != expected_hash:
            raise ScientificSpecError(f"locked source drift: {relative_path}")



def _verify_repository_binding(
    *,
    root: Path,
    lock_path: Path,
    lock: Mapping[str, Any],
) -> None:
    canonical_lock = root / "experiments/level_0_grokking/PREREG.lock"
    if lock_path.resolve() != canonical_lock.resolve():
        raise ScientificSpecError("lock path differs from the canonical PREREG.lock")
    source_commit = str(lock["source_commit"])
    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", source_commit, "HEAD"],
        cwd=root,
        check=False,
    )
    if ancestor.returncode != 0:
        raise ScientificSpecError("locked source commit is not an ancestor of HEAD")
    try:
        relative_lock = lock_path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError as error:
        raise ScientificSpecError("PREREG.lock must live inside the repository") from error
    tracked = subprocess.run(
        ["git", "ls-files", "--error-unmatch", relative_lock],
        cwd=root,
        check=False,
        capture_output=True,
    )
    unchanged = subprocess.run(
        ["git", "diff", "--quiet", "HEAD", "--", relative_lock],
        cwd=root,
        check=False,
    )
    if tracked.returncode != 0 or unchanged.returncode != 0:
        raise ScientificSpecError("PREREG.lock must be committed and unchanged")

def _dataset_for_run(
    definition: RunDefinition,
    *,
    label_seed: int,
) -> DatasetBundle:
    bundle = build_dataset(run_config(definition))
    if definition.control == "random-label":
        bundle = random_label_control(bundle, seed=label_seed)
    if bundle.split_hash != definition.split_hash:
        raise ScientificSpecError(f"split hash drift for {definition.run_id}")
    if definition.label_hash is not None and bundle.universe_hash != definition.label_hash:
        raise ScientificSpecError(f"label hash drift for {definition.run_id}")
    return bundle


@torch.no_grad()
def _frequency_energies(model: GrokkingTransformer) -> dict[str, list[float]]:
    embedding = model.W_E[: model.config.reporting_classes]
    unembedding = model.W_U[:, : model.config.reporting_classes].T
    embedding_energy = frequency_energy(project_residue_axis(embedding))
    unembedding_energy = frequency_energy(project_residue_axis(unembedding))
    return {
        "embedding": [float(value) for value in embedding_energy],
        "unembedding": [float(value) for value in unembedding_energy],
    }


def _observation(
    *,
    step: int,
    model: GrokkingTransformer,
    optimizer: torch.optim.Optimizer,
    dataset: DatasetBundle,
    interlock: ExecutionInterlock,
) -> dict[str, object]:
    train = evaluate(
        model,
        dataset.learner.inputs,
        dataset.learner.targets,
        interlock=interlock,
    )
    held_out = evaluate(
        model,
        dataset.evaluation.inputs,
        dataset.evaluation.targets,
        interlock=interlock,
    )
    if not all(
        torch.isfinite(torch.tensor(value))
        for value in (train.loss, train.accuracy, held_out.loss, held_out.accuracy)
    ):
        raise FloatingPointError("non-finite outcome metric")
    return {
        "step": step,
        "elapsed_seconds": interlock.elapsed_seconds,
        "learning_rate": float(optimizer.param_groups[0]["lr"]),
        "train": asdict(train),
        "held_out": asdict(held_out),
        "scored_parameter_l2": scored_parameter_l2(model),
        "full_parameter_l2": full_parameter_l2(model),
        "frequency_energy": _frequency_energies(model),
    }


def _save_model_snapshot(
    path: Path,
    *,
    step: int,
    model: GrokkingTransformer,
    manifest_hash: str,
) -> None:
    _atomic_torch_save(
        path,
        {
            "kind": "philosophia-level0-model-snapshot",
            "step": step,
            "manifest_hash": manifest_hash,
            "model_state_hash": model_state_hash(model),
            "model_state": model.state_dict(),
        },
    )


def _checkpoint_sources(
    static_hashes: Mapping[str, str],
    *,
    metrics_path: Path,
    manifest_path: Path,
) -> dict[str, str]:
    return {
        **static_hashes,
        "metrics_prefix": sha256_file(metrics_path),
        "run_manifest": sha256_file(manifest_path),
    }


def _save_resume_checkpoint(
    *,
    output_dir: Path,
    step: int,
    definition: RunDefinition,
    config: Any,
    dataset: DatasetBundle,
    model: GrokkingTransformer,
    optimizer: torch.optim.Optimizer,
    repository_head: str,
    static_hashes: Mapping[str, str],
    full_checkpoint_cadence: int,
) -> None:
    sources = _checkpoint_sources(
        static_hashes,
        metrics_path=output_dir / METRICS_NAME,
        manifest_path=output_dir / MANIFEST_NAME,
    )
    metadata = build_metadata(
        purpose=f"level0-locked-outcome/{definition.run_id}",
        config=config,
        split_hash=dataset.split_hash,
        repository_head=repository_head,
        source_hashes=sources,
        model=model,
        optimizer=optimizer,
    )
    temporary = output_dir / (RESUME_NAME + ".tmp")
    save_checkpoint(
        temporary,
        step=step,
        config=config,
        model=model,
        optimizer=optimizer,
        metadata=metadata,
    )
    os.replace(temporary, output_dir / RESUME_NAME)
    if step % full_checkpoint_cadence == 0 or step == definition.fixed_updates:
        archive = output_dir / "checkpoints" / f"checkpoint_{step:08d}.pt"
        archive.parent.mkdir(exist_ok=True)
        if archive.exists():
            raise FileExistsError(f"archival checkpoint already exists: {archive}")
        save_checkpoint(
            archive,
            step=step,
            config=config,
            model=model,
            optimizer=optimizer,
            metadata=metadata,
        )


def _new_manifest(
    *,
    definition: RunDefinition,
    config: Any,
    dataset: DatasetBundle,
    spec_path: Path,
    lock_path: Path,
    repository_head: str,
    static_hashes: Mapping[str, str],
) -> dict[str, object]:
    return {
        "kind": "philosophia-level0-run-manifest",
        "run_id": definition.run_id,
        "control": definition.control,
        "master_seed": definition.master_seed,
        "fixed_updates": definition.fixed_updates,
        "config_hash": config_hash(config),
        "split_hash": dataset.split_hash,
        "universe_hash": dataset.universe_hash,
        "scientific_spec_sha256": sha256_file(spec_path),
        "prereg_lock_sha256": sha256_file(lock_path),
        "repository_head": repository_head,
        "torch_num_threads": torch.get_num_threads(),
        "torch_num_interop_threads": torch.get_num_interop_threads(),
        "source_hashes": dict(static_hashes),
        "scientific_outcome": True,
        "verdict_derived": False,
    }


def run_locked_outcome(
    *,
    run_id: str,
    output_root: Path,
    spec_path: Path,
    lock_path: Path,
    resume: bool,
) -> Path:
    configure_canonical_torch_runtime()
    root = Path(__file__).resolve().parents[3]
    repository_head = _repository_head(root)
    canonical_spec = root / "experiments/level_0_grokking/SCIENTIFIC_SPEC.json"
    if spec_path.resolve() != canonical_spec.resolve():
        raise ScientificSpecError("spec path differs from canonical scientific spec")
    spec = load_spec(spec_path, require_accepted=True)
    expected_output_root = (root / str(spec["output_root"])).resolve()
    if output_root.resolve() != expected_output_root:
        raise ScientificSpecError("outcome root differs from scientific spec")
    definitions = run_definitions(spec)
    if run_id not in definitions:
        raise ScientificSpecError(f"unknown run id: {run_id}")
    definition = definitions[run_id]
    config = run_config(definition)
    lock = load_lock(
        lock_path,
        spec_path=spec_path,
    )
    _verify_locked_sources(lock, root=root)
    _verify_repository_binding(root=root, lock_path=lock_path, lock=lock)
    raw_run_lock = lock["runs"][run_id]
    if raw_run_lock["split_hash"] != definition.split_hash:
        raise ScientificSpecError("lock/spec split hash mismatch")
    max_artifact_bytes = int(raw_run_lock["max_artifact_bytes"])
    max_total_artifact_bytes = int(lock["max_total_artifact_bytes"])
    label_seed = int(spec["controls"]["random_label"]["label_seed"])
    dataset = _dataset_for_run(definition, label_seed=label_seed)

    if torch.get_default_dtype() != torch.float32:
        raise RuntimeError("locked outcome requires default float32")
    torch.use_deterministic_algorithms(True)
    output_dir = output_root / run_id
    complete_path = output_dir / COMPLETE_NAME
    if complete_path.exists():
        raise FileExistsError(f"run {run_id} is already complete")
    if (output_dir / RESOURCE_STOP_NAME).exists():
        raise FileExistsError(f"run {run_id} has a terminal resource stop")
    if output_dir.exists() and not resume:
        raise FileExistsError("output directory exists; use explicit --resume")
    if not output_dir.exists() and resume:
        raise FileNotFoundError("cannot resume a missing output directory")

    static_hashes = _static_source_hashes(
        root=root,
        spec_path=spec_path,
        lock_path=lock_path,
    )
    model = GrokkingTransformer(config.model, init_seed=config.init_seed)
    optimizer = make_optimizer(model, config)
    metrics_path = output_dir / METRICS_NAME
    manifest_path = output_dir / MANIFEST_NAME
    initial_step = 0
    initial_elapsed = 0.0

    if not resume:
        output_dir.mkdir(parents=True)
        (output_dir / "snapshots").mkdir()
        manifest = _new_manifest(
            definition=definition,
            config=config,
            dataset=dataset,
            spec_path=spec_path,
            lock_path=lock_path,
            repository_head=repository_head,
            static_hashes=static_hashes,
        )
        _atomic_json(manifest_path, manifest)
        metrics_path.touch(exist_ok=False)
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        run_repository_head = str(manifest.get("repository_head", ""))
        if len(run_repository_head) != 40:
            raise ScientificSpecError("run manifest has no repository head")
        if subprocess.run(
            ["git", "merge-base", "--is-ancestor", run_repository_head, "HEAD"],
            cwd=root,
            check=False,
        ).returncode != 0:
            raise ScientificSpecError("run repository head is not an ancestor of HEAD")
        expected_manifest = _new_manifest(
            definition=definition,
            config=config,
            dataset=dataset,
            spec_path=spec_path,
            lock_path=lock_path,
            repository_head=run_repository_head,
            static_hashes=static_hashes,
        )
        if manifest != expected_manifest:
            raise ScientificSpecError("run manifest drift on resume")
        repository_head = run_repository_head
        observations = _read_metrics(metrics_path)
        if not observations:
            raise ScientificSpecError("resume metrics prefix is empty")
        loaded_step, metadata = load_checkpoint(
            output_dir / RESUME_NAME,
            model=model,
            optimizer=optimizer,
            expected_config_hash=definition.config_hash,
            expected_split_hash=definition.split_hash,
        )
        if loaded_step != int(observations[-1]["step"]):
            checkpoint_metrics_hash = metadata.source_hashes.get("metrics_prefix")
            if not isinstance(checkpoint_metrics_hash, str):
                raise ScientificSpecError("checkpoint has no metrics-prefix hash")
            observations = _recover_uncommitted_metric_tail(
                metrics_path=metrics_path,
                checkpoint_step=loaded_step,
                checkpoint_metrics_hash=checkpoint_metrics_hash,
                snapshot_dir=output_dir / "snapshots",
            )
        initial_step = int(observations[-1]["step"])
        initial_elapsed = float(observations[-1]["elapsed_seconds"])
        expected_sources = _checkpoint_sources(
            static_hashes,
            metrics_path=metrics_path,
            manifest_path=manifest_path,
        )
        if loaded_step != initial_step:
            raise ScientificSpecError("checkpoint/metrics step mismatch")
        if metadata.source_hashes != expected_sources:
            raise ScientificSpecError("checkpoint source or metrics-prefix drift")
        if metadata.repository_head != repository_head:
            raise ScientificSpecError("checkpoint repository head drift")
        if initial_step % int(spec["observations"]["full_checkpoint_cadence"]) == 0:
            archive = output_dir / "checkpoints" / f"checkpoint_{initial_step:08d}.pt"
            if not archive.exists():
                archive.parent.mkdir(exist_ok=True)
                shutil.copyfile(output_dir / RESUME_NAME, archive)

    interlock = ExecutionInterlock.from_preregistration(
        lock_path,
        spec_path=spec_path,
        run_id=run_id,
        expected_config_hash=definition.config_hash,
        expected_fixed_steps=definition.fixed_updates,
        consumed_steps=initial_step,
        consumed_seconds=initial_elapsed,
    )

    def persist_observation(step: int) -> None:
        interlock.require_within_wall()
        observation = _observation(
            step=step,
            model=model,
            optimizer=optimizer,
            dataset=dataset,
            interlock=interlock,
        )
        _append_json_line(metrics_path, observation)
        manifest_hash = sha256_file(manifest_path)
        snapshot_path = output_dir / "snapshots" / f"model_{step:08d}.pt"
        if snapshot_path.exists():
            raise FileExistsError(f"model snapshot already exists: {snapshot_path}")
        _save_model_snapshot(
            snapshot_path,
            step=step,
            model=model,
            manifest_hash=manifest_hash,
        )
        _save_resume_checkpoint(
            output_dir=output_dir,
            step=step,
            definition=definition,
            config=config,
            dataset=dataset,
            model=model,
            optimizer=optimizer,
            repository_head=repository_head,
            static_hashes=static_hashes,
            full_checkpoint_cadence=int(
                spec["observations"]["full_checkpoint_cadence"]
            ),
        )
        if _directory_bytes(output_dir) > max_artifact_bytes:
            raise ResourceStop("run exceeded its locked artifact-byte ceiling")
        if _directory_bytes(output_root) > max_total_artifact_bytes:
            raise ResourceStop("battery exceeded its locked artifact-byte ceiling")

    try:
        if not resume:
            persist_observation(0)
        for step in range(initial_step + 1, definition.fixed_updates + 1):
            optimization_step(
                model,
                optimizer,
                dataset.learner,
                interlock=interlock,
            )
            if step % int(spec["observations"]["metric_cadence"]) == 0:
                persist_observation(step)
        if interlock.steps_used != definition.fixed_updates:
            raise RuntimeError("run ended before its fixed update budget")
    except ExecutionNotAuthorized as error:
        if "wall-clock cap" not in str(error):
            raise
        stop = {
            "kind": "philosophia-level0-resource-stop",
            "run_id": run_id,
            "step": interlock.steps_used,
            "elapsed_seconds": interlock.elapsed_seconds,
            "reason": str(error),
            "scientific_verdict": None,
        }
        _atomic_json(output_dir / RESOURCE_STOP_NAME, stop)
        raise ResourceStop(str(error)) from error
    except ResourceStop as error:
        stop = {
            "kind": "philosophia-level0-resource-stop",
            "run_id": run_id,
            "step": interlock.steps_used,
            "elapsed_seconds": interlock.elapsed_seconds,
            "reason": str(error),
            "scientific_verdict": None,
        }
        _atomic_json(output_dir / RESOURCE_STOP_NAME, stop)
        raise

    report = {
        "kind": "philosophia-level0-complete-run",
        "run_id": run_id,
        "control": definition.control,
        "fixed_updates": definition.fixed_updates,
        "steps_used": interlock.steps_used,
        "elapsed_seconds": interlock.elapsed_seconds,
        "config_hash": definition.config_hash,
        "split_hash": definition.split_hash,
        "metrics_sha256": sha256_file(metrics_path),
        "manifest_sha256": sha256_file(manifest_path),
        "final_model_state_hash": model_state_hash(model),
        "final_optimizer_state_hash": optimizer_state_hash(optimizer),
        "prereg_lock_sha256": sha256_file(lock_path),
        "torch_num_threads": torch.get_num_threads(),
        "torch_num_interop_threads": torch.get_num_interop_threads(),
        "scientific_verdict": None,
    }
    _atomic_json(complete_path, report)
    return complete_path
