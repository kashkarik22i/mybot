from persistence.domain import save_mood

class DialogManager:
    goodbyes = {"bye bye","bye", "goodbye", "farewell", "ciao","cu", "see u", "c u", "see you", "until later", "till later", "talk to you later"}

    def get_next_move(self, msg):
        if "intent" in msg and msg["intent"] == 'hello':
            return "start"
        if "intent" in msg and msg["intent"] == 'language':
            lang = msg["slots"][0][1]
            return "language" +  lang
        msg_text = msg.get("text")
        if msg_text.endswith("start"):
            return "start"
        elif msg_text.lower() in DialogManager.goodbyes:
            return "end"
        elif msg.get("mood"):
            self.save_mood_to_db(msg["msg_obj"], msg.get("mood"))
            return "mood" + msg.get("mood")
        else:
            return "next"

    def save_mood_to_db(self, msg_obj, mood):
        save_mood(msg_obj, mood)
