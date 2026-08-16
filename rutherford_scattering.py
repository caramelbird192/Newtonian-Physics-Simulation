import numpy as np
import matplotlib.pyplot as plt

# Repulsive Coulomb scattering in convenient arbitrary units.
C = 1.0
effective_charge = 2.0
impact_parameter = 2.5
initial_x = -12.0
initial_speed = 4.0
dt = 0.001
total_time = 7.0

steps = int(total_time / dt)
x = np.empty(steps + 1)
y = np.empty(steps + 1)
vx = np.empty(steps + 1)
vy = np.empty(steps + 1)

x[0], y[0] = initial_x, impact_parameter
vx[0], vy[0] = initial_speed, 0.0

for i in range(steps):
    r2 = x[i] ** 2 + y[i] ** 2
    r3 = r2 ** 1.5

    # Repulsive inverse square acceleration.
    ax = C * effective_charge * x[i] / r3
    ay = C * effective_charge * y[i] / r3

    vx[i + 1] = vx[i] + ax * dt
    vy[i + 1] = vy[i] + ay * dt
    x[i + 1] = x[i] + vx[i] * dt
    y[i + 1] = y[i] + vy[i] * dt

# Estimate the outgoing direction from the final velocity.
scattering_angle = np.arctan2(vy[-1], vx[-1])
print(f"Estimated scattering angle: {np.degrees(scattering_angle):.3f} degrees")

plt.figure(figsize=(8, 5))
plt.plot(x, y, label=f"b = {impact_parameter}")
plt.scatter([0], [0], s=90, label="target nucleus")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Numerical Rutherford scattering")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
