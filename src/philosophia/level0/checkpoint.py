from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import platform
from pathlib import Path
from typing import Any, Mapping

import torch

from .config import PINNED_TORCH_VERSION, RunConfig, canonical_json, config_hash
from .model import GrokkingTransformer


SCHEMA_VERSION = 2


class CheckpointMismatch(RuntimeError):
    pass


@dataclass(frozen=True)
class CheckpointMetadata:
    config_hash: str
    split_hash: str
    model_state_hash: str
    optimizer_state_hash: str
    repository_head: str
    source_hashes: dict[str, str]
    python_version: str
    torch_version: str
    device: str
    dtype: str
    init_scales: tuple[dict[str, object], ...]


def _update_tree_hash(digest: Any, value: object) -> None:
    digest.update(type(value).__name__.encode("ascii"))
    if isinstance(value, torch.Tensor):
        tensor = value.detach().cpu().contiguous()
        digest.update(str(tensor.dtype).encode("ascii"))
        digest.update(str(tuple(tensor.shape)).encode("ascii"))
        digest.update(tensor.numpy().tobytes())
    elif isinstance(value, Mapping):
        for key in sorted(value, key=repr):
            _update_tree_hash(digest, key)
            _update_tree_hash(digest, value[key])
    elif isinstance(value, (list, tuple)):
        for item in value:
            _update_tree_hash(digest, item)
    elif value is None or isinstance(value, (bool, int, float, str)):
        digest.update(repr(value).encode("ascii"))
    else:
        raise TypeError(f"unsupported checkpoint hash value: {type(value)!r}")


def state_tree_hash(value: object) -> str:
    digest = hashlib.sha256()
    _update_tree_hash(digest, value)
    return digest.hexdigest()


def model_state_hash(model: GrokkingTransformer) -> str:
    return state_tree_hash(model.state_dict())


def optimizer_state_hash(optimizer: torch.optim.Optimizer) -> str:
    return state_tree_hash(optimizer.state_dict())


def build_metadata(
    *,
    config: RunConfig,
    split_hash: str,
    repository_head: str,
    source_hashes: Mapping[str, str],
    model: GrokkingTransformer,
    optimizer: torch.optim.Optimizer,
) -> CheckpointMetadata:
    first_parameter = next(model.parameters())
    return CheckpointMetadata(
        config_hash=config_hash(config),
        split_hash=split_hash,
        model_state_hash=model_state_hash(model),
        optimizer_state_hash=optimizer_state_hash(optimizer),
        repository_head=repository_head,
        source_hashes=dict(sorted(source_hashes.items())),
        python_version=platform.python_version(),
        torch_version=str(torch.__version__),
        device=str(first_parameter.device),
        dtype=str(first_parameter.dtype),
        init_scales=tuple(asdict(record) for record in model.init_scale_observables()),
    )


def save_checkpoint(
    path: Path,
    *,
    step: int,
    config: RunConfig,
    model: GrokkingTransformer,
    optimizer: torch.optim.Optimizer,
    metadata: CheckpointMetadata,
) -> None:
    if metadata.config_hash != config_hash(config):
        raise CheckpointMismatch("metadata/config hash mismatch before save")
    if metadata.model_state_hash != model_state_hash(model):
        raise CheckpointMismatch("metadata/model state hash mismatch before save")
    if metadata.optimizer_state_hash != optimizer_state_hash(optimizer):
        raise CheckpointMismatch("metadata/optimizer state hash mismatch before save")
    payload = {
        "schema_version": SCHEMA_VERSION,
        "step": step,
        "config_json": canonical_json(config),
        "metadata": asdict(metadata),
        "model_state": model.state_dict(),
        "optimizer_state": optimizer.state_dict(),
    }
    torch.save(payload, path)


def _enforce_canonical_environment(
    raw_metadata: Mapping[str, object],
    model: GrokkingTransformer,
) -> None:
    recorded_torch = str(raw_metadata["torch_version"])
    current_base = torch.__version__.split("+", maxsplit=1)[0]
    recorded_base = recorded_torch.split("+", maxsplit=1)[0]
    if current_base != PINNED_TORCH_VERSION or recorded_base != PINNED_TORCH_VERSION:
        raise CheckpointMismatch("checkpoint requires pinned PyTorch 2.9.1")
    parameter = next(model.parameters())
    if raw_metadata["device"] != "cpu" or parameter.device.type != "cpu":
        raise CheckpointMismatch("canonical checkpoint load requires CPU")
    if raw_metadata["dtype"] != "torch.float32" or parameter.dtype != torch.float32:
        raise CheckpointMismatch("canonical checkpoint load requires float32")


def load_checkpoint(
    path: Path,
    *,
    model: GrokkingTransformer,
    optimizer: torch.optim.Optimizer,
    expected_config_hash: str,
    expected_split_hash: str,
) -> tuple[int, CheckpointMetadata]:
    payload = torch.load(path, map_location="cpu", weights_only=True)
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise CheckpointMismatch("checkpoint schema mismatch")
    raw_metadata = payload["metadata"]
    stored_config_hash = hashlib.sha256(payload["config_json"].encode("ascii")).hexdigest()
    if raw_metadata["config_hash"] != stored_config_hash:
        raise CheckpointMismatch("checkpoint config payload is internally inconsistent")
    if raw_metadata["config_hash"] != expected_config_hash:
        raise CheckpointMismatch("checkpoint config hash mismatch")
    if raw_metadata["split_hash"] != expected_split_hash:
        raise CheckpointMismatch("checkpoint split hash mismatch")
    if raw_metadata["model_state_hash"] != state_tree_hash(payload["model_state"]):
        raise CheckpointMismatch("checkpoint model state integrity failure")
    if raw_metadata["optimizer_state_hash"] != state_tree_hash(
        payload["optimizer_state"]
    ):
        raise CheckpointMismatch("checkpoint optimizer state integrity failure")
    _enforce_canonical_environment(raw_metadata, model)

    model.load_state_dict(payload["model_state"], strict=True)
    optimizer.load_state_dict(payload["optimizer_state"])
    metadata = CheckpointMetadata(
        config_hash=raw_metadata["config_hash"],
        split_hash=raw_metadata["split_hash"],
        model_state_hash=raw_metadata["model_state_hash"],
        optimizer_state_hash=raw_metadata["optimizer_state_hash"],
        repository_head=raw_metadata["repository_head"],
        source_hashes=raw_metadata["source_hashes"],
        python_version=raw_metadata["python_version"],
        torch_version=raw_metadata["torch_version"],
        device=raw_metadata["device"],
        dtype=raw_metadata["dtype"],
        init_scales=tuple(raw_metadata["init_scales"]),
    )
    return int(payload["step"]), metadata
