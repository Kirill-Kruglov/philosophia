from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

from .config import (
    RunConfig,
    artifact_fidelity_arm,
    config_hash,
    paper_mainline_arm,
)


SPEC_KIND = "philosophia-level0-scientific-spec"
LOCK_KIND = "philosophia-level0-preregistration"
LOCK_SCHEMA_VERSION = 2
REQUIRED_RUN_IDS = (
    "A-0",
    "A-1",
    "A-2",
    "A-3",
    "A-4",
    "B-1",
    "B-2",
    "B-3",
    "R-0",
)


class ScientificSpecError(RuntimeError):
    pass


@dataclass(frozen=True)
class RunDefinition:
    run_id: str
    control: str
    master_seed: int
    fixed_updates: int
    config_hash: str
    split_hash: str
    label_hash: str | None = None

    @property
    def arm(self) -> str:
        return self.run_id[0]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_json_bytes(value: object) -> bytes:
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
        + "\n"
    ).encode("ascii")


def load_json_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ScientificSpecError(f"cannot read JSON object: {path}") from error
    if not isinstance(value, dict):
        raise ScientificSpecError(f"expected JSON object: {path}")
    return value


def run_config(definition: RunDefinition) -> RunConfig:
    if definition.arm in ("A", "R"):
        arm = paper_mainline_arm()
    elif definition.arm == "B":
        arm = artifact_fidelity_arm((1, 2, 3))
    else:
        raise ScientificSpecError(f"unknown run arm: {definition.run_id}")
    config = RunConfig(arm=arm, master_seed=definition.master_seed)
    if config_hash(config) != definition.config_hash:
        raise ScientificSpecError(f"config hash drift for {definition.run_id}")
    if config.arm.fixed_epochs != definition.fixed_updates:
        raise ScientificSpecError(f"fixed budget drift for {definition.run_id}")
    return config


def _parse_runs(raw_runs: object) -> dict[str, RunDefinition]:
    if not isinstance(raw_runs, list):
        raise ScientificSpecError("spec runs must be a list")
    definitions: dict[str, RunDefinition] = {}
    for raw in raw_runs:
        if not isinstance(raw, Mapping):
            raise ScientificSpecError("each run definition must be an object")
        definition = RunDefinition(
            run_id=str(raw["run_id"]),
            control=str(raw["control"]),
            master_seed=int(raw["master_seed"]),
            fixed_updates=int(raw["fixed_updates"]),
            config_hash=str(raw["config_hash"]),
            split_hash=str(raw["split_hash"]),
            label_hash=(str(raw["label_hash"]) if "label_hash" in raw else None),
        )
        if definition.run_id in definitions:
            raise ScientificSpecError(f"duplicate run id: {definition.run_id}")
        if definition.control not in ("real-label", "random-label"):
            raise ScientificSpecError(f"unknown control: {definition.control}")
        if (definition.run_id == "R-0") != (definition.control == "random-label"):
            raise ScientificSpecError("R-0 must be the sole random-label control")
        if definition.control == "random-label" and definition.label_hash is None:
            raise ScientificSpecError("random-label run requires a label hash")
        run_config(definition)
        definitions[definition.run_id] = definition
    if tuple(definitions) != REQUIRED_RUN_IDS:
        raise ScientificSpecError("run order or membership differs from locked battery")
    return definitions


def validate_spec(raw: Mapping[str, Any], *, require_accepted: bool) -> None:
    if raw.get("schema_version") != 1 or raw.get("kind") != SPEC_KIND:
        raise ScientificSpecError("scientific spec identity mismatch")
    accepted_status = "accepted-by-kirill-before-outcome"
    allowed_statuses = {"draft-before-review-and-signature", accepted_status}
    if raw.get("status") not in allowed_statuses:
        raise ScientificSpecError("scientific spec status is invalid")
    if require_accepted and raw.get("status") != accepted_status:
        raise ScientificSpecError("scientific spec is not accepted by Kirill")
    if raw.get("environment") != {
        "backend": "cpu",
        "default_dtype": "torch.float32",
        "deterministic_algorithms": True,
        "python": "3.12.3",
        "torch": "2.9.1+cpu",
    }:
        raise ScientificSpecError("canonical environment contract drift")
    resources = raw.get("resource_wall")
    if not isinstance(resources, Mapping) or {
        "arm_a_max_seconds_per_run": resources.get("arm_a_max_seconds_per_run"),
        "arm_b_max_seconds_per_run": resources.get("arm_b_max_seconds_per_run"),
        "random_label_max_seconds": resources.get("random_label_max_seconds"),
        "max_total_artifact_bytes": resources.get("max_total_artifact_bytes"),
    } != {
        "arm_a_max_seconds_per_run": 21600,
        "arm_b_max_seconds_per_run": 64800,
        "random_label_max_seconds": 21600,
        "max_total_artifact_bytes": 26843545600,
    }:
        raise ScientificSpecError("resource wall contract drift")
    controls = raw.get("controls")
    if not isinstance(controls, Mapping):
        raise ScientificSpecError("control contract is missing")
    random_label = controls.get("random_label")
    if (
        controls.get("all_real_label_runs_must_fit") is not True
        or not isinstance(random_label, Mapping)
        or random_label.get("master_seed") != 0
        or random_label.get("label_seed") != 20000
    ):
        raise ScientificSpecError("control contract drift")
    predicates = raw.get("predicates")
    observations = raw.get("observations")
    decision = raw.get("decision")
    if not isinstance(predicates, Mapping) or not isinstance(observations, Mapping):
        raise ScientificSpecError("missing predicate or observation contract")
    if not isinstance(decision, Mapping):
        raise ScientificSpecError("missing decision contract")
    expected = {
        "fit": (0.99, 1000),
        "generalize": (0.95, 1000),
    }
    for name, (minimum, window) in expected.items():
        raw_predicate = predicates.get(name)
        if not isinstance(raw_predicate, Mapping):
            raise ScientificSpecError(f"missing {name} predicate")
        if raw_predicate.get("minimum") != minimum:
            raise ScientificSpecError(f"{name} threshold drift")
        if raw_predicate.get("persistence_window") != window:
            raise ScientificSpecError(f"{name} persistence drift")
    if predicates.get("delayed", {}).get("delta_min") != 2000:
        raise ScientificSpecError("delay threshold drift")
    if observations.get("metric_cadence") != 100:
        raise ScientificSpecError("metric cadence drift")
    if observations.get("model_snapshot_cadence") != 100:
        raise ScientificSpecError("snapshot cadence drift")
    if observations.get("full_checkpoint_cadence") != 1000:
        raise ScientificSpecError("checkpoint cadence drift")
    if decision.get("arm_a_quorum") != 4 or decision.get("arm_a_total") != 5:
        raise ScientificSpecError("primary quorum drift")
    if raw.get("output_root") != "experiments/level_0_grokking/outcomes":
        raise ScientificSpecError("canonical outcome root drift")
    _parse_runs(raw.get("runs"))


