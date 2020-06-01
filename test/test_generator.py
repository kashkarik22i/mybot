import unittest
from conversation.nlg.generator import NLG

class TestGenerator(unittest.TestCase):

    def test_start(self):
        self.assertEqual(NLG().make_answer({"move": "start"}, "en"), 'Hello!')


    def test_mood_positive(self):
        self.assertEqual(NLG().make_answer({"move": "mood", "mood": "positive"}, "en"), 'Nice!')

    def test_mood_negative(self):
        self.assertEqual(NLG().make_answer({"move": "mood", "mood": "negative"}, "en"), "I'm sorry to hear that.")

    def test_mood_neutral(self):
        self.assertEqual(NLG().make_answer({"move": "mood", "mood": "neutral"}, "en"), 'OK')

    def test_next(self):
        self.assertEqual(NLG().make_answer("next"), "Let's talk about it.")

if __name__ == '__main__':
    unittest.main()
