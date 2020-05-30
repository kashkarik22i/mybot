import unittest
from conversation.nlg.generator import NLG

class TestGenerator(unittest.TestCase):

    def test_start(self):
        self.assertEqual(NLG().make_answer("start"), 'Hello!')

if __name__ == '__main__':
    unittest.main()
