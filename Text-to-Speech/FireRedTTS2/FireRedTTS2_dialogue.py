import os
import sys
import torch
import torchaudio
from fireredtts2.fireredtts2 import FireRedTTS2

device = "cuda"

fireredtts2 = FireRedTTS2(
    pretrained_dir="./pretrained_models/FireRedTTS2",
    gen_type="dialogue",
    device=device,
)

text_list = [
    "[S1]那可能说对对，没有去过美国来说去去看到美国线下。巴斯曼也好，沃尔玛也好，他们线下不管说，因为深圳出去的还是电子周边的会表达，会发现哇对这个价格真的是很高呀。都是卖三十五美金、四十美金，甚至一个手机壳，就是二十五美金开。",
    "[S2]对，没错，我每次都觉得不不可思议。我什么人会买三五十美金的手机壳？但是其实在在那个target啊，就塔吉特这种超级市场，大家都是这样的，定价也很多人买。",
    "[S1]对对，那这样我们再去看说亚马逊上面卖卖卖手机壳也好啊，贴膜也好，还包括说车窗也好，各种线材也好，大概就是七块九九或者说啊八块九九，这个价格才是卖的最多的啊。因为亚马逊的游戏规则限定的。如果说你卖七块九九以下，那你基本上是不赚钱的。",
    "[S2]那比如说呃除了这个可能去到海外这个调查，然后这个调研考察那肯定是最直接的了。那平时我知道你是刚才建立了一个这个叫做呃rean的这样的一个一个播客，它是一个英文的。然后平时你还听一些什么样的东西，或者是从哪里获取一些这个海外市场的一些信息呢？",
    "[S1]嗯，因为做做亚马逊的话呢，我们会关注很多行业内的东西。就比如说行业有什么样亚马逊有什么样新的游戏规则呀。呃，物流的价格有没有波动呀，包括说有没有什么新的评论的政策呀，广告有什么新的打法呀？那这些我们会会关关注很多行业内部的微信公众号呀，还包括去去查一些知乎专栏的文章呀，以及说我们周边有很多同行。那我们经常会坐在一起聊天，看看信息有什么共享。那这个是关注内内的一个方式。",
]
prompt_wav_list = [
    "examples/chat_prompt/zh/S1.flac",
    "examples/chat_prompt/zh/S2.flac",
]

prompt_text_list = [
    "[S1]啊，可能说更适合美国市场应该是什么样子。那这这个可能说当然如果说有有机会能亲身的去考察去了解一下，那当然是有更好的帮助。",
    "[S2]比如具体一点的，他觉得最大的一个跟他预想的不一样的是在什么地方。",
]

all_audio = fireredtts2.generate_dialogue(
    text_list=text_list,
    prompt_wav_list=prompt_wav_list,
    prompt_text_list=prompt_text_list,
    temperature=0.9,
    topk=30,
)
torchaudio.save("chat_clone.wav", all_audio, 24000)

