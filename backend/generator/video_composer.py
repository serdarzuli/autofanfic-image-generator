from moviepy.editor import ImageClip, concatenate_videoclips
import os
from typing import List

def compose_video(image_paths: List[str], dialogue_lines: List[str], output_path="static/videos/output.mp4") -> str:
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        print("[DEBUG] Başladı: compose_video")

        # Görsel sayısı, diyalog sayısı kadar çoğaltılıyor
        total_scenes = len(dialogue_lines)
        image_cycle = (image_paths * ((total_scenes + len(image_paths) - 1) // len(image_paths)))[:total_scenes]
        print(f"[DEBUG] Görsel sayısı: {len(image_cycle)}")

        clips = []
        for i, img_path in enumerate(image_cycle):
            print(f"[DEBUG] Görsel sahne {i+1}: {img_path}")
            clip = ImageClip(img_path).set_duration(3).resize(width=720)
            clips.append(clip)

        final = concatenate_videoclips(clips, method="compose")
        print("[DEBUG] Videoyu yazıyor...")
        final.write_videofile(output_path, fps=24, codec="libx264")
        print("[DEBUG] Video yazıldı:", output_path)

        return os.path.basename(output_path)

    except Exception as e:
        print("[ERROR] Video oluşturulamadı:", e)
        return None
