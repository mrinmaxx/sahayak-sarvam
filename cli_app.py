import os
import sys
from services.llm import ask
from services.tts import speak
from services.stt import transcribe
from config.languages import LANGUAGES

def main():
    print("=== Sahayak Voice Agent (CLI Demo) ===")
    print("Languages:", ", ".join(LANGUAGES.keys()))
    lang = input("Choose language (default hi-IN): ").strip() or "hi-IN"
    if lang not in LANGUAGES:
        print("Invalid language. Using hi-IN.")
        lang = "hi-IN"

    mode = input("Type 'audio' to use a wav file, or 'text' to type input: ").strip().lower()

    if mode == "audio":
        audio_path = input("Enter path to .wav file: ").strip()
        if not os.path.exists(audio_path):
            print("File not found.")
            return
        print("Transcribing...")
        transcript = transcribe(audio_path, lang)
        print("Transcript:", transcript)
    else:
        transcript = input("Type your question: ").strip()

    print("Thinking...")
    response = ask(transcript, lang)
    print("Response:", response)

    print("Generating audio...")
    audio_bytes = speak(response, lang)
    out_path = "data/cache/response.wav"
    os.makedirs("data/cache", exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(audio_bytes)
    print(f"Audio saved to: {out_path}")
    print("Play it with: start " + out_path)

if __name__ == "__main__":
    main()
