import math
import random
from typing import List


# Type aliases
Matrix = List[List[complex]]
Vector = List[complex]


# ── single‑qubit primitives ────────────────────────────────────────────────

def I() -> Matrix:
    """1‑qubit identity gate"""
    return [[1+0j, 0+0j],
            [0+0j, 1+0j]]


def X() -> Matrix:
    """Flip gate (Pauli‑X or NOT function)"""
    return [[0+0j, 1+0j],
            [1+0j, 0+0j]]


def H() -> Matrix:
    """Hadamard gate"""
    s = 1 / math.sqrt(2)
    return [[s+0j, s+0j],
            [s+0j, -s+0j]]


# ── two‑qubit primitives ───────────────────────────────────────────────────

def SWAP() -> Matrix:
    """Swap gate (swaps two qubits)"""
    m = identity(4)
    m[1], m[2] = m[2], m[1]
    return m


def CX() -> Matrix:
    """Controlled NOT gate (CNOT function)"""
    m = identity(4)
    m[2], m[3] = m[3], m[2]
    return m


# ── helper functions ───────────────────────────────────────────────────────

def identity(n: int) -> Matrix:
    """Create an n×n identity matrix"""
    m = [[0+0j] * n for _ in range(n)]
    for i in range(n):
        m[i][i] = 1+0j
    return m


def log2(n: int) -> int:
    """Compute base-2 logarithm. The helper function"""
    if n <= 0:
        raise ValueError("log2: input must be positive")
    return int(math.log2(n))


def kronecker(a: Matrix, b: Matrix) -> Matrix:
    """Compute the Kronecker product of two matrices"""
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    
    result = [[0+0j] * (cols_a * cols_b) for _ in range(rows_a * rows_b)]
    
    for i in range(rows_a):
        for j in range(cols_a):
            for pi in range(rows_b):
                for pj in range(cols_b):
                    result[i * rows_b + pi][j * cols_b + pj] = a[i][j] * b[pi][pj]
    
    return result


def matrix_mult(a: Matrix, b: Matrix) -> Matrix:
    """Multiply two matrices"""
    rows_a = len(a)
    cols_b = len(b[0])
    cols_a = len(a[0])
    
    result = [[0+0j] * cols_b for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    
    return result


def matrix_vector_mult(m: Matrix, v: Vector) -> Vector:
    """Multiply a matrix by a vector"""
    result = [0+0j] * len(m)
    
    for i in range(len(m)):
        for j in range(len(v)):
            result[i] += m[i][j] * v[j]
    
    return result


# ── core routine ───────────────────────────────────────────────────────────

def apply(v: Vector, *gates: Matrix) -> Vector:
    """Apply a sequence of gates to a quantum state vector"""
    num_qubits = log2(len(v))
    m = None
    
    for gate in gates:
        gate_size = log2(len(gate))
        
        if gate_size == 1:
            # Single-qubit gate: expand to full system (I ⊗ gate)
            eye = identity(2 ** (num_qubits - 1))
            expanded_gate = kronecker(eye, gate)
        else:
            # Multi-qubit gate: use as-is
            expanded_gate = gate
        
        # Compose gates
        if m is None:
            m = expanded_gate
        else:
            m = matrix_mult(expanded_gate, m)
    
    if m is None:
        m = identity(len(v))
    
    return matrix_vector_mult(m, v)


def observe(v: Vector) -> int:
    """Collapse the wave function and return a random basis index"""
    # Calculate probabilities (|amplitude|^2)
    probs = []
    total = 0.0
    
    for amp in v:
        prob = abs(amp) ** 2
        probs.append(prob)
        total += prob
    
    # Normalize probabilities
    probs = [p / total for p in probs]
    
    # Random selection weighted by probabilities
    r = random.random()
    cumulative = 0.0
    for i, p in enumerate(probs):
        cumulative += p
        if r <= cumulative:
            return i
    
    return len(v) - 1


if __name__ == "__main__":
    a = [1+0j, 0+0j, 0+0j, 0+0j]
    print("measure:", observe(a))

    a = apply(a, X(), H())
    print("after X,H:", observe(a))

    a = [0+0j, 0+0j, 0+0j, 1+0j]
    print("measure:", observe(a))

    a = apply(a, I())
    print("after I:", observe(a))

    print("-" * 50)
    a = apply(a, I(), SWAP())
    print("after I,SWAP:", observe(a))
