import numpy as np
import matplotlib.pyplot as plt

m = 1
alpha = .5
g = 9.81
time_end = 10
dt = .01

def drag_force(vy):
    return alpha * vy**2

def dv_dt(vy,t):
    s = np.sign(vy)
    return (-m * g - drag_force(vy) * s) / m

time_points = np.arange(0, time_end, dt)

def solve_velocity(vy0):
    vy = np.zeros_like(time_points)
    vy[0] = vy0
    for i in range(1, len(time_points)):
        vy[i] = vy[i-1] + dv_dt(vy[i-1], time_points[i-1]) *dt
    return vy

initial_velocities = [0, 10, -10]

plt.figure(figsize=(10,8))

for vy0 in initial_velocities:
    vy = solve_velocity(vy0)
    drag = drag_force(vy)
    gravitational_force = m * g * np.ones_like(vy)
    
    plt.subplot(1, 2, 1)
    plt.plot(
        time_points,
        vy,
        label = f'Initial $v_y(0)$ = {vy0} m/s'
    )
    plt.xlabel('Time (s)')
    plt.ylabel("Velcoity (m/s)")
    plt.xlim(-1,2)
    plt.title("Velcoity vs Time")
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(
        time_points, 
        drag,
        label = f'Initial $v_y(0)$ = {vy0} m/s'
    )
    plt.xlabel("Time (s)")
    plt.ylabel("Drag Force (N)")
    plt.xlim(-1,5)

    plt.title("Drag Foce vs Time")
    plt.legend()
      
    plt.plot(
        time_points,
        gravitational_force,
        label = f'Gravitational Force: Initial $v_y(0)$ = {vy0} m/s'
    )
    plt.xlim(-1,2)
    plt.legend()
    
plt.tight_layout()
plt.savefig("RobertoRamil_HW08-p1.pdf")
plt.show()

def save_data(vy0):
    vy = solve_velocity(vy0)
    drag = drag_force(vy)
    data = np.column_stack((time_points, vy, drag))
    filename = f"data_vy0_{vy0}.txt"
    np.savetxt(filename, data)
    print(f"data saved to {filename}")
    
for vy0 in initial_velocities:
    save_data(vy0)

print("")    
print("I get the first part but i dont know if the rest is correct.")
print("Since it all just converges after a few seconds of flight.")
print("No matter what it said using differet start points it still")
print("just ended up at thes same thing as the rest")