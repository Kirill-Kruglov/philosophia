from __future__ import annotations

import argparse
from pathlib import Path
import subprocess

from philosophia.level0.scientific_spec import (
    REQUIRED_RUN_IDS,
    canonical_json_bytes,
    load_spec,
    run_definitions,
    sha256_file,
)


SOURCE_PATHS = (
    "experiments/level_0_grokking/SCIENTIFIC_SPEC.json",
    "experiments/level_0_grokking/ANCHOR_CLAIMS.md",
    "src/philosophia/level0/config.py",
    "src/philosophia/level0/data.py",
    "src/philosophia/level0/model.py",
    "src/philosophia/level0/train.py",
    "src/philosophia/level0/metrics.py",
    "src/philosophia/level0/fourier.py",
    "src/philosophia/level0/checkpoint.py",
    "src/philosophia/level0/interlock.py",
    "src/philosophia/level0/scientific_spec.py",
    "src/philosophia/level0/outcome.py",
    "src/philosophia/level0/outcome_evaluator.py",
    "src/philosophia/level0/decision_verifier.py",
    "scripts/level0_run_outcome.py",
    "scripts/level0_evaluate_battery.py",
    "scripts/level0_verify_decision.py",
    "scripts/verify_all.py",
    "scripts/level0_create_lock.py",
)


def _git_output(root: Path, *arguments: str) -> str:
    result = subprocess.run(
        ["git", *arguments],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def create_lock(*, root: Path, spec_path: Path, output_path: Path) -> Path:
    canonical_spec = root / "experiments/level_0_grokking/SCIENTIFIC_SPEC.json"
    canonical_lock = root / "experiments/level_0_grokking/PREREG.lock"
    if spec_path.resolve() != canonical_spec.resolve():
        raise ValueError("spec path must be the canonical SCIENTIFIC_SPEC.json")
    if output_path.resolve() != canonical_lock.resolve():
        raise ValueError("lock output must be the canonical PREREG.lock")
    if output_path.exists():
        raise FileExistsError("PREREG.lock already exists")
    spec = load_spec(spec_path, require_accepted=True)
    definitions = run_definitions(spec)
    source_commit = _git_output(root, "rev-parse", "HEAD")
    for relative in SOURCE_PATHS:
        _git_output(root, "ls-files", "--error-unmatch", relative)
    diff = subprocess.run(
        ["git", "diff", "--quiet", "HEAD", "--", *SOURCE_PATHS],
        cwd=root,
        check=False,
    )
    if diff.returncode != 0:
        raise RuntimeError("locked source paths differ from repository HEAD")

    runs = {}
    for run_id in REQUIRED_RUN_IDS:
        definition = definitions[run_id]
        is_b = run_id.startswith("B-")
        runs[run_id] = {
            "config_hash": definition.config_hash,
            "split_hash": definition.split_hash,
            "control": definition.control,
            "fixed_updates": definition.fixed_updates,
            "max_seconds": 64800 if is_b else 21600,
            "max_artifact_bytes": 4294967296 if is_b else 2147483648,
        }
    payload = {
        "schema_version": 2,
        "kind": "philosophia-level0-preregistration",
        "status": "locked",
        "authorized_by": "Kirill",
        "authorization_statement": "I_ACCEPT_LEVEL0_SCIENTIFIC_SPEC",
        "scientific_spec_sha256": sha256_file(spec_path),
        "source_commit": source_commit,
        "max_total_artifact_bytes": int(
            spec["resource_wall"]["max_total_artifact_bytes"]
        ),
        "source_hashes": {
            relative: sha256_file(root / relative) for relative in SOURCE_PATHS
        },
        "runs": runs,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(canonical_json_bytes(payload))
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--spec", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--authorized-by", required=True)
    parser.add_argument("--confirm", required=True)
    arguments = parser.parse_args()
    if arguments.authorized_by != "Kirill":
        raise SystemExit("--authorized-by must be Kirill")
    if arguments.confirm != "I_ACCEPT_LEVEL0_SCIENTIFIC_SPEC":
        raise SystemExit("exact confirmation statement required")
    path = create_lock(
        root=arguments.root.resolve(),
        spec_path=arguments.spec.resolve(),
        output_path=arguments.output.resolve(),
    )
    print(path)


if __name__ == "__main__":
    main()
