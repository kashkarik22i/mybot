import unittest
from conversation.nlg.generator import NLG

class TestGenerator(unittest.TestCase):

    def test_start(self):
        self.assertEqual(NLG().make_answer("start"), 'Hello!')


    def test_mood_positive(self):
        self.assertEqual(NLG().make_answer("mood positive"), 'Nice!')

    def test_mood_negative(self):
        self.assertEqual(NLG().make_answer("mood negative"), "I'm sorry to hear that.")

    def test_mood_neutral(self):
        self.assertEqual(NLG().make_answer("mood neutral"), 'OK')

if __name__ == '__main__':
    unittest.main()
