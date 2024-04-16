from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

import azure.quantum
from azure.quantum.qiskit import AzureQuantumProvider
from azure.quantum import Workspace

import numpy as np

from azure.identity import DefaultAzureCredential

default_credential = DefaultAzureCredential()


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

    result = simulatorRun(qc)
    counts = result.get_counts(qc)

    return counts

def simulatorRun(circuit):
    simulator = AerSimulator()
    compiled_circuit = transpile(circuit, simulator)

    result = simulator.run(compiled_circuit).result()
    return result

def azureqpuRun(circuit):
    workspace = Workspace ( 
        resource_id = "/subscriptions/bb7d82f6-5626-486b-8e29-835b0d417e07/resourceGroups/AzureQuantum/providers/Microsoft.Quantum/Workspaces/Tester", 
        location = "East US"  
    )

    provider = AzureQuantumProvider(workspace)

    qpu_backend = provider.get_backend("rigetti.qpu.ankaa-2")    

    job = qpu_backend.run(circuit, shots=1024)
    result = job.result()

    return result