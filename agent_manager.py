import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. LOAD THE KEY FIRST
load_dotenv()

# 2. INITIALIZE CLIENT
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 🖼️ NANO BANANA 2 (Images)
def get_tile_image(prompt):
    print(f"🎨 Dreaming up tile...")
    response = client.models.generate_content(
        model="gemini-3.1-flash-image-preview",
        contents=[prompt],
        config=types.GenerateContentConfig(
            # Using 1:1 ratio for a square game grid
            candidate_count=1
        )
    )
    # This returns a PIL Image object that main.py can .show()
    return response.generated_images[0]

# 🎵 LYRIA 3 (Music)
def get_background_music(theme):
    print(f"🎵 Composing {theme} track...")
    response = client.models.generate_content(
        model="lyria-3-clip-preview",
        contents=[f"Looping {theme} game music, top-down RPG style, instrumental."],
        config=types.GenerateContentConfig(response_modalities=["AUDIO"])
    )
    # Save to a file so the team can play it
    audio_path = "background_loop.mp3"
    with open(audio_path, "wb") as f:
        f.write(response.generated_audio[0].audio_bytes)
    return audio_path

# 🎥 VEO 3.1 (Video)
def get_victory_video(theme):
    print(f"🎬 Rendering cinematic finale...")
    operation = client.models.generate_videos(
        model="veo-3.1-generate-preview",
        prompt=f"Cinematic 4K top-down view of a player escaping a {theme} world, radiant light.",
    )
    
    # Video takes time to "cook," so we wait
    while not operation.done:
        time.sleep(1)
        
    return operation.result # This will be the video file/URL