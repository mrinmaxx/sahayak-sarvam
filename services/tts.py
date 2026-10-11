import base64
from core.client import client
from config.settings import DEFAULT_TTS, DEFAULT_SPEAKER

def speak(text: str, lang_code: str) -> bytes:
    resp = client.text_to_speech.convert(
        text=text,
        language_code=lang_code,
        model=DEFAULT_TTS,
        speaker=DEFAULT_SPEAKER,
    )
    # Response contains base64-encoded audio in a list
    audio_b64 = resp.audios[0]
    return base64.b64decode(audio_b64)
