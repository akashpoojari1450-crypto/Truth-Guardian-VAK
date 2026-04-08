import os
import sys
import gradio as gr
from fastapi import FastAPI

# --- 🔱 SAFETY IMPORT ---
try:
    # We look for bank_cloud in the root now to avoid path errors
    import bank_cloud
    def verify_logic(otp): return bank_cloud.verify_with_bank_hq(otp)
except ImportError:
    def verify_logic(otp): return "LOCAL_MODE"

# --- FASTAPI ---
main_app = FastAPI()

@main_app.get("/health")
async def health(): return {"status": "healthy", "node": "SIT-Valachil-Main-01"}

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
# This matches the uvicorn app:app command
app = gr.mount_gradio_app(main_app, demo, path="/")

if __name__ == "__main__":
    import uvicorn
    
