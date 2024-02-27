from flask import Flask, render_template
from flask_socketio import SocketIO
import utils as u

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('execute_quantum')
def execute_quantum(data):

    result = u.generateNoise(data)  
    socketio.emit('quantum_result', result)


if __name__ == '__main__':
    socketio.run(app, debug=True)
