import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.special import comb

# Returns a bag of the appropriate type given the bag ID
def fillBag(bagID):
    bag = []
    if(bagID == 1):
        bag.extend(['cherry'] * 100)
    if(bagID == 2):
        bag.extend(['cherry'] * 75)
        bag.extend(['lime'] * 25)
    if(bagID == 3):
        bag.extend(['cherry'] * 50)
        bag.extend(['lime'] * 50)
    if(bagID == 4):
        bag.extend(['cherry'] * 25)
        bag.extend(['lime'] * 75)
    if(bagID == 5):
        bag.extend(['lime'] * 100)
    return bag

def likelihood(bagActual, bagGuess):
    product = 1
    for candy in bagActual:
    	candyChance = posteriorWithEvidence(candy, bagGuess)
	product = product * candyChance
    return product
def posteriorWithEvidence(candy, bagGuess):
    if(bagGuess == 1):
        return 0 if candy == 'lime' else 1
    elif(bagGuess == 2):
        return 0.25 if candy == 'lime' else 0.75
    elif(bagGuess == 3):
        return 0.50
    elif(bagGuess == 4):
        return 0.75 if candy == 'lime' else 0.25
    else:
        return 1 if candy == 'lime' else 0
    
def posterior(bagActual, bagGuess):
    bagGuessProb = [0.1, 0.2, 0.4, 0.2, 0.1]

    toReturn = []

    for candy in range(0, len(bagActual)):
        temp_list = bagActual[0:candy]
        likeliness = likelihood(temp_list, bagGuess)
        toReturn.append(likeliness * bagGuessProb[bagGuess - 1])

    return toReturn

def plotGeneral(): 

	candyBag1 = fillBag(1)
	candyBag2 = fillBag(2)
	candyBag3 = fillBag(3)
	candyBag4 = fillBag(4)
	candyBag5 = fillBag(5)

	guess = 1
	while (guess != 6):
		d1 = posterior(candyBag1, guess)
		d2 = posterior(candyBag2, guess)
		d3 = posterior(candyBag3, guess)
		d4 = posterior(candyBag4, guess)
		d5 = posterior(candyBag5, guess)

		f_list = []

		for i in range(0, len(d1)): #average it all together 
			sum = d1[i] + d2[i] + d3[i] + d4[i] + d5[i]
			f_list.append( sum/5 )

		x = range(0, len(candyBag1), 1)
		plt.plot(x, f_list)
		guess = guess + 1

	plt.gca().legend(('bag1','bag2', 'bag3', 'bag4', 'bag5'))
	plt.show()

plotGeneral()

# print(fillBag(1))
# print(fillBag(2))
# print(fillBag(3))
# print(fillBag(4))
# print(fillBag(5))
