import unittest
from conversation.nlg.generator import NLG


class TestGenerator(unittest.TestCase):

    def test_start(self):
        self.assertIn(NLG().make_answer({"move": "start"}, "en"),
                      ["Hello!", "Hi there!", "What's up?", "Nice to see you!", "Hello dear!"])

    def test_mood_positive(self):
        self.assertIn(NLG().make_answer({"move": "mood", "mood": "positive"}, "en"),
                      ["Nice to hear that!", "I'm happy for you!", "Great news!"])

    def test_mood_negative(self):
        self.assertIn(NLG().make_answer({"move": "mood", "mood": "negative"}, "en"),
                      ["What a pity", "I'm sorry to hear that.", "So sad."])

    def test_mood_neutral(self):
        self.assertIn(NLG().make_answer({"move": "mood", "mood": "neutral"}, "en"), ["I got it", "I see", "OK"])

    def test_next(self):
        self.assertIn(NLG().make_answer({"move": "next"}, "en"), ["I am not super smart, I did't not understand you. "
                                                                  "But you can always ask me to explain what I can "
                                                                  "and cannot do for you",
                                                                  "I dod not understand you this time", "sorry, what?"])

    def test_get_mood_none(self):
        answer = NLG().make_answer({"move": "get_mood"}, "en", {"positive": 0, "negative": 0})
        self.assertIn(answer, ["Sorry, you don't remember you telling me anything"])

    def test_get_mood_some(self):
        answer = NLG().make_answer({"move": "get_mood"}, "en", {"positive": 50, "negative": 50})
        self.assertIn(answer, ["From what you've told me you mood was 50% positive and 50% negative"])


if __name__ == '__main__':
    unittest.main()
