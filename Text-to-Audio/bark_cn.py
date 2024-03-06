# pip install bark

from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

preload_models()

prompt = """
大家好, 我试着用中文說明一下这个AI模型的用法[clears throat]
然后演示一下文字生成语音
"""

audio_array = generate_audio(prompt)

write_wav("output.wav", SAMPLE_RATE, audio_array)
