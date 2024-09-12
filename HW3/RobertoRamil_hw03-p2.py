import sys
import matplotlib.pyplot as plt
import numpy as np

x0, y0, v0, th0, g = 0, 0, 0, 0, 9.8

if len(sys.argv) != 4:
    print("Usage: python3 RobertoRamil_hw03-p2.py y0 v0 th0")
    print("Expected name of file then 3 numbers for y0, v0, th0 respectfully")
    sys.exit(1)


y0 = float(sys.argv[1])
v0 = float(sys.argv[2])
th0 = float(sys.argv[3])


def Xpos(t, th0):
    deg = np.deg2rad(th0)
    return x0 + v0*t*np.cos(deg)

def Ypos(t,th0):
    deg = np.deg2rad(th0)
    return y0 + v0*t*np.sin(deg)-1/2*(g)*(t**2)

def Range(th0):
    deg = np.deg2rad(th0)
    return (v0**2)/g *(np.sin(2*deg))

t = np.arange(0, Range(th0),.01)

plt.figure("A")

plt.plot(Xpos(t,th0),
         Ypos(t,th0),
         linestyle = '-',
         color = 'red',
         label = f'y₀ = {y0:.1f} m, v₀ = {v0:.1f} m/s, th₀ = {th0:.1f}\u00b0'
)


plt.legend()
plt.title("Projectile from Inserted Values")
plt.ylim(bottom = 0)
plt.xlim(0,40)
plt.savefig("RobertoRamil_hw03-p2_fig.pdf")
plt.show()