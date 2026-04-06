import sys
import os

# Make sure /app is in the Python path (important for Docker/Render)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Request
from models import (
    call_gemini_pro,
    call_gemini_flash,
    call_mistral_large,
    call_openrouter_free,
    call_mistral_small,
    call_groq
)

app = FastAPI()

def run_fallback_chain(prompt):
    chain = [
        call_gemini_pro,
        call_gemini_flash,
        call_mistral_large,
        call_openrouter_free,
        call_mistral_small,
        call_groq
    ]
    for model in chain:
        try:
            result = model(prompt)
            if result:
                return result
        except Exception:
            continue
    return "All models failed."

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    msg = data.get("message", "")
    reply = run_fallback_chain(msg)
    return {"reply": reply}

@app.get("/health")
async def health():
    return {"status": "ok"}
