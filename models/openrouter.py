import os, requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def call_openrouter_free(prompt: str) -> str:
    try:
        r = requests.post(
            "https://openrouter.ai/api/v1/free",
            headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
            json={"prompt": prompt},
            timeout=10
        )
        return r.json().get("reply", "")
    except Exception as e:
        print(f"OpenRouter Free failed: {e}")
        return None
