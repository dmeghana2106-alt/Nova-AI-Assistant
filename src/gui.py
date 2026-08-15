import tkinter as tk
from tkinter import scrolledtext
import threading
import subprocess
import sounddevice as sd
import speech_recognition as sr
import pyttsx3
import wave

from core.ai_engine import AIEngine
from command_router import route_command


class NovaGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Nova AI Assistant")
        self.root.geometry("900x650")
        self.root.minsize(700, 500)

        # Colors
        self.bg_color = "#1e1e1e"
        self.chat_color = "#252526"
        self.input_color = "#333333"
        self.text_color = "#ffffff"
        self.nova_color = "#4fc3f7"
        self.user_color = "#81c784"

        self.root.configure(
            bg=self.bg_color
        )

        # AI
        self.ai = AIEngine()

        # Voice
        self.recognizer = sr.Recognizer()
        self.speaker = pyttsx3.init()

        # Stores a command waiting for confirmation
        self.pending_command = None

        # ---------------- TITLE ----------------

        title = tk.Label(
            root,
            text="🤖 NOVA AI ASSISTANT",
            font=("Arial", 22, "bold"),
            bg=self.bg_color,
            fg=self.nova_color
        )

        title.pack(
            pady=(15, 5)
        )

        subtitle = tk.Label(
            root,
            text="Your personal AI assistant",
            font=("Arial", 10),
            bg=self.bg_color,
            fg="#aaaaaa"
        )

        subtitle.pack(
            pady=(0, 10)
        )

        # ---------------- CHAT AREA ----------------

        self.chat_area = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            font=("Arial", 12),
            bg=self.chat_color,
            fg=self.text_color,
            insertbackground="white",
            relief=tk.FLAT,
            padx=15,
            pady=15,
            state="disabled"
        )

        self.chat_area.pack(
            padx=20,
            pady=10,
            fill=tk.BOTH,
            expand=True
        )

        self.chat_area.tag_config(
            "nova",
            foreground=self.nova_color,
            font=("Arial", 12, "bold")
        )

        self.chat_area.tag_config(
            "user",
            foreground=self.user_color,
            font=("Arial", 12, "bold")
        )

        self.chat_area.tag_config(
            "message",
            foreground=self.text_color,
            font=("Arial", 12)
        )

        self.add_message(
            "Nova",
            "Hello! 👋\n"
            "I'm Nova, your personal AI assistant.\n"
            "How can I help you today?"
        )

        # ---------------- INPUT AREA ----------------

        input_frame = tk.Frame(
            root,
            bg=self.bg_color
        )

        input_frame.pack(
            padx=20,
            pady=(5, 10),
            fill=tk.X
        )

        # Message entry
        self.message_entry = tk.Entry(
            input_frame,
            font=("Arial", 13),
            bg=self.input_color,
            fg=self.text_color,
            insertbackground="white",
            relief=tk.FLAT
        )

        self.message_entry.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            ipady=12,
            padx=(0, 8)
        )

        self.message_entry.insert(
            0,
            "Type your message..."
        )

        self.message_entry.bind(
            "<FocusIn>",
            self.clear_placeholder
        )

        self.message_entry.bind(
            "<Return>",
            lambda event: self.send_message()
        )

        # Microphone button
        mic_button = tk.Button(
            input_frame,
            text="🎤",
            font=("Arial", 13),
            bg="#444444",
            fg="white",
            activebackground="#555555",
            relief=tk.FLAT,
            padx=15,
            pady=8,
            command=self.start_listening
        )

        mic_button.pack(
            side=tk.RIGHT,
            padx=(0, 8)
        )

        # Send button
        send_button = tk.Button(
            input_frame,
            text="SEND ➤",
            font=("Arial", 11, "bold"),
            bg=self.nova_color,
            fg="#000000",
            activebackground="#81d4fa",
            relief=tk.FLAT,
            padx=20,
            pady=10,
            command=self.send_message
        )

        send_button.pack(
            side=tk.RIGHT
        )

        # Status
        self.status = tk.Label(
            root,
            text="● Nova is ready",
            font=("Arial", 9),
            bg=self.bg_color,
            fg="#81c784"
        )

        self.status.pack(
            pady=(0, 8)
        )

    # ==================================================
    # PLACEHOLDER
    # ==================================================

    def clear_placeholder(self, event):

        if self.message_entry.get() == "Type your message...":

            self.message_entry.delete(
                0,
                tk.END
            )

    # ==================================================
    # ADD MESSAGE
    # ==================================================

    def add_message(self, sender, message):

        self.chat_area.config(
            state="normal"
        )

        if sender == "Nova":

            self.chat_area.insert(
                tk.END,
                "Nova 🤖\n",
                "nova"
            )

        else:

            self.chat_area.insert(
                tk.END,
                "You 👤\n",
                "user"
            )

        self.chat_area.insert(
            tk.END,
            message + "\n\n",
            "message"
        )

        self.chat_area.config(
            state="disabled"
        )

        self.chat_area.see(
            tk.END
        )

    # ==================================================
    # SEND MESSAGE
    # ==================================================

    def send_message(self):

        user_message = self.message_entry.get().strip()

        if not user_message:
            return

        if user_message == "Type your message...":
            return

        self.message_entry.delete(
            0,
            tk.END
        )

        self.add_message(
            "You",
            user_message
        )

        self.status.config(
            text="● Nova is thinking...",
            fg="#ffcc80"
        )

        thread = threading.Thread(
            target=self.get_response,
            args=(user_message,),
            daemon=True
        )

        thread.start()

    # ==================================================
    # GET RESPONSE
    # ==================================================

    def get_response(self, user_message):

        try:

            # ------------------------------------------
            # CHECK PENDING CONFIRMATION
            # ------------------------------------------

            if self.pending_command is not None:

                answer = user_message.lower().strip()

                if answer in [
                    "yes",
                    "yeah",
                    "y",
                    "confirm",
                    "do it",
                    "sure"
                ]:

                    command = self.pending_command

                    self.pending_command = None

                    response = self.execute_confirmed_command(
                        command
                    )

                elif answer in [
                    "no",
                    "nope",
                    "n",
                    "cancel",
                    "don't",
                    "dont"
                ]:

                    self.pending_command = None

                    response = (
                        "Okay, I cancelled that action."
                    )

                else:

                    response = (
                        "Please say YES to confirm "
                        "or NO to cancel."
                    )

                self.root.after(
                    0,
                    self.display_response,
                    response
                )

                return

            # ------------------------------------------
            # COMMAND ROUTER
            # ------------------------------------------

            command_result = route_command(
                user_message
            )

            # ------------------------------------------
            # NORMAL AI QUESTION
            # ------------------------------------------

            if command_result is None:

                response = self.ai.get_response(
                    user_message
                )

            # ------------------------------------------
            # DANGEROUS COMMAND
            # ------------------------------------------

            elif command_result["type"] == "confirmation":

                self.pending_command = (
                    command_result["command"]
                )

                response = command_result["message"]

                response += (
                    "\n\nPlease say YES to confirm "
                    "or NO to cancel."
                )

            # ------------------------------------------
            # SAFE COMMAND
            # ------------------------------------------

            else:

                response = command_result["message"]

            self.root.after(
                0,
                self.display_response,
                response
            )

        except Exception as error:

            self.root.after(
                0,
                self.display_response,
                f"Sorry, something went wrong:\n{error}"
            )

    # ==================================================
    # EXECUTE CONFIRMED COMMAND
    # ==================================================

    def execute_confirmed_command(self, command):

        command = command.lower().strip()

        # Shutdown
        if (
            "shutdown" in command
            or "shut down" in command
        ):

            subprocess.Popen(
                ["shutdown", "/s", "/t", "0"]
            )

            return "Shutting down the computer."

        # Restart
        if "restart" in command:

            subprocess.Popen(
                ["shutdown", "/r", "/t", "0"]
            )

            return "Restarting the computer."

        # Lock
        if "lock" in command:

            import ctypes

            ctypes.windll.user32.LockWorkStation()

            return "Locking the computer."

        return (
            "I couldn't perform that "
            "confirmed action."
        )

    # ==================================================
    # DISPLAY RESPONSE
    # ==================================================

    def display_response(self, response):

        self.add_message(
            "Nova",
            response
        )

        self.status.config(
            text="● Nova is ready",
            fg="#81c784"
        )

        # Speak the response
        threading.Thread(
            target=self.speak,
            args=(response,),
            daemon=True
        ).start()

    # ==================================================
    # MICROPHONE
    # ==================================================

    def start_listening(self):

        self.status.config(
            text="● Listening... 🎤",
            fg="#ffcc80"
        )

        thread = threading.Thread(
            target=self.listen,
            daemon=True
        )

        thread.start()

    # ==================================================
    # LISTEN
    # ==================================================

    def listen(self):

        try:

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

            with wave.open(
                filename,
                "wb"
            ) as audio_file:

                audio_file.setnchannels(1)
                audio_file.setsampwidth(2)
                audio_file.setframerate(sample_rate)

                audio_file.writeframes(
                    recording.tobytes()
                )

            with sr.AudioFile(filename) as source:

                audio = self.recognizer.record(
                    source
                )

            text = self.recognizer.recognize_google(
                audio
            )

            self.root.after(
                0,
                self.voice_text_received,
                text
            )

        except sr.UnknownValueError:

            self.root.after(
                0,
                self.voice_error,
                "I couldn't understand you."
            )

        except sr.RequestError:

            self.root.after(
                0,
                self.voice_error,
                "Speech recognition service is unavailable."
            )

        except Exception as error:

            self.root.after(
                0,
                self.voice_error,
                str(error)
            )

    # ==================================================
    # VOICE TEXT RECEIVED
    # ==================================================

    def voice_text_received(self, text):

        self.message_entry.delete(
            0,
            tk.END
        )

        self.message_entry.insert(
            0,
            text
        )

        self.status.config(
            text="● Voice recognized",
            fg="#81c784"
        )

        self.send_message()

    # ==================================================
    # VOICE ERROR
    # ==================================================

    def voice_error(self, message):

        self.status.config(
            text="● " + message,
            fg="#ef5350"
        )

    # ==================================================
    # SPEAK
    # ==================================================

    def speak(self, text):

        try:

            self.speaker.say(text)

            self.speaker.runAndWait()

        except Exception as error:

            print(
                "Voice error:",
                error
            )


# ======================================================
# START APPLICATION
# ======================================================

def main():

    root = tk.Tk()

    NovaGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()