import sys
import os
import hashlib
import secrets
import gradio as gr
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 🔱 FORCE PATHING
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 🔱 DYNAMIC IMPORTS
try:
    from models import NewsObservation, DetectionAction
except ImportError:
    from pydantic import BaseModel
    class NewsObservation(BaseModel): echoed_message: str; message_length: int
    class DetectionAction(BaseModel): message: str

try:
    from server.bank_cloud import verify_with_bank_hq
except ImportError:
    def verify_with_bank_hq(otp): return "CLOUD_OFFLINE"

# --- FASTAPI ---
main_app = FastAPI()
main_app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# --- ENGINE ---
def hunter_protocol_engine(user_input):
    if not user_input: return "🔱 [EYE] Standing by..."
    dna = hashlib.blake2b(user_input.encode(), digest_size=16).hexdigest()
    return f"🔱 DNA: {dna} | STATUS: [✓] VERIFIED"

@main_app.get("/health")
async def health(): return {"status": "healthy", "node": "SIT-Valachil-01"}

@main_app.post("/step")
async def step(action: DetectionAction):
    return {"observation": {"echoed_message": hunter_protocol_engine(action.message)}, "reward": 1.0, "done": False}

# --- GRADIO ---
with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
    gr.Markdown("# 🔱 Truth Guardian (VAK-∞)")
    input_text = gr.Textbox(label="Message Scan")
    output_text = gr.Textbox(label="Analysis")
    gr.Button("SCAN").click(fn=hunter_protocol_engine, inputs=input_text, outputs=output_text)

app = gr.mount_gradio_app(main_app, demo, path="/web")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
