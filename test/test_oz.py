import unittest
from datetime import datetime
from unittest.mock import patch
from conversation.oz import is_oz_message, is_oz_on, respond_oz_message, log_to_oz

class TestOz(unittest.TestCase):

    def test_is_oz_on(self):
        # should not be enabled for test chat
        self.assertFalse(is_oz_on({"chat_id": "222772"}))

    @patch('conversation.oz.is_oz_enabled')
    def test_is_oz_calls_persistence(self, test_patch):
        test_patch.return_value = False
        self.assertFalse(is_oz_on({"chat_id": "222773"}))
        test_patch.assert_called_once()

    def test_is_oz_message(self):
        self.assertFalse(is_oz_message({"chat_id": "222772", "text": "oz oz"}))
        self.assertFalse(is_oz_message({"chat_id": "222773", "text": "oz oz"}))
        self.assertTrue(is_oz_message({"chat_id": "798772222", "text": "oz oz"}))
        self.assertFalse(is_oz_message({"chat_id": "798772222", "text": "boz boz"}))

    @patch('integration.integration.send_reply_message')
    def test_log_to_oz(self, test_patch):
        message = TestOz._create_message()
        log_to_oz(message)
        message["chat_id"] = "798772222"
        test_patch.assert_called_once_with(message, "222772 1234 foo")

    @patch('conversation.oz.enabled_oz')
    @patch('integration.integration.send_reply_message')
    def test_respond_oz_message_on(self, test_patch1, test_patch2):
        respond_oz_message({"text": "oz on"})
        test_patch1.assert_called_once()
        test_patch2.assert_called_once()

    @patch('conversation.oz.disable_oz')
    @patch('integration.integration.send_reply_message')
    def test_respond_oz_message_on(self, test_patch1, test_patch2):
        respond_oz_message({"text": "oz off"})
        test_patch1.assert_called_once()
        test_patch2.assert_called_once()

    @patch('conversation.oz.get_last')
    @patch('conversation.oz.get_message')
    @patch('integration.integration.send_reply_message')
    def test_respond_oz_message_fake(self, patch_send_reply_message, patch_get_message, patch_get_last):
        old_message = TestOz._create_message()
        patch_get_message.return_value = old_message
        patch_get_last.return_value = old_message

        respond_oz_message({"text": "oz 222772 1234 text bar bar"})

        patch_get_message.assert_called_once_with("222772", "1234")
        patch_get_last.assert_called_once_with("222772")
        patch_send_reply_message.assert_called_once_with(old_message, "bar bar", False)

    @staticmethod
    def _create_message():
        return {"chat_id": "222772", "msg_id": "1234", "text": "foo", "language": "en", "date": datetime.utcnow()}

if __name__ == '__main__':
    unittest.main()
