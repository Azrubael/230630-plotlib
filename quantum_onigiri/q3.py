import numpy as np
"""Quantum logic gate
https://en.wikipedia.org/wiki/Quantum_logic_gate
"""

# ── single‑qubit primitives ────────────────────────────────────────────────
def I():
    """1‑qubit identity Gate
    """
    return np.array([[1, 0],
                     [0, 1]])


def X():
    """Flip Gate (Pauli‑X or NOT function)
    """
    return np.array([[0, 1],
                     [1, 0]])


def H():
    """Hadamard Gate
    """
    return np.array([[1, 1],
                    [1, -1]]) / np.sqrt(2)

# ── two‑qubit primitives ───────────────────────────────────────────────────
def SWAP():
    """Swap gate (swaps two qubits)
    """
    m = np.identity(4)
    m[[1, 2]] = m[[2, 1]]
    return m


def CX():
    """Controlled NOT gate CNOT function
    """
    m = np.identity(4)
    m[[3, 2]] = m[[2, 3]]
    return m


# ── core routine ───────────────────────────────────────────────────────────
def apply(v, *gates):
    num_qubits = int(np.log2(v.size))
    m = None
    
    for gate in gates:
        gate_size = int(np.log2(gate.shape[0]))
        
        if gate_size == 1:
            # Single-qubit gate: expand to full system (I ⊗ gate for 2-qubit system)
            expanded_gate = np.kron(np.eye(2**(num_qubits - 1)), gate)
        else:
            # Multi-qubit gate: use as-is
            expanded_gate = gate
        
        # Compose gates
        if m is None:
            m = expanded_gate
        else:
            m = expanded_gate @ m
    
    return m.dot(v)

def observe(v):
    """Collapse the wave function and return a random basis index."""
    probs = np.abs(v) ** 2
    return np.random.choice(v.size, p=probs)


if __name__ == "__main__":
    a = np.array([1, 0, 0, 0])
    print("measure:", observe(a))

    a = apply(a, X(), H())
    print("after X,H:", observe(a))

    a = np.array([0, 0, 0, 1])
    print("measure:", observe(a))

    a = apply(a, I())
    print("after I:", observe(a))

    print("-" * 50)
    a = apply(a, I(), SWAP())
    print("after I,SWAP:", observe(a))