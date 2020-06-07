class DialogManager:
    goodbyes = {"bye bye","bye", "goodbye", "farewell", "ciao","cu", "see u", "c u", "see you", "until later", "till later", "talk to you later"}

    def get_next_move(self, msg):
        if "intent" in msg:
            return DialogManager.move_by_intent(msg)
        msg_text = msg.get("text")
        if msg_text.endswith("start"):
            return {"move": "start"}
        elif msg_text in DialogManager.goodbyes:
            return {"move": "end"}
        elif "mood" in msg and msg.get("mood"):
            return {"move": "mood", "mood": msg.get("mood")}
        elif DialogManager.is_bot_first_message(msg) or msg["lat_move" == "initial_dialog_first_hello"]:
            return DialogManager.run_first_dialog(msg)
        else:
            return {"move": "next"}



    def move_by_intent(self, msg):
        if "intent" not in msg:
            print("No intent! Cannot move by intent cos there is no intent!")
            return None
        elif msg["intent"] == 'hello':
            return {"move": "start"}
        elif msg["intent"] == 'latest':
            return {"move": "get_mood", "get_mood": "non-empty"}
        elif msg["intent"] == 'help':
            return {"move": "help"}
        elif msg["intent"] == 'language':
            lang = msg["slots"][0][1]
            return {"move": "language", "language": lang}
        elif msg["intent"] == 'get_mood':
            return {"move": 'get_mood', "get_mood": "week"}
        print("Unknown intent {intent}".format(intent=msg["intent"]))
        return None


    def run_first_dialog(self, msg):

        if "last_move" not in msg:
            return {"move" : "initial_dialog_first_hello"}
        elif msg["last_move"] == "initial_dialog_first_hello":
            return {"move" : "initial_dialog_purpose"}
        else:
            return None

    def is_bot_first_message(self, msg):
        return True
