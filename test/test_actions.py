import unittest
from conversation import actions


class TestActions(unittest.TestCase):

    def test_compute_percentage_positive(self):
        moods = [{"mood": "positive"}, {"mood": "positive"}, {"mood": "positive"}]
        out = actions._compute_percentage(moods)
        self.assertEqual(out["positive"], 100)
        self.assertEqual(out["negative"], 0)

    def test_compute_percentage_mixes(self):
        moods = [{"mood": "positive"}, {"mood": "negative"}]
        out = actions._compute_percentage(moods)
        self.assertEqual(out["positive"], 50)
        self.assertEqual(out["negative"], 50)

    def test_compute_percentage_negative(self):
        moods = [{"mood": "negative"}, {"mood": "negative"}]
        out = actions._compute_percentage(moods)
        self.assertEqual(out["positive"], 0)
        self.assertEqual(out["negative"], 100)

    def test_compute_percentage_nothing(self):
        moods = []
        out = actions._compute_percentage(moods)
        self.assertEqual(out["positive"], 0)
        self.assertEqual(out["positive"], 0)
