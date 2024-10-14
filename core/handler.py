from core.notification import send_notification

def handle_notification(title: str, body: str, message_type: str) -> bool:
    try:
        send_notification(title, body, message_type)
        return True
    except Exception as e:
        print(f"Error handling notification: {e}")
        return False