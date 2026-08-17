# Nova AI Assistant

Nova is a full-stack AI voice assistant built using Python, FastAPI, React, Ollama, and Llama 3.2.

It supports natural-language conversations, voice input, voice output, conversation memory, and a web-based user interface.

## Features

- AI-powered conversations using Llama 3.2
- Voice input using browser speech recognition
- Voice output using text-to-speech
- Conversation memory using SQLite
- React-based web interface
- Python backend
- FastAPI API integration
- Safety handling for assistant responses
- Automated testing
- Modular project architecture

## Technology Stack

### Frontend

- React
- Vite
- JavaScript
- HTML
- CSS

### Backend

- Python
- FastAPI
- Uvicorn
- SQLite

### AI

- Ollama
- Llama 3.2

### Development

- Git
- GitHub
- Pytest

## Project Architecture

```text
nova-ai-assistant/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── src/
│   ├── assistant.py
│   ├── command_router.py
│   ├── commands.py
│   ├── gui.py
│   ├── main.py
│   ├── memory.py
│   ├── safety.py
│   ├── speak.py
│   ├── voice.py
│   ├── voice_output.py
│   ├── core/
│   │   └── ai_engine.py
│   └── utils/
│       └── config.py
│
├── tests/
│   └── test_assistant.py
│
├── docs/
│   └── TESTING.md
│
├── requirements.txt
├── .gitignore
└── README.md