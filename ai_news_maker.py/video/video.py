from moviepy import ImageClip, concatenate_videoclips, AudioFileClip
import numpy as np
import os


def get_video(images, output_file="shorts_video.mp4"):
    clips = []

    audio_path = os.path.join(os.path.dirname(__file__), "..", "..", "output.mp3")
    audio_path = os.path.abspath(audio_path)
    audio = AudioFileClip(audio_path)
    print(f"Audio duration: {audio.duration}")

    duration_per_image = audio.duration / len(images)

    for img in images:
        w, h = img.size
        target_width = 1080
        target_height = 1920

        new_width = int(w * (target_height / h))
        img_resized = img.resize((new_width, target_height))

        left = (new_width - target_width) // 2
        right = left + target_width
        img_cropped = img_resized.crop((left, 0, right, target_height))

        clip = ImageClip(np.array(img_cropped),duration=duration_per_image)
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")

    final_video = video.with_audio(audio)

    final_video.write_videofile(
        output_file,
        fps=24,
        codec="libx264",
    )