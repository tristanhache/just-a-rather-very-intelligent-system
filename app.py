from flask import Flask, render_template, request

app = Flask(__name__)

# Store chat messages in a list (for simplicity; you should use a database)
chat_messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=chat_messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form.get('message')
    chat_messages.append(message)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)