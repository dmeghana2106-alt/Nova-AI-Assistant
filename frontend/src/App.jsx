import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [isListening, setIsListening] = useState(false);

  const startListening = () => {
  const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

  if (!SpeechRecognition) {
    alert("Speech recognition is not supported.");
    return;
  }

  const recognition = new SpeechRecognition();

  recognition.lang = "en-US";

  recognition.onstart = () => {
    setIsListening(true);
  };

  recognition.onresult = (event) => {
    const spokenText = event.results[0][0].transcript;
    setMessage(spokenText);
  };

  recognition.onend = () => {
    setIsListening(false);
  };

  recognition.start();
};

  

  const sendMessage = async () => {
    if (message.trim() === "") return;

    const newMessage = {
      sender: "user",
      text: message,
    };
  

    setMessages((prev) => [...prev, newMessage]);
    setMessage("");

    try {
  const response = await fetch("http://localhost:8000/ask", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message: newMessage.text,
    }),
  });

  const data = await response.json();

  setMessages((prev) => [
    ...prev,
    {
      sender: "nova",
      text: data.response,
    },
  ]);
} catch (error) {
  setMessages((prev) => [
    ...prev,
    {
      sender: "nova",
      text: "Sorry, I could not connect to my AI backend.",
    },
  ]);
}
  };

  return (
    <div className="nova-app">
      <header className="nova-header">
        <div className="nova-logo">N</div>

        <div>
          <h1>Nova</h1>
          <p>AI Assistant</p>
        </div>

        <div className="status">
          <span></span> Online
        </div>
      </header>

      <main className="chat-area">
        {messages.length === 0 ? (
          <div className="welcome">
            <div className="nova-orb">✦</div>
            <h2>Hello, I'm Nova</h2>
            <p>Your intelligent AI assistant.</p>
          </div>
        ) : (
          <div className="messages">
            {messages.map((msg, index) => (
              <div
                key={index}
                className={`message ${msg.sender}`}
              >
                <div className="message-name">
                  {msg.sender === "user" ? "You" : "Nova"}
                </div>

                <div className="message-text">
                  {msg.text}
                </div>
              </div>
            ))}
          </div>
        )}
      </main>

      <div className="input-area">
       <button
  className={`mic-button ${isListening ? "listening" : ""}`}
  onClick={startListening}
>
  {isListening ? "🔴" : "🎤"}
</button>

        <input
          type="text"
          placeholder="Ask Nova anything..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              sendMessage();
            }
          }}
        />

        <button
          className="send-button"
          onClick={sendMessage}
        >
          ➤
        </button>
      </div>
    </div>
  );
}

export default App;