from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, join_room, leave_room, emit
import secrets

app = Flask(__name__)

# Generate a random secret key with 24 bytes (48 characters)
secret_key = secrets.token_hex(24)

# Set the secret key for the Flask application
app.config['SECRET_KEY'] = secret_key

socketio = SocketIO(app)

# Dictionary to store chat messages for different rooms
chat_messages = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print(f'User connected: {request.sid}')

@socketio.on('disconnect')
def handle_disconnect():
    print(f'User disconnected: {request.sid}')

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    session['room'] = room

    # Send existing messages when a user joins the room
    emit('messages', chat_messages.get(room, []))

@socketio.on('leave')
def handle_leave(data):
    room = session.get('room')
    if room:
        leave_room(room)
        session.pop('room')

@socketio.on('message')
def handle_message(data):
    room = session.get('room')
    if room:
        username = data.get('username', 'Anonymous')
        message = data['message']

        # Store the message
        if room not in chat_messages:
            chat_messages[room] = []
        chat_messages[room].append({'username': username, 'message': message})

        # Emit the message to all users in the room
        emit('message', {'username': username, 'message': message}, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
