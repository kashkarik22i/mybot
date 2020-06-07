import unittest
from unittest.mock import patch
from conversation.languages import detect_language

class TestLanguages(unittest.TestCase):

    @patch('conversation.languages.get_chat_language')
    def test_detect_language_is_set(self, patch_get_chat_language):
        patch_get_chat_language.return_value = "ru"
        self.assertEqual(detect_language({"language": "de"}), "ru")

    @patch('conversation.languages.get_chat_language')
    def test_detect_language_in_message(self, patch_get_chat_language):
        patch_get_chat_language.return_value = None
        self.assertEqual(detect_language({"language": "de"}), "de")

    @patch('conversation.languages.get_chat_language')
    def test_detect_language_unset(self, patch_get_chat_language):
        patch_get_chat_language.return_value = None
        self.assertEqual(detect_language({"language": None}), "en")

if __name__ == '__main__':
    unittest.main()
