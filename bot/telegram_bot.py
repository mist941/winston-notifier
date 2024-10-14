from bot.exceptions import TelegramBotError
from bot.message_formatter import MessageFormatter
import requests
from typing import Any
from config.settings import TELEGRAM_TOKEN, CHAT_ID

class TelegramBot:
    def __init__(self, token: str, chat_id: str) -> None:
        self.token = token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{self.token}"
        self.message_formatter = MessageFormatter()

    def send_message(self, message: str) -> Any:
        url = f"{self.api_url}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise TelegramBotError(f"Failed to send message: {e}")

        return response.json()

    def send_formatted_message(
            self,
            title: str,
            body: str,
            message_type: MessageFormatter.MessageType
    ) -> Any:
        formatted_message = self.message_formatter.format(title, body, message_type)
        return self.send_message(formatted_message)

telegram_bot = TelegramBot(TELEGRAM_TOKEN, CHAT_ID)