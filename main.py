from fastapi import FastAPI
from pydantic import BaseModel
from agent import run_agent

app = FastAPI()

class Query(BaseModel):
    prompt:str

@app.post("/ask")
async def ask(data: Query):

    result = await run_agent(
        data.prompt
    )

    return {
        "success":True,
        "answer":result
    }