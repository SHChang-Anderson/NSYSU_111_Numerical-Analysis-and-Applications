import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(42)


rand_nums = np.random.normal(loc=0, scale=1, size=20000)








x_vals = np.linspace(-4, 4, 1000)


y_vals = norm.pdf(x_vals, loc=0, scale=1)


plt.hist(rand_nums, bins=50, density=True, alpha=0.7, color='blue',edgecolor =  "black")
plt.plot(x_vals, y_vals, color='red')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('RNG')
plt.show()

