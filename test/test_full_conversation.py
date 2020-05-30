import unittest
from conversation.conversation import get_response
from datetime import datetime

# only runs when env var is set up correctly to assess GCP services, e.g. dialogflow
# export GOOGLE_APPLICATION_CREDENTIALS=~/Documents/work/projects/mybot/data/credentials/key
# need to reference the service account json file for now
class FullTestConversation(unittest.TestCase):

    def test_start(self):
        self.assertEqual(get_response(self._create_message()), 'Hello!')

    def _create_message(self):
        return {"chat_id": 1,
                "msg_id": 1,
                "date": datetime.now(),
                "text": "hello"}

if __name__ == '__main__':
    unittest.main()
