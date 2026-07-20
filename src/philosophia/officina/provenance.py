from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Mapping

from .canonical import (
    atomic_create,
    atomic_replace,
    canonical_json,
    load_canonical_json,
    sha256_bytes,
)
from .interlock import TestOnlyCapability, require_test_only
from .quarantine import ArtifactLabel, PathPolicy, QuarantineViolation, Surface


SCHEMA = "philosophia.officina.artifact-provenance.v2"
REGISTRY_HEAD_SCHEMA = "philosophia.officina.provenance-registry-head.v1"
GENESIS = "0" * 64


@dataclass(frozen=True)
class ArtifactView:
    """Read-only observation; it conveys no write or promotion authority."""

    path: Path
    payload: bytes = field(repr=False)
    label: ArtifactLabel
    provenance_sha256: str


def _registry_head(events: list[dict[str, object]]) -> bytes:
    return canonical_json(
        {
            "entry_count": len(events),
            "head_sha256": str(events[-1]["event_sha256"]) if events else GENESIS,
            "schema": REGISTRY_HEAD_SCHEMA,
            "scientific_outcome": False,
        }
    )


class ProvenanceRegistry:
    """Externally headed append-only commitment to exact provenance records."""

    def __init__(self, directory: Path) -> None:
        self.directory = directory
        self.head_path = directory / "HEAD.json"

    def initialize(self) -> None:
        self.directory.mkdir(parents=True, exist_ok=True)
        atomic_create(self.head_path, _registry_head([]))

    def entries(self) -> list[dict[str, object]]:
        if not self.head_path.exists():
            raise QuarantineViolation("provenance registry is not initialized")
        events: list[dict[str, object]] = []
        event_paths = sorted(
            self.directory.glob("[0-9][0-9][0-9][0-9][0-9][0-9].json")
        )
        expected_names = {"HEAD.json", *(path.name for path in event_paths)}
        actual_names = {
            path.name for path in self.directory.iterdir() if path.is_file()
        }
        if actual_names != expected_names:
            raise QuarantineViolation("provenance registry files differ")
        for index, path in enumerate(event_paths):
            value = load_canonical_json(path)
            expected = {
                "event_sha256", "previous_sha256", "record", "sequence"
            }
            if not isinstance(value, dict) or set(value) != expected:
                raise QuarantineViolation("provenance registry event fields differ")
            if type(value["sequence"]) is not int or value["sequence"] != index:
                raise QuarantineViolation("provenance registry sequence mismatch")
            previous = GENESIS if not events else str(events[-1]["event_sha256"])
            if value["previous_sha256"] != previous:
                raise QuarantineViolation("provenance registry chain mismatch")
            core = {key: item for key, item in value.items() if key != "event_sha256"}
            if value["event_sha256"] != sha256_bytes(canonical_json(core)):
                raise QuarantineViolation("provenance registry event hash mismatch")
            if not isinstance(value["record"], dict):
                raise QuarantineViolation("provenance registry record must be an object")
            events.append(value)
        if canonical_json(load_canonical_json(self.head_path)) != canonical_json(
            json.loads(_registry_head(events))
        ):
            raise QuarantineViolation("provenance registry head mismatch")
        return events

    def _append(self, record: Mapping[str, object]) -> None:
        events = self.entries()
        path_value = record.get("path")
        if any(event["record"].get("path") == path_value for event in events):
            raise QuarantineViolation("artifact path already has provenance")
        sequence = len(events)
        core = {
            "previous_sha256": GENESIS if not events else events[-1]["event_sha256"],
            "record": dict(record),
            "sequence": sequence,
        }
        event = {**core, "event_sha256": sha256_bytes(canonical_json(core))}
        atomic_create(self.directory / f"{sequence:06d}.json", canonical_json(event))
        atomic_replace(self.head_path, _registry_head([*events, event]))

    def require_exact(self, record: Mapping[str, object]) -> None:
        matches = [
            event["record"]
            for event in self.entries()
            if event["record"].get("path") == record.get("path")
        ]
        if len(matches) != 1 or canonical_json(matches[0]) != canonical_json(dict(record)):
            raise QuarantineViolation("artifact provenance differs from registry")


