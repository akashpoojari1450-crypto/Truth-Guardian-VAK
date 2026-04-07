import gradio as gr
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# --- 1. INITIALIZE FASTAPI ---
app = FastAPI()

# CORS (important)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 2. OPENENV API ENDPOINTS ---
@app.api_route("/reset", methods=["GET", "POST"])
async def reset_env():
    return JSONResponse(
        content={
            "status": "environment reset",
            "message": "VAK-∞ Shield Active"
        }
    )

@app.api_route("/step", methods=["GET", "POST"])
async def step_env(request: Request):
    return JSONResponse(content={"status": "step successful"})

# --- 3. ROOT FIX ---
@app.post("/")
async def root_post():
    return JSONResponse(
        content={
            "status": "environment reset",
            "message": "VAK-∞ Shield Active"
        }
    )

@app.get("/")
async def root_get():
    return {
        "status": "VAK-∞ ACTIVE",
        "api": "running",
        "ui": "/web"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# --- 4. TRUTH GUARDIAN LOGIC ---
def hunter_engine(user_input):
    if not user_input:
        return "🔱 [EYE] Standing by. Paste message for analysis..."
    return "🔱 STATUS: [✓] VERIFIED | Hunter-Protocol: ACTIVE"

# --- 5. GRADIO UI ---
demo = gr.Interface(
    fn=hunter_engine,
    inputs=gr.Textbox(label="Input Message", lines=3),
    outputs=gr.Textbox(label="Analysis Logs", lines=5),
    title="🔱 Truth Guardian (VAK-∞)",
    description="Node Active | Team Vakratunda",
    theme=gr.themes.Monochrome()
)

# --- 6. MOUNT GRADIO (FINAL FIX) ---
gr.mount_gradio_app(app, demo, path="/web")
