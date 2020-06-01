import unittest
from datetime import datetime
from conversation.dialog.dialogmanager import DialogManager

class test_dialogmanager(unittest.TestCase):

    def test_get_next_move_goodbye(self):
        msg_obj = self._create_message()
        test_msg = {"text" : "bye bye", "mood" : "", "msg_obj": msg_obj}
        self.assertEqual(DialogManager().get_next_move(test_msg), {"move": "end"})


    def test_get_next_move_start(self):
        msg_obj = self._create_message()
        test_msg = {"text" : "sssstart", "mood" : "", "msg_obj": msg_obj}
        self.assertEqual(DialogManager().get_next_move(test_msg), {"move": "start"})


    def test_get_next_move_mood(self):
        msg_obj = self._create_message()
        test_msg = {"text" : "I'm fine", "mood" : "positive", "msg_obj": msg_obj}
        self.assertEqual(DialogManager().get_next_move(test_msg), {"move": "mood", "mood": "positive"})

    def _create_message(self):
        return {"chat_id": "222772",
                "text": "does not matter",
                "msg_id": "100500",
                "date": datetime.utcnow()}

if __name__ == '__main__':
    unittest.main()
