import os
import sys

# Ensure Python can import models.py inside /app
sys.path.append("/app")

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

def run_fallback_chain(prompt: str) -> str:
    chain = [
        call_gemini_pro,
        call_gemini_flash,
        call_mistral_large,
        call_openrouter_free,
        call_mistral_small,
        call_groq,
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

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))  # Render injects PORT
    uvicorn.run("server:app", host="0.0.0.0", port=port)
