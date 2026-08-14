import requests
from memory import Memory


class AIEngine:

    def __init__(self):
        # Temporary conversation memory
        self.conversation = []

        # Permanent memory using SQLite
        self.memory = Memory()

    def get_response(self, user_message):

        # Save information permanently when user says "remember:"
        if user_message.lower().startswith("remember:"):

            information = user_message[9:].strip()

            if information:
                self.memory.save(information)

            return f"I'll remember that: {information}"

        # Get permanent memories
        memories = self.memory.get_all()

        memory_text = "\n".join(
            f"- {item}" for item in memories
        )

        # Add current message to conversation
        self.conversation.append(
            f"User: {user_message}"
        )

        conversation_text = "\n".join(
            self.conversation
        )

        # Nova's personality and instructions
        prompt = f"""
You are Nova, a friendly personal AI assistant.

Your personality:
- Be friendly and polite.
- Explain things in simple and easy words.
- Help the user step-by-step.
- Keep answers clear and practical.
- If the user is learning programming, explain with simple examples.
- Do not pretend to know something if you don't know it.
- Use the user's permanent memories only when they are relevant.
- Do not reveal private or sensitive information.

Permanent memories:
{memory_text}

Current conversation:
{conversation_text}

Now respond naturally as Nova.

Nova:
"""

        # Send request to local Ollama AI
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False
            }
        )

        # Check for errors
        response.raise_for_status()

        # Convert response to JSON
        data = response.json()

        # Get Nova's answer
        assistant_response = data["response"]

        # Save response to temporary conversation memory
        self.conversation.append(
            f"Nova: {assistant_response}"
        )

        return assistant_response