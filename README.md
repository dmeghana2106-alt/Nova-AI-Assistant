# Nova AI Assistant

Nova is a full-stack AI voice assistant built with Python, React, FastAPI, and a locally running LLM through Ollama.

The project combines conversational AI, voice input/output, conversation memory, safety handling, and a web-based frontend into one assistant application.

## Features

- AI-powered conversational assistant
- Local LLM integration using Ollama
- Voice input using SpeechRecognition
- Voice output using text-to-speech
- Conversation memory
- Command routing
- Safety handling
- React-based web frontend
- Python backend
- Automated testing with pytest
- Modular project structure

## Tech Stack

### Backend
- Python
- FastAPI
- Ollama
- Llama 3.2
- SpeechRecognition
- Text-to-Speech

### Frontend
- React
- JavaScript
- Vite
- CSS

### Testing
- Pytest

### Development Tools
- Git
- GitHub
- VS Code

## Project Architecture

```text
Nova-AI-Assistant/
│
├── frontend/
│   ├── public/
│   ├── src/
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
│   ├── __init__.py
│   └── test_assistant.py
│
├── docs/
│   └── TESTING.md
│
├── requirements.txt
├── .gitignore
└── README.md