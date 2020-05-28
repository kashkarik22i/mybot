from telebot.external.dflow import detect_intent_texts

LANGUAGE = "en_US"

class NLU:

    def parse(self, msg):
        intent, score = detect_intent_texts(msg, LANGUAGE)
        return [msg, intent, score] # need to use proper upjects later


    def tokenize(self, msg):
        return msg.replace(".", "").split()
