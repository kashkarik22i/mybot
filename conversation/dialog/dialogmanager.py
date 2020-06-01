class DialogManager:
    goodbyes = {"bye bye","bye", "goodbye", "farewell", "ciao","cu", "see u", "c u", "see you", "until later", "till later", "talk to you later"}

    def get_next_move(self, msg):
        if "intent" in msg and msg["intent"] == 'hello':
            return {"move": "start"}
        if "intent" in msg and msg["intent"] == 'language':
            lang = msg["slots"][0][1]
            return {"move": "language", "language": lang}
        msg_text = msg.get("text")
        if msg_text.endswith("start"):
            return {"move": "start"}
        elif msg_text.lower() in DialogManager.goodbyes:
            return {"move": "end"}
        elif "mood" in msg and msg.get("mood"):
            return {"move": "mood", "mood": msg.get("mood")}
        else:
            return {"move": "next"}

