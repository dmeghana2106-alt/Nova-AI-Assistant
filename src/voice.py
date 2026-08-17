import speech_recognition as sr


def listen() -> str:
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Nova is listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You: {text}")
        return text

    except sr.UnknownValueError:
        print("Nova: Sorry, I couldn't understand.")
        return ""

    except sr.RequestError as error:
        print(f"Nova voice error: {error}")
        return ""