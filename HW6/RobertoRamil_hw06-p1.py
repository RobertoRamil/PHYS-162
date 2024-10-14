import numpy as np
import matplotlib.pyplot as plt
#asdfa
def Xpos(t, th0):
    deg = np.deg2rad(th0)
    return x0 + v0*t*np.cos(deg)

def Ypos(t,th0):
    deg = np.deg2rad(th0)
    return y0 + v0*t*np.sin(deg)-1/2*(g)*(t**2)

def Range(th0):
    deg = np.deg2rad(th0)
    return (v0**2)/g *(np.sin(2*deg))

def gFunction(x):
    return x**(1/3)

def bisection(int1, int2, prec):
    while (int1 - int2)/2 > prec:
        xmid = (int1 - int2)/2
        t = (xmid - x0)/(v0*np.cos(np.deg2rad(th0)))
        ymid = Ypos(t,th0)
        
        if ymid > gFunction(xmid):
            int1 = xmid
        else:
            int2 = xmid
    return (int1+int2)/2 
        
v0_vals = [7, 17, 27]
x0, y0, th0,  g = 0, 5, 27, 9.8
xvals = np.linspace(0, 15, 300)
gYvals = gFunction(xvals)

plt.figure()

plt.plot(
    xvals,
    gYvals,
    label = r'Ground $y(x) = x^{1/3}$'
)
landing_points =[]
for v0 in v0_vals:
    xleft = 0
    xright = 15
    prec = .01
    
    landx = bisection(xright, xleft, prec)
    tland = (landx -x0) / (v0 * np.cos(np.deg2rad(th0)))
    landy = Ypos(tland, th0)
    
    landing_points.append((v0,landx, landy))
    
    t_flight = 2 * v0 * np.sin(np.deg2rad(th0))/g
    t_val = np.linspace(0, t_flight, 500)
    
    plt.plot(Xpos(t_val, th0), Ypos(t_val, th0),
             label = f'$v_0$ = {v0} m/s'
             )
    plt.scatter(
        landx, landy,
        
    )
    
    
    


plt.ylabel("y (m)")
plt.xlabel("x (m)")
plt.xlim(0,15)
plt.ylim(0,10)
plt.legend()
plt.savefig("RobertoRamil_hw06-p1_fig.pdf")
plt.show()

for v, x, y in landing_points:
    print(f'v0 = {v} m/s, (x, y) = ({x:.2f}, {y:.2f}) m')