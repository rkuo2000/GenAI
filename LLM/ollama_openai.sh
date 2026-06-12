#curl http://localhost:11434/api/chat -d '{
curl http://localhost:11434/v1/chat/completions -d '{
  "model": "gemma4:e2b",
  "messages": [{
    "role": "user",
    "content": "Why is the sky blue?"
  }],
}'
