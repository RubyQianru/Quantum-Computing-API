# Qiskit simulators
from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Azure Quantum
import azure.quantum
from azure.quantum.qiskit import AzureQuantumProvider
from azure.quantum import Workspace
from azure.identity import DefaultAzureCredential
default_credential = DefaultAzureCredential()
from qiskit import transpile


# IBM Quantum
# from qiskit_ibm_runtime import QiskitRuntimeService
# from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Estimator, Session

import numpy as np
import asyncio

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

    print("Circuit ready!")
    
    result = azureqpuRun(qc)

    # fail 
    '''
    Result(backend_name='rigetti.qpu.ankaa-2', backend_version='1', qobj_id='circuit-164-11358', job_id='dd5e5d76-00d6-11ef-bc97-acde48001122', success=True, results=[ExperimentResult(shots=28, success=True, meas_level=2, data=ExperimentResultData(counts={'10100': 1.0, '10010': 2.0, '00001': 2.0, '10011': 1.0, '01010': 2.0, '11010': 3.0, '10000': 1.0, '00010': 1.0, '11001': 3.0, '01100': 1.0, '01000': 2.0, '11100': 1.0, '01001': 1.0, '01111': 1.0, '01110': 1.0, '10110': 2.0, '00011': 1.0, '01011': 1.0, '11011': 1.0}, probabilities={'10100': 0.03571428571428571, '10010': 0.07142857142857142, '00001': 0.07142857142857142, '10011': 0.03571428571428571, '01010': 0.07142857142857142, '11010': 0.10714285714285714, '10000': 0.03571428571428571, '00010': 0.03571428571428571, '11001': 0.10714285714285714, '01100': 0.03571428571428571, '01000': 0.07142857142857142, '11100': 0.03571428571428571, '01001': 0.03571428571428571, '01111': 0.03571428571428571, '01110': 0.03571428571428571, '10110': 0.07142857142857142, '00011': 0.03571428571428571, '01011': 0.03571428571428571, '11011': 0.03571428571428571}), header=QobjExperimentHeader(metadata={}, name='circuit-164-11358', num_qubits='5', qiskit='True'))], date=None, status=None, header=None, error_data=None)
    '''
    counts = {format(n, "03b"): 0 for n in range(8)}
    counts.update(result.get_counts(qc))

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

    simulator_backend = provider.get_backend("ionq.simulator")
    circuit = transpile(circuit, simulator_backend)

    qpu_backend = provider.get_backend("rigetti.qpu.ankaa-2")    
    print("Backend job ready!")
    job = qpu_backend.run(circuit, shots=28)
    result = job.result()
    print(result)
    return result


