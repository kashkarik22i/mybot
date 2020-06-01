from persistence.chats import get_chat_language

def detect_language(message):
    stored_language = get_chat_language(message)
    if stored_language:
        print("using saved language {}".format(stored_language))
        return stored_language
    else:
        print("using language as in user settings {}".format(message["language"]))
        return message["language"]


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

def name_to_code(language):
    language = language.casefold()
    if language == 'russian':
        return "ru"
    elif language == 'russisch':
        return "ru"
    elif language == 'ru':
        return "ru"
    elif language == 'русский':
        return "ru"
    elif language == 'по-русски':
        return "ru"
    elif language == 'по русски':
        return "ru"
    if language == 'english':
        return "en"
    elif language == 'englisch':
        return "en"
    elif language == 'englischem':
        return "en"
    elif language == 'en':
        return "en"
    elif language == 'английский':
        return "en"
    elif language == 'по-английски':
        return "en"
    elif language == 'по английски':
        return "en"
    if language == 'german':
        return "de"
    elif language == 'de':
        return "de"
    elif language == 'deutsch':
        return "de"
    elif language == 'немецкий':
        return "de"
    elif language == 'по-немецки':
        return "de"
    elif language == 'по немецки':
        return "de"
    else:
        return None
