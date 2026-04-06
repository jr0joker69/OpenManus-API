import os, requests

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

def call_mistral_large(prompt: str) -> str:
    try:
        r = requests.post(
            "https://api.mistral.ai/v1/large",
            headers={"Authorization": f"Bearer {MISTRAL_API_KEY}"},
            json={"prompt": prompt},
            timeout=10
        )
        return r.json().get("reply", "")
    except Exception as e:
        print(f"Mistral Large failed: {e}")
        return None

def call_mistral_small(prompt: str) -> str:
    try:
        r = requests.post(
            "https://api.mistral.ai/v1/small",
            headers={"Authorization": f"Bearer {MISTRAL_API_KEY}"},
            json={"prompt": prompt},
            timeout=10
        )
        return r.json().get("reply", "")
    except Exception as e:
        print(f"Mistral Small failed: {e}")
        return None
