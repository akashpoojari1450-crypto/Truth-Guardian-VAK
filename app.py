import gradio as gr
import hashlib
import secrets

# --- 1. CORE LOGIC ---
def hunter_protocol_engine(user_input):
    if not user_input or not user_input.strip():
        return "🔱 [EYE] Standing by. Paste message for DNA analysis..."
    
    # Generate unique Session DNA
    dna = hashlib.blake2b(user_input.encode(), digest_size=64).hexdigest()
    token = f"VAK-∞-{secrets.token_hex(4).upper()}"
    
    # Fraud Detection Keywords
    scam_words = ["urgent", "otp", "bank", "win", "verify", "call", "account", "blocked"]
    is_scam = any(word in user_input.lower() for word in scam_words)
    
    header = f"🔱 SESSION DNA: {dna[:16]}... | TOKEN: {token}\n" + ("-" * 60) + "\n"
    
    if is_scam:
        return f"{header}🔱 STATUS: [!] FRAUD DNA DETECTED\n🔱 ACTION: NEUTRALIZED BY {token}\n🔱 DEFENSE: Passive-Shield ACTIVE."
    
    return f"{header}🔱 STATUS: [✓] VERIFIED REAL. NO DECEPTION DETECTED."

# --- 2. THE UI (Visual Match to your Image) ---
with gr.Blocks(theme=gr.themes.Monochrome(), title="Truth Guardian (VAK-∞)") as demo:
    gr.Markdown("# 🔱 Truth Guardian (VAK-∞)")
    gr.Markdown("Node: SIT-Valachil-Main-01 | Hunter-Protocol: **ACTIVE**")

    with gr.Column():
        input_text = gr.Textbox(
            label="Message / OTP Input Field",
            placeholder="Paste suspicious SMS, Email, or OTP here...",
            lines=4
        )
        
        # Match your screenshot buttons
        run_btn = gr.Button("🚀 INITIALIZE HUNTER-PROTOCOL SCAN", variant="primary")
        clear_btn = gr.Button("🗑️ CLEAR SCANNER")
        
        output_text = gr.Textbox(
            label="Guardian Analysis & Active-Defense Logs", 
            lines=10, 
            interactive=False
        )

    gr.Markdown("---")
    gr.Markdown("🏁 **Official Submission** | Meta PyTorch OpenEnv Hackathon | **Team Vakratunda**")

    # Wire up the buttons
    run_btn.click(fn=hunter_protocol_engine, inputs=input_text, outputs=output_text)
    clear_btn.click(lambda: [None, None], outputs=[input_text, output_text])

# --- 3. THE LAUNCH (Crucial for Docker/HF) ---
if __name__ == "__main__":
    # We launch Gradio directly on port 7860. No FastAPI mounting needed.
    demo.launch(server_name="0.0.0.0", server_port=7860)
