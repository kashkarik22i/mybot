import unittest
from time import sleep
from conversation.conversation import get_response
from datetime import datetime
from persistence.chats import get_chat_language, save_chat_language

# only runs when env var is set up correctly to assess GCP services, e.g. dialogflow
# export GOOGLE_APPLICATION_CREDENTIALS=~/Documents/work/projects/mybot/data/credentials/key
# need to reference the service account json file for now
class FullTestConversation(unittest.TestCase):

    def test_hello_en_language(self):
        message = self._create_message()
        save_chat_language(message, "english")
        self.add_dialog_flow(message)
        self.assertEqual(get_response(message), 'Hello!')

    def test_hello_ru_language(self):
        message = self._create_message()
        save_chat_language(message, "russian")
        self.add_dialog_flow(message)
        message["language"] = 'ignore'
        message["text"] = 'хало блин'
        self.assertEqual(get_response(message), 'Hello!')

    def test_mood_en_language(self):
        message = self._create_message()
        message["text"] = "I feel moody"
        self.add_dialog_flow(message)
        self.assertEqual(get_response(message), "I'm sorry to hear that.")

    def test_switch_language_en(self):
        message = self._create_message()
        save_chat_language(message, "english")
        self.add_dialog_flow(message)
        message["language"] = 'en' # this is just default just in case
        message["text"] = 'change to russian'
        self.assertEqual(get_response(message), 'switched language setting russian')
        self.assertEqual(get_chat_language(message), "ru")

    def test_switch_language_ru(self):
        message = self._create_message()
        save_chat_language(message, "russian")
        self.add_dialog_flow(message)
        message["language"] = 'en' # default is not what user uses, why not...
        message["text"] = 'смени язык на english'
        self.assertEqual(get_response(message), 'switched language setting english')
        self.assertEqual(get_chat_language(message), "en")

    def add_dialog_flow(self, message):
        sleep(1)
        del message["ignore_dialogflow"]

    def _create_message(self):
        return {"chat_id": 222772,
                "msg_id": 1,
                "date": datetime.now(),
                "text": "hello",
                "language": "en",
                "ignore_dialogflow": "ignored"}

if __name__ == '__main__':
    unittest.main()
