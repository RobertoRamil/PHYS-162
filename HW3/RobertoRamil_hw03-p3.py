import numpy as np

x, y, z = np.loadtxt("HW3\hw03-data.txt", delimiter=' ', skiprows= 3, usecols={1, 2, 4}, unpack= True)

print(x)