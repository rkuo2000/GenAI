import os
import sys
import torch
import torchaudio
from fireredtts2.fireredtts2 import FireRedTTS2

device = "cuda"
lines = [
    "Hello everyone, welcome to our newly launched FireRedTTS2. It supports multiple languages including English, Chinese, Japanese, Korean, French, German, and Russian. Additionally, this TTS model features long-context dialogue generation capabilities.",
    "如果你厌倦了千篇一律的AI音色，不满意于其他模型语言支持不够丰富，那么本项目将会成为你绝佳的工具。",
    "ランダムな話者と言語を選択して合成できます",
    "이는 많은 인공지능 시스템에 유용합니다. 예를 들어, 제가 다양한 음성 데이터를 대량으로 생성해 여러분의 ASR 모델이나 대화 모델에 풍부한 데이터를 제공할 수 있습니다.",
    "J'évolue constamment et j'espère pouvoir parler davantage de langues avec plus d'aisance à l'avenir.",
]

fireredtts2 = FireRedTTS2(
    pretrained_dir="./pretrained_models/FireRedTTS2",
    gen_type="monologue",
    device=device,
)

# random speaker
for i in range(len(lines)):
    text = lines[i].strip()
    audio = fireredtts2.generate_monologue(text=text)
    # adjust temperature & topk
    # audio = fireredtts2.generate_monologue(text=text, temperature=0.8, topk=30)
    torchaudio.save(str(i) + ".wav", audio.cpu(), 24000)


# # voice clone
# for i in range(len(lines)):
#     text = lines[i].strip()

#     audio = fireredtts2.generate_monologue(
#         text=text,
#         prompt_wav=<prompt_wav_path>,
#         prompt_text=<prompt_wav_text>,
#     )
#     torchaudio.save(str(i) + ".wav", audio.cpu(), 24000)

