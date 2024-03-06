from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np


def generateNoise(num_qubits):
    qc = QuantumCircuit(num_qubits, num_qubits)

    qc.h(range(num_qubits))
    qc.measure(range(num_qubits), range(num_qubits))

    simulator = AerSimulator()

    compiled_circuit = transpile(qc, simulator)

    result = simulator.run(compiled_circuit).result()
    counts = result.get_counts()

    binary_string = max(counts, key=counts.get)
    random_bits = np.array([int(bit) for bit in binary_string])[::-1]

    random_bits = random_bits.tolist()

    return random_bits

