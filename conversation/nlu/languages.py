from persistence.chats import get_chat_language

def detect_language(message):
    stored_language = get_chat_language(message)
    if stored_language:
        return stored_language
    else:
        return message["language"]
