import numpy as np
import matplotlib.pyplot as plt

# Numerical model for a falling object with quadratic drag.
dt = 0.05
total_time = 8.0
g = 9.81
drag_coefficient = 0.018
initial_height = 2.5

n_steps = int(total_time / dt) + 1
time = np.linspace(0.0, total_time, n_steps)
height = np.empty(n_steps)
velocity = np.empty(n_steps)
acceleration = np.empty(n_steps)

height[0] = initial_height
velocity[0] = 0.0
acceleration[0] = -g

for i in range(n_steps - 1):
    drag_accel = -drag_coefficient * velocity[i] * abs(velocity[i])
    acceleration[i] = -g + drag_accel

    # Explicit Euler update.
    velocity[i + 1] = velocity[i] + acceleration[i] * dt
    height[i + 1] = height[i] + velocity[i] * dt

acceleration[-1] = -g - drag_coefficient * velocity[-1] * abs(velocity[-1])

fig, axes = plt.subplots(3, 1, figsize=(7, 8), sharex=True)
axes[0].plot(time, height)
axes[0].set_ylabel("height")
axes[0].grid(True)

axes[1].plot(time, velocity)
axes[1].set_ylabel("velocity")
axes[1].grid(True)

axes[2].plot(time, acceleration)
axes[2].set_ylabel("acceleration")
axes[2].set_xlabel("time")
axes[2].grid(True)

fig.suptitle("Falling object with quadratic air resistance")
fig.tight_layout()
plt.show()
