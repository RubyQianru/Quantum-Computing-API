If you want to learn more about quantum physics and quantum information, please refer to [More About Quantum](https://github.com/RubyQianru/Quantum-Computing-API/blob/main/Week1/More-about-Quantum.md)

# Intro to Python 
* Download Python: [Link](https://www.python.org/downloads/)
* Download pip: Python install pip via terminal
```
python get-pip.py
```
* If you want to get some practice before we start with Qiskit, take a look at: [Python and Numpy Tutorials](https://cs231n.github.io/python-numpy-tutorial/), [Introduction to Python and Jupyter notebooks](https://github.com/Qiskit/textbook/blob/main/notebooks/ch-prerequisites/python-and-jupyter-notebooks.ipynb)

# Intro to Qiskit
* [Atoms of Computation](https://github.com/Qiskit/textbook/blob/main/notebooks/intro/atoms-of-computation.ipynb)
> In this section, we will explain how to build quantum circuits. 

### Download Qiskit
``` 
pip install qiskit --user
pip install qiskit-ibm-runtime --user
```
### Your First Quantum Circuit
> In a circuit, we typically need to do three jobs: First, encode the input, then do some actual computation, and finally extract an output. For your first quantum circuit, we'll focus on the last of these jobs. We start by creating a quantum circuit with 3 qubits and 3 outputs.
* [Code Example](https://github.com/RubyQianru/Quantum-Computing-API/blob/main/Week1/Code-Examples/Quantum-Circuit.ipynb)
* Refer to [Atoms of Computation](https://github.com/Qiskit/textbook/blob/main/notebooks/intro/atoms-of-computation.ipynb) for the complete setup.

# Your First Real-Time Server
* Python Flask Documentation: [Link](https://flask.palletsprojects.com/en/3.0.x/)
* Install Flask & socket.io:
```
pip install Flask, Flask-SocketIO
```
### Set up Backend server.py
* Create a Python script (e.g., server.py) for your Flask server:
```python
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('execute_quantum')
def execute_quantum(data):
    # Use Qiskit to perform quantum computation
    # Send the results back to the client
    result = {}  # Replace with your quantum computation logic
    socketio.emit('quantum_result', result)

if __name__ == '__main__':
    socketio.run(app, debug=True)
```

### Set up Frontend index.html
* If you want to get some knowledge on HTML and CSS take a look at these useful Links: [Mozilla - Intro to HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML), [Mozilla - Getting Started with CSS Tutorials Parts 1-14](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps)
* Create an HTML file (e.g., templates/index.html) for the front-end using p5.js:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/p5.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.1.2/socket.io.js"></script>
    <title>Quantum Art Simulation</title>
</head>
<body>

    <script>
        let socket = io.connect('http://' + document.domain + ':' + location.port);

        function executeQuantumComputation() {
            // Collect any data needed for quantum computation
            // Send data to the server
            socket.emit('execute_quantum', { /* your data here */ });
        }

        socket.on('quantum_result', function(result) {
            // Handle the quantum computation result
            console.log(result);
        });
    </script>
</body>
</html>
```
### Example: Generate Random Numbers
* Link to the folder: [Link](https://github.com/RubyQianru/Quantum-Computing-API/tree/main/Week1/Code-Examples/Server)
* The server will "ask" qiskit quantum computer to generate an array of 29 random bits, and the browser will receive the array, and console.log the array to the console.

# Intro to Qiskit REST API
* Main Documentation: [Link](https://docs.quantum.ibm.com/api/runtime)
> The Qiskit IBM Runtime REST API allows you to run on quantum systems using Qiskit Runtime primitives, a simplified interface for circuit execution powered by advanced runtime compilation, error suppression, and error mitigation techniques, as well as getting information about instances and systems you have access to.

### Authentication Setup
1. Set up Qiskit and IBM Quantum account:
* Install Qiskit: Follow the installation instructions on the (Qiskit documentation).
* Create an IBM Quantum account: Sign up on the (IBM Quantum Experience) website.

2. Get API key and access token:
* After creating an IBM Quantum account, generate an API key from the IBM Quantum Experience dashboard.
* Use the API key to generate an access token.
* Authentication Test:
```python
import requests
 
reqUrl = "https://runtime-us-east.quantum-computing.ibm.com/jobs?limit=10&offset=0&exclude_params=true"
 
headersList = {
  "Accept": "application/json",
  "Authorization": "Bearer YOUR_API_TOKEN_HERE" 
}
 
payload = ""
 
response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
 
print(response.json())
```
* Example Response:
```
{'jobs': [], 'count': 0, 'limit': 10, 'offset': 0}
```
