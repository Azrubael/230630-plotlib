import cmath
import math

def T():
    return [
        [1, 0],
        [0, cmath.exp(1j * math.pi / 4)]
    ]

def CT():
    return [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, cmath.exp(1j * math.pi / 4)]
    ]

def CT_dagger():
    return [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, cmath.exp(-1j * math.pi / 4)]
    ]
