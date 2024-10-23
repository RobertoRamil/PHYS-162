import numpy as np
import matplotlib.pyplot as plt
import sys


def calc_motion(a_x, a_y, v0_x, v0_y, t, x0, y0):
    x = x0 + v0_x * t + .5 * a_x * t**2
    y = y0 + v0_y * t + .5 * a_y * t**2
    v_x = v0_x + a_x * t
    v_y = v0_y + a_y * t
    ssd = 0
    if a_y == -9.8:
        if y[-1] <= 3605:
            ssd = y[-1]
    return x, y, v_x, v_y, ssd

def int_check(num):
    try:
        return(int(num))
    except:
        num = input("\nInput was not a number.\nPlease Enter the intital postition on the x axis (in meters)")
        return(int_check(num))
    
if len(sys.argv)>1:
    ground_file = sys.argv[1]
    with open(ground_file) as f:
        data = f.read()
    data_list = data.replace('\n', ',').split(',')
    y_ground = [float(x.strip()) for x in data_list if x.strip()]
else:
    print ("Exptected ground file after the .py script.\n Now using the Default ground of y=0")
    y_ground = (np.zeros(2000))

g = 9.8
x_ground = (np.arange(1,len(y_ground)+1))
initial_pos_x = int_check(input("Please Enter the intital postition on the x axis (in meters)"))
initial_pos_y = y_ground[initial_pos_x]

slowdown_height = 3605

t_engine_on = 51
a_acel_on = (.69, 4.3) #a_x, a_y
t_engine_on = np.linspace(0, t_engine_on, 100) #making the array for the time that the engine will be on.
#Calc x,y,vx, vy when the engine is on
x_on, y_on, v_x_on, v_y_on, ssd = calc_motion(a_acel_on[0], a_acel_on[1], 0, 0, t_engine_on, initial_pos_x, initial_pos_y)

a_acel_off = (-.97, -9.8) #a_x, a_y when off
t_engine_off = np.linspace(t_engine_on[-1], 100, 100)
#Calc x,y,vx, vy when the engine is off
x_off, y_off, v_x_off, v_y_off, ssd = calc_motion(a_acel_off[0], a_acel_off[1], v_x_on[-1], v_y_on[-1], t_engine_off-t_engine_on[-1], x_on[-1], y_on[-1])
t_engine_off = np.linspace(t_engine_on[-1], ssd, 100)
print(ssd)
x_off, y_off, v_x_off, v_y_off, ssd = calc_motion(a_acel_off[0], a_acel_off[1], v_x_on[-1], v_y_on[-1], t_engine_on[-1]-t_engine_off, x_on[-1], y_on[-1])

a_slow_down = (.61, 6.9)
#placeholder numbers
t_slow_down = np.linspace(0,20,100)
#Calc x,y,vx,vy when it is slowing down
x_sd, y_sd, v_x_sd, v_y_sd, ssd = calc_motion(a_slow_down[0], a_slow_down[1], v_x_off[-1], v_y_off[-1],t_slow_down-t_engine_off[-1], x_off[-1], y_off[-1])
for i in y_sd:
    if i <= 0:
       l_point = i
       break

t_slow_down = np.linspace(0,-l_point,100)
x_sd, y_sd, v_x_sd, v_y_sd, ssd = calc_motion(a_slow_down[0], a_slow_down[1], v_x_off[-1], v_y_off[-1],t_slow_down-t_engine_off[-1], x_off[-1], y_off[-1])


t_engine_off = t_engine_off[::-1] #IDK why but this makes it work.
plt.figure(figsize=(10,8))


#Plot 1 Main plot on left
ax1 = plt.subplot2grid((4,2),(0,0), rowspan=4)
#Ground
ax1.plot(
    x_ground,
    y_ground,
    color = "black",
    linewidth = 3
)
#Rocket
ax1.plot(
    x_on,
    y_on,
    color = "red",
    label = f"Engine on, $a = (.69, 4.3)m/s^2$"
)
ax1.plot(
    x_off,
    y_off,
    color = "b",
    label = f"Engine off, $a = (-.97, -{g})m/s^2$"
)
ax1.plot(
    x_sd,
    y_sd,
    color = 'purple',
    label = f'Slow Down, $a = (.61, 6.9)m/s^2$'
)
#Scatter plots for the Symbols
ax1.scatter(
    x_on[-1],
    y_on[-1],
    color = "red",
    marker= '*',
)
ax1.scatter(
    x_off[-1],
    y_off[-1],
    color = "b",
    marker= 's',
)
ax1.scatter(
    x_sd[-1],
    y_sd[-1],
    color = 'purple',
    marker = 'v'
)
#Text for the Scatter Plots
ax1.text(
    x_on[0],
    y_on[-4],
    s='Engine turns off',
    color = 'r',
)
ax1.text(
    x_off[0],
    y_off[-4],
    s='Engine turns on',
    color = 'b',
)
ax1.text(
    x_sd[0],
    y_sd[-4],
    s='Landing Point',
    color = 'purple',
)

