from persistence.logs import are_there_past_responses


class DialogManager:
    goodbyes = {"bye bye", "bye", "goodbye", "farewell", "ciao", "пока",
                "cu", "see u", "c u", "see you", "until later", "till later", "talk to you later"}

    def get_next_move(self, msg):
        if "intent" in msg:
            return self.move_by_intent(msg)
        msg_text = msg.get("text")
        if msg_text.endswith("start"):
            return {"move": "start"}
        elif msg_text in self.goodbyes:
            return {"move": "end"}
        elif "mood" in msg and msg.get("mood"):
            return {"move": "mood", "mood": msg.get("mood")}
        elif self.is_bot_first_message(msg["msg_obj"]) or msg["msg_obj"].get("last_move") == "initial_dialog_first_hello":
            return self.run_first_dialog(msg["msg_obj"])
        else:
            return {"move": "next"}

    @staticmethod
    def move_by_intent(msg):
        if msg["intent"] == 'hello':
            if DialogManager.is_bot_first_message(msg["msg_obj"]):
                return DialogManager.run_first_dialog(msg["msg_obj"])
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

    @staticmethod
    def run_first_dialog(msg):
        if "last_move" not in msg:
            return {"move": "initial_dialog_first_hello"}
        elif msg["last_move"] == "initial_dialog_first_hello":
            return {"move": "initial_dialog_purpose"}
        else:
            return {"move": "start"}

    @staticmethod
    def is_bot_first_message(msg):
        return not are_there_past_responses(msg)
