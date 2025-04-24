# backend/utils/image_utils.py

from backend.generator.sd_client import generate_image
import os

def generate_images_from_characters(characters: list[str]) -> list[str]:
    image_paths = []

    for character in characters:
        safe_name = character.lower().replace(" ", "_")
        save_path = os.path.join("static", "images", f"{safe_name}.png")

        success = generate_image(character, save_path)
        if success:
            image_paths.append(save_path)
        else:
            print(f"[WARN] Görsel oluşturulamadı: {character}")

    return image_paths
