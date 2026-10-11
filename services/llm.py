from core.client import client
from config.settings import DEFAULT_LLM

def ask(prompt: str, lang_code: str = "hi-IN", system_prompt: str = None) -> str:
    if system_prompt is None:
        lang_name = {"hi-IN": "Hindi", "ta-IN": "Tamil", "bn-IN": "Bengali"}.get(lang_code, "Hindi")
        system_prompt = (
            f"You are a helpful assistant. The user may speak in code-mixed "
            f"{lang_name}/English. Respond in simple, friendly {lang_name}."
        )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]

    resp = client.chat.completions(
        model=DEFAULT_LLM,
        messages=messages,
        temperature=0.3,
        max_tokens=2000,           # ← increased from 300
        reasoning_effort="low",    # ← new: minimize reasoning overhead
    )

    msg = resp.choices[0].message
    content = msg.content

    # Fallback: if content is None, try reasoning_content
    if content is None:
        content = getattr(msg, "reasoning_content", None)

    return content if content else "(empty response)"message.content
