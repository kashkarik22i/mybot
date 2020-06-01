from persistence.chats import save_chat_language
from persistence.domain import save_mood

def act_on_move(message, move):
    if "language" in move and move["language"]:
        lang = move["language"]
        save_chat_language(message=message, language=lang)
    if "mood" in move and move["mood"]:
        save_mood(message, move["mood"])

