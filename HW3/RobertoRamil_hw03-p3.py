import numpy as np
import matplotlib.pyplot as plt

x, y, z = np.loadtxt("hw03-data.txt", delimiter=' ', skiprows= 3, usecols={1, 2, 4}, unpack= True)

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
sumx, sumy, sumz = sum(x), sum(y), sum(z)
avgx, avgy, avgz = sumx/len(x), sumy/len(y), sumz/len(z)

out1 = f"Sum of Array x is {sumx:.2f}, average = {avgx:.3f}\n"
out2 = f"Sum of Array y is {sumy:.2f}, average = {avgy:.3f}\n"
out3 = f"Sum of Array z is {sumz:.2f}, average = {avgz:.3f}\n"



with open("out-p3.txt", 'w') as file:
    file.write(out1)
    file.write(out2)
    file.write(out3)

plt.legend()
plt.title("Curves based on data.txt")
plt.savefig("RobertoRamil_hw03-p3_fig.pdf")
plt.show()