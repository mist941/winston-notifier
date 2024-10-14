from bot.telegram_bot import telegram_bot
from bot.message_formatter import message_formater

def send_notification(title: str, body: str, message_type: str) -> None:
    formatted_message = message_formater.format(title, body, message_type)
    telegram_bot.send_message(formatted_message)