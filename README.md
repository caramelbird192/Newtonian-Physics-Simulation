# Newtonian Physics Simulation

A collection of small Python simulations that demonstrate how Euler's method can be used to evolve Newtonian systems numerically.

The project keeps the core ideas of the reference examples but uses different notation, parameters, structure, and plotting choices.

**Included simulations**

**Air drag**

A falling body is evolved under gravity and a v² drag force. The program records position, velocity, and acceleration and plots all three quantities against time.

**Orbital motion**

A test particle moves in the gravitational field of a fixed central mass. By changing the initial velocity, the numerical trajectory can produce different orbital shapes.

**Rutherford scattering**

A positively charged projectile is deflected by a repulsive Coulomb force from a fixed nucleus. The impact parameter controls the amount of deflection.

**Running the examples**

Install the required packages with:

```bash
pip install numpy matplotlib
```

Then run any example with Python, for example:

```bash
python air_drag.py
python orbit.py
python rutherford_scattering.py
```

The simulations are intended as simple demonstrations of numerical integration rather than high precision solvers. Decreasing the time step generally improves the approximation while increasing the computational cost.
