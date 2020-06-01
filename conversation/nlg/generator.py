from conversation.languages import code_to_name
import random

class NLG:
    """ A class that translates moves into textual responces"""
    def make_answer(self, move_obj, language, action=None):
        move = move_obj["move"]
        if move == "mood":
            return random.choice(NLG.intents_to_utterances[language][move + " " + move_obj["mood"]])
        elif move != "language" and move != "next":
            return random.choice(NLG.intents_to_utterances[language][move])
        elif "language" in move_obj:
            return self.utter_language_switch(language, move_obj["language"])
        elif action is not None:
            # super hacky just to test now
            return "\n".join([a["text"] for a in action])
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


    intents_to_utterances = {
        "en" : {
            "start" : ["Hello!", "Hi there!", "What's up?", "Nice to see you!", "Hello dear!"],
            "end" : ["Bye!", "Bye bye!", "See you!", "It was nice to talk to you.", "See you later!"],
            "mood positive" : ["Nice to hear that!", "I'm happy for you!", "Great news!"],
            "mood negative" : ["What a pity", "I'm sorry to hear that.", "So sad."],
            "mood neutral" : ["I got it", "I see", "OK"]
        },
        "ru" : {
            "start" : ["Привет!", "Здорово!", "Че каво?", "Здравствуй!", "Привет тебе!"],
            "end" : ["Пока!", "Пока пока!", "Увидимся", "Приятно было поболтать", "До скорого!"],
            "mood positive" : ["Хорошие новости!", "Я за тебя рад", "Приятно слышать"],
            "mood negative" : ["Жаль", "Увы", "Грустно", "Грустишка", "Что поделать..."],
            "mood neutral" : ["Понтяно", "Ясно", "Ок", "Угу"]
        },
        "de" : {
            "start" : ["Hallo!", "Servus", "Was geht?", "Ich freue mich", "Hallo mein Freund!"],
            "end" : ["Tschüss!", "Ciao!", "Wir sehen uns", "Auf Wiedersehen", "Bis später", "Bis dann"],
            "mood positive" : ["Wie nett!", "Gute Nachrichten!", "Toll!"],
            "mood negative" : ["Schade", "Es tut mir leid", "Ach du Arme!"],
            "mood neutral" : ["Jaha", "Jawohl", "Alles klar", "OK"]
        }
    }
