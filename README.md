# ASTR4470 Final Project: N-Body Gravitational Simulations

This project investigates numerical methods for solving the gravitational N-body problem using Python. The simulation models the motion of particles interacting through Newtonian gravity and compares the performance of several numerical integrators, including:

- Euler Method
- Leapfrog Integrator
- Fourth-Order Runge-Kutta (RK4)

The project focuses on orbital stability, energy conservation, and the emergence of chaotic behavior in multi-body systems. Simulations include both stable two-body orbital systems and chaotic three-body interactions.

---

## Scientific Motivation

Analytical solutions exist for the two-body gravitational problem, but systems containing three or more interacting bodies generally do not have closed-form solutions. Numerical methods are therefore essential for studying realistic astrophysical systems such as:

- Planetary systems
- Star clusters
- Binary stars
- Galactic dynamics
- Accretion environments

This project explores how different numerical integration schemes affect the accuracy and long-term stability of gravitational simulations.

---

## Features

- Newtonian gravitational force calculations
- Modular simulation framework
- Multiple numerical integrators:
  - Euler
  - Leapfrog
  - RK4
- Two-body orbital simulations
- Three-body chaotic systems
- Energy conservation diagnostics
- Orbit visualization
- Integrator comparison tools
- Command-line simulation interface

---

## Repository Structure

```text
ASTR4470-finalproject/
│
├── src/
│   ├── __init__.py
│   ├── forces.py
│   ├── integrators.py
│   ├── analysis.py
│   ├── simulation.py
│   └── systems.py
│
├── notebooks/
│   ├── two_body_demo.ipynb
│   ├── three_body_demo.ipynb
│   └── animation_demo.ipynb
│
├── data/
│
├── plots/
│   ├── orbit_comparison_two_body.png
│   ├── energy_comparison_two_body.png
│   ├── energy_error_two_body.png
│   └── ...
│
├── run_simulation.py
├── compare_integrators.py
│
├── README.md
├── requirements.txt
└── .gitignore 
```

---

## Installation

Clone the repository:

```text
git clone git@github.com:kassbell/ASTR4470-finalproject.git
cd ASTR4470-finalproject
```

Install dependencies:

```text
pip install -r requirements.txt
```

---

## Running Simulations

The main simulation script supports different systems and numerical integrators through command-line arguments.

Example: Two-Body Leapfrog Simulation
```text
python run_simulation.py --system two_body --method leapfrog
```

Example: Three-Body RK4 Simulation
```text
python run_simulation.py --system three_body --method rk4
```

--- 

## Command-Line Options

### Systems:
- two_body
- three_body

### Integrators:
- euler
- leapfrog
- rk4

### Optional Parameters:
```text
--dt       timestep size
--nsteps   number of simulation steps
```

Example:
```text
python run_simulation.py --system two_body --method leapfrog --dt 0.001 --nsteps 10000
```

---

## Comparing Integrators

The comparison script loads saved simulation data and generates orbit and energy comparison plots.

Example
```text
python compare_integrators.py --system two_body
```
This generates:
- Orbit comparison plots
- Total energy comparison plots
- Relative energy error plots

--- 

## Numerical Methods

### Euler Method

The Euler method is simple and computationally inexpensive but suffers from significant energy drift and poor long-term stability.

### Leapfrog Integrator

The leapfrog method is symplectic, meaning it preserves the geometric structure of Hamiltonian systems and conserves energy much more effectively over long timescales.

### RK4

The fourth-order Runge-Kutta method provides high short-term accuracy but does not preserve energy as effectively as leapfrog in long simulations.

---

## Results

### Two-Body Simulations

Two-body systems demonstrate stable orbital motion and provide a baseline for comparing integrator performance.

Key findings:
- Euler orbits spiral over time due to energy drift.
- RK4 performs well short-term but slowly accumulates error.
- Leapfrog maintains stable closed orbits and bounded energy oscillations.

### Three-Body Simulations

Three-body systems exhibit chaotic behavior and strong sensitivity to initial conditions. Small perturbations lead to dramatically different trajectories over time.

These simulations demonstrate the necessity of numerical methods for studying realistic gravitational systems.

--- 

## Output Files

Simulation outputs are automatically saved to:

<code>data/</code>
- Trajectories (<code>traj_*.npy</code>)
- Energy histories (<code>energy_*.npy</code>)

<code>plots/</code>
- Orbit visualizations
- Energy comparison plots
- Relative energy error plots

File names are automatically labeled by system and integrator.

Example:
```text
traj_two_body_leapfrog.npy
energy_three_body_rk4.npy
orbit_two_body_leapfrog.png
```

--- 

## Dependencies
- numpy
- matplotlib
- ipython

---

## Future Improvements

Potential future extensions include:
- Adaptive timestep methods
- Barnes-Hut tree algorithms
- Larger N-body systems
- Collision handling
- Softened gravity
- GPU acceleration
- 3D visualization tools

---

## Author
Kass Bell \
ASTR4470 Final Project \
University of Virginia

---

## License

This project is intended for educational and academic use.