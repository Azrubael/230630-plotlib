import numpy as np
"""Quantum logic gate
https://en.wikipedia.org/wiki/Quantum_logic_gate
NB: This script can work only with the matrixes of equal dimension
"""

def I():
    """Identity Gate
    [[1,0],
     [0,1]]
    """
    return np.identity(2)
    
def X():
    """NOT Gate
    [[0,1],
     [1,0]]
    """
    return np.identity(2)[..., ::-1]
    
def H():
    """Walsh-Hadamard Gate (it creates an equal superposition state if given a computational basis state)
    [[1,1],
     [1,-1]] * sqrt(2)
    """
    return np.array([[1,1],[1,-1]]) / np.sqrt(2)
    
def SWAP():
    """Swap gate (swaps two qubits)
    [[1,0,0,0],
     [0,1,0,0],
     [0,0,0,1],
     [0,0,1,0]]
    """
    m = np.identity(4)
    m[[1,2]] = m[[2,1]]
    return m
    
def CX():
    """Controlled NOT gate (act on 2 or more qubits, where one or more qubits act as a control for some operation)
    [[1,0,0,0],
     [0,0,1,0],
     [0,1,0,0],
     [0,0,0,1]]    
    """
    m = np.identity(4)
    m[[3,2]] = m[[2,3]]
    return m
    
def apply(v, *gates):
    """Inplemented passed gates upon the qubit v
    """
    m = gates[0]
    gates = gates[1:]
    for gate in gates:
        m = np.kron(gate,m)
    return m.dot(v)
    
def observe(v):
    """Collapse the wave function and take a random result
    """
    v2 = np.absolute(v) ** 2
    c = np.random.choice(v.size, 1, p=v2)
    return c[0]
    
if __name__ == "__main__":
    a = np.array([1,0,0,0])
    print(observe(a))
    a = apply(a, X(), H())
    print(observe(a))
    print("-" * 50)
    a = np.array([0,0,0,1])
    print(observe(a))
    a = apply(a, H())
    print(observe(a))
    