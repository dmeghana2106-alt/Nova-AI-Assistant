import subprocess
import sounddevice as sd
import speech_recognition as sr
import pyttsx3
import wave

from core.ai_engine import AIEngine


# ---------------- VOICE SETUP ----------------

recognizer = sr.Recognizer()
speaker = pyttsx3.init()


def speak(text):
    print("Nova:", text)
    speaker.say(text)
    speaker.runAndWait()


def listen():
    print("\n🎤 Listening... Speak now!")

    sample_rate = 16000
    duration = 5

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    filename = "voice_input.wav"

    with wave.open(filename, "wb") as audio_file:
        audio_file.setnchannels(1)
        audio_file.setsampwidth(2)
        audio_file.setframerate(sample_rate)
        audio_file.writeframes(recording.tobytes())

    try:
        with sr.AudioFile(filename) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)

        print("You:", text)
        return text

    except sr.UnknownValueError:
        print("Nova: Sorry, I couldn't understand you.")
        return ""

    except sr.RequestError:
        print("Nova: Speech recognition service is unavailable.")
        return ""


# ---------------- COMPUTER COMMANDS ----------------

def handle_command(user_input):

    command = user_input.lower().strip()

    # Calculator
    if "calculator" in command or "calc" in command:
        subprocess.Popen(["calc.exe"])
        return "Opening Calculator."

    # Notepad
    if "notepad" in command:
        subprocess.Popen(["notepad.exe"])
        return "Opening Notepad."

    # Chrome
    if "chrome" in command or "google chrome" in command:
        subprocess.Popen(["cmd", "/c", "start", "chrome"])
        return "Opening Chrome."

    # VS Code
    if "vs code" in command or "visual studio code" in command:
        subprocess.Popen(["cmd", "/c", "start", "code"])
        return "Opening VS Code."

    return None


# ---------------- NOVA ----------------

def main():

    nova = AIEngine()

    speak("Hello! I am Nova. I am ready.")

    print("\n🤖 NOVA AI ASSISTANT")
    print("--------------------")
    print("Press ENTER to speak.")
    print("Say 'bye' to exit.\n")

    while True:

        input("👉 Press ENTER and speak...")

        user_input = listen()

        if not user_input:
            continue

        if user_input.lower().strip() == "bye":
            speak("Goodbye! Have a great day.")
            break

        command_response = handle_command(user_input)

        if command_response is not None:
            speak(command_response)

        else:
            try:
                response = nova.get_response(user_input)
                speak(response)

            except Exception as error:
                print("Error:", error)
                speak("Sorry, something went wrong.")


if __name__ == "__main__":
    main()