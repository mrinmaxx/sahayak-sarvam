from core.client import client
from config.settings import DEFAULT_STT

def transcribe(audio_path: str, lang_code: str, mode: str = "codemix") -> str:
    resp = client.speech_to_text(
        model=DEFAULT_STT,
        audio_file=audio_path,
        language_code=lang_code,
        mode=mode,
    )
    return resp.text
