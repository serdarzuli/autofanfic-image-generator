from fastapi import APIRouter, Request
from pydantic import BaseModel
from backend.generator.sd_client import generate_image
from backend.utils.file_handler import get_temp_output_path, get_temp_output_image_path
import os


router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/generate")
async def generate_fanfic_video(request: PromptRequest, fastapi_request: Request):
    try:
        print("[INFO] AutoFanFic API is running.")
        prompt = request.prompt.strip()
        if not prompt:
            return {"error": "Prompt cannot be empty."}
        path = get_temp_output_image_path()
        print("path: ",path)
        resposne_img = generate_image(prompt, path)
        print("[INFO] Image generation response:", resposne_img)

        base_url = str(fastapi_request.base_url).rstrip("/")
        relative_url = f"/static/img/{os.path.basename(path)}"
        full_url = f"{base_url}{relative_url}"
        print("[INFO] Full image URL:", full_url)


        return {"image_url": full_url}

    except Exception as e:
        print("[ERROR]", e)
        return {"error": str(e)}
