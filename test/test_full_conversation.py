import unittest
from time import sleep
from conversation.conversation import get_response
from datetime import datetime
from persistence.settings import get_chat_language, save_chat_language
from persistence.domain import delete_all_chat_moods


# only runs when env var is set up correctly to assess GCP services, e.g. dialogflow, firebase
# export GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_key>
# need to reference the service account json file for now
class FullTestConversation(unittest.TestCase):

    def tearDown(self):
        # just to avoid garbage in the db
        delete_all_chat_moods(self._create_message())

    def test_initial_conversation_en(self):
        message = self._create_message()
        save_chat_language(message, "en")
        message["last_move"] = "some_move_long_time_ago"
        self.add_dialog_flow(message)
        message["text"] = 'hi'
        self.assertIn(get_response(message)[0], ["Hello!", "Hi there!", "What's up?", "Nice to see you!", "Hello dear!"])

    def test_initial_conversation_ru(self):
        message = self._create_message()
        save_chat_language(message, "ru")
        self.add_dialog_flow(message)
        message["text"] = 'привет'
        response, move = get_response(message)
        self.assertIn(response, ["Приветик :) Давай начнем. Как тебя зовут?",
                                           "Привет! Для начала скажи мне, как тебя зовут",
                                           "Привет, добро пожаловать! Как мне тебя называть?"])
        message = self._create_message()
        save_chat_language(message, "ru")
        self.add_dialog_flow(message)
        message["last_move"] = move["move"]
        message["text"] = 'меня зовут Артем а тебя'
        self.assertIn(get_response(message)[0], [
                "А я Псих. Приятно познакомиться. Я немного разбираюсь в человеческих чувствах, а еще я запомню все, "
                "что ты мне скажешь. Как думаешь, как я тебе буду полезен?"])

    def test_mood_en_language(self):
        message = self._create_message()
        save_chat_language(message, "en")
        message["text"] = "I feel moody"
        self.add_dialog_flow(message)
        self.assertIn(get_response(message)[0], ["What a pity", "I'm sorry to hear that.", "So sad."])

    def test_mood_en_language_amazing(self):
        message = self._create_message()
        save_chat_language(message, "en")
        message["text"] = "I feel amazing now because this shit works"
        self.add_dialog_flow(message)
        self.assertIn(get_response(message)[0], ["Nice to hear that!", "I'm happy for you!", "Great news!"])

    def test_mood_en_language_amazing_negation(self):
        message = self._create_message()
        save_chat_language(message, "en")
        message["text"] = "I don't feel amazing"
        self.add_dialog_flow(message)
        self.assertIn(get_response(message)[0], ["What a pity", "I'm sorry to hear that.", "So sad."])

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
        self.assertTrue("100% плохое" in get_response(message)[0])

    def test_switch_language_en(self):
        message = self._create_message()
        save_chat_language(message, "en")
        self.add_dialog_flow(message)
        message["text"] = 'change to russian'
        self.assertEqual(get_response(message)[0], 'I will switch to russian now')
        self.assertEqual(get_chat_language(message), "ru")

    def test_help_en(self):
        message = self._create_message()
        save_chat_language(message, "en")
        self.add_dialog_flow(message)
        message["text"] = 'help'
        self.assertTrue("Sure," in get_response(message)[0])

    def test_switch_language_ru(self):
        message = self._create_message()
        save_chat_language(message, "ru")
        self.add_dialog_flow(message)
        message["text"] = 'смени язык на английский'
        self.assertEqual(get_response(message)[0], 'Меняю язык на английский')
        self.assertEqual(get_chat_language(message), "en")

    @staticmethod
    def add_dialog_flow(message):
        sleep(1)
        del message["ignore_dialogflow"]

    @staticmethod
    def _create_message():
        return {"chat_id": 222772,
                "msg_id": 1,
                "date": datetime.utcnow(),
                "text": "hello",
                "language": "en",
                "ignore_dialogflow": "ignored"}


if __name__ == '__main__':
    unittest.main()
