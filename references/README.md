# References and clean rooms

## Literature map

Level -1 will cover grokking and progress measures, transfer in grokked models,
active learning under equal information, error consistency across seeds and
architectures, continual learning, library learning, open-ended environment
design, automated geometry/proof systems, RL with verifiable reward, and the Era
of Experience thesis.

Each entry must identify a primary source, the exact proposition it supports,
replication status, and whether the corresponding Philosophia claim is known,
partial, or open. Literature summaries cannot replace anchor replications.

## Clean-room families

Available external rooms include Claude Opus, GPT, free Gemini chat, and free Grok
chat. Available local rooms include Gemma, Llama, and Qwen-family models served by
`llama-server`.

Independence is measured by model family and information boundary, not by session
count. Online and local variants from the same underlying family do not
automatically count as independent.

For every clean-room build:

1. Freeze a task-language specification that does not name the detector or its
   expected signature.
2. Record provider, displayed model name, date, sampling settings when available,
   and the exact prompt.
3. Hash and commit the prompt before inspecting the response.
4. Save the response verbatim before adaptation or comparison.
5. Do not expose outputs from another room, reference-field thresholds, holdout
   identities, or the desired verdict.
6. Treat unavailable model/version metadata as an explicit limitation.

Cursor Compose is a development executor for frozen routine specifications, not
an independent scientific room after it has read the implementation or detector.
