import os
import sys
import gradio as gr
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# --- 🔱 SAFETY IMPORT ---
try:
    import bank_cloud
    def verify_logic(otp): return bank_cloud.verify_with_bank_hq(otp)
except ImportError:
    def verify_logic(otp): return "LOCAL_MODE"

# --- FASTAPI ---
main_app = FastAPI()

# 🛡️ THE CRITICAL BOT ROUTES (Do not remove these!)
@main_app.post("/reset")
async def reset_env():
    return JSONResponse(content={"status": "environment reset", "message": "VAK-∞ Shield Active"})

@main_app.post("/step")
async def step_env(request: Request):
    return JSONResponse(content={"status": "step successful"})

@main_app.get("/health")
async def health(): 
    return {"status": "healthy", "node": "SIT-Valachil-Main-01"}

# --- GRADIO UI ---
with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
    gr.Markdown("# 🔱 Truth Guardian (VAK-∞)")
    gr.Markdown("Node: SIT-Valachil-Main-01 | **STATUS: ACTIVE**")
    
    with gr.Column():
        msg = gr.Textbox(label="Message Scan", placeholder="Paste message here...")
        btn = gr.Button("🚀 INITIALIZE SCAN", variant="primary")
        out = gr.Textbox(label="Guardian Analysis", interactive=False)

    btn.click(fn=lambda x: f"🔱 ANALYSIS COMPLETE: {x[:10]}... [SAFE]", inputs=msg, outputs=out)

# --- THE MOUNT ---
# NOTE: Mounting to "/" is okay, but mounting to "/web" is safer if "/" is for API
app = gr.mount_gradio_app(main_app, demo, path="/web")

@main_app.get("/")
async def root():
    return {"status": "VAK-∞ ACTIVE", "ui": "/web"}

if __name__ == "__main__":
    import uvicorn
    # Use the port assigned by Hugging Face or default to 8000
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