tick = np.arange(0,2000,500)
ax1.set_xticks(tick)
tick = np.arange(0,8000, 1000)
ax1.set_yticks(tick)
ax1.set_xticklabels([0.0, 0.5, 1.0, 1.5])
ax1.set_yticklabels([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
ax1.set_xlabel('x (km)')
ax1.set_ylabel('y (km)')
ax1.set_xlim(0,2000)
ax1.legend(loc = 'upper left')
#plot 2
ax2 = plt.subplot2grid((4,2),(0, 1))
ax2.plot(
    t_engine_on,
    x_on,
    color = 'r',
    linestyle = '-.'
)
ax2.plot(
    t_engine_on,
    y_on,
    color = 'r',
)
ax2.plot(
    t_engine_off+t_engine_on[-1],
    x_off,
    color = 'b',
    linestyle = '-.'
)
ax2.plot(
    t_engine_off+t_engine_on[-1],
    y_off,
    color = 'b',
)
ax2.plot(
    t_slow_down+t_engine_off[-1]+t_engine_on[-1],
    x_sd,
    color = 'purple',
    linestyle = '-.'
)
ax2.plot(
    t_slow_down+t_engine_off[-1]+t_engine_on[-1],
    y_sd,
    color = 'purple'
)
#Scatter
ax2.scatter(
    t_engine_on[-1],
    x_on[-1],
    color = 'r',
    marker='*'
)
ax2.scatter(
    t_engine_on[-1],
    y_on[-1],
    color = 'r',
    marker='*'
)
ax2.scatter(
    t_engine_off[-1]+t_engine_on[-1],
    x_off[-1],
    color = 'b',
    marker = 's'
)
ax2.scatter(
    t_engine_off[-1]+t_engine_on[-1],
    y_off[-1],
    color = 'b',
    marker = 's'
)
ax2.scatter(
    t_slow_down[-1]+t_engine_off[-1]+t_engine_on[-1],
    x_sd[-1],
    color = 'purple',
    marker = 'v'
)
ax2.scatter(
    t_slow_down[-1]+t_engine_off[-1]+t_engine_on[-1],
    y_sd[-1],
    color = 'purple',
    marker = 'v'
)

tick = np.arange(0,60*2,30)
ax2.set_xticks(tick)
tick = np.arange(0,7000, 2000)
ax2.set_yticks(tick)
ax2.set_xticklabels([0.0, 0.5, 1.0, 1.5])
ax2.set_yticklabels([0.0, 2.0, 4.0, 6.0])
ax2.set_xlabel('t (min)')
ax2.set_ylabel('position (km)')

#plot 3
v_on = np.sqrt(v_x_on**2 + v_y_on**2)
v_off = np.sqrt(v_x_off**2 + v_y_off**2)
v_sd = np.sqrt(v_x_sd**2 + v_y_sd**2)

if v_y_sd[-1] <= 5:
    print('Smooth landing')
elif v_y_sd[-1] >5 and v_y_sd[-1] <= 25:
    print('Rough Landing')
elif v_y_sd[-1] > 25:
    print('Crash Landing')

ax3 = plt.subplot2grid((4,2),(1, 1))
ax3.plot(
    t_engine_on,
    v_on,
    color = 'r'
)
ax3.plot(
    t_engine_off+t_engine_on[-1],
    v_off,
    color = 'b'
)
ax3.plot(
    t_slow_down+t_engine_off[-1]+t_engine_on[-1],
    v_sd,
    color = 'purple',
)
#Scatter
ax3.scatter(
    t_engine_on[-1],
    v_on[-1],
    color = 'r',
    marker = '*'
)
ax3.scatter(
    t_engine_off[-1]+t_engine_on[-1],
    v_off[-1],
    color = 'b',
    marker = 's'
)

ax3.scatter(
    t_slow_down[-1]+t_engine_off[-1]+t_engine_on[-1],
    v_sd[-1],
    color = 'purple',
    marker = 'v'
)

tick = np.arange(0,60*2,30)
ax3.set_xticks(tick)
ax3.set_yticks([0,200])
ax3.set_xticklabels([0.0, 0.5, 1.0, 1.5])
ax3.set_xlabel('t (min)')
ax3.set_ylabel('v (m/s)')


#plot 4
ax4 = plt.subplot2grid((4,2),(2, 1))
ax4.plot(
    t_engine_on,
    v_x_on,
    color = 'r',
    linestyle = 'dashed'
)
ax4.plot(
    t_engine_off+t_engine_on[-1],
    v_x_off,
    color = 'b',
    linestyle = 'dashed'
)
ax4.plot(
    t_slow_down+t_engine_off[-1]+t_engine_on[-1],
    v_x_sd,
    color = 'purple',
    linestyle = 'dashed'
)
#Scatter
ax4.scatter(
    t_engine_on[-1],
    v_x_on[-1],
    color = 'r',
    marker = '*'
)
ax4.scatter(
    t_engine_off[-1]+t_engine_on[-1],
    v_x_off[-1],
    color = 'b',
    marker = 's'
)
ax4.scatter(
    t_slow_down[-1]+t_engine_off[-1]+t_engine_on[-1],
    v_x_sd[-1],
    color = 'purple',
    marker = 'v'
)
tick = np.arange(0,60*2,30)
ax4.set_xticks(tick)
ax4.set_yticks([0,25])
ax4.set_xticklabels([0.0, 0.5, 1.0, 1.5])
ax4.set_xlabel('t (min)')
ax4.set_ylabel(f'$v_x$ (m/s)')


#plot 5
ax5 = plt.subplot2grid((4,2),(3, 1))
ax5.plot(
    t_engine_on,
    v_y_on,
    color = 'r',
    linestyle = 'dotted'
)
ax5.plot(
    t_engine_off+t_engine_on[-1],
    v_y_off,
    color = 'b',
    linestyle = 'dotted'
)
ax5.plot(
    t_slow_down+t_engine_off[-1]+t_engine_on[-1],
    v_y_sd,
    color = 'purple',
    linestyle = 'dotted'
)
#Scatter
ax5.scatter(
    t_engine_on[-1],
    v_y_on[-1],
    color = 'r',
    marker = '*'
)
ax5.scatter(
    t_engine_off[-1]+t_engine_on[-1],
    v_y_off[-1],
    color = 'b',
    marker = 's'
)
ax5.scatter(
    t_slow_down[-1]+t_engine_off[-1]+t_engine_on[-1],
    v_y_sd[-1],
    color = 'purple',
    marker = 'v'
)

tick = np.arange(0,60*2,30)
ax5.set_xticks(tick)
ax5.set_yticks([-250, 0])
ax5.set_xticklabels([0.0, 0.5, 1.0, 1.5])
ax5.set_xlabel('t (min)')
ax5.set_ylabel(f'$v_y$ (m/s)')


#xlim
ax1.set_xlim(left=0)
ax2.set_xlim(left=0)
ax3.set_xlim(left=0)
ax4.set_xlim(left=0)
ax5.set_xlim(left=0)
#ylim
ax2.set_ylim(bottom=-.5)
ax3.set_ylim(bottom=-.5)
#ground line
ax2.axhline(y=0,linewidth = 1, color = 'black')
ax3.axhline(y=0,linewidth = 1, color = 'black')
ax4.axhline(y=0,linewidth = 1, color = 'black')
ax5.axhline(y=0,linewidth = 1, color = 'black')
#yaxis
ax2.axvline(x=0,linewidth = 1, color = 'black')
ax3.axvline(x=0,linewidth = 1, color = 'black')
ax4.axvline(x=0,linewidth = 1, color = 'black')
ax5.axvline(x=0,linewidth = 1, color = 'black')
#remove box from right plots
ax2.set_frame_on(False)
ax3.set_frame_on(False)
ax4.set_frame_on(False)
ax5.set_frame_on(False)


plt.tight_layout()
plt.savefig("RobertoRamil_M1_p1.pdf")
plt.show()