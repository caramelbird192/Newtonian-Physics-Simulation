import numpy as np
import matplotlib.pyplot as plt

# Dimensionless two body test particle model.
G = 1.0
central_mass = 1.0
dt = 0.002
total_time = 20.0

steps = int(total_time / dt)
x = np.empty(steps + 1)
y = np.empty(steps + 1)
vx = np.empty(steps + 1)
vy = np.empty(steps + 1)

x[0], y[0] = 1.0, 0.0
vx[0], vy[0] = 0.0, 0.85

for i in range(steps):
    radius_sq = x[i] ** 2 + y[i] ** 2
    radius = np.sqrt(radius_sq)
    ax = -G * central_mass * x[i] / radius**3
    ay = -G * central_mass * y[i] / radius**3

    vx[i + 1] = vx[i] + ax * dt
    vy[i + 1] = vy[i] + ay * dt
    x[i + 1] = x[i] + vx[i] * dt
    y[i + 1] = y[i] + vy[i] * dt

plt.figure(figsize=(7, 7))
plt.plot(x, y, label="test-particle path")
plt.scatter([0], [0], s=80, label="central mass")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Euler integration of a gravitational orbit")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
