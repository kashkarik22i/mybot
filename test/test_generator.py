import unittest
from conversation.nlg.generator import NLG

class TestGenerator(unittest.TestCase):

    def test_start(self):
        self.assertIn(NLG().make_answer({"move": "start"}, "en"), ["Hello!", "Hi there!", "What's up?", "Nice to see you!", "Hello dear!"])

    def test_mood_positive(self):
        self.assertIn(NLG().make_answer({"move": "mood", "mood": "positive"}, "en"),  ["Nice to hear that!", "I'm happy for you!", "Great news!"])

    def test_mood_negative(self):
        self.assertIn(NLG().make_answer({"move": "mood", "mood": "negative"}, "en"), ["What a pity", "I'm sorry to hear that.", "So sad."])

    def test_mood_neutral(self):
        self.assertIn(NLG().make_answer({"move": "mood", "mood": "neutral"}, "en"), ["I got it", "I see", "OK"])

    def test_next(self):
        self.assertTrue(NLG().make_answer({"move": "next"}, "en").startswith("I am not super smart"))

if __name__ == '__main__':
    unittest.main()
