from flask import Flask, render_template, request, session, jsonify
from flask_socketio import SocketIO, join_room, leave_room, emit

import secrets

# Generate a random secret key with 24 bytes (48 characters)
secret_key = secrets.token_hex(24)

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
socketio = SocketIO(app)

# Dictionary to store chat messages (replace with a database in production)
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

        # Store the message (replace with database storage in production)
        if room not in chat_messages:
            chat_messages[room] = []
        chat_messages[room].append({'username': username, 'message': message})

        # Emit the message to all users in the room
        emit('message', {'username': username, 'message': message}, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
