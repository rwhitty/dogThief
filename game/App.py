from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

players = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join_game')
def handle_join_game(data):
    username = data['username']
    if username not in players:
        players.append(username)
    emit('update_player_list', players, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')