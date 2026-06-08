from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# Create a circuit with 1 qubit
qc = QuantumCircuit(1)

# Apply a Hadamard gate to put qubit in superposition
qc.h(0)

# Get the statevector
state = Statevector.from_instruction(qc)

# Plot Bloch sphere
plot_bloch_multivector(state)

# Show the plot
plt.show()