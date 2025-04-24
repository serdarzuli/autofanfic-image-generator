import os
import uuid

def get_temp_output_path(filename="output.mp4"):
    """Generates a safe, unique path for saving video output."""
    os.makedirs("static/videos", exist_ok=True)
    unique_id = uuid.uuid4().hex[:8]
    return os.path.join("static/videos", f"{unique_id}_{filename}")

def get_temp_output_image_path(filename="img.png"):
    """Generates a safe, unique path for saving image output."""
    unique_id = uuid.uuid4().hex[:8]
    return os.path.join("static", "img", f"{unique_id}_{filename}")