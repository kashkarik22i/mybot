from persistence.settings import save_chat_language
from persistence.domain import save_mood
from persistence.domain import get_moods_for_week

def act_on_move(message, move):
    if "language" in move and move["language"]:
        lang = move["language"]
        save_chat_language(message=message, language=lang)
        return None
    if "mood" in move and move["mood"]:
        save_mood(message, move["mood"])
        return None
    if "get_mood" in move and move["get_mood"]:
        return get_moods_for_week(message)


