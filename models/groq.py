import os, requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def call_groq(prompt: str) -> str:
    try:
        r = requests.post(
            "https://api.groq.com/v1/chat",
            headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
            json={"prompt": prompt},
            timeout=10
        )
        return r.json().get("reply", "")
    except Exception as e:
        print(f"Groq failed: {e}")
        return None
