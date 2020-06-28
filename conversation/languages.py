from persistence.settings import get_chat_language


def detect_language(message):
    stored_language = get_chat_language(message)
    if stored_language:
        print("using saved language {}".format(stored_language))
        result = stored_language
    else:
        print("using language as in user settings {}".format(message["language"]))
        result = message["language"]
    if result is None:
        result = 'en'  # no better choice yet, need to autodetect later
    return result



