import unittest
from conversation.nlu.analyzer import NLU

class TestLanguages(unittest.TestCase):

    def test_detect_ru_ignores_ok(self):
        message = {"text": "я думаю все тока началось", "ignore_dialogflow": True}
        self.assertEqual(NLU().parse(message, "ru")["mood"], "")

    def test_detect_ru_good(self):
        message = {"text": "я думаю все зашибись", "ignore_dialogflow": True}
        self.assertEqual(NLU().parse(message, "ru")["mood"], "positive")

    def test_detect_ru_bad(self):
        message = {"text": "жизнь говно", "ignore_dialogflow": True}
        self.assertEqual(NLU().parse(message, "ru")["mood"], "negative")

    def test_detect_en_good(self):
        message = {"text": "i feel great", "ignore_dialogflow": True}
        self.assertEqual(NLU().parse(message, "en")["mood"], "positive")

    def test_detect_en_bad(self):
        message = {"text": "i feel bad", "ignore_dialogflow": True}
        self.assertEqual(NLU().parse(message, "en")["mood"], "negative")

if __name__ == '__main__':
    unittest.main()
