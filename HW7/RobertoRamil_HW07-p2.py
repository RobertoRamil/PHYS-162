import numpy as np
import matplotlib.pyplot as plt


x, y = np.loadtxt('HW07-linearFit.dat', unpack=True)

degrees = np.arange(11)

plt.figure()

plt.scatter(x, y, color = 'b', label = 'Data')

for i in degrees:
    coeffs = np.polyfit(x, y, i)
    poly = np.poly1d(coeffs)
    
    y_fit = poly(x)
    
    plt.plot(x, y_fit, label = f'Degrees {i}')


print("I found that around 10 lines or so is when it gets pretty good.")
print("If we go more it will get even better but it does get a bit much")
print("on how many lines there are.")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Pollynoial Fits')
plt.legend()
plt.savefig('RobertoRamil_HW07-p2.pdf')
plt.show()