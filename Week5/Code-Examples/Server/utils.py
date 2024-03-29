from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np

def randomWalker():
    counts = generateRandomness(2)
    binary_string = max(counts, key=counts.get)

    return binary_string

def randomFloat():
    counts = generateRandomness(5)
    measurement = list(counts.keys())[0]  
    random_float = int(measurement, 2) / (2**5)  

    return random_float

def generateRandomness(num_qubits):

    qc = QuantumCircuit(num_qubits, num_qubits)
    qc.h(range(num_qubits))

    for i in range(num_qubits-1):
        qc.cx(i, i+1)

    qc.measure(range(num_qubits),range(num_qubits))

    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)

    result = simulator.run(compiled_circuit).result()
    counts = result.get_counts(qc)

    return counts