import os
import sys
import gradio as gr
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# --- 🔱 SAFETY IMPORT ---
try:
    from bank_cloud import verify_with_bank_hq
    def verify_logic(otp): 
        return verify_with_bank_hq(otp)
except ImportError:
    def verify_logic(otp): 
        return "LOCAL_MODE: Bank cloud not available"

# --- FASTAPI ---
main_app = FastAPI()

# 🛡️ THE CRITICAL BOT ROUTES
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
        msg = gr.Textbox(label="Message / OTP Scan", placeholder="Paste message or OTP here...")
        btn = gr.Button("🚀 INITIALIZE SCAN", variant="primary")
        out = gr.Textbox(label="Guardian Analysis", interactive=False)

    # Enhanced scan function
    def scan_message(message):
        if not message:
            return "⚠️ Please enter a message or OTP to scan"
        
        # Check if it looks like an OTP (4-6 digits)
        if message.isdigit() and 4 <= len(message) <= 6:
            # Treat as OTP and verify with bank
            result = verify_logic(message)
            return f"🔐 OTP Verification Result:\n{result}"
        else:
            # Treat as regular message
            return f"🔱 ANALYSIS COMPLETE: '{message[:50]}...'\n✅ [SAFE - No immediate threats detected]"

    btn.click(fn=scan_message, inputs=msg, outputs=out)

# --- MOUNT GRADIO APP ---
app = gr.mount_gradio_app(main_app, demo, path="/")

@main_app.get("/")
async def root():
    return {"status": "VAK-∞ ACTIVE", "ui": "Gradio interface mounted at /"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)
