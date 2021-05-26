from datetime import datetime

def sample_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi","hey","你好"):
        return "Hey, how are you?"

    if user_message in ("who r u?"):
        return "I'm bot"

    return "I don't understand you"

