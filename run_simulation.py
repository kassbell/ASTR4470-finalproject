import numpy as np
import matplotlib.pyplot as plt
from src.simulation import run_simulation
import src.systems as systems

# choose system
x0, v0, m = systems.two_body()
# x0, v0, m = systems.three_body()

# simulation params
dt = 0.001
nsteps = 10000

# run
traj, energy = run_simulation(x0, v0, m, dt, nsteps, method="leapfrog")

# plot orbit
plt.plot(traj[:,1,0], traj[:,1,1])
plt.scatter(traj[:,0,0], traj[:,0,1])

plt.gca().set_aspect('equal')
plt.title("Orbit (Leapfrog)")
plt.savefig("plots/orbit.png", dpi=200)
plt.show()

# plot energy
plt.figure()
plt.plot(energy)
plt.title("Energy")
plt.savefig("plots/energy.png", dpi=200)
plt.show()

np.save("data/traj.npy", traj)
np.save("data/energy.npy", energy)

print("Energy shape:", energy.shape)
print("First 5 energy values:", energy[:5])