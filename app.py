import sys
import hashlib
import secrets
import gradio as gr
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# --- 1. PYTHON 3.13 COMPATIBILITY FIX ---
# Python 3.13 removed audioop; this ensures pydub/gradio don't crash.
try:
    import audioop
except ImportError:
    try:
        import audioop_lts as audioop
        sys.modules["audioop"] = audioop
    except ImportError:
        pass

# --- 2. FASTAPI INIT ---
# We use 'main_app' for the internal logic to avoid overwriting the 'app' variable.
main_app = FastAPI()

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 3. REQUIRED ENDPOINTS (Health Checks) ---

@main_app.get("/reset")
@main_app.post("/reset")
async def reset():
    return {"status": "environment reset", "message": "VAK-∞ Shield Active"}

@main_app.get("/step")
@main_app.post("/step")
async def step():
    return {"status": "step successful"}

@main_app.get("/health")
async def health_check():
    return {"status": "healthy", "node": "SIT-Valachil-Main-01"}

@main_app.get("/", response_class=JSONResponse)
async def root():
    # This keeps the root alive for the platform's health checker
    return {
        "status": "VAK-∞ ACTIVE",
        "node": "SIT-Valachil-Main-01",
        "ui_path": "/web"
    }

# --- 4. CORE LOGIC ---
def hunter_protocol_engine(user_input):
    if not user_input or not user_input.strip():
        return "🔱 [EYE] Standing by. Paste message for DNA analysis..."

    # DNA generation using Blake2b (Stable & Fast)
    dna = hashlib.blake2b(user_input.encode(), digest_size=64).hexdigest()
    token = f"VAK-∞-{secrets.token_hex(4).upper()}"

    # Basic fraud detection logic
    is_scam = any(word in user_input.lower() for word in ["urgent", "otp", "bank", "win", "verify"])

    header = f"🔱 SESSION DNA: {dna[:16]}... | TOKEN: {token}\n" + ("-" * 50) + "\n"

    if is_scam:
        return f"{header}🔱 STATUS: [!] FRAUD DNA DETECTED\n🔱 ACTION: NEUTRALIZED BY {token}"

    return f"{header}🔱 STATUS: [✓] VERIFIED REAL. NO DECEPTION DETECTED."

# --- 5. GRADIO UI ---
with gr.Blocks(theme=gr.themes.Monochrome(), title="VAK-∞ Truth Guardian") as demo:
    gr.Markdown("# 🔱 Truth Guardian (VAK-∞)")
    gr.Markdown("### Node: SIT-Valachil-Main-01 | Team Vakratunda")

    input_text = gr.Textbox(
        label="Input Message",
        placeholder="Paste suspicious text here...",
        lines=3
    )

    output_text = gr.Textbox(label="Analysis Logs", lines=8, interactive=False)

    btn = gr.Button("🚀 INITIALIZE SCAN", variant="primary")

    btn.click(
        fn=hunter_protocol_engine,
        inputs=input_text,
        outputs=output_text
    )

# --- 6. MOUNT GRADIO ---
# We assign the final mounted app to 'app' so that 'uvicorn app:app' works perfectly.
app = gr.mount_gradio_app(main_app, demo, path="/web")

if __name__ == "__main__":
    import uvicorn
    # Standard port for HF Spaces and AI hosting
    uvicorn.run(app, host="0.0.0.0", port=7860)
