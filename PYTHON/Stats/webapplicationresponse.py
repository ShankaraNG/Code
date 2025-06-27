# A data scientist is looking at how a web application responds, with an average response time of 250 milliseconds and a standard deviation of 30 milliseconds.

# Find the critical value for a 96% confidence level.

from scipy.stats import norm
import math


U = 250
sigma = 30
alpha = 0.04

z = norm.ppf(1-(0.04/2))
print("The Z stats value is ", z)

Xbar = (z*sigma) + U
print("The Critical value at which the stats will fail is ", Xbar)
