import sys
import matplotlib.pyplot as plt
import numpy as np

x0, y0, v0, th0, g = 0, 0, 0, 0, 9.8

'''if len(sys.argv) != 4:
    print("Usage: python3 RobertoRamil_hw03-p2.py y0 v0 th0")
    sys.exit(1)


y0 = float(sys.argv[1])
v0 = float(sys.argv[2])
th0 = float(sys.argv[3])

'''
def Xpos(t, th0):
    deg = np.deg2rad(th0)
    return x0 + v0*t*np.cos(deg)

def Ypos(t,th0):
    deg = np.deg2rad(th0)
    return y0 + v0*t*np.sin(deg)-1/2*(g)*(t**2)

def Range(th0):
    deg = np.deg2rad(th0)
    return (v0**2)/g *(np.sin(2*deg))


plt.figure("A")


plt.legend()
plt.savefig("RobertoRamil_hw03-p2_fig.pdf")
plt.show()