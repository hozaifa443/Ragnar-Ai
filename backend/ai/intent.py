import re

def get_intent(text):

    text = text.lower()

    if any(word in text for word in ["open", "start", "launch"]):
        return "open"

    elif any(word in text for word in ["remember", "save"]):
        return "remember"

    elif any(word in text for word in ["search", "google"]):
        return "search"

    elif any(word in text for word in ["shutdown"]):
        return "shutdown"

    elif any(word in text for word in ["lock"]):
        return "lock"

    else:
        return "chat"