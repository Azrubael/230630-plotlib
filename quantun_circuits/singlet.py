# singlet_simulation.py
import numpy as np

# базові кубіти (фотони) у когерентній біні: |0> = [1,0], |1> = [0,1]
zero = np.array([1, 0], dtype=complex)
one  = np.array([0, 1], dtype=complex)

# оператор Тензорного добутку
def kron(*mats):
    res = mats[0]
    for M in mats[1:]:
        res = np.kron(res, M)
    return res

# Cтандартний сінглет: (|01> - |10>)/sqrt(2)
psi_singlet = (kron(zero, one) - kron(one, zero)) / np.sqrt(2)

# перевірка нормування
print("Норма |ψ_singlet|^2:", np.vdot(psi_singlet, psi_singlet).real)

# матриця густини для чистого стану rho = |ψ><ψ|
rho = np.outer(psi_singlet, np.conjugate(psi_singlet))

# частковий слід: віддаємо другий фотон (отримуємо стан першого)
def partial_trace(rho, keep=0, dims=[2,2]):
    # keep: індекс підсистеми, який зберігаємо (0 або 1)
    dimA, dimB = dims
    if keep == 0:
        # trace по другій підсистемі
        rhoA = np.zeros((dimA, dimA), dtype=complex)
        for i in range(dimB):
            # проектор на |i><i> для другої підсистеми
            proj = np.zeros((dimB, dimB), dtype=complex)
            proj[i, i] = 1.0
            rhoA += (np.kron(np.eye(dimA), proj) @ rho @ np.kron(np.eye(dimA), proj)).reshape((dimA, dimB, dimA, dimB)).trace(axis1=1, axis2=3)
        return rhoA
    else:
        # trace по першій підсистемі
        rhoB = np.zeros((dimB, dimB), dtype=complex)
        for i in range(dimA):
            proj = np.zeros((dimA, dimA), dtype=complex)
            proj[i, i] = 1.0
            rhoB += (np.kron(proj, np.eye(dimB)) @ rho @ np.kron(proj, np.eye(dimB))).reshape((dimA, dimB, dimA, dimB)).trace(axis1=0, axis2=2)
        return rhoB

# простіший спосіб зробити частковий слід (більш ефективний)
def partial_trace_fast(rho, keep=0, dims=[2,2]):
    dA, dB = dims
    rho = rho.reshape((dA, dB, dA, dB))
    if keep == 0:
        # сумуємо по індексу другої підсистеми
        return np.einsum('ijik->jk', rho)
    else:
        return np.einsum('iijk->jk', rho)

rho_A = partial_trace_fast(rho, keep=0)
rho_B = partial_trace_fast(rho, keep=1)

print("Матриця густини rho (4x4):\n", np.round(rho, 3))
print("Частковий слід по другому фотону (rho_A):\n", np.round(rho_A, 3))
print("Частковий слід по першому фотону (rho_B):\n", np.round(rho_B, 3))

# перевірка чистоти підсистем: для сінглету вони повинні бути максимально змішані (I/2)
I2 = np.eye(2) / 2
print("Відмінність rho_A від I/2 (норма):", np.linalg.norm(rho_A - I2))
print("Відмінність rho_B від I/2 (норма):", np.linalg.norm(rho_B - I2))

# перевірка власних значень rho (чистий стан має один власний =1, решта 0)
eigvals = np.linalg.eigvals(rho)
print("Власні значення rho:", np.round(eigvals.real, 6))

# обчислення фіделітету між отриманим rho і ідеальним сінглетом (для чистого з стану це просто |<ψ|ψ_ideal>|^2)
def fidelity_pure(rho, psi):
    # якщо rho чистий зі станом psi_rho, fidelity = <psi|rho|psi>
    return np.real(np.vdot(psi, rho @ psi))

f = fidelity_pure(rho, psi_singlet)
print("Фіделітет з ідеальним сінглетом:", f)

# Якщо потрібно: побудова випадкового змішаного стану близького до сінглету (наприклад, деяка деполяризація)
def depolarize(rho, p):
    d = rho.shape[0]
    return (1 - p) * rho + p * np.eye(d) / d

rho_noisy = depolarize(rho, p=0.1)
print("Фіделітет для зашумленого стану (p=0.1):", np.real(np.trace(rho @ rho_noisy)))
