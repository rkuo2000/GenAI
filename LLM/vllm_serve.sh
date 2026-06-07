#vllm serve Qwen/Qwen3-0.6B --port 8000
vllm serve google/gemma-4-E2B-it --tensor-parallel-size 2 --quantization fp8 --max-model-len 8192 --trust-remote-code