def load_spec(path: Path, *, require_accepted: bool = False) -> dict[str, Any]:
    raw = load_json_object(path)
    validate_spec(raw, require_accepted=require_accepted)
    return raw


def run_definitions(raw: Mapping[str, Any]) -> dict[str, RunDefinition]:
    return _parse_runs(raw.get("runs"))


def validate_lock(
    raw: Mapping[str, Any],
    *,
    spec_path: Path,
) -> None:
    if raw.get("schema_version") != LOCK_SCHEMA_VERSION:
        raise ScientificSpecError("lock schema mismatch")
    required = {
        "kind": LOCK_KIND,
        "status": "locked",
        "authorized_by": "Kirill",
        "authorization_statement": "I_ACCEPT_LEVEL0_SCIENTIFIC_SPEC",
        "scientific_spec_sha256": sha256_file(spec_path),
    }
    for key, expected in required.items():
        if raw.get(key) != expected:
            raise ScientificSpecError(f"lock field {key!r} mismatch")
    source_commit = raw.get("source_commit")
    if (
        not isinstance(source_commit, str)
        or len(source_commit) != 40
        or any(character not in "0123456789abcdef" for character in source_commit)
    ):
        raise ScientificSpecError("lock source_commit is invalid")
    spec = load_spec(spec_path, require_accepted=True)
    definitions = run_definitions(spec)
    run_entries = raw.get("runs")
    if not isinstance(run_entries, Mapping) or tuple(run_entries) != REQUIRED_RUN_IDS:
        raise ScientificSpecError("lock run membership mismatch")
    for run_id, definition in definitions.items():
        entry = run_entries[run_id]
        if not isinstance(entry, Mapping):
            raise ScientificSpecError(f"lock run entry is invalid: {run_id}")
        expected = {
            "config_hash": definition.config_hash,
            "split_hash": definition.split_hash,
            "control": definition.control,
            "fixed_updates": definition.fixed_updates,
            "max_seconds": 64800 if run_id.startswith("B-") else 21600,
            "max_artifact_bytes": (
                4294967296 if run_id.startswith("B-") else 2147483648
            ),
        }
        if dict(entry) != expected:
            raise ScientificSpecError(f"lock run contract mismatch: {run_id}")
    if raw.get("max_total_artifact_bytes") != int(
        spec["resource_wall"]["max_total_artifact_bytes"]
    ):
        raise ScientificSpecError("lock total artifact ceiling mismatch")
    source_hashes = raw.get("source_hashes")
    if not isinstance(source_hashes, Mapping) or not source_hashes:
        raise ScientificSpecError("lock source hashes are missing")
    if any(
        not isinstance(path, str)
        or not isinstance(digest, str)
        or len(digest) != 64
        for path, digest in source_hashes.items()
    ):
        raise ScientificSpecError("lock source hash map is invalid")


def load_lock(
    path: Path,
    *,
    spec_path: Path,
) -> dict[str, Any]:
    if path.name != "PREREG.lock" or not path.is_file():
        raise ScientificSpecError("a real PREREG.lock file is required")
    raw_bytes = path.read_bytes()
    raw = load_json_object(path)
    if raw_bytes != canonical_json_bytes(raw):
        raise ScientificSpecError("PREREG.lock is not canonical JSON")
    validate_lock(raw, spec_path=spec_path)
    return raw
