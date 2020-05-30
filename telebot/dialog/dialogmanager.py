class DialogManager:
    goodbyes = {"bye bye","bye", "goodbye", "farewell", "ciao","cu", "see u", "c u", "see you", "until later", "till later", "talk to you later"}

    def get_next_move(self, msg):
        if "intent" in msg and msg["intent"] == 'hello':
            return "start"
        msg_text = msg.get("text")
        if msg_text.endswith("start"):
            return "start"
        elif msg_text.lower() in DialogManager.goodbyes:
            return "end"
        elif len(msg.get("mood")) > 0:
            self.save_mood_to_db(msg.get("mood"))
            return "next"
        else:
            return "next"


    def save_mood_to_db(self, mood):
        return
