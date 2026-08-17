import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [isListening, setIsListening] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  // Start a completely new conversation
  const clearConversation = async () => {
    try {
      await fetch("http://localhost:8000/clear", {
        method: "POST",
      });

      setMessages([]);
      setMessage("");

      window.speechSynthesis.cancel();
    } catch (error) {
      console.error("Could not clear conversation:", error);
    }
  };

  // Voice input
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

  // Send message to Nova
  const sendMessage = async () => {
    if (message.trim() === "" || isLoading) return;

    const newMessage = {
      sender: "user",
      text: message,
    };

    setMessages((prev) => [...prev, newMessage]);
    setMessage("");
    setIsLoading(true);

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

      if (!response.ok) {
        throw new Error("Backend request failed");
      }

      const data = await response.json();

      setMessages((prev) => [
        ...prev,
        {
          sender: "nova",
          text: data.response,
        },
      ]);

      // Make Nova speak
      const speech = new SpeechSynthesisUtterance(data.response);
      speech.lang = "en-US";
      speech.rate = 1;
      speech.pitch = 1;

      window.speechSynthesis.cancel();
      window.speechSynthesis.speak(speech);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          sender: "nova",
          text: "Sorry, I could not connect to my AI backend.",
        },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="nova-app">

      {/* Header */}
      <header className="nova-header">

        <div className="nova-logo">
          N
        </div>

        <div>
          <h1>Nova</h1>
          <p>AI Assistant</p>
        </div>

        <div className="status">
          <span></span> Online
        </div>

        <button
          className="clear-button"
          onClick={clearConversation}
        >
          Clear
        </button>

      </header>


      {/* Chat Area */}
      <main className="chat-area">

        {messages.length === 0 ? (

          <div className="welcome">

            <div className="nova-orb">
              ✦
            </div>

            <h2>
              Hello, I'm Nova
            </h2>

            <p>
              Your intelligent AI assistant.
            </p>

          </div>

        ) : (

          <div className="messages">

            {messages.map((msg, index) => (

              <div
                key={index}
                className={`message ${msg.sender}`}
              >

                <div className="message-name">
                  {msg.sender === "user"
                    ? "You"
                    : "Nova"}
                </div>

                <div className="message-text">
                  {msg.text}
                </div>

              </div>

            ))}

            {isLoading && (
              <div className="message nova">

                <div className="message-name">
                  Nova
                </div>

                <div className="message-text">
                  Thinking...
                </div>

              </div>
            )}

          </div>

        )}

      </main>


      {/* Input Area */}
      <div className="input-area">

        <button
          className={`mic-button ${
            isListening ? "listening" : ""
          }`}
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
          disabled={isLoading}
        >
          ➤
        </button>

      </div>

    </div>
  );
}

export default App;