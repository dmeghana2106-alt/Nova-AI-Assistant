from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import urllib.request

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Nova backend is running"}


@app.post("/ask")
def ask(data: dict):
    user_message = data.get("message", "")

    url = "http://localhost:11434/api/chat"

    payload = {
        "model": "llama3.2",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are Nova, a helpful personal AI assistant. "
                    "Be friendly, concise, and useful."
                ),
            },
            {
                "role": "user",
                "content": user_message,
            },
        ],
        "stream": False,
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode("utf-8"))

    return {
        "response": result["message"]["content"]
    }