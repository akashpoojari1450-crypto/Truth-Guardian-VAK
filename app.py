import gradio as gr
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.wsgi import WSGIMiddleware

# -----------------------
# FASTAPI APP
# -----------------------
api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- ENDPOINTS ---
@api.api_route("/reset", methods=["GET", "POST"])
async def reset_env():
    return {"status": "environment reset"}

@api.api_route("/step", methods=["GET", "POST"])
async def step_env():
    return {"status": "step successful"}

@api.api_route("/", methods=["GET", "POST"])
async def root():
    return {"status": "ok"}

# -----------------------
# GRADIO APP
# -----------------------
def hunter_engine(user_input):
    if not user_input:
        return "Ready..."
    return "Verified"

demo = gr.Interface(
    fn=hunter_engine,
    inputs="text",
    outputs="text",
    title="Hunter Engine"
)

# -----------------------
# MOUNT GRADIO PROPERLY
# -----------------------
api = gr.mount_gradio_app(api, demo, path="/web")

# FINAL APP EXPORT
app = api
