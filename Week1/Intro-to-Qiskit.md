# Intro to Quantum Physics
* [Basics of quantum information](https://learning.quantum.ibm.com/course/basics-of-quantum-information/single-systems)
* If you want to learn more about quantum physics and quantum information, please refer to the 

# Intro to Python 
* Download Python: [Link](https://www.python.org/downloads/)
* Download pip: Python install pip via terminal
```
python get-pip.py
```
* If you want to get some practice before we start with Qiskit, take a look at: [Python and Numpy Tutorials](https://cs231n.github.io/python-numpy-tutorial/)

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

```python
from qiskit import QuantumCircuit
# Create quantum circuit with 3 qubits and 3 classical bits
# (we'll explain why we need the classical bits later)
qc = QuantumCircuit(3, 3)
qc.draw()  # returns a drawing of the circuit
```

# Intro to Qiskit REST API
* Main Documentation: [Link](https://docs.quantum.ibm.com/api/runtime)
> The Qiskit IBM Runtime REST API allows you to run on quantum systems using Qiskit Runtime primitives, a simplified interface for circuit execution powered by advanced runtime compilation, error suppression, and error mitigation techniques, as well as getting information about instances and systems you have access to.


### Backend Setup
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
