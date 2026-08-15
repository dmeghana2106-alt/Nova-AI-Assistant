from commands import handle_command


def route_command(user_input):
    """
    Decide whether the user's message
    is a computer command or a normal AI question.
    """

    response = handle_command(user_input)

    if response is not None:
        return response

    return None