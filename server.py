from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    
    # Replace with actual OpenClaude inference call
    response = f"OpenClaude reply to: {user_message}"
    
    return {"reply": response}
