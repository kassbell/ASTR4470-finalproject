import numpy as np

def two_body(G=1.0):
    m = np.array([10.0, 1.0])

    x0 = np.array([
        [0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0]
    ])

    r = 1.0
    v_circ = np.sqrt(G * m[0] / r)

    v0 = np.array([
        [0.0, 0.0, 0.0],
        [0.0, v_circ, 0.0]
    ])

    v0[0] = - (m[1] / m[0]) * v0[1] # make star stationary (set CoM frame)

    return x0, v0, m

def three_body():
    m = np.array([1.0, 1.0, 1.0])

    x0 = np.array([
        [-1.0, 0.0, 0.0],
        [ 1.0, 0.0, 0.0],
        [ 0.0, 0.5, 0.0]
    ])

    v0 = np.array([
        [ 0.0, -0.3, 0.0],
        [ 0.0,  0.3, 0.0],
        [ 0.5,  0.0, 0.0]
    ])

    return x0, v0, m