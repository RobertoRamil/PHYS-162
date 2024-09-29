import numpy as np
import matplotlib.pyplot as plt
import sys

def Xpos(t, v0, th0):
    deg = np.deg2rad(th0)
    return x0 + v0*t*np.cos(deg)

def Ypos(t, y0, v0, th0):
    deg = np.deg2rad(th0)
    return y0 + v0*t*np.sin(deg)-1/2*(g)*(t**2)


def plot_traj(y0,v0,th0,tmax,color):
    t_vals = np.linspace(0, tmax, num=500)
    x_vals = Xpos(t_vals, v0, th0)
    y_vals = Ypos(t_vals, y0, v0, th0)
    
    plt.plot(x_vals, y_vals, color = color, 
             label = f'y0 = {y0}m, v0 = {v0}m/s, th0 = {th0}°')
    
    plt.plot(x_vals[-1], y_vals[-1], marker = 'o', color=color)

def tland(y0, v0, th0):
    dt = .01
    t=0
    while True:
        t+=dt
        if Ypos(t,y0,v0,th0) <0:
            return t

x0, g = 0, 9.8

if len(sys.argv) <2:
    print("Usage: python3 RobertoRamil_hw04-p1.py angles")
    print("Expected name of file then a list of numbers for different angles")
    sys.exit(1)

plt.figure()
y0 = float(input("Entre the initial height for y0 (in meters): "))
angles = list(map(float, sys.argv[1:]))

with open("v0vals.txt", "r") as file:
    stringvals = file.readline().split(',')
    v0_vals = list(map(int, stringvals))
    
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
color_index = 0

for v0 in v0_vals:
    for th0 in angles:
        tmax = tland(y0, v0, th0)
        plot_traj(y0, v0, th0, tmax, colors[color_index %len(colors)])
        color_index += 1

plt.legend()
plt.title("Projctiles")
plt.xlabel("Time")
plt.ylabel("Height")
plt.savefig("RobertoRamil_hw04-p1_fig.pdf")
plt.show()