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
        moods = get_moods_for_week(message)
        return _compute_percentage(moods)


def _compute_percentage(moods):
    positive = sum([1 for m in moods if m["mood"] == "positive"])
    negative = sum([1 for m in moods if m["mood"] == "negative"])
    neutral = sum([1 for m in moods if m["mood"] == "neutral"])
    total = positive + negative + neutral
    if total == 0:
        return {"positive": 0, "negative": 0}
    pos_percent = int((100 * positive) / total)
    neg_percent = int((100 * negative) / total)
    return {"positive": pos_percent, "negative": neg_percent}



