def S():
    return [
        [1, 0],
        [0, 1j]
    ]

def CS():
    # Controlled-S gate in 4x4 matrix form
    return [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1j]
    ]

def CS_dagger():
    # Controlled-S^† (controlled inverse of S)
    return [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, -1j]
    ]
