from qiskit import QuantumCircuit
from qiskit_aer import Aer

# Step 1: Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Step 2: Apply a Hadamard gate to qubit 0
qc.h(0)

# Step 3: Apply a CNOT gate (control=0, target=1)
qc.cx(0, 1)

# Step 4: Measure both qubits
qc.measure([0,1], [0,1])

# Step 5: Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
job = simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts(qc)

print("Measurement results:", counts)