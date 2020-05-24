class NLU:

    def parse(self, msg):
        return msg


    def tokenize(self, msg):
        return msg.replace(".", "").split()
