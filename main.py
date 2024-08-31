from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Path to the directory containing audio files
AUDIO_DIR = os.path.join(os.path.dirname(__file__), "sounds")

@app.get("/play/{audio_name}")
async def play_audio(audio_name: str):
    file_path = os.path.join(AUDIO_DIR, f"{audio_name}.mp3")
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type='audio/mpeg')
    else:
        return {"error": "Audio file not found"}
