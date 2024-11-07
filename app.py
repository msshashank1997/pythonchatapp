from flask import Flask, render_template
from flask_socketio import SocketIO, send
from datetime import datetime
import logging
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, async_mode='eventlet')

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        app.logger.error(f"Error rendering template: {e}")
        return "An error occurred", 500

@socketio.on('message')
def handleMessage(msg):
    try:
        timestamp = datetime.now().strftime('%H:%M:%S')
        send({'user': msg['user'], 'message': msg['message'], 'time': timestamp}, broadcast=True)
    except Exception as e:
        app.logger.error(f"Error handling message: {e}")

if __name__ == '__main__':
    try:
        socketio.run(app, host='0.0.0.0', port=5000)
    except Exception as e:
        app.logger.error(f"Error starting the server: {e}")
