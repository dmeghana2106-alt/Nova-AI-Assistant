import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def speak(text):
    print("Nova:", text)
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("Hello! I am Nova, your AI assistant.")