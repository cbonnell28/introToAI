import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.special import comb

def likelihood():
    n = 4
    p = 0.75
    k = np.arange(0, 4.5, .5)
    values = (comb(n, k) * p**k * (1-p)**(n-k))
    plt.plot(k, values, color='blue', marker='*')
    plt.title('Q1 part b')
    plt.ylabel('n=4, theta=3/4')
    plt.xlabel('k')
    plt.show()

likelihood()
