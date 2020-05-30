import unittest
from time import sleep
from conversation.conversation import get_response
from datetime import datetime

# only runs when env var is set up correctly to assess GCP services, e.g. dialogflow
# export GOOGLE_APPLICATION_CREDENTIALS=~/Documents/work/projects/mybot/data/credentials/key
# need to reference the service account json file for now
class FullTestConversation(unittest.TestCase):

    def test_hello_en_language(self):
        sleep(1) # need in order for API limits not to be reached yet
        self.assertEqual(get_response(self._create_message()), 'Hello!')

    def test_hello_ru_language(self):
        sleep(1) # need in order for API limits not to be reached yet
        message = self._create_message()
        message["language"] = 'ru'
        message["text"] = 'хало блин'
        self.assertEqual(get_response(message), 'Hello!')

    def test_mood_en_language(self):
        sleep(1) # need in order for API limits not to be reached yet
        message = self._create_message()
        message["text"] = "I feel moody"
        self.assertEqual(get_response(message), 'Hello!')

    def _create_message(self):
        return {"chat_id": 1,
                "msg_id": 1,
                "date": datetime.now(),
                "text": "hello",
                "language": "en",
                "ignore_dialogflow": "ignored"}

if __name__ == '__main__':
    unittest.main()
