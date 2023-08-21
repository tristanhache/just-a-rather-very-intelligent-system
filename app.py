from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to store chat messages
messages = []

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_message = request.form['message']
        messages.append(user_message)
        return redirect(url_for('chat'))

    return render_template('chat.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
