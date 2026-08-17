from voice import listen
from speak import speak
import json
import urllib.request


def ask_nova(user_message: str) -> str:
    url = "http://localhost:11434/api/chat"

    data = {
        "model": "llama3.2",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are Nova, a helpful personal AI assistant. "
                    "Be friendly, concise, and useful. "
                    "If you do not know something, say so honestly."
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
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode("utf-8"))

    return result["message"]["content"]


if __name__ == "__main__":
    print("Nova AI Assistant started.")
    print("Type 'exit' to stop Nova.")

    while True:
        user_input = listen()
        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Nova: Goodbye!")
            break

        try:
            answer = ask_nova(user_input)
            speak(answer)

        except Exception as error:
            print(f"Nova error: {error}")