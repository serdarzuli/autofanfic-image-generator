from diffusers import StableDiffusionXLPipeline, StableDiffusionPipeline
import torch
import os 
from PIL import Image

# SDXL Pipeline
device = "cuda" if torch.cuda.is_available() else "cpu"

if device == "cuda":
    pipe = StableDiffusionXLPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0",
        torch_dtype=torch.float16,
        use_safetensors=True,
    )
    pipe = pipe.to("cuda")
    print("INFO Using device: 'cuda'")     
    pipe.safety_checker = None  # Optional: can be disabled for faster results
else:
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float32,
        use_safetensors=True,
    )
    pipe = pipe.to("cpu")
    print("INFO Using device: 'cpu'")
    pipe.safety_checker = None


def generate_image(prompt:str, save_path:str) -> bool:
    try:
        prompt = f"{prompt}"
        print(f"[INFO] Generating image for: {prompt}")
        result = pipe(prompt, guidance_scale=7.5, num_inference_steps=30)
        image: Image.Image = result.images[0]

        image.save(save_path)
        print(f"[INFO] Image saved to: {save_path}")    
        
        return True
    except Exception as e:
        print(f"[ERROR] Failed to generate image for {prompt}: {e}")
        return False
