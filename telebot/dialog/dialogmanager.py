class DialogManager:
    def get_next_move(self, msg_obj):
        msg, intent, score = msg_obj
        if score > 0.9 and intent == 'hello':
            return "start"
        goodbyes = {"bye", "goodbye", "farewell", "ciao", "see you", "until later", "talk to you later"}
        if msg.endswith("start"):
            return "start"
        elif msg.lower() in set({v.lower() : v for v in goodbyes}.values()):
            return "end"
        else:
            return "next"
