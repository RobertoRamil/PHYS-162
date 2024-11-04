import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def double_gaussian(x, A1, mu1, sigma1, A2, mu2,sigma2):
    gauss1 = A1*np.exp(-((x-mu1)**2)/(2*sigma1**2))
    gauss2 = A2*np.exp(-((x-mu2)**2)/(2*sigma2**2))
    return gauss1+gauss2

G = np.loadtxt('HW07-prob3-data.txt')

plt.subplot(2,2,1)
plt.scatter(
    np.arange(len(G)),
    G,
    marker = 'o',
    label = "G Values" 
)
plt.xlabel('Index')
plt.ylabel('Conductance (G)')
plt.title("Scatter Plot of G vs Index")
plt.legend()

bins = 30
counts, bin_edges = np.histogram(G, bins)
bin_centers = .5 * (bin_edges[1:] + bin_edges[:-1])
plt.subplot(1,2,2)
plt.bar(
    bin_centers,
    counts,
    width = bin_edges[1] - bin_edges[0],
    color = 'b',
    edgecolor = 'black'
)
for x, y in zip(bin_centers,counts):
    plt.scatter(
        x,
        y+.5,
        marker='o',
        s = 10
    )
plt.xlabel('Conductane (G)')
plt.ylabel('Frequencey')
plt.title("Histogram of G")

initial_guesses = [max(counts), bin_centers[np.argmax(counts)],1,
                   max(counts)/2, bin_centers[np.argmax(counts)]+1, 1]

params, covariance = curve_fit(double_gaussian, bin_centers,counts, p0=initial_guesses)

A1, mu1, sigma1, A2, mu2, sigma2 = params

plt.subplot(2,2,3)
plt.bar(
    bin_centers,
    counts,
    width=bin_edges[1] - bin_edges[0],
    label = 'data'
)
x_fit = np.linspace(min(bin_centers), max(bin_centers),1000)
y_fit = double_gaussian(x_fit, *params)
plt.plot(
    x_fit,
    y_fit,
    color = 'r',
    label = 'Double Gaussian Fit'
)





plt.tight_layout()
plt.savefig('RobertoRamil_HW07-p3.pdf')
plt.show()
