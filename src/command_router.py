from commands import handle_command
from safety import is_dangerous, confirmation_message


def route_command(user_input):
    """
    Decide whether the user's message is:
    1. A normal computer command
    2. A dangerous command requiring confirmation
    3. Not a command at all
    """

    # Check for dangerous commands first
    if is_dangerous(user_input):

        return {
            "type": "confirmation",
            "message": confirmation_message(user_input),
            "command": user_input
        }

    # Check normal commands
    response = handle_command(user_input)

    if response is not None:

        return {
            "type": "command",
            "message": response
        }

    # Not a computer command
    return None