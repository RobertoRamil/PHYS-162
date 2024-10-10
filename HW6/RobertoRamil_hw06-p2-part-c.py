import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def system(vars):
    x, y = vars
    eq1 = x**5 - y**3 + y**2 - np.sin(x)
    eq2 = y**5 - x**3 + 1
    return [eq1, eq2]

initial_guess = [(1,1),(2,2),(3,3),(4,4),(5,5)]
solutions = []

for guess in initial_guess:
    sol = fsolve(system, guess)
    if all(val > 0 for val in sol) and not any(np.allclose(sol, exsisting_sol) for exsisting_sol in solutions):
        solutions.append(sol)
        
solutions = np.unique(solutions, axis = 0)[:5]

print ("Solutions for the system of eqations: ", solutions)
plt.figure()
x_vals = np.linspace(0,5,100)
y_vals = np.linspace(0,5,100)
X,Y = np.meshgrid(x_vals,y_vals)

Z1 = X**5 - Y**3 + Y**2 - np.sin(X)
Z2 = Y**5 - X**3 + (.25*(np.cos(X)**2-.98))

plt.contour(
    X,
    Y,
    Z1,
    levels = [0],
    colors = 'blue',
    linewidths = 2,
    clabel = f'$x^5 -y^3+y^2=sin(x)$'
)
plt.contour(
    X,
    Y,
    Z2,
    levels = [0],
    colors = 'orange',
    linewidths = 2,
    clabel = f'$y^5 -x^3=-1/4(cos^2(x)-.98$'
)
plt.scatter(
    solutions[:,0],
    solutions[:,1], 
    color = 'r',
    zorder = 5
)
plt.title('Solutions for the system of equations')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('RobertoRamil_hw06-p2-part-c.pdf')
plt.show()