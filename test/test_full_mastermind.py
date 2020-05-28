import unittest
from telebot.mastermind import get_response

# only runs when env var is set up correctly to assess GCP services, e.g. dialogflow
# export GOOGLE_APPLICATION_CREDENTIALS=~/Documents/work/projects/mybot/data/credentials/key
# need to reference the service account json file for now
class FullTestMastermind(unittest.TestCase):

    def test_start(self):
        self.assertEqual(get_response("hello"), 'Hello!')

if __name__ == '__main__':
    unittest.main()
