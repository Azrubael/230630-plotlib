import cmath
import math
import random
from typing import List

# Type aliases
Matrix = List[List[complex]]
Vector = List[complex]


def I() -> Matrix:
    """1‑qubit identity gate"""
    return [
        [1, 0],
        [0, 1]
    ]


def H() -> Matrix:
    """Hadamard gate"""
    s = 1 / math.sqrt(2)
    return [
        [s, s],
        [s, -s]
    ]


def SWAP() -> Matrix:
    """Swap gate (swaps two qubits)"""
    return [
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]
    ]


def X() -> Matrix:
    """Flip gate (Pauli‑X or NOT function)"""
    return [
        [0, 1],
        [1, 0]
    ]


def S() -> Matrix:
    """S gate applies a phase of i to the |1> state."""
    return [
        [1, 0],
        [0, 0+1j]
    ]


def T() -> Matrix:
    """T gate applies a phase of e^(i*pi/4) to the |1> state.
    It is a key non-Clifford gate used for universal quantum computation."""
    return [
        [1, 0],
        [0, cmath.exp(1j * math.pi / 4)]
    ]


def Z() -> Matrix:
    """Z gate applies a phase of -1 to the |1> state.
   It flips the sign of the |1> amplitude and is self-inverse. """
    return [
        [1, 0],
        [0, -1]
    ]


def CX() -> Matrix:
    """Controlled NOT gate (CNOT function)"""
    return [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ]


def CS() -> Matrix:
    """CS applies a phase of i to the |11> state.
    It is the controlled version of the S gate and is useful in phase-based circuits.
    """
    return [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0+1j]
    ]


def CT() -> Matrix:
    """CT applies a phase of e^(-i*pi/4) to the |11> state.
    It is the inverse of controlled-T and is used to undo T-phase effects.
    """
    return [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, cmath.exp(1j * math.pi / 4)]
    ]


def CZ() -> Matrix:
    """CZ applies a phase of -1 to the |11> state.
    It is a controlled phase flip and is self-inverse.
    """
    return [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, -1]
    ]


def CX_dagger() -> Matrix:
    """Controlled NOT gate dagger (fully the same as CX)"""
    return CX()


def CS_dagger():
    """Controlled-S^† (controlled inverse of S)"""
    return [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, -1j]
    ]


def CT_dagger():
    """CT_dagger applies a phase of e^(-i*pi/4) to the |11> state.
    It is the inverse of CT and cancels its action on the target phase.
    """
    return [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, cmath.exp(-1j * math.pi / 4)]
    ]


def CZ_dagger():
    """Fully the same as CZ"""
    return [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, -1]
    ]
    

def obserVe(v: Vector, return_binary: bool = False) -> int | str:
    if not v:
        raise ValueError("Vector is empty")

    # Calculate probabilities (|amplitude|^2)
    probs = [abs(amp) ** 2 for amp in v]
    total = sum(probs)
    if total == 0:
        raise ValueError("All amplitudes are zero")

    # Normalize probabilities
    probs = [p / total for p in probs]

    # Random selection weighted by probabilities
    r = random.random()
    cumulative = 0.0
    idx = len(v) - 1  # fallback
    for i, p in enumerate(probs):
        cumulative += p
        if r <= cumulative:
            idx = i
            break

    if return_binary:
        # Transform index into a binary string
        qubits = int(math.log2(len(v)))
        return format(idx, f'0{qubits}b')
    return idx


"""
Що ще можна додати

Y gate (Pauli‑Y): ще один фундаментальний оператор, який поєднує фазовий зсув і фліп.

RX, RY, RZ (обертальні ворота): дозволяють обертати кубіт навколо осей Блоха на довільний кут. Це критично для варіаційних алгоритмів.

Toffoli gate (CCX, контрольований‑контрольований‑NOT): трьохкубітний оператор, важливий для квантових алгоритмів у криптографії.

Fredkin gate (контрольований SWAP): ще один трьохкубітний оператор, корисний для симуляцій.
"""