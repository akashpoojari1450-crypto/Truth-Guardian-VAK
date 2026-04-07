import requests

def reset():
    # This tells the bot the reset was successful
    return {"status": "environment reset", "message": "VAK-∞ Shield Active"}

def step(action):
    # This tells the bot the environment moved forward
    return {"status": "step successful"}

if __name__ == "__main__":
    print(reset())
