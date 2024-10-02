import numpy as np
import matplotlib.pyplot as plt

# Load data from text files
x1, y1 = np.loadtxt('hw05-data1.txt', delimiter= ' ', unpack= True)
x2, y2 = np.loadtxt('hw05-data2.txt', delimiter= ' ', unpack= True)
x3, y3 = np.loadtxt('hw05-data3.txt', delimiter= ' ', unpack= True)

plt.figure()
#Plot 1
ax1 = plt.subplot2grid((2,2),(0,0))
ax1.scatter(x1,y1,color = 'r', facecolors = 'none', marker ='v',label = 'data 1')
ax1.scatter(x2,y2,color = 'b', facecolors = 'none', marker ='s',label = 'data 2')
ax1.scatter(x3,y3,color = 'g', marker ='x',label = 'data 3')
ax1.set_xlim(-10, 10)
ax1.set_ylim(-30, 59)
ax1.set_title("subplot2grid((2,2),(0,0))")
ax1.legend()

#plot 2
ax2 = plt.subplot2grid((2,2),(1,0))

ax2.set_title("subplot 223, polar Coordinates")

#plot 3
x = np.arange(.01,np.pi,.001)
y = np.sin(1/x)

ax3 = plt.subplot2grid((2,2),(0,1))
ax3.plot(x,y, label = r'$sin(\dfrac{1}{x})$')
ax3.scatter([1/(3*np.pi),1/(2*np.pi), 1/(np.pi)],[0,0,0], color = 'b', marker='o')

ax3.set_xlim(1/(8*np.pi),2/np.pi)
ax3.set_title("Subplot2grid (2,2), (0,1)")
ax3.set_xticks([1/(3*np.pi),1/(2*np.pi),1/np.pi])
ax3.set_xticklabels([r'$\dfrac{1}{3\pi}$',r'$\dfrac{1}{2\pi}$',r'$\dfrac{1}{\pi}$'])
ax3.legend()

#plot 4
ax4 = plt.subplot2grid((2,2),(1,1))

ax4.set_title("Subplot 224")


plt.savefig('RobertoRamil_hw05-p2_fig1.pdf')
plt.show()