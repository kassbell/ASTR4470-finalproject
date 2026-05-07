import numpy as np
import argparse

# ---------------------------
# CLI arguments
# ---------------------------
parser = argparse.ArgumentParser()

parser.add_argument("--system", type=str, default="two_body",
                    choices=["two_body", "three_body"])

args = parser.parse_args()

system = args.system

methods = ["euler", "leapfrog", "rk4"]

print()
print(f"Energy Analysis: {system}")
print("-" * 40)

for method in methods:

    tag = f"{system}_{method}"

    energy = np.load(f"data/energy_{tag}.npy")

    E0 = energy[0]
    Efinal = energy[-1]

    rel_drift = (Efinal - E0) / E0

    max_error = np.max(np.abs((energy - E0) / E0))

    print(f"{method.upper():<12}")
    print(f"  Initial Energy: {E0:.6e}")
    print(f"  Final Energy:   {Efinal:.6e}")
    print(f"  Relative Drift: {rel_drift:.6e}")
    print(f"  Max Rel Error:  {max_error:.6e}")
    print()