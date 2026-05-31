# pip install nemo_toolkit['asr']

import nemo.collections.asr as nemo_asr

asr_model = nemo_asr.models.ASRModel.from_pretrained("nvidia/canary-1b-v2")

text = asr_model.transcribe(["audio/audio4.flac"])[0].text

print(text)
