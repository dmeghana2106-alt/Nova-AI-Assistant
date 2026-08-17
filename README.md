# Nova AI Assistant

Nova is a full-stack AI voice assistant built with **Python, React, FastAPI, and a locally running LLM using Ollama**.

The project combines conversational AI, voice interaction, conversation memory, command routing, safety handling, and a web-based interface into a single assistant application.

## Key Features

* AI-powered conversational assistant
* Local LLM integration using Ollama
* Llama 3.2 model support
* Voice input using SpeechRecognition
* Text-to-speech voice output
* Conversation memory
* Command routing
* Safety handling
* FastAPI backend
* React-based frontend
* REST API communication
* Automated testing with pytest
* Modular project architecture

## System Architecture

```text
User
 │
 ▼
React Frontend
 │
 │ HTTP Request
 ▼
FastAPI Backend
 │
 ├── Command Router
 │
 ├── Conversation Memory
 │
 ├── Safety Layer
 │
 └── AI Engine
       │
       ▼
    Ollama
       │
       ▼
   Llama 3.2
       │
       ▼
  AI Response
       │
       ▼
React Frontend
```

## Tech Stack

### Backend

* Python
* FastAPI
* Ollama
* Llama 3.2
* SpeechRecognition
* Text-to-Speech

### Frontend

* React
* JavaScript
* Vite
* CSS

### Testing

* Pytest

### Development Tools

* Git
* GitHub
* VS Code

## Project Structure

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
│   │
│   ├── core/
│   │   └── ai_engine.py
│   │
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
```

## How It Works

1. The user interacts with Nova through the React frontend.
2. The frontend sends the user's request to the FastAPI backend.
3. The backend processes the request through the command-routing and safety layers.
4. Conversation memory provides relevant previous context.
5. The AI engine communicates with the locally running Ollama model.
6. Llama 3.2 generates the response.
7. The response is returned through the FastAPI API.
8. The React frontend displays the response to the user.
9. Voice functionality can be used for speech input and audio output.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/dmeghana2106-alt/Nova-AI-Assistant.git
cd Nova-AI-Assistant
```

### 2. Create a Python Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Install Ollama on your system and make sure it is running.

Then download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

Verify the model:

```bash
ollama list
```

### 5. Start the Backend

From the project directory:

```bash
uvicorn src.main:app --reload
```

The FastAPI backend should be available at:

```text
http://127.0.0.1:8000
```

### 6. Start the Frontend

Open another terminal:

```powershell
cd frontend
npm install
npm run dev
```

Vite will provide the local frontend URL in the terminal.

## API

Nova uses FastAPI to provide communication between the frontend and AI backend.

The backend can also be inspected through FastAPI's interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Testing

The project uses pytest for automated testing.

Run:

```bash
pytest
```

Current test result:

```text
2 passed
```

The project currently has automated tests covering core assistant functionality.

## Safety

Nova includes a dedicated safety layer to help control and validate assistant behavior before processing certain requests.

This allows safety-related logic to remain separated from the main AI engine and makes the project easier to maintain and extend.

## Engineering Highlights

This project demonstrates practical experience with:

* Full-stack application development
* REST API development using FastAPI
* React frontend development
* Local LLM integration
* AI application architecture
* Voice-enabled applications
* Conversation state and memory
* Modular Python development
* Automated testing
* Git and GitHub version control

## Future Improvements

Planned improvements include:

* Persistent database-backed conversation memory
* Authentication and user accounts
* Streaming LLM responses
* Improved voice recognition
* Advanced command execution
* Docker containerization
* Cloud deployment
* More comprehensive automated testing
* Production monitoring and logging

## Project Status

**Status: Working Prototype**

The core assistant, frontend, backend, local LLM integration, voice functionality, and automated testing are implemented.

## Author

**Akshith Koutilya**

GitHub: [Akshithkoutilya](https://github.com/Akshithkoutilya)
