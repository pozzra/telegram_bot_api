from flask import Flask
import threading
from main import main as start_telegram_bot

app = Flask(__name__)

# Start the Telegram bot in a background thread when the Flask app starts
bot_thread = threading.Thread(target=start_telegram_bot, daemon=True)
bot_thread.start()

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'