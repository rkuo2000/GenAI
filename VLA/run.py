# git clone https://github.com/openvla/openvla
# cd openvla
# pip install -r requirements-min.txt

from transformers import AutoModelForVision2Seq, AutoProcessor
from PIL import Image

import torch

# Load Processor & VLA
processor = AutoProcessor.from_pretrained("openvla/openvla-7b", trust_remote_code=True)
vla = AutoModelForVision2Seq.from_pretrained(
    "openvla/openvla-7b", 
    attn_implementation="flash_attention_2",  # [Optional] Requires `flash_attn`
    torch_dtype=torch.bfloat16, 
    low_cpu_mem_usage=True, 
    trust_remote_code=True
).to("cuda:0")

# Grab image input & format prompt
#image: Image.Image = get_from_camera(...)
from PIL import Image
image = Image.open("./apple_orange.jpg")
image.show()

INSTRUCTION = "grap the apple"
prompt = "In: What action should the robot take to " +INSTRUCTION+ "?\n"
print(prompt)

# Predict Action (7-DoF; un-normalize for BridgeData V2)
inputs = processor(prompt, image).to("cuda:0", dtype=torch.bfloat16)
action = vla.predict_action(**inputs, unnorm_key="bridge_orig", do_sample=False)

print(action)
# Execute...
#robot.act(action, ...)
