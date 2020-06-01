from conversation.external.dflow import detect_intent_texts
import os.path

class NLU:
    def parse(self, msg_obj, language):
        # Ilya made this super ugly:)
        msg = msg_obj["text"]
        if "ignore_dialogflow" not in msg_obj: # hack for testing for now
            intent_data = detect_intent_texts(msg, language)
            intent = intent_data["intent"]
            score = intent_data["score"]
            slots = intent_data["slots"]
            if score > 0.9:
                # start using logger soon
                print("using dialogflow: got intent {} and score {}".format(intent, score))
                return {"text": self.preprocess(msg),
                        "mood" : self.parse_mood(msg),
                        "msg_obj": msg_obj,
                        "intent": intent,
                        "slots": slots}
            else:
                print("NOT using dialogflow: got intent {} and score {}".format(intent, score))
        print("NOT using dialogflow")
        return {"text": self.preprocess(msg), "mood" : self.parse_mood(msg), "msg_obj": msg_obj}

    def parse_mood(self, msg_text:str):
        mood_markers = ["i'm", "i am", "i feel", "it feels like"]
        is_mood = any([x in msg_text.casefold() for x in mood_markers])
        if is_mood:
            is_negated =  any([x in msg_text.casefold() for x in ["not", "no", "don't"]])
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
        return any([x in msg_text.casefold() for x in result])

    def preprocess(self, msg:str):
        return msg
