import numpy as np
import matplotlib.pyplot as plt

m = 1
alpha = .5
g = 9.81
time_end = 10
dt = .01
time_points = np.arange(0, time_end, dt)
initial_velocities = [0, 10, -10]


def compute_position(vy):
    x = np.zeros_like(vy)
    for i in range(1, len(vy)):
        x[i] = x[i-1] + .5 * (vy[i] + vy[i-1]) * dt
    return x

plt.figure(figsize=(10,8))

for vy0 in initial_velocities:
    vy = np.loadtxt(f"data_vy0_{vy0}.txt",usecols=1)
    position = compute_position(vy)
    
    plt.plot(
        time_points,
        position,
        label = f'Initial $v_y(0)$ = {vy0} m/s' 
    )

plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.xlim(-1,5)
plt.ylim(-10,2)
plt.title("Position vs Time")
plt.legend()
plt.savefig("RobertoRamil_HW08-p2.pdf")
plt.show()