from flask import Flask, render_template
from flask_socketio import SocketIO
import utils as u

app = Flask(__name__)
socketio = SocketIO(app)

# If the user just goes to the "route" / then run this function
# Tell Flask to look in the "template" folder and render "index.html" file
@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('execute_quantum')
def execute_quantum(data):
    # Use Qiskit to perform quantum computation
    # Send the results back to the client
    result = u.generateNoise(data)  # Replace with your quantum computation logic
    # Send the calculation result to all of the clients
    socketio.emit('quantum_result', result)


if __name__ == '__main__':
    socketio.run(app, debug=True)
