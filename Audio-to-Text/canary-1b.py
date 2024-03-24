# pip install git+https://github.com/NVIDIA/NeMo.git@r1.23.0#egg=nemo_toolkit[asr]

from nemo.collections.asr.models import EncDecMultiTaskModel

# load model
model_name = "nvidia/canary-1b"
model = EncDecMultiTaskModel.from_pretrained(model_name)

# update dcode params
decode_cfg = model.cfg.decoding
decode_cfg.beam.beam_size = 1
model.change_decoding_strategy(decode_cfg)

# model transcribe
predicted_text = model.transcribe(
    paths2audio_files=['gTTS.mp3'],
    batch_size=16,  # batch size to run the inference with
)
print(predicted_text[0])
