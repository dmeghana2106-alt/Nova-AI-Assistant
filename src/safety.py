DANGEROUS_COMMANDS = {
    "shutdown",
    "restart",
    "delete",
    "format",
    "lock",
    "test confirmation",
}


def is_dangerous(command):

    command = command.lower().strip()

    for dangerous_word in DANGEROUS_COMMANDS:

        if dangerous_word in command:
            return True

    return False


def confirmation_message(command):

    command = command.lower().strip()

    if "test confirmation" in command:
        return (
            "🧪 Confirmation test requested.\n"
            "Do you want Nova to continue?"
        )

    if "shutdown" in command:
        return (
            "⚠️ Shutdown requested.\n"
            "Are you sure you want to shut down "
            "the computer?"
        )

    if "restart" in command:
        return (
            "⚠️ Restart requested.\n"
            "Are you sure you want to restart "
            "the computer?"
        )

    if "delete" in command:
        return (
            "⚠️ Delete action requested.\n"
            "Are you sure you want to delete something?"
        )

    if "format" in command:
        return (
            "⚠️ Format action requested.\n"
            "Are you sure you want to format something?"
        )

    if "lock" in command:
        return (
            "⚠️ Lock action requested.\n"
            "Are you sure you want to lock the computer?"
        )

    return (
        "⚠️ This action requires confirmation.\n"
        "Do you want Nova to continue?"
    )