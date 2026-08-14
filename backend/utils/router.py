from backend.skills.commands import execute_command
from backend.ai.brain import ask_ragnar

def process_request(user_text):
    """
    Decides whether the request is a local command
    or should be answered by the AI.
    """

    command_result = execute_command(user_text)

    if command_result:
        return command_result

    return ask_ragnar(user_text)