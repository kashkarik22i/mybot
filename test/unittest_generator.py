import unittest
from telebot.nlg.generator import NLG

class test_generator(unittest.TestCase):

    def test_start(self):
        self.assertEqual(NLG().make_answer("start", 0), 'Hello!')

if __name__ == '__main__':
    unittest.main()
