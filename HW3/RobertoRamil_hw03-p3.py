import numpy as np
import matplotlib.pyplot as plt

x, y, z = np.loadtxt("HW3\hw03-data.txt", delimiter=' ', skiprows= 3, usecols={1, 2, 4}, unpack= True)

plt.figure("A")


plt.plot(x, y,
         linestyle = "-",
         label = "f(x)",
         color = 'green'
    
)
plt.plot(x, z,
         linestyle = "-",
         label = "f(z)",
         color = 'blue'
    
)
plt.plot(x, z/y,
         linestyle = "-",
         label = "f(z/y)",
         color = 'red',
)

plt.legend()
plt.title("Curves based on data.txt")
plt.savefig("RobertoRamil_hw03-p3_fig.pdf")
plt.show()