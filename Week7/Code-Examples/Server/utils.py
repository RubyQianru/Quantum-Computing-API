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

# IBM Quantum
# from qiskit_ibm_runtime import QiskitRuntimeService
# from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Estimator, Session

import numpy as np
import asyncio

async def randomWalker():
    counts = await generateRandomness(2)
    binary_string = max(counts, key=counts.get)

    return binary_string

async def randomFloat():
    counts = await generateRandomness(5)
    measurement = list(counts.keys())[0]  
    random_float = int(measurement, 2) / (2**5)  

    return random_float

async def generateRandomness(num_qubits):

    qc = QuantumCircuit(num_qubits, num_qubits)
    qc.h(range(num_qubits))

    for i in range(num_qubits-1):
        qc.cx(i, i+1)

    qc.measure(range(num_qubits),range(num_qubits))

    print("Circuit ready!")
    counts = None
    try: 
        result = await azureqpuRun(qc)
        counts = result.get_counts(qc)
    except Exception as e:
        print(f"Unexpected error: {e}")

    return counts

def simulatorRun(circuit):
    simulator = AerSimulator()
    compiled_circuit = transpile(circuit, simulator)

    result = simulator.run(compiled_circuit).result()
    return result

async def azureqpuRun(circuit):

    workspace = Workspace ( 
        resource_id = "/subscriptions/bb7d82f6-5626-486b-8e29-835b0d417e07/resourceGroups/AzureQuantum/providers/Microsoft.Quantum/Workspaces/Tester", 
        location = "East US"  
    )

    provider = AzureQuantumProvider(workspace)

    qpu_backend = provider.get_backend("rigetti.qpu.ankaa-2")    
    print("Backend job ready!")
    job = qpu_backend.run(circuit, shots=1024)
    result = job.result()
    print("Rsult ready!")

    return result


