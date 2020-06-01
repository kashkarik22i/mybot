from conversation.languages import code_to_name

class NLG:
    """ A class that translates moves into textual responces"""
    def make_answer(self, move_obj, language):
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
            return self.utter_language_switch(language, move_obj["language"])
        else:
            return "I am not super smart, I did't not understand you. But you can always ask me to explain what I can and cannot do for you"

    # this simple bullshit can be fully implemented in dialogflow without this ugly hacky code
    def utter_language_switch(self, language, new_language):
        if language == "en":
            return "i will switch to {language} now".format(language=code_to_name(language, new_language))
        if language == "ru":
            return "меняю язык на {language}".format(language=code_to_name(language, new_language))
        if language == "de":
            return "jetzt werde ich {language} sprechen".format(language=code_to_name(language, new_language))
