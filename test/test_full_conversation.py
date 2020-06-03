import unittest
from time import sleep
from conversation.conversation import get_response
from datetime import datetime
from persistence.settings import get_chat_language, save_chat_language

# only runs when env var is set up correctly to assess GCP services, e.g. dialogflow
# export GOOGLE_APPLICATION_CREDENTIALS=~/Documents/work/projects/mybot/data/credentials/key
# need to reference the service account json file for now
class FullTestConversation(unittest.TestCase):

    def test_hello_en_language(self):
        message = self._create_message()
        save_chat_language(message, "en")
        self.add_dialog_flow(message)
        self.assertIn(get_response(message), ["Hello!", "Hi there!", "What's up?", "Nice to see you!", "Hello dear!"])

    def test_hello_ru_language(self):
        message = self._create_message()
        save_chat_language(message, "ru")
        self.add_dialog_flow(message)
        message["text"] = 'привет'
        self.assertIn(get_response(message), ["Привет!", "Здорово!", "Че каво?", "Здравствуй!", "Привет тебе!"])

    def test_wrong_language(self):
        message = self._create_message()
        save_chat_language(message, "ru")
        self.add_dialog_flow(message)
        message["text"] = 'hi'
        self.assertIn(get_response(message), ["Я не понял, повтори по-другому", "Или я глупый или ты хочешь что-то чего я не умею",
                        "Я не понял, ты всегда можешь спросить у меня что я умею а что нет"])

    def test_mood_en_language(self):
        message = self._create_message()
        save_chat_language(message, "en")
        message["text"] = "I feel moody"
        self.add_dialog_flow(message)
        self.assertIn(get_response(message), ["What a pity", "I'm sorry to hear that.", "So sad."])

    def test_mood_en_language_amazing(self):
        message = self._create_message()
        save_chat_language(message, "en")
        message["text"] = "I feel amazing now because this shit works"
        self.add_dialog_flow(message)
        self.assertIn(get_response(message), ["Nice to hear that!", "I'm happy for you!", "Great news!"])

    def test_mood_en_language_amazing_negation(self):
        message = self._create_message()
        save_chat_language(message, "en")
        message["text"] = "I don't feel amazing"
        self.add_dialog_flow(message)
        self.assertIn(get_response(message), ["What a pity", "I'm sorry to hear that.", "So sad."])

    def test_get_mood_ru(self):
        message = self._create_message()
        save_chat_language(message, "ru")
        message["text"] = "я устал"
        self.add_dialog_flow(message)
        get_response(message)

        message = self._create_message()
        save_chat_language(message, "ru")
        message["text"] = "как я себя последнее время чувствовал?"
        self.add_dialog_flow(message)
        self.assertTrue("я устал" in get_response(message))

    def test_switch_language_en(self):
        message = self._create_message()
        save_chat_language(message, "en")
        self.add_dialog_flow(message)
        message["text"] = 'change to russian'
        self.assertEqual(get_response(message), 'I will switch to russian now')
        self.assertEqual(get_chat_language(message), "ru")

    def test_switch_language_ru(self):
        message = self._create_message()
        save_chat_language(message, "ru")
        self.add_dialog_flow(message)
        message["text"] = 'смени язык на английский'
        self.assertEqual(get_response(message), 'Меняю язык на английский')
        self.assertEqual(get_chat_language(message), "en")

    def add_dialog_flow(self, message):
        sleep(1)
        del message["ignore_dialogflow"]

    def _create_message(self):
        return {"chat_id": 222772,
                "msg_id": 1,
                "date": datetime.utcnow(),
                "text": "hello",
                "language": "en",
                "ignore_dialogflow": "ignored"}

if __name__ == '__main__':
    unittest.main()
