from persistence.chats import save_chat_language

def act_on_move(message, move):
    if "language" not in move:
        return
    language = move.lstrip("language ")
    save_chat_language(message=message, language=language)



