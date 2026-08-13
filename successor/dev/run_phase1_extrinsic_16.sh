#!/usr/bin/env bash
# Phase-1 extrinsic Kleene eval orchestrator (NON-CITABLE).
# Invokes minimo proofsearch.py evaluate_agent only; does not retrain.
set -euo pipefail

MINIMO_LEARNING=/home/master/llm_projects/minimo/learning
VENV=/home/master/llm_projects/minimo/.venv/bin/python
CKPT_DIR=/home/master/llm_projects/minimo/learning/outputs/2026-08-10/00-14-33
OUT=/home/master/llm_projects/philosophia/successor/dev/phase1_extrinsic_16
LOG=/home/master/llm_projects/philosophia/successor/dev/phase1_extrinsic_16_run.log

mkdir -p "$OUT"
: > "$LOG"
cd "$MINIMO_LEARNING"

export OMP_NUM_THREADS=16
export PYTHONUNBUFFERED=1

echo "phase1_extrinsic_16 start $(date -Is)" | tee -a "$LOG"

for ck in 0 1 2 3 4; do
  echo "===== checkpoint ${ck} $(date -Is) =====" | tee -a "$LOG"
  nice -n 10 "$VENV" ./proofsearch.py \
    task=eval \
    problemset=kleene \
    agent=mcts-lm \
    agent.max_mcts_nodes=2000 \
    agent.node_type=holophrasm \
    accumulate_library=false \
    +seed=0 \
    +agent_path="$CKPT_DIR/${ck}.pt" \
    job.wandb_project=null \
    +results_path="$OUT/checkpoint_${ck}.json" \
    "hydra.run.dir=$OUT/hydra_ck${ck}" \
    2>&1 | tee -a "$LOG"
done

echo "phase1_extrinsic_16 done $(date -Is)" | tee -a "$LOG"
