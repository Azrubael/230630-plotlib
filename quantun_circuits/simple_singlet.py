import numpy as np

# Define basis states
zero = np.array([1, 0])
one = np.array([0, 1])

# Tensor products for |01> and |10>
state_01 = np.kron(zero, one)
state_10 = np.kron(one, zero)

# Create singlet state (normalized)
singlet = (state_01 - state_10) / np.sqrt(2)

print("Quantum singlet state vector:")
print(singlet)
