# !pip install --upgrade -q accelerate bitsandbytes
# !pip install git+https://github.com/huggingface/transformers.git

from PIL import Image
import requests
from transformers import AutoProcessor, LlavaForConditionalGeneration
from transformers import BitsAndBytesConfig
import torch

model_id = "llava-hf/llava-1.5-7b-hf"

quantization_config = BitsAndBytesConfig( load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16 )

model = LlavaForConditionalGeneration.from_pretrained(model_id, quantization_config=quantization_config, device_map="auto")
processor = AutoProcessor.from_pretrained(model_id)

#prompt = "USER: <image>\nWhat are the things I should be cautious about when I visit this place?\nASSISTANT:"
#url = "https://llava-vl.github.io/static/images/view.jpg"
#image = Image.open(requests.get(url, stream=True).raw)

prompt = "USER: <image>\n這是什麼有名的台南美食?\nASSISTANT:"
filepath = "images/Tainan_BeefSoup.jpg"
image = Image.open(filepath)

inputs = processor(text=prompt, images=image, return_tensors="pt")

output = model.generate(**inputs, max_new_tokens=200)

generated_text = processor.batch_decode(output, skip_special_tokens=True)[0]
print()
print(generated_text.split("ASSISTANT:")[-1])
