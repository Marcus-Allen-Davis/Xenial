# Importing the Libraries
import numpy as np

# Setting conversion rates and the number of samples
conversion_rate = [0.15, 0.04, 0.13, 0.11, 0.05]
N = 100000
d = len(conversion_rate)
# Above are five slot machines the numbers represent the chance of a win
# The number of samples is 100000

# Creating the dataset
X = np.zeros((N, d))
for i in range(N):
    for j in range(d):
        if np.random.rand() < conversion_rate[j]:
            X[i][j] = 1
# First line above is a 2d-array of zeros with 100000 rows and 5 columns
# The second line above is a for loop that goes through each row and column
# If the random number is less than the conversion rate then the value is 1

# Making arrays to count our losses and wins
nPosReward = np.zeros(d)
nNegReward = np.zeros(d)

# Taking our best slot machine through beta distribution and updating its losses and wins
for i in range(N):
    selected = 0
    maxRandom = 0

for j in range(d):
    randomBeta = np.random.beta(nPosReward[j] + 1, nNegReward[j] +
1)
    if randomBeta > maxRandom:
        maxRandom = randomBeta
        selected = j

if X[i][selected] == 1:
    nPosReward[selected] += 1
else:
    nNegReward[selected] += 1

# Showing which slot machine is considered the best
nSelected = nPosReward + nNegReward
for i in range(d):
    print('Machine number ' + str(i + 1) + ' was selected ' +
str(nSelected[i]) + ' times')
print('Conclusion: Best machine is machine number ' + str(np.
argmax(nSelected) + 1))
# 2,000 samples in set x to achieve result
