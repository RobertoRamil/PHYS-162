import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x):
    return x- 8*np.cos(x)

initial_guess = np.linspace(1,10,10)
solutions = []

for guess in initial_guess:
    sol = fsolve(f,guess)
    if sol[0] > 0 and sol [0] not in solutions:
        solutions.append(sol[0])
        
solutions = np.unique(solutions)[:5]   

print("Solutions for x = 8 cos(x): ", solutions)
plt.figure()
x_vals = np.linspace(1,10,400)
plt.plot(
    x_vals,
    f(x_vals),
    label = 'f(x) = x - 8 cos(x)'
)
plt.axhline(0, color = 'gray', linestyle = '--', lw = .7)
plt.scatter(solutions, f(solutions), color= 'red', zorder = 5)
plt.title('Solutions for x = 8 cos(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.savefig('RobertoRamil_hw06-p2-part-b.pdf')
plt.show()