from flask import Flask, request
from .main import gemini_text_response

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/ai')
def ai():
    prompt = request.args.get('prompt', '')
    if not prompt:
        return 'Missing prompt', 400
    response = gemini_text_response(prompt)
    return response
    