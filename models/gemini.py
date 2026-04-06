import os, requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def call_gemini_pro(prompt: str) -> str:
    try:
        r = requests.post(
            "https://api.gemini.com/v1/pro",
            headers={"Authorization": f"Bearer {GEMINI_API_KEY}"},
            json={"prompt": prompt},
            timeout=10
        )
        return r.json().get("reply", "")
    except Exception as e:
        print(f"Gemini Pro failed: {e}")
        return None

def call_gemini_flash(prompt: str) -> str:
    try:
        r = requests.post(
            "https://api.gemini.com/v1/flash",
            headers={"Authorization": f"Bearer {GEMINI_API_KEY}"},
            json={"prompt": prompt},
            timeout=10
        )
        return r.json().get("reply", "")
    except Exception as e:
        print(f"Gemini Flash failed: {e}")
        return None
