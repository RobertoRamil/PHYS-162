import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import beta

a, b = 1.7, 8.5
N1, N2 = 500, 50000

data_500 = np.random.beta(a,b,N1)
data_50k = np.random.beta(a,b,N2)

def beta_fit(x, d0, a, b):
    return d0 * (x**a) * ((1-x)**b)

def plot_Hist(data, num_bins, ax, title):
    counts, bin_edges = np.histogram(data, bins=num_bins, density=True)
    bins_centers = .5 * (bin_edges[1:] + bin_edges[:-1])
    
    popt, _ = curve_fit(beta_fit, bins_centers, counts, p0=[1, a, b])
    d0_fit, a_fit, b_fit = popt
    
    ax.hist(data, bins=num_bins, density=True, alpha= .5, color = 'gray', label = "Hist")
    ax.scatter(bins_centers, counts, color = 'b', marker = 'o', label = 'Midpoints')
    ax.plot(bins_centers, beta_fit(bins_centers, *popt), color = 'r', linestyle = 'dashed', label = f'Fit: $d_0$ = {d0_fit:.2f}, $a$ = {a_fit:.2f}, $b$ = {b_fit:.2f}')
    
    mean = np.mean(data)
    median = np.median(data)
    
    ax.axvline(mean, color = 'g', linestyle = '--', label = f'Mean: {mean:.2f}')
    ax.axvline(median, color = 'purple', linestyle = ':', label = f'Median: {median:.2f}')
    
    ax.set_title(title)
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    
fig, (ax1, ax2) = plt.subplots(1, 2)

plot_Hist(data_500, num_bins=30, ax=ax1, title='500 samples')

plot_Hist(data_50k, num_bins=30, ax=ax2, title='50k samples')

print("The more samples the better the curve histogram gets since it does even out eventually")

plt.tight_layout()
plt.savefig('RobertoRamil_hw07-p1.pdf')
plt.show()