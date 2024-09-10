import matplotlib.pyplot as plt
import numpy as np


x0, y0 = 0, 0
v0 = 20 #m/s
g = 9.8 #m/s^2
deg = 0




def Xpos(t, theta0):
    deg = np.deg2rad(theta0)
    return x0 + v0*t*np.cos(deg)

def Ypos(t,theta0):
    deg = np.deg2rad(theta0)
    return y0 + v0*t*np.sin(deg)-1/2*(g)*(t**2)

def Range(theta0):
    deg = np.deg2rad(theta0)
    return (v0**2)/g *(np.sin(2*deg))

plt.figure("A")

theta0 = 45
t = np.arange(0, Range(theta0), .1)

plt.plot(Xpos(t, theta0), Ypos(t, theta0),
         linestyle = "--",
         color="red",
         label = "A 45 deg"
)
plt.plot([Range(theta0)],[0],
         marker = '*',
         color = "red"
)

theta0 = 40
t = np.arange(0, Range(theta0),.1)
plt.plot(Xpos(t,theta0), Ypos(t,theta0),
         linestyle = "--",
         color="green",
         label = "A 40 deg"
)
plt.plot([Range(theta0)],[0],
         marker = '*',
         color = "green"
)

theta0 = 50
t = np.arange(0, Range(theta0),.1)
plt.plot(Xpos(t,theta0), Ypos(t,theta0),
         linestyle = "--",
         color="blue",
         label = "A 50 deg"
)

plt.plot([Range(theta0)],[0],
         marker = '*',
         color = "blue"
)



plt.title("Projectiles")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.xlim(-.5, 48)
plt.ylim(-.5, 20)
plt.legend()
plt.savefig("RobertoRamil_hw02-p2_figA.pdf")
plt.show()

plt.figure("B")
y0 = 5 #Chaning initial height of proj

theta0 = 45
t = np.arange(0, Range(theta0),.1)
plt.plot(Xpos(t,theta0),Ypos(t,theta0),
         linestyle = "-.",
         color = "red",
         label = 'B 45 deg'
)
plt.plot([Range(theta0)],[0],
         marker = '*',
         color = "red"
)


theta0 = 40
t = np.arange(0, Range(theta0),.1)
plt.plot(Xpos(t,theta0),Ypos(t,theta0),
         linestyle = "-.",
         color = "green",
         label = 'B 40 deg'
)
plt.plot([Range(theta0)],[0],
         marker = '*',
         color = "green"
)

theta0 = 50
t = np.arange(0, Range(theta0),.1)
plt.plot(Xpos(t,theta0),Ypos(t,theta0),
         linestyle = "-.",
         color = "blue",
         label = 'B 50 deg'
)
plt.plot([Range(theta0)],[0],
         marker = '*',
         color = "blue"
)

plt.title("Projectiles")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.xlim(-.5, 48)
plt.ylim(-.5, 20)

plt.legend()

plt.savefig("RobertoRamil_hw02-p2_figB.pdf")
plt.show()

print("It changes since the inital height will change the angle of the projectile")
print("since the second equation involves yoru initla height it addes a number that")
print("is then taken into effect chaning how far the projectile can go")