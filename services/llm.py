from core.client import client
from config.settings import DEFAULT_LLM

def ask(prompt: str, lang_code: str = "hi-IN", system_prompt: str = None) -> str:
    if system_prompt is None:
        lang_name = {"hi-IN": "Hindi", "ta-IN": "Tamil", "bn-IN": "Bengali"}.get(lang_code, "Hindi")
        system_prompt = f"You are a helpful assistant. The user may speak in code-mixed {lang_name}/English. Respond in simple, friendly {lang_name}."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]
    resp = client.chat.completions(
        model=DEFAULT_LLM,
        messages=messages,
        temperature=0.3,
        max_tokens=300,
    )
    return resp.choices[0].message.content
