from persistence.chats import save_chat_language

def act_on_move(message, move):
    if "language" not in move:
        return
    lang = move["language"]
    if lang is None:
        return
    save_chat_language(message=message, language=lang)

