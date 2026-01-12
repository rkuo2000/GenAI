import torch
import torchaudio
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
from huggingface_hub import hf_hub_download

device = "cuda" if torch.cuda.is_available() else "cpu"

model_id = "ibm-granite/granite-speech-3.3-2b"
processor = AutoProcessor.from_pretrained(model_id)
tokenizer = processor.tokenizer
model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id, device_map=device, torch_dtype=torch.bfloat16
)
# load audio
audio_path = hf_hub_download(repo_id=model_id, filename="10226_10111_000000.wav")
wav, sr = torchaudio.load(audio_path, normalize=True)
assert wav.shape[0] == 1 and sr == 16000  # mono, 16khz

# create text prompt
system_prompt = "Knowledge Cutoff Date: April 2024.\nToday's Date: April 9, 2025.\nYou are Granite, developed by IBM. You are a helpful AI assistant"
user_prompt = "<|audio|>can you transcribe the speech into a written format?"
chat = [
    dict(role="system", content=system_prompt),
    dict(role="user", content=user_prompt),
]
prompt = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)

# run the processor+model
model_inputs = processor(prompt, wav, device=device, return_tensors="pt").to(device)
model_outputs = model.generate(**model_inputs, max_new_tokens=200, do_sample=False, num_beams=1)

# Transformers includes the input IDs in the response.
num_input_tokens = model_inputs["input_ids"].shape[-1]
new_tokens = torch.unsqueeze(model_outputs[0, num_input_tokens:], dim=0)
output_text = tokenizer.batch_decode(
    new_tokens, add_special_tokens=False, skip_special_tokens=True
)
print(f"STT output = {output_text[0].upper()}")

