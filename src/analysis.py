import numpy as np

def compute_energy(x, v, m, G=1.0):
    # kinetic energy
    KE = 0.5 * np.sum(m[:, None] * v**2)
    
    # potential energy
    PE = 0.0
    N = len(m)
    
    for i in range(N):
        for j in range(i+1, N):
            r = np.linalg.norm(x[i] - x[j])
            PE += -G * m[i] * m[j] / r
    
    return KE + PE