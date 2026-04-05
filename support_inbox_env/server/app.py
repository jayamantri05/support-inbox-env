from fastapi import FastAPI
from env.env import SupportInboxEnv
from env.models import Action
import uvicorn

app = FastAPI()
env = SupportInboxEnv()

@app.post("/reset")
async def reset():
    return await env.reset()

@app.post("/step")
async def step(action: Action):
    return await env.step(action)

@app.get("/state")
def state():
    return env.state()


# ✅ REQUIRED FOR OPENENV
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)


# ✅ GOOD PRACTICE
if __name__ == "__main__":
    main()