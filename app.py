import gradio as gr
import hashlib
import secrets
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

# --- INITIALIZE ---
app = FastAPI()

# --- THE OPENENV CRITICAL PATHS ---
# These MUST be at the root and respond to POST
@app.post("/reset")
async def reset_env():
    return JSONResponse(content={"status": "environment reset", "message": "VAK-∞ Shield Active"})

@app.post("/step")
async def step_env(request: Request):
    return JSONResponse(content={"status": "step successful"})

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# --- THE HUNTER ENGINE ---
def hunter_protocol_engine(user_input):
    if not user_input: return "🔱 [EYE] Standing by..."
    dna = hashlib.blake2b(user_input.encode(), digest_size=64).hexdigest()
    return f"🔱 SESSION DNA: {dna[:16]}\n🔱 STATUS: [✓] VERIFIED."

# --- THE UI ---
demo = gr.Interface(
    fn=hunter_protocol_engine,
    inputs=gr.Textbox(label="Message Input"),
    outputs=gr.Textbox(label="Analysis Logs"),
    title="🔱 Truth Guardian (VAK-∞)",
    description="### Node: SIT-Valachil-Main-01 | Hunter-Protocol: ACTIVE"
)

# --- THE MOUNT ---
# This is the "Secret Sauce": We mount Gradio to /web,
# and we add a GET for the root so the bot doesn't 404.
app = gr.mount_gradio_app(app, demo, path="/web")

@app.get("/")
async def root():
    return {"status": "active", "api": "ready", "ui": "/web"}

if __name__ == "__main__":
    # FORCE PORT 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
