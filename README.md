# Nova AI Assistant

Nova is a full-stack AI voice assistant built with Python, React, and a local Large Language Model.

The project combines voice interaction, conversational memory, AI responses, safety controls, and a web-based interface into one personal AI assistant.

## Features

- AI-powered conversational assistant
- Voice input using speech recognition
- Voice output using text-to-speech
- Conversational memory
- Safety and command handling
- Local AI inference using Ollama
- React-based web interface
- Python backend
- Automated testing
- Modular project architecture

## Tech Stack

### Frontend
- React
- Vite
- JavaScript
- CSS

### Backend
- Python
- FastAPI
- Uvicorn

### AI
- Ollama
- Llama 3.2

### Testing
- Pytest

### Development Tools
- Git
- GitHub
- VS Code

## Project Structure

```text
Nova-AI-Assistant/
│
├── frontend/              # React frontend
│
├── src/                   # Python backend and assistant modules
│   ├── assistant.py
│   ├── command_router.py
│   ├── commands.py
│   ├── core/
│   │   └── ai_engine.py
│   ├── gui.py
│   ├── main.py
│   ├── memory.py
│   ├── safety.py
│   ├── speak.py
│   ├── voice.py
│   ├── voice_output.py
│   └── utils/
│       └── config.py
│
├── tests/                 # Automated tests
│   └── test_assistant.py
│
├── docs/                  # Project documentation
│   └── TESTING.md
│
├── requirements.txt
├── .gitignore
└── README.md