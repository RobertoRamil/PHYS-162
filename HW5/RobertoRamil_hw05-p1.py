import numpy as np
import matplotlib.pyplot as plt

def Xpos(t, th0):
    deg = np.deg2rad(th0)
    return x0 + v0*t*np.cos(deg)

def Ypos(t,th0):
    deg = np.deg2rad(th0)
    return y0 + v0*t*np.sin(deg)-1/2*(g)*(t**2)

def Xvel(th0):
    deg = np.deg2rad(th0)
    return v0 *np.cos(deg)

def Yvel(t, th0):
    deg = np.deg2rad(th0)
    return v0 * np.sin(deg) -g *t

def Velocity(t,th0):
    vx = Xvel(th0)
    vy = Yvel(t, th0)
    return np.sqrt(vx**2 + vy**2)

def Range(th0):
    deg = np.deg2rad(th0)
    return (v0**2)/g *(np.sin(2*deg))
        
v0, x0, y0, th0,  g = 25, 0, 15, 55, 9.8
t = np.linspace(0, 2*v0*np.sin(np.deg2rad(th0))/g,500)



plt.figure()
plt.suptitle("Projectile Motion")


#plot 1 with x(m) and time
ax1 = plt.subplot2grid((3,3),(0,0))
ax1.plot(
    t,
    Xpos(t, th0),
    color = "b"
)
ax1.set_ylabel("x (m)")
ax1.set_ylim(0,60)
ax1.set_xlim(0, t.max())

#plot 2 with y(m) and time
ax2 = plt.subplot2grid((3,3),(1,0))
ax2.plot(
    t,
    Ypos(t, th0),
    color = "green"
)
ax2.set_ylabel("y (m)")
ax2.set_ylim(0,40)
ax2.set_xlim(0,t.max())


#plot 3 with velocity(m/s) and time
ax3 = plt.subplot2grid((3,3),(2,0))
ax3.plot(
    t, Xvel(th0) * np.ones_like(t),
    label = "$v_x(t)$",
    color = "b"
)
ax3.plot(
    t, Yvel(t, th0),
    label = "$v_y(t)$",
    color = 'g'
)
ax3.plot(
    t, Velocity(t, th0),
    label = "$|v_y(t)|$",
    color = 'r'
)
ax3.set_ylabel("Velocity (m/s)")
ax3.set_xlabel("time t (s)")
ax3.set_ylim(-30,30)
ax3.set_xlim(0,t.max())
ax3.legend()


#plot 4 with y(m) and x(m)
ax4 = plt.subplot2grid((3,3),(0,1),rowspan=3)
ax4.plot(
    Xpos(t, th0),
    Ypos(t, th0),
    color = 'r'
)
ax4.set_ylabel("y (m)")
ax4.set_xlabel("x (m)")
ax4.set_ylim(0,40)
ax4.set_xlim(0,70)
ax4.text(20,10, f'$y_0$ = {y0} m\n$v_0$ = {v0} m/s\n$\\theta_0$ = {th0}°')




plt.savefig("RobertoRamil_hw05-p1_fig1.pdf")
plt.show()