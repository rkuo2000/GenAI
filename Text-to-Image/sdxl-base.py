# pip install diffusers --upgrade
# pip install invisible_watermark transformers accelerate safetensors

from diffusers import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("cuda")

prompt = "An astronaut riding a horse"

images = pipe(prompt=prompt).images[0]
images.save("output.png")
images.show()
