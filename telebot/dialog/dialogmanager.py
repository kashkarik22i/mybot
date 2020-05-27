class DialogManager:
    def get_next_move(self, msg):
        goodbyes = {"bye", "goodbye", "farewell", "ciao", "see you", "until later", "talk to you later"}
        msg_text = msg.get("text")
        if msg_text.endswith("start"):
            return "start"
        elif msg_text.lower() in set({v.lower() : v for v in goodbyes}.values()):
            return "end"
        elif len(msg.get("mood")) > 0:
            self.save_mood_to_db(msg.get("mood"))
            return "next"
        else:
            return "next"


    def save_mood_to_db(self, mood):
        return
