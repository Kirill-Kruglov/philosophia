from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import platform
from pathlib import Path
from typing import Mapping

import torch

from .config import RunConfig, canonical_json, config_hash
from .model import GrokkingTransformer


SCHEMA_VERSION = 1


class CheckpointMismatch(RuntimeError):
    pass


@dataclass(frozen=True)
class CheckpointMetadata:
    config_hash: str
    split_hash: str
    repository_head: str
    source_hashes: dict[str, str]
    python_version: str
    torch_version: str
    device: str
    dtype: str
    init_scales: tuple[dict[str, object], ...]


def build_metadata(
    *,
    config: RunConfig,
    split_hash: str,
    repository_head: str,
    source_hashes: Mapping[str, str],
    model: GrokkingTransformer,
) -> CheckpointMetadata:
    first_parameter = next(model.parameters())
    return CheckpointMetadata(
        config_hash=config_hash(config),
        split_hash=split_hash,
        repository_head=repository_head,
        source_hashes=dict(sorted(source_hashes.items())),
        python_version=platform.python_version(),
        torch_version=torch.__version__,
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
    payload = {
        "schema_version": SCHEMA_VERSION,
        "step": step,
        "config_json": canonical_json(config),
        "metadata": asdict(metadata),
        "model_state": model.state_dict(),
        "optimizer_state": optimizer.state_dict(),
    }
    torch.save(payload, path)


def load_checkpoint(
    path: Path,
    *,
    model: GrokkingTransformer,
    optimizer: torch.optim.Optimizer,
    expected_config_hash: str,
    expected_split_hash: str,
) -> tuple[int, CheckpointMetadata]:
    payload = torch.load(path, map_location="cpu", weights_only=False)
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

    model.load_state_dict(payload["model_state"], strict=True)
    optimizer.load_state_dict(payload["optimizer_state"])
    metadata = CheckpointMetadata(
        config_hash=raw_metadata["config_hash"],
        split_hash=raw_metadata["split_hash"],
        repository_head=raw_metadata["repository_head"],
        source_hashes=raw_metadata["source_hashes"],
        python_version=raw_metadata["python_version"],
        torch_version=raw_metadata["torch_version"],
        device=raw_metadata["device"],
        dtype=raw_metadata["dtype"],
        init_scales=tuple(raw_metadata["init_scales"]),
    )
    return int(payload["step"]), metadata


def model_state_hash(model: GrokkingTransformer) -> str:
    digest = hashlib.sha256()
    for name, tensor in sorted(model.state_dict().items()):
        value = tensor.detach().cpu().contiguous()
        digest.update(name.encode("ascii"))
        digest.update(str(value.dtype).encode("ascii"))
        digest.update(str(tuple(value.shape)).encode("ascii"))
        digest.update(value.numpy().tobytes())
    return digest.hexdigest()
