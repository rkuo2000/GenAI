# pip install bark

from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

preload_models()

prompt = """
大家好, 我試著用中文說明一下這個AI模型的用法[clears throat]
然後展示一下文字生成語音
"""

audio_array = generate_audio(prompt)

write_wav("output.wav", SAMPLE_RATE, audio_array)
