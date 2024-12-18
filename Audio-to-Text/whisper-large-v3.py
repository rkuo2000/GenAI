## pip install --upgrade pip
## pip install --upgrade transformers datasets[audio] accelerate
# usage: python whisper-large-v3.py test.mp3

import sys
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

device = "cuda:0" if torch.cuda.is_available() else "cpu"
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

#dataset = load_dataset("distil-whisper/librispeech_long", "clean", split="validation")
#sample = dataset[0]["audio"]
#result = pipe(sample)

if len(sys.argv)>1:
    audiofile = sys.argv[1]
else:
    audiofile = 'audio/test.mp3'

#result = pipe(["audio_1.mp3", "audio_2.mp3"], batch_size=2) # batch
result = pipe(audiofile) 
print(result["text"])
