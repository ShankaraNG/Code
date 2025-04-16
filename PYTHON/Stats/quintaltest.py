# Traditionally it is known that a green gram cultivation yields 12.0 quintals per hectare on an average.

# In order to increase crop yields, scientists have developed a new variety of green grams, that can supposedly produce more than the expected average yield of 12 quintals per hectare.

# To test the same, this variety of green grams was tested on 10 randomly selected farmer's fields.

# The yield (quintals/hectare) was recorded as: [14.3,12.6,13.7,10.9,13.7,12.0,11.4,12.0,12.6,13.1]

# With a 5% significance level, can we conclude that the average yield of this variety of green grams is more than the expected yield (12 quintals/hectare)?

# Perform an appropriate test and choose the correct option below :


import numpy as np
from scipy.stats import norm
import pandas as pd
from scipy.stats import ttest_1samp

a = [14.3,12.6,13.7,10.9,13.7,12.0,11.4,12.0,12.6,13.1]
mean = np.mean(a)
sd = np.std(a)
xbar = 12
t = (mean-xbar)/(sd/np.sqrt(len(a)))
print(f't={t}')
pvalue = 1 - norm.cdf(t)
print(f'pvalue={pvalue}')
alpha = 0.05

if(pvalue < 0.05):
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")

tvalue , pvalue = ttest_1samp(a, xbar, alternative='greater')
print(f'tvalue={tvalue}')
print(f'pvalue={pvalue}')

alpha = 0.05
if(pvalue < 0.05):
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")
