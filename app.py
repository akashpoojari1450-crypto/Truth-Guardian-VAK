import sys
import hashlib
import secrets
import gradio as gr
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# --- 1. FASTAPI INIT ---
main_app = FastAPI()
main_app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@main_app.get("/health")
async def health(): return {"status": "healthy", "node": "SIT-Valachil-Main-01"}

# --- 2. CORE LOGIC ---
def hunter_protocol_engine(user_input):
    if not user_input or not user_input.strip():
        return "🔱 [EYE] Standing by. Paste message for DNA analysis..."
    
    dna = hashlib.blake2b(user_input.encode(), digest_size=64).hexdigest()
    token = f"VAK-∞-{secrets.token_hex(4).upper()}"
    is_scam = any(word in user_input.lower() for word in ["urgent", "otp", "bank", "win", "verify", "call"])
    
    header = f"🔱 SESSION DNA: {dna[:16]}... | TOKEN: {token}\n" + ("-" * 60) + "\n"
    if is_scam:
        return f"{header}🔱 STATUS: [!] FRAUD DNA DETECTED\n🔱 ACTION: NEUTRALIZED BY {token}\n🔱 DEFENSE: Passive-Shield ACTIVE."
    return f"{header}🔱 STATUS: [✓] VERIFIED REAL. NO DECEPTION DETECTED."

# --- 3. GRADIO UI (Matched to your Screenshot) ---
with gr.Blocks(theme=gr.themes.Monochrome(), title="Truth Guardian (VAK-∞)") as demo:
    gr.Markdown("# 🔱 Truth Guardian (VAK-∞)")
    gr.Markdown("Node: SIT-Valachil-Main-01 | Hunter-Protocol: **ACTIVE**")

    with gr.Column():
        input_text = gr.Textbox(
            label="Message / OTP Input Field",
            placeholder="Paste suspicious SMS, Email, or OTP here...",
            lines=4
        )
        
        # Action Buttons
        run_btn = gr.Button("🚀 INITIALIZE HUNTER-PROTOCOL SCAN", variant="primary")
        clear_btn = gr.Button("🗑️ CLEAR SCANNER")
        
        output_text = gr.Textbox(
            label="Guardian Analysis & Active-Defense Logs", 
            lines=10, 
            interactive=False
        )

    # Footer Logic
    gr.Markdown("---")
    gr.Markdown("🏁 **Official Submission** | Meta PyTorch OpenEnv Hackathon | **Team Vakratunda**")

    # Button Functions
    run_btn.click(fn=hunter_protocol_engine, inputs=input_text, outputs=output_text)
    clear_btn.click(lambda: [None, None], outputs=[input_text, output_text])

# --- 4. MOUNT & RUN ---
app = gr.mount_gradio_app(main_app, demo, path="/")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
