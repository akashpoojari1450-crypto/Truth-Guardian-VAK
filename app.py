from fastapi import FastAPI

app = FastAPI()

@app.api_route("/reset", methods=["GET", "POST"])
async def reset():
    return {"status": "reset ok"}

@app.api_route("/step", methods=["GET", "POST"])
async def step():
    return {"status": "step ok"}

@app.api_route("/", methods=["GET", "POST"])
async def root():
    return {"status": "ok"}
