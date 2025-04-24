from fastapi import APIRouter
from pydantic import BaseModel
import uuid
from backend.generator.sd_client import generate_image
# from backend.generator.dialogue_creator import generate_dialogue
# from backend.generator.video_composer import compose_video
# from backend.utils.text_utils import extract_characters_and_topic

import os

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/generate")
async def generate_fanfic_video(request: PromptRequest):
    try:
        print("[INFO] AutoFanFic API is running.")
        prompt = request.prompt.strip()
        print("[INFO] Received prompt:", prompt)
        path = uuid.uuid4()
        resposne_img = generate_image(prompt, f"backend/generator/static/images/anime/{path}.png")
        print("[INFO] Image generation response:", resposne_img)
        if not prompt:
            return {"error": "Prompt cannot be empty."}

        # 1. Extract characters and topic
        # characters, topic = extract_characters_and_topic(prompt)
        # print("[INFO] Characters:", characters)
        # print("[INFO] Topic:", topic)

        # # 2. Generate dialogue
        # dialogue_lines = generate_dialogue(characters, topic)
        # print("[INFO] Dialogue:", dialogue_lines)

        # # 3. Generate images using Diffusers + SDXL
        # # image_paths = generate_images_from_characters(characters)
        # print("[INFO] Image paths:", image_paths)

        # if not image_paths:
        #     return {"error": "Image generation failed."}
        # # if not dialogue_lines:
        # #     return {"error": "Dialogue generation failed."}

        # 4. Compose video from generated assets
        # video_path = compose_video(image_paths, dialogue_lines)

        # if not video_path or not os.path.exists(video_path):
        #     return {"error": "Video generation failed."}

        # # 5. Convert path to URL for frontend
        # # If path is 'static/videos/output.mp4', convert to '/static/videos/output.mp4'
        # relative_url = "/" + video_path.replace("\\", "/") if not video_path.startswith("/") else video_path

        return {"video_url": "relative_url"}

    except Exception as e:
        print("[ERROR]", e)
        return {"error": str(e)}
