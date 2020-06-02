from persistence.settings import get_chat_language

def detect_language(message):
    stored_language = get_chat_language(message)
    if stored_language:
        print("using saved language {}".format(stored_language))
        result = stored_language
    else:
        print("using language as in user settings {}".format(message["language"]))
        result = message["language"]
    message["language"] = result
    return result


def code_to_name(language, code):
    if language == 'ru':
        if code == 'ru':
            return "русский"
        if code == 'en':
            return "английский"
        if code == 'de':
            return "немецкий"
    if language == 'en':
        if code == 'ru':
            return "russian"
        if code == 'en':
            return "english"
        if code == 'de':
            return "german"
    if language == 'de':
        if code == 'ru':
            return "russisch"
        if code == 'en':
            return "englisch"
        if code == 'de':
            return "deutsch"
    return None


