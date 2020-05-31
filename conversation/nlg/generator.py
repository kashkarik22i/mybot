class NLG:
    """ A class that translates moves into textual responces"""
    def make_answer(self, move):
        if move == "start":
            return "Hello!"
        elif move == "end":
            return "Bye!"
        elif move == "mood":
            return "So that's how you're feeling..."
        else:
            return "Nice! =)"
