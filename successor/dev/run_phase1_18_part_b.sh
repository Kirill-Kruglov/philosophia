#!/usr/bin/env bash
# PHASE1_18 Part B (amended): OMP=1 five-ck + gate. NO_SEED_SPEND.
# Intended instrument = OMP=1 until/unless the ck1 determinism control falsifies
# that (amendment 3 Q1). Thread config is stamped into every results JSON.
set -euo pipefail

MINIMO_LEARNING=/home/master/llm_projects/minimo/learning
VENV=/home/master/llm_projects/minimo/.venv/bin/python
CKPT_DIR=/home/master/llm_projects/minimo/learning/outputs/2026-08-10/00-14-33
DEV=/home/master/llm_projects/philosophia/successor/dev
OUT="$DEV/phase1_18_part_b"
LOG="$DEV/phase1_18_part_b_run.log"
STAMP="$DEV/phase1_18_stamp_threads.py"
ANALYZE="$DEV/phase1_18_part_b_analyze.py"

mkdir -p "$OUT"
: > "$LOG"
cd "$MINIMO_LEARNING"
export PYTHONUNBUFFERED=1
export PYTHONDONTWRITEBYTECODE=1

stamp_and_log() {
  local json_path="$1" threads="$2" role="${3:-default}"
  "$VENV" "$STAMP" "$json_path" "$threads" - "$role" | tee -a "$LOG"
}

run_cfg() {
  local threads="$1"
  local tag="omp${threads}"
  export OMP_NUM_THREADS="$threads"
  export MKL_NUM_THREADS="$threads"
  export OPENBLAS_NUM_THREADS="$threads"
  export NUMEXPR_NUM_THREADS="$threads"
  export TORCH_NUM_THREADS="$threads"
  export VECLIB_MAXIMUM_THREADS="$threads"
  echo "===== config ${tag} start $(date -Is) =====" | tee -a "$LOG"
  for ck in 0 1 2 3 4; do
    echo "===== ${tag} ck${ck} budget 8000 $(date -Is) =====" | tee -a "$LOG"
    local results="$OUT/checkpoint_${ck}_${tag}.json"
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
      "hydra.run.dir=$OUT/hydra_ck${ck}_${tag}" \
      2>&1 | tee -a "$LOG"
    # ck0 of this arm is pre-patch (process started before D1); stamp auto-detects too.
    if [[ "$ck" -eq 0 && "$threads" -eq 1 ]]; then
      stamp_and_log "$results" "$threads" pre_patch_ck0
    else
      stamp_and_log "$results" "$threads" default
    fi
  done
  echo "===== config ${tag} done $(date -Is) =====" | tee -a "$LOG"
}

echo "phase1_18_part_b start $(date -Is)" | tee -a "$LOG"
echo "Lenovo Legion excluded: 8 GiB VRAM gave no expected performance gain." | tee -a "$LOG"

# Amendment 2: full five-ck OMP=16 CUT. This script only finishes OMP=1 + gate.
# Items 2-3 (ck1 OMP=1 repeat; three OMP=16 ck1 repeats) run via am2 continuation.
run_cfg 1
"$VENV" "$ANALYZE" --gate-omp1-only | tee -a "$LOG"
echo "phase1_18_part_b omp1+gate done $(date -Is); am2 watcher launches continuation" | tee -a "$LOG"
