import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import argparse

# ---------------------------
# CLI arguments
# ---------------------------
parser = argparse.ArgumentParser()

parser.add_argument("--system", type=str, default="two_body",
                    choices=["two_body", "three_body"])

parser.add_argument("--method", type=str, default="leapfrog",
                    choices=["euler", "leapfrog", "rk4"])

parser.add_argument("--stride", type=int, default=10,
                    help="Frame downsampling factor")

args = parser.parse_args()

# ---------------------------
# Load trajectory data
# ---------------------------
tag = f"{args.system}_{args.method}"

traj = np.load(f"data/traj_{tag}.npy")

# downsample for speed
traj = traj[::args.stride]

N = traj.shape[1]

# ---------------------------
# Plot setup
# ---------------------------
fig, ax = plt.subplots(figsize=(6,6))

colors = ['blue', 'orange', 'green', 'red', 'purple']

# axis limits from data
xmin = np.min(traj[:,:,0])
xmax = np.max(traj[:,:,0])

ymin = np.min(traj[:,:,1])
ymax = np.max(traj[:,:,1])

padding = 0.1 * max(xmax - xmin, ymax - ymin)

ax.set_xlim(xmin - padding, xmax + padding)
ax.set_ylim(ymin - padding, ymax + padding)

ax.set_aspect('equal')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"{args.system} ({args.method})")

# initialize artists
points = []
trails = []

for i in range(N):
    trail, = ax.plot([], [], color=colors[i % len(colors)], lw=1)
    point, = ax.plot([], [], 'o', color=colors[i % len(colors)])

    trails.append(trail)
    points.append(point)

# ---------------------------
# Animation function
# ---------------------------
trail_length = 100

def update(frame):

    start = max(0, frame - trail_length)

    for i in range(N):

        trails[i].set_data(
            traj[start:frame, i, 0],
            traj[start:frame, i, 1]
        )

        points[i].set_data(
            [traj[frame, i, 0]],
            [traj[frame, i, 1]]
        )

    return trails + points

# ---------------------------
# Create animation
# ---------------------------
anim = FuncAnimation(
    fig,
    update,
    frames=len(traj),
    interval=30,
    blit=True
)

# ---------------------------
# Save movie
# ---------------------------
outfile = f"plots/movie_{tag}.gif"

anim.save(outfile, writer="pillow", fps=30)

print(f"Saved animation to {outfile}")