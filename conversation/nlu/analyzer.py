from conversation.external.dflow import detect_intent_texts

class NLU:
    def parse(self, msg_obj):
        # Ilya made this super ugly:)
        msg = msg_obj["text"]
        language = msg_obj["language"]
        if "ignore_dialogflow" not in msg_obj: # hack for testing for now
            intent_data = detect_intent_texts(msg, language)
            intent = intent_data["intent"]
            score = intent_data["score"]
            if score > 0.9:
                # start using logger soon
                print("using dialogflow: got intent {} and score {}".format(intent, score))
                return {"text": self.preprocess(msg), "mood" : self.parse_mood(msg), "intent": intent}
            else:
                print("NOT using dialogflow: got intent {} and score {}".format(intent, score))
        print("NOT using dialogflow")
        return {"text": self.preprocess(msg), "mood" : self.parse_mood(msg)}

    def parse_mood(self, msg:str):
        mood_markers = ["i'm", "i am", "i feel", "it feels like"]
        is_mood = any([x in msg.casefold() for x in mood_markers])
        if is_mood:
            is_negated =  any([x in msg.casefold() for x in ["not", "no", "don't"]])
            for feeling in ["positive", "negative", "neutral"]:
                if (self.is_feeling(msg, feeling) and not is_negated):
                    return feeling
                elif is_negated and feeling == "positive":
                    return "negative"
                elif is_negated and feeling == "negative":
                    return "positive"
        return ""

    def is_feeling(self, msg, feeling):
        with open("/resources/"+feeling) as f:
            result = [x.strip() for x in f.readlines()]
        return any([x in msg.casefold() for x in result])

    def preprocess(self, msg:str):
        return msg
