import numpy as np
import matplotlib.pyplot as plt
import sys


def calc_motion(a_x, a_y, v0_x, v0_y, t, x0, y0):
    x = x0 + v0_x * t + .5 * a_x * t**2
    y = y0 + v0_y * t + .5 * a_y * t**2
    v_x = v0_x + a_x * t
    v_y = v0_y + a_y * t
    return x, y, v_x, v_y

if len(sys.argv)>1:
    ground_file = sys.argv[1]
    with open(ground_file) as f:
        data = f.read()
    data_list = data.replace('\n', ',').split(',')
    y_ground = [float(x.strip()) for x in data_list if x.strip()]
            
else:
    print ("Exptected ground file after the .py script.\n Now using the Defautl ground of y=0")
    y_ground = (np.zeros(2000))

g = 9.8
t_engine_on = 51
a_acel_on = (.69, 4.3) #a_x, a_y
a_acel_off = (-.97, -g) #a_x, a_y when off
a_slow_down = (.61, 6.9)

t_engine_on = np.linspace(0, t_engine_on, 100)
t_engine_off = np.linspace(t_engine_on[-1], 80, 100)


x_ground = (np.arange(1,len(y_ground)+1))
initial_pos_x = int(input("Please Enter the intital postition on the x axis (in meters)"))
initial_pos_y = y_ground[initial_pos_x]

#Calc x,y,vx, vy when the engine is on
x_on, y_on, v_x_on, v_y_on = calc_motion(a_acel_on[0], a_acel_on[1], 0, 0, t_engine_on, initial_pos_x, initial_pos_y)
#Calc x,y,vx, vy when the engine is off
x_off, y_off, v_x_off, v_y_off = calc_motion(a_acel_off[0], a_acel_off[1], v_x_on[-1], v_y_on[-1], t_engine_off, x_on[-1], y_on[-1])


plt.figure()

#Plot 1 Main plot on left
ax1 = plt.subplot2grid((4,2),(0,0), rowspan=4)
ax1.plot(
    x_ground,
    y_ground,
    color = "black",
    linewidth = 3
)
ax1.plot(
    x_on,
    y_on,
    color = "red",
    label = f"Engine on, $a = (.69, 4.3)m/s^2$"
)
ax1.scatter(
    x_on[-1],
    y_on[-1],
    color = "red",
    marker= '*',
)
ax1.text(
    x_on[0],
    y_on[-4],
    s='Engine turns off',
    color = 'r',
)
ax1.plot(
    x_off,
    y_off,
    color = "b",
    label = f"Engine off, $a = (-.97, -9.8)m/s^2$"
)
ax1.scatter(
    x_off[-1],
    y_off[-1],
    color = "b",
    marker= 's',
)
ax1.text(
    x_off[0],
    y_off[-4],
    s='Engine turns off',
    color = 'b',
)

tick = np.arange(0,2000,500)
ax1.set_xticks(tick)
tick = np.arange(0,11000, 1000)
ax1.set_yticks(tick)
ax1.set_xticklabels([0.0, 0.5, 1.0, 1.5])
ax1.set_yticklabels([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, "", "", ""])
ax1.set_xlabel('x (km)')
ax1.set_ylabel('y (km)')
ax1.set_xlim(0,3000)
ax1.legend()

#plot 2
ax2 = plt.subplot2grid((4,2),(0, 1))
ax2.plot(
    
)
ax2.set_xlabel('t (min)')
ax2.set_ylabel('position (km)')

#plot 3
ax3 = plt.subplot2grid((4,2),(1, 1))

ax3.set_xlabel('t (min)')
ax3.set_ylabel('v (m/s)')

#plot 4
ax4 = plt.subplot2grid((4,2),(2, 1))

ax4.set_xlabel('t (min)')
ax4.set_ylabel(f'$v_x$ (km)')

#plot 5
ax5 = plt.subplot2grid((4,2),(3, 1))

ax5.set_xlabel('t (min)')
ax5.set_ylabel(f'$v_y$ (km)')


plt.tight_layout()
plt.savefig("RobertoRamil_M1_p1.pdf")
plt.show()









# total_time = 120
# t_engine_on = 51
# t_engine_off = 36.05 * 60
# t_slow_down = (36.05) / np.sqrt(.83**2 + 7.01**2)

# t_engine_on = np.linspace(0,t_engine_on/60, 100)
# t_engine_off = np.linspace(t_engine_on[-1], t_slow_down, 100)

# a_engine_on_x, a_engine_on_y = 6.0, 3.74
# a_engine_off_x, a_engine_off_y = -.97, -g
# a_slow_down = (.83, -7.01)

# x_on = initial_pos_x + 0 * t_engine_on + .5 * a_engine_on_x * t_engine_on**2
# x_off = x_on[-1] + 0 * t_engine_off + .5 * a_engine_off_x * t_engine_off**2

# y_on = initial_pos_y + 0 * t_engine_on + .5 * a_engine_on_y * t_engine_on**2
# y_off = y_on[-1] + 0 * t_engine_off + .5 * a_engine_off_y * t_engine_off**2

# v_x_on = a_engine_on_x * t_engine_on
# v_x_off = a_engine_off_x * t_engine_off

# v_y_on = a_engine_on_y * t_engine_on
# v_y_off = a_engine_off_y * t_engine_off