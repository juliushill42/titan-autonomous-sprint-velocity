from fastapi import FastAPI
from agent import Agent37
app = FastAPI(title="Autonomous-Sprint-Velocity")
agent = Agent37()

@app.post("/execute")
async def execute(payload: dict):
    return agent.execute(payload)
