import sys
import os
import hashlib
import secrets
import gradio as gr
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1. FIX: Tell Python to look one folder up for models.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 2. IMPORT MODELS (from root)
try:
    from models import NewsObservation, DetectionAction
except ImportError:
    # Fallback if pathing is tricky in certain Docker environments
    from pydantic import BaseModel
    from typing import Optional, Dict
    class NewsObservation(BaseModel):
        echoed_message: str
        message_length: int
        done: bool = False
    class DetectionAction(BaseModel):
        message: str
        label: Optional[str] = "FAKE"

# 3. FIX: Relative import for the file in the same 'server' folder
# Note: Ensure your file is named bank_cloud.py
from .bank_cloud import verify_with_bank_hq

# --- FASTAPI INIT ---
main_app = FastAPI()
main_app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# --- CORE ENGINE ---
def hunter_protocol_engine(user_input):
    if not user_input or not user_input.strip():
        return "🔱 [EYE] Standing by. Paste message for DNA analysis..."
    
    dna = hashlib.blake2b(user_input.encode(), digest_size=64).hexdigest()
    token = f"VAK-∞-{secrets.token_hex(4).upper()}"
    scam_words = ["urgent", "otp", "bank", "win", "verify", "call", "account", "blocked"]
    is_scam = any(word in user_input.lower() for word in scam_words)
    
    header = f"🔱 SESSION DNA: {dna[:16]}... | TOKEN: {token}\n" + ("-" * 60) + "\n"
    if is_scam:
        return f"{header}🔱 STATUS: [!] FRAUD DNA DETECTED\n🔱 ACTION: NEUTRALIZED BY {token}"
    return f"{header}🔱 STATUS: [✓] VERIFIED REAL. NO DECEPTION DETECTED."

# --- API ENDPOINTS (OpenEnv Compliance) ---
@main_app.get("/health")
async def health(): return {"status": "healthy", "node": "SIT-Valachil-Main-01"}

@main_app.get("/reset")
@main_app.post("/reset")
async def reset():
    return {
        "episode_id": secrets.token_hex(8),
        "step_count": 0,
        "observation": {"echoed_message": "VAK-∞ Reset Complete", "message_length": 0}
    }

@main_app.post("/step")
async def step(action: DetectionAction):
    analysis = hunter_protocol_engine(action.message)
    # Extract digits for Bank HQ verification
    otp_code = "".join(filter(str.isdigit, action.message))[:6]
    cloud_status = verify_with_bank_hq(otp_code) if otp_code else "NO_OTP"
    
    return {
        "observation": {
            "echoed_message": f"{analysis} | CLOUD: {cloud_status}",
            "message_length": len(action.message),
            "metadata": {"node": "SIT-Valachil-Main-01"}
        },
        "reward": 1.0 if "[!]" in analysis else 0.5,
        "done": False
    }

# --- GRADIO UI ---
with gr.Blocks(theme=gr.themes.Monochrome(), title="Truth Guardian (VAK-∞)") as demo:
    gr.Markdown("# 🔱 Truth Guardian (VAK-∞)")
    gr.Markdown("Node: SIT-Valachil-Main-01 | Hunter-Protocol: **ACTIVE**")
    
    with gr.Column():
        input_text = gr.Textbox(label="Message / OTP Input Field", placeholder="Paste suspicious text here...", lines=4)
        run_btn = gr.Button("🚀 INITIALIZE HUNTER-PROTOCOL SCAN", variant="primary")
        clear_btn = gr.Button("🗑️ CLEAR SCANNER")
        output_text = gr.Textbox(label="Guardian Analysis & Active-Defense Logs", lines=10, interactive=False)
    
    gr.Markdown("---")
    gr.Markdown("🏁 **Official Submission** | Meta PyTorch OpenEnv Hackathon | **Team Vakratunda**")

    run_btn.click(fn=hunter_protocol_engine, inputs=input_text, outputs=output_text)
    clear_btn.click(lambda: [None, None], outputs=[input_text, output_text])

# --- MOUNT & LAUNCH ---
# This 'app' object is what uvicorn looks for
app = gr.mount_gradio_app(main_app, demo, path="/web")

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
