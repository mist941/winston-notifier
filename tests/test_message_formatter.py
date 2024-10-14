import unittest
from venv import logger

from bot.message_formatter import message_formater


class TestMessageFormatter(unittest.TestCase):

    def test_notification_format(self):
        message = message_formater.format("Notification", "works", "notification")
        logger.info(message)
        self.assertEqual(message, "🔔 *Notification*\n\nworks")

    def test_success_format(self):
        message = message_formater.format("Success", "works", "success")
        self.assertEqual(message, "✅ *Success*\n\nworks")

    def test_error_format(self):
        message = message_formater.format("Error", "works", "error")
        self.assertEqual(message, "❌ *Error*\n\nworks")

    def test_warning_format(self):
        message = message_formater.format("Warning", "works", "warning")
        self.assertEqual(message, "⚠️ *Warning*\n\nworks")

if __name__ == '__main__':
    unittest.main()
