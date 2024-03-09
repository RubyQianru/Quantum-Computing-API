from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np

class QC:
    def __init__ (self, num_qubits):
        self.qc = QuantumCircuit(num_qubits, num_qubits)
        self.num_qubits = num_qubits
        self.result = None
    
    def compile(self):
        simulator = AerSimulator()
        compiled_circuit = transpile(self.qc, simulator)

        print("Compiled Circuit:")
        print(compiled_circuit)

        try:
            self.result = simulator.run(compiled_circuit).result()
        except Exception as e:
            print(f"Error during simulation: {e}")
    
    
    def getCount(self):
        if self.result is not None:
            try:
                counts = self.result.get_counts()
                if counts:
                    binary_string = max(counts, key=counts.get)
                    result = np.array([int(bit) for bit in binary_string])[::-1]
                    result = result.tolist()
                    return result
                else:
                    print("No counts available.")
            except Exception as e:
                print(f"Error while getting counts: {e}")
        else:
            print("Result object is None. Make sure to run compile() before getCount().")
        return [0] * self.num_qubits  # or any default value


    def hedamard(self):
        self.qc.h(range(self.num_qubits))   
    
    def controlNot(self):
        for i in range(self.num_qubits-1):
            self.qc.cx(i, i+1)
    

def singleHadamard(num_qubits=20):
    qc = QC(num_qubits)
    qc.hedamard()
    qc.compile()
    return qc.getCount()

def hadamardControlNot(num_qubits=20):
    qc = QC(num_qubits)
    qc.hedamard()
    qc.controlNot()
    qc.compile()
    return qc.getCount()




