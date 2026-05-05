import numpy as np
import src.integrators as integrators
import src.analysis as analysis

def run_simulation(x0, v0, m, dt, nsteps, method="leapfrog"):
    '''
    Runs an N-body simulation.

    Returns:
        traj: (nsteps, N, 3)
        energy: (nsteps,)
    '''

    # choose integrator
    if method == "euler":
        step = integrators.step_euler
    elif method == "leapfrog":
        step = integrators.step_leapfrog
    elif method == "rk4":
        step = integrators.step_rk4
    else:
        raise ValueError("Invalid method")

    x = x0.copy()
    v = v0.copy()

    traj = []
    energy = []

    for n in range(nsteps):
        x, v = step(x, v, m, dt)
        traj.append(x.copy())
        energy.append(analysis.compute_energy(x, v, m))

    return np.array(traj), np.array(energy)