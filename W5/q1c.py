import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.special import comb

def posteriorDist():
    p = np.arange(0, 1, .1)

    dist1 = calcDist(1, 1, p)
    plt.plot(p, dist1, color='blue', marker='*')

    dist1 = calcDist(2, 2, p)
    plt.plot(p, dist1, color='red', marker='*')

    dist1 = calcDist(3, 2, p)
    plt.plot(p, dist1, color='yellow', marker='*')

    dist1 = calcDist(4, 3, p)
    plt.plot(p, dist1, color='green', marker='*')

    plt.gca().legend(('head = 1, trial = 1', 'head = 2, trial = 2', 'head = 2, trial = 3', 'head = 3, trial = 4'))
    plt.title('Problem 1 part c')
    plt.ylabel('Heads and Trials')
    plt.xlabel('Theta')
    plt.show()

def calcDist(trials, heads, p):
    return comb(trials, heads) * p**heads * (1-p)**(trials-heads) * (1 + trials);

posteriorDist()
