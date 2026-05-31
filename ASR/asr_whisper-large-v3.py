## pip install --upgrade pip
## pip install --upgrade transformers datasets[audio] accelerate
# usage: python whisper-large-v3.py test.mp3

from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

import torch
device = "cuda" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3"
#model_id = "openai/whisper-large-v3-turbo"

model = AutoModelForSpeechSeq2Seq.from_pretrained( model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True)

model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)

import sys
audiofile = sys.argv[1]

#result = pipe(["audio_1.mp3", "audio_2.mp3"], batch_size=2) # batch
result = pipe(audiofile) 
print(result["text"])
