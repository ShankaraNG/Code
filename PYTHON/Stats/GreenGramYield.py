# Traditionally it is known that a green gram cultivation yields 12.0 quintals per hectare on an average.

# In order to increase crop yields, scientists have developed a new variety of green grams, that can supposedly produce more than the expected average yield of 12 quintals per hectare.

# To test the same, this variety of green grams was tested on 10 randomly selected farmer's fields.

# The yield (quintals/hectare) was recorded as: [14.3,12.6,13.7,10.9,13.7,12.0,11.4,12.0,12.6,13.1]

# With a 5% significance level, can we conclude that the average yield of this variety of green grams is more than the expected yield (12 quintals/hectare)?

# Perform an appropriate test and choose the correct option below :

import numpy as np
from statsmodels.stats.weightstats import _tstat_generic
import math
from scipy.stats import norm
import sys

ybar = 12
y = [14.3,12.6,13.7,10.9,13.7,12.0,11.4,12.0,12.6,13.1]
n = 10
alpha = 0.05
Ho = "The given average yield of this variety of Green Grams is Equal to 12 quintals/hectare"
Ha = "The given average yield is more than the expected Yield of 12 Quintal/hectar"
tail = "larger"


def method1(y,ybar,n,alpha,ho,ha,tail):
    y = np.array(y)
    ymean = np.mean(y)
    ystd = np.std(y, ddof=1)
    tstats = (ymean-ybar)/(ystd/math.sqrt(n))
    print("The T Statistics is ", tstats)
    if(tail.upper()== "LARGER"):
        pvalue = 1-norm.cdf(tstats)
    elif(tail.upper()== "SMALLER"):
        pvalue = norm.cdf(tstats)
    elif(tail.upper() == "TWOSIDED"):
        pvalue = 2*(1-norm.cdf(tstats))
    else:
        print("Wrong Input for the Tail test")
        sys.exit(1)
    
    print("The pvalue for the Tstats is ", pvalue)
    if(pvalue<alpha):
        print("Rejecting Null Hypothesis")
        print(ha)
    else:
        print("Failed to Reject Null Hypothesis")
        print(ho)

def method2(y,ybar,n,alpha,ho,ha,tail):
    y = np.array(y)
    ymean = np.mean(y)
    ystd = np.std(y, ddof=1)
    se = ystd/math.sqrt(n)
    dof = n-1
    
    if(tail.upper()== "LARGER"):
        tstats, pvalue = _tstat_generic(ymean,ybar,se, dof=dof, alternative="larger")
    elif(tail.upper()== "SMALLER"):
        tstats, pvalue = _tstat_generic(ymean,ybar,se, dof=dof, alternative="smaller")
    elif(tail.upper() == "TWOSIDED"):
        tstats, pvalue = _tstat_generic(ymean,ybar,se, dof=dof, alternative="two-sided")
    else:
        print("Wrong Input for the Tail test")
        sys.exit(1)
        
    print("The T Statistics is ", tstats)    
    print("The pvalue for the Tstats is ", pvalue)
    if(pvalue<alpha):
        print("Rejecting Null Hypothesis")
        print(ha)
    else:
        print("Failed to Reject Null Hypothesis")
        print(ho)


method1(y,ybar,n,alpha,Ho,Ha,tail)
method2(y,ybar,n,alpha,Ho,Ha,tail)
