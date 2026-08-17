from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import urllib.request
import sqlite3

app = FastAPI()

# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# DATABASE
# --------------------------------------------------

DATABASE = "nova_memory.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_database():
    connection = get_db_connection()

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()


create_database()


# --------------------------------------------------
# SYSTEM PROMPT
# --------------------------------------------------

SYSTEM_PROMPT = (
    "You are Nova, a helpful personal AI assistant. "
    "Be friendly, concise, and useful. "
    "Remember the conversation and use previous messages "
    "when answering the user."
)


# --------------------------------------------------
# HOME
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Nova backend is running"
    }


# --------------------------------------------------
# ASK NOVA
# --------------------------------------------------

@app.post("/ask")
def ask(data: dict):

    user_message = data.get("message", "").strip()

    if not user_message:
        return {
            "response": "Please enter a message."
        }

    connection = get_db_connection()

    # Get previous conversation
    rows = connection.execute(
        """
        SELECT role, content
        FROM conversations
        ORDER BY id ASC
        """
    ).fetchall()

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    # Add previous conversation
    for row in rows:
        messages.append(
            {
                "role": row["role"],
                "content": row["content"]
            }
        )

    # Add current user message
    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    # Save user message
    connection.execute(
        """
        INSERT INTO conversations (role, content)
        VALUES (?, ?)
        """,
        ("user", user_message)
    )

    connection.commit()

    connection.close()

    # --------------------------------------------------
    # SEND TO OLLAMA
    # --------------------------------------------------

    url = "http://localhost:11434/api/chat"

    payload = {
        "model": "llama3.2",
        "messages": messages,
        "stream": False
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:

        with urllib.request.urlopen(request) as response:

            result = json.loads(
                response.read().decode("utf-8")
            )

        answer = result["message"]["content"]

    except Exception as error:

        return {
            "response": f"Nova backend error: {error}"
        }


    # --------------------------------------------------
    # SAVE NOVA RESPONSE
    # --------------------------------------------------

    connection = get_db_connection()

    connection.execute(
        """
        INSERT INTO conversations (role, content)
        VALUES (?, ?)
        """,
        ("assistant", answer)
    )

    connection.commit()

    connection.close()


    return {
        "response": answer
    }


# --------------------------------------------------
# CLEAR CONVERSATION
# --------------------------------------------------

@app.post("/clear")
def clear_conversation():

    connection = get_db_connection()

    connection.execute(
        "DELETE FROM conversations"
    )

    connection.commit()

    connection.close()

    return {
        "message": "New conversation started."
    }