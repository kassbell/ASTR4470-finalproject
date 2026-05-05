import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--system", type=str, default="two_body")
args = parser.parse_args()

system = args.system

methods = ["euler", "leapfrog", "rk4"]

traj_data = {}
energy_data = {}

for method in methods:
    tag = f"{system}_{method}"
    
    traj_data[method] = np.load(f"data/traj_{tag}.npy")
    energy_data[method] = np.load(f"data/energy_{tag}.npy")

# orbit comparison
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for ax, method in zip(axes, methods):
    traj = traj_data[method]
    
    for i in range(traj.shape[1]):
        ax.plot(traj[:, i, 0], traj[:, i, 1])
    
    ax.set_title(method.capitalize())
    ax.set_aspect('equal')

plt.tight_layout()
plt.savefig(f"plots/orbit_comparison_{system}.png", dpi=200)
plt.show()

# energy comparison
plt.figure(figsize=(6,4))

for method in methods:
    energy = energy_data[method]
    plt.plot(energy, label=method)

plt.xlabel("Time step")
plt.ylabel("Total Energy")
plt.title(f"Energy Comparison ({system})")
plt.legend()

plt.savefig(f"plots/energy_comparison_{system}.png", dpi=200)
plt.show()

# relative energy error
plt.figure(figsize=(6,4))

for method in methods:
    energy = energy_data[method]
    rel_error = (energy - energy[0]) / energy[0]
    plt.plot(rel_error, label=method)

plt.xlabel("Time step")
plt.ylabel("Relative Energy Error")
plt.title(f"Energy Error ({system})")
plt.legend()

plt.savefig(f"plots/energy_error_{system}.png", dpi=200)
plt.show()