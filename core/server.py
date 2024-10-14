from flask import Flask, request, jsonify
from core.handler import handle_notification
from config.settings import SERVER_PORT

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    if not data or 'message_type' not in data or 'title' not in data or 'body' not in data:
        return jsonify({"error": "Invalid data"}), 400

    title = data['title']
    body = data['body']
    message_type = data['message_type']
    result = handle_notification(title, body, message_type)

    if result:
        return jsonify({"status": "Message sent successfully"}), 200
    else:
        return jsonify({"error": "Failed to send message"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=SERVER_PORT)