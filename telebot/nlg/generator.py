class NLG:
    """ A class that translates moves into textual responces"""
    def make_answer(self, move, chat_id):
        if move == "start":
            return "Hello!"
        elif move == "end":
            return "Bye!"
        else:
            return "Nice! =)"
