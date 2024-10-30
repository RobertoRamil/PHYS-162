import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import norm

mu = 5
sigma = 1.25
sampleSize = 10000

data = np.random.normal(mu, sigma, sampleSize)

bin_counts, bin_edges, _ = plt.hist(
    data, bins = 30, density = True, alpha = .6, color = 'b'
)

bin_midpoints = (bin_edges[:-1]+bin_edges[1:])/2

def gaussian(x, d0, mu, sigma):
    return d0 * np.exp(-((x-mu)**2)/(2*sigma**2))

popt, pcov = curve_fit(gaussian, bin_midpoints,bin_counts, p0=[1, mu, sigma])

d0_fitted, mu_fitted, sigma_fitted = popt
x_vals = np.linspace(min(data), max(data), 1000)

plt.plot(
    x_vals,
    gaussian(x_vals, *popt),
    color = 'r',
    label = "Fitted Gaussian"
)
plt.plot(
    bin_midpoints,
    bin_counts,
    color = 'g',
    label = "Data Midpoints"
)

plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.title('Normally Distributed Numbers. Gaussian Fit')
plt.savefig('RobertoRamil_hw07-p1.pdf')
plt.show()