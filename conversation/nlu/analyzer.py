import os.path

from conversation.external.dflow import detect_intent_texts
from conversation.languages import name_to_code


class NLU:
    def parse(self, msg_obj, language):
        # Ilya made this super ugly:)
        msg = msg_obj["text"]
        if "ignore_dialogflow" not in msg_obj: # hack for testing for now
            intent_data = detect_intent_texts(msg, language)
            intent = intent_data["intent"]
            score = intent_data["score"]
            slots = intent_data["slots"]
            if intent == "language":
                slots = self.convert_language(slots=slots)
            if score > 0.65 and not intent == "Default Fallback Intent":
                # start using logger soon
                print("using dialogflow: got intent {} and score {}".format(intent, score))
                return {"text": self.preprocess(msg),
                        "msg_obj": msg_obj,
                        "intent": intent,
                        "slots": slots}
            else:
                print("NOT using dialogflow: got intent {} and score {}".format(intent, score))
        print("NOT using dialogflow")
        return {"text": self.preprocess(msg), "mood" : self.parse_mood(msg, language), "msg_obj": msg_obj}

    def parse_mood(self, msg_text:str, language:str):
        mood_markers =  {
            "en" : ["i'm", "i am", "i feel", "i don't feel","it does not feel", "it doesn't feel", "it feels"],
            "de" : ["ich bin", "ich fühle", "mir geht"],
            "ru" : ["мне", "я", "зашибись"]
        }
        is_mood = any([x in msg_text.casefold() for x in mood_markers[language]])
        if is_mood:
            matched = [x for x in [" not ", " no ", " don't ", " doesn't ", " nicht ", " kein ", " keine ", " не "] if x in msg_text.casefold()]
            is_negated =  any(matched)
            for feeling in ["positive", "negative", "neutral"]:
                if (self.is_feeling(msg_text, feeling) and not is_negated):
                    return feeling
                elif is_negated and feeling == "positive":
                    return "negative"
                elif is_negated and feeling == "negative":
                    return "positive"
        return ""

    def is_feeling(self, msg_text, feeling):
        file_path = os.path.join(os.path.dirname(__file__), '..','resources', feeling)
        print (file_path)
        with open(file_path) as f:
            result = [x.strip() for x in f.readlines()]
        print(result)
        matching_words = [x for x in result if x in msg_text.casefold()]
        print("found matching words")
        print(matching_words)
        return any(matching_words)

    def preprocess(self, msg:str):
        return msg

    def convert_language(self, slots):
         return [(slot[0], name_to_code(slot[1])) for slot in slots]
