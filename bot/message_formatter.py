from typing import Literal


class MessageFormatter:
    MessageType = Literal["notification", "success", "error", "warning"]

    def format(self, title: str, body: str, message_type: MessageType = "notification") -> str:
        if message_type == "notification":
            return self._format_notification(title, body)
        elif message_type == "success":
            return self._format_success(title, body)
        elif message_type == "error":
            return self._format_error(title, body)
        elif message_type == "warning":
            return self._format_warning(title, body)
        else:
            return self._format_notification(title, body)

    def _format_notification(self, title: str, body: str) -> str:
        return f"🔔 *{title}*\n\n{body}"

    def _format_success(self, title: str, body: str) -> str:
        return f"✅ *{title}*\n\n{body}"

    def _format_error(self, title: str, body: str) -> str:
        return f"❌ *{title}*\n\n{body}"

    def _format_warning(self, title: str, body: str) -> str:
        return f"⚠️ *{title}*\n\n{body}"

message_formater = MessageFormatter()