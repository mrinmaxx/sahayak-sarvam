import os
from dotenv import load_dotenv
load_dotenv()

from core.client import client
from config.settings import DEFAULT_LLM, DEFAULT_TTS, DEFAULT_STT, DEFAULT_SPEAKER

print("=== DIAGNOSTIC TEST ===")
print("API Key loaded:", bool(os.getenv("SARVAM_API_KEY")))
print("LLM:", DEFAULT_LLM)
print("TTS:", DEFAULT_TTS)
print("STT:", DEFAULT_STT)
print("Speaker:", DEFAULT_SPEAKER)
print()

# Test 1: LLM
print("[1/3] Testing LLM...")
try:
    resp = client.chat.completions(
        model=DEFAULT_LLM,
        messages=[{"role": "user", "content": "Say hi in Hindi"}],
        max_tokens=2000,
        reasoning_effort="low",
    )
    msg = resp.choices[0].message
    content = msg.content or getattr(msg, "reasoning_content", None)
    print("  OK:", content[:60] if content else "(empty)")
    print("  content type:", type(msg.content))
    print("  reasoning_content present:", hasattr(msg, "reasoning_content"))
except Exception as e:
    print("  FAIL:", type(e).__name__, str(e)[:300])

# Test 2: TTS
print("[2/3] Testing TTS...")
try:
    resp = client.text_to_speech.convert(
        text="नमस्ते",
        language_code="hi-IN",
        model=DEFAULT_TTS,
        speaker=DEFAULT_SPEAKER,
    )
    print("  OK, audio type:", type(resp.audios), "length:", len(resp.audios))
    print("  First item type:", type(resp.audios[0]))
except Exception as e:
    print("  FAIL:", type(e).__name__, str(e)[:300])

# Test 3: STT
print("[3/3] Testing STT...")
sample = "data/samples/test.wav"
if not os.path.exists(sample):
    print("  SKIPPED: no sample audio at", sample)
else:
    try:
        resp = client.speech_to_text(
            model=DEFAULT_STT,
            audio_file=sample,
            language_code="hi-IN",
            mode="codemix",
        )
        print("  OK:", resp.text[:80])
    except Exception as e:
        print("  FAIL:", type(e).__name__, str(e)[:300])

print()
print("=== DONE ===")