#!/usr/bin/env bash
# PHASE1_18 Part B amendment 2/3/4 continuation after OMP=1 gate.
# Order: ck0 OMP=1 re-run (canonical post-patch) → ck1 OMP=1 rep → 3× OMP=16 ck1.
set -euo pipefail

MINIMO_LEARNING=/home/master/llm_projects/minimo/learning
VENV=/home/master/llm_projects/minimo/.venv/bin/python
CKPT_DIR=/home/master/llm_projects/minimo/learning/outputs/2026-08-10/00-14-33
DEV=/home/master/llm_projects/philosophia/successor/dev
OUT="$DEV/phase1_18_part_b"
LOG="$DEV/phase1_18_part_b_run.log"
STAMP="$DEV/phase1_18_stamp_threads.py"
ANALYZE="$DEV/phase1_18_part_b_analyze.py"
MONITOR="$DEV/phase1_18_host_monitor.py"

cd "$MINIMO_LEARNING"
export PYTHONUNBUFFERED=1
export PYTHONDONTWRITEBYTECODE=1

set_threads() {
  local threads="$1"
  export OMP_NUM_THREADS="$threads"
  export MKL_NUM_THREADS="$threads"
  export OPENBLAS_NUM_THREADS="$threads"
  export NUMEXPR_NUM_THREADS="$threads"
  export TORCH_NUM_THREADS="$threads"
  export VECLIB_MAXIMUM_THREADS="$threads"
}

# Preserve pre-patch ck0 under binary-labeled name before canonical overwrite.
archive_prepatch_ck0() {
  local src="$OUT/checkpoint_0_omp1.json"
  if [[ ! -f "$src" ]]; then
    echo "archive_prepatch_ck0: missing $src" | tee -a "$LOG"
    return 1
  fi
  "$VENV" "$STAMP" "$src" 1 - pre_patch_ck0 | tee -a "$LOG"
  local sha
  sha=$(python3 -c "import json; print(json.load(open('$src'))['proofsearch_py_sha256'][:16])")
  local labeled="$OUT/checkpoint_0_omp1_bin_${sha}.json"
  cp -a "$src" "$labeled"
  cp -a "$src" "$OUT/checkpoint_0_omp1_PRE_PATCH.json"
  echo "archive_prepatch_ck0: kept $labeled and checkpoint_0_omp1_PRE_PATCH.json" | tee -a "$LOG"
}

run_one() {
  local threads="$1" ck="$2" tag="$3" role="${4:-default}"
  local results_name="${5:-checkpoint_${ck}_${tag}.json}"
  local hydra_name="${6:-hydra_ck${ck}_${tag}}"
  set_threads "$threads"
  local results="$OUT/$results_name"
  local stem="${results_name%.json}"
  local side="$OUT/${stem}_load.json"
  local jsonl="$OUT/${stem}_load.jsonl"
  local self_tag="$stem"
  echo "===== ${tag} ck${ck} budget 8000 role=${role} $(date -Is) =====" | tee -a "$LOG"
  local t0 t1 mon_pid=""
  rm -f "$jsonl"
  t0=$(date +%s)
  "$VENV" "$MONITOR" snapshot --when start --self-tag "$self_tag" \
    --out "$OUT/${stem}_load_start.json"
  "$VENV" "$MONITOR" sample-loop --jsonl "$jsonl" --self-tag "$self_tag" --interval 60 &
  mon_pid=$!
  nice -n 10 "$VENV" ./proofsearch.py \
    task=eval \
    problemset=kleene \
    agent=mcts-lm \
    agent.max_mcts_nodes=8000 \
    agent.node_type=holophrasm \
    accumulate_library=false \
    +seed=0 \
    +agent_path="$CKPT_DIR/${ck}.pt" \
    job.wandb_project=null \
    +results_path="$results" \
    "hydra.run.dir=$OUT/$hydra_name" \
    2>&1 | tee -a "$LOG"
  t1=$(date +%s)
  if [[ -n "$mon_pid" ]]; then
    kill "$mon_pid" 2>/dev/null || true
    wait "$mon_pid" 2>/dev/null || true
  fi
  "$VENV" "$MONITOR" snapshot --when end --self-tag "$self_tag" \
    --out "$OUT/${stem}_load_end.json"
  "$VENV" "$MONITOR" finalize \
    --jsonl "$jsonl" \
    --start "$OUT/${stem}_load_start.json" \
    --end "$OUT/${stem}_load_end.json" \
    --out "$side" \
    --wall-s $((t1 - t0)) | tee -a "$LOG"
  "$VENV" "$STAMP" "$results" "$threads" "$side" "$role" | tee -a "$LOG"
}

echo "phase1_18_part_b amendment4 continuation start $(date -Is)" | tee -a "$LOG"
echo "Full OMP=16 five-checkpoint arm CUT. ck0 OMP=1 re-run is canonical post-patch." | tee -a "$LOG"

archive_prepatch_ck0

# Q1: re-run ck0 at OMP=1 under post-patch binary; pre-patch object already archived.
run_one 1 0 "omp1_postpatch" "canonical" "checkpoint_0_omp1.json" "hydra_ck0_omp1_postpatch"
python3 - <<PY
import json, shutil
from pathlib import Path
out = Path("$OUT")
src = out / "checkpoint_0_omp1.json"
payload = json.loads(src.read_text(encoding="ascii"))
sha = payload["proofsearch_py_sha256"][:16]
dst = out / ("checkpoint_0_omp1_bin_%s.json" % sha)
shutil.copy2(src, dst)
print("canonical_ck0_bin", dst)
PY

run_one 1 1 "omp1_rep1" "default"
run_one 16 1 "omp16_rep1" "default"
run_one 16 1 "omp16_rep2" "default"
run_one 16 1 "omp16_rep3" "default"

"$VENV" "$ANALYZE" | tee -a "$LOG"
echo "phase1_18_part_b amendment4 done $(date -Is)" | tee -a "$LOG"
