class DialogManager:
    def get_next_move(self, msg):
        goodbyes = {"bye", "goodbye", "farewell", "ciao", "see you", "until later", "talk to you later"}
        if msg.endswith("start"):
            return "start"
        elif msg.lower() in set({v.lower() : v for v in goodbyes}.values()):
            return "end"
        else:
            return "next"
