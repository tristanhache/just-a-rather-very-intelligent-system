from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, join_room, leave_room, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xcbg\xae-\xe4\x95\xb7\x14\xa1\xb5\\ e\x11l\xc5\x13\x0b#\x82\xc8\x18_\xd7'
socketio = SocketIO(app)

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
        emit('message', data, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
