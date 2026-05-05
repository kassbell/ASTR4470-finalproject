import numpy as np
import matplotlib.pyplot as plt
import argparse

from src.simulation import run_simulation
import src.systems as systems

# ---------------------------
# CLI arguments
# ---------------------------
parser = argparse.ArgumentParser()

parser.add_argument("--system", type=str, default="two_body",
                    choices=["two_body", "three_body"])

parser.add_argument("--method", type=str, default="leapfrog",
                    choices=["euler", "leapfrog", "rk4"])

parser.add_argument("--dt", type=float, default=0.001)
parser.add_argument("--nsteps", type=int, default=10000)

args = parser.parse_args()

if args.system == "two_body":
    x0, v0, m = systems.two_body()
elif args.system == "three_body":
    x0, v0, m = systems.three_body()

# run
traj, energy = run_simulation(
    x0, v0, m,
    dt=args.dt,
    nsteps=args.nsteps,
    method=args.method
)

# save data
tag = f"{args.system}_{args.method}"

np.save(f"data/traj_{tag}.npy", traj)
np.save(f"data/energy_{tag}.npy", energy)

# plot orbit
plt.figure()

colors = ['blue', 'orange', 'green', 'red', 'purple']

for i in range(len(m)):
    plt.plot(traj[:, i, 0], traj[:, i, 1], color=colors[i % len(colors)], label=f"Body {i}")
    plt.scatter(traj[0, i, 0], traj[0, i, 1], marker='x', color=colors[i % len(colors)])
    plt.scatter(traj[-1,i,0], traj[-1,i,1], color=colors[i % len(colors)])

plt.gca().set_aspect('equal')
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Orbit ({tag})")
plt.legend()

plt.savefig(f"plots/orbit_{tag}.png", dpi=200)
plt.close()

# plot energy
plt.figure()
plt.plot(energy)
plt.title(f"Energy ({tag})")

plt.savefig(f"plots/energy_{tag}.png", dpi=200)
plt.close()

# run using python run_simulation.py --system [choice] --method [choice]