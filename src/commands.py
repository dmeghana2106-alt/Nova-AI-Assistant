import subprocess
import webbrowser
from datetime import datetime
import os
import urllib.parse
import ctypes


def handle_command(user_input):

    # Convert the user's message to lowercase
    command = user_input.lower().strip()

    # Remove common natural-language words
    words_to_remove = [
        "nova",
        "please",
        "can you",
        "could you",
        "would you",
        "will you",
        "i want you to",
        "i need you to",
        "for me",
        "my",
    ]

    for word in words_to_remove:
        command = command.replace(word, "")

    command = command.strip()

    # ==================================================
    # APPLICATIONS
    # ==================================================

    # Calculator
    if any(word in command for word in [
        "calculator",
        "calc",
        "calculate"
    ]):

        subprocess.Popen(["calc.exe"])

        return "Opening Calculator."

    # Notepad
    if any(word in command for word in [
        "notepad",
        "text editor"
    ]):

        subprocess.Popen(["notepad.exe"])

        return "Opening Notepad."

    # Chrome
    if any(word in command for word in [
        "chrome",
        "browser"
    ]):

        subprocess.Popen(
            ["cmd", "/c", "start", "chrome"]
        )

        return "Opening Chrome."

    # ==================================================
    # FILE EXPLORER
    # ==================================================

    if any(word in command for word in [
        "file explorer",
        "explorer",
        "open my files",
        "show my files",
        "my files"
    ]):

        subprocess.Popen(["explorer.exe"])

        return "Opening File Explorer."

    # ==================================================
    # DOWNLOADS
    # ==================================================

    if "downloads" in command or "download folder" in command:

        downloads = os.path.join(
            os.path.expanduser("~"),
            "Downloads"
        )

        subprocess.Popen(
            ["explorer.exe", downloads]
        )

        return "Opening Downloads."

    # ==================================================
    # DESKTOP
    # ==================================================

    if "desktop" in command:

        desktop = os.path.join(
            os.path.expanduser("~"),
            "Desktop"
        )

        subprocess.Popen(
            ["explorer.exe", desktop]
        )

        return "Opening Desktop."

    # ==================================================
    # DOCUMENTS
    # ==================================================

    if "documents" in command or "documents folder" in command:

        documents = os.path.join(
            os.path.expanduser("~"),
            "Documents"
        )

        subprocess.Popen(
            ["explorer.exe", documents]
        )

        return "Opening Documents."

    # ==================================================
    # WEBSITES
    # ==================================================

    if (
        "youtube" in command
        or "go to youtube" in command
        or "open youtube" in command
        or "launch youtube" in command
    ):
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    if (
        "gmail" in command
        or "go to gmail" in command
        or "open gmail" in command
        or "launch gmail" in command
    ):
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail."

    if (
        command == "google"
        or "open google" in command
        or "go to google" in command
        or "launch google" in command
    ):
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    # ==================================================
    # GOOGLE SEARCH
    # ==================================================

    search_phrases = [
        "search google for",
        "search google",
        "search for",
        "google",
        "look up",
        "find information about",
        "search",
    ]

    for phrase in search_phrases:

        if phrase in command:

            query = command.split(
                phrase,
                1
            )[1].strip()

            # Remove unnecessary words
            query = query.replace(
                "on google",
                ""
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

    # ==================================================
    # TIME
    # ==================================================

    if (
        "what time is it" in command
        or "current time" in command
        or command == "time"
    ):

        current_time = datetime.now().strftime(
            "%I:%M %p"
        )

        return f"The current time is {current_time}."

    # ==================================================
    # DATE
    # ==================================================

    if (
        "what is today's date" in command
        or "what is the date" in command
        or "today's date" in command
        or command == "date"
    ):

        current_date = datetime.now().strftime(
            "%d %B %Y"
        )

        return f"Today's date is {current_date}."

    # ==================================================
    # WINDOWS SETTINGS
    # ==================================================

    if "open settings" in command or command == "settings":

        subprocess.Popen(
            ["cmd", "/c", "start", "ms-settings:"]
        )

        return "Opening Windows Settings."

    # ==================================================
    # LOCK COMPUTER
    # ==================================================

    if (
        "lock computer" in command
        or "lock my computer" in command
        or command == "lock"
    ):

        ctypes.windll.user32.LockWorkStation()

        return "Locking your computer."

    # ==================================================
    # SHUTDOWN
    # ==================================================

    if (
        "shutdown computer" in command
        or "shut down computer" in command
    ):

        return "I won't shut down your computer automatically yet."

    # ==================================================
    # NO COMMAND FOUND
    # ==================================================

    return None