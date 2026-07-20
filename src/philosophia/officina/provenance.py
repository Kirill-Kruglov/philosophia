from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from .canonical import (
    atomic_create,
    canonical_json,
    load_canonical_json,
    sha256_bytes,
    sha256_file,
)
from .interlock import TestOnlyCapability, require_test_only
from .quarantine import ArtifactLabel, PathPolicy, QuarantineViolation, Surface


_TAG_TOKEN = object()
SCHEMA = "philosophia.officina.artifact-provenance.v1"


@dataclass(frozen=True)
class TaggedArtifact:
    path: Path
    payload: bytes = field(repr=False)
    label: ArtifactLabel
    provenance_sha256: str
    _token: object = field(repr=False, compare=False)

    def __post_init__(self) -> None:
        if self._token is not _TAG_TOKEN:
            raise QuarantineViolation("artifact tags must come from ArtifactStore")


class ArtifactStore:
    """Mediates artifact bytes and durable, content-bound provenance records."""

    def __init__(self, policy: PathPolicy) -> None:
        self.policy = policy

    @staticmethod
    def metadata_path(path: Path) -> Path:
        return path.with_name(f"{path.name}.provenance.json")

    def _tag(
        self,
        *,
        path: Path,
        payload: bytes,
        label: ArtifactLabel,
        provenance_sha256: str,
    ) -> TaggedArtifact:
        return TaggedArtifact(
            path=path,
            payload=payload,
            label=label,
            provenance_sha256=provenance_sha256,
            _token=_TAG_TOKEN,
        )

    def read(self, path: Path, *, surface: Surface) -> TaggedArtifact:
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
            return self._tag(
                path=resolved,
                payload=payload,
                label=storage_label,
                provenance_sha256=sha256_bytes(descriptor),
            )

        metadata_path = self.metadata_path(resolved)
        try:
            record = load_canonical_json(metadata_path)
        except FileNotFoundError as error:
            raise QuarantineViolation("native artifact provenance is missing") from error
        expected = {
            "content_sha256", "parent_provenance_sha256", "path", "promotable",
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
        parents = record["parent_provenance_sha256"]
        if (
            not isinstance(sources, list)
            or not sources
            or not all(isinstance(item, str) and item for item in sources)
            or not isinstance(parents, list)
            or not all(isinstance(item, str) and len(item) == 64 for item in parents)
            or type(record["promotable"]) is not bool
            or not isinstance(record["purpose"], str)
            or not record["purpose"]
        ):
            raise QuarantineViolation("native artifact provenance values are malformed")
        if record["promotable"] is not False:
            raise QuarantineViolation(
                "WP-1/WP-2 expose no promotable provenance authority"
            )
        allowed_sources = {"engineering-fixture", "test-only-native"}
        if not set(sources).issubset(allowed_sources):
            raise QuarantineViolation("native artifact provenance source is unauthorized")
        label = ArtifactLabel(
            sources=tuple(sources),
            promotable=record["promotable"],
            certified=True,
        )
        tagged = self._tag(
            path=resolved,
            payload=payload,
            label=label,
            provenance_sha256=str(record["provenance_sha256"]),
        )
        tagged.label.require_promotable(surface)
        return tagged

    def _write(
        self,
        *,
        path: Path,
        payload: bytes,
        purpose: str,
        label: ArtifactLabel,
        parents: Iterable[TaggedArtifact],
    ) -> TaggedArtifact:
        if not purpose:
            raise ValueError("artifact purpose must be named")
        resolved, _ = self.policy.authorize(path, surface=Surface.T, write=True)
        parent_values = tuple(parents)
        for parent in parent_values:
            if not isinstance(parent, TaggedArtifact) or parent._token is not _TAG_TOKEN:
                raise QuarantineViolation("derived artifacts require store-issued parents")
        core = {
            "content_sha256": sha256_bytes(payload),
            "parent_provenance_sha256": [
                parent.provenance_sha256 for parent in parent_values
            ],
            "path": str(resolved),
            "promotable": label.promotable,
            "purpose": purpose,
            "schema": SCHEMA,
            "sources": list(label.sources),
        }
        record = {
            **core,
            "provenance_sha256": sha256_bytes(canonical_json(core)),
        }
        atomic_create(resolved, payload)
        atomic_create(self.metadata_path(resolved), canonical_json(record))
        return self.read(resolved, surface=Surface.T)

    def write_test_only(
        self,
        *,
        path: Path,
        payload: bytes,
        purpose: str,
        capability: TestOnlyCapability,
    ) -> TaggedArtifact:
        require_test_only(capability)
        return self._write(
            path=path,
            payload=payload,
            purpose=purpose,
            label=ArtifactLabel.test_only_native(),
            parents=(),
        )

    def write_derived(
        self,
        *,
        path: Path,
        payload: bytes,
        purpose: str,
        parents: tuple[TaggedArtifact, ...],
    ) -> TaggedArtifact:
        if not parents:
            raise ValueError("derived provenance requires at least one parent")
        return self._write(
            path=path,
            payload=payload,
            purpose=purpose,
            label=ArtifactLabel.derived(*(parent.label for parent in parents)),
            parents=parents,
        )

    def admit(self, path: Path, *, surface: Surface) -> TaggedArtifact:
        if surface not in {Surface.Q, Surface.C}:
            raise ValueError("admission is defined only for Q/C")
        artifact = self.read(path, surface=surface)
        artifact.label.require_promotable(surface)
        return artifact
