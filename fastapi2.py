from fastapi.middleware.cors import CORSMiddleware
from llminference import (
    llm_inference,
)  # Assuming llminference is defined in this module

# create the FastAPI app
from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/summarize")
async def summarizewithllm(request: Request):
    data = await request.json()
    text = data.get("text", "")
    text = llm_inference(text)
    response = {
        "summary": text,  # Placeholder summary logic
    }
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ],  # Django dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
