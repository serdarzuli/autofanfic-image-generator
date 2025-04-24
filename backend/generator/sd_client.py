from diffusers import StableDiffusionXLPipeline
import torch
import os 
from PIL import Image

# SDXL Pipeline
pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    use_safetensors=True,
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
print(f"[INFO] Using device: {'cuda' if torch.cuda.is_available() else 'cpu'}")
pipe.safety_checker = None  # Optional: can be disabled for faster results

def generate_image(prompt:str, save_path:str) -> bool:
    try:
        prompt = f"{prompt}"
        print(f"[INFO] Generating image for: {prompt}")
        result = pipe(prompt, guidance_scale=7.5, num_inference_steps=30)
        image: Image.Image = result.images[0]

        os.mkdir(os.path.dirname(save_path), exist_ok=True)
        image.save(save_path)
        
        return True
    except Exception as e:
        print(f"[ERROR] Failed to generate image for {prompt}: {e}")
        return False
