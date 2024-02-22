from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np

def generateNoise(num_qubits):
    # Create a quantum circuit
    qc = QuantumCircuit(num_qubits, num_qubits)

    # Apply Hadamard gate to each qubit
    qc.h(range(num_qubits))

    # Measure all qubits
    qc.measure(range(num_qubits), range(num_qubits))

    # Use the Aer simulator
    simulator = AerSimulator()

    # Transpile the circuit for the simulator
    compiled_circuit = transpile(qc, simulator)

    # Run the simulation
    result = simulator.run(compiled_circuit).result()

    # Get the counts from the result
    counts = result.get_counts()

    # Convert counts to an array of random bits
    binary_string = max(counts, key=counts.get)
    random_bits = np.array([int(bit) for bit in binary_string])[::-1]

    random_bits = random_bits.tolist()
    print(random_bits)
    return random_bits
