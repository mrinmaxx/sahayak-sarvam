from services.llm import ask
from services.tts import speak

def test_llm():
    out = ask("Say hi in Hindi", "hi-IN")
    print("LLM OK:", out[:80])

def test_tts():
    audio = speak("Namaste", "hi-IN")
    print("TTS OK:", len(audio), "bytes")

if __name__ == "__main__":
    test_llm()
    test_tts()
