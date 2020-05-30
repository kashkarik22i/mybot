import unittest
from conversation.dialog.dialogmanager import DialogManager

class test_dialogmanager(unittest.TestCase):

    def test_get_next_move_goodbye(self):
        test_msg = {"text" : "bye bye", "mood" : ""}
        self.assertEqual(DialogManager().get_next_move(test_msg), "end")


    def test_get_next_move_start(self):
        test_msg = {"text" : "sssstart", "mood" : ""}
        self.assertEqual(DialogManager().get_next_move(test_msg), "start")


    def test_get_next_move_mood(self):
        test_msg = {"text" : "I'm fine", "mood" : "positive"}
        self.assertEqual(DialogManager().get_next_move(test_msg), "mood")

if __name__ == '__main__':
    unittest.main()
