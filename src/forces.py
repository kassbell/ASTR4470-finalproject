# imports
import numpy as np

def compute_accs(x, m, G=1.0):
    """
    x: (N, 3) array
    m: (N,) array
    returns: (N, 3) accelerations
    """
    N = len(m)
    acc = np.zeros_like(x)

    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            r_ij = x[i] - x[j]
            dist = np.linalg.norm(r_ij)

            acc[i] += -G * m[j] * r_ij / dist**3

    return acc