class ArtifactStore:
    """Mediates bytes and verifies exact recursive ancestry against a registry."""

    def __init__(self, policy: PathPolicy, registry: ProvenanceRegistry) -> None:
        self.policy = policy
        self.registry = registry

    @staticmethod
    def metadata_path(path: Path) -> Path:
        return path.with_name(f"{path.name}.provenance.json")

    def read(self, path: Path, *, surface: Surface) -> ArtifactView:
        return self._read(path, surface=surface, visited=frozenset())

    def _read(
        self, path: Path, *, surface: Surface, visited: frozenset[str]
    ) -> ArtifactView:
        resolved, storage_label = self.policy.authorize(path, surface=surface)
        payload = resolved.read_bytes()
        if storage_label.certified:
            descriptor = canonical_json(
                {
                    "content_sha256": sha256_bytes(payload),
                    "path": str(resolved),
                    "sources": list(storage_label.sources),
                }
            )
            return ArtifactView(
                path=resolved,
                payload=payload,
                label=storage_label,
                provenance_sha256=sha256_bytes(descriptor),
            )

        try:
            record = load_canonical_json(self.metadata_path(resolved))
        except FileNotFoundError as error:
            raise QuarantineViolation("native artifact provenance is missing") from error
        expected = {
            "content_sha256", "parents", "path", "promotable",
            "provenance_sha256", "purpose", "schema", "sources",
        }
        if not isinstance(record, dict) or set(record) != expected:
            raise QuarantineViolation("native artifact provenance fields differ")
        core = {key: value for key, value in record.items() if key != "provenance_sha256"}
        if record["schema"] != SCHEMA:
            raise QuarantineViolation("native artifact provenance schema mismatch")
        if record["path"] != str(resolved):
            raise QuarantineViolation("native artifact provenance path mismatch")
        if record["content_sha256"] != sha256_bytes(payload):
            raise QuarantineViolation("native artifact content hash mismatch")
        if record["provenance_sha256"] != sha256_bytes(canonical_json(core)):
            raise QuarantineViolation("native artifact provenance hash mismatch")
        sources = record["sources"]
        parents = record["parents"]
        if (
            not isinstance(sources, list)
            or not sources
            or not all(isinstance(item, str) and item for item in sources)
            or not isinstance(parents, list)
            or type(record["promotable"]) is not bool
            or not isinstance(record["purpose"], str)
            or not record["purpose"]
        ):
            raise QuarantineViolation("native artifact provenance values are malformed")
        if record["promotable"] is not False:
            raise QuarantineViolation("WP-1/WP-2 have no promotion authority")
        provenance_hash = str(record["provenance_sha256"])
        if provenance_hash in visited:
            raise QuarantineViolation("provenance ancestry contains a cycle")
        self.registry.require_exact(record)

        parent_sources: set[str] = set()
        for parent in parents:
            if not isinstance(parent, dict) or set(parent) != {
                "path", "provenance_sha256"
            }:
                raise QuarantineViolation("parent provenance fields differ")
            if not isinstance(parent["path"], str) or not isinstance(
                parent["provenance_sha256"], str
            ):
                raise QuarantineViolation("parent provenance values are malformed")
            parent_view = self._read(
                Path(parent["path"]),
                surface=Surface.T,
                visited=visited | {provenance_hash},
            )
            if parent_view.provenance_sha256 != parent["provenance_sha256"]:
                raise QuarantineViolation("parent provenance identity mismatch")
            parent_sources.update(parent_view.label.sources)

        expected_sources = {"test-only-native"} if not parents else parent_sources
        if set(sources) != expected_sources:
            raise QuarantineViolation("artifact source union differs from its parents")
        label = ArtifactLabel(sources=tuple(sorted(expected_sources)), certified=True)
        label.require_promotable(surface)
        return ArtifactView(
            path=resolved,
            payload=payload,
            label=label,
            provenance_sha256=provenance_hash,
        )

    def _write(
        self,
        *,
        path: Path,
        payload: bytes,
        purpose: str,
        parents: tuple[ArtifactView, ...],
    ) -> ArtifactView:
        if not purpose:
            raise ValueError("artifact purpose must be named")
        resolved, _ = self.policy.authorize(path, surface=Surface.T, write=True)
        sources = {"test-only-native"} if not parents else {
            source for parent in parents for source in parent.label.sources
        }
        core = {
            "content_sha256": sha256_bytes(payload),
            "parents": [
                {"path": str(parent.path), "provenance_sha256": parent.provenance_sha256}
                for parent in parents
            ],
            "path": str(resolved),
            "promotable": False,
            "purpose": purpose,
            "schema": SCHEMA,
            "sources": sorted(sources),
        }
        record = {**core, "provenance_sha256": sha256_bytes(canonical_json(core))}
        atomic_create(resolved, payload)
        atomic_create(self.metadata_path(resolved), canonical_json(record))
        self.registry._append(record)  # noqa: SLF001 - store owns registry issuance
        return self.read(resolved, surface=Surface.T)

    def write_test_only(
        self,
        *,
        path: Path,
        payload: bytes,
        purpose: str,
        capability: TestOnlyCapability,
    ) -> ArtifactView:
        require_test_only(capability)
        return self._write(path=path, payload=payload, purpose=purpose, parents=())

    def write_derived(
        self,
        *,
        path: Path,
        payload: bytes,
        purpose: str,
        parent_paths: tuple[Path, ...],
    ) -> ArtifactView:
        if not parent_paths:
            raise ValueError("derived provenance requires at least one parent")
        parents = tuple(self.read(parent, surface=Surface.T) for parent in parent_paths)
        return self._write(
            path=path, payload=payload, purpose=purpose, parents=parents
        )

    def admit(self, path: Path, *, surface: Surface) -> ArtifactView:
        if surface not in {Surface.Q, Surface.C}:
            raise ValueError("admission is defined only for Q/C")
        return self.read(path, surface=surface)
