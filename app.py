from flask import Flask, render_template
from flask_socketio import SocketIO, send
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    timestamp = datetime.now().strftime('%H:%M:%S')
    send({'user': msg['user'], 'message': msg['message'], 'time': timestamp}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
