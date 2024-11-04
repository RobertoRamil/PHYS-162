import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


x, y = np.loadtxt('HW07-linearFit.dat', unpack=True)

def polynomial_model(x, *coeffs):
    result = 0
    for i, c in enumerate(coeffs):
        result += c*x **i
    return result

degrees = np.arange(11)

plt.figure()

plt.scatter(x, y, color = 'b', label = 'Data')

for i in degrees:
    initial_guess = np.ones(i+1)
    
    coeffs, _ = curve_fit(polynomial_model, x, y, p0=initial_guess)
    
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = polynomial_model(x_fit, *coeffs)
    
    plt.plot(x_fit, y_fit, label = f'Degrees {i}')


print("I found that around 10 lines or so is when it gets pretty good.")
print("If we go more it will get even better but it does get a bit much")
print("on how many lines there are.")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Pollynoial Fits')
plt.legend()
plt.savefig('RobertoRamil_HW07-p2.pdf')
plt.show()