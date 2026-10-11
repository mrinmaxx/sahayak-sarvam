from services.stt import transcribe
from services.llm import ask
from services.tts import speak

def run(audio_path: str, lang_code: str) -> dict:
    transcript = transcribe(audio_path, lang_code)
    if not transcript or len(transcript.strip()) == 0:
        return {"transcript": "", "response": "Sorry, I didn't catch that.", "audio": b""}
    response_text = ask(transcript, lang_code)
    audio_bytes = speak(response_text, lang_code)
    return {"transcript": transcript, "response": response_text, "audio": audio_bytes}
