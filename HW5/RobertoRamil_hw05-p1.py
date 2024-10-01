import numpy as np
import matplotlib.pyplot as plt

def Xpos(t, v0, th0):
 deg = np.deg2rad(th0)
 return x0+v0*t*np.cos(deg)

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

#plot 1 with x(m) and time
ax1 = plt.subplot2grid((2,2),(0,0))
ax1.plot(
    
)
ax1.set_ylabel("x (m)")

#plot 2 with y(m) and time
ax2 = plt.subplot2grid((2,2),(1,0))
ax2.plot(
    
)
ax2.set_ylabel("y (m)")


#plot 3 with velocity(m/s) and time
ax3 = plt.subplot2grid((2,2),(2,0))
ax3.plot(
    
)
ax3.set_ylabel("Velocity (m/s)")
ax3.set_xlabel("time t (s)")


#plot 4 with y(m) and x(m)
ax4 = plt.subplot2grid((2,2),(0,1),rowspan=3)
ax4.plot(
    
)
ax4.set_ylabel("y (m)")
ax4.set_xlabel("x (m)")



plt.legend()
plt.title("Projectile Motion")
plt.savefig("RobertoRamil_hw05-p1_fig1.pdf")
plt.show()