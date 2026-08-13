#!/usr/bin/env bash
# Phase-1b extrinsic diagnostic (NON-CITABLE): budget-masked or policy-limited?
# Identical wiring to run_phase1_extrinsic_16.sh. Only two things change:
#   - MCTS budget 2000 -> 8000 (4x)
#   - checkpoints 0 and 4 only
# All 30 Kleene statements are run (not just the 19 never-solved): the 11 already
# solved cost ~8 s each, so restricting the set would save minutes while adding a
# selection step. Full set keeps ck0/ck4 directly comparable at the new budget.
# No retraining, no agent/theory/config edits.
set -euo pipefail

MINIMO_LEARNING=/home/master/llm_projects/minimo/learning
VENV=/home/master/llm_projects/minimo/.venv/bin/python
CKPT_DIR=/home/master/llm_projects/minimo/learning/outputs/2026-08-10/00-14-33
OUT=/home/master/llm_projects/philosophia/successor/dev/phase1_extrinsic_16b
LOG=/home/master/llm_projects/philosophia/successor/dev/phase1_extrinsic_16b_run.log

mkdir -p "$OUT"
: > "$LOG"
cd "$MINIMO_LEARNING"

export OMP_NUM_THREADS=16
export PYTHONUNBUFFERED=1

echo "phase1_extrinsic_16b start $(date -Is)" | tee -a "$LOG"

for ck in 0 4; do
  echo "===== checkpoint ${ck} budget 8000 $(date -Is) =====" | tee -a "$LOG"
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
    +results_path="$OUT/checkpoint_${ck}.json" \
    "hydra.run.dir=$OUT/hydra_ck${ck}" \
    2>&1 | tee -a "$LOG"
done

echo "phase1_extrinsic_16b done $(date -Is)" | tee -a "$LOG"
