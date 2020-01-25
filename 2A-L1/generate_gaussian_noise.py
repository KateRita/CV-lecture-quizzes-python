import numpy as np
import matplotlib.pyplot as plt

# Generate Gaussian noise
# sigma = standard deviation
sigma = 1
noise = np.random.normal(0, sigma, 1000)
histogram_count, bin_edges, ignored = plt.hist(noise, 21, density=True)
plt.show()

# TODO: Try generating other kinds of random numbers.
#       How about a 2D grid of random Gaussian values?