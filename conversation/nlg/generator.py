class NLG:
    """ A class that translates moves into textual responces"""
    def make_answer(self, move):
        if move == "start":
            return "Hello!"
        elif move == "end":
            return "Bye!"
        elif move == "mood positive":
            return "Nice!"
        elif move == "mood neutral":
            return "OK"
        elif move == "mood negative":
            return "I'm sorry to hear that."
        elif "language" in move:
            return "switched language setting"
        else:
            return "Nice! =)"
