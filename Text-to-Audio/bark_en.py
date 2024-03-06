# pip install bark

from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

preload_models()

prompt = """
Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
But I also have other interests such as playing tic tac toe.
"""

audio_array = generate_audio(prompt)

write_wav("output.wav", SAMPLE_RATE, audio_array)
