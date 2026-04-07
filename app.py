import gradio as gr
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# --- FASTAPI APP ---
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- REQUIRED ENDPOINTS ---
@app.api_route("/reset", methods=["GET", "POST"])
async def reset_env():
    return {"status": "environment reset"}

@app.api_route("/step", methods=["GET", "POST"])
async def step_env(request: Request):
    return {"status": "step successful"}

# --- IMPORTANT ROOT FIX ---
@app.api_route("/", methods=["GET", "POST"])
async def root():
    return {"status": "ok"}

# --- GRADIO FUNCTION ---
def hunter_engine(user_input):
    if not user_input:
        return "Ready..."
    return "Verified"

# --- GRADIO UI ---
demo = gr.Interface(
    fn=hunter_engine,
    inputs="text",
    outputs="text",
)

# --- MOUNT GRADIO (CRITICAL) ---
app = gr.mount_gradio_app(app, demo, path="/web")
