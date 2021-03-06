import random


class NLG:
    """ A class that translates moves into textual responses"""

    def make_answer(self, move_obj, language, action=None):
        if action is None:
            action = {}
        move = move_obj["move"]
        if move == "get_mood":
            if action["positive"] == 0 and action["negative"] == 0:
                return random.choice(NLG.intents_to_utterances[language]["get_mood_nothing"]).format(**action)
            return random.choice(NLG.intents_to_utterances[language][move]).format(**action)
        elif move == "mood":
            return random.choice(NLG.intents_to_utterances[language][move + " " + move_obj["mood"]])
        elif "language" in move_obj:
            return random.choice(NLG.intents_to_utterances[language][move]).format(
                language=code_to_name(language, move_obj["language"]))
        elif move in self.intents_to_utterances[language]:
            return random.choice(NLG.intents_to_utterances[language][move]).format(**action)
        else:
            return random.choice(NLG.intents_to_utterances[language]["default"]).format(**action)

    intents_to_utterances = {
        "en": {
            "start": ["Hello!", "Hi there!", "What's up?", "Nice to see you!", "Hello dear!"],
            "end": ["Bye!", "Bye bye!", "See you!", "It was nice to talk to you.", "See you later!"],
            "mood positive": ["Nice to hear that!", "I'm happy for you!", "Great news!"],
            "mood negative": ["What a pity", "I'm sorry to hear that.", "So sad."],
            "mood neutral": ["I got it", "I see", "OK"],
            "language": ["I will switch to {language} now"],
            "get_mood": ["From what you've told me you mood was {positive}% positive and {negative}% negative"],
            "get_mood_nothing": ["Sorry, you don't remember you telling me anything"],
            "help": ["Sure, you can tell me how you feel now and ask how you felt lately"],
            "default": ["I am not super smart, I did't not understand you. But you can always ask me to explain what "
                        "I can and cannot do for you",
                        "I did not understand you this time", "sorry, what?"],
            "initial_dialog_first_hello": ["Oh hello! :) Let's begin. What is you name?",
                                           "Hello there! Let's start. What should I call you?",
                                           "Hello and welcome! What's your name?"],
            "initial_dialog_purpose": [
                "Nice to meet you! I'm Moody. I can understand emotions and will remember all that you tell me. How "
                "do you think you will use me?"]
        },
        "ru": {
            "start": ["Привет!", "Здорово!", "Че каво?", "Здравствуй!", "Привет тебе!"],
            "end": ["Пока!", "Пока пока!", "Увидимся", "Приятно было поболтать", "До скорого!"],
            "mood positive": ["Хорошие новости!", "Я за тебя рад", "Приятно слышать"],
            "mood negative": ["Жаль", "Увы", "Грустно", "Грустишка", "Что поделать..."],
            "mood neutral": ["Понтяно", "Ясно", "Ок", "Угу"],
            "language": ["Меняю язык на {language}"],
            "get_mood": ["На сколько я помню {positive}% времени настроение было хорошее и {negative}% плохое"],
            "get_mood_nothing": ["Прости, у меня пока недостаточно информации чтобы судить",
                                 "Сложно сказать, мы пока мало говорили"],
            "help": [
                "Tы можешь мне рассказать как себя чувствуешь и что тебя беспокоит а потом спросить что тебя "
                "беспокоило последнее время"],
            "default": ["Я не понял, повтори по-другому", "Или я глупый или ты хочешь что-то чего я не умею",
                        "Я не понял, ты всегда можешь спросить у меня что я умею а что нет"],
            "initial_dialog_first_hello": ["Приветик :) Давай начнем. Как тебя зовут?",
                                           "Привет! Для начала скажи мне, как тебя зовут",
                                           "Привет, добро пожаловать! Как мне тебя называть?"],
            "initial_dialog_purpose": [
                "А я Псих. Приятно познакомиться. Я немного разбираюсь в человеческих чувствах, а еще я запомню все, "
                "что ты мне скажешь. Как думаешь, как я тебе буду полезен?"]
        },
        "de": {
            "start": ["Hallo!", "Servus", "Was geht?", "Ich freue mich", "Hallo mein Freund!"],
            "end": ["Tschüss!", "Ciao!", "Wir sehen uns", "Auf Wiedersehen", "Bis später", "Bis dann"],
            "mood positive": ["Wie nett!", "Gute Nachrichten!", "Toll!"],
            "mood negative": ["Schade", "Es tut mir leid", "Ach du Arme!"],
            "language": ["Ich werde jetzt {language} sprechen"],
            "mood neutral": ["Jaha", "Jawohl", "Alles klar", "OK"],
            "get_mood": ["Du warst {positive}% gut gelaunt and {negative}% schlecht gelaunt"],
            "get_mood_nothing": ["Entschuldige, ich have noch nicht genug Daten"],
            "help": ["Naturlich, sag mir was dir storst oder frag nach dine laune letzte Woche"],
            "default": ["Entschuldige, ich habe dich nicht verstanden",
                        "Leider, habe ich nicht verstanden, oder ich kann es nicht machen",
                        "Manchmal verstehe ich dich nicht, kanns du es umformulieren"],
            "initial_dialog_first_hello": ["Hallo :) Lassen uns anfangen. Wie heisst du?"],
            "initial_dialog_purpose": [
                "Und ich bin Spinn. Nett, dich kennenzulernen. Ich verstehe etwas von Emotionen und dazu kann ich mir "
                "auch merken alles, was du sagst. Wie kann ich dir helfen?"]
        }
    }


def code_to_name(language, code):
    if language == 'ru':
        if code == 'ru':
            return "русский"
        if code == 'en':
            return "английский"
        if code == 'de':
            return "немецкий"
    if language == 'en':
        if code == 'ru':
            return "russian"
        if code == 'en':
            return "english"
        if code == 'de':
            return "german"
    if language == 'de':
        if code == 'ru':
            return "russisch"
        if code == 'en':
            return "englisch"
        if code == 'de':
            return "deutsch"
    return None
