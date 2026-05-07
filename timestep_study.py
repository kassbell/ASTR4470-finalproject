import numpy as np
import matplotlib.pyplot as plt

from src.simulation import run_simulation
import src.systems as systems

# ---------------------------
# Simulation setup
# ---------------------------
x0, v0, m = systems.two_body()

methods = ["euler", "leapfrog", "rk4"]

dts = [1e-1, 5e-2, 1e-2, 5e-3, 1e-3]

nsteps_base = 1000

results = {}

# ---------------------------
# Run convergence study
# ---------------------------
for method in methods:

    errors = []

    for dt in dts:

        # keep total simulation time fixed
        nsteps = int(nsteps_base / dt)

        traj, energy = run_simulation(
            x0, v0, m,
            dt=dt,
            nsteps=nsteps,
            method=method
        )

        E0 = energy[0]
        Efinal = energy[-1]

        rel_error = abs((Efinal - E0) / E0)

        errors.append(rel_error)

        print(f"{method:10s} dt={dt:.1e} error={rel_error:.3e}")

    results[method] = errors

plt.figure(figsize=(6,4))

for method in methods:

    plt.loglog(
        dts,
        results[method],
        marker='o',
        label=method
    )

plt.xlabel("Timestep (dt)")
plt.ylabel("Relative Energy Drift")
plt.title("Integrator Convergence Study")

plt.legend()

plt.savefig("plots/timestep_convergence.png", dpi=200)

plt.show()