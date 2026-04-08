import sys
import os
import gradio as gr
from fastapi import FastAPI

# --- FASTAPI SETUP ---
main_app = FastAPI()

@main_app.get("/health")
async def health(): 
    return {"status": "healthy", "node": "SIT-Valachil-01"}

# --- GRADIO UI ---
with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
    gr.Markdown("# 🔱 Truth Guardian (VAK-∞)")
    gr.Markdown("Status: **ACTIVE**")
    input_box = gr.Textbox(label="Message Scan")
    output_box = gr.Textbox(label="Result")
    gr.Button("SCAN").click(fn=lambda x: f"Verified: {x}", inputs=input_box, outputs=output_box)

# Mount Gradio to FastAPI
app = gr.mount_gradio_app(main_app, demo, path="/")

if __name__ == "__main__":
    import uvicorn
    # MUST BE 7860
    uvicorn.run(app, host="0.0.0.0", port=7860)
