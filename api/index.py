from flask import Flask, request, render_template_string
from .main import gemini_text_response

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KH AI V2 - Gemini Web</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f7f7f7; margin: 0; padding: 0; }
        .container { max-width: 600px; margin: 40px auto; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px #0001; padding: 32px; }
        h1 { color: #2b7cff; }
        form { margin-bottom: 24px; }
        textarea { width: 100%; min-height: 80px; padding: 8px; border-radius: 4px; border: 1px solid #ccc; font-size: 1em; }
        button { background: #2b7cff; color: #fff; border: none; padding: 10px 24px; border-radius: 4px; font-size: 1em; cursor: pointer; }
        button:hover { background: #1a5fcc; }
        .response { background: #f0f4ff; border-left: 4px solid #2b7cff; padding: 16px; margin-top: 16px; border-radius: 4px; white-space: pre-wrap; }
        .error { color: #c00; margin-top: 16px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>KH AI V2 - Gemini Web</h1>
        <form method="get" action="/ai">
            <label for="prompt"><b>Enter your prompt:</b></label><br>
            <textarea id="prompt" name="prompt" required>{{ prompt|default('') }}</textarea><br>
            <button type="submit">Ask Gemini</button>
        </form>
        {% if response %}
            <div class="response"><b>AI Response:</b><br>{{ response }}</div>
        {% endif %}
        {% if error %}
            <div class="error">{{ error }}</div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, prompt='', response=None, error=None)

@app.route('/ai')
def ai():
    prompt = request.args.get('prompt', '').strip()
    if not prompt:
        return render_template_string(HTML_TEMPLATE, prompt='', response=None, error='Please enter a prompt.')
    try:
        response = gemini_text_response(prompt)
        return render_template_string(HTML_TEMPLATE, prompt=prompt, response=response, error=None)
    except Exception as e:
        return render_template_string(HTML_TEMPLATE, prompt=prompt, response=None, error=f'Error: {e}')
    