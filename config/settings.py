import os
from dotenv import load_dotenv

load_dotenv()

SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")
DEFAULT_LLM = "sarvam-105b"
DEFAULT_STT = "saaras:v3"
DEFAULT_TTS = "bulbul:v3"
DEFAULT_SPEAKER = "priya"
