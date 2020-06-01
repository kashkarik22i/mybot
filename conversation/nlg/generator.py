class NLG:
    """ A class that translates moves into textual responces"""
    def make_answer(self, move_obj):
        move = move_obj["move"]
        if move == "start":
            return "Hello!"
        elif move == "end":
            return "Bye!"
        elif move == "mood" and move_obj["mood"] == "positive":
            return "Nice!"
        elif move == "mood" and move_obj["mood"] == "neutral":
            return "OK"
        elif move == "mood" and move_obj["mood"] == "negative":
            return "I'm sorry to hear that."
        elif "language" in move_obj:
            return "switched language setting " + move_obj["language"]
        else:
            return "Let's talk about it."
