import subprocess
import webbrowser
from datetime import datetime
import os
import urllib.parse
import ctypes


def handle_command(user_input):

    command = user_input.lower().strip()

    # ---------------- APPLICATIONS ----------------

    if "calculator" in command or "calc" in command:
        subprocess.Popen(["calc.exe"])
        return "Opening Calculator."

    if "notepad" in command:
        subprocess.Popen(["notepad.exe"])
        return "Opening Notepad."

    if "chrome" in command:
        subprocess.Popen(["cmd", "/c", "start", "chrome"])
        return "Opening Chrome."

    # ---------------- FILE EXPLORER ----------------

    if "file explorer" in command or command == "explorer":
        subprocess.Popen(["explorer.exe"])
        return "Opening File Explorer."

    if "downloads" in command:
        downloads = os.path.join(
            os.path.expanduser("~"),
            "Downloads"
        )

        subprocess.Popen(
            ["explorer.exe", downloads]
        )

        return "Opening Downloads."

    if "desktop" in command:
        desktop = os.path.join(
            os.path.expanduser("~"),
            "Desktop"
        )

        subprocess.Popen(
            ["explorer.exe", desktop]
        )

        return "Opening Desktop."

    if "documents" in command:
        documents = os.path.join(
            os.path.expanduser("~"),
            "Documents"
        )

        subprocess.Popen(
            ["explorer.exe", documents]
        )

        return "Opening Documents."

    # ---------------- WEBSITES ----------------

    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    if "open gmail" in command:
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail."

    # ---------------- GOOGLE SEARCH ----------------

    if command.startswith("search google for "):

        query = command.replace(
            "search google for ",
            "",
            1
        ).strip()

        if query:

            encoded_query = urllib.parse.quote_plus(
                query
            )

            webbrowser.open(
                "https://www.google.com/search?q="
                + encoded_query
            )

            return f"Searching Google for {query}."

    # ---------------- TIME ----------------

    if "what time is it" in command:

        current_time = datetime.now().strftime(
            "%I:%M %p"
        )

        return f"The current time is {current_time}."

    # ---------------- DATE ----------------

    if (
        "what is today's date" in command
        or "what is the date" in command
    ):

        current_date = datetime.now().strftime(
            "%d %B %Y"
        )

        return f"Today's date is {current_date}."
        # ---------------- WINDOWS SETTINGS ----------------

    if "open settings" in command:
        subprocess.Popen(["cmd", "/c", "start", "ms-settings:"])
        return "Opening Windows Settings."

    # ---------------- LOCK COMPUTER ----------------

    if "lock computer" in command or "lock my computer" in command:
        ctypes.windll.user32.LockWorkStation()
        return "Locking your computer."

    # ---------------- SHUTDOWN ----------------

    if "shutdown computer" in command or "shut down computer" in command:
        return "I won't shut down your computer automatically yet."

    return